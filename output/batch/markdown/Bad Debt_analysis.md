## 1. Spreadsheet Overview
- **Sheet Name**: Bad Debt
- **Key Sections Identified**:
    - Reconciliation Header
    - AFDA Reconciliation Table

## 2. Detailed Section Analysis

### Section Name: Reconciliation Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the reconciliation.
- **Cell Range**: B2:B2
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: B2:B2
- **Time Series Details**: N/A
- **Key Components**: ADFDA Reconciliation 2020
- **Notes & Customizations**: Simple title for the sheet.

### Section Name: AFDA Reconciliation Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section reconciles the Allowance for Doubtful Accounts (AFDA) balance between a working paper (WP) and Intacct (accounting software), calculating the necessary adjustment to the AFDA.
- **Cell Range**: B5:CT21
- **Layout Structure**:
    - **Row Headers Location**: B6:B21
    - **Column Headers Location**: C5:CT5
    - **Data Range**: C6:CT21
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: ADFA beg balance per WP, ADFA beg balance per Intacct, Invoices written-off/collected, AFDA balance before adj, A/R ending balance per Intacct, AFDA as % of A/R to be maintained, 3.18% of current A/R, Less: AFDA balance before adj, Amount to be added to AFDA, AFDA end balance per WP, ADFA end balance per Intacct, Difference
- **Notes & Customizations**: The table calculates the difference between the required AFDA balance (based on a percentage of A/R) and the existing balance, determining the necessary adjustment. Values are scaled by 1000.
