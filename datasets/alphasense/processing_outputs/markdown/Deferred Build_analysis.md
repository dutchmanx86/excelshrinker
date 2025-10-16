## 1. Spreadsheet Overview
- **Sheet Name**: Deferred Build
- **Key Sections Identified**:
    - Header
    - Deferred Revenue Summary
    - Deferred Revenue Detail
    - Revenue Recognition

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and report title.
- **Cell Range**: B2:FS3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:H3, I3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**: E3:H3, I3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: Not explicitly defined, but implied by the presence of number formatting in E3:H3 and I3:Q3. The years are not explicitly stated in the JSON.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31.
    - **Frequency**: Annual, Monthly
- **Key Components**: Company Name, Report Title, Dates
- **Notes & Customizations**: Contains both annual and monthly time series.

### Deferred Revenue Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the deferred revenue balance and its components.
- **Cell Range**: B6:DV14
- **Layout Structure**:
    - **Row Headers Location**: B6:B14
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E8:Q14
      - Monthly data: T8:DV14
- **Time Series Details**:
    - Annual: Not explicitly defined, but implied by the presence of number formatting in E3:Q3. The years are not explicitly stated in the JSON.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31.
    - **Frequency**: Annual, Monthly
- **Key Components**: ARR, Deferred Beginning Balance, Add (Projected), Recognized as Revenue (Projected), Deferred Ending Balance, % of ARR
- **Notes & Customizations**: Contains both annual and monthly time series. Values are scaled by 1000.

### Deferred Revenue Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of the additions to the deferred revenue balance.
- **Cell Range**: B19:DV29
- **Layout Structure**:
    - **Row Headers Location**: B19:B29
    - **Column Headers Location**: BP3:DV3 (Monthly) - Implied from the monthly date series in the header.
    - **Data Range**: BP22:DV29
- **Time Series Details**:
    - Monthly: 2019-01-31 to 2027-12-31 (BP3:DV3). Anchor points: BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31.
    - **Frequency**: Monthly
- **Key Components**: ARR Added (Bookings, Renewals), Total ARR Added Previous Month, Added to Deferred Revenue Balance (Bookings, Renewals), Total Added to Deferred Revenue Balance
- **Notes & Customizations**: Values are scaled by 1000.

### Revenue Recognition
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the revenue recognized from various sources.
- **Cell Range**: B31:DV34
- **Layout Structure**:
    - **Row Headers Location**: B31:B34
    - **Column Headers Location**: BP3:DV3 (Monthly) - Implied from the monthly date series in the header.
    - **Data Range**: BP32:DV34
- **Time Series Details**:
    - Monthly: 2019-01-31 to 2027-12-31 (BP3:DV3). Anchor points: BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31.
    - **Frequency**: Monthly
- **Key Components**: Revenue, Bookings Revenue Recognized, Renewal Revenue Recognized, Revenue from Deferred Revenue Balance
- **Notes & Customizations**: Values are scaled by 1000.
