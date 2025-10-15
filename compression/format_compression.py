"""Unified format compression interface"""

from typing import Optional
from pathlib import Path

from boundary_detector.models.boundary_result import BoundaryResult
from boundary_detector.models.detection_config import DetectionConfig
from compression.format_detector.format_detector import FormatDetector
from compression.format_detector.format_result import FormatResult


def compress_formats(
    file_path: str,
    sheet_name: Optional[str] = None,
    boundary_result: Optional[BoundaryResult] = None,
    config: Optional[DetectionConfig] = None,
    verbose: bool = False
) -> FormatResult:
    """
    Compress Excel sheet by detecting and consolidating format ranges.

    This function performs "format compression" which:
    1. Detects number formats in cells (currency, percentage, date, etc.)
    2. Groups adjacent cells with the same format into ranges
    3. Detects and consolidates time series patterns
    4. Returns a compact representation of the sheet's format structure

    Args:
        file_path: Path to the Excel file
        sheet_name: Name of the sheet to analyze. If None, uses first sheet.
        boundary_result: Optional pre-computed boundary result for efficiency
        config: Optional detection configuration
        verbose: If True, prints progress messages to stderr.

    Returns:
        FormatResult with detected format ranges and statistics

    Example:
        >>> result = compress_formats('financial_model.xlsx', 'Sheet1')
        >>> print(f"Cells analyzed: {result.cells_analyzed}")
        >>> print(f"Format ranges: {len(result.format_ranges)}")
        >>>
        >>> # Export to JSON
        >>> json_output = result.to_json(indent=2)
    """
    # Validate file exists
    file_path_obj = Path(file_path)
    if not file_path_obj.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Create format detector
    detector = FormatDetector(config)

    # Detect and consolidate formats
    result = detector.detect(file_path, sheet_name, boundary_result, verbose=verbose)

    return result
