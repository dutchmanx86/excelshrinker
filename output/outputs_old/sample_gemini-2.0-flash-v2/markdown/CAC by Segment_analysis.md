## 1. Spreadsheet Overview
- **Sheet Name**: CAC by Segment
- **Key Sections Identified**:
    - Summary Upsell and CAC Cost
    - Detail Upsell and CAC Cost by Team
    - Adjusted Sales and Marketing Cost
    - Adjusted People Costs

## 2. Detailed Section Analysis

### Section Name: Summary Upsell and CAC Cost
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a high-level summary of Upsell and CAC (Customer Acquisition Cost) metrics for the Total Company, broken down by Financial and Corporate segments. It's used to quickly assess overall cost efficiency.
- **Cell Range**: B5:FS20
- **Layout Structure**:
    - **Row Headers Location**: B5:B20
    - **Column Headers Location**: E2:Q2, T2:FS2
    - **Data Range**:
      - Annual data: E8:Q20
      - Monthly data: T8:FS20
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined in the data, but implied to be a series of years based on the column structure.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Upsell Cost, CAC, Support Cost, Total Company, Financial, Corporate.
- **Notes & Customizations**: Values in columns G:Q and AR:FS are scaled by 1000.

### Section Name: Detail Upsell and CAC Cost by Team
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down the Upsell and CAC metrics by individual teams (Account Manager, AE, VP - Bus Dev, AE - Enterprise). This allows for a more granular view of cost drivers and team performance.
- **Cell Range**: B22:FS68
- **Layout Structure**:
    - **Row Headers Location**: B22:B68
    - **Column Headers Location**: E2:Q2, T2:FS2
    - **Data Range**:
      - Annual data: G25:Q68
      - Monthly data: AR25:FS68, T41:FS46
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined in the data, but implied to be a series of years based on the column structure.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Account Manager - Corp, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise, Total, % Financial, % Corporate, Wages.
- **Notes & Customizations**: Values in columns G:Q and AR:FS are scaled by 1000.

### Section Name: Adjusted Sales and Marketing Cost
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates adjusted sales and marketing costs and key ratios like "% to CAC" and "% to Upsell". It provides insights into the efficiency of sales and marketing spend.
- **Cell Range**: A71:FS79
- **Layout Structure**:
    - **Row Headers Location**: B71:B79
    - **Column Headers Location**: E2:Q2, T2:FS2
    - **Data Range**:
      - Annual data: E73:Q79
      - Monthly data: T73:FS79
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined in the data, but implied to be a series of years based on the column structure.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Total Company, Adjusted Sales and Marketing Cost, % to CAC, % to Upsell, $ to CAC, $ to Upsell.
- **Notes & Customizations**: Values in columns E:Q and T:FS are scaled by 1000 for rows 76 and 79.

### Section Name: Adjusted People Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates adjusted people costs related to support, taking into account capitalized wages and outsourced R&D. It helps understand the true cost of support personnel.
- **Cell Range**: B81:FS140
- **Layout Structure**:
    - **Row Headers Location**: B81:B140
    - **Column Headers Location**: E2:Q2, T2:FS2
    - **Data Range**:
      - Annual data: E81:Q140
      - Monthly data: T81:FS140
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined in the data, but implied to be a series of years based on the column structure.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Total Wages, Product Specialist Salary, % of Total Wages, People Costs, Add: Capitalized Wages, Less: Wages, Less: Outsourced R&D, Less: Commission (Duplicative), Adjusted People Costs, All-In Support Costs, Total Users (excl. Other), Financial Users, % Financial, Financial Support Costs, Corporate Users, % Corporate, Corporate Support Costs.
- **Notes & Customizations**: Values in columns E:Q and T:FS are scaled by 1000 in several rows.
