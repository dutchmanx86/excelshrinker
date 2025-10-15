"""Debug script to check row lengths in Summary sheet"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from python_calamine import CalamineWorkbook

file_path = "sample_data/sample.xlsx"
workbook = CalamineWorkbook.from_path(file_path)
sheet = workbook.get_sheet_by_name("Summary")
data = sheet.to_python()

print("Checking Summary sheet row lengths:")
print(f"Total rows: {len(data)}")

# Check rows around row 40 (0-indexed = row 39)
for row_idx in [39, 40, 41, 64, 65, 66]:
    print(f"\nChecking row {row_idx + 1} (0-indexed {row_idx}):")
    if row_idx < len(data):
        row_data = data[row_idx]
        print(f"  Row exists, length = {len(row_data)}")

        # Find last non-empty cell
        last_non_empty = -1
        for col_idx in range(len(row_data) - 1, -1, -1):
            if row_data[col_idx] is not None and row_data[col_idx] != '':
                last_non_empty = col_idx
                break

        if last_non_empty >= 0:
            from boundary_detector.utils.excel_utils import column_index_to_letter
            col_letter = column_index_to_letter(last_non_empty)
            print(f"  Last non-empty cell: column {last_non_empty} ({col_letter}), value: {repr(row_data[last_non_empty])}")
    else:
        print(f"  Row does NOT exist in data (data has only {len(data)} rows)")
