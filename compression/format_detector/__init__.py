"""Format detection support utilities"""

from compression.format_detector.format_detector import FormatDetector
from compression.format_detector.format_result import FormatResult
from compression.format_detector.format_range import FormatRange
from compression.format_detector.time_period_parser import TimePeriodParser
from compression.format_detector.time_range_detector import TimeRangeDetector

__all__ = [
    'FormatDetector',
    'FormatResult',
    'FormatRange',
    'TimePeriodParser',
    'TimeRangeDetector',
]
