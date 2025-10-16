## 1. Spreadsheet Overview
- **Sheet Name**: Retention
- **Key Sections Identified**:
    - Header
    - Financial Retention Detail
    - Corporate Retention Detail
    - Other Retention Detail
    - Summary Retention Detail

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the data.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:FS3 (Time series data)
    - **Data Range**: E3:I3, J3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: Not explicitly defined in a single range, but implied by the data structure in E3:I3 and J3:Q3. Likely represents 2010-2014 and 2015-2021.
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
        - Frequency: Monthly
- **Key Components**: Company Name, Data Description, Time Series Headers.
- **Notes & Customizations**: Contains both annual and monthly time series data.

### Financial Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Financial segment, including churn and retention percentages.
- **Cell Range**: B8:FS18
- **Layout Structure**:
    - **Row Headers Location**: B8:B18
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E9:Q11, E12:Q12, E15:Q17, E18:Q18
      - Monthly data: T9:FS11, T12:FS12, T15:FS17, T18:FS18
- **Time Series Details**:
    - Annual: E3:Q3 (likely representing 2010-2021)
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
        - Frequency: Monthly
- **Key Components**: Churn, Total Churn, Financial, Blended Retention %.
- **Notes & Customizations**: Data is scaled by 1000.

### Corporate Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Corporate segment.
- **Cell Range**: B23:FS40
- **Layout Structure**:
    - **Row Headers Location**: B25:B40
    - **Column Headers Location**: E3:Q3, T3:FS3, CJ3:FS3
    - **Data Range**:
      - Annual data: E25:Q28, E30:Q31, J33:Q33, J39:Q39, E40:Q40
      - Monthly data: T25:FS28, CJ30:FS31, CI33:FS33, CJ34:FS38, CJ39:FS40, T40:FS40
- **Time Series Details**:
    - Annual: E3:Q3 (likely representing 2010-2021)
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
        - Frequency: Monthly
- **Key Components**: Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal.
- **Notes & Customizations**: Data is scaled by 1000. Contains "Annual Financial Up for Renewal" section with data in J33:Q33 and CI33:FS33.

### Corporate Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Corporate segment.
- **Cell Range**: A42:FS59
- **Layout Structure**:
    - **Row Headers Location**: B44:B59
    - **Column Headers Location**: E3:Q3, T3:FS3, CJ3:FS3
    - **Data Range**:
      - Annual data: E44:Q47, E49:Q50, J52:Q52, J58:Q58, E59:Q59
      - Monthly data: T44:FS47, CJ49:FS50, CI52:FS52, CJ53:FS57, CJ58:FS59, T59:FS59
- **Time Series Details**:
    - Annual: E3:Q3 (likely representing 2010-2021)
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
        - Frequency: Monthly
- **Key Components**: Total Corporate Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal.
- **Notes & Customizations**: Data is scaled by 1000. Contains "Annual Up for Renewal" section with data in J52:Q52 and CI52:FS52.

### Other Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Other segment.
- **Cell Range**: A61:FS78
- **Layout Structure**:
    - **Row Headers Location**: B63:B78
    - **Column Headers Location**: E3:Q3, T3:FS3, CJ3:FS3
    - **Data Range**:
      - Annual data: E63:Q66, E68:Q69, J71:Q71, J77:Q77, E78:Q78
      - Monthly data: T63:FS66, CJ68:FS69, CI71:FS71, CJ72:FS76, CJ77:FS78, T78:FS78
- **Time Series Details**:
    - Annual: E3:Q3 (likely representing 2010-2021)
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-12-31
        - Frequency: Monthly
- **Key Components**: Total Other Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal.
- **Notes & Customizations**: Data is scaled by 1000. Contains "Annual Other Up for Renewal" section with data in J71:Q71 and CI71:FS71.

### Summary Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of retention metrics.
- **Cell Range**: A80:FS86
- **Layout Structure**:
    - **Row Headers Location**: B82:B86
    - **Column Headers Location**: E3:Q3, T3:FS3, CJ3:FS3
    - **Data Range**:
      - Annual data: E82:Q84
      - Monthly data: T82:FS84, CJ86:FS86
- **Time Series Details**:
    - Annual: E3:Q3 (likely representing 2010-2021)
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
        - Frequency: Monthly
- **Key Components**: Up for Renewal, Retention %, Renewed, Churned.
- **Notes & Customizations**: Data is scaled by 1000.
