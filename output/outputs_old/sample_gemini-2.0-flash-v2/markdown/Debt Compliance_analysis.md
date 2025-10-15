## 1. Spreadsheet Overview
- **Sheet Name**: Debt Compliance
- **Key Sections Identified**:
    - Revenue Growth Rate
    - Debt Compliance Check
    - Liquidity Analysis
    - Liquidity Buffer Analysis

## 2. Detailed Section Analysis

### Revenue Growth Rate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the revenue and its growth rate.
- **Cell Range**: A5:EC9
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Rows 2 and 3 for annual and monthly data, respectively.
    - **Data Range**:
      - Annual data: C7:L9
      - Monthly data: N7:EC9
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2027
      - Monthly: 2018-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Revenue, T3M, Growth Rate
- **Notes & Customizations**: T3M data is scaled by 1000.

### Debt Compliance Check
- **Section Type**: Compliance Check
- **Description & Purpose**: Checks compliance with growth covenants.
- **Cell Range**: A11:EC44
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 1 for quarterly data.
    - **Data Range**:
      - Quarterly data: AO11:EC44
- **Time Series Details**:
    - **Date Range**: Q1 2018 to Q4 2027
    - **Frequency**: Quarterly
- **Key Components**: Growth Covenant, OK, Breaks
- **Notes & Customizations**: "OK" indicates compliance. "Breaks" indicates a breach of the covenant.

### Liquidity Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes the company's liquidity position.
- **Cell Range**: A15:EC44
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Rows 2 and 3 for annual and monthly data, respectively.
    - **Data Range**:
      - Annual data: C24:L28
      - Monthly data: N17:EC44
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2027
      - Monthly: 2018-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Remaining Months Liquidity (RML), Total Borrowings, Total Availability, Net Availability + Unrestricted Cash, EBITDA, Capitalized R&D, Capitalized Expenditures, Change in Deferred Revenue, Adjusted EBITDA, RML, Liquidity Threshold, Restricted Cash, Net Availability, Liquidity, Thershold, Compliance Check
- **Notes & Customizations**: Some data is scaled by 1000.

### Liquidity Buffer Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes the company's liquidity buffer.
- **Cell Range**: A48:EC52
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Rows 2 and 3 for annual and monthly data, respectively.
    - **Data Range**:
      - Monthly data: AP48:EC52
- **Time Series Details**:
    - **Date Range**: 2018-01-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: $5m Liquidity Buffer, RML Liquidity Buffer, Overall Liqudity Buffer
- **Notes & Customizations**: Some data is scaled by 1000.
