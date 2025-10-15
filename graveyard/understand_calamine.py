"""Understand what calamine provides"""

from python_calamine import CalamineWorkbook

file_path = "sample_data/sample.xlsx"
wb = CalamineWorkbook.from_path(file_path)
sheet = wb.get_sheet_by_name("Summary")
data = sheet.to_python()

print("What does calamine provide?")
print(f"Type: {type(data)}")
print(f"Length (rows): {len(data)}")
print(f"\nFirst row type: {type(data[0])}")
print(f"First row length: {len(data[0])}")
print(f"\nLast row (index {len(data)-1}):")
print(f"  Type: {type(data[-1])}")
print(f"  Length: {len(data[-1])}")

# Check what happens with rows that have data far to the right
print(f"\nRow 40 (index 39) - should have data in column BW (74):")
print(f"  Length: {len(data[39])}")
print(f"  Column 73 (BV): {data[39][73]}")
print(f"  Column 74 (BW): {data[39][74] if len(data[39]) > 74 else 'NOT PROVIDED'}")

print(f"\nSo calamine provides:")
print(f"  - A list of rows (lists)")
print(f"  - Each row is a list of cell values")
print(f"  - Rows are trimmed to their rightmost non-empty cell")
print(f"  - Trailing completely empty rows are removed")
