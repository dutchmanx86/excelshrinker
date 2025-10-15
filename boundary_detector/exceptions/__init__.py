"""Custom exceptions for Excel boundary detection"""

from .errors import (
    BoundaryDetectorError,
    FileLoadError,
    SheetNotFoundError,
    DetectionError
)

__all__ = [
    "BoundaryDetectorError",
    "FileLoadError",
    "SheetNotFoundError",
    "DetectionError",
]