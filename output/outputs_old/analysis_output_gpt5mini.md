## 1. Spreadsheet Overview
- **Sheet Name**: Fin
- **Key Sections Identified**:
  - Income Statement
  - Balance Sheet
  - Cash Flow Statement
  - Balance Sheet Support & Detailed Schedules (AR, Billings, CapEx, Depreciation, Accrued Bonus/Commissions, etc.)
  - Long‑term Liabilities (Tekes schedules, Convertible notes, Bridge Loan)
  - Equity Investment & Financing (Equity tiers, SVB Line, Revolver, Cash waterfall)
  - Income‑Tax / FCF / Valuation Support (NOLs, Taxable Income, FCF, NOPAT, Unlevered FCF, Adjusted FCF)

---

## 2. Detailed Section Analysis

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Consolidated income statement showing historical and projected revenue, cost of sales, gross profit, operating expenses (S&M, G&A, R&D), non‑operating items (interest, FX, other), taxes and net income. Used for profitability analysis, margin trending and as an input to cash flow and valuation schedules.
- **Cell Range**: B6:FS55
- **Time Series Horizon**:
  - **Dates Location**:
    - Historical / annual column headers: E2:Q2 (date series definition ds_2)
    - Forecast / detailed columns: T3:FS3 (date series definition ds_4)
  - **Date Range**:
    - Annual series (E2:Q2 / ds_2): 2015 → 2027
    - Monthly series (T3:FS3 / ds_4): 2015-01 → 2027-12
  - **Frequency**: Mixed — Annual (historical summary columns) + Monthly (forecast/period columns)
- **Key Components**:
  - Total ARR / Total Revenue and Revenue sublines
  - Cost of Sales and Gross Profit
  - Operating expense groups: Sales & Marketing, G&A, Research & Development
  - Non‑operating items: Amortization, Interest Income/Expense, FX Gain/Loss, Other Income/Expenses
  - Bottom line: Taxes and Net Income
- **Notes & Customizations**:
  - Two distinct column blocks: E:Q (annual/historical) and T:FS (granular monthly forecast).
  - Amounts scaled in formatting (values appear scaled by 1,000 in many ranges).
  - Some cells in early rows contain 'na' placeholders; section includes intercompany line and internal “checks”.

---

### Balance Sheet
- **Section Type**: Balance Sheet (statement of financial position)
- **Description & Purpose**: Snapshot of Assets, Liabilities, and Equity across the same historical and forecast periods used in the P&L. Includes current assets (cash, AR, VAT, prepaid items), fixed assets (accumulated depreciation, cap R&D amortization), current liabilities (payables, accrued items), long‑term liabilities and equity breakdown.
- **Cell Range**: B57:FS141
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual column headers: E2:Q2 (ds_2)
    - Monthly/forecast column headers: T3:FS3 (ds_4)
  - **Date Range**:
    - Annual: 2015 → 2027
    - Monthly: 2015-01 → 2027-12
  - **Frequency**: Mixed — Annual + Monthly (matching Income Statement)
- **Key Components**:
  - Current Assets (Cash, Custody Account, AR, VAT Receivable, Prepaid items, Deposits)
  - Fixed Assets and related accumulated depreciation / Cap R&D amortization
  - Current Liabilities (Commission Payable, VAT Payable, Payroll Clearing, Taxes Payable, Short Term Loans, etc.)
  - Long Term Liabilities and Equity (Common stock, Preferred, Retained Earnings, Cumulative Translation)
  - Totals and reconciliation rows (Total Assets; Total Liabilities & Equity; Check)
- **Notes & Customizations**:
  - Column layout mirrors Income Statement: E:Q for annual, T:FS for granular forecast.
  - Several payable / accrued buckets are tracked in detail (commissions, bonus, holiday pay, etc.) to feed working capital schedules elsewhere.

---

### Cash Flow Statement
- **Section Type**: Standard Cash Flow Statement (Indirect / Operating, Investing, Financing)
- **Description & Purpose**: Cash flows from operating, investing and financing activities with detailed movements in working capital and financing lines (draws/repayments, convertible notes, bridge loan, equity flows). Used for cash burn analysis and as an input to the cash waterfall / cash balance monitoring.
- **Cell Range**: B143:FS224
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual column headers: E2:Q2 (ds_2)
    - Monthly/forecast column headers: T3:FS3 (ds_4)
  - **Date Range**:
    - Annual: 2015 → 2027
    - Monthly: 2015-01 → 2027-12
  - **Frequency**: Mixed — Annual + Monthly
- **Key Components**:
  - Net cash from Operating Activities (with detailed decreases/increases in operating assets and liabilities)
  - Cash Flows from Investing (Fixed assets, Capitalized R&D)
  - Cash Flows from Financing (loans, equity contributions, convertible notes, Bridge Loan draws/repayments)
  - Opening and ending cash balances and Net Change in Cash
- **Notes & Customizations**:
  - Operating cash flow section has detailed line items that map directly to the Balance Sheet Support schedules (AR, deferred comps, accrued items).
  - Formatting indicates numbers are scaled by 1,000 in many columns.

---

### Balance Sheet Support & Detailed Schedules
- **Section Type**: Key Metrics / Detailed schedules (supporting Balance Sheet & Cash Flow)
- **Description & Purpose**: Long block of supporting schedules used to derive Balance Sheet and Cash Flow items. Includes billing / bookings decomposition, AR aging / DSO, prepaid schedules, detailed PP&E and depreciation runoffs, CapEx schedules, accrual & bonus/commission workings, web services and CC payable details, and multiple check / reconciliation rows.
- **Cell Range**: B228:FS729
- **Time Series Horizon**:
  - **Dates Location**:
    - Columnar period headers: E2:Q2 (annual columns, ds_2) and T3:FS3 (monthly columns, ds_4)
    - Row-level schedule dates (for detailed PP&E / amortization / running schedules): B282:B572 (date series definition ds_5)
  - **Date Range**:
    - Column headers: Annual 2015 → 2027; Monthly 2015-01 → 2027-12
    - Row-schedule dates (B282:B572 / ds_5): 2015-01-31 → 2028-06-30 (unordered column of 162 dates)
  - **Frequency**: Mixed — Annual + Monthly column series, plus unordered schedule dates for item-level amortization/runoff
- **Key Components**:
  - Total Billings / Billings by New Business / Upsells / Renewals
  - Days Sales Outstanding (DSO) and AR mechanics
  - Operating Expenses ex-headcount, web service COGS, and % of Opex calculations
  - Prepaid schedules (FactSet / AMR), Prepaid expense rollforwards
  - AR, Allowance for Doubtful Accounts adjustments and % of AR
  - PP&E and CapEx schedules, months depreciated, depreciation runoffs and FX adjustments
  - Accrued Bonus & Commissions schedules (start/end accrual positions, bonus paid, commission added/paid), TTM bonus math
  - Detailed columns span both I:Q (near history) and extended CJ:FS (forecast / long horizon)
- **Notes & Customizations**:
  - This area contains both columnar period data and table-like schedules with explicit row dates (ds_5) — consumers must use both column headers (E2/T3) and the B282:B572 row dates depending on the schedule.
  - Many internal mapping columns use non‑contiguous extended columns (CJ:FS) for long‑range forecast; some intermediate columns (I:Q) hold near history.
  - Several internal "na" and check lines exist; extensive use of scaled numeric formatting (values ×1,000).

---

### Long‑term Liabilities (Tekes schedules, Convertible Notes, Bridge Loan)
- **Section Type**: Long-term debt schedule / Waterfall data
- **Description & Purpose**: Detailed schedules for multiple long‑term loans (named Tekes loans with identifiers), convertible notes (including accrued interest), SVB Line, Bridge Loan and related amortization, admin fees, interest and payback totals. Used to model debt balances, interest / admin expense, paybacks and amortization.
- **Cell Range**: B692:FS729
- **Time Series Horizon**:
  - **Dates Location**:
    - Column headers: E2:Q2 (ds_2) and T3:FS3 (ds_4)
  - **Date Range**:
    - Annual: 2015 → 2027
    - Monthly: 2015-01 → 2027-12
  - **Frequency**: Mixed — Annual + Monthly
- **Key Components**:
  - Starting balances, additions and paybacks for each long‑term instrument (Tekes -14887, -15118, -14560, -14223, -15543 and “Other long‑term loans”)
  - Convertible Notes (balance and accrued interest) and Bridge Loan book
  - Admin fee, Total interest/admin expense and total payback rows
- **Notes & Customizations**:
  - The schedule uses both E:Q and U:/T.. blocks to show different segments (starting, added, ending balances) and uses CJ:FS for longer horizon numeric columns.
  - Payback and FX fluctuation adjustments appear in later columns for multi‑period modeling.

---

### Equity Investment & Financing
- **Section Type**: Financing / Investment summary and debt availability
- **Description & Purpose**: Summarizes equity injections (Base/Growth scenarios), new investments (1st/2nd close), SVB debt and line availability, minimum cash policy, cash waterfall (from ops/investing/financing), revolver draws, and drawn/ending balances for debt facilities. Used for funding planning and liquidity analysis.
- **Cell Range**: B731:FS776
- **Time Series Horizon**:
  - **Dates Location**:
    - Column headers: E2:Q2 (ds_2) and T3:FS3 (ds_4)
  - **Date Range**:
    - Annual: 2015 → 2027
    - Monthly: 2015-01 → 2027-12
  - **Frequency**: Mixed — Annual + Monthly
- **Key Components**:
  - Net Investment Amount by scenario (Base $25mm, Growth $25mm, Base $50mm, etc.)
  - Bridge Note, SVB Debt, MRR / Multiplier / Retention and Total Availability calculations
  - Minimum Cash Balance, Cash from Ops/Investing/Financing, Revolver draws (Y/N), Cash Needed
  - Beginning / Add / Paid Down / End lines for debt movements and Debt Issuance Amortization
- **Notes & Customizations**:
  - Extended numeric columns are held in CJ:FS for long horizon; some scalars (e.g., Minimum Cash Balance) in single numeric cells (C759, C760).
  - Section feeds the cash summary/monitor (Cash BoP/EoP and cash excluding revolver).

---

### Income‑Tax, FCF & Valuation Support
- **Section Type**: Income statement support / tax schedule / FCF bridge
- **Description & Purpose**: Tax and NOL schedule, taxable income, tax rate, taxes paid and detailed Free Cash Flow calculations (FCF, CFO adjustments, D&A and other adds/subtracts, EBITDA checks, EBIT, NOPAT, Unlevered FCF and Adjusted FCF). Used for tax accounting, NOL tracking and valuation/unlevered cash flow analysis.
- **Cell Range**: B791:FS836
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual column headers: E2:Q2 (ds_2)
    - Monthly/forecast headers: T3:FS3 (ds_4)
    - Specific taxable / NOL rows map to I795:Q795 and CJ795:FS795 for extended periods (see format ranges)
  - **Date Range**:
    - Annual: 2015 → 2027
    - Monthly: 2015-01 → 2027-12
  - **Frequency**: Mixed — Annual + Monthly
- **Key Components**:
  - Pre‑tax Income, Starting NOL, NOL usage / additions and Ending NOL
  - Taxable Income, Tax Rate and Taxes Paid
  - FCF and FCF bridge lines: CFO, Add: Deltas, Add/remove Other items, Less: D&A and Taxes, EBITDA check and Unlevered FCF
  - Adjusted FCF (after other income/expenses and interest adjustments)
- **Notes & Customizations**:
  - NOL tracking is presented both in near history (I‑columns) and extended horizon (CJ‑columns).
  - FCF derivation is comprehensive and designed to reconcile EBITDA → Unlevered/Adjusted FCF, with check lines for consistency.

---

If you want, I can also:
- produce a compact mapping table (section → exact start/end rows & columns) for programmatic retrieval, or
- extract the specific ranges for a given sub‑item (for example "Accrued Bonus schedule" or "CapEx amortization table") so an automated agent can pull that block.