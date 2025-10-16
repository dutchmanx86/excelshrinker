"""Result model for format detection operations"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime
import json
import hashlib

from .format_range import FormatRange


@dataclass
class FormatResult:
    """
    Result of a format detection operation.
    
    Attributes:
        sheet_name: Name of the worksheet that was analyzed
        format_ranges: List of detected format ranges
        processing_time_ms: Time taken for detection in milliseconds
        cells_analyzed: Total number of cells analyzed
        format_counts: Dictionary mapping format types to their counts
    """
    
    sheet_name: str
    format_ranges: List[FormatRange] = field(default_factory=list)
    processing_time_ms: float = 0.0
    cells_analyzed: int = 0
    format_counts: Dict[str, int] = field(default_factory=dict)
    
    def __post_init__(self):
        """Calculate statistics if not provided"""
        if not self.format_counts and self.format_ranges:
            self._calculate_format_counts()
    
    def _calculate_format_counts(self):
        """Calculate count of each format type"""
        self.format_counts = {}
        for format_range in self.format_ranges:
            format_type = format_range.type
            self.format_counts[format_type] = self.format_counts.get(format_type, 0) + 1

    def add_range(self, format_range: FormatRange):
        """
        Add a format range to the result.
        
        Args:
            format_range: FormatRange to add
        """
        self.format_ranges.append(format_range)
        # Update counts
        format_type = format_range.type
        self.format_counts[format_type] = self.format_counts.get(format_type, 0) + 1
    
    def to_dict(self, include_debug: bool = False, deduplicate_date_series: bool = True) -> Dict[str, Any]:
        """
        Convert to dictionary for JSON serialization.

        Args:
            include_debug: If True, include debug information in format ranges
            deduplicate_date_series: If True, deduplicate identical date_series objects

        Returns:
            Dictionary representation of the format result
        """
        if deduplicate_date_series:
            return self._to_dict_with_deduplication(include_debug)

        return {
            'success': True,
            'sheet_name': self.sheet_name,
            'format_ranges': [
                fr.to_dict(include_debug=include_debug)
                for fr in self.format_ranges
            ],
            'statistics': {
                'processing_time_ms': round(self.processing_time_ms, 2),
                'cells_analyzed': self.cells_analyzed,
                'total_ranges': len(self.format_ranges),
                'format_counts': self.format_counts
            },
            'metadata': {
                'detected_at': datetime.utcnow().isoformat() + 'Z'
            }
        }

    def _to_dict_with_deduplication(self, include_debug: bool = False) -> Dict[str, Any]:
        """
        Convert to dictionary with date series deduplication.

        Collects all date_series/date_series_info objects, deduplicates them,
        and replaces them with ID references.
        """
        # Step 1: Collect and deduplicate date series
        date_series_map = {}  # hash -> (id, series_dict)
        date_series_counter = 1

        for fr in self.format_ranges:
            # Check for date_series (old format) or date_series_info (new format)
            series_dict = getattr(fr, 'date_series', None) or getattr(fr, 'date_series_info', None)

            if series_dict:
                # Create a hash of the series dict for deduplication
                series_hash = self._hash_dict(series_dict)

                if series_hash not in date_series_map:
                    series_id = f"ds_{date_series_counter}"
                    date_series_map[series_hash] = (series_id, series_dict)
                    date_series_counter += 1

        # Step 2: Build format_ranges with ID references
        format_ranges_output = []

        for fr in self.format_ranges:
            fr_dict = fr.to_dict(include_debug=include_debug)

            # Check for date_series or date_series_info
            if 'date_series' in fr_dict or 'date_series_info' in fr_dict:
                series_key = 'date_series' if 'date_series' in fr_dict else 'date_series_info'
                series_dict = fr_dict[series_key]
                series_hash = self._hash_dict(series_dict)
                series_id, _ = date_series_map[series_hash]

                # Replace with ID reference
                del fr_dict[series_key]
                fr_dict['date_series_id'] = series_id

            format_ranges_output.append(fr_dict)

        # Step 3: Build result with date_series_definitions
        result = {
            'success': True,
            'sheet_name': self.sheet_name,
            'format_ranges': format_ranges_output,
            'statistics': {
                'processing_time_ms': round(self.processing_time_ms, 2),
                'cells_analyzed': self.cells_analyzed,
                'total_ranges': len(self.format_ranges),
                'format_counts': self.format_counts
            },
            'metadata': {
                'detected_at': datetime.utcnow().isoformat() + 'Z'
            }
        }

        # Only add date_series_definitions if there are any
        if date_series_map:
            # Add anchor points to each date series definition
            date_series_defs_with_anchors = {}
            for series_id, series_dict in date_series_map.values():
                # Find the range that uses this series_id to get cell coordinates
                range_str = None
                for fr in format_ranges_output:
                    if fr.get('date_series_id') == series_id:
                        range_str = fr['range']
                        break

                # Add anchor points if we found a range
                if range_str:
                    series_with_anchors = series_dict.copy()
                    anchor_points = self._calculate_anchor_points(
                        series_dict, range_str
                    )
                    if anchor_points:
                        series_with_anchors['anchor_points'] = anchor_points
                    date_series_defs_with_anchors[series_id] = series_with_anchors
                else:
                    date_series_defs_with_anchors[series_id] = series_dict

            result['date_series_definitions'] = date_series_defs_with_anchors

        return result

    def _calculate_anchor_points(
        self,
        series_dict: Dict[str, Any],
        range_str: str
    ) -> Optional[Dict[str, str]]:
        """
        Calculate anchor points for a date series (every 12th cell for series > 24 cells).

        Args:
            series_dict: Date series definition dictionary
            range_str: Excel range string (e.g., "T3:FS3")

        Returns:
            Dictionary mapping cell references to dates, or None if series is too short
        """
        # Only add anchor points for horizontal series longer than 24 cells
        if ':' not in range_str:
            return None

        start_cell, end_cell = range_str.split(':')

        # Parse start and end cells
        import re
        start_match = re.match(r'([A-Z]+)(\d+)', start_cell)
        end_match = re.match(r'([A-Z]+)(\d+)', end_cell)

        if not start_match or not end_match:
            return None

        start_col_str, start_row_str = start_match.groups()
        end_col_str, end_row_str = end_match.groups()

        # Only process horizontal series (same row)
        if start_row_str != end_row_str:
            return None

        # Convert column letters to indices
        def col_to_num(col_str):
            num = 0
            for char in col_str:
                num = num * 26 + (ord(char) - ord('A') + 1)
            return num

        start_col = col_to_num(start_col_str)
        end_col = col_to_num(end_col_str)
        series_length = end_col - start_col + 1

        # Only create anchor points if series is longer than 24 cells
        if series_length <= 24:
            return None

        # Get start date from series_dict
        start_date = series_dict.get('start_date')
        if not start_date:
            return None

        # Parse start date
        from datetime import datetime
        try:
            start_datetime = datetime.fromisoformat(start_date)
        except:
            return None

        # Calculate anchor points every 12 cells
        anchor_points = {}
        row_num = start_row_str

        # Helper to convert column number to letter
        def num_to_col(n):
            result = ''
            while n > 0:
                n -= 1
                result = chr(65 + n % 26) + result
                n //= 26
            return result

        for offset in range(0, series_length, 12):
            col_num = start_col + offset
            if col_num > end_col:
                break

            col_letter = num_to_col(col_num)
            cell_ref = f"{col_letter}{row_num}"

            # Calculate date for this anchor point
            # Add months based on offset (assuming monthly series)
            from dateutil.relativedelta import relativedelta
            anchor_date = start_datetime + relativedelta(months=offset)
            anchor_points[cell_ref] = anchor_date.date().isoformat()

        return anchor_points if anchor_points else None

    def _hash_dict(self, d: Dict[str, Any]) -> str:
        """
        Create a consistent hash of a dictionary for deduplication.

        Args:
            d: Dictionary to hash

        Returns:
            Hash string
        """
        # Convert dict to sorted JSON string for consistent hashing
        dict_str = json.dumps(d, sort_keys=True)
        return hashlib.md5(dict_str.encode()).hexdigest()
    
    def to_json(self, indent: int = 2, include_debug: bool = False, deduplicate_date_series: bool = True) -> str:
        """
        Export as JSON string.

        Args:
            indent: Number of spaces for JSON indentation
            include_debug: If True, include debug information
            deduplicate_date_series: If True, deduplicate identical date_series objects

        Returns:
            JSON string representation
        """
        return json.dumps(
            self.to_dict(include_debug=include_debug, deduplicate_date_series=deduplicate_date_series),
            indent=indent
        )
    
    def get_ranges_by_type(self, format_type: str) -> List[FormatRange]:
        """
        Get all ranges of a specific format type.
        
        Args:
            format_type: The format type to filter by
        
        Returns:
            List of FormatRange objects matching the type
        """
        return [fr for fr in self.format_ranges if fr.type == format_type]
    
    def get_string_values(self) -> List[str]:
        """
        Get all string values from string-type ranges.
        
        Returns:
            List of string values
        """
        return [
            fr.value 
            for fr in self.format_ranges 
            if fr.type == 'string' and fr.value is not None
        ]
    
    def get_summary(self) -> str:
        """
        Get a human-readable summary of the detection results.
        
        Returns:
            Summary string
        """
        lines = [
            f"Format Detection Summary for '{self.sheet_name}'",
            f"=" * 60,
            f"Total ranges detected: {len(self.format_ranges)}",
            f"Cells analyzed: {self.cells_analyzed}",
            f"Processing time: {self.processing_time_ms:.2f}ms",
            f"",
            f"Format Type Breakdown:"
        ]
        
        # Sort format counts by count (descending)
        sorted_counts = sorted(
            self.format_counts.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        for format_type, count in sorted_counts:
            lines.append(f"  {format_type:12s}: {count:4d} ranges")
        
        return '\n'.join(lines)
    
    def __repr__(self) -> str:
        """String representation for debugging"""
        return (
            f"FormatResult(sheet='{self.sheet_name}', "
            f"ranges={len(self.format_ranges)}, "
            f"time={self.processing_time_ms:.2f}ms)"
        )