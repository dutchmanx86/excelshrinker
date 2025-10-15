"""Script to detect boundaries for all sheets in sample.xlsx"""

import sys
import os
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'

# Add parent directory to path
sys.path.append(str(Path(__file__).parent))

from boundary_detector.core.boundary_detector import BoundaryDetector
from boundary_detector.models.detection_config import DetectionConfig


def detect_all_sheets(file_path: str):
    """Detect boundaries for all sheets in a workbook."""
    # Get sheet names
    print("Step 1: Loading workbook to get sheet names...")
    try:
        from python_calamine import CalamineWorkbook
        workbook = CalamineWorkbook.from_path(file_path)
        sheet_names = workbook.sheet_names
        print(f"  Loaded successfully")
    except ImportError:
        print("Error: python-calamine not installed")
        return

    print(f"\nAnalyzing file: {file_path}")
    print(f"Found {len(sheet_names)} sheet(s): {sheet_names}\n")
    print("=" * 80)

    # Create detector without chart detection
    print("\nStep 2: Creating BoundaryDetector...")
    config = DetectionConfig()
    detector = BoundaryDetector(config)
    print(f"  Detector created with config: empty_threshold={config.empty_threshold}")

    # Detect boundaries for each sheet
    results = {}
    for idx, sheet_name in enumerate(sheet_names, 1):
        print(f"\n[{idx}/{len(sheet_names)}] Processing sheet: '{sheet_name}'")
        print("-" * 80)

        try:
            print(f"  Calling detector.detect() without chart detection...")
            result = detector.detect(file_path, sheet_name, detect_charts=False)
            print(f"  Detection complete!")
            results[sheet_name] = result

            print(f"  Max Column (0-indexed): {result.max_column}")
            print(f"  Max Row (0-indexed):    {result.max_row}")
            print(f"  Total Columns:          {result.total_columns}")
            print(f"  Total Rows:             {result.total_rows}")
            print(f"  Cells Scanned:          {result.cells_scanned:,}")
            print(f"  Non-Empty Cells:        {result.non_empty_cells:,}")
            print(f"  Processing Time:        {result.processing_time_ms:.2f} ms")

            # Convert to Excel-style range
            from boundary_detector.utils.excel_utils import column_index_to_letter
            max_col_letter = column_index_to_letter(result.max_column)
            max_row_1indexed = result.max_row + 1
            print(f"  Excel Range:            A1:{max_col_letter}{max_row_1indexed}")

        except Exception as e:
            print(f"  ERROR: {e}")
            results[sheet_name] = None

    print("\n" + "=" * 80)
    print("\nSummary for test file creation:")
    print("-" * 80)

    for sheet_name, result in results.items():
        if result:
            from boundary_detector.utils.excel_utils import column_index_to_letter
            max_col_letter = column_index_to_letter(result.max_column)
            max_row_1indexed = result.max_row + 1
            print(f"  '{sheet_name}': {{")
            print(f"    'max_column': {result.max_column},")
            print(f"    'max_row': {result.max_row},")
            print(f"    'range': 'A1:{max_col_letter}{max_row_1indexed}'")
            print(f"  }},")

    return results


if __name__ == "__main__":
    file_path = "sample_data/sample.xlsx"
    detect_all_sheets(file_path)
