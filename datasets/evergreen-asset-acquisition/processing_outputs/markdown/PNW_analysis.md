## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary

- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of utilization metrics for different categories (Street-MH, Street-EVG, Terminal, Grand Total) and calculates utilization rates. It helps understand how effectively the chassis are being used.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**: H6:Q8, H10:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on different categories.

### Section Name: Cost and Revenue Drivers

- **Section Type**: Revenue and Cost Driver Analysis
- **Description & Purpose**: This section analyzes the key drivers of revenue and costs, including usage days, rates, and inflation assumptions. It is used for forecasting revenue and expenses.
- **Cell Range**: B16:Q43
- **Layout Structure**:
    - **Row Headers Location**: B17:C43
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**: H17:Q43, E17:G17
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: M&R, Admin, Repo, Usage Days, Contr. Days, Per Usage Day, Per Contr. Day, Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Usage, Street Utilization, Annual Inflation Assumptions (Trucker Rate Inflation, EVG Rate Inflation, Terminal Rate Inflation, M&R Cost Inflation, Admin Cost Inflation, Repo Cost Inflation, Other Cost Inflation).
- **Notes & Customizations**: Includes inflation assumptions for various cost and revenue components.

### Section Name: Revenue and Cost Summary

- **Section Type**: Summary P&L
- **Description & Purpose**: This section summarizes the revenue, costs, and EBITDA, providing a high-level overview of the financial performance.
- **Cell Range**: B45:Q79
- **Layout Structure**:
    - **Row Headers Location**: B45:C79
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**: H46:Q79, E18:G19
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, EVG Average Cost per EVG Usage Day, EVG Average Cost per EVG Street Day, EVG Terminal Cost per Terminal Day, Per Usage Day Costs (M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Other Cost per Day, Lease Cost per Day on EVG Chassis, Lease Cost per Day on EVG Leases, Incremental Pool Overuse Cost per Day), M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Lease Cost on EVG Owned Chassis, Lease Cost on EVG Existing Leases, Lease Cost for Additional Capactiy, Gain Sharing with EVG on MH Conversion, Total Cost, EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes calculations for EBITDA per usage day and EBITDA margin.

### Section Name: Initial Investment

- **Section Type**: Initial Investment Analysis
- **Description & Purpose**: This section details the upfront investment required, including chassis acquisition costs, reconditioning, and other related expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: None (Single Column)
    - **Data Range**: G83:G98
- **Time Series Details**:
    - **Date Range**: Not Applicable (Upfront Costs)
    - **Frequency**: Not Applicable
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Premium / (Discount) to Book, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Less: Scrap Chassis at $1,000 per Chassis, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: Calculates the total effective purchase price based on various cost components.

### Section Name: Cash Flow Analysis - Depreciated Value Exit

- **Section Type**: Discounted Cash Flow Analysis
- **Description & Purpose**: This section calculates the cash flows, NPV, and IRR based on a depreciated value exit scenario.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Years)
    - **Data Range**: H108:Q115
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for accelerated depreciation and working capital investment.

### Section Name: Cash Flow Analysis - TEV Exit

- **Section Type**: Discounted Cash Flow Analysis
- **Description & Purpose**: This section calculates the cash flows, NPV, and IRR based on a Total Enterprise Value (TEV) exit scenario.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Years)
    - **Data Range**: H125:L132
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for accelerated depreciation and working capital investment.
