## 1. Spreadsheet Overview
- **Sheet Name**: Additional FDS Content
- **Key Sections Identified**:
    - FDS RT Expense - User Tier Analysis
    - FDS RT Excess Expense Calculation
    - FDS Transcripts - User Tier Analysis
    - FDS M&A - User Tier Analysis

## 2. Detailed Section Analysis

### FDS RT Expense - User Tier Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total FDS RT (Real-Time) users, their associated costs, and percentage of total users, broken down by user tiers. It provides a snapshot of user distribution and cost allocation across different user segments.
- **Cell Range**: B5:DF34
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Up to 1500", "2000 - 425000", etc.)
    - **Column Headers Location**: C2:DF3. C2 contains "Users", D2 contains "Cost". F3:M3 contains annual dates, O3:DF3 contains monthly dates.
    - **Data Range**:
      - Annual data: C11:D34 (numeric values for annual periods)
      - Monthly data: V11:DF34 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (F3:M3)
      - Monthly: 2020-01-31 to 2027-12-31 (O3:DF3). Anchor points: O3=2020-01-31, AA3=2021-01-31, AM3=2022-01-31, AY3=2023-01-31, BK3=2024-01-31, BW3=2025-01-31, CI3=2026-01-31, CU3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS RT Users, User Tiers, Users, Cost, % of Total Users.
- **Notes & Customizations**: Costs are scaled by 1000.

### FDS RT Excess Expense Calculation
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section calculates the Total FDS RT Excess Expense, adjusting for discounts and pool floors. It aims to determine the minimum excess spend based on user buckets.
- **Cell Range**: B36:DF49
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Total FDS RT Excess Expense", "Pool Floor", "Total Adjusted FDS RT Excess Expense", etc.)
    - **Column Headers Location**: F3:M3 contains annual dates, O3:DF3 contains monthly dates.
    - **Data Range**:
      - Annual data: F36:M49 (numeric values for annual periods)
      - Monthly data: O36:DF49 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (F3:M3)
      - Monthly: 2020-01-31 to 2027-12-31 (O3:DF3). Anchor points: O3=2020-01-31, AA3=2021-01-31, AM3=2022-01-31, AY3=2023-01-31, BK3=2024-01-31, BW3=2025-01-31, CI3=2026-01-31, CU3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS RT Excess Expense, Pool Floor, Discount (%), Discount Adjusted FDS RT Excess Expense, Minimum Excess Spend.
- **Notes & Customizations**: Expenses are scaled by 1000.

### FDS Transcripts - User Tier Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total FDS Transcript users, broken down by user tiers. It provides a snapshot of user distribution across different user segments.
- **Cell Range**: B51:DF80
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Up to 6000", "7001 - 65000", etc.)
    - **Column Headers Location**: C2:DF3. C2 contains "Users", D2 contains "Cost". O3:DF3 contains monthly dates.
    - **Data Range**:
      - Annual data: C57:D78 (numeric values for annual periods)
      - Monthly data: V57:DF78 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (O2:DF2). Anchor points: O2=2020-01-01, AA2=2021-01-01, AM2=2022-01-01, AY2=2023-01-01, BK2=2024-01-01, BW2=2025-01-01, CI2=2026-01-01, CU2=2027-01-01
      - Monthly: 2020-01-31 to 2027-12-31 (O3:DF3). Anchor points: O3=2020-01-31, AA3=2021-01-31, AM3=2022-01-31, AY3=2023-01-31, BK3=2024-01-31, BW3=2025-01-31, CI3=2026-01-31, CU3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS Transcript Users, User Tiers, Users, Cost, % of Total Users, Total FDS Transcripts Excess Expense.
- **Notes & Customizations**: Users are scaled by 1000.

### FDS M&A - User Tier Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total FDS M&A users, broken down by user tiers. It provides a snapshot of user distribution across different user segments.
- **Cell Range**: B83:DF112
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Up to 6000", "TBD")
    - **Column Headers Location**: C2:DF3. C2 contains "Users", D2 contains "Cost". O3:DF3 contains monthly dates.
    - **Data Range**:
      - Annual data: C89:D110 (numeric values for annual periods)
      - Monthly data: V89:DF110 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (O2:DF2). Anchor points: O2=2020-01-01, AA2=2021-01-01, AM2=2022-01-01, AY2=2023-01-01, BK2=2024-01-01, BW2=2025-01-01, CI2=2026-01-01, CU2=2027-01-01
      - Monthly: 2020-01-31 to 2027-12-31 (O3:DF3). Anchor points: O3=2020-01-31, AA3=2021-01-31, AM3=2022-01-31, AY3=2023-01-31, BK3=2024-01-31, BW3=2025-01-31, CI3=2026-01-31, CU3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS M&A Users, User Tiers, Users, Cost, % of Total Users, Total FDS M&A Excess Expense.
- **Notes & Customizations**: Values are scaled by 1000.
