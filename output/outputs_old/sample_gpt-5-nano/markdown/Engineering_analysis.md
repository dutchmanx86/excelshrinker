## 1. Spreadsheet Overview
- **Sheet Name**: Engineering
- **Key Sections Identified**:
  - Engineering Operating Expenses Summary (Custom P&L)

## 2. Detailed Section Analysis

### Engineering Operating Expenses Summary (Custom P&L)
- **Section Type**: Custom P&L
- **Description & Purpose**: A detailed engineering expense breakdown used to analyze operating costs and support the reorganization of expenses around engineering activities. It consolidates wages, benefits, travel, admin, and other costs, with a monthly time series across 2015-01 to 2027-12.
- **Cell Range**: A5:Q396
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: Jan 2015 to Dec 2027
  - **Frequency**: Monthly
- **Key Components**: Major sub-sections include a Total Engineering Expense line, a Total Engineering People Costs line, and an extensive set of engineering cost categories (e.g., Wages, Salaries Working Abroad, Travel, Benefits, Admin & Facility costs, Capitalized components). The structure supports a category-level breakdown alongside an overall engineering expense total.
- **Notes & Customizations**: This is a custom reorganization of expenses focused on engineering; scales many cost figures to thousands (scale: 1000 for I–Q ranges); includes capitalization adjustments (e.g., Capitalized Wages, Capitalized Outsourced R&D, Capitalized R&D) and multiple category-specific lines, enabling a monthly time-series view aligned to the ds_1 monthly date series. Dictionary-driven metrics for allocation (e.g., Headcount, % of Wages, Cost Per Head) are defined across dedicated ranges and referenced for cost attribution, rather than being presented as standalone rows in this primary section.