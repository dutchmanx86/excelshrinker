"""Data models for Excel boundary detection"""

from .detection_config import DetectionConfig
from .boundary_result import BoundaryResult, ChartInfo

__all__ = ["DetectionConfig", "BoundaryResult", "ChartInfo"]