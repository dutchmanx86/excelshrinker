## 1. Spreadsheet Overview
- **Sheet Name**: Bonus Support (Sales non Ops)
- **Key Sections Identified**:
  - Compensation Data Grid
  - Bonus Components & Payouts
  - Bonus Attainment Metrics
  - Time Series Definitions

## 2. Detailed Section Analysis

### Compensation Data Grid
- **Section Type**: Custom P&L
- **Description & Purpose**: This section represents the core compensation budget data for the department, combining base salary inputs with annual budgets and monthly allocations. It provides the budgeting foundation used to plan payouts and monitor compensation against targets.
- **Cell Range**: A1:CX54
- **Time Series Horizon**:
  - **Dates Location**: D4:CX4
  - **Date Range**: 2019-10-01 to 2027-12-01
  - **Frequency**: Monthly
- **Key Components**: Salary; 2019 Budget; 2020 Budget; Adjustment
- **Notes & Customizations**: The data is scaled in thousands (scale 1000) for many numeric columns. The sheet title and headers indicate this is a Bonus Support view for Sales non-ops, with department-level aggregation and a department header region at A1.

### Bonus Components & Payouts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section captures the various bonus components and their payout structure (e.g., adjustments, total sales bonus, quarterly bonuses, and adj Kiva adjustments), providing the components that drive total compensation outcomes.
- **Cell Range**: B6:CX54
- **Time Series Horizon**:
  - **Dates Location**: D4:CX4
  - **Date Range**: 2019-10-01 to 2027-12-01
  - **Frequency**: Monthly
- **Key Components**: Adjustment; Total Sales Bonus; Quarterly Bonus Paid; Quarterly Bonus Paid (Adj Kiva)
- **Notes & Customizations**: Numbers across these columns are largely scaled (scale 1000). This section aggregates multiple bonus lines that feed into overall compensation calculations and potential payouts.

### Bonus Attainment Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section consolidates attainment-related metrics for bonuses (e.g., Average Bonus Attainment, Count, Total, and Avg) and displays them across the defined time horizon. It supports performance evaluation and dashboard-style reporting.
- **Cell Range**: B17:CX54
- **Time Series Horizon**:
  - **Dates Location**: D4:CX4
  - **Date Range**: 2019-10-01 to 2027-12-01
  - **Frequency**: Monthly
- **Key Components**: AVERAGE BONUS ATTAINMENT; Count; Total; Avg (with monthly value blocks across F21:CX21, F22:CX22, etc.)
- **Notes & Customizations**: The metrics use thousands scaling (scale 1000) for numerical fields. The section integrates monthly attainment data with the broader compensation framework.

### Time Series Definitions
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Defines the monthly date series used to align and anchor data across the compensation sheet. It includes the primary monthly date headers (ds_1) and a secondary monthly date series (ds_2) that are defined for cross-referencing and charting.
- **Cell Range**: D4:CX39
- **Time Series Horizon**:
  - **Dates Location**: D4:CX4
  - **Date Range**:
    - ds_1: 2019-10-01 to 2027-12-01 (Monthly)
    - ds_2: 2019-12-31 to 2027-12-01 (Monthly)
  - **Frequency**: Monthly
- **Key Components**: ds_1 (Monthly series starting 2019-10), ds_2 (Monthly series starting 2019-12)
- **Notes & Customizations**: The sheet includes two monthly date series to support different dashboards or alignment needs. The primary date labels reside in D4:CX4, with a secondary series shown at the ds_2 row/columns (e.g., ds_2 appears around F39:CX39). This dual-series approach is documented in the time-series metadata.