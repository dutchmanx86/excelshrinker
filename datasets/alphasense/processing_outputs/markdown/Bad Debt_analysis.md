## 1. Spreadsheet Overview
- **Sheet Name**: Bad Debt
- **Key Sections Identified**:
    - Reconciliation Header
    - AFDA Reconciliation

## 2. Detailed Section Analysis

### Section Name (Reconciliation Header)
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the reconciliation.
- **Cell Range**: B2:CT2
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: B2
- **Time Series Details**: None
- **Key Components**: Title: "ADFDA Reconciliation 2020"
- **Notes & Customizations**: None

### Section Name (AFDA Reconciliation)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section reconciles the Allowance for Doubtful Accounts (AFDA) balance between two sources (WP and Intacct) over a monthly time series.
- **Cell Range**: B5:CT21
- **Layout Structure**:
    - **Row Headers Location**: B6:B21
    - **Column Headers Location**: C5:CT5
    - **Data Range**: C6:CT21
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2027-12-01 (C5:CT5). Anchor points: C5=2020-01-01, O5=2021-01-01, AA5=2022-01-01, AM5=2023-01-01, AY5=2024-01-01, BK5=2025-01-01, BW5=2026-01-01, CI5=2027-01-01
    - **Frequency**: Monthly
- **Key Components**: ADFA beg balance per WP, ADFA beg balance per Intacct, Invoices written-off/collected, AFDA balance before adj, A/R ending balance per Intacct, AFDA as % of A/R to be maintained, Amount to be added to AFDA, AFDA end balance per WP, ADFA end balance per Intacct, Difference.
- **Notes & Customizations**: Values are scaled by 1000. Includes a calculation for "AFDA as % of A/R to be maintained" and an adjustment to the AFDA balance.
