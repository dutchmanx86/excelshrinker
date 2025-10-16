## 1. Spreadsheet Overview
- **Sheet Name**: Filings
- **Key Sections Identified**:
    - Header
    - Revenue by Segment

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the sheet title and potentially other high-level information.
- **Cell Range**: A1:B1
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: None
- **Notes & Customizations**: This is a simple header section.

### Revenue by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows revenue broken down by different segments (Other, Corporate, Broker Partner) over a period of time. It includes total revenue as well.
- **Cell Range**: B3:T8
- **Layout Structure**:
    - **Row Headers Location**: B3:B7
    - **Column Headers Location**: C2:T2
    - **Data Range**:
      - Annual data: C3:K7
      - Thousands data: L3:N7
      - Monthly data: O3:T7
    - **Total Revenue Range**: C8:T8
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017-01-01 to 2017-09-01 (C2:K2)
      - Thousands: 2017-10-01 to 2017-12-01 (L2:N2)
      - Monthly: 2018-01-01 to 2018-06-01 (O2:T2)
    - **Frequency**:
      - Annual: Monthly
      - Thousands: Monthly
      - Monthly: Monthly
- **Key Components**: Financial, Other, Corporate, Broker Partner, Total Revenue.
- **Notes & Customizations**: There are three time series within this section: Annual, Thousands, and Monthly. The "Thousands" section appears to be a scaling factor applied to the data. The date series definition indicates a monthly series, but the column headers suggest it's being used to represent different periods within a year.
