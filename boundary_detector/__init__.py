"""
Excel Boundary Detector - High-performance boundary detection for Excel files

This package provides efficient boundary detection for Excel worksheets using
a hybrid approach with calamine for fast cell scanning and openpyxl for chart detection.
"""

from .core.boundary_detector import BoundaryDetector
from .core.batch_detector import BatchBoundaryDetector
from .models.detection_config import DetectionConfig
from .models.boundary_result import BoundaryResult, ChartInfo
from .exceptions.errors import (
    BoundaryDetectorError,
    FileLoadError,
    SheetNotFoundError,
    DetectionError
)

__version__ = "1.0.0"
__all__ = [
    "BoundaryDetector",
    "BatchBoundaryDetector",
    "DetectionConfig",
    "BoundaryResult",
    "ChartInfo",
    "BoundaryDetectorError",
    "FileLoadError",
    "SheetNotFoundError",
    "DetectionError",
]