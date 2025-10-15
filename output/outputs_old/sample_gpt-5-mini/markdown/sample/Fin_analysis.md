## 1. Spreadsheet Overview
- **Sheet Name**: Fin
- **Key Sections Identified**:
  - Income Statement
  - Balance Sheet
  - Cash Flow Statement
  - Balance Sheet Support (detailed schedules: Billings, DSO, AR, Prepaids, etc.)
  - Fixed Assets & Capex Schedule (PPE, depreciation / amortization schedules)
  - Accrued Bonus & Commission Schedules
  - Long‑Term Liabilities (Tekes lines, Bridge Loan, interest/admin)
  - Equity Investment (investment scenarios / closes)
  - Debt & Cash Forecast (Revolver, minimum cash, availability)
  - KPI / Operational Metrics (ARR, Total Bookings, Total Billings, MRR, DSO)
  - Income Tax & NOL Schedule
  - FCF & Cash Metrics (EBITDA check, CFO, NOPAT, Unlevered FCF)

---

## 2. Detailed Section Analysis

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Consolidated income statement showing revenue (ARR / Total Revenue), cost of sales, gross profit, operating expenses (Sales & Marketing, G&A, R&D), D&A, interest, other income/expense, taxes and bottom‑line metrics (EBITDA, Net Income). Used for historical / forecast profit and loss analysis and driver inputs for cash flow and valuation.
- **Cell Range**: A6:FS55
- **Time Series Horizon**:
  - **Dates Location**: E2:Q2 (annual columns) and T3:FS3 (monthly columns)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly: 2015-01 → 2027-12
  - **Frequency**: Annual (E..Q) and Monthly (T..FS). (Quarterly headers exist elsewhere if required: AF2:DW2)
- **Key Components**:
  - Revenue lines (Total ARR, Total Revenue)
  - Cost of Sales and Gross Profit
  - Operating expense split: Sales & Marketing, General & Administrative, Research & Development
  - Depreciation / Amortization, Interest Net, Taxes
  - EBITDA and Net Income / EBITDA check
- **Notes & Customizations**:
  - Numbers are presented in thousands (scale = 1,000).
  - Both historical annual columns and a monthly forecast band are present.
  - Some cells marked "na" / placeholders for specific columns.
  - Capitalized R&D and intercompany adjustments are explicit lines (non‑standard P&L detail).

---

### Balance Sheet
- **Section Type**: Balance Sheet (Standard)
- **Description & Purpose**: Full balance sheet with current assets (cash, AR, VAT receivable, prepaids), fixed assets (accumulated depreciation, capitalized R&D amortization), current & long‑term liabilities (payables, deferred revenue, loans), and equity (common stock, preferred, retained earnings). Used for position reporting and supporting cash flow / working capital analysis.
- **Cell Range**: A57:FS141
- **Time Series Horizon**:
  - **Dates Location**: E2:Q2 (annual columns) and T3:FS3 (monthly columns)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly: 2015-01 → 2027-12
  - **Frequency**: Annual and Monthly
- **Key Components**:
  - Current assets (Cash, Custody Account, AR, Prepaid Rent, Deposits)
  - Fixed assets net of Accumulated Depreciation and Cap R&D amortization
  - Current liabilities (Commission Payable, VAT Payable, Payroll Clearing, Taxes Payable, Short Term Loans)
  - Long‑term liabilities & total equity (loan lines, convertible notes, retained earnings)
- **Notes & Customizations**:
  - Multiple column blocks across E:Q, T:FS and additional wide columns (CJ..FS) for extended forecasts.
  - Detailed sub‑accounts for accruals and commissions that feed the cash flow support.

---

### Cash Flow Statement
- **Section Type**: Standard Cash Flow Statement (Indirect)
- **Description & Purpose**: Cash flows from Operating, Investing and Financing activities with detailed changes in working capital lines, capex and cap R&D, loan draws/repayments, equity flows and reconciliation to period opening/closing cash. Used for liquidity forecasting and covenant monitoring.
- **Cell Range**: A143:FS224
- **Time Series Horizon**:
  - **Dates Location**: E147:Q147 (annual/historical band) and T147:FS147 (monthly forecast band)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly: 2015-01 → 2027-12
  - **Frequency**: Annual and Monthly
- **Key Components**:
  - Cash Flows from Operating Activities (adjustments for D&A, changes in AR/AP, accrued items)
  - Cash Flows from Investing Activities (Fixed Assets, Capitalized R&D)
  - Cash Flows from Financing Activities (subsidy, loans, SVB line draws/repayments, equity)
  - Cash, beginning and end of period
- **Notes & Customizations**:
  - Convertible note interest, bridge loan and SVB flows appear in financing.
  - Numbers scaled to thousands.
  - Financing section contains both draw and repayment lines (separate columns for first/second closes).

---

### Balance Sheet Support (Billings, DSO, AR, Prepaids, Operating Expense analytics)
- **Section Type**: Key Metrics Table / Supporting Schedules
- **Description & Purpose**: Detailed operational support and roll‑forwards that reconcile P&L to balance sheet — includes total billings, new business / upsells / renewals, days sales outstanding (DSO) schedule, AR rollforwards, operating expense ex‑headcount/bad debt/cap R&D, prepaid schedules and FactSet AMR prepaid detail. Used to drive working capital and cash flow lines.
- **Cell Range**: B228:FS326
- **Time Series Horizon**:
  - **Dates Location**: E234:Q234 (annual/historical band) and T234:FS234 (monthly forecast band)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly: 2015-01 → 2027-12 (support schedules also use extended columns for multi‑period roll‑forwards)
  - **Frequency**: Annual and Monthly (some detailed schedules use an unordered column series for multi-year amortization)
- **Key Components**:
  - Total Billings / New Business / Upsells / Renewals
  - Days Sales Outstanding (DSO) and AR (% of AR) metrics and roll‑forwards
  - Operating Expense (Less Headcount/Bad Debt/Cap. R&D) and % of Opex calculations
  - Prepaid schedules and FactSet AMR prepaid tracking (start / expense / ending)
- **Notes & Customizations**:
  - Some schedules use extended, non‑standard column blocks (wide forecast horizon across CJ..FS and BP..FS).
  - There is a dedicated unordered column date series used for long amortization tables (see Fixed Assets schedule).

---

### Fixed Assets & Capex Schedule (PPE, Depreciation, Amortization)
- **Section Type**: Balance Sheet Support / Amortization Schedule
- **Description & Purpose**: Property, Plant & Equipment roll forwards, capex lines, depreciation / amortization schedules, cap R&D amortization and FX/FX adjustments. Used to derive fixed asset balances and D&A flows for P&L and cash flow.
- **Cell Range**: B268:FS307
- **Time Series Horizon**:
  - **Dates Location**: I270:Q270 (annual band for this schedule) and CJ270:FS270 (extended forecast columns)
  - **Date Range**: Annual: 2015 → 2027 ; Extended forecast columns align to same monthly/extended pattern (some amortization tables use an unordered column series ending 2028-06)
  - **Frequency**: Annual and Monthly / multi‑period amortization (unordered columns for schedule)
- **Key Components**:
  - PPE opening, additions, disposals, and depreciated amounts
  - Months depreciated / % depreciated patterns and FX adjustments
  - Capex totals and Capex as % of Revenue
- **Notes & Customizations**:
  - Large multi‑column amortization tables extend far into the sheet (many per‑month/per‑asset columns).
  - Some fields reference date series ds_5 (unordered columns) for multi‑year asset schedules.

---

### Accrued Bonus & Commission Schedules
- **Section Type**: Supporting Schedule / Accrual Roll‑forwards
- **Description & Purpose**: Full detail for accrued bonus and commission calculations: start balances, bonus expense by function, bonus paid, commission added, commission paid, and accrued start/end roll‑forwards. These feed current liabilities and cash flow (bonus & commission cash payments).
- **Cell Range**: B610:FS666
- **Time Series Horizon**:
  - **Dates Location**: I613:Q613 (annual/historical band) and BP613:FS613 (forecast / extended band)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly/Extended: monthly forecast columns to 2027 (extended columns used for multi‑period accrual)
  - **Frequency**: Annual and Monthly / extended forecast columns
- **Key Components**:
  - Total Bonus Expense and its split (Sales, Engineering, Other)
  - Bonus paid (Engineering / Other) and actuals adjustments
  - Commission added, commission paid and accrued commissions (start / end)
  - TTM bonus expense and %TTM metrics
- **Notes & Customizations**:
  - Very granular, distributed across multiple non‑contiguous column blocks (I..Q, BP..FS, CJ..FS).
  - Many interim helper columns and multi‑period cumulative calculations are present.

---

### Long‑Term Liabilities
- **Section Type**: Long‑Term Debt Schedule / Liability Roll‑forwards
- **Description & Purpose**: Multi‑line roll‑forwards for long‑term loans (Tekes lines by ID), convertible notes, bridge loans and related interest/admin fees; tracks Starting Balance / Added / Ending Balance and payback schedules. Used to compute interest, amortization and cash flows relating to long‑term debt.
- **Cell Range**: B692:FS729
- **Time Series Horizon**:
  - **Dates Location**: E696:Q696 (annual/historical band) and T696:FS696 (monthly forecast band)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly: 2015-01 → 2027-12
  - **Frequency**: Annual and Monthly
- **Key Components**:
  - Individual Tekes loan lines (14887, 15118, 14560, 14223, 15543)
  - Starting balance / added / ending balance roll‑forwards
  - Admin fee, interest/admin expense, total payback
- **Notes & Customizations**:
  - Payback / FX fluctuation lines exist for multiple loans (special adjustments).
  - Debt issuance amortization appears in adjacent columns.

---

### Equity Investment (Investment Scenarios & Closes)
- **Section Type**: Investment / Funding Assumptions Table
- **Description & Purpose**: Scenario table for investment sizes (Base $25mm, Growth $25mm, Base $50mm, Bridge Note and 1st/2nd close) and net investment amounts — used to model financing inflows and produce cash from financing activities.
- **Cell Range**: B731:FS745
- **Time Series Horizon**:
  - **Dates Location**: C735 (single net investment amount) and E735:Q735 / T735:FS735 (detail columns)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly: 2015-01 → 2027-12 (where detailed columns used)
  - **Frequency**: One‑time inputs (C column) and multi‑period forecast columns (E..Q, T..FS)
- **Key Components**:
  - Named investment scenarios and Net Investment Amount
  - Investment timing / multi‑close amounts
- **Notes & Customizations**:
  - Some inputs are one‑cell inputs (C column) used to seed cash flow scenarios.

---

### Debt & Cash Forecast (Revolver, Minimum Cash, Availability)
- **Section Type**: Liquidity / Debt Facility Model
- **Description & Purpose**: Tracks SVB availability / MRR multiplier, revolver drawings, minimum cash buffer, beginning/add/paid down/end balances for debt, revolver drawn flags, and cash (excluding revolver). Used for liquidity management and covenant checks.
- **Cell Range**: B755:FS779
- **Time Series Horizon**:
  - **Dates Location**: CJ755:FS755 (debt availability band) and T779:FS779 (end balances)
  - **Date Range**: Monthly forecast band primarily to 2027 (columns CJ..FS align with the sheet's extended monthly horizon)
  - **Frequency**: Monthly (forecast) with some single inputs (C759 etc.)
- **Key Components**:
  - SVB debt availability, MRR multiplier and retention assumptions
  - Minimum cash balance and computed Cash Needed / Revolver Drawn (Y/N)
  - Debt beginning / added / paid down / end roll‑forwards and debt issuance amortization
- **Notes & Customizations**:
  - Several wide column blocks (CJ..FS) used for the liquidity horizon (multiple months).
  - LIBOR and interest inputs exist nearby for interest calculation (LIBOR lines).

---

### KPI / Top‑level Operational Metrics (ARR / Revenue)
- **Section Type**: KPI Summary Table
- **Description & Purpose**: Top‑of‑sheet KPIs used for quick review and to drive the model (Total ARR, Total Revenue, % YoY Growth, margins). Primary KPI band at the top of the sheet for quick reference.
- **Cell Range**: B8:FS20
- **Time Series Horizon**:
  - **Dates Location**: E2:Q2 (annual KPI band) and T3:FS3 (monthly KPI band for rolling metrics)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly: 2015-01 → 2027-12
  - **Frequency**: Annual and Monthly
- **Key Components**:
  - Total ARR, Revenue, % YoY Growth, % Margin
- **Notes & Customizations**:
  - ARR and Revenue lines feed downstream P&L and KPI calculations.
  - KPI figures are scaled to thousands.

---

### Operational Metrics — Billings, DSO, MRR & Availability (separate retrieval blocks)
- **Section Type**: KPI / Operational Metrics (detailed)
- **Description & Purpose**: Additional operational KPI blocks used throughout the sheet:
  - Billings / DSO (supporting working capital),
  - MRR and revolver availability (debt capacity),
  - Total Bookings and related billings breakdowns.
  These are located in the Balance Sheet Support area and separate MRR block.
- **Cell Ranges for retrieval**:
  - Total Billings / DSO block: B236:FS242
  - MRR / Debt availability block: B749:FS756
- **Time Series Horizon**:
  - **Dates Location**: E237:L237 and T237:FS237 (Billings) ; CJ749:FS749 (MRR / availability)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly: 2015-01 → 2027-12
  - **Frequency**: Annual and Monthly
- **Key Components**:
  - Billings split (New Business, Upsells, Renewals), Days Sales Outstanding (DSO)
  - MRR, retention and availability multipliers for debt facility
- **Notes & Customizations**:
  - These KPI clusters are spatially separate from the top KPI band — retrieve using the specific ranges above.

---

### Income Tax & NOL Schedule
- **Section Type**: Tax Support Schedule
- **Description & Purpose**: Tracks pre‑tax income, starting NOL, NOL use/add, ending NOL, taxable income, tax rate and taxes paid. Used to compute taxes paid and deferred tax impacts for cash flow and NOPAT.
- **Cell Range**: B791:FS801
- **Time Series Horizon**:
  - **Dates Location**: E793:Q793 (pre‑tax band) and T793:FS793 (forecast)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly forecast columns where present
  - **Frequency**: Annual (primarily) and Monthly (where applied)
- **Key Components**:
  - Starting/ending NOL, NOL usage adjustments
  - Taxable income, tax rate input, taxes paid
- **Notes & Customizations**:
  - NOL amounts appear both in narrow annual columns and extended forecast columns (CJ..FS for longer horizon).

---

### FCF & Cash Metrics (EBITDA check, NOPAT, Unlevered FCF)
- **Section Type**: Key Metrics Table / Valuation Inputs
- **Description & Purpose**: Consolidated calculation of FCF, CFO, adjustments (interest, taxes, other income/expenses), EBITDA check, EBIT, NOPAT, Unlevered FCF and Adjusted FCF used for valuation and cash generation analysis.
- **Cell Range**: B803:FS836
- **Time Series Horizon**:
  - **Dates Location**: E805:Q805 (FCF / CFO historic band) and T805:FS805 (monthly forecast)
  - **Date Range**: Annual: 2015 → 2027 ; Monthly: 2015-01 → 2027-12
  - **Frequency**: Annual and Monthly
- **Key Components**:
  - FCF, CFO, Add/Deltas, EBITDA check and NOPAT
  - Less: Cash from Investing, Change in NWC to compute Unlevered FCF
  - Adjusted FCF after adding/subtracting other income/expenses
- **Notes & Customizations**:
  - Contains cross‑checks (EBITDA CHECK / Delta) and ties back to P&L and cash flow sections.

---

Notes for a future retrieval AI:
- Many numeric ranges are scaled to thousands (scale=1000) — convert as needed when ingesting.
- The sheet uses multiple date series:
  - E2:Q2 and similar E:Q blocks = annual series (ds_2: 2015 → 2027).
  - AF2:DW2 etc = quarterly where present (ds_3).
  - T3:FS3 and CJ..FS column blocks = monthly forecast series (ds_4: 2015-01 → 2027-12).
  - Some large amortization/support schedules use an unordered column series (ds_5) spanning many months (2015-01-31 → 2028-06-30).
- When programmatically extracting a section, use the exact cell ranges listed under each section. Several sections span both narrow historical columns (E:Q) and a wide monthly forecast band (T:FS and other wide blocks); include both blocks by using the full horizontal span provided in the "Cell Range" to avoid missing forecast columns.