"""Result models for boundary detection"""

from dataclasses import dataclass
from typing import List, Dict, Any
from datetime import datetime


@dataclass
class ChartInfo:
    """
    Information about a chart detected in the worksheet.
    
    Attributes:
        chart_type: Type of chart (e.g., 'BarChart', 'LineChart')
        from_column: Starting column index (0-indexed)
        from_row: Starting row index (0-indexed)
        to_column: Ending column index (0-indexed)
        to_row: Ending row index (0-indexed)
        overlaps_data: Whether the chart overlaps with detected data area
    """
    
    chart_type: str
    from_column: int
    from_row: int
    to_column: int
    to_row: int
    overlaps_data: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            'chart_type': self.chart_type,
            'from_column': self.from_column,
            'from_row': self.from_row,
            'to_column': self.to_column,
            'to_row': self.to_row,
            'overlaps_data': self.overlaps_data,
            'cell_range': self._get_cell_range()
        }
    
    def _get_cell_range(self) -> str:
        """Get Excel-style cell range (e.g., 'A1:D10')"""
        from ..utils.excel_utils import column_index_to_letter
        
        start_col = column_index_to_letter(self.from_column)
        end_col = column_index_to_letter(self.to_column)
        
        return f"{start_col}{self.from_row + 1}:{end_col}{self.to_row + 1}"


@dataclass
class BoundaryResult:
    """
    Result of boundary detection operation.
    
    Attributes:
        max_column: Maximum column with data (0-indexed)
        max_row: Maximum row with data (0-indexed)
        total_columns: Total count of columns with data
        total_rows: Total count of rows with data
        charts: List of detected charts
        sheet_name: Name of the worksheet
        processing_time_ms: Time taken for detection in milliseconds
    """
    
    max_column: int
    max_row: int
    total_columns: int
    total_rows: int
    charts: List[ChartInfo]
    sheet_name: str
    processing_time_ms: float
    cells_scanned: int = 0
    non_empty_cells: int = 0
    calamine_time_ms: float = 0.0
    buffer_time_ms: float = 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        from ..utils.excel_utils import column_index_to_letter
        
        return {
            'success': True,
            'sheet_name': self.sheet_name,
            'boundary': {
                'max_column': self.max_column,
                'max_row': self.max_row,
                'total_columns': self.total_columns,
                'total_rows': self.total_rows,
                'column_letter': column_index_to_letter(self.max_column),
                'last_cell': f"{column_index_to_letter(self.max_column)}{self.max_row + 1}"
            },
            'charts': [chart.to_dict() for chart in self.charts],
            'scan_statistics': {
                'cells_scanned': self.cells_scanned,
                'non_empty_cells': self.non_empty_cells,
                'processing_time_ms': round(self.processing_time_ms, 2)
            },
            'metadata': {
                'detected_at': datetime.utcnow().isoformat() + 'Z'
            }
        }