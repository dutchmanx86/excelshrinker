# Excel Compression Tools - API Reference

## Quick Start

### Format Compression - **Recommended approach**
```python
from compression import compress_formats

# Analyze and compress Excel sheet formats
result = compress_formats('financial_model.xlsx', 'Sheet1')

print(f"Cells analyzed: {result.cells_analyzed}")
print(f"Format ranges: {len(result.format_ranges)}")
print(f"Processing time: {result.processing_time_ms:.2f}ms")

# Export to JSON
json_output = result.to_json(indent=2)
```

### Inverted Index Compression
```python
from compression import compress_format_result_json

# Compress format result JSON (reduces repeated values)
compressed = compress_format_result_json(
    json_output,
    min_occurrences=2  # Compress values appearing 2+ times
)

print(f"Original: {compressed['compression_stats']['original_size_bytes']} bytes")
print(f"Compressed: {compressed['compression_stats']['compressed_size_bytes']} bytes")
print(f"Saved: {compressed['compression_stats']['space_saved_percent']}%")
```

---

## What This Does

The compression tools provide two complementary compression techniques:

### 1. Format Compression
**Detects and consolidates cell formats** by:
1. Scanning cells and identifying number formats (currency, percentage, date, etc.)
2. Grouping adjacent cells with the same format into ranges
3. Detecting time series patterns (quarterly, monthly, annual)
4. Returning a compact representation instead of individual cell data

**Example:** Instead of storing 100 individual currency cells, store one range: `A1:CV1` with format `currency`.

### 2. Inverted Index Compression
**Reduces repetition in JSON output** by:
1. Finding values that repeat multiple times
2. Creating an inverted index (value → list of locations)
3. Removing those entries from the main data structure
4. Typically achieves 30-70% size reduction

**Example:** If "Corporate" appears in 100 cells, store it once with a list of 100 cell references instead of repeating the string 100 times.

---

## Core Functions

### `compress_formats()`

**Main entry point** for format compression.

```python
from compression import compress_formats

result = compress_formats(
    file_path='model.xlsx',
    sheet_name='Summary',          # None = first sheet
    boundary_result=None,          # Optional pre-computed boundaries
    config=None,                   # Optional DetectionConfig
    verbose=False                  # True to print progress
)
```

**Returns:** `FormatResult` object with detected format ranges

**Performance:**
- Typical: 50-200ms for sheets with 10,000 cells
- Uses hybrid approach: Calamine (fast) + openpyxl (accurate)

---

### `compress_format_result_json()`

**Compress format result JSON** using inverted index.

```python
from compression import compress_format_result_json

compressed = compress_format_result_json(
    json_data=result.to_json(),    # JSON string or dict
    min_length=3,                  # Min string length to compress
    min_occurrences=2              # Min repetitions to compress
)
```

**Returns:** Dict with structure:
```python
{
    "inverted_index": {
        "Corporate": {"type": "string", "ranges": ["A1", "A5", ...]},
        "Revenue": {"type": "string", "ranges": ["B1", "B2", ...]}
    },
    "data": {
        "format_ranges": [...],  # Remaining non-compressed entries
        ...
    },
    "compression_stats": {
        "original_size_bytes": 45231,
        "compressed_size_bytes": 28901,
        "space_saved_percent": 36.1
    }
}
```

---

### `decompress_format_result_json()`

**Decompress inverted index compressed data.**

```python
from compression import decompress_format_result_json

# Decompress back to original format
original_data = decompress_format_result_json(compressed)
```

**Returns:** Original decompressed data structure

---

## Result Objects

### `FormatResult`

Main result object from format compression.

```python
result.sheet_name          # str: Sheet name
result.format_ranges       # List[FormatRange]: Detected ranges
result.processing_time_ms  # float: Processing time in ms
result.cells_analyzed      # int: Number of non-empty cells analyzed
result.format_counts       # Dict[str, int]: Count by format type

# Methods
result.to_dict()                      # Convert to dict
result.to_json(indent=2)              # Export as JSON string
result.get_ranges_by_type('currency') # Filter by format type
result.get_string_values()            # Get all string values
result.get_summary()                  # Human-readable summary
```

### `FormatRange`

Represents a range of cells with the same format.

```python
range_obj.range            # str: "A1:C1" or "B5" (single cell)
range_obj.type             # str: 'number', 'currency', 'percentage',
                          #      'string', 'date', 'time', 'other'
range_obj.value            # Optional[str]: Cell value (for strings)
range_obj.parsed_date      # Optional[str]: ISO date (for dates)
range_obj.format_code      # Optional[str]: Excel format code
range_obj.scale            # Optional[int]: Scale factor (1000, 1000000)
range_obj.date_series_info # Optional[Dict]: Time series metadata

# Properties
range_obj.is_single_cell   # bool: True if single cell
range_obj.start_cell       # str: Starting cell reference
range_obj.end_cell         # str: Ending cell reference

# Methods
range_obj.to_dict(include_debug=False)  # Convert to dict
```

---

## Format Types

The system detects these format types:

| Type | Description | Example |
|------|-------------|---------|
| `number` | General numbers | `1234.56`, `#,##0.00` |
| `currency` | Currency values | `$1,234.56`, `€100.00` |
| `percentage` | Percentages | `45.2%`, `0.452` with `0.0%` format |
| `string` | Text values | `"Revenue"`, `"Corporate"` |
| `date` | Date values | `2024-01-01`, `1Q24`, `FY2024` |
| `time` | Time values | `14:30:00`, `2:30 PM` |
| `other` | Unrecognized formats | Custom formats |

---

## Time Series Detection

The system automatically detects and consolidates time series patterns:

### Horizontal Series (Row-based)
```python
# Detected pattern: Quarterly series
{
    'range': 'B1:M1',
    'type': 'date',
    'date_series_info': {
        'series_type': 'quarterly',
        'increment': '1 quarter',
        'start_date': '2024-Q1',
        'pattern': 'Quarterly series from Q1 2024 to Q4 2026'
    }
}
```

**Supported series types:**
- `annual`: Years incrementing by 1
- `quarterly`: Quarters incrementing by 1
- `monthly`: Months incrementing by 1
- `repeating_annual`: Same year repeated N times
- `repeating_quarterly`: Same quarter repeated N times

### Vertical Series (Column-based)
```python
# Detected pattern: Unordered column dates
{
    'range': 'C2:C50',
    'type': 'date',
    'date_series_info': {
        'series_type': 'unordered_column',
        'count': 48,
        'start_date': '2020-01-01',
        'end_date': '2023-12-31'
    }
}
```

---

## Time Period Parsing

### Supported Formats

The parser recognizes financial time period strings:

```python
from compression.format_detector import TimePeriodParser

parser = TimePeriodParser()

# Quarters
parser.parse_to_date("1Q24")      # → "2024-01-01"
parser.parse_to_date("Q2 2024")   # → "2024-04-01"
parser.parse_to_date("Q3-24")     # → "2024-07-01"

# Fiscal years
parser.parse_to_date("FY24")      # → "2024-01-01"
parser.parse_to_date("FY2024")    # → "2024-01-01"

# Calendar years
parser.parse_to_date("CY24")      # → "2024-01-01"
parser.parse_to_date("CY2024")    # → "2024-01-01"

# Check if string is a time period
parser.is_time_period("1Q24")     # → True
parser.is_time_period("Revenue")  # → False
```

---

## Compression Statistics

### Format Compression Stats

```python
result = compress_formats('model.xlsx', 'Sheet1')

print(result.get_summary())
# Output:
# Format Detection Summary for 'Sheet1'
# ============================================================
# Total ranges detected: 125
# Cells analyzed: 8,432
# Processing time: 156.23ms
#
# Format Type Breakdown:
#   number      :   45 ranges
#   currency    :   32 ranges
#   percentage  :   18 ranges
#   string      :   15 ranges
#   date        :   12 ranges
#   time        :    3 ranges
```

### Inverted Index Compression Stats

```python
compressed = compress_format_result_json(json_data, min_occurrences=2)

stats = compressed['compression_stats']
print(f"Unique values indexed: {stats['unique_values']}")
print(f"Entries moved to index: {stats['entries_moved_to_index']}")
print(f"Entries remaining: {stats['entries_remaining']}")
print(f"Original size: {stats['original_size_bytes']:,} bytes")
print(f"Compressed size: {stats['compressed_size_bytes']:,} bytes")
print(f"Compression ratio: {stats['compression_ratio']}")
print(f"Space saved: {stats['space_saved_percent']}%")
```

---

## Complete Example

```python
from compression import compress_formats, compress_format_result_json
from compression import decompress_format_result_json, save_compressed_json
from boundary_detector import DetectionConfig

# Step 1: Configure detection (optional)
config = DetectionConfig(
    min_columns=50,
    min_rows=100,
    empty_threshold=20,
    min_columnar_dates=5  # Min dates for columnar series detection
)

# Step 2: Detect and compress formats
result = compress_formats(
    'financial_model.xlsx',
    sheet_name='P&L',
    config=config,
    verbose=True  # Print progress
)

# Step 3: Export to JSON
json_output = result.to_json(indent=2)

# Step 4: Apply inverted index compression
compressed = compress_format_result_json(
    json_output,
    min_occurrences=2  # Compress values appearing 2+ times
)

# Step 5: Save compressed result
save_compressed_json(compressed, 'compressed_pl.json')

# Later: Load and decompress
from compression import load_compressed_json
restored = load_compressed_json('compressed_pl.json')

print(f"Compression saved {compressed['compression_stats']['space_saved_percent']}%")
```

---

## Performance Tips

### 1. Pre-compute Boundaries
If analyzing multiple aspects of the same sheet, compute boundaries once:

```python
from boundary_detector import BoundaryDetector

detector = BoundaryDetector()
boundaries = detector.detect('model.xlsx', 'Sheet1')

# Reuse boundaries
result = compress_formats(
    'model.xlsx',
    'Sheet1',
    boundary_result=boundaries  # Skip boundary detection
)
```

### 2. Adjust Compression Thresholds
For more aggressive compression:

```python
# More aggressive (compress values appearing only once)
compressed = compress_format_result_json(json_data, min_occurrences=1)

# Less aggressive (only compress frequently repeated values)
compressed = compress_format_result_json(json_data, min_occurrences=5)
```

### 3. Use Verbose Mode for Large Sheets
```python
result = compress_formats('large_model.xlsx', verbose=True)
# Prints progress: "Progress: 20% (row 2000/10000)"
```

---

## Technical Details

### Libraries Used
- **python-calamine** (Rust): Ultra-fast cell value reading
- **openpyxl**: Accurate number format code extraction
- **dateutil**: Flexible date parsing and arithmetic

### Why It's Fast
1. Hybrid approach: Calamine for values, openpyxl for formats
2. Pre-loads all format codes in one pass using `iter_rows`
3. Groups adjacent cells with same format (reduces output size)
4. Early termination using boundary detection
5. Minimal memory usage (streams data)

### Architecture
```
compression/
├── format_compression.py       # Main entry point
├── inverted_index_compression.py  # JSON compression
├── format_detector/
│   ├── format_detector.py      # Core detection engine
│   ├── format_result.py        # Result model
│   ├── format_range.py         # Range model
│   ├── format_mappings.py      # Format classification
│   ├── time_period_parser.py   # Parse "1Q24", "FY2024", etc.
│   ├── time_range_detector.py  # Detect time series
│   └── date_series_analyzer.py # Analyze date intervals
```

---

## Use Cases

### 1. Large Model Analysis
Quickly understand the structure and format patterns in large financial models.

```python
result = compress_formats('budget_2024.xlsx', 'Monthly P&L')
currency_ranges = result.get_ranges_by_type('currency')
print(f"Found {len(currency_ranges)} currency ranges")
```

### 2. Format Validation
Ensure consistent formatting across sheets.

```python
result = compress_formats('report.xlsx', 'Summary')
for fmt_range in result.format_ranges:
    if fmt_range.type == 'percentage' and fmt_range.scale:
        print(f"Warning: Scaled percentage at {fmt_range.range}")
```

### 3. Data Export Optimization
Compress JSON exports for efficient storage and transmission.

```python
# Full pipeline
result = compress_formats('data.xlsx', 'Sheet1')
json_str = result.to_json()
compressed = compress_format_result_json(json_str)
save_compressed_json(compressed, 'export.json')

# Typical compression: 30-70% size reduction
```

### 4. Time Series Extraction
Extract time dimensions from financial models.

```python
result = compress_formats('forecast.xlsx', 'Revenue')
date_ranges = result.get_ranges_by_type('date')

for dr in date_ranges:
    if dr.date_series_info:
        series = dr.date_series_info
        print(f"{dr.range}: {series['series_type']} - {series['pattern']}")
```

---

## Error Handling

```python
from compression import compress_formats
from boundary_detector.exceptions import (
    FileLoadError,
    SheetNotFoundError,
    DetectionError
)

try:
    result = compress_formats('model.xlsx', 'NonExistent')
except FileNotFoundError as e:
    print(f"File not found: {e}")
except SheetNotFoundError as e:
    print(f"Sheet not found: {e}")
    print(f"Available sheets: {e.available_sheets}")
except DetectionError as e:
    print(f"Detection error: {e}")
```

---

## Installation

```bash
pip install python-calamine openpyxl python-dateutil
```

---

## Related Documentation

- [Boundary Detector API](../boundary_detector/API_REFERENCE.md) - Efficient data boundary detection
- Excel format codes: [Microsoft Support](https://support.microsoft.com/en-us/office/number-format-codes-5026bbd6-04bc-48cd-bf33-80f18b4eae68)
