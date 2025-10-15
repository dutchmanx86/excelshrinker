## 1. Spreadsheet Overview
- **Sheet Name**: Fleet Summary - Pending
- **Key Sections Identified**:
    - Header Information
    - Assumptions
    - Chassis Age Analysis

## 2. Detailed Section Analysis

### Section Name: Header Information
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the report.
- **Cell Range**: A1:A3
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: None
    - **Data Range**: A1:A3
- **Time Series Details**: None
- **Key Components**: Company Name, Report Title
- **Notes & Customizations**: Basic header information.

### Section Name: Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains key assumptions used in the analysis, such as Value New, Residual Value, and Useful Life.
- **Cell Range**: B5:C7
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C5:C7
- **Time Series Details**: None
- **Key Components**: Value New, Residual Value, Useful Life
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: ASI/CSG Premium
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains ASI/CSG Premium value.
- **Cell Range**: B8:D10
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: D10
- **Time Series Details**: None
- **Key Components**: Premium, ASI/CSG
- **Notes & Customizations**: Single value.

### Section Name: Chassis Age Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes chassis based on age, providing counts, percentages, and value calculations.
- **Cell Range**: B11:M13
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 11
    - **Data Range**: D12:M13
- **Time Series Details**: None
- **Key Components**: Year, Date Estimate, Count, % of total, Book Value Per, Purchase Per, Total Purchase, Age 10 years Later, Depreciated 10 year value per, Depreciated 10 year value total
- **Notes & Customizations**: Values are scaled by 1000. Contains calculations for 10-year depreciation.

### Section Name: Chassis Age Analysis - Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of chassis book values.
- **Cell Range**: B16:C38
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C19:C38
- **Time Series Details**: None
- **Key Components**: Book Value, PO
- **Notes & Customizations**: Values are scaled by 1000.
