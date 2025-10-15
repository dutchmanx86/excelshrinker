## 1. Spreadsheet Overview
- **Sheet Name**: Deferred Build
- **Key Sections Identified**:
    - Header
    - Deferred Revenue Summary
    - Deferred Revenue Detail
    - Revenue Recognition Detail

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and scenario information.
- **Cell Range**: B2:Q4
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: E3:H3, I3:Q3
    - **Data Range**: E3:Q3
- **Time Series Details**:
    - Annual: Not explicitly defined, but E3:H3 and I3:Q3 suggest annual data. No specific date range is available.
    - Frequency: Annual (implied)
- **Key Components**: AlphaSense, Inc., Deferred Revenue Detail, 1 - Base - $25mm
- **Notes & Customizations**: Contains the title and scenario assumption.

### Deferred Revenue Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the deferred revenue balance, ARR, and related metrics over time.
- **Cell Range**: B6:DV14
- **Layout Structure**:
    - **Row Headers Location**: B6:B14
    - **Column Headers Location**: E8:Q8, T8:DV8
    - **Data Range**:
      - Annual data: E8:Q14
      - Monthly data: T8:DV14
- **Time Series Details**:
    - Annual: No specific date range is available.
    - Monthly: 2015-01-31 to 2027-12-31
    - Frequency:
      - Annual (implied)
      - Monthly
- **Key Components**: ARR, Deferred Beginning Balance, Add (Projected), Recognized as Revenue (Projected), Deferred Ending Balance, % of ARR
- **Notes & Customizations**: Contains both annual and monthly time series data. Values are scaled by 1000.

### Deferred Revenue Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of how ARR is added to the deferred revenue balance.
- **Cell Range**: B19:DV29
- **Layout Structure**:
    - **Row Headers Location**: B19:B29
    - **Column Headers Location**: BP22:DV22, BP23:DV23, BP24:DV24, BP27:DV27, BP28:DV28, BP29:DV29
    - **Data Range**:
      - Monthly data: BP22:DV24, BP27:DV29
- **Time Series Details**:
    - Monthly: 2015-01-31 to 2027-12-31
    - Frequency: Monthly
- **Key Components**: ARR Added, Renewals, Bookings, Total ARR Added Previous Month, Added to Deferred Revenue Balance, Total Added to Deferred Revenue Balance
- **Notes & Customizations**: Values are scaled by 1000.

### Revenue Recognition Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows how deferred revenue is recognized as revenue over time.
- **Cell Range**: B31:DV34
- **Layout Structure**:
    - **Row Headers Location**: B31:B34
    - **Column Headers Location**: BP32:DV32, BP33:DV33, BP34:DV34
    - **Data Range**:
      - Monthly data: BP32:DV34
- **Time Series Details**:
    - Monthly: 2015-01-31 to 2027-12-31
    - Frequency: Monthly
- **Key Components**: Revenue, Bookings Revenue Recognized, Renewal Revenue Recognized, Revenue from Deferred Revenue Balance
- **Notes & Customizations**: Values are scaled by 1000.
