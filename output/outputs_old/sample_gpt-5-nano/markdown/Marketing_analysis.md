## 1. Spreadsheet Overview
- **Sheet Name**: Marketing
- **Key Sections Identified**: Marketing Operating Expenses Summary (Detailed Cost Breakdown for Marketing)

## 2. Detailed Section Analysis

### Marketing Operating Expenses Summary
- **Section Type**: `Custom P&L`
- **Description & Purpose**: A comprehensive, user-defined profit-and-loss style layout for the Marketing department, breaking out wage-related costs, benefits, outsourcing, travel, office & admin expenses, and other marketing-specific cost centers. The section is designed to track monthly operating expenditures for budgeting, forecasting, and cost control within the Marketing function.
- **Cell Range**: `A5:Q384`
- **Time Series Horizon**:
  - **Dates Location**: `T2:FS2`
  - **Date Range**: January 2015 to December 2027 (monthly series)
  - **Frequency**: `Monthly`
- **Key Components**: The section is organized around major cost clusters rather than a single label, including:
  - Overall Marketing expense and sub-totals (e.g., "Total Marketing Expense," "Total Marketing People Costs")
  - Employee-related costs (Wages, Marketing Wages, Salaries Working Abroad, Holiday Pay, Sick Leave, Benefits, Payroll Taxes, Share Based Compensation, Recruiting Fees)
  - Outsourced and capitalized items (Outsourced R&D, Capitalized Wages, Capitalized Outsourced R&D, Marketing Capitalized R&D)
  - Travel and related costs (Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, etc.)
  - General & Admin and support costs (Phone, Internet, Home Office, Memberships, Subscriptions, Postage, Conferences, Office Supplies, IT/Software, Utilities, Bank Fees, Professional Services, Insurance, etc.)
  - Other marketing-specific line items (Total Marketing Other Costs, Marketing General & Admin, Public Relations, Advertising & Promotion, etc.)
  - Grouping headers and base-case context (e.g., "1 - Base - $25mm" and separators marked by "x" rows)
- **Date Series Context & Ranges**:
  - **Time Series Horizon Details**: The data is aligned to a monthly date axis defined by the ds_1 series (Monthly, 1 month increment) with a start date of 2015-01-31 and a pattern spanning 2015-01 to 2027-12.
  - **Dates Location**: `T2:FS2`
  - **Date Range**: January 2015 – December 2027
  - **Frequency**: `Monthly`
- **Notes & Customizations**:
  - The layout uses a broad, highly granular breakdown of Marketing-related expenses, with many rows scaled by 1000 (i.e., values presented in thousands).
  - Includes explicit base-case labeling and internal grouping markers (e.g., "1 - Base - $25mm" and various "x" markers) indicating scenario planning or segment separation.
  - Some line items appear to be labeled with marketing-specific contexts (e.g., "Marketing Recruiting Fees," "Marketing Relocation," "Marketing Benefits," "Marketing Capitalized R&D") suggesting a non-standard, department-specific P&L structure.
- **Dictionary-Resolved Context (Key KPI References)**:
  - The workbook includes KPI-like references documented in the dictionary section, which define additional metrics used in or around this data. Examples of such strings include:
    - "% of Wages" 
    - "Headcount"
    - "Cost Per Head"
    - "2-Mo Lead Bookings"
    - "$ Spend to 2-Mo Lead Bookings"
  - These terms are mapped to various cell ranges in the inverted index (e.g., "% of Wages" ranges: B17, B22, B26, B32, B38, B42, B46, B50; "Headcount" and "Cost Per Head" map to multiple B-column ranges). They represent KPI anchors that could be used to derive efficiency or headcount-related metrics from the Marketing expense data.
-