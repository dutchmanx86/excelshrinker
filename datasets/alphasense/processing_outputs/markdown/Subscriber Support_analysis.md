## 1. Spreadsheet Overview
- **Sheet Name**: Subscriber Support
- **Key Sections Identified**:
    - Subscriber Counts by Type
    - Expense Allocation

## 2. Detailed Section Analysis

### Section Name: Subscriber Counts by Type
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the number of subscribers, broken down by different subscriber types (Financial, Corp, Other). It shows the beginning count, added subscribers, churned subscribers, and the ending subscriber count for each type. This allows for analysis of subscriber growth and churn rates.
- **Cell Range**: C4:DS20
- **Layout Structure**:
    - **Row Headers Location**: Column C (C5:C8, C11:C14, C17:C20)
    - **Column Headers Location**: Row 2 (E2:DS2) and Row 4 (C4)
    - **Data Range**:
      - Monthly data: F5:DS8, F11:DS14, F17:DS20
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-08-31 (E2:DS2). Anchor points: E2=2010-10-01, Q2=2011-10-01, AC2=2012-10-01, AO2=2013-10-01, BA2=2014-10-01, BM2=2015-10-01, BY2=2016-10-01, CK2=2017-10-01, CW2=2018-10-01, DI2=2019-10-01
    - **Frequency**: Monthly
- **Key Components**: Financial, Corp, Other, Beginning, Added, Churn, End.
- **Notes & Customizations**: Subscriber counts are displayed in thousands (scale=1000), except for DA6:DS6, DA12:DS12, and DA18:DS18.

### Section Name: Expense Allocation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section allocates expenses to different categories. It shows the total expenses and then breaks them down by category (e.g., Admin). This helps understand the cost structure.
- **Cell Range**: CM25:CY26
- **Layout Structure**:
    - **Row Headers Location**: Column CM (CM25, CM26)
    - **Column Headers Location**: Row 25 (CM25)
    - **Data Range**: CN25:CY26
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the provided JSON. Assuming the same monthly series as Subscriber Counts, but only for a subset of time.
    - **Frequency**: Monthly (assumed)
- **Key Components**: Total, Admin, Soros / Cap Group - Internal Content
- **Notes & Customizations**: Expenses are displayed in thousands (scale=1000).
