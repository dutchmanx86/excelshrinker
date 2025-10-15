"""Test boundary detection on a single sheet for quick verification"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent))

from boundary_detector.core.boundary_detector import BoundaryDetector
from boundary_detector.models.detection_config import DetectionConfig


def column_index_to_letter(col_index):
    """Convert 0-indexed column number to letter"""
    if col_index is None:
        return None
    result = []
    col_index += 1  # Convert to 1-indexed for calculation
    while col_index > 0:
        col_index -= 1
        result.append(chr(col_index % 26 + ord('A')))
        col_index //= 26
    return ''.join(reversed(result))


def test_summary_sheet():
    """Test Summary sheet - should be BW66"""
    file_path = "sample_data/sample.xlsx"
    sheet_name = "Summary"
    expected = ('BW', 66)

    # Create detector
    config = DetectionConfig()
    detector = BoundaryDetector(config)

    print(f"Testing sheet: {sheet_name}")
    print(f"Expected: {expected[0]}{expected[1]}")

    # Detect boundaries
    result = detector.detect(file_path, sheet_name, detect_charts=False)

    detected_col_letter = column_index_to_letter(result.max_column)
    detected_row = result.max_row + 1  # Convert 0-indexed to 1-indexed

    print(f"Detected: {detected_col_letter}{detected_row}")
    print(f"Processing time: {result.processing_time_ms:.0f}ms")
    print(f"  - Calamine scan: {result.calamine_time_ms:.0f}ms")
    print(f"  - Buffer check: {result.buffer_time_ms:.0f}ms")
    print(f"Cells scanned: {result.cells_scanned:,}")
    print(f"Non-empty cells: {result.non_empty_cells:,}")

    if detected_col_letter == expected[0] and detected_row == expected[1]:
        print("PASS")
        return True
    else:
        print("FAIL")
        print(f"  Column diff: {result.max_column - (ord(expected[0][-1]) - ord('A') + (ord(expected[0][0]) - ord('A') + 1) * 26 - 1) if len(expected[0]) == 2 else result.max_column - (ord(expected[0]) - ord('A'))}")
        print(f"  Row diff: {(result.max_row + 1) - expected[1]}")
        return False


if __name__ == "__main__":
    success = test_summary_sheet()
    sys.exit(0 if success else 1)
