## 1. Spreadsheet Overview
- **Sheet Name**: Headcount and Salaries CTRL
- **Key Sections Identified**:
  - Headcount Overview
  - Departmental Salary Cost Breakdown

## 2. Detailed Section Analysis

### Headcount Overview
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section aggregates and presents the core headcount metrics used for planning and budgeting. It highlights total headcount and key headcount change deltas (e.g., executive headcount additions) to support staffing forecasts and headcount-driven budgeting.
- **Cell Range**: B11:B66
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6
  - **Date Range**: 2015-01-01 to 2027-01-01
  - **Frequency**: Annual
- **Key Components**: Total Headcount (and its growth drivers), Executive headcount metrics, and period-based headcount changes. This section centers on the top-level staffing footprint and its year-over-year development.
- **Notes & Customizations**: The sheet models headcount with multiple drivers and period-based adjustments (e.g., “Executive Headcount Added in Period”). It uses a mix of baseline and driver-based figures to support scenario analysis.

### Departmental Salary Cost Breakdown
- **Section Type**: Custom Salary Breakdown Table (department/function-level salary data)
- **Description & Purpose**: This section provides a department-level and function-level breakdown of salary costs, including base salaries, driver-based components, and driver-scaled figures across time. It supports granular budgeting and scenario analysis for each major function (engineering, marketing, content, finance/HR/ops, product, etc.), as well as regional considerations (e.g., India).
- **Cell Range**: A17:BX151
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual headers: E6:Q6
    - Repeating annual headers: T6:FS6
    - Monthly headers: T8:FS8
  - **Date Range**:
    - Annual: 2015-01-01 to 2027-01-01
    - Monthly: 2015-01-31 to 2027-12-31
  - **Frequency**: Annual (ds_1 and ds_2), Monthly (ds_3)
- **Key Components**: Departmental blocks such as Engineering, Marketing, Content, Finance/HR/Operations, Product, and Engineering/Ops India. Each block includes salary lines (e.g., base salaries, executive salaries, department-specific driver metrics) and driver-based aggregates (e.g., ARR per engineer, ARR per product, ARR per marketing head, etc.). Major sub-areas include:
  - Engineering and related salary data (including India variant)
  - Marketing salary data
  - Content salary data
  - Finance, HR, and Operations salary data
  - Product salary data
- **Notes & Customizations**: The data include numerous driver-based metrics and scale factors (notably scale: 1000) to convert units to a common thousand-dollar basis. The section reflects a custom cost-build rather than a standard P&L, with many driver-driven lines (e.g., ARR per X Driver) and department-specific salary aggregations. Some blocks also capture regional variations (e.g., India) and headcount additions.