```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Revenue Build
- **Key Sections Identified**:
    - Header
    - Revenue Summary
    - ARR Waterfall - All Lead Types
    - ARR Waterfall - Inbound
    - ARR Waterfall - Enterprise
    - ARR Waterfall - Commercial
    - Revenue Reconciliation

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and units. Provides context for the entire sheet.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: B2:B4
- **Time Series Details**: N/A
- **Key Components**: LogRocket, Revenue Build, $ in 000s
- **Notes & Customizations**: None

### Revenue Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the revenue by lead type and provides a reconciliation to the P&L.
- **Cell Range**: B10:AH18
- **Layout Structure**:
    - **Row Headers Location**: B12:B18
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D13:R18
      - Monthly data: S13:AA18
      - Annual data: AC13:AH18
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S13:AA18)
        - Frequency: Monthly
- **Key Components**: Revenue, Revenue Reconciliation to P&L, Total Revenue, % growth
- **Notes & Customizations**: Revenue is scaled by 1000.

### ARR Waterfall - All Lead Types
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for all lead types, breaking down the components of growth and churn.
- **Cell Range**: A20:AH41
- **Layout Structure**:
    - **Row Headers Location**: B23:B31, B33, B36, B38:B41
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D24:R41
      - Monthly data: S24:AA41
      - Annual data: AC24:AH41
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S24:AA41)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### ARR Waterfall - Inbound
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for Inbound leads, breaking down the components of growth and churn.
- **Cell Range**: A43:AH60
- **Layout Structure**:
    - **Row Headers Location**: B44:B52, B55, B57:B60
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D45:R60
      - Monthly data: S45:AA60
      - Annual data: AC45:AH60
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S45:AA60)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### ARR Waterfall - Enterprise
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for Enterprise leads, breaking down the components of growth and churn.
- **Cell Range**: A62:AH80
- **Layout Structure**:
    - **Row Headers Location**: B63:B72, B75, B77:B80
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D65:R80
      - Monthly data: S65:AA80
      - Annual data: AC65:AH80
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S65:AA80)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### ARR Waterfall - Commercial
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for Commercial leads, breaking down the components of growth and churn.
- **Cell Range**: A82:AH99
- **Layout Structure**:
    - **Row Headers Location**: B82:B91, B94, B96:B99
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D84:R99
      - Monthly data: S84:AA99
      - Annual data: AC84:AH99
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S84:AA99)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### ARR Waterfall - Total Outbound
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for Total Outbound leads, breaking down the components of growth and churn.
- **Cell Range**: A101:AH118
- **Layout Structure**:
    - **Row Headers Location**: B101:B110, B113, B115:B118
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D103:R118
      - Monthly data: S103:AA118
      - Annual data: AC103:AH118
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S103:AA118)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### ARR Waterfall - Tradeshow
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for Tradeshow leads, breaking down the components of growth and churn.
- **Cell Range**: A120:AH137
- **Layout Structure**:
    - **Row Headers Location**: B120:B129, B132, B134:B137
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D122:R137
      - Monthly data: S122:AA137
      - Annual data: AC122:AH137
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S122:AA137)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### Revenue Reconciliation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Reconciles the revenue to the P&L.
- **Cell Range**: B139:AH140
- **Layout Structure**:
    - **Row Headers Location**: B139:B140
    - **Column Headers Location**: D7:R7, AC7:AH7
    - **Data Range**:
      - Annual data: D140:R140
      - Annual data: AC140:AH140
- **Time Series Details**:
    - Annual: 2018 to 2021
        - Frequency: Annual
    - Annual: 2018 to 2023
        - Frequency: Annual
- **Key Components**: Revenue Reconcilitaion to P&L
- **Notes & Customizations**: Revenue is scaled by 1000.
```