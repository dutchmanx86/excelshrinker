"""Debug XML scanner"""

from boundary_detector.core.boundary_detector import BoundaryDetector
from boundary_detector.models.detection_config import DetectionConfig

detector = BoundaryDetector(DetectionConfig())

# Test on Summary sheet
file_path = "sample_data/sample.xlsx"
sheet_name = "Summary"

try:
    xml_max_col, xml_max_row = detector._scan_xml_for_boundaries(file_path, sheet_name)
    print(f"XML scanner returned: col={xml_max_col}, row={xml_max_row}")

    # Convert to Excel notation
    if xml_max_col >= 0:
        col_letter = ""
        col_idx = xml_max_col + 1
        while col_idx > 0:
            col_idx -= 1
            col_letter = chr(col_idx % 26 + ord('A')) + col_letter
            col_idx //= 26
        print(f"  Column: {col_letter} (index {xml_max_col})")

    if xml_max_row >= 0:
        print(f"  Row: {xml_max_row + 1} (index {xml_max_row})")

except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
