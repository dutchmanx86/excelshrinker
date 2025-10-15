## 1. Spreadsheet Overview
- **Sheet Name**: Salary Support
- **Key Sections Identified**: Salary Allocation Data Grid (Department-by-role monthly salary costs and staffing data)

## 2. Detailed Section Analysis

### Salary Support Data Grid
- **Section Type**: Custom Salary/Headcount Data Table
- **Description & Purpose**: This section represents the monthly salary costs and staffing data allocated by department and role. It serves as the core budgeting and headcount planning matrix, enabling workforce cost modeling, scenario analysis, and alignment with department-level budget assumptions. The data is structured to support monthly time series (two aligned date axes) and is scaled to thousands for readability.
- **Cell Range**: A1:BM86
- **Time Series Horizon**:
  - **Dates Location**: D1:CI1 (ds_1) and CY1:GD1 (ds_2)
  - **Date Range**:
    - ds_1: 2015-01 to 2021-12
    - ds_2: 2021-01 to 2027-12
    - Overall span: 2015-01 through 2027-12
  - **Frequency**: Monthly
- **Key Components**: 
  - Department headers (e.g., R&D, G&A, Mktg, Finance & Admin, Product, Sales- or Ops-related groupings)
  - Role/Staffing labels (e.g., Account Manager, Account Executive, SDR, CS Manager, etc.)
  - Salary data blocks (monthly amounts) scaled by 1,000
  - Budget reference (e.g., "2020 Budget" present at BW2)
  - Department-specific salary matrices across two date axes
- **Notes & Customizations**:
  - Data are labeled and scaled in thousands (e.g., 1000x values)
  - The sheet combines two monthly date series to cover a long horizon (2015-01 to 2027-12) within the same grid
  - There is a mixture of department-level headers (e.g., R&D, G&A, Mktg) and a detailed roster of roles with associated salary blocks
  - A separate FX Rate region appears in the sheet (e.g., FX RATE) and a budgeting reference, which may be used alongside the salary data for currency adjustments and scenario modeling, though these are not part of the primary salary grid’s rectangular range
  - The section serves as a foundation for budgetary planning and headcount cost allocation across departments and roles

Notes:
- The dictionary-like mapping in the inverted_index includes department and role references (e.g., “R&D,” “G&A,” “Mktg,” “Account Manager,” “Account Executive,” “SDR,” “Sales Operations Manager,” etc.). These values are actual strings in the sheet and align with the labels used within the Salary Support grid.
- The data are organized to support retrieval by the defined two monthly date series, with the primary date labels located in D1:CI1 and CY1:GD1, enabling time-series-driven queries across the 2015–2027 horizon.