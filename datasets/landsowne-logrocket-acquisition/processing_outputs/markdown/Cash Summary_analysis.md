```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Cash Summary
- **Key Sections Identified**:
    - Header
    - Cash Balance Waterfall

## 2. Detailed Section Analysis

### Section Name (Header)
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and units for the data presented.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: B2:B4
    - **Column Headers Location**: N/A
    - **Data Range**: N/A
- **Time Series Details**: N/A
- **Key Components**: LogRocket, $ in 000s
- **Notes & Customizations**: This section provides context for the entire sheet.

### Section Name (Cash Balance Waterfall)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a waterfall analysis of the cash balance, showing the beginning balance, net cash burn, and ending balance. It includes both actual (A) and estimated (E) values.
- **Cell Range**: B12:AH15
- **Layout Structure**:
    - **Row Headers Location**: B13:B15
    - **Column Headers Location**: D7:AH8 (multiple time series)
    - **Data Range**:
      - Annual data: R13:AA15
      - Annual data: AF13:AH15
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018A to 2021E (using CY2018A, CY2019A, CY2020A, CY2021E headers)
      - Annual: 2022E to 2023E (using CY2022E, CY2023E headers)
    - **Frequency**: Annual
- **Key Components**: Beginning Cash Balance, Net Cash Burn From Operations, Ending Cash Balance
- **Notes & Customizations**: The data is presented in thousands of dollars. There are two separate blocks of annual data, one from columns R to AA, and another from columns AF to AH.
```