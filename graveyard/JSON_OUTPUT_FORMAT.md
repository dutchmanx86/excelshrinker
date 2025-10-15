# JSON Output Format for Time Series

## Overview
The compressed JSON output now includes comprehensive time series information for all detected date ranges.

## JSON Structure

```json
{
  "success": true,
  "sheet_name": "SheetName",
  "format_ranges": [
    {
      "range": "E2:Q2",
      "type": "date",
      "date_series": {
        "series_type": "annual",
        "increment": "1 year",
        "start_date": "2015-01-01",
        "pattern": "Annual series from 2015 to 2027"
      }
    },
    {
      "range": "T3:FS3",
      "type": "date",
      "date_series": {
        "series_type": "monthly",
        "increment": "1 month",
        "start_date": "2015-01-31",
        "pattern": "Monthly series from 2015-01 to 2027-12"
      }
    },
    {
      "range": "T1:FS1",
      "type": "date",
      "date_series": {
        "series_type": "repeating_annual",
        "increment": "12 months (annual)",
        "start_date": "2015-01-01",
        "pattern": "Annual values repeating 12 times from 2015 to 2027"
      }
    }
  ],
  "statistics": {
    "processing_time_ms": 150.25,
    "cells_analyzed": 5000,
    "total_ranges": 120,
    "format_counts": {
      "date": 15,
      "number": 80,
      "currency": 20,
      "string": 5
    }
  },
  "metadata": {
    "detected_at": "2025-10-09T14:18:16.956159Z"
  }
}
```

## Time Series Fields

### `date_series` Object
Present in format ranges that are part of a detected time series pattern.

| Field | Type | Description | Example Values |
|-------|------|-------------|----------------|
| `series_type` | string | Type of time series | `"annual"`, `"monthly"`, `"quarterly"`, `"repeating_annual"`, `"repeating_quarterly"` |
| `increment` | string | How the series increments | `"1 year"`, `"1 month"`, `"1 quarter"`, `"12 months (annual)"`, `"3 months (quarterly)"` |
| `start_date` | string | Starting date/period | `"2015-01-01"`, `"2015-Q1"` |
| `pattern` | string | Human-readable description | `"Annual series from 2015 to 2027"` |

### Series Types

1. **`annual`** - Years incrementing by 1
   - Example: 2015, 2016, 2017, ...
   - Increment: `"1 year"`

2. **`quarterly`** - Quarters incrementing by 1
   - Example: 1Q15, 2Q15, 3Q15, 4Q15, 1Q16, ...
   - Increment: `"1 quarter"`

3. **`monthly`** - Months incrementing by 1
   - Example: Jan 2015, Feb 2015, Mar 2015, ...
   - Increment: `"1 month"`

4. **`repeating_annual`** - Same year repeated N times before incrementing
   - Example: 2015 (x12), 2016 (x12), 2017 (x12), ...
   - Increment: `"12 months (annual)"` or other multiples
   - Common in financial models where each column represents a month

5. **`repeating_quarterly`** - Same quarter repeated N times before incrementing
   - Example: 1Q16 (x3), 2Q16 (x3), 3Q16 (x3), ...
   - Increment: `"3 months (quarterly)"` or other multiples
   - Common where each column represents a month within quarters

## Usage Examples

### Python: Extract Time Series

```python
import json

# Load JSON output
with open('excel_output.json', 'r') as f:
    data = json.load(f)

# Get all time series ranges
time_series = [
    r for r in data['format_ranges']
    if 'date_series' in r
]

# Print time series information
for series in time_series:
    print(f"Range: {series['range']}")
    print(f"  Type: {series['date_series']['series_type']}")
    print(f"  Increment: {series['date_series']['increment']}")
    print(f"  Pattern: {series['date_series']['pattern']}")
    print(f"  Start: {series['date_series']['start_date']}")
    print()
```

### Python: Filter by Series Type

```python
# Get only annual series
annual_series = [
    r for r in data['format_ranges']
    if r.get('date_series', {}).get('series_type') == 'annual'
]

# Get monthly series
monthly_series = [
    r for r in data['format_ranges']
    if r.get('date_series', {}).get('series_type') == 'monthly'
]

# Get repeating patterns (for column headers)
repeating_series = [
    r for r in data['format_ranges']
    if r.get('date_series', {}).get('series_type', '').startswith('repeating_')
]
```

### JavaScript: Parse Time Series

```javascript
// Load JSON
const data = JSON.parse(jsonString);

// Get time series
const timeSeries = data.format_ranges.filter(r => r.date_series);

// Group by series type
const byType = timeSeries.reduce((acc, range) => {
    const type = range.date_series.series_type;
    if (!acc[type]) acc[type] = [];
    acc[type].push(range);
    return acc;
}, {});

console.log('Annual series:', byType.annual);
console.log('Monthly series:', byType.monthly);
```

## Benefits

1. **Compression**: Multiple individual date cells are consolidated into single range entries
2. **Clarity**: Series type and pattern are explicitly identified
3. **Flexibility**: Easy to reconstruct original data or transform to other formats
4. **Validation**: Increment information helps validate data integrity
5. **Documentation**: Pattern descriptions provide human-readable context

## Backward Compatibility

- Non-time-series date cells will still have individual entries
- The `date_series` field is optional - only present when a pattern is detected
- Existing code that doesn't check for `date_series` will continue to work
- All existing format range fields (`range`, `type`, etc.) are preserved

## File Size Impact

Time series detection significantly reduces JSON file size:
- **Before**: 156 individual date cell entries for monthly data (2015-2027)
- **After**: 1 consolidated range entry with series metadata
- **Reduction**: ~99% fewer entries for long time series

## Testing

Run `test_json_output.py` to verify JSON serialization:

```bash
python test_json_output.py
```

Expected output: All tests pass with properly formatted time series information.
