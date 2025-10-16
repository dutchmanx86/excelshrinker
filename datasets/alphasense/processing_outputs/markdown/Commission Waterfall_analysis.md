## 1. Spreadsheet Overview
- **Sheet Name**: Commission Waterfall
- **Key Sections Identified**:
    - Header
    - Commissions Expense Summary
    - Financial Commission Waterfall
    - Corporate Commission Waterfall
    - Other Commission Waterfall
    - AE Commission Waterfall
    - Commissions Expense

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and report title.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: Company Name, Report Title, Scenario Description
- **Notes & Customizations**: None

### Commissions Expense Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of commissions expense, including bonus expense and total commission expense. It also includes bookings data and commission percentages.
- **Cell Range**: A6:FS24
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G6:Q6 (Annual), AR6:FS6 (Monthly)
    - **Data Range**:
      - Annual data: `G8:Q24`
      - Monthly data: `AR8:FS24`
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but likely 2015 to 2021 based on column count.
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Commissions Expense, Bonus Expense, Total Commission Expense, Financial Bookings, Corporate Bookings, Other Bookings, Commission Percentages, Financial Commission, Corporate Commission, Other Commission, Sales Manager Commission.
- **Notes & Customizations**: Data is scaled by 1000.

### Financial Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of financial commissions over time.
- **Cell Range**: B26:FS162
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Column C, AR3:FS3 (Monthly)
    - **Data Range**:
      - Monthly data: `AR30:FS161`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Data is scaled by 1000.

### Corporate Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of corporate commissions over time.
- **Cell Range**: B165:FS301
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Column C, AR3:FS3 (Monthly)
    - **Data Range**:
      - Monthly data: `AR169:FS300`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Data is scaled by 1000.

### Other Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of other commissions over time.
- **Cell Range**: B304:FS440
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Column C, AR3:FS3 (Monthly)
    - **Data Range**:
      - Monthly data: `AR308:FS439`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Data is scaled by 1000.

### AE Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of AE commissions over time.
- **Cell Range**: B443:FS579
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Column C, AR3:FS3 (Monthly)
    - **Data Range**:
      - Monthly data: `AR447:FS578`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Data is scaled by 1000.

### Commissions Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of commissions expense, including bonus expense and total commission expense.
- **Cell Range**: B581:FS583
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G6:Q6 (Annual), AR6:FS6 (Monthly)
    - **Data Range**:
      - Annual data: `G581:Q583`
      - Monthly data: `AR581:FS583`
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but likely 2015 to 2021 based on column count.
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Commissions Expense, Bonus Expense, Total Commission Expense
- **Notes & Customizations**: Data is scaled by 1000.
