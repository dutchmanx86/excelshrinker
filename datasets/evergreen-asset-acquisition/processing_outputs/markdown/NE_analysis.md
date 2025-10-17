## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of utilization metrics for different categories (Street - MH, Street - EVG, Terminal, Grand Total) and calculates utilization rates. It helps in understanding the efficiency of chassis usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied Year 0 to Year 10 from G21:Q21)
    - **Data Range**: G6:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations and grand totals.

### Section Name: Cost and Revenue Drivers
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the key cost and revenue drivers related to EVG operations, including M&R, Admin, Repo costs, and usage days. It's used to project revenue and costs based on usage and rates.
- **Cell Range**: B16:Q46
- **Layout Structure**:
    - **Row Headers Location**: B17:B46, C18:C43
    - **Column Headers Location**: G21:Q21 (Years 0 to 10)
    - **Data Range**: E17:Q46
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG, M&R, Admin, Repo, Usage Days, Contr. Days, Per Usage Day, Per Contr. Day, Chassis Used per Day, Street - Trucker, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Usage, Street Utilization, Revenue.
- **Notes & Customizations**: Includes annual inflation assumptions for various rates and costs, located in column U.

### Section Name: Cost Analysis
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: This section breaks down costs related to EVG operations, including per-usage-day costs, M&R, Admin, Repo, Lease costs, and total costs. It is used to calculate EBITDA and EBITDA margins.
- **Cell Range**: B48:Q79
- **Layout Structure**:
    - **Row Headers Location**: B48:B79, C57:C63, C77:C78
    - **Column Headers Location**: H21:Q21 (Years 0 to 10)
    - **Data Range**: H46:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, Per Usage Day Costs, M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Other Cost per Day, Lease Costs, M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Total Cost, EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes calculations for average costs per usage day and EBITDA margin.

### Section Name: Chassis Acquisition & Investment Analysis
- **Section Type**: Investment Analysis
- **Description & Purpose**: This section analyzes the costs associated with acquiring chassis, including purchase price, reconditioning, decoupling, repositioning, retitling, working capital investment, offhire costs, and scrap chassis. It calculates the total effective purchase price and provides metrics like cash multiple of EBITDA.
- **Cell Range**: B82:Q100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: G21:Q21 (Years 0 to 10)
    - **Data Range**: G83:Q98
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Scrap Chassis, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: Includes calculations for total effective purchase price and cash multiple of EBITDA.

### Section Name: Cash Flow Analysis - Depreciated Value Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit scenario. It includes investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, Capex, and cash flow. It calculates NPV and Unlevered IRR.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Years 0 to 10)
    - **Data Range**: H108:Q117, E111:E119
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for NPV and Unlevered IRR.

### Section Name: Cash Flow Analysis - TEV Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit scenario. It includes investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, Capex, and cash flow. It calculates NPV and Unlevered IRR.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Years 0 to 5)
    - **Data Range**: H125:L134, E128:E136
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes calculations for NPV and Unlevered IRR.
