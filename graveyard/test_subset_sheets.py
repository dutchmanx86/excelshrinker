"""Test boundary detection on a subset of representative sheets"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent))

from boundary_detector.core.boundary_detector import BoundaryDetector
from boundary_detector.models.detection_config import DetectionConfig


def column_letter_to_index(col_letter):
    """Convert column letter to 0-indexed number"""
    if col_letter is None:
        return None
    result = 0
    for char in col_letter:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result - 1


def column_index_to_letter(col_index):
    """Convert 0-indexed column number to letter"""
    if col_index is None:
        return None
    result = []
    col_index += 1
    while col_index > 0:
        col_index -= 1
        result.append(chr(col_index % 26 + ord('A')))
        col_index //= 26
    return ''.join(reversed(result))


# Test a diverse subset of sheets
TEST_CASES = [
    ('Summary', 'BW', 66),                    # Large sheet with wide columns
    ('Master Ctrl', 'E', 33),                 # Small sheet
    ('Renewed', 'N', 7899),                   # Very tall sheet
    ('Engineering', 'FS', 64),                # Wide sheet (FS = 189 columns!)
    ('Revenue by Client', 'BU', 22),          # Medium sheet
    ('ARR and Revenue -->', None, None),      # Empty sheet
    ('LN', 'T', 9),                           # Very small sheet
]


def test_sheets():
    """Test multiple sheets and report results"""
    file_path = "sample_data/sample.xlsx"

    config = DetectionConfig()
    detector = BoundaryDetector(config)

    print("Testing Boundary Detection on Subset of Sheets")
    print("=" * 100)
    print(f"{'Sheet Name':<30} {'Expected':<15} {'Detected':<15} {'Time (ms)':<12} {'Cells':<12} {'Status'}")
    print("=" * 100)

    passed = 0
    failed = 0
    total_time = 0

    for sheet_name, expected_col_letter, expected_row in TEST_CASES:
        try:
            result = detector.detect(file_path, sheet_name, detect_charts=False)

            detected_col_letter = column_index_to_letter(result.max_column)
            detected_row = result.max_row + 1

            if expected_col_letter is None:
                expected_display = "EMPTY"
                detected_display = f"{detected_col_letter}{detected_row}"
                status = "PASS" if result.max_column <= 1 and result.max_row <= 1 else "FAIL"
            else:
                expected_display = f"{expected_col_letter}{expected_row}"
                detected_display = f"{detected_col_letter}{detected_row}"

                if detected_col_letter == expected_col_letter and detected_row == expected_row:
                    status = "PASS"
                else:
                    status = "FAIL"

            if status == "PASS":
                passed += 1
            else:
                failed += 1

            total_time += result.processing_time_ms

            print(f"{sheet_name:<30} {expected_display:<15} {detected_display:<15} {result.processing_time_ms:<12.0f} {result.cells_scanned:<12,} {status}")

        except Exception as e:
            print(f"{sheet_name:<30} {'ERROR':<15} {str(e):<50}")
            failed += 1

    print("=" * 100)
    print(f"\nSummary:")
    print(f"  Total sheets tested: {len(TEST_CASES)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Success rate: {(passed/len(TEST_CASES))*100:.1f}%")
    print(f"  Total time: {total_time/1000:.1f}s")
    print(f"  Average time per sheet: {total_time/len(TEST_CASES)/1000:.1f}s")

    return passed == len(TEST_CASES)


if __name__ == "__main__":
    success = test_sheets()
    sys.exit(0 if success else 1)
