```markdown
## 1. **Sheet Name**: Sheet1

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of utilization metrics for different categories (Street - MH, Street - EVG, Terminal, Grand Total) and their respective percentages. It helps to understand the efficiency of chassis usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied "Year 0" to "Year 10" from date series)
    - **Data Range**:
      - Annual data: G7:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on different categories.

### Cost Breakdown (EVG)
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: Breaks down the costs associated with EVG (Evergreen) operations, including M&R, Admin, and Repo costs, both in total and per usage day/contributed day.
- **Cell Range**: B16:Q19
- **Layout Structure**:
    - **Row Headers Location**: B17:C19
    - **Column Headers Location**: H16:Q16 (Implied "Year 0" to "Year 10" from date series)
    - **Data Range**:
      - Annual data: E17:Q19
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: M&R, Admin, Repo, Per Usage Day, Per Contr. Day.
- **Notes & Customizations**: The table shows both total costs and costs per usage/contributed day.

### Chassis Usage and Revenue Forecast
- **Section Type**: Revenue and Usage Forecast
- **Description & Purpose**: Forecasts chassis usage, rates, and revenue for different segments (Trucker Street, EVG Street, Terminal) over a 10-year period. Also includes inflation assumptions.
- **Cell Range**: B21:Q46
- **Layout Structure**:
    - **Row Headers Location**: B23:C43
    - **Column Headers Location**: G21:Q21 (Year 0 to Year 10)
    - **Data Range**:
      - Annual data: H23:Q43
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Usage, Street Utilization, Revenue.
- **Notes & Customizations**: Includes annual inflation assumptions for various rates and costs.

### Cost Analysis per Usage Day
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: Analyzes costs per usage day for various expense categories.
- **Cell Range**: B45:Q63
- **Layout Structure**:
    - **Row Headers Location**: B45:C63
    - **Column Headers Location**: H46:Q46 (Implied "Year 0" to "Year 10" from date series)
    - **Data Range**:
      - Annual data: H46:Q63
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, EVG Average Cost per EVG Usage Day, Per Usage Day Costs, M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Other Cost per Day, Lease Cost per Day on EVG Chassis, Lease Cost per Day on EVG Leases, Incremental Pool Overuse Cost per Day.
- **Notes & Customizations**: Includes calculations for average costs per usage day.

### Expense Forecast
- **Section Type**: Expense Forecast
- **Description & Purpose**: Forecasts various expenses including M&R, Admin, Repo, Other, Bad Debt, and Lease Costs.
- **Cell Range**: B65:Q74
- **Layout Structure**:
    - **Row Headers Location**: B65:B74
    - **Column Headers Location**: H66:Q66 (Implied "Year 0" to "Year 10" from date series)
    - **Data Range**:
      - Annual data: H65:Q74
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Lease Cost on EVG Owned Chassis, Lease Cost on EVG Existing Leases, Lease Cost for Additional Capactiy, Gain Sharing with EVG on MH Conversion, Total Cost.
- **Notes & Customizations**: Includes different types of lease costs.

### EBITDA and Margin Analysis
- **Section Type**: Profitability Analysis
- **Description & Purpose**: Calculates EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, and EBITDA Margin.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76:C79
    - **Column Headers Location**: H77:Q77 (Implied "Year 0" to "Year 10" from date series)
    - **Data Range**:
      - Annual data: H77:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes calculations for EBITDA per usage day and per chassis per day.

### Chassis Acquisition Costs
- **Section Type**: Investment Analysis
- **Description & Purpose**: Calculates the total cost of acquiring chassis, including purchase price, reconditioning costs, and other related expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98
    - **Column Headers Location**: G82 (Single Column)
    - **Data Range**:
      - Annual data: G83:G98
- **Time Series Details**:
    - **Date Range**: Not time series, but related to upfront investment.
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Less: Scrap Chassis, Transaction Expenses, Total Effective Purchase Price.
- **Notes & Customizations**: Includes various costs associated with chassis acquisition.

### Cash Flow Analysis - Depreciated Value Exit
- **Section Type**: Cash Flow Projection
- **Description & Purpose**: Projects cash flows based on a depreciated value exit scenario.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Year 0 to Year 10)
    - **Data Range**:
      - Annual data: H108:Q117
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for Unlevered IRR and NPV.

### Cash Flow Analysis - TEV Exit
- **Section Type**: Cash Flow Projection
- **Description & Purpose**: Projects cash flows based on a Total Enterprise Value (TEV) exit scenario.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Year 0 to Year 5)
    - **Data Range**:
      - Annual data: H125:L134
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes calculations for Unlevered IRR.
```