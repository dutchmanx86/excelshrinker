## 1. Spreadsheet Overview
- **Sheet Name**: FDS AMR
- **Key Sections Identified**:
    - Header
    - User Statistics
    - Documents Purchased Statistics
    - Cost Analysis

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report.
- **Cell Range**: B5:DD5
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: D5:K5, M5:DD5
    - **Data Range**: D5:K5, M5:DD5
- **Time Series Details**:
    - **Date Range**: 2020 to 2027 (D5:K5), 2020 to 2027 (M5:DD5)
    - **Frequency**: Annual (D5:K5), Annual (M5:DD5)
- **Key Components**: "FDS AMR"
- **Notes & Customizations**: Scale is in thousands.

### User Statistics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays key user statistics, including total bookings, active users, and active trialer users.
- **Cell Range**: B6:DD24
- **Layout Structure**:
    - **Row Headers Location**: B6:B24
    - **Column Headers Location**: D2:K3, M2:DD3
    - **Data Range**:
      - Annual data: D6:K24
      - Monthly data: M6:DD24
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (D2:K2)
      - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: "% Active", "Total Bookings", "Active Users", "Active Trialer Users", "FDS Entitled AMR Users"
- **Notes & Customizations**: Some values are scaled in thousands.

### Documents Purchased Statistics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents data related to documents purchased by different user types.
- **Cell Range**: B26:DD59
- **Layout Structure**:
    - **Row Headers Location**: B26:B59
    - **Column Headers Location**: D2:K3, M2:DD3
    - **Data Range**:
      - Annual data: D28:K59
      - Monthly data: M28:DD59
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (D2:K2)
      - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: "Active Users", "Active - Documents Purchased", "Trialers - Documents Purchased", "Internal - Documents Purchased", "Total Docs Purchased"
- **Notes & Customizations**: Some values are scaled in thousands.

### Cost Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes document costs, including costs per tier and total costs.
- **Cell Range**: B61:DD89
- **Layout Structure**:
    - **Row Headers Location**: B61:B89
    - **Column Headers Location**: D2:K3, M2:DD3
    - **Data Range**:
      - Annual data: D61:K89
      - Monthly data: M61:DD89
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (D2:K2)
      - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: "Annual Documents Read", "Document Cost - Tier 1", "Total Document Cost", "FactSet AMR Minimum", "Total FactSet AMR Cost", "Rollover Balance", "Excess Over Minimum", "Adjusted Excess", "Total Adjusted FactSet AMR Cost"
- **Notes & Customizations**: Some values are scaled in thousands.
