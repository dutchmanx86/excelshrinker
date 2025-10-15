"""Format detection engine for Excel spreadsheets"""

import sys
import time
from typing import Optional, Tuple, List
from pathlib import Path
from datetime import datetime, date

from boundary_detector.models.detection_config import DetectionConfig
from boundary_detector.models.boundary_result import BoundaryResult
from boundary_detector.exceptions.errors import FileLoadError, SheetNotFoundError, DetectionError
from boundary_detector.utils.excel_utils import is_cell_empty, column_index_to_letter
from boundary_detector.core.boundary_detector import BoundaryDetector
from compression.format_detector.format_result import FormatResult
from compression.format_detector.format_range import FormatRange
from compression.format_detector.format_mappings import classify_format, get_format_scale
from compression.format_detector.time_period_parser import TimePeriodParser
from compression.format_detector.time_range_detector import TimeRangeDetector
from compression.format_detector.date_series_analyzer import DateSeriesAnalyzer


class FormatDetector:
    """
    High-performance Excel number format detector.
    
    Uses a hybrid approach:
    1. Calamine for fast cell value scanning
    2. Openpyxl for accurate number format code extraction
    """
    
    def __init__(self, config: Optional[DetectionConfig] = None):
        """
        Initialize the format detector.

        Args:
            config: Detection configuration. Uses defaults if not provided.
        """
        self.config = config or DetectionConfig()
        self.time_parser = TimePeriodParser()
        self.time_range_detector = TimeRangeDetector()
    
    def detect(
        self,
        file_path: str,
        sheet_name: Optional[str] = None,
        boundary_result: Optional[BoundaryResult] = None,
        verbose: bool = False
    ) -> FormatResult:
        """
        Detect number formats in an Excel worksheet.
        
        Args:
            file_path: Path to the Excel file
            sheet_name: Name of the sheet to analyze. If None, uses first sheet.
            boundary_result: Optional pre-computed boundary result for efficiency
            verbose: If True, prints progress messages to stderr.
        
        Returns:
            FormatResult with detected format ranges
        
        Raises:
            FileLoadError: If file cannot be loaded
            SheetNotFoundError: If specified sheet is not found
            DetectionError: If detection process fails
        """
        start_time = time.time()
        
        # Validate file exists
        file_path_obj = Path(file_path)
        if not file_path_obj.exists():
            raise FileLoadError(file_path, f"File not found: {file_path}")
        
        try:
            # Determine sheet name
            if sheet_name is None:
                sheet_name = self._get_first_sheet_name(file_path)
            
            # Get boundaries (either from parameter or detect using proper boundary detector)
            if boundary_result:
                max_col = boundary_result.max_column
                max_row = boundary_result.max_row
            else:
                # Use the proper BoundaryDetector which handles sparse data correctly
                boundary_detector = BoundaryDetector(self.config)
                boundary_result = boundary_detector.detect(file_path, sheet_name)
                max_col = boundary_result.max_column
                max_row = boundary_result.max_row
            
            # Scan formats using hybrid approach
            format_ranges, cells_analyzed, sheet_data, start_row, start_col = self._scan_formats_hybrid(
                file_path, sheet_name, max_col, max_row, verbose=verbose
            )

            # Detect and consolidate vertical (columnar) date series
            columnar_ranges, consolidated_cells = self._detect_columnar_date_series(
                format_ranges, max_row
            )

            # Detect and consolidate horizontal time series, excluding cells from columnar ranges
            time_series_ranges, time_series_cells = self._detect_and_consolidate_time_series(
                sheet_data, format_ranges, max_col, max_row, start_row, start_col, exclude_cells=consolidated_cells
            )
            
            # Combine all non-date, non-time-series ranges with the new consolidated ranges
            final_ranges = []
            
            # Add all non-date ranges first
            for fmt_range in format_ranges:
                if fmt_range.type != 'date':
                    final_ranges.append(fmt_range)

            # Add the consolidated ranges
            final_ranges.extend(columnar_ranges)
            final_ranges.extend(time_series_ranges)

            # Remove any single date cells that are now part of a consolidated range
            format_ranges = []
            all_consolidated_cells = consolidated_cells.union(time_series_cells)
            for fmt_range in final_ranges:
                if ':' in fmt_range.range or fmt_range.range not in all_consolidated_cells:
                    format_ranges.append(fmt_range)
            
            # Sort final ranges by row position
            format_ranges.sort(key=lambda r: self._get_row_from_range(r.range))

            # Merge consecutive rows with identical column spans into rectangular regions
            format_ranges = self._merge_rectangular_regions(format_ranges)

            # Calculate processing time
            processing_time = (time.time() - start_time) * 1000  # Convert to ms
            
            # Create and return result
            result = FormatResult(
                sheet_name=sheet_name,
                format_ranges=format_ranges,
                processing_time_ms=processing_time,
                cells_analyzed=cells_analyzed
            )
            
            return result
            
        except FileLoadError:
            raise
        except SheetNotFoundError:
            raise
        except Exception as e:
            raise DetectionError(f"Error during format detection: {str(e)}") from e

    def _scan_formats_hybrid(
        self,
        file_path: str,
        sheet_name: str,
        max_col: int,
        max_row: int,
        verbose: bool = False
    ) -> Tuple[List[FormatRange], int, List[List], int, int]:
        """
        Scan formats using hybrid approach:
        1. Calamine for cell values (fast)
        2. Openpyxl for format codes (accurate, using iter_rows for speed)
        3. Group adjacent cells with same format

        Args:
            file_path: Path to Excel file
            sheet_name: Sheet name
            max_col: Maximum column to scan
            max_row: Maximum row to scan

        Returns:
            Tuple of (list of FormatRange objects, cells_analyzed count, sheet data, start_row, start_col)
        """
        try:
            from python_calamine import CalamineWorkbook
            import openpyxl
        except ImportError as e:
            raise DetectionError(
                f"Required library not installed: {str(e)}. "
                "Install with: pip install python-calamine openpyxl"
            )

        # Load with calamine for calculated values (fast - handles formulas)
        if verbose:
            print("Loading workbook with calamine...", file=sys.stderr)
        workbook_cal = CalamineWorkbook.from_path(file_path)
        sheet_cal = workbook_cal.get_sheet_by_name(sheet_name)
        data = sheet_cal.to_python()

        # Get the offset from calamine - this tells us which Excel row/col data[0][0] corresponds to
        start_row, start_col = sheet_cal.start  # 0-indexed: (4, 1) means Excel row 5, column B
        if verbose:
            print(f"Calamine data starts at Excel row {start_row + 1}, column {start_col + 1}", file=sys.stderr)

        # Load with openpyxl for formats only - OPTIMIZED: use iter_rows
        if verbose:
            print("Loading formats with openpyxl (using iter_rows for speed)...", file=sys.stderr)
        workbook_xl = openpyxl.load_workbook(file_path, data_only=False, read_only=True)
        sheet_xl = workbook_xl[sheet_name]

        # PRE-LOAD all formats in one pass using iter_rows (MUCH faster than cell-by-cell)
        # Build cache for the ACTUAL range where calamine has data
        if verbose:
            print(f"Pre-loading format cache for {max_row + 1} rows x {max_col + 1} columns...", file=sys.stderr)
            print(f"  Fetching formats from Excel rows {start_row + 1} to {start_row + max_row + 1}", file=sys.stderr)
        format_cache = {}  # (row_idx, col_idx) -> (number_format, format_id)

        # Use iter_rows starting from where calamine's data actually begins
        for row_idx, row_cells in enumerate(sheet_xl.iter_rows(
            min_row=start_row + 1,  # Excel rows are 1-indexed
            max_row=start_row + max_row + 1,
            min_col=start_col + 1,
            max_col=start_col + max_col + 1
        )):
            for col_idx, cell_xl in enumerate(row_cells):
                number_format = cell_xl.number_format or 'General'
                format_id = cell_xl._style if hasattr(cell_xl, '_style') else 0
                # Cache key matches calamine data indices (0-indexed from start of data)
                format_cache[(row_idx, col_idx)] = (number_format, format_id)

        if verbose:
            print(f"Format cache loaded: {len(format_cache)} cells", file=sys.stderr)

        format_ranges = []
        cells_analyzed = 0

        # Progress tracking
        last_progress = 0

        if verbose:
            print("Scanning cells and grouping formats...", file=sys.stderr)
        # Scan row by row (top to bottom)
        for row_idx in range(max_row + 1):
            # Progress indicator every 10%
            if verbose and row_idx > 0 and (max_row + 1) > 100 and row_idx % ((max_row + 1) // 10) == 0:
                progress = (row_idx / (max_row + 1)) * 100
                if progress - last_progress >= 10:
                    print(f"Progress: {progress:.0f}% (row {row_idx}/{max_row + 1})", file=sys.stderr)
                    last_progress = progress

            current_range = None

            # Get row data from calamine (calculated values)
            row_data = data[row_idx] if row_idx < len(data) else []

            # Only scan up to max_col (not the full 16384 columns that calamine returns)
            scan_limit = min(max_col + 1, len(row_data))

            for col_idx in range(scan_limit):
                # Get cell value from calamine (handles formulas automatically)
                cell_value = row_data[col_idx] if col_idx < len(row_data) else None

                # Skip empty cells (don't even count them or access format cache)
                if is_cell_empty(cell_value):
                    # Save any current range
                    if current_range:
                        format_ranges.append(current_range)
                        current_range = None
                    continue

                # Only count and lookup format for non-empty cells
                cells_analyzed += 1

                # Get format from cache (instant lookup)
                number_format, format_id = format_cache.get((row_idx, col_idx), ('General', 0))

                # Check value type and handle accordingly
                is_string_value = isinstance(cell_value, str)
                is_datetime_value = isinstance(cell_value, (datetime, date))

                if is_datetime_value:
                    # Cell contains a datetime object (from formula or direct date)
                    # Convert to ISO date string
                    if isinstance(cell_value, datetime):
                        parsed_date = cell_value.date().isoformat()
                    else:
                        parsed_date = cell_value.isoformat()

                    # Create single-cell range for datetime
                    # Convert calamine indices to Excel coordinates
                    excel_row = start_row + row_idx + 1  # Convert to 1-indexed Excel row
                    excel_col_letter = column_index_to_letter(start_col + col_idx)
                    cell_ref = f"{excel_col_letter}{excel_row}"
                    format_range = FormatRange(
                        range=cell_ref,
                        type='date',
                        parsed_date=parsed_date,
                        format_code=number_format
                    )
                    format_ranges.append(format_range)

                    # Dates don't continue ranges
                    if current_range:
                        format_ranges.append(current_range)
                        current_range = None

                elif is_string_value:
                    # Check if it's a time period string
                    if self.time_parser.is_time_period(cell_value):
                        parsed_date = self.time_parser.parse_to_date(cell_value)

                        # Create single-cell range for parsed time period
                        # Convert calamine indices to Excel coordinates
                        excel_row = start_row + row_idx + 1
                        excel_col_letter = column_index_to_letter(start_col + col_idx)
                        cell_ref = f"{excel_col_letter}{excel_row}"
                        format_range = FormatRange(
                            range=cell_ref,
                            type='date',
                            original_value=cell_value,
                            parsed_date=parsed_date,
                            format_code=number_format
                        )
                        format_ranges.append(format_range)
                    else:
                        # Regular string - create single-cell range
                        # Convert calamine indices to Excel coordinates
                        excel_row = start_row + row_idx + 1
                        excel_col_letter = column_index_to_letter(start_col + col_idx)
                        cell_ref = f"{excel_col_letter}{excel_row}"
                        format_range = FormatRange(
                            range=cell_ref,
                            type='string',
                            value=cell_value,
                            format_code=number_format
                        )
                        format_ranges.append(format_range)

                    # Strings don't continue ranges
                    if current_range:
                        format_ranges.append(current_range)
                        current_range = None

                else:
                    # Non-string value - classify format
                    format_type = classify_format(number_format, format_id)
                    scale = get_format_scale(number_format)

                    # Group adjacent cells with same format
                    # Convert calamine indices to Excel coordinates
                    excel_row = start_row + row_idx + 1
                    excel_col_letter = column_index_to_letter(start_col + col_idx)
                    cell_ref = f"{excel_col_letter}{excel_row}"

                    if current_range is None:
                        # Start new range
                        current_range = self._create_range(
                            cell_ref, cell_ref, format_type, number_format, format_id, scale
                        )
                    elif (current_range.type == format_type and
                          current_range.format_code == number_format):
                        # Extend current range
                        current_range = self._create_range(
                            current_range.start_cell, cell_ref, format_type,
                            number_format, format_id, scale
                        )
                    else:
                        # Different format - save current and start new
                        format_ranges.append(current_range)
                        current_range = self._create_range(
                            cell_ref, cell_ref, format_type, number_format, format_id, scale
                        )

            # End of row - save any open range
            if current_range:
                format_ranges.append(current_range)
                current_range = None

        workbook_xl.close()

        return format_ranges, cells_analyzed, data, start_row, start_col

    def _detect_and_consolidate_time_series(
        self,
        data: List[List],
        format_ranges: List[FormatRange],
        max_col: int,
        max_row: int,
        start_row: int,
        start_col: int,
        exclude_cells: set = None
    ) -> Tuple[List[FormatRange], set]:
        """
        Detect horizontal time series patterns, excluding specified cells.

        Args:
            data: Sheet data from calamine.
            format_ranges: List of format ranges.
            max_col: Maximum column index.
            max_row: Maximum row index.
            start_row: Starting row offset from calamine (0-indexed).
            start_col: Starting column offset from calamine (0-indexed).
            exclude_cells: A set of cell references (e.g., "A1") to exclude.

        Returns:
            A tuple of (new time series ranges, set of cells in these series).
        """
        if exclude_cells is None:
            exclude_cells = set()

        time_series_cells = set()
        new_time_series_ranges = []

        for row_idx in range(max_row + 1):
            row_data = data[row_idx] if row_idx < len(data) else []
            series_list = self.time_range_detector.detect_row_series(
                row_data, row_number=row_idx, start_col=0
            )

            for series_info in series_list:
                series_is_valid = True
                current_series_cells = set()

                # Check if any cell in the potential series is already excluded
                # Convert calamine indices to Excel coordinates
                for col_idx in range(series_info.start_col, series_info.end_col + 1):
                    excel_row = start_row + row_idx + 1
                    excel_col_letter = column_index_to_letter(start_col + col_idx)
                    cell_ref = f"{excel_col_letter}{excel_row}"
                    if cell_ref in exclude_cells:
                        series_is_valid = False
                        break
                    current_series_cells.add(cell_ref)

                if not series_is_valid:
                    continue

                # Create and add the new range - convert calamine indices to Excel coordinates
                start_excel_row = start_row + row_idx + 1
                start_excel_col_letter = column_index_to_letter(start_col + series_info.start_col)
                end_excel_col_letter = column_index_to_letter(start_col + series_info.end_col)
                start_cell = f"{start_excel_col_letter}{start_excel_row}"
                end_cell = f"{end_excel_col_letter}{start_excel_row}"
                
                time_series_range = FormatRange(
                    range=f"{start_cell}:{end_cell}",
                    type='date',
                    date_series_info={
                        'series_type': series_info.series_type,
                        'increment': series_info.increment,
                        'start_date': series_info.start_date,
                        'pattern': series_info.pattern
                    }
                )
                new_time_series_ranges.append(time_series_range)
                time_series_cells.update(current_series_cells)

        return new_time_series_ranges, time_series_cells

    def _detect_columnar_date_series(
        self,
        format_ranges: List[FormatRange],
        max_row: int
    ) -> Tuple[List[FormatRange], set]:
        """
        Detect vertical (columnar) date series and create consolidated ranges.

        Args:
            format_ranges: The list of format ranges from the initial scan.
            max_row: The maximum row number in the sheet.

        Returns:
            A tuple containing:
            - A list of new FormatRange objects for columnar date series.
            - A set of cell references (e.g., "C2") that are now part of a columnar series.
        """
        date_cells_by_column = {}
        
        # Step 1: Group all date cells by column
        for fmt_range in format_ranges:
            if fmt_range.type == 'date' and ':' not in fmt_range.range:
                col_idx = self._cell_to_col_index(fmt_range.range)
                row_idx = self._cell_to_row_index(fmt_range.range)
                
                if col_idx not in date_cells_by_column:
                    date_cells_by_column[col_idx] = []
                
                date_cells_by_column[col_idx].append({
                    "row": row_idx,
                    "date": fmt_range.parsed_date,
                    "cell_ref": fmt_range.range
                })

        new_columnar_ranges = []
        consolidated_cells = set()
        
        # Step 2: Analyze each column for unordered date series
        for col_idx, cells in date_cells_by_column.items():
            if len(cells) < self.config.min_columnar_dates:
                continue
                
            cells.sort(key=lambda x: x['row'])
            dates = [cell['date'] for cell in cells if cell['date']]

            if not dates:
                continue
            
            series_info = DateSeriesAnalyzer.analyze_date_range(dates)
            
            # Step 3: Create a new FormatRange if an unordered series is detected
            if series_info and series_info.get('interval_type') == 'unordered':
                min_row = cells[0]['row']
                max_row = cells[-1]['row']
                
                col_letter = column_index_to_letter(col_idx)
                start_cell = f"{col_letter}{min_row + 1}"
                end_cell = f"{col_letter}{max_row + 1}"
                
                column_range = FormatRange(
                    range=f"{start_cell}:{end_cell}",
                    type='date',
                    date_series_info={
                        'series_type': 'unordered_column',
                        'count': series_info.get('count'),
                        'start_date': series_info.get('first_date'),
                        'end_date': series_info.get('last_date')
                    }
                )
                new_columnar_ranges.append(column_range)
                
                # Step 4: Track all cells that are now part of this new range
                for cell in cells:
                    consolidated_cells.add(cell['cell_ref'])
                    
        return new_columnar_ranges, consolidated_cells

    def _cell_to_col_index(self, cell_ref: str) -> int:
        """Convert cell reference to 0-indexed column number (e.g., 'A1' -> 0, 'B1' -> 1)"""
        import re
        match = re.match(r'^([A-Z]+)(\d+)$', cell_ref)
        if not match:
            return -1

        col_letters = match.group(1)
        col_idx = 0
        for char in col_letters:
            col_idx = col_idx * 26 + (ord(char) - ord('A') + 1)
        return col_idx - 1

    def _cell_to_row_index(self, cell_ref: str) -> int:
        """Convert cell reference to 0-indexed row number (e.g., 'A1' -> 0, 'A2' -> 1)"""
        import re
        match = re.match(r'^([A-Z]+)(\d+)$', cell_ref)
        if not match:
            return -1

        return int(match.group(2)) - 1

    def _get_row_from_range(self, range_str: str) -> int:
        """
        Extract row number from a range string for sorting.

        Args:
            range_str: Cell range like "A1", "A1:C1", or "AF2:DW2"

        Returns:
            Row number (1-indexed) from the start of the range
        """
        import re
        # Handle both single cells and ranges - just get the first cell
        first_cell = range_str.split(':')[0]

        # Extract row number (e.g., "AF2" -> 2)
        match = re.match(r'^([A-Z]+)(\d+)$', first_cell)
        if match:
            return int(match.group(2))

        # If parsing fails, return a large number to put it at the end
        return 999999

    def _create_range(
        self,
        start_cell: str,
        end_cell: str,
        format_type: str,
        number_format: str,
        format_id: int,
        scale: Optional[int]
    ) -> FormatRange:
        """
        Create a FormatRange object.
        
        Args:
            start_cell: Starting cell (e.g., "A1")
            end_cell: Ending cell (e.g., "C1")
            format_type: Format type classification
            number_format: Excel number format string
            format_id: Excel format ID
            scale: Optional scaling factor
        
        Returns:
            FormatRange object
        """
        if start_cell == end_cell:
            range_str = start_cell
        else:
            range_str = f"{start_cell}:{end_cell}"
        
        return FormatRange(
            range=range_str,
            type=format_type,
            format_code=number_format,
            format_id=format_id,
            scale=scale
        )
    
    def _merge_rectangular_regions(self, format_ranges: List[FormatRange]) -> List[FormatRange]:
        """
        Merge consecutive rows with identical column spans and format attributes
        into rectangular 2D regions.

        Args:
            format_ranges: Sorted list of format ranges

        Returns:
            New list with rectangular regions merged
        """
        if not format_ranges:
            return format_ranges

        merged_ranges = []
        i = 0

        while i < len(format_ranges):
            current = format_ranges[i]

            # Skip single cells and date series (don't merge these)
            if ':' not in current.range or current.type == 'date' or current.type == 'string':
                merged_ranges.append(current)
                i += 1
                continue

            # Try to find consecutive rows with matching attributes
            group = [current]
            j = i + 1

            while j < len(format_ranges):
                candidate = format_ranges[j]

                # Check if candidate can be merged with the group
                if self._can_merge_into_rectangle(group[0], candidate):
                    group.append(candidate)
                    j += 1
                else:
                    break

            # If we found multiple rows to merge, create a rectangular region
            if len(group) > 1:
                merged_range = self._create_rectangular_range(group)
                merged_ranges.append(merged_range)
            else:
                merged_ranges.append(current)

            i = j

        return merged_ranges

    def _can_merge_into_rectangle(self, base_range: FormatRange, candidate: FormatRange) -> bool:
        """
        Check if a candidate range can be merged with a base range into a rectangle.

        Requirements:
        - Same format type
        - Same format attributes (scale, format_code)
        - Consecutive row numbers
        - Identical column span
        - Not a date or string type
        """
        # Must both be ranges (not single cells)
        if ':' not in candidate.range:
            return False

        # Skip dates and strings
        if candidate.type in ('date', 'string'):
            return False

        # Must have same type and format attributes
        if (base_range.type != candidate.type or
            base_range.format_code != candidate.format_code or
            base_range.scale != candidate.scale):
            return False

        # Parse ranges
        base_start, base_end = base_range.range.split(':')
        cand_start, cand_end = candidate.range.split(':')

        # Extract columns and rows
        base_start_col, base_start_row = self._parse_cell_ref(base_start)
        base_end_col, base_end_row = self._parse_cell_ref(base_end)
        cand_start_col, cand_start_row = self._parse_cell_ref(cand_start)
        cand_end_col, cand_end_row = self._parse_cell_ref(cand_end)

        # Must have identical column spans
        if (base_start_col != cand_start_col or base_end_col != cand_end_col):
            return False

        # Must be consecutive rows (candidate should be next row after base)
        if cand_start_row != base_end_row + 1:
            return False

        return True

    def _create_rectangular_range(self, group: List[FormatRange]) -> FormatRange:
        """
        Create a single FormatRange representing a rectangular region from a group
        of consecutive row ranges.
        """
        first = group[0]
        last = group[-1]

        # Parse first and last ranges
        first_start, _ = first.range.split(':')
        _, last_end = last.range.split(':')

        # Create new rectangular range
        return FormatRange(
            range=f"{first_start}:{last_end}",
            type=first.type,
            format_code=first.format_code,
            format_id=first.format_id,
            scale=first.scale
        )

    def _parse_cell_ref(self, cell_ref: str) -> Tuple[str, int]:
        """
        Parse a cell reference into column letter(s) and row number.

        Args:
            cell_ref: Cell reference like "E8" or "AB10"

        Returns:
            Tuple of (column_letters, row_number)
        """
        import re
        match = re.match(r'^([A-Z]+)(\d+)$', cell_ref)
        if not match:
            return ("", 0)
        return (match.group(1), int(match.group(2)))

    def _get_first_sheet_name(self, file_path: str) -> str:
        """Get the name of the first sheet in the workbook"""
        try:
            from python_calamine import CalamineWorkbook
            workbook = CalamineWorkbook.from_path(file_path)
            sheet_names = workbook.sheet_names
            return sheet_names[0] if sheet_names else "Sheet1"
        except Exception:
            return "Sheet1"  # Fallback