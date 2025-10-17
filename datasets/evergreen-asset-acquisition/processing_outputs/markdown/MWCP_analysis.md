## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization rates and related metrics for different categories (Street - MH, Street - EVG, Terminal, Grand Total). It provides a high-level overview of asset usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H10:Q10, G11:Q11, H12:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on different categories.

### Section Name: EVG Cost Analysis
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: This section analyzes the costs associated with EVG operations, breaking them down by M&R, Admin, and Repo. It also includes calculations for per-usage-day costs.
- **Cell Range**: B16:Q19
- **Layout Structure**:
    - **Row Headers Location**: B17:B19, C18:C19
    - **Column Headers Location**: H16:Q16 (Usage Days, Contr. Days) and G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H17:I17
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG, M&R, Admin, Repo, Usage Days, Contr. Days, Per Usage Day, Per Contr. Day.
- **Notes & Customizations**: Includes cost breakdowns and per-day calculations.

### Section Name: Revenue and Usage Days Forecast
- **Section Type**: Revenue and Usage Forecast
- **Description & Purpose**: This section forecasts revenue based on usage days, rates, and inflation assumptions for Trucker Street, EVG Street, and Terminal operations.
- **Cell Range**: B21:Q46
- **Layout Structure**:
    - **Row Headers Location**: B23:B41, C24:C43
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H23:Q23, H24:Q26, H28:Q28, I29:Q29, H30:Q30, H32:Q32, H33, H34, H36:Q36, H37, H38, H40:Q41, H42:Q43, H45:Q45, H46:Q46
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Revenue.
- **Notes & Customizations**: Includes annual inflation assumptions for various rates and costs.

### Section Name: Cost per Usage Day Analysis
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: This section analyzes the cost per usage day for EVG Street and Terminal operations, including M&R, Admin, Repo, and other costs.
- **Cell Range**: B48:Q63
- **Layout Structure**:
    - **Row Headers Location**: B48:B54, C57:C63
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H48:Q49, H50:Q51, H52:Q54, H57:Q57, H58:Q60, I61:Q63
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, EVG Average Cost per EVG Usage Day, M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Lease Cost per Day.
- **Notes & Customizations**: Includes calculations for average costs per usage day.

### Section Name: Expense Forecast
- **Section Type**: Expense Forecast
- **Description & Purpose**: This section forecasts various expenses, including M&R, Admin, Repo, Other, Bad Debt, and Lease Costs.
- **Cell Range**: B65:Q74
- **Layout Structure**:
    - **Row Headers Location**: B65:B74
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H65:Q65, H66:Q68, H69:Q69, H70:Q73, H74:Q74
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Lease Cost, Total Cost.
- **Notes & Customizations**: Includes different types of lease costs and gain sharing.

### Section Name: EBITDA Analysis
- **Section Type**: Profitability Analysis
- **Description & Purpose**: This section calculates EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, and EBITDA Margin.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76:B79, C77:C78
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H77:Q78, H79:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes profitability metrics.

### Section Name: Chassis Acquisition Costs
- **Section Type**: Investment Analysis
- **Description & Purpose**: This section details the costs associated with acquiring chassis, including the price per chassis, reconditioning costs, and other related expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98, B100
    - **Column Headers Location**: None (Single Column)
    - **Data Range**: G83, G84, G85, G86, G87, G88, G89, G90, G91, G92, G93, G94, G95, G96, G97, G98, G100
- **Time Series Details**: None (Upfront Costs)
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Scrap Chassis, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: Includes a breakdown of various acquisition-related costs.

### Section Name: Cash Flows - Depreciated Value Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit scenario.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Years)
    - **Data Range**:
      - Annual data: H108:Q108, H109:Q109, H110:Q110, H111:Q114, H115:Q115, G117:Q117
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for IRR and NPV.

### Section Name: Cash Flows - TEV Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit scenario.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B121:B136
    - **Column Headers Location**: G121:L121 (Years)
    - **Data Range**:
      - Annual data: H125:L125, H126:L126, H127:L127, H128:L131, H132:L132, G134:L134
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes calculations for IRR and NPV.
