"""Configuration model for boundary detection"""

from dataclasses import dataclass


@dataclass
class DetectionConfig:
    """
    Configuration for Excel boundary detection.
    
    Attributes:
        min_columns: Minimum number of columns to scan before considering boundary
        min_rows: Minimum number of rows to scan before considering boundary
        empty_threshold: Number of consecutive empty cells/rows to declare boundary
        min_columnar_dates: Minimum number of dates in a column to be considered a series
    """
    
    min_columns: int = 50
    min_rows: int = 100
    empty_threshold: int = 20
    min_columnar_dates: int = 10
    
    def __post_init__(self):
        """Validate configuration values"""
        if self.min_columns < 1:
            raise ValueError("min_columns must be at least 1")
        if self.min_rows < 1:
            raise ValueError("min_rows must be at least 1")
        if self.empty_threshold < 1:
            raise ValueError("empty_threshold must be at least 1")
        if self.min_columnar_dates < 2:
            raise ValueError("min_columnar_dates must be at least 2")