"""Main boundary detection logic using calamine for fast cell scanning"""

import time
from typing import Tuple, Optional
from pathlib import Path

from ..models.detection_config import DetectionConfig
from ..models.boundary_result import BoundaryResult
from ..exceptions.errors import FileLoadError, SheetNotFoundError, DetectionError
from ..utils.excel_utils import is_cell_empty
from .chart_detector import ChartDetector


class BoundaryDetector:
    """
    High-performance Excel boundary detector using calamine.
    
    This class uses python-calamine (Rust-based) for ultra-fast cell scanning
    and delegates chart detection to openpyxl.
    """
    
    def __init__(self, config: Optional[DetectionConfig] = None):
        """
        Initialize the boundary detector.
        
        Args:
            config: Detection configuration. Uses defaults if not provided.
        """
        self.config = config or DetectionConfig()
    
    def detect(self, file_path: str, sheet_name: Optional[str] = None, detect_charts: bool = True) -> BoundaryResult:
        """
        Detect boundaries in an Excel worksheet.

        Args:
            file_path: Path to the Excel file
            sheet_name: Name of the sheet to analyze. If None, uses first sheet.
            detect_charts: Whether to detect charts (default: True). Set to False for faster performance.

        Returns:
            BoundaryResult with detected boundaries and charts

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
            # Step 1: Fast boundary scanning with calamine
            boundaries, stats = self._scan_boundaries_calamine(file_path, sheet_name)
            max_col, max_row = boundaries

            # Step 2: Chart detection with openpyxl (optional)
            if detect_charts:
                charts = ChartDetector.detect_charts(file_path, sheet_name)

                # Step 3: Check chart overlaps with data
                for chart in charts:
                    chart.overlaps_data = ChartDetector.check_overlap(
                        chart, max_col, max_row
                    )
            else:
                charts = []
            
            # Calculate processing time
            processing_time = (time.time() - start_time) * 1000  # Convert to ms
            
            # Determine actual sheet name if not provided
            if sheet_name is None:
                sheet_name = self._get_first_sheet_name(file_path)
            
            return BoundaryResult(
                max_column=max_col,
                max_row=max_row,
                total_columns=max_col + 1,
                total_rows=max_row + 1,
                charts=charts,
                sheet_name=sheet_name,
                processing_time_ms=processing_time,
                cells_scanned=stats['cells_scanned'],
                non_empty_cells=stats['non_empty_cells'],
                calamine_time_ms=stats.get('calamine_time_ms', 0.0),
                buffer_time_ms=stats.get('buffer_time_ms', 0.0)
            )
            
        except FileLoadError:
            raise
        except SheetNotFoundError:
            raise
        except Exception as e:
            raise DetectionError(f"Error during boundary detection: {str(e)}") from e
    
    def _scan_boundaries_calamine(
        self,
        file_path: str,
        sheet_name: Optional[str]
    ) -> Tuple[Tuple[int, int], dict]:
        """
        Hybrid boundary scan: Calamine for speed + openpyxl buffer for accuracy.

        Phase 1: Fast scan with Calamine
        Phase 2: Check buffer zone beyond Calamine with openpyxl

        Args:
            file_path: Path to Excel file
            sheet_name: Sheet name or None for first sheet

        Returns:
            Tuple of ((max_col, max_row), statistics_dict)
        """
        try:
            from python_calamine import CalamineWorkbook
            import openpyxl
        except ImportError as e:
            raise DetectionError(f"Required library not installed: {str(e)}")

        try:
            # === PHASE 1: CALAMINE SCAN ===
            calamine_start = time.time()

            # Load workbook with Calamine
            workbook = CalamineWorkbook.from_path(file_path)

            if sheet_name:
                try:
                    sheet = workbook.get_sheet_by_name(sheet_name)
                except Exception:
                    available = workbook.sheet_names
                    raise SheetNotFoundError(sheet_name, available)
            else:
                sheet = workbook.get_sheet_by_index(0)

            # Get all data from Calamine (fast)
            data = sheet.to_python()

            # Initialize tracking
            max_col_with_data = -1  # 0-indexed
            max_row_with_data = -1  # 0-indexed
            cells_scanned = 0
            non_empty_cells = 0

            # Track consecutive empty rows for early stopping
            consecutive_empty_rows = 0

            # Scan through Calamine's data
            for row_idx, row_cells in enumerate(data):
                row_has_data = False
                consecutive_empty_cols = 0

                # Determine how far to scan this row:
                # - At least min_columns (50)
                # - At least to the max column we've seen data in so far
                min_col_to_scan = max(self.config.min_columns, max_col_with_data + 1)

                # Scan through the cells in this row
                for col_idx, cell_value in enumerate(row_cells):
                    cells_scanned += 1

                    if not is_cell_empty(cell_value):
                        # Found data
                        max_col_with_data = max(max_col_with_data, col_idx)
                        max_row_with_data = row_idx
                        row_has_data = True
                        non_empty_cells += 1
                        consecutive_empty_cols = 0
                    else:
                        consecutive_empty_cols += 1

                        # Stop scanning this row after threshold consecutive empty cells
                        # But ensure we've scanned at least to min_col_to_scan
                        if consecutive_empty_cols >= self.config.empty_threshold and (col_idx + 1) >= min_col_to_scan:
                            break

                # Track consecutive empty rows
                if row_has_data:
                    consecutive_empty_rows = 0
                else:
                    consecutive_empty_rows += 1

                # Stop scanning rows after threshold consecutive empty rows
                # But ensure we meet minimum row requirement
                if consecutive_empty_rows >= self.config.empty_threshold and (row_idx + 1) >= self.config.min_rows:
                    break

            calamine_time = (time.time() - calamine_start) * 1000  # ms

            # === PHASE 2: RAW XML BUFFER CHECK ===
            buffer_start = time.time()

            # Remember where Calamine stopped
            calamine_max_row = len(data) - 1  # 0-indexed, last row in data
            calamine_max_col = max(len(row) for row in data) - 1 if data else -1  # 0-indexed

            # Scan raw XML to find any cells beyond Calamine's boundaries
            try:
                xml_max_col, xml_max_row = self._scan_xml_for_boundaries(file_path, sheet_name)

                # Update our boundaries if XML found cells beyond Calamine
                if xml_max_col > max_col_with_data:
                    max_col_with_data = xml_max_col
                if xml_max_row > max_row_with_data:
                    max_row_with_data = xml_max_row
            except Exception as e:
                # If XML scan fails, just use Calamine results
                pass

            buffer_time = (time.time() - buffer_start) * 1000  # ms

            stats = {
                'cells_scanned': cells_scanned,
                'non_empty_cells': non_empty_cells,
                'calamine_time_ms': calamine_time,
                'buffer_time_ms': buffer_time
            }

            return (max_col_with_data, max_row_with_data), stats

        except SheetNotFoundError:
            raise
        except Exception as e:
            raise FileLoadError(file_path, f"Error during boundary scan: {str(e)}")
    
    def _scan_xml_for_boundaries(self, file_path: str, sheet_name: Optional[str]) -> Tuple[int, int]:
        """
        Fast XML scan to find cell boundaries by reading raw Excel XML.

        Excel files are ZIP archives. Cell data is in xl/worksheets/sheet{N}.xml
        with cells tagged as <c r="A1"> where r is the cell reference.

        Returns: (max_col_0indexed, max_row_0indexed)
        """
        import zipfile
        import xml.etree.ElementTree as ET
        import re

        try:
            # Excel files are ZIP archives
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Get workbook.xml to map sheet names to sheet numbers
                workbook_xml = zip_ref.read('xl/workbook.xml')
                workbook_root = ET.fromstring(workbook_xml)

                # Find sheet index by name
                sheets = workbook_root.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheet')
                sheet_idx = 1  # Default to first sheet

                if sheet_name:
                    for idx, sheet_elem in enumerate(sheets, 1):
                        if sheet_elem.get('name') == sheet_name:
                            sheet_idx = idx
                            break

                # Read the sheet XML
                sheet_xml_path = f'xl/worksheets/sheet{sheet_idx}.xml'
                sheet_xml = zip_ref.read(sheet_xml_path).decode('utf-8')

                # Find all cells WITH DATA using density-based outlier detection
                # Strategy: Collect all cell positions, then filter out isolated outliers

                # Split into cell chunks to check for actual data
                cell_chunks = re.split(r'<c\s+r="', sheet_xml)

                # Collect all cells with data
                cells_with_data = []
                col_counts = {}  # Count cells per column
                row_counts = {}  # Count cells per row

                for chunk in cell_chunks[1:]:  # Skip first chunk (before any cells)
                    # Extract cell reference (e.g., "BW66")
                    ref_match = re.match(r'([A-Z]+)(\d+)"', chunk)
                    if not ref_match:
                        continue

                    col_letter = ref_match.group(1)
                    row_num = int(ref_match.group(2))

                    # Find where this cell ends (</c>)
                    end_pos = chunk.find('</c>')
                    if end_pos == -1:
                        # Check if it's a self-closing tag
                        if '/>' not in chunk[:100]:
                            continue
                        # Self-closing tags have no data
                        continue

                    cell_content = chunk[:end_pos]

                    # Check if cell has actual data: <v>, <is>, or <f>
                    has_data = ('<v>' in cell_content or
                               '<is>' in cell_content or
                               '<f>' in cell_content or
                               '<f ' in cell_content)

                    if not has_data:
                        continue

                    # Convert column letter to 0-indexed number
                    col_idx = 0
                    for char in col_letter:
                        col_idx = col_idx * 26 + (ord(char) - ord('A') + 1)
                    col_idx -= 1  # Convert to 0-indexed

                    cells_with_data.append((col_idx, row_num - 1))  # Store as 0-indexed
                    col_counts[col_idx] = col_counts.get(col_idx, 0) + 1
                    row_counts[row_num - 1] = row_counts.get(row_num - 1, 0) + 1

                if not cells_with_data:
                    return (-1, -1)

                # Density-based outlier detection
                # Find max column/row, ignoring isolated outliers

                # Sort columns by position
                sorted_cols = sorted(col_counts.keys())
                sorted_rows = sorted(row_counts.keys())

                # Find rightmost column that isn't an outlier
                max_col = -1
                outlier_gap_threshold = 50  # If gap > 50 cols, likely an outlier

                for i, col in enumerate(sorted_cols):
                    # Check if this column is isolated (big gap from previous column)
                    if i > 0:
                        gap = col - sorted_cols[i - 1]
                        # If huge gap AND this column has very few cells, it's an outlier
                        if gap > outlier_gap_threshold and col_counts[col] <= 2:
                            # This and all subsequent columns are likely outliers
                            break
                    max_col = col

                # Find bottommost row that isn't an outlier
                max_row = -1
                outlier_gap_threshold_rows = 100  # Rows can have bigger gaps

                for i, row in enumerate(sorted_rows):
                    if i > 0:
                        gap = row - sorted_rows[i - 1]
                        # If huge gap AND this row has very few cells, it's an outlier
                        if gap > outlier_gap_threshold_rows and row_counts[row] <= 2:
                            break
                    max_row = row

                return (max_col, max_row)

        except Exception as e:
            # If XML scan fails, return -1, -1 (no data found)
            return (-1, -1)

    def _get_first_sheet_name(self, file_path: str) -> str:
        """Get the name of the first sheet in the workbook"""
        try:
            from python_calamine import CalamineWorkbook
            workbook = CalamineWorkbook.from_path(file_path)
            sheet_names = workbook.sheet_names
            return sheet_names[0] if sheet_names else "Sheet1"
        except Exception:
            return "Sheet1"  # Fallback