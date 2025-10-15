## 1. Spreadsheet Overview
- **Sheet Name**: Operating Expenses
- **Key Sections Identified**:
  - Operating Expenses Detail
  - Revenues

## 2. Detailed Section Analysis

### Operating Expenses Detail
- **Section Type**: Custom P&L
- **Description & Purpose**: This section holds a comprehensive, itemized breakdown of operating costs. It serves as the core expense ledger for monthly cost planning, variance analysis, and margin assessment. The layout combines granular line items (e.g., wages, benefits, marketing, facilities, professional services) with totals and derived metrics to support detailed cost management.
- **Cell Range**: B3:FS231
- **Time Series Horizon**:
  - **Dates Location**: T3:FS3
  - **Date Range**: 2015-01-31 to 2027-12 (monthly sequence)
  - **Frequency**: Monthly
- **Key Components**: Major sub-blocks that define the structure of this section include:
  - Salaries & Wages and related payroll costs (e.g., Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Payroll Taxes, Stock Based Compensation)
  - Other People Costs (e.g., Recruiting Fees, Contractors, Benefits, % of Wages, Wages-related metrics)
  - Administrative & Overhead categories (e.g., General and Administrative, Marketing, Legal, Insurance, Professional Services, Data Feeds, Bank Fees, Audit & Tax, Rent & Occupancy, Utilities, Telecommunications)
  - Facilities & Occupancy (e.g., Facilities Costs, Rent, CAM, Repairs & Maintenance, Utilities, Office/Infrastructure)
  - Marketing & Sales Support (Advertising & Promotion, Marketing Events, Public Relations, Paid Search/Social/Display, Marketing Tech)
  - Data & Miscellaneous (Data Feeds, Fees, Penalties, Miscellaneous, Other Costs)
  - Earnings/Expense totals and derived rows (Total Operating Expenses, % of Wages, Total Headcount, etc.)
  - Income/Offset items (Rental Income, Total Other Costs, Net/Total rows)
- **Notes & Customizations**:
  - The section is a highly granular, custom P&L layout with numerous line items and cross-month data columns (many multi-column ranges such as E/N:Q, T:FS, CJ:FS, etc.).
  - It includes YoY and per-headcount metrics, several “Total” summary rows, and multiple subcategories that extend into later rows (e.g., Stock Based Compensation, Bonuses, Benefits, etc.).
  - Formatting uses scaling (commonly 1000x) for many numeric blocks to represent thousands and to manage large values.
  - A monthly date axis is shared with the rest of the sheet via the ds_1 monthly date series.

---

### Revenues
- **Section Type**: Revenue Block (Standard P&L context)
- **Description & Purpose**: This section records monthly revenues to be used in conjunction with the operating expense data for margin analysis, profitability modeling, and top-line trend assessment. It provides a top-line view synchronized with the expense timeline.
- **Cell Range**: B229:FS231
- **Time Series Horizon**:
  - **Dates Location**: T3:FS3
  - **Date Range**: 2015-01-31 to 2027-12 (monthly sequence)
  - **Frequency**: Monthly
- **Key Components**: Core elements include:
  - Monthly Revenues (header at B229 and corresponding monthly values across E229:Q229, T229:FS229, etc.)
  - Adjacent total/aggregate rows that summarize revenue activity across the time series (e.g., BY231:FS231 as a total segment)
- **Notes & Customizations**:
  - The revenues area is positioned to align with the operating expenses timeline, enabling straightforward calculation of gross and net margins when combined with the expense data.
  - This block leverages the same monthly date axis as the expenses section for consistency in time-series retrieval.