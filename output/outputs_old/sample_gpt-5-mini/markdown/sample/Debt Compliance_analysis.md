## 1. Spreadsheet Overview
- **Sheet Name**: Debt Compliance
- **Key Sections Identified**:
  - Time Header / Column Dates (sheet time axis)
  - Revenue / T3M
  - Growth Covenant (covenant values + per-period status)
  - RML Calculation (Remaining Months Liquidity and its drivers)
  - Liquidity Threshold & Compliance (threshold comparison and flags)
  - Liquidity Buffers ( $5m, RML, Overall )
  - Compliance Status Matrix (per-period "OK" indicators consolidated)

## 2. Detailed Section Analysis

### Time Header / Column Dates
- **Section Type**: Date / Time Axis (multi-frequency)
- **Description & Purpose**: Master column/row date headers used across the sheet. Contains multiple date series used by downstream blocks: quarterly repeating series, annual series and a monthly series. This is the primary place to resolve which period each numeric column corresponds to.
- **Cell Range**: C1:EC3
- **Time Series Horizon**:
  - **Dates Location**:
    - Quarterly header: N1:EC1 (primary repeating-quarterly axis)
    - Annual headers: C2:L2 and C3:L3 (annual axis for left-side annual columns)
    - Repeating-annual: N2:EC2 (annual values repeating)
    - Monthly: N3:EC3 (monthly series)
  - **Date Range** (resolved from date series definitions):
    - Quarterly (ds_1): 2018-Q1 through 2027-Q4 (series_type: repeating_quarterly)
    - Annual (ds_2 / ds_3): 2018 through 2027 (annual series / repeating-annual pattern)
    - Monthly (ds_4): 2018-01 to 2027-12 (monthly)
  - **Frequency**: Mixed — Quarterly (primary), Annual, Monthly
- **Key Components**: column-period labels for the main table; multiple parallel date bands used by different numeric columns (left-side annual band; main N:EC band with quarterly/monthly).
- **Notes & Customizations**: There are overlapping date series for different column bands (annual on C:L vs. quarterly/monthly on N:EC). Any data retrieval must pick the correct date series based on column band.

### Revenue / T3M
- **Section Type**: Key Revenue Table (time series)
- **Description & Purpose**: Top-left financial time series showing Revenue and a short-term metric labeled "T3M" (likely trailing 3 months). Presented in both left-side annual columns and the main N:EC time band (thousand-scaled in portions).
- **Cell Range**: A7:EC9
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual columns (left band): C7:L7 (aligns to ds_2 annual)
    - Main band: N7:EC7 (aligns to ds_1 repeating-quarterly / ds_3 repeating-annual depending on column)
  - **Date Range**:
    - Annual: 2018 — 2027
    - Quarterly (main band): 2018-Q1 — 2027-Q4
  - **Frequency**: Annual (left) and Quarterly (main band); some main-band numeric ranges use a 1,000 scale (see format for P8:EC8 and AB9:EC9).
- **Key Components**: Revenue row and a "T3M" indicator (short-term trailing measure). Numeric values are presented in both annual and period (quarter/month) columns.
- **Notes & Customizations**: Portions of the main band are stored with a scale (1000) in certain ranges — callers should apply scaling where indicated.

### Growth Covenant
- **Section Type**: Covenant / Compliance Row (Custom covenant check)
- **Description & Purpose**: Single-row covenant definition and per-period numeric covenant values with per-period status flags. Used to indicate whether the growth covenant is met each period.
- **Cell Range**: A11:EC12
- **Time Series Horizon**:
  - **Dates Location**:
    - Numeric covenant series: AO11:EC11 (main N:EC band)
    - Per-period status flags: AO12:EC12 (OK / status strings)
  - **Date Range**: AO11/EC11 align to the main date band (Quarterly: 2018-Q1 — 2027-Q4)
  - **Frequency**: Quarterly (main band)
- **Key Components**: covenant numeric series (per period) and an adjacent status row of per-period indicators (OK/flag).
- **Notes & Customizations**: Status cells are string flags ("OK") distributed across the same columns as covenant numbers. The covenant numeric series is located in the N:EC band beginning at AO; retrieval should map AO..EC columns to the sheet time axis.

### RML Calculation (Remaining Months Liquidity and drivers)
- **Section Type**: Composite calculation table (Liquidity / cash covenant driver)
- **Description & Purpose**: Central calculation block for RML (Remaining Months Liquidity). Includes borrowings, availability, net availability, unrestricted cash, EBITDA and its adjustments (capitalized R&D, capitalized CapEx, change in deferred revenue), Adjusted EBITDA and the derived RML values along with component breakdowns and per-period status indicators.
- **Cell Range**: A15:EC33
- **Time Series Horizon**:
  - **Dates Location**:
    - Left-band annual values: C24:L24 (EBITDA annual band)
    - Main period band (drivers & RML): N17:EC17 (Total Borrowings), AP18:EC18 (Total Availability), AP22:EC22 (Net Availability + Unrestricted Cash), N24:EC24 and O25:EC27 etc. (EBITDA and adjustments), AP30:EC30 (RML), AP31: various component columns, AP32:EC32 (component totals)
    - Status row: AP33:EC33 (per-period "OK" flags)
  - **Date Range**:
    - Annual left columns: 2018 — 2027
    - Main band: 2018-Q1 — 2027-Q4 (quarterly repeating), and certain monthly detail may align to the monthly series where specified (N3:EC3 / ds_4)
  - **Frequency**: Mixed — Annual (left summary columns) and Quarterly (primary main band). Some component ranges are scaled (1000).
- **Key Components**: Total Borrowings, Total Availability, Net Availability + Unrestricted Cash, EBITDA, adjustments (Capitalized R&D, Capitalized Expenditures, Change in Deferred Revenue), Adjusted EBITDA, RML result and component breakdown, per-period pass/fail status row.
- **Notes & Customizations**: Several numeric columns are stored with a 1,000 scale. The block is an integrated calculation area — EBITDA and its adjustments live adjacent to borrowing/availability lines used to compute RML. Per-period OK flags appear in row 33.

### Liquidity Threshold & Compliance
- **Section Type**: Threshold comparison table / Covenant check
- **Description & Purpose**: Compares computed Liquidity (Net Availability + Unrestricted Cash etc.) to defined thresholds and outputs per-period compliance flags. Also exposes Restricted Cash and Net Availability breakdowns used in the threshold comparison.
- **Cell Range**: A35:EC44
- **Time Series Horizon**:
  - **Dates Location**:
    - Threshold and numeric comparison band: N37:EC37 (numeric threshold row), AP39:EC39 (Net Availability), AP40:EC40 (Liquidity), AP42:CC42 (thresholds by column), CC41/CC43 referenced numbers
    - Compliance status row: AP44:EC44 (per-period "OK" indicators)
  - **Date Range**: Main band aligns to 2018-Q1 — 2027-Q4 (quarterly); some numeric entries use 1,000-scale in later columns.
  - **Frequency**: Quarterly (primary)
- **Key Components**: Restricted Cash, Net Availability, Liquidity calculation, per-period threshold values and resulting compliance flags.
- **Notes & Customizations**: The sheet contains a spelled label "Thershold" at A42 (typo). Threshold values are split between AP:CC and CD:EC regions (mixed scales) — be careful to pick the appropriate numeric column when retrieving threshold values.

### Liquidity Buffers
- **Section Type**: Buffer lines (safety cushion reporting)
- **Description & Purpose**: Shows the $5m Liquidity Buffer, an RML Liquidity Buffer, and an Overall Liquidity Buffer by period — used to present additional buffer calculations on top of computed liquidity.
- **Cell Range**: A48:EC52
- **Time Series Horizon**:
  - **Dates Location**:
    - $5m Buffer: AP48:EC48
    - RML Liquidity Buffer: AP50:EC50 (left part AP50:BM50 plus BN50 and BO50:EC50 with scaling)
    - Overall Liquidity Buffer: AP52:EC52
  - **Date Range**: AP..EC aligns to main sheet date axis (2018-Q1 — 2027-Q4)
  - **Frequency**: Quarterly (primary)
- **Key Components**: Fixed $5m buffer row, RML buffer (period breakdown with mixed scaling in BN50), and aggregated overall buffer row.
- **Notes & Customizations**: RML Liquidity Buffer row uses a mixed layout (AP50:BM50 numeric, BN50 is scaled by 1,000, BO50:EC50 continues) — ensure scaling rules from format ranges are applied.

### Compliance Status Matrix
- **Section Type**: Status / Compliance flags matrix
- **Description & Purpose**: Consolidated matrix of per-period "OK" flags used throughout the sheet to indicate compliance across different covenant checks and thresholds. These rows provide quick boolean-style checks across the time band.
- **Cell Range**: AO12:EC12, AP33:EC33, AP44:EC44 (three separate horizontal status rows; if a single rectangular envelope is preferred: AO12:EC44 covers them with other content)
- **Time Series Horizon**:
  - **Dates Location**: status columns are within the main band AO..EC (aligns to N1:EC1)
  - **Date Range**: 2018-Q1 — 2027-Q4 (quarterly)
  - **Frequency**: Quarterly
- **Key Components**: Per-period "OK" flags for Growth Covenant (row 12), RML (row 33), and Liquidity Threshold (row 44).
- **Notes & Customizations**: Many status cells are identical "OK" strings; some non-applicable periods are populated with "N/A" in isolated blocks (see N/A ranges in the inverted index). Use these status rows as the primary quick pass/fail indicators.

---

If you want, I can:
- produce a minimal map of each section to the column-by-period mapping (i.e., list which column letter corresponds to which quarter/date for the main N:EC band), or
- return these sections as JSON with the same ranges for programmatic retrieval.