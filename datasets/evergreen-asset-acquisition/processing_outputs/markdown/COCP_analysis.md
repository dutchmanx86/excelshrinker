## 1. **Sheet Name**: Evergreen

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of chassis utilization metrics across different categories (Street - MH, Street - EVG, Terminal, Grand Total) and calculates utilization rates. It helps to understand how effectively the chassis are being used.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied, based on data and other sections)
    - **Data Range**: G6:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes calculations for percentages and utilization rates.

### Cost and Revenue Drivers
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the key cost and revenue drivers, broken down by M&R, Admin, and Repo. It also includes usage days and contributed days. This section is used to understand the cost structure and revenue generation.
- **Cell Range**: B16:Q19
- **Layout Structure**:
    - **Row Headers Location**: B17:C19
    - **Column Headers Location**: E16:Q16 (Implied, based on data and other sections)
    - **Data Range**: E17:Q19
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: EVG (M&R, Admin, Repo, Usage Days, Contr. Days), Per Usage Day, Per Contr. Day.
- **Notes & Customizations**: Includes costs per usage day and per contributed day.

### Chassis Usage and Revenue Projections
- **Section Type**: Revenue and Cost Projection
- **Description & Purpose**: Projects chassis usage, rates, and revenue for different categories (Street - Trucker, EVG Street, Terminal). It also includes annual inflation assumptions for various rates and costs. This section is used to forecast revenue and costs based on usage and rates.
- **Cell Range**: B21:Q43
- **Layout Structure**:
    - **Row Headers Location**: B23:C43
    - **Column Headers Location**: G21:Q21
    - **Data Range**: H23:Q43
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Usage, Street Utilization.
- **Notes & Customizations**: Includes annual inflation assumptions for various rates and costs (U32:V41).

### Revenue and Cost Analysis
- **Section Type**: Revenue and Cost Analysis
- **Description & Purpose**: Analyzes revenue, costs, and profitability metrics. It includes revenue projections, cost breakdowns (EVG Street Costs, Terminal Billings), and per-day cost analysis. This section is used to understand the profitability of the business.
- **Cell Range**: B45:Q79
- **Layout Structure**:
    - **Row Headers Location**: B45:C79
    - **Column Headers Location**: H46:Q46 (Implied, based on data and other sections)
    - **Data Range**: H46:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, EVG Average Cost per EVG Usage Day, Per Usage Day Costs (M&R, Admin, Repo, Other, Lease), M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Lease Cost, Total Cost, EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes calculations for per-day costs and profitability metrics.

### Chassis Acquisition Cost
- **Section Type**: Investment Analysis
- **Description & Purpose**: Details the costs associated with acquiring chassis, including the price per chassis, reconditioning costs, decoupling costs, repositioning costs, retitling & stenciling costs, working capital investment, offhire costs, and transaction expenses. It also calculates the total effective purchase price and cash multiple of EBITDA.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: G82 (Total (Upfront))
    - **Data Range**: G83:G100
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Premium / (Discount) to Book, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Less: Scrap Chassis, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: Includes calculations for the total effective purchase price and cash multiple of EBITDA.

### Cash Flow Projections (Depreciated Value Exit)
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: Projects cash flows based on a depreciated value exit scenario. It includes investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, capex, and cash flow. It also calculates the unlevered IRR and NPV.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104
    - **Data Range**: H108:Q115
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G104:Q104)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for unlevered IRR and NPV.

### Cash Flow Projections (TEV Exit)
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: Projects cash flows based on a Total Enterprise Value (TEV) exit scenario. It includes investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, capex, and cash flow.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121
    - **Data Range**: H125:L132
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5 (G121:L121)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes calculations for unlevered IRR. The exit multiple is specified in E123.
