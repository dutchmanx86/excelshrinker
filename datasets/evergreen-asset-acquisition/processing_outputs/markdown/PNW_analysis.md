```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: PNW
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Upfront Investment Analysis
    - Cash Flow Projections (Depreciated Value Exit)
    - Cash Flow Projections (TEV Exit)
    - Annual Inflation Assumptions

## 2. Detailed Section Analysis

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of assets (chassis) across different categories (Street - MH, Street - EVG, Terminal) and calculates utilization rates. It provides a high-level overview of asset usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (implied years)
    - **Data Range**: G7:Q12
- **Time Series Details**:
    - **Date Range**: Implied years, likely 2015 to 2021 (based on other sections).
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate
- **Notes & Customizations**: The percentages provide a breakdown of utilization across different categories.

### Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section analyzes revenue and costs related to EVG Street and Terminal operations. It breaks down revenue by source (Trucker, EVG, Terminal) and costs by type (M&R, Admin, Repo, etc.). It helps understand the profitability drivers of the business.
- **Cell Range**: B16:Q74
- **Layout Structure**:
    - **Row Headers Location**: B17:B74, C19, C24, C29, C33, C37, C41, C42, C43, C57:C63
    - **Column Headers Location**: H16:Q16 (implied years)
    - **Data Range**: H17:Q74, E17:G19
- **Time Series Details**:
    - **Date Range**: Implied years, likely 2015 to 2021 (based on other sections).
    - **Frequency**: Annual
- **Key Components**: EVG Street Revenue, Terminal Revenue, Total Revenue, M&R Cost, Admin Expense, Repo Expense, Other Expense, Total Cost
- **Notes & Customizations**: Includes calculations for cost per usage day and various lease costs.

### EBITDA Calculation
- **Section Type**: Standard P&L (EBITDA section)
- **Description & Purpose**: This section calculates EBITDA and related metrics (EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin). It provides a measure of operating profitability.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76, C77, C78, B79
    - **Column Headers Location**: H76:Q76 (implied years)
    - **Data Range**: H76:Q79
- **Time Series Details**:
    - **Date Range**: Implied years, likely 2015 to 2021 (based on other sections).
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%)
- **Notes & Customizations**: EBITDA is calculated based on the revenue and cost analysis above.

### Upfront Investment Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the upfront investment required for the transaction, including the purchase price of chassis, reconditioning costs, and working capital investment. It provides a summary of the initial cash outlay.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: G82 (Total (Upfront))
    - **Data Range**: G83:G100, F88
- **Time Series Details**:
    - **Date Range**: Single point in time (Upfront).
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Total Chassis Price, Reconditioning Costs, Working Capital Investment, Total Effective Purchase Price
- **Notes & Customizations**: Includes adjustments for scrap chassis and transaction expenses.

### Cash Flow Projections (Depreciated Value Exit)
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit scenario. It includes EBITDA, depreciation, taxes, working capital investment, and capex. It calculates total cash flows, NPV, and unlevered IRR.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B104:B119
    - **Column Headers Location**: H104:Q104 (implied years)
    - **Data Range**: G104:Q117, E111, E113, E119, F119
- **Time Series Details**:
    - **Date Range**: Implied years, likely 2015 to 2021 (based on other sections).
    - **Frequency**: Annual
- **Key Components**: EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR
- **Notes & Customizations**: Includes a calculation for NPV.

### Cash Flow Projections (TEV Exit)
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit scenario. It includes EBITDA, depreciation, taxes, working capital investment, and capex. It calculates total cash flows, and unlevered IRR.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B121:B136
    - **Column Headers Location**: H125:L125 (implied years)
    - **Data Range**: G122:L134, E128, E130, E136
- **Time Series Details**:
    - **Date Range**: Implied years, likely 2015 to 2020 (based on other sections).
    - **Frequency**: Annual
- **Key Components**: EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR
- **Notes & Customizations**: Includes a calculation for exit value.

### Annual Inflation Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section lists the annual inflation assumptions used in the model for various cost and revenue components.
- **Cell Range**: U32:V41
- **Layout Structure**:
    - **Row Headers Location**: U33:U41
    - **Column Headers Location**: U32 (Annual Inflation Assumptions:)
    - **Data Range**: V33:V41
- **Time Series Details**:
    - **Date Range**: Single point in time (Assumptions).
    - **Frequency**: N/A
- **Key Components**: Trucker Rate Inflation, EVG Rate Inflation, Terminal Rate Inflation, M&R Cost Inflation, Admin Cost Inflation, Repo Cost Inflation, Other Cost Inflation
- **Notes & Customizations**: These assumptions drive the growth rates in the projected financials.
```