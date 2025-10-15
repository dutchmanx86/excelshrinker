# Known Issues and Testing Guide

## Current Status (2025-10-09)

### Boundary Detection Algorithm Status

The boundary detection algorithm has been **modified** with a hybrid approach but is **not yet validated** against the full test suite.

**Current Implementation**: `boundary_detector/core/boundary_detector.py`
- **Phase 1**: Fast scan with calamine (scans all data calamine provides)
- **Phase 2**: Openpyxl verification of 100-row × 100-column buffer zone beyond calamine's boundaries

**Status**: Modified but untested on full dataset

---

## Known Issues

### Issue #1: Calamine Relies on Stale Excel Metadata
**Severity**: High
**Impact**: Missing data at sheet boundaries

**Description**:
Calamine uses Excel's internal "dimension" or "used range" metadata, which can become stale when cells are deleted or cleared. This causes calamine to pre-trim data before we can scan it.

**Example**:
- Summary sheet has data in cells C66:H66 and BW40:BW42
- Calamine only returns 65 rows (missing row 66)
- Calamine returns row data of length 74 (missing column BW which is column 75)

**Root Cause**: Excel stores dimension metadata that doesn't always reflect actual cell contents after deletions/moves.

---

### Issue #2: Openpyxl's max_row/max_column Also Unreliable
**Severity**: High
**Impact**: Cannot use as ground truth

**Description**:
Openpyxl's `max_row` and `max_column` properties also use Excel's stale metadata and are highly inaccurate.

**Test Results** (from `test_openpyxl_max.py`):
- **Summary**: Off by +1 column
- **Engineering**: Off by +335 rows (reports 399, actual 64)
- **Renewed**: Off by -300 rows (reports 7,599, actual 7,899)
- **Dash**: Off by +19,534 rows! (reports 19,907, actual 373)
- **Revenue by Client**: Off by +1,025 rows
- **Success rate**: 14.3% (1/7 sheets)

**Conclusion**: Both calamine AND openpyxl rely on the same unreliable Excel metadata.

---

### Issue #3: Performance vs Accuracy Tradeoff
**Severity**: Medium
**Impact**: Processing time

**Description**:
- **Cell-by-cell openpyxl scanning**: Accurate but very slow (~24 seconds for Summary sheet with 5,545 cells)
- **Calamine data loading**: Fast but misses data beyond Excel's metadata boundaries
- **Hybrid approach**: Unknown performance (currently implemented but not tested)

**Challenge**: Large sheets like "Renewed" (7,899 rows) would take excessive time with pure openpyxl scanning.

---

### Issue #4: Accidental Peripheral Cells
**Severity**: Medium
**Impact**: Processing time and file size

**Description**:
User concern about "errant single cells way out in the periphery that make processing time-intensive for what's really just an accidental user inputting a value into a cell."

**Need to Solve For**:
1. Capture all legitimate content
2. Ignore accidental outlier cells that bloat processing

**Status**: Not yet addressed

---

## Test Suite

### Reference Data

**Location**: `boundary_detector/test_boundaries.py`

The `EXPECTED_BOUNDARIES` dictionary contains **85 manually verified sheet boundaries** from `sample.xlsx`:

```python
EXPECTED_BOUNDARIES = {
    'Summary': ('BW', 66),
    'Master Ctrl': ('E', 33),
    'Dash Control': ('FS', 66),
    # ... 82 more sheets
}
```

**Note**: One correction was made after initial verification:
- **Revenue by Client**: Changed from BU11 to **BU22** (confirmed by user)

---

## How to Run Tests

### Test 1: Full Test Suite (85 sheets)
**File**: `boundary_detector/test_boundaries.py`

```bash
cd "C:\Users\piete\OneDrive\Desktop\Valuepath\CursorExperiments\ExcelShrinkerv6"
python boundary_detector/test_boundaries.py
```

**Output Format**:
```
Testing Boundary Detection
====================================================================================================
Sheet Name                               Expected        Detected        Column Diff  Row Diff     Status
====================================================================================================
Summary                                  BW66            BW66            0            0            PASS
Master Ctrl                              E33             E33             0            0            PASS
...
====================================================================================================

Summary:
  Total sheets: 85
  Passed: X
  Failed: Y
  Success rate: Z%
```

**Last Known Results** (before current modifications):
- **Success rate**: 31.8% (27/85 sheets passed)
- **Common failure**: Off by -1 row and/or -1 column due to calamine trimming

---

### Test 2: Single Sheet Quick Test
**File**: `test_single_sheet.py`

Tests only the Summary sheet for quick validation:

```bash
python test_single_sheet.py
```

**Expected Output**:
```
Testing sheet: Summary
Expected: BW66
Detected: BW66
Processing time: XXXXms
Cells scanned: X,XXX
Non-empty cells: XXX
PASS
```

**Last Known Results** (pure openpyxl approach):
- **Status**: PASS (BW66 detected correctly)
- **Processing time**: 24,032ms (~24 seconds)
- **Cells scanned**: 5,545

---

### Test 3: Subset of Representative Sheets
**File**: `test_subset_sheets.py`

Tests 7 diverse sheet types:

```bash
python test_subset_sheets.py
```

**Sheets tested**:
- Summary (large, wide)
- Master Ctrl (small)
- Renewed (very tall - 7,899 rows)
- Engineering (very wide - FS/189 columns)
- Revenue by Client (medium)
- ARR and Revenue --> (empty)
- LN (very small)

**Last Known Results**: Timed out after 5 minutes (likely stuck on "Renewed" sheet)

---

### Test 4: Openpyxl Accuracy Test
**File**: `test_openpyxl_max.py`

Tests openpyxl's `max_row` and `max_column` properties against expected values:

```bash
python test_openpyxl_max.py
```

**Purpose**: Determine if openpyxl's built-in properties can be trusted.

**Conclusion**: No - only 14.3% success rate on 7 test sheets.

---

## Interpreting Test Results

### Success Metrics

**100% Success**: All 85 sheets match expected boundaries exactly
- Column letter matches (e.g., BW = BW)
- Row number matches (e.g., 66 = 66)

**Acceptable Tolerance**: TBD - needs discussion with user
- Should we allow +/- N rows/columns for accidental outliers?
- How to distinguish "real data" from "accidental cell input"?

### Common Failure Patterns

**Pattern 1: -1 Row/Column**
- **Cause**: Calamine trimming based on stale Excel metadata
- **Example**: Detecting BV65 instead of BW66

**Pattern 2: Large Over-estimates**
- **Cause**: Stale Excel metadata from deleted rows
- **Example**: Engineering showing 399 rows instead of 64

**Pattern 3: Large Under-estimates**
- **Cause**: Excel metadata not updated after data added
- **Example**: Renewed showing 7,599 rows instead of 7,899

---

## Investigation Scripts

### Script 1: Investigate Calamine Behavior
**File**: `investigate_calamine.py`

Compares calamine vs openpyxl on Summary sheet:

```bash
python investigate_calamine.py
```

**Key Findings**:
```
CALAMINE:
  sheet.height: 65        (missing row 66!)
  sheet.width: 74         (missing column BW/75!)

OPENPYXL:
  max_row: 66
  max_column: 76

SPECIFIC CELLS:
  C66: 'Avg Bkgs'         (calamine misses this)
  BW40: datetime(...)     (calamine misses this)
```

---

## Next Steps / Open Questions

### Questions to Answer

1. **What level of accuracy is acceptable?**
   - Must we capture 100% of cells, or is 99% acceptable?
   - How do we handle accidental outlier cells?

2. **Performance requirements?**
   - What's the acceptable processing time per sheet?
   - Total time for all 85 sheets?

3. **Hybrid approach validation?**
   - Does the current hybrid implementation work?
   - What's the performance vs accuracy tradeoff?

### Potential Solutions to Explore

**Option 1: Increase Buffer Zone**
- Current: 100 rows × 100 columns beyond calamine
- Could increase to 200 × 200 or make configurable
- **Risk**: Slower performance

**Option 2: Smart Outlier Detection**
- Scan full sheet but identify "isolated" cells far from main data cluster
- Report outliers to user for decision
- **Benefit**: Catches accidental cells without bloating boundaries

**Option 3: Configurable Scan Strategy**
- Let user choose: "Fast" (calamine only) vs "Accurate" (full openpyxl scan)
- **Benefit**: Flexibility for different use cases

**Option 4: Two-Pass Approach**
- Pass 1: Quick scan with calamine + small buffer
- Pass 2: If failures detected, full openpyxl scan on problem sheets
- **Benefit**: Fast for most sheets, accurate for edge cases

---

## Benchmark Targets

### Performance Targets (TBD)

- **Per sheet**: Target <5 seconds average
- **Full suite (85 sheets)**: Target <7 minutes total
- **Large sheets (>1000 rows)**: Target <15 seconds

### Accuracy Targets

- **Primary goal**: 100% success rate on all 85 test sheets
- **Minimum acceptable**: >95% success rate
- **Zero false negatives**: Must not miss actual data

---

## Version History

### Current Version (Hybrid - Untested)
- **Date**: 2025-10-09
- **Approach**: Calamine scan + 100×100 openpyxl buffer
- **Status**: Implemented but not validated
- **File**: `boundary_detector/core/boundary_detector.py` (modified)

### Previous Version (Pure Calamine)
- **Success rate**: 31.8% (27/85 sheets)
- **Issue**: Missing data beyond calamine's trimmed boundaries

### Tested Alternatives

1. **Pure Openpyxl cell-by-cell**: Accurate but too slow (>5min for full suite)
2. **Openpyxl max_row/max_column**: Fast but inaccurate (14.3% success)
3. **Calamine + offset**: Doesn't work - made results worse

---

## File Locations

```
ExcelShrinkerv6/
├── boundary_detector/
│   ├── core/
│   │   └── boundary_detector.py         [MODIFIED - Hybrid approach]
│   ├── models/
│   │   └── detection_config.py          [Config: min_rows=100, min_cols=50, threshold=20]
│   └── test_boundaries.py               [MAIN TEST SUITE - 85 sheets]
├── test_single_sheet.py                 [Quick test - Summary only]
├── test_subset_sheets.py                [Medium test - 7 representative sheets]
├── test_openpyxl_max.py                 [Openpyxl accuracy validation]
├── investigate_calamine.py              [Debug calamine behavior]
└── sample_data/
    └── sample.xlsx                      [Test data - 85 sheets]
```
