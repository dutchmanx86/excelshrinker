## 1. Spreadsheet Overview
- **Sheet Name**: Total FDS Cost
- **Key Sections Identified**:
  - Summary FDS COGS Expense
  - FDS Content
  - FDS Excess Expense & Totals
  - Pool Contribution & Carryover
  - AMR Expense
  - Adjusted AMR Expense
  - Adjusted FDS COGS Expense

## 2. Detailed Section Analysis

### Summary FDS COGS Expense
- **Section Type**: Custom Cost Summary Table
- **Description & Purpose**: High-level overview of FDS-related COGS expenses; establishes the top-level cost structure and anchors the time-series data that feed the rest of the sheet.
- **Cell Range**: A3:DC14
- **Time Series Horizon**:
  - **Dates Location**: C1:J1 (annual) and L1:DC1 (monthly)
  - **Date Range**:
    - Annual: 2020-01-01 through 2027-01-01
    - Monthly: 2020-01-31 through 2027-12-31
  - **Frequency**:
    - Annual
    - Monthly
- **Key Components**: Overall summary header, core cost lines, and the primary blocks that feed subsequent detail sections.
- **Notes & Customizations**: The section integrates multiple sub-blocks under a single summary, with several numeric blocks scaled by 1000 in downstream rows.

### FDS Content
- **Section Type**: Cost Content Breakdown Table
- **Description & Purpose**: Detailed decomposition of FDS content costs by category and period, forming the main body of the cost structure beneath the summary header.
- **Cell Range**: A5:DC14
- **Time Series Horizon**:
  - **Dates Location**: C1:J1 (annual) and L1:DC1 (monthly)
  - **Date Range**:
    - Annual: 2020-01-01 through 2027-01-01
    - Monthly: 2020-01-31 through 2027-12-31
  - **Frequency**:
    - Annual
    - Monthly
- **Key Components**: FDS Content label, per-category cost lines across both annual and monthly date axes.
- **Notes & Customizations**: Contains multiple sub-blocks and scaled figures (notably many ranges scaled by 1000); designed to align with the dual annual/monthly date series.

### FDS Excess Expense & Totals
- **Section Type**: Totals & Excess Allocation Table
- **Description & Purpose**: Tracks excess FDS-related expenses and associated totals, including explicit lines for Total Excess, Total FDS Spend, and Total FDS Minimum.
- **Cell Range**: A16:DC25
- **Time Series Horizon**:
  - **Dates Location**: C1:J1 (annual) and L1:DC1 (monthly)
  - **Date Range**:
    - Annual: 2020-01-01 through 2027-01-01
    - Monthly: 2020-01-31 through 2027-12-31
  - **Frequency**:
    - Annual
    - Monthly
- **Key Components**: FDS Excess Expense, Total Excess, Total FDS Spend, Total FDS Minimum.
- **Notes & Customizations**: Continues the same time-series alignment and scaling conventions as the content block; reflects how excess costs flow into the broader cost structure.

### Pool Contribution & Carryover
- **Section Type**: Pool/Carryover Worksheet
- **Description & Purpose**: Defines pool contribution mechanics and subsequent carryover and balance dynamics; important for inter-period and inter-component cost settlement.
- **Cell Range**: A27:DC33
- **Time Series Horizon**:
  - **Dates Location**: C1:J1 (annual) and L1:DC1 (monthly)
  - **Date Range**:
    - Annual: 2020-01-01 through 2027-01-01
    - Monthly: 2020-01-31 through 2027-12-31
  - **Frequency**:
    - Annual
    - Monthly
- **Key Components**: Pool Contribution, Paid, Carryover, Excess, Carryover Balance.
- **Notes & Customizations**: Indicates interplays with other cost blocks; uses the same 1000x scaling convention in relevant rows.

### AMR Expense
- **Section Type**: Expense Allocation Table
- **Description & Purpose**: Captures AMR-related expenses within the Total FDS Cost framework; serves as a primary allocation block for AMR costs.
- **Cell Range**: A36:DC46
- **Time Series Horizon**:
  - **Dates Location**: C1:J1 (annual) and L1:DC1 (monthly)
  - **Date Range**:
    - Annual: 2020-01-01 through 2027-01-01
    - Monthly: 2020-01-31 through 2027-12-31
  - **Frequency**:
    - Annual
    - Monthly
- **Key Components**: AMR Expense header plus associated cost rows within the same block.
- **Notes & Customizations**: Aligns with the dual annual/monthly time series; part of the broader FDS cost framework.

### Adjusted AMR Expense
- **Section Type**: Adjusted Expense Table
- **Description & Purpose**: Post-adjustment AMR expense values used for final reconciliation within the FDS cost structure.
- **Cell Range**: A38:DC46
- **Time Series Horizon**:
  - **Dates Location**: C1:J1 (annual) and L1:DC1 (monthly)
  - **Date Range**:
    - Annual: 2020-01-01 through 2027-01-01
    - Monthly: 2020-01-31 through 2027-12-31
  - **Frequency**:
    - Annual
    - Monthly
- **Key Components**: "Adjusted AMR Expense" header with adjustment lines across the same time axes.
- **Notes & Customizations**: Maintains the same time-series alignment as the unadjusted AMR section; uses consistent scaling conventions.

### Adjusted FDS COGS Expense
- **Section Type**: Adjusted COGS Table
- **Description & Purpose**: Final adjusted FDS COGS expenses after AMR considerations and other adjustments.
- **Cell Range**: A40:DC46
- **Time Series Horizon**:
  - **Dates Location**: C1:J1 (annual) and L1:DC1 (monthly)
  - **Date Range**:
    - Annual: 2020-01-01 through 2027-01-01
    - Monthly: 2020-01-31 through 2027-12-31
  - **Frequency**:
    - Annual
    - Monthly
- **Key Components**: "Adjusted FDS COGS Expense" header plus the adjusted cost rows within the same time frame.
- **Notes & Customizations**: Continues the sheet’s standard dual time-series structure; 1000x scaling remains in effect for many values.