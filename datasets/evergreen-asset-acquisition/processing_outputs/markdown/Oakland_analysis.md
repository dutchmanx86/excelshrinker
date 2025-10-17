## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of chassis across different categories (Street - MH, Street - EVG, Terminal, Grand Total) and calculates utilization rates. It provides a high-level overview of how effectively the chassis are being used.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied Year 0 to Year 10 from date_series_definitions)
    - **Data Range**: G6:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on the different categories.

### Section Name: Cost and Revenue Assumptions
- **Section Type**: Custom P&L
- **Description & Purpose**: This section projects revenue and costs associated with chassis usage, including M&R, Admin, and Repo costs. It calculates revenue based on usage days and rates, and projects costs based on per-day costs.
- **Cell Range**: B16:Q79
- **Layout Structure**:
    - **Row Headers Location**: B17:B79, C18:C19, C24, C29, C33, C37, C41, C57:C63
    - **Column Headers Location**: G21:Q21 (Year 0 to Year 10)
    - **Data Range**:
      - Annual data: H17:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG, M&R, Admin, Repo, Usage Days, Contr. Days, Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Revenue, EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, Per Usage Day Costs, M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Other Cost per Day, Lease Cost per Day, M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Lease Cost, Total Cost, EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes per-day cost calculations, lease costs, and gain sharing. Contains inflation assumptions in column U.

### Section Name: Purchase Price Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the total effective purchase price for the chassis acquisition, including chassis price, reconditioning costs, decoupling costs, repositioning, retitling & stenciling costs, working capital investment, offhire costs, scrap chassis value, and transaction expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: None (Single Point in Time)
    - **Data Range**: G83:G100
- **Time Series Details**:
    - **Date Range**: N/A
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Premium / (Discount) to Book, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Less: Scrap Chassis, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: Includes a calculation of the cash multiple of 2014 EBITDA.

### Section Name: Cash Flow Analysis - Depreciated Value Exit
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit scenario. It includes investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, capex, and cash flow. It calculates the unlevered IRR and NPV.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Year 0 to Year 10)
    - **Data Range**: H108:Q117, E111:E113, E119
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for accelerated depreciation and working capital investment.

### Section Name: Cash Flow Analysis - TEV Exit
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit scenario. It includes investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, capex, and cash flow. It calculates the unlevered IRR.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Year 0 to Year 5)
    - **Data Range**: H125:L134, E128, E130, E136
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes an exit multiple calculation.
