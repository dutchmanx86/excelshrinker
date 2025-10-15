## 1. Spreadsheet Overview
- **Sheet Name**: Detailed Balance Sheet
- **Key Sections Identified**:
  - Assets
  - Liabilities
  - Equity
  - Check / Validation (balance verification section)

## 2. Detailed Section Analysis

### Assets
- **Section Type**: Balance Sheet
- **Description & Purpose**: Captures the company’s current and long-term resources expected to generate future economic benefits. This section aggregates granular asset lines (e.g., cash, receivables, prepaid items, and fixed assets) to present the total asset position and the breakdown by asset type.
- **Cell Range**: A4:BV32
- **Time Series Horizon**:
  - **Dates Location**: Not explicitly provided in the data; the asset data spans multiple columns (likely multi-period/point-in-time values), but a single explicit date header is not given.
  - **Date Range**: N/A (not specified in the provided data)
  - **Frequency**: One-time snapshot or multi-period (not explicitly defined by dates in the data)
- **Key Components**: 
  - Current Assets (e.g., Cash, Custody Account, Restricted Cash, Accounts Receivable, Allowance for Doubtful Accounts, etc.)
  - Total Current Assets
  - Long Term Assets (e.g., Other Long Term Assets, Total Long Term Assets)
  - Total Assets
- **Notes & Customizations**:
  - The assets side includes a mix of conventional line items and intercompany/adjustment items (e.g., Accumulated Depreciation, Capitalized R&D, Cap R&D Amortization, Total Fixed Assets), with multi-column numeric blocks (scale 1000) indicating a potential multi-period presentation.
  - The range covers both straightforward asset categories and more specialized items such as intercompany accounts and deferred/adjustment items, which is a customization relative to a standard plain-vanilla balance sheet.

---

### Liabilities
- **Section Type**: Balance Sheet
- **Description & Purpose**: Aggregates the company’s obligations to outside parties, including current liabilities and long-term liabilities, to show total liabilities and the financial leverage position.
- **Cell Range**: A34:BV85
- **Time Series Horizon**:
  - **Dates Location**: Not explicitly provided in the data; similar to Assets, multiple period columns are present but no explicit date header is specified.
  - **Date Range**: N/A
  - **Frequency**: One-time snapshot or multi-period (not explicitly defined by dates in the data)
- **Key Components**:
  - Current Liabilities (e.g., Accounts Payable, Commission Payable, Credit Card Payable, VAT Payable, Accrued Expenses, etc.)
  - Total Current Liabilities
  - Long Term Liabilities (e.g., various intercompany loans, credit facilities, other long-term liabilities)
  - Total Long Term Liabilities
  - Total Liabilities
- **Notes & Customizations**:
  - The liabilities section includes extensive intercompany items and loans (Intercompany Current Account 1–5, Intercompany Loan 1–5, Intercompany Custody Account), as well as specialized payables (Taxes Payable, Tax Clearing, Deferred Revenue, Deferred Rent, Unrealized Subsidy).
  - Presence of non-standard line items (e.g., SVB Line of Credit, Tekes notes, and multiple intercompany accounts) reflects a customized consolidation/holding-structure view rather than a simple external-liability focus.

---

### Equity
- **Section Type**: Balance Sheet
- **Description & Purpose**: Represents the owners’ residual interest in the company after liabilities, including share capital, equity-type instruments, and retained earnings. This section aggregates core equity accounts and culminates with Total Equity.
- **Cell Range**: A87:BV98
- **Time Series Horizon**:
  - **Dates Location**: Not explicitly provided; equity values span across multiple columns similar to assets and liabilities, but no explicit date header is shown.
  - **Date Range**: N/A
  - **Frequency**: One-time snapshot or multi-period (not explicitly defined by dates in the data)
- **Key Components**:
  - Total Equity (summary line)
  - Common Stock
  - Preferred Series A
  - Shares In Subsidiary
  - Unrealized Stock Compensation
  - Investments (and related equity positions)
- **Notes & Customizations**:
  - The equity portion includes items typical of a holding/parent structure (e.g., Investments in Subsidiary, Investment From Parent, Cumulative Translation Adjustment) alongside standard equity accounts.
  - The range encompasses the core equity lines up to Total Equity, aligning with the balance-sheet structure that ends with Total Liabilities & Equity.

---

### Check / Validation
- **Section Type**: Balance Sheet – Validation / Balancing
- **Description & Purpose**: Provides a final verification that Total Assets balance with Total Liabilities and Equity; includes a “Check” line that distributes across multiple columns for validation figures.
- **Cell Range**: A101:BV101
- **Time Series Horizon**:
  - **Dates Location**: N/A
  - **Date Range**: N/A
  - **Frequency**: N/A (static validation row)
- **Key Components**: Check line and the per-column validation values used to confirm the balance equation.
- **Notes & Customizations**:
  - The presence of a dedicated Check row across multiple column blocks (F101:AE101, AF101:BB101, BC101:BJ101, BO101:BV101) indicates a structured, per-period or per-criterion validation scheme beyond a simple single-number check.
  - This is a practical enhancement for auditing the integrity of the multi-column balance sheet presentation.

End of document.