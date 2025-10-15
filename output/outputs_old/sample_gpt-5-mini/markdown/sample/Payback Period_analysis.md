## 1. Spreadsheet Overview
- **Sheet Name**: Payback Period
- **Key Sections Identified**:
  - Title / Scenario header
  - Payback Period — Summary (Total Company)
  - Total Company — Detailed Time Series (monthly)
  - Payback Period — Financial (summary + detailed time series)
  - Payback Period — Corporate (summary + detailed time series)
  - Repeated small input cells for "Multiplier" / "Increase" at each time-series block

## 2. Detailed Section Analysis

### Title / Scenario header
- **Section Type**: Document header / scenario metadata
- **Description & Purpose**: High-level worksheet header identifying the company, the sheet purpose and scenario name. Also includes a small row of numeric scenario parameters (across D2:P2).
- **Cell Range**: A1:P3
- **Time Series Horizon**:
  - **Dates Location**: none (this is a header area)
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**:
  - Company name cell (A1 = "AlphaSense, Inc.")
  - Sheet title (A2 = "Payback Period")
  - Scenario label (A3 = "1 - Base - $25mm")
  - Scenario numeric row across D2:P2
- **Notes & Customizations**:
  - D2:P2 contains numeric scenario parameters (format detected as numbers).
  - This area is not part of the time-series tables.

---

### Payback Period — Summary (Total Company)
- **Section Type**: Key Metrics / KPI Summary table
- **Description & Purpose**: Consolidated Payback KPIs for the entire company (LTV, CAC, ARR metrics, Gross Margin, Contribution ARR, Support/Upsell costs, Payback, Cash Payback, etc.). Intended for quick readout of core payback indicators.
- **Cell Range**: A5:P44
- **Time Series Horizon**:
  - **Dates Location**: summary values are presented horizontally across columns D:P on multiple summary rows (see D15:P15, D19:P19, etc. — summary numeric columns in this area). The row labels (metric names) live in column A (e.g., A13 = "LTV / CAC", A15 = "Initial Period ARR", A16 = "New Clients Added", ... A43 = "Payback").
  - **Date Range**: Not explicitly present as calendar dates in the extracted metadata — summary rows include multiple period columns across D:P (these columns correspond to whatever scenario periods the workbook uses).
  - **Frequency**: The summary is periodized across columns (same periodicity as underlying time-series — see Time Series sections below). The sheet uses "Month" as the primary frequency elsewhere; summary columns follow that periodization.
- **Key Components**:
  - High-level metrics group (LTV / CAC, Initial Period ARR, ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR)
  - Cost and unit metrics (Support Cost, Support Cost per Client, Upsell Cost, Upsell Cost per Client)
  - Derived metrics (Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback)
  - "Cash Payback" row and adjacent numeric columns
- **Notes & Customizations**:
  - Many numeric summary columns use a thousands scale (several numeric cells in D:E and onward flagged with scale = 1000).
  - The summary area occupies a compact region for quick KPI retrieval; metric labels are concentrated in column A and numeric datapoints across D:P.

---

### Total Company — Detailed Time Series
- **Section Type**: Time-series table / Detailed metric roll-forward (Company-wide)
- **Description & Purpose**: Detailed month-by-month ledger of payback-related metrics for the Total Company. This is the primary time-series block that underpins the summary KPIs above and contains many metric rows with period columns across F:P (and other columns).
- **Cell Range**: A46:P341
- **Time Series Horizon**:
  - **Dates Location**: A46 contains the column label "Month"; the actual period labels are in A47:A341 (the column of row labels under "Month").
  - **Date Range**: The sheet extract does not include explicit calendar values for these months in the provided metadata. The date labels live in A47:A341 (so this block holds the full set of monthly periods from row 47 through 341).
  - **Frequency**: Monthly (header label is "Month")
- **Key Components**:
  - Column A: "Month" label + period (row) dates/periods (A47:A341)
  - Columns B–C: small per-block input cells present at the top of the block (B46 = "Multiplier", C46 = "Increase") used as scenario knobs
  - Columns D–P: primary numeric time-series values (metric values across periods)
  - Multiple metric rows grouped vertically (revenue/ARR build, costs, contributions, cumulative sums used to compute payback)
- **Notes & Customizations**:
  - Many numeric time-series cells are formatted with a thousands scale (several ranges flagged as scale=1000). Consumers of this range should apply that formatting / scaling when reading raw numbers.
  - Within this block there are repeated sub-groups (the A-column "Month" reappears later in the sheet at other starting rows for other blocks) — but the full Total Company block to retrieve all company-level months is A46:P341.

---

### Payback Period — Financial (summary + detailed)
- **Section Type**: KPI summary (Financial) + Time-series table (Financial)
- **Description & Purpose**: A second major payback analysis scoped to a "Financial" view. Includes a Financial header, a compact financial summary (metrics similar to summary but scoped to Financial), and then a detailed monthly time-series region for financial metrics.
- **Cell Range**: A344:P574
- **Time Series Horizon**:
  - **Dates Location**:
    - Header row: A344 ("Payback Period - Financial")
    - Time-series month label for this block appears at A379 ("Month"); corresponding period labels are in A380:A574.
  - **Date Range**: Actual calendar labels are not provided in the extracted metadata. Period labels are in A380:A574 (assumed monthly).
  - **Frequency**: Monthly (label "Month")
- **Key Components**:
  - Financial header and compact financial KPIs (summary numeric columns in F348:P353, F355:P356 etc. — summary numeric rows near the header)
  - Column A: Month header and period labels (A379 onward)
  - Columns B–C at the top of this block: B379 = "Multiplier", C379 = "Increase" — per-block inputs for scenario adjustments
  - Columns F–P: primary financial metric time-series (values across months)
- **Notes & Customizations**:
  - The Financial summary uses many of the same metric names as the company summary (e.g., ARR, LTV, CAC elements) but scoped to the Financial view.
  - Numeric cells in this area frequently use a thousands scale (format metadata shows repeated scale=1000 entries for F/G and later columns).
  - This block runs up to the row immediately before the Corporate header at A575.

---

### Payback Period — Corporate (summary + detailed)
- **Section Type**: KPI summary (Corporate) + Time-series table (Corporate)
- **Description & Purpose**: Corporate-scoped payback analysis (corporate-level costs, support/up-sell/cost allocations, corporate payback metrics). Includes a corporate header and summary rows followed by detailed monthly time-series for corporate metrics.
- **Cell Range**: A575:P804
- **Time Series Horizon**:
  - **Dates Location**:
    - Header row: A575 ("Payback Period - Corporate")
    - Time-series month label for this block appears at A610 ("Month"); corresponding period labels are in A611:A804.
    - (The inverted index shows additional "Month" occurrences at A610 and A708 which are contained in this section; primary period labels for the corporate table live in A611:A804.)
  - **Date Range**: Not supplied explicitly in the extracted metadata. Period labels are present down the block (A611:A804), assumed to be consecutive monthly periods.
  - **Frequency**: Monthly (label "Month")
- **Key Components**:
  - Corporate header and compact KPI rows (F579:P585 etc. — summary numeric rows adjacent to the header)
  - Column A: Month header and period labels (starting A611)
  - Columns B–C at the top of this block: B610 = "Multiplier", C610 = "Increase" — per-block inputs for scenario adjustments
  - Columns F–P (and other columns) contain the corporate time-series numeric values (many rows).
- **Notes & Customizations**:
  - Numeric formatting in this section often uses a thousands scale (format metadata indicates many F/P ranges with scale=1000).
  - Corporate block extends to the end of the analyzed sheet area (the extract continues through A804 and F804:P804). If you need an absolute sheet-end capture, use A575:P804.

---

Notes common to multiple sections
- The sheet is organized as three parallel time-series groups (Total Company starting at row 46, Financial starting at row 379 / header A344, Corporate starting at row 610 / header A575). Each group uses:
  - Column A for the "Month" header and period labels for that group
  - Columns B and C for small per-block inputs titled "Multiplier" and "Increase" (entries B46/C46, B379/C379, B610/C610)
  - Time-series numeric columns spanning F (or D/E) through P for period values
- Numeric scale: many numeric ranges are flagged with scale = 1000 in the format metadata. When retrieving raw values, be aware that displayed values are commonly in thousands.
- Where the extracted metadata does not include actual calendar strings, use the "Month" column ranges (A47:A341, A380:A574, A611:A804) to retrieve period labels — the calendar values themselves are present in the sheet rows but were not exported in the provided metadata. If concrete start/end calendar dates are required, read the cell values in those A-column ranges in the live workbook.

If you want, I can:
- Produce a concise range map you can feed to a retrieval script (JSON of section → [start_row,end_row,start_col,end_col]) or
- Extract the explicit period strings from A47:A341, A380:A574, A611:A804 if you provide the full cell-value export.