## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of chassis utilization metrics, including street and terminal usage, and overall utilization rates. This section is used to assess the efficiency of chassis deployment.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**: G6:Q12
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate
- **Notes & Customizations**: Includes percentage calculations based on different usage categories.

### Section Name: Cost & Revenue Projections
- **Section Type**: Standard P&L
- **Description & Purpose**: Projects revenue and costs associated with chassis usage, including street and terminal revenue, M&R, Admin, and Repo costs. It calculates EBITDA and EBITDA margin.
- **Cell Range**: B16:Q79
- **Layout Structure**:
    - **Row Headers Location**: B17:B79, C19, C24, C29, C33, C37, C41, C57:C63, C77:C78
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**: H17:Q79 (excluding row headers)
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG, M&R, Admin, Repo, Usage Days, Contr. Days, Revenue, EVG Street Costs, Terminal Billings, M&R Cost, Admin Expense, Repo Expense, Total Cost, EBITDA, EBITDA Margin (%)
- **Notes & Customizations**: Includes per-usage-day cost calculations and inflation assumptions.

### Section Name: Chassis Acquisition & Total Purchase Price
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Calculates the total effective purchase price for chassis acquisition, considering factors like reconditioning costs, repositioning, and scrap chassis value.
- **Cell Range**: B82:G98
- **Layout Structure**:
    - **Row Headers Location**: B83:B98
    - **Column Headers Location**: G82
    - **Data Range**: G83:G98
- **Time Series Details**:
    - **Date Range**: N/A (Upfront costs)
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Scrap Chassis, Transaction Expenses, Total Effective Purchase Price
- **Notes & Customizations**: Includes calculations for premium/discount to book value and total effective purchase price.

### Section Name: Cash Flow Analysis - Depreciated Value Exit
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Projects cash flows based on a depreciated value exit strategy, including investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, capex, and cash flow.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B115, B117, B119
    - **Column Headers Location**: G104:Q104 (Years)
    - **Data Range**: H105:Q117
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV
- **Notes & Customizations**: Calculates unlevered IRR and NPV based on projected cash flows.

### Section Name: Cash Flow Analysis - TEV Exit
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Projects cash flows based on a Total Enterprise Value (TEV) exit strategy, including investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, capex, and cash flow.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B132, B134, B136
    - **Column Headers Location**: G121:L121 (Years)
    - **Data Range**: H122:L134
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR
- **Notes & Customizations**: Calculates unlevered IRR based on projected cash flows.
