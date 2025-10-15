## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Engineering
- **Key Sections Identified**: 
  - Income Statement

## 2. Detailed Section Analysis

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: This section represents the engineering-focused operating profit-and-loss structure, aggregating revenue, cost of sales, and operating expenses to illustrate gross profit and net expenses for the period. It serves as the primary profitability and cost-structure view for the engineering OpEx scope.
- **Cell Range**: A5:U138
- **Time Series Horizon**:
  - **Dates Location**: C3:U3
  - **Date Range**: 02/28/2019 to 09/30/2019
  - **Frequency**: Monthly
- **Key Components**: Revenue; Cost of Sales; Gross Profit; Expenses (with multi-line subcategories under People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, and Other/Taxes/Interest sections); Other Income; Taxes; Interest Net; Total Expenses
- **Notes & Customizations**:
  - The sheet combines revenue items within an OpEx context, indicating a blended P&L layout rather than a pure separate-revenue view.
  - Numeric cells are stored with a scale of 1000 (values appear in thousands).
  - There are multi-level, indented sub-items under major expense categories, including numerous granular line items (e.g., People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, etc.).
  - A “Year To Date” indicator appears in the header area (B3), and there are formatting artifacts such as duplicate revenue labels, which may reflect layout conventions rather than distinct data blocks.
  - The dictionary-provided date location points to C3:U3 for month-end dates, but the format_ranges data includes the monthly values starting in C4 across the period; interpret accordingly when aligning data retrieval to the exact sheet.