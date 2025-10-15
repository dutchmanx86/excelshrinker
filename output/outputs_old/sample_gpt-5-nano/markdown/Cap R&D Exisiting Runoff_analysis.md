## 1. Spreadsheet Overview
- **Sheet Name**: Cap R&D Exisiting Runoff
- **Key Sections Identified**:
  - Time Series Axis (Monthly)
  - FX Rate Metadata
  - Runoff Data Grid
  - Annual ds_2 Dates
  - Annual ds_2 Values
  - Cross-Sectional Metrics (N17:P17)

## 2. Detailed Section Analysis

### Time Series Axis (Monthly)
- **Section Type**: Time Series Header
- **Description & Purpose**: Defines the primary monthly time axis used across the sheet to anchor projections and calculations. The header row provides the chronological labels for the main data grid.
- **Cell Range**: `C1:BJ1`
- **Time Series Horizon**:
  - **Dates Location**: `C1:BJ1`
  - **Date Range**: Start 2020-01; End 2024-12
  - **Frequency**: Monthly
- **Key Components**: Monthly date headers across the column span (C through BJ) forming the central time axis.
- **Notes & Customizations**: The monthly series is defined in the metadata as ds_1 with the pattern “Monthly series from 2020-01 to 2024-12.”

---

### FX Rate Metadata
- **Section Name**: FX Rate Metadata
- **Section Type**: Metadata Table
- **Description & Purpose**: Provides a reference FX rate used for currency conversions within the workbook. Serves as a fixed FX anchor rather than a historical series.
- **Cell Range**: `A11:B11`
- **Time Series Horizon**:
  - **Dates Location**: N/A
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**: The label in A11 reads "1/31/20 Exchange Rate" and the corresponding numeric rate is in B11.
- **Notes & Customizations**: This is a single-point FX reference (not a full history). The date label is included in the dictionary for clarity but there is no ongoing series in this section.

---

### Runoff Data Grid
- **Section Name**: Runoff Data Grid
- **Section Type**: Standard Data Grid
- **Description & Purpose**: Main numeric data matrix representing runoff-related projections (e.g., capex/R&D runoff) aligned to the monthly time axis. Typically used to feed KPI calculations or scenario analyses.
- **Cell Range**: `C9:BJ10`
- **Time Series Horizon**:
  - **Dates Location**: `C1:BJ1`
  - **Date Range**: Start 2020-01; End 2024-12
  - **Frequency**: Monthly
- **Key Components**: Two data rows across the monthly grid that hold the primary numeric projections.
- **Notes & Customizations**: Standard data grid; values may be linked to other metrics or calculations within the workbook. May require cross-referencing with the FX rate anchor where currency adjustments are involved.

---

### Annual ds_2 Dates
- **Section Name**: Annual ds_2 Dates (ds_2)
- **Section Type**: Time Series Anchor
- **Description & Purpose**: Annual time-axis labels for the secondary time series (ds_2), used to structure metrics that are evaluated on a yearly basis (2015–2020).
- **Cell Range**: `G16:L16`
- **Time Series Horizon**:
  - **Dates Location**: `G16:L16`
  - **Date Range**: Start 2015-01; End 2020-01 (Annual)
  - **Frequency**: Annual
- **Key Components**: Date headers across six yearly periods (one per year from 2015 to 2020).
- **Notes & Customizations**: Defined by the date_series_definitions entry ds_2: “Annual series from 2015 to 2020.”

---

### Annual ds_2 Values
- **Section Name**: Annual ds_2 Values
- **Section Type**: Time Series Data
- **Description & Purpose**: Numeric values aligned to the ds_2 annual dates, representing year-level metrics or baselines used in annual analyses.
- **Cell Range**: `G17:L17`
- **Time Series Horizon**:
  - **Dates Location**: `G16:L16`
  - **Date Range**: 2015–2020
  - **Frequency**: Annual
- **Key Components**: A row of numeric values corresponding to the years 2015–2020.
- **Notes & Customizations**: These values feed into annual calculations or scenario analyses anchored by the ds_2 axis.

---

### Cross-Sectional Metrics (N17:P17)
- **Section Name**: Cross-Sectional Metrics (N17:P17)
- **Section Type**: Supplemental Metrics
- **Description & Purpose**: Additional ad-hoc metrics located on row 17 across columns N through P. These are ancillary values that may be used for final adjustments or miscellaneous calculations.
- **Cell Range**: `N17:P17`
- **Time Series Horizon**:
  - **Dates Location**: N/A
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**: Isolated metric values at N17 and P17 (with O17 included in the range if accessed as a contiguous segment).
- **Notes & Customizations**: Not part of the main monthly or annual time-series grids; requires context from workbook references for proper interpretation.