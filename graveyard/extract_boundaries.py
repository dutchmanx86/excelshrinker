"""Extract sheet boundaries from detection results"""

import re

with open('detection_results.txt', 'r') as f:
    content = f.read()

# Find all sheet processing blocks
pattern = r"Processing sheet: '([^']+)'.*?Excel Range:\s+A1:([A-Z]+)(\d+)"
matches = re.findall(pattern, content, re.DOTALL)

print("All sheet boundaries:")
print("=" * 60)
for sheet_name, max_col, max_row in matches:
    print(f"{sheet_name} - {max_col} - {max_row}")
