## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of utilization metrics, including percentages of street and terminal usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied Years based on later time series)
    - **Data Range**: G6:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (based on `date_series_definitions` and G21:Q21)
    - **Frequency**: Annual
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on street and terminal usage.

### Section Name: Cost and Revenue Drivers
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the key drivers of cost and revenue, including rates, usage days, and resulting revenue/costs.
- **Cell Range**: B16:Q46
- **Layout Structure**:
    - **Row Headers Location**: B17:C43
    - **Column Headers Location**: H16:Q16, G21:Q21 (Years)
    - **Data Range**: E17:Q46
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: M&R, Admin, Repo costs, Usage Days, Trucker Street Usage Days, EVG Street Rental Days, Terminal Usage Days, Total Usage Days, Revenue.
- **Notes & Customizations**: Includes annual inflation assumptions in U32:V41.

### Section Name: Revenue and Cost Analysis
- **Section Type**: Standard P&L (Partial)
- **Description & Purpose**: Analyzes revenue, costs, and profitability metrics.
- **Cell Range**: B45:Q79
- **Layout Structure**:
    - **Row Headers Location**: B45:C79
    - **Column Headers Location**: H46:Q46, G21:Q21 (Years)
    - **Data Range**: H46:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, M&R Cost, Admin Expense, Repo Expense, Total Cost, EBITDA, EBITDA Margin (%).
- **Notes & Customizations**: Includes per usage day costs and profitability metrics. Contains a repeating annual series from 2080 to 2080 in H71:Q71.

### Section Name: Chassis Acquisition
- **Section Type**: Investment Analysis
- **Description & Purpose**: Details the costs associated with chassis acquisition.
- **Cell Range**: B82:G98
- **Layout Structure**:
    - **Row Headers Location**: B83:B98
    - **Column Headers Location**: G82
    - **Data Range**: G83:G98
- **Time Series Details**:
    - **Date Range**: Not applicable (Upfront costs)
    - **Frequency**: Not applicable
- **Key Components**: Chassis to be Acquired, Price per Chassis, Total Chassis Price, Reconditioning Costs, Transaction Expenses, Total Effective Purchase Price.
- **Notes & Customizations**: Calculates the total cost of acquiring chassis, including various related expenses.

### Section Name: Investment Analysis - Depreciated Value Exit
- **Section Type**: Investment Analysis
- **Description & Purpose**: Analyzes cash flows with a depreciated value exit strategy.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Years)
    - **Data Range**: H108:Q117
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G104:Q104)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Calculates IRR and NPV based on projected cash flows and a depreciated value exit.

### Section Name: Investment Analysis - TEV Exit
- **Section Type**: Investment Analysis
- **Description & Purpose**: Analyzes cash flows with a Total Enterprise Value (TEV) exit strategy.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Years)
    - **Data Range**: H125:L134
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5 (G121:L121)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Calculates IRR based on projected cash flows and a TEV exit.
