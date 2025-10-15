"""Check cell C66 using both calamine and openpyxl"""

from python_calamine import CalamineWorkbook
import openpyxl

file_path = "sample_data/sample.xlsx"

print("=== Calamine ===")
wb_cal = CalamineWorkbook.from_path(file_path)
sheet_cal = wb_cal.get_sheet_by_name("Summary")
data = sheet_cal.to_python()

print(f"Total rows from calamine: {len(data)}")
print(f"Row 66 (0-indexed 65) exists: {65 < len(data)}")
if 65 < len(data):
    row_data = data[65]
    col_c = 2  # Column C is index 2
    print(f"Cell C66 value: {repr(row_data[col_c] if col_c < len(row_data) else None)}")

print("\n=== Openpyxl ===")
wb_xl = openpyxl.load_workbook(file_path, data_only=True, read_only=True)
sheet_xl = wb_xl["Summary"]

# Check C66
cell = sheet_xl['C66']
print(f"Cell C66 value: {repr(cell.value)}")
print(f"Cell C66 is None: {cell.value is None}")

# Check BW40
cell_bw40 = sheet_xl['BW40']
print(f"Cell BW40 value: {repr(cell_bw40.value)}")

wb_xl.close()
