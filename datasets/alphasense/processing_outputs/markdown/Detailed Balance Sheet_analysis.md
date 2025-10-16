```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Detailed Balance Sheet
- **Key Sections Identified**:
    - Header
    - Assets
    - Liabilities
    - Equity
    - Liabilities & Equity Total & Check

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report.
- **Cell Range**: A1:A1
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: A1
- **Time Series Details**: None
- **Key Components**: Balance Sheet
- **Notes & Customizations**: None

### Section Name: Assets
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's assets, broken down into current, long-term, and fixed assets.
- **Cell Range**: A4:BV32
- **Layout Structure**:
    - **Row Headers Location**: A4:D30
    - **Column Headers Location**: E3:BV3
    - **Data Range**:
      - Monthly data: F7:BV30
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the JSON, but inferred from the data range F7:BV30. The "Actual" string is present in S2:BV2, suggesting a monthly time series. Assuming the data starts a reasonable period before the "detected_at" date (2025-10-15), a plausible range is 2023-01-31 to 2025-09-30.
    - **Frequency**: Monthly
- **Key Components**: Current Assets (Cash, Accounts Receivable, Prepaid Expenses), Long Term Assets (Other Long Term Assets), Fixed Assets (Capitalized R&D).
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Liabilities
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's liabilities, broken down into current and long-term liabilities.
- **Cell Range**: A34:BV83
- **Layout Structure**:
    - **Row Headers Location**: A34:D82
    - **Column Headers Location**: E3:BV3
    - **Data Range**:
      - Monthly data: F37:BV82
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the JSON, but inferred from the data range F37:BV82. The "Actual" string is present in S2:BV2, suggesting a monthly time series. Assuming the data starts a reasonable period before the "detected_at" date (2025-10-15), a plausible range is 2023-01-31 to 2025-09-30.
    - **Frequency**: Monthly
- **Key Components**: Current Liabilities (Accounts Payable, Accrued Expenses, Deferred Revenue), Long Term Liabilities (Long-term loan from credit institution, Convertible Notes).
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Equity
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's equity accounts.
- **Cell Range**: A87:BV98
- **Layout Structure**:
    - **Row Headers Location**: A87:D97
    - **Column Headers Location**: E3:BV3
    - **Data Range**:
      - Monthly data: F88:BV97
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the JSON, but inferred from the data range F88:BV97. The "Actual" string is present in S2:BV2, suggesting a monthly time series. Assuming the data starts a reasonable period before the "detected_at" date (2025-10-15), a plausible range is 2023-01-31 to 2025-09-30.
    - **Frequency**: Monthly
- **Key Components**: Common Stock, Preferred Series A, Net Income, Retained Earnings.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Liabilities & Equity Total & Check
- **Section Type**: Balance Sheet
- **Description & Purpose**: Calculates the total liabilities and equity and includes a check to ensure the balance sheet balances.
- **Cell Range**: A100:BV101
- **Layout Structure**:
    - **Row Headers Location**: A100:A101
    - **Column Headers Location**: E3:BV3
    - **Data Range**:
      - Monthly data: F100:BV101
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the JSON, but inferred from the data range F100:BV101. The "Actual" string is present in S2:BV2, suggesting a monthly time series. Assuming the data starts a reasonable period before the "detected_at" date (2025-10-15), a plausible range is 2023-01-31 to 2025-09-30.
    - **Frequency**: Monthly
- **Key Components**: Total Liabilities & Equity, Check.
- **Notes & Customizations**: Values are scaled by 1000.
```