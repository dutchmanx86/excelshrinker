# Excel Boundary Detector - API Reference

## Quick Start

### Fast Mode (No Charts) - **Recommended for most use cases**
```python
from excel_boundary_detector import BatchBoundaryDetector

detector = BatchBoundaryDetector()
results = detector.detect_all_sheets('file.xlsx', detect_charts=False)

# 86 sheets in ~6 seconds
for sheet_name, result in results.items():
    print(f"{sheet_name}: {result.total_columns} × {result.total_rows}")
```

### With Chart Detection
```python
from excel_boundary_detector import BatchBoundaryDetector

detector = BatchBoundaryDetector()
results = detector.detect_all_sheets('file.xlsx', detect_charts=True)

# 86 sheets in ~36 seconds (slower but includes chart positions)
for sheet_name, result in results.items():
    print(f"{sheet_name}: {result.total_columns} × {result.total_rows}")
    print(f"  Charts: {len(result.charts)}")
```

---

## What This Does

Finds the **actual data boundaries** in Excel files by:
1. Scanning left-to-right, top-to-bottom for non-empty cells
2. Stopping after 20 consecutive empty cells (configurable)
3. Ensuring minimum 50 columns × 100 rows scanned
4. Optionally detecting chart positions

**Why it's fast:** Uses calamine (Rust-based) for cell scanning instead of pure Python.

---

## Core Functions

### `BatchBoundaryDetector.detect_all_sheets()`

**Recommended for multi-sheet workbooks** - Opens file once, processes all sheets.

```python
from excel_boundary_detector import BatchBoundaryDetector

detector = BatchBoundaryDetector()
results = detector.detect_all_sheets(
    file_path='sample.xlsx',
    detect_charts=False,  # True to detect charts (adds ~30s)
    parallel=False        # True for parallel processing (experimental)
)
```

**Returns:** `Dict[str, BoundaryResult]` - Dictionary mapping sheet names to results

**Performance:**
- Without charts: ~6s for 86 sheets (70ms/sheet)
- With charts: ~36s for 86 sheets (420ms/sheet)

---

### `BoundaryDetector.detect()`

**For single sheets** - Use when you only need one specific sheet.

```python
from excel_boundary_detector import BoundaryDetector

detector = BoundaryDetector()
result = detector.detect(
    file_path='sample.xlsx',
    sheet_name='Summary'  # None = first sheet
)

print(f"Boundary: {result.total_columns} × {result.total_rows}")
print(f"Charts: {len(result.charts)}")
```

**Returns:** `BoundaryResult` object

---

## Configuration

### `DetectionConfig`

```python
from excel_boundary_detector import DetectionConfig, BatchBoundaryDetector

config = DetectionConfig(
    min_columns=50,      # Minimum columns to scan
    min_rows=100,       # Minimum rows to scan
    empty_threshold=20  # Empty cells before declaring boundary
)

detector = BatchBoundaryDetector(config)
results = detector.detect_all_sheets('file.xlsx', detect_charts=False)
```

---

## Result Objects

### `BoundaryResult`

```python
result.max_column         # int: Last column with data (0-indexed)
result.max_row           # int: Last row with data (0-indexed)
result.total_columns     # int: Total columns (max_column + 1)
result.total_rows        # int: Total rows (max_row + 1)
result.charts            # List[ChartInfo]: Detected charts
result.sheet_name        # str: Sheet name
result.cells_scanned     # int: Number of cells scanned
result.non_empty_cells   # int: Number of non-empty cells
result.processing_time_ms # float: Processing time in milliseconds

# Convert to dictionary
result_dict = result.to_dict()  # JSON-serializable
```

### `ChartInfo`

```python
chart.chart_type      # str: e.g., 'BarChart', 'LineChart'
chart.from_column     # int: Starting column (0-indexed)
chart.from_row       # int: Starting row (0-indexed)
chart.to_column      # int: Ending column (0-indexed)
chart.to_row         # int: Ending row (0-indexed)
chart.overlaps_data  # bool: Whether chart overlaps data area

# Get Excel-style reference
chart_dict = chart.to_dict()
print(chart_dict['cell_range'])  # e.g., 'C7:H21'
```

---

## Performance Comparison

| Sheets | Without Charts | With Charts | Speedup |
|--------|---------------|-------------|---------|
| 86     | 5.9s          | 35.9s       | 6.1x    |

**When to skip charts:**
- You don't need chart positions → Use `detect_charts=False`
- Need maximum speed → Use `detect_charts=False`

**When to detect charts:**
- Analyzing dashboard layouts
- Avoiding chart overlaps when writing data
- Chart inventory/auditing

---

## Error Handling

```python
from excel_boundary_detector import (
    BoundaryDetector,
    FileLoadError,
    SheetNotFoundError,
    DetectionError
)

try:
    detector = BoundaryDetector()
    result = detector.detect('file.xlsx', sheet_name='NonExistent')
except FileLoadError as e:
    print(f"File error: {e}")
except SheetNotFoundError as e:
    print(f"Sheet not found: {e}")
    print(f"Available: {e.available_sheets}")
except DetectionError as e:
    print(f"Detection error: {e}")
```

---

## Technical Details

### Libraries Used
- **python-calamine** (Rust): Ultra-fast cell reading (5-10x faster than Python)
- **openpyxl**: Chart detection (requires normal mode, not read-only)

### Why It's Fast
1. Opens workbook **once** for all sheets (not per-sheet)
2. Rust-based calamine for cell scanning
3. Early termination after empty thresholds
4. Minimal memory usage (streams data)

### Architecture
```
excel_boundary_detector/
├── BoundaryDetector      # Single sheet detection
├── BatchBoundaryDetector # Multi-sheet (40x faster)
├── DetectionConfig       # Configuration options
├── BoundaryResult        # Results + metadata
└── ChartInfo            # Chart metadata
```

---

## Complete Example

```python
from excel_boundary_detector import BatchBoundaryDetector, DetectionConfig

# Custom configuration
config = DetectionConfig(
    min_columns=100,
    min_rows=200,
    empty_threshold=30
)

# Process workbook
detector = BatchBoundaryDetector(config)
results = detector.detect_all_sheets(
    'sample.xlsx',
    detect_charts=False  # Fast mode
)

# Analyze results
for sheet_name, result in results.items():
    if result.non_empty_cells > 10000:
        print(f"Large sheet: {sheet_name}")
        print(f"  Size: {result.total_columns} × {result.total_rows}")
        print(f"  Data: {result.non_empty_cells:,} non-empty cells")
        print(f"  Time: {result.processing_time_ms:.0f}ms")

# Save to JSON
import json
json_output = {name: r.to_dict() for name, r in results.items()}
with open('boundaries.json', 'w') as f:
    json.dump(json_output, f, indent=2)
```

---

## Installation

```bash
pip install python-calamine openpyxl