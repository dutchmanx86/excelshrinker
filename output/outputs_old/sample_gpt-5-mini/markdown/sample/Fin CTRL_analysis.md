## 1. Spreadsheet Overview
- **Sheet Name**: Fin CTRL
- **Key Sections Identified**:
  - Sheet header / Time axis (Year / Month / Date series)
  - Balance Sheet Support & Working Capital Assumptions (DSO, Prepaids, A/P, Accruals, Commissions)
  - CapEx & Grant Schedules (CapEx % of Revenue; Tekes grant lines)
  - Payroll & Payroll-related Accruals (Accrued wages, holiday pay, payroll taxes)
  - Taxes, Sales Taxes & Deferred Commissions
  - Interest & Cash Assumptions (interest rates, cash interest, percent cash, LIBOR)
  - Commission & ARR Assumptions (Effective commission rate, Commissions Payable, Deferred/Accrued Commissions, Target Hit Rate)
  - Other Liabilities & KPIs (Credit card payable, Day Sales Outstanding duplicates, other control rows)

---

## 2. Detailed Section Analysis

### Sheet Header / Time Axis
- **Section Type**: Date / Control Header
- **Description & Purpose**: Top-of-sheet header containing company title and the main period axes used by the entire sheet. This includes the Year and Month labels and the primary date series used to drive annual and monthly timelines for the control table below.
- **Cell Range**: B1:FS8
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual column headers (primary annual axis): E6:Q6 (date series ds_1)
    - Extended/repeating annual axis: T6:FS6 (date series ds_2)
    - Monthly axis: T8:FS8 (date series ds_3)
  - **Date Range**:
    - ds_1 (E6:Q6) — Annual series from 2015 to 2027 (start 2015)
    - ds_2 (T6:FS6) — Repeating annual pattern from 2015 to 2027 (annual values repeated across columns)
    - ds_3 (T8:FS8) — Monthly series covering 2015-01 to 2027-12
  - **Frequency**: Annual (E6:Q6, T6:FS6) and Monthly (T8:FS8)
- **Key Components**:
  - Company title and sheet descriptor (B1:B3)
  - "Year" and "Month" row labels (B6:B7)
  - Three date series (annual primary, repeating annual, monthly)
- **Notes & Customizations**:
  - Three distinct date series drive the sheet: a yearly series, a repeating-annual block, and a full monthly timeline. Future retrievals must pick the correct date series (E6:Q6 vs T6:FS6 vs T8:FS8) depending on whether a row is annual or monthly.

---

### Balance Sheet Support & Working Capital Assumptions
- **Section Type**: Balance Sheet Support / Working Capital Assumptions Table
- **Description & Purpose**: Control block defining receivables/payables timing and working capital drivers used to build balance sheet schedules (e.g., Days Sales Outstanding, Prepaid Expenses as % of OpEx, Accounts Payable DPO, Accrued Expenses). These are the inputs used to generate the detailed balance-sheet line-items in downstream models.
- **Cell Range**: B11:FS59
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (primary annual), T6:FS6 (extended annual) — rows in this block use the sheet's annual and extended annual axes; some rows also reference monthly blocks where appropriate.
  - **Date Range**: 2015 to 2027 (annual blocks); monthly values (if present for a specific sub-row) use 2015-01 to 2027-12
  - **Frequency**: Primarily Annual (with some inputs organized at monthly granularity in repeating blocks)
- **Key Components**:
  - Days Sales Outstanding and related receivables controls
  - Prepaid Expenses (Monthly % of Operating Expenses)
  - Accounts Payable / Days Payable Outstanding controls
  - Accrued Expenses and Commissions payables (% of ARR)
- **Notes & Customizations**:
  - Numeric blocks in this area appear in both the E:Q (primary annual) and the T:FS (extended/repeating) column groups. Several numeric rows are scaled by 1,000 (thousands), so retrieval routines must honor the scale attribute for values within J..Q and BX..CA blocks listed in the sheet metadata.

---

### Capital Expenditures & Grant Schedules
- **Section Type**: CapEx Schedule & Grant / Subsidy Lines
- **Description & Purpose**: Controls for capital expenditure assumptions (CapEx as % of revenue) and dedicated grant/subsidy lines (multiple "Tekes - ####" entries). These lines provide timing and absolute values for CapEx and grant inflows/offsets.
- **Cell Range**: B25:B31 is the CapEx label row region; for a single contiguous logical block including CapEx and all Tekes grant lines: B27:FS136
  - (Consolidated range to include CapEx at row 27 and Tekes grant lines at rows 104–132)
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (primary annual) and T6:FS6 (extended/repeating); individual grant line data appear across E..Q and BX..FS blocks
  - **Date Range**: 2015 to 2027 (annual blocks)
  - **Frequency**: Annual (with repeating/extended column blocks for multi-period schedules)
- **Key Components**:
  - Capital Expenditures as a percentage of revenue (drivers and resulting absolute CapEx)
  - Multiple Tekes grant lines (Tekes - 14887, Tekes - 15118, Tekes - 14560, Tekes - 14223, Tekes - 15543 — each has its own timing block)
- **Notes & Customizations**:
  - Grant lines are structured as individual schedule rows, some of which populate values in more distant column blocks (BX:FS). Several grant rows are stored/scaled in thousands (scale = 1,000). Treat Tekes lines as distinct funding items rather than operating revenue.

---

### Payroll & Payroll-related Accruals
- **Section Type**: Payroll Accruals / Labor-related Liabilities
- **Description & Purpose**: Inputs controlling payroll-linked liabilities and growth assumptions — accrued wages (growth), accrued holiday pay (as % of wages), payroll taxes (growth), and related timing. These feed payroll liability balances on the balance sheet.
- **Cell Range**: B62:FS87
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (primary annual) and T6:FS6 (extended/repeating); some rows include explicit monthly blocks U:BW.. and other non-contiguous monthly columns referenced in metadata (for long repeating series).
  - **Date Range**: 2015 to 2027 (annual); monthly sub-series exist within 2015-01 to 2027-12 where marked
  - **Frequency**: Annual primary; some inputs use monthly repeating blocks
- **Key Components**:
  - Accrued wages growth assumptions
  - Accrued holiday pay (% of wages)
  - Payroll taxes payable (growth assumptions and timing)
- **Notes & Customizations**:
  - Several payroll-related cells are flagged "na" at certain anchor columns (e.g., E62, T62, E83, T83) — these indicate intentionally blank/not-applicable anchors and a pattern where the repeating series populates a later block (U:BW, CB, CN, etc.). Retrieval logic must account for these sparse, repeating blocks.

---

### Taxes, Sales Taxes & Deferred Commissions
- **Section Type**: Tax & Deferred Liability Controls
- **Description & Purpose**: Controls for sales taxes payable (as % of revenue), deferred commissions growth, and the timing/amounts for deferred commission recognition. Used to compute sales tax liabilities and deferred commission balances over time.
- **Cell Range**: B90:FS101
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (primary annual) and T6:FS6 (extended/repeating); deferred commission rows also populate BX:FS blocks for long horizons
  - **Date Range**: 2015 to 2027 (annual blocks)
  - **Frequency**: Annual
- **Key Components**:
  - Sales Taxes Payable (% of Revenue)
  - Deferred Commissions Growth and the associated deferred commission schedules
- **Notes & Customizations**:
  - Deferred commission schedules populate both standard annual blocks (I..Q) and extended blocks (BX..FS). Some rows in this area are scaled (thousands).

---

### Interest & Cash Assumptions
- **Section Type**: Interest Rate Schedule & Cash Assumptions
- **Description & Purpose**: Inputs for interest rate assumptions (base rates and admin fee), interest on cash account, percent of cash held in the account, plus LIBOR. These drive interest income/expense calculations and cash interest flows applied to the balance sheet model.
- **Cell Range**: B139:FS166
- **Time Series Horizon**:
  - **Dates Location**: I139:Q139 / T139:FS139 (interest rate values are provided across the same annual/extended axes); percent-of-cash and cash-interest rows follow the same column pattern
  - **Date Range**: 2015 to 2027 (annual blocks)
  - **Frequency**: Annual (with repeating/extended blocks where present)
- **Key Components**:
  - Interest Rate (base)
  - Interest Rate - Admin Fee
  - Interest on Cash Account (rate and absolute values)
  - Percent of Cash in Account (apportionment)
  - LIBOR (separate control row)
- **Notes & Customizations**:
  - Some interest-related numeric rows are represented in thousands. LIBOR and other reference rates are listed as explicit control rows and use the same annual/extended timeline as the rest of the sheet.

---

### Commission & ARR Assumptions
- **Section Type**: Commission Schedule / ARR-linked Assumptions
- **Description & Purpose**: Controls that define effective commission rates, commissions payable as a percent of ARR, deferred and accrued commission schedules, and target hit rates used to model sales commissions and commission liabilities over time.
- **Cell Range**: B41:FS66 (primary commission controls) and B97:FS105 (deferred commission growth and related rows)
  - For consolidated retrieval: B41:FS105 (this includes the main commissions block and the deferred commissions block)
- **Time Series Horizon**:
  - **Dates Location**: BX41:FS41 and BX42:FS45 (commission payables and related accrual/absolute rows use the BX:FS extended column block in metadata), plus E..Q and T..FS for rates
  - **Date Range**: 2015 to 2027 (annual/repeating annual); extended blocks for long-horizon commission amortization
  - **Frequency**: Annual (commission rates) and multi-period amortization mapping across extended blocks
- **Key Components**:
  - Commissions Payable (% of ARR)
  - Accrued Commissions (% of ARR) and Accrued Commissions absolute schedule
  - Deferred Commissions Growth and deferred recognition schedules
  - Effective Commission Rate (driver row)
  - Target Hit Rate for accrued commission recognition
- **Notes & Customizations**:
  - Commission schedules are split across standard (E:Q / I:Q) and extended (BX:FS) column blocks — the BX..FS block holds multi-period amortization/recognition values. Several commission rows are scaled (thousands).

---

### Other Liabilities & KPIs
- **Section Type**: Misc Liabilities & Key Metric Controls
- **Description & Purpose**: Miscellaneous control rows that feed smaller liability categories and KPI controls used by downstream statements: duplicate Day Sales Outstanding entries (for different contexts), Credit Card Payable (% of OpEx), Target Hit Rates, and LIBOR lines. These are final control lines that cover residual items not grouped earlier.
- **Cell Range**: B166:FS188
- **Time Series Horizon**:
  - **Dates Location**: I166:Q166 / E166:Q166 and T166:FS166 for extended columns as applicable
  - **Date Range**: 2015 to 2027
  - **Frequency**: Annual (with repeating periods in extended column blocks)
- **Key Components**:
  - Day Sales Outstanding (a second DSO row used in a different part of the model)
  - Credit Card Payable (% of OpEx)
  - Target Hit Rate - Accrued Commission
  - LIBOR and related short-term rate rows
- **Notes & Customizations**:
  - The sheet contains duplicate or parallel KPI lines (e.g., two DSO control rows at B13 and B166). Ensure retrieval logic references the correct row for the intended model (working capital vs KPI context).

---

Notes common to the sheet
- Scenario indicator / control: B3 contains "1 - Base - $25mm" (sheet-level scenario selector). Repeated strings such as "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)" appear in multiple rows (referenced in the sheet index) and are used as labels across many rows (see metadata inverted index).
- Multiple column blocks: The sheet uses at least three distinct date/column blocks (E:Q, T:FS, and extended BX:FS/other sparse blocks) for different purposes: primary annual axes, repeating annual blocks, and long-run amortization/recognition blocks. Retrieval logic must map a given row to the correct date block(s).
- Scaling: Numerous numeric ranges are flagged with scale = 1,000 (thousands) in the sheet metadata (notably many J..Q and BX..FS ranges). Honor these scales when extracting absolute dollar values.
- Sparsity & "na" flags: Some anchor cells are intentionally "na" (e.g., E62, T62, E83, T83). In those cases the repeating series begins in a different column block (U:BW, CB, CN, CZ, etc.). Extraction routines should detect these anchor "na" values and then read from the populated repeating blocks.

If you want, I can produce a simple index mapping each labeled row (B11, B13, B20, B27, etc.) to its exact row number and the preferred date column block (E6:Q6, T6:FS6, or T8:FS8) for automated extraction.