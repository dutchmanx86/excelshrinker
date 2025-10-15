## 1. Spreadsheet Overview
- **Sheet Name**: Dash Control
- **Key Sections Identified**:
  - Time Series Setup & Dashboard Headers
  - ARR & Perpetuity Projection Model

## 2. Detailed Section Analysis

### Time Series Setup & Dashboard Headers
- **Section Type**: Time Series Setup
- **Description & Purpose**: This section defines the dashboard’s time axes and the primary date series used to drive the charts and calculations. It includes the Year/Month headers and three date series (two annual and one monthly) that anchor the time context for the dashboard.
- **Cell Range**: B6:FS8
- **Time Series Horizon**:
  - ds_1
    - Dates Location: E6:Q6
    - Date Range: 2015-01-01 to 2027-01-01
    - Frequency: Annual
  - ds_2
    - Dates Location: T6:FS6
    - Date Range: 2015-01-01 to 2027-01-01
    - Frequency: Annual
  - ds_3
    - Dates Location: E8:Q8 and T8:FS8
    - Date Range: 2015-01-31 to 2027-12-31
    - Frequency: Monthly
- **Key Components**: Year label (B6), Month label (B7), ds_1 (E6:Q6), ds_2 (T6:FS6), ds_3 (E8:Q8, T8:FS8)
- **Notes & Customizations**: The sheet integrates two annual date series and a monthly series to support both annual and monthly horizon views within the dashboard.

### ARR & Perpetuity Projection Model
- **Section Type**: Forecast Model Table
- **Description & Purpose**: This section aggregates the major modeling blocks used to project ARR multipliers and perpetuity-based values across scenarios (including base, growth, financial, and corporate flavors), along with travel-cost sensitivities. It serves as the core data model behind the dashboard’s forecast and valuation calculations.
- **Cell Range**: A11:BW65
- **Time Series Horizon**:
  - ds_1
    - Dates Location: E6:Q6
    - Date Range: 2015-01-01 to 2027-01-01
    - Frequency: Annual
  - ds_2
    - Dates Location: T6:FS6
    - Date Range: 2015-01-01 to 2027-01-01
    - Frequency: Annual
  - ds_3
    - Dates Location: E8:Q8 and T8:FS8
    - Date Range: 2015-01-31 to 2027-12-31
    - Frequency: Monthly
- **Key Components**: 
  - ARR Multipler (Base – $25mm, Growth – $25mm, Base – $50mm, Base – $50mm (R&D))
  - Perpetuity Factor (Base, Financial, Corporate)
  - Travel Costs (%)
  - Support Fees - % of CAC
- **Notes & Customizations**: Many numeric blocks use a scale factor of 1000 for display (e.g., J14:Q14, J15:Q15, etc.), indicating a custom, thousand-multiplied display convention within this dashboard data model. This is a tailored model rather than a standard, out-of-the-box financial statement.