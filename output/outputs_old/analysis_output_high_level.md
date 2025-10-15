## 1. Spreadsheet Overview
- Sheet Name: Fin
- Key Sections Identified:
  - Income Statement
  - Balance Sheet
  - Cash Flow Statement
  - Balance Sheet Support
  - Long Term Liabilities
  - Equity Investment
  - Income Statement Support – Income Taxes
  - FCF/EBITDA Reconciliation

## 2. Detailed Section Analysis

### Income Statement
- Section Type: Custom P&L
- Description & Purpose: Core P&L with subscription metrics, revenue, gross profit, operating expenses by function, EBITDA bridge, below-the-line items, and Net Income. Designed for both monthly and annual reporting.
- Cell Range: A6:FS55
- Time Series Horizon:
  - Dates Location: T3:FS3 (monthly columns), E2:Q2 (annual columns)
  - Date Range: Monthly 2015-01 to 2027-12; Annual 2015 to 2027
  - Frequency: Monthly and Annual
- Key Components:
  - Subscription metrics: ARR, Total ARR, % YoY Growth
  - Revenue and Total Revenue
  - Cost of Sales and Gross Profit (with % Margin)
  - Operating Expenses: Sales & Marketing, G&A, R&D, Capitalized R&D and amortization
  - Intercompany Revenue/(Expenses)
  - D&A, Interest Income/Expense/Net, Other Income/Expenses, Taxes, FX and Consolidation gains/losses
  - Net Income
- Notes & Customizations:
  - Includes ARR tracking and intercompany lines not found in a standard P&L
  - Explicit FX and consolidation impacts
  - Dual calendar: monthly detail and annual summaries

### Balance Sheet
- Section Type: Balance Sheet
- Description & Purpose: Period-end financial position with detailed current assets/liabilities, long-term liabilities, and equity; includes balancing check.
- Cell Range: A57:FS141
- Time Series Horizon:
  - Dates Location: T3:FS3 (monthly columns), E2:Q2 (annual columns)
  - Date Range: Monthly 2015-01 to 2027-12; Annual 2015 to 2027
  - Frequency: Monthly and Annual
- Key Components:
  - Current Assets: Cash, Custody Account, Accounts Receivable with Allowance, Other/Tax/VAT receivables, Prepaids (incl. rent), Deferred Commissions, Deposits
  - Fixed Assets: PP&E, Accumulated Depreciation, Capitalized R&D and related amortization
  - Liabilities: Current (AP, commissions, credit card payable, accrued items, taxes, payroll, deferred revenue/rent) and Long Term (named loan tranches, LOC)
  - Equity: Share capital, preferred, investment from parent, CTA, retained earnings, current year gain/loss
  - Balance check
- Notes & Customizations:
  - Jurisdiction-specific items (VAT, Social Security Deferral)
  - Loan tranches identified by “Tekes” references
  - Explicit “Check” line for balance validation

### Cash Flow Statement
- Section Type: Cash Flow Statement
- Description & Purpose: Indirect cash flow statement with operating working capital detail, investing (capex and capitalized R&D), financing activities including debt/equity flows, and cash reconciliation.
- Cell Range: A143:FS224
- Time Series Horizon:
  - Dates Location: T3:FS3 (monthly columns), E2:Q2 (annual columns)
  - Date Range: Monthly 2015-01 to 2027-12; Annual 2015 to 2027
  - Frequency: Monthly and Annual
- Key Components:
  - CFO: Net income to cash with detailed changes in AR, VAT/other receivables, prepaids, deposits; AP, commissions/bonuses, credit card, payroll/taxes payable, deferred revenue/rent; D&A, amortization, convertible note interest, bad debt
  - CFI: Fixed Assets and Capitalized R&D
  - CFF: Unrealized subsidy, short-term/capital loans, credit institution loans, Tekes tranches, LOC draw/repay, bridge loan, equity items
  - Net change in cash, Cash BoP/EoP
- Notes & Customizations:
  - Extensive working-capital granularity
  - Financing lines mirror named long-term debt tranches and equity movements

### Balance Sheet Support
- Section Type: Supporting Schedules
- Description & Purpose: Detailed support for balance sheet accounts: AR/allowance/DSO, prepaids (including vendor-specific), PP&E depreciation roll-forward, capitalized R&D amortization, accrued commissions/bonuses, operating expense allocation metrics, and related working capital assumptions.
- Cell Range: A228:FS691
- Time Series Horizon:
  - Dates Location: 
    - T3:FS3 (monthly columns for most schedules), E2:Q2 (annual summaries)
    - B282:B572 (vertical monthly dates used in roll-forward schedules)
  - Date Range: 
    - Monthly horizontal: 2015-01 to 2027-12
    - Monthly vertical: 2015-01-31 to 2028-06-30
    - Annual: 2015 to 2027
  - Frequency: Monthly and Annual (mix of horizontal and vertical timelines)
- Key Components:
  - AR/Bookings/DSO: Total Billings, New Business/Upsells/Renewals, DSO, AR %, allowances, days in period
  - Prepaids: FactSet (AMR) prepaid roll-forward (starting, expense, ending)
  - PP&E: Beginning/Added/Ending, Months depreciated, Existing runoff; Capex and Capex % of Revenue
  - Capitalized R&D: Beginning/Added/Ending, Amortization, FX adjustment
  - Accrued Bonuses and Commissions: category-level expenses, paid amounts, start/end accruals, TTM metrics, effective rates, less TTM accruals
  - Current liabilities analytics: AP, CC Payable, Accrued Expenses; DPO; operating expense bases and % of opex
- Notes & Customizations:
  - Mixed timeline orientation: horizontal monthly headers plus vertical monthly date series for roll-forwards
  - Vendor-specific prepaid tracking (e.g., FactSet AMR)
  - Region-specific items (VAT), and detailed commission/bonus mechanics

### Long Term Liabilities
- Section Type: Debt Schedule
- Description & Purpose: Loan-by-loan schedules for long-term debt tranches, including balances, payback/FX effects, interest/admin costs, and total payback.
- Cell Range: A692:FS729
- Time Series Horizon:
  - Dates Location: T3:FS3 (monthly columns)
  - Date Range: Monthly 2015-01 to 2027-12
  - Frequency: Monthly
- Key Components:
  - Tranches: Tekes - 14887, 15118, 14560, 14223, 15543
  - Balance roll-forwards: Starting Balance (Long Term), Payback / FX Fluctuation, Ending Balance
  - Cost lines: Interest Rate, Admin Fee, Total Interest/Admin Expense, Total Payback
- Notes & Customizations:
  - Incorporates FX fluctuation at the tranche level
  - Aligns with cash flow financing activities and balance sheet long-term liabilities

### Equity Investment
- Section Type: Financing Schedule
- Description & Purpose: Equity raise scenarios and revolver/debt availability modeling linked to MRR, multipliers, and retention, with cash flow integration and covenant/availability checks.
- Cell Range: A731:FS789
- Time Series Horizon:
  - Dates Location: T3:FS3 (monthly columns), E2:Q2 (annual columns for scenario summaries)
  - Date Range: Monthly 2015-01 to 2027-12; Annual 2015 to 2027
  - Frequency: Monthly and Annual
- Key Components:
  - Equity Scenarios: Net Investment Amount for Base/Growth/$50mm variants and close timing
  - Debt/Revolver: SVB Debt, MRR, Multiplier, Retention, Total Availability; Beginning/Add/Paid Down/End; Debt Issuance Amortization
  - Liquidity: Minimum Cash Balance, Cash from Ops/Investing/Financing, Change in Cash, Cash BoP/EoP, Cash (Ex- revolver), Revolver Drawn (Y/N), Cash Needed
  - Rates: LIBOR/Interest assumptions, Leverage
- Notes & Customizations:
  - Combines equity timing with an availability-based revolver model driven by subscription metrics
  - Separate early-column inputs for scenario control alongside full monthly projection columns

### Income Statement Support – Income Taxes
- Section Type: Tax Schedule
- Description & Purpose: Tax computation support including NOL utilization, taxable income, tax rate, and taxes paid feeding the P&L and cash flow.
- Cell Range: A791:FS801
- Time Series Horizon:
  - Dates Location: T3:FS3 (monthly columns), E2:Q2 (annual columns)
  - Date Range: Monthly 2015-01 to 2027-12; Annual 2015 to 2027
  - Frequency: Monthly and Annual
- Key Components:
  - Pre-Tax Income
  - NOL roll-forward: Starting NOL, NOL (Use)/Add, Ending NOL
  - Taxable Income, Tax Rate, Taxes Paid
- Notes & Customizations:
  - Explicit NOL tracking at monthly and annual levels
  - Integrates to both the Income Statement (tax expense) and Cash Flow (taxes paid)

### FCF/EBITDA Reconciliation
- Section Type: Key Metrics Table
- Description & Purpose: Analytical bridge from EBITDA to EBIT/NOPAT to Unlevered FCF and Adjusted FCF, including change in NWC and investing cash flows; includes internal checks.
- Cell Range: A803:FS836
- Time Series Horizon:
  - Dates Location: T3:FS3 (monthly columns), E2:Q2 (annual columns)
  - Date Range: Monthly 2015-01 to 2027-12; Annual 2015 to 2027
  - Frequency: Monthly and Annual
- Key Components:
  - FCF and CFO, EBITDA check and delta
  - Add-backs/deductions: D&A, Taxes, Other Income/Expenses, Interest
  - EBIT, NOPAT, Change in NWC, Cash from Investing
  - Unlevered FCF and Adjusted FCF
- Notes & Customizations:
  - Includes a formal “[EBITDA CHECK]” control
  - Provides an investor-friendly unlevered FCF view alongside adjustments