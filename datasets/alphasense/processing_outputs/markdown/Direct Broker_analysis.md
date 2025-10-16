```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Direct Broker
- **Key Sections Identified**:
    - Overview Metrics
    - Reads Consumption by Broker
    - WSI Broker Expense Detail

## 2. Detailed Section Analysis

### Section Name: Overview Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a high-level overview of key metrics related to AlphaSense's cost of goods sold, including expenses, user activity, and consumption data. It helps track overall performance and efficiency.
- **Cell Range**: B6:Q47
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**: E8:Q47
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**:
    - Bernstein Expense, Deutsche Bank Expense, Barclays Expense, HSBC Expense, BOA Expense, UBS Expense, Morgan Stanley Expense, Cowen Expense, Autonomous Expense, Evercore Expense, Citi Expense, Credit Suisse Expense, JP Morgan Expense, Raymond James Expense, RBC Expense, Direct Consumption Expense, Total WSI, Total Active Users, Cost per User, FS BRM Expense, Total Users, Active Users, Active (%), Total Page Reads, Page Reads per Active User, Contribution per User, Total Pool Contribution ($)
- **Notes & Customizations**: Expenses are scaled by 1000. Cost per user is calculated from column J onwards.

### Section Name: Reads Consumption by Broker
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the reads consumption and percentage of reads consumption by broker. This helps understand which brokers are driving the most usage.
- **Cell Range**: B49:Q95
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**: E51:Q95
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**:
    - Bernstein, Deutsche Bank, Barclays, HSBC, BOA, UBS, Morgan Stanley, Cowen, Autonomous, Evercore, Citi , Credit Suisse , JP Morgan , Raymond James, RBC, Direct Broker, FactSet AMR, FactSet RT, Total
- **Notes & Customizations**: Reads Consumption is displayed in absolute numbers and as a percentage.

### Section Name: WSI Broker Expense Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of expenses associated with each broker, including strategic investment, usage, consumption, revenue share, expense, minimum, and adjusted expense. It helps in understanding the cost structure for each broker.
- **Cell Range**: B97:Q255
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q and T to FS
    - **Data Range**: E101:Q255
- **Time Series Details**:
    - **Date Range**:
        - Annual: 2015 to 2027 (E101:Q255)
        - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
        - Annual
        - Monthly
- **Key Components**:
    - Total Pool Contribution, Direct Broker Expense, Strategic Investment, Usage, Consumption, Revenue Share, Expense, Minimum, Adjusted Expense
- **Notes & Customizations**: Expenses are scaled by 1000. There are two time series: annual data in columns E:Q and monthly data in columns T:FS.
```