## 1. **Sheet Name**: (Assumed Sheet1, as the JSON doesn't explicitly name the sheet)

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of utilization metrics for different categories (Street - MH, Street - EVG, Terminal, Grand Total) and calculates utilization rates. It helps to understand how effectively the chassis are being used.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied, based on data and formula structure)
    - **Data Range**: G7:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21, inferred from `date_series_definitions.ds_1`)
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations and grand totals.

### Section Name: Cost and Revenue Assumptions
- **Section Type**: Assumptions Table
- **Description & Purpose**: This section outlines the cost and revenue assumptions used in the financial model, including M&R, Admin, and Repo costs, as well as usage days and rates.
- **Cell Range**: B16:Q19
- **Layout Structure**:
    - **Row Headers Location**: B17:C19
    - **Column Headers Location**: H16:Q16 (Implied, based on data and formula structure)
    - **Data Range**: E17:Q19
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21, inferred from `date_series_definitions.ds_1`)
    - **Frequency**: Annual
- **Key Components**: EVG, Per Usage Day, M&R, Admin, Repo, Usage Days, Contr. Days.
- **Notes & Customizations**: Includes cost per day calculations.

### Section Name: Chassis Usage and Revenue Projections
- **Section Type**: Revenue Forecast
- **Description & Purpose**: This section projects chassis usage, rates, and revenue for various categories, including Street - Trucker, EVG Street, and Terminal. It's used to forecast revenue based on different usage scenarios.
- **Cell Range**: B23:Q46
- **Layout Structure**:
    - **Row Headers Location**: B23:C43, B45
    - **Column Headers Location**: G21:Q21 (Year 0 to Year 10)
    - **Data Range**: H24:Q43, H46:Q46
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21, inferred from `date_series_definitions.ds_1`)
    - **Frequency**: Annual
- **Key Components**: Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Usage, Street Utilization, Revenue.
- **Notes & Customizations**: Includes calculations for usage, revenue, and utilization rates.

### Section Name: Cost Analysis
- **Section Type**: Cost Analysis
- **Description & Purpose**: This section analyzes costs associated with EVG Street and Terminal operations, including costs per usage day and total costs.
- **Cell Range**: B48:Q74
- **Layout Structure**:
    - **Row Headers Location**: B48:C74
    - **Column Headers Location**: H16:Q16 (Implied, based on data and formula structure)
    - **Data Range**: H46:Q46, H57:Q60, H61:Q63, H65:Q74
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21, inferred from `date_series_definitions.ds_1`)
    - **Frequency**: Annual
- **Key Components**: EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, EVG Average Cost per EVG Usage Day, Per Usage Day Costs (M&R, Admin, Repo, Other, Lease), M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Lease Cost, Total Cost.
- **Notes & Customizations**: Includes cost per day calculations and total cost analysis.

### Section Name: EBITDA and Margin Analysis
- **Section Type**: Profitability Analysis
- **Description & Purpose**: This section calculates EBITDA, EBITDA per usage day, EBITDA per chassis per day, and EBITDA margin.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76:C79
    - **Column Headers Location**: H16:Q16 (Implied, based on data and formula structure)
    - **Data Range**: H77:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21, inferred from `date_series_definitions.ds_1`)
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes EBITDA margin calculation.

### Section Name: Chassis Acquisition Costs
- **Section Type**: Investment Analysis
- **Description & Purpose**: This section details the costs associated with acquiring chassis, including the price per chassis, reconditioning costs, and other related expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98, B100
    - **Column Headers Location**: None (Single Point in Time)
    - **Data Range**: G83:G98, G100
- **Time Series Details**:
    - **Date Range**: Not Applicable (Upfront Costs)
    - **Frequency**: Not Applicable
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Premium / (Discount) to Book, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Less: Scrap Chassis, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: Includes calculations for total effective purchase price and cash multiple.

### Section Name: Cash Flow Analysis - Depreciated Value Exit
- **Section Type**: Cash Flow Projection
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit strategy, including investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, Capex, and cash flow.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B106:B115, F118, B117, B119
    - **Column Headers Location**: G104:Q104 (Year 0 to Year 10)
    - **Data Range**: H108:Q115, G117:Q117
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G104:Q104, inferred from `date_series_definitions.ds_1`)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for unlevered IRR and NPV.

### Section Name: Cash Flow Analysis - TEV Exit
- **Section Type**: Cash Flow Projection
- **Description & Purpose**: This section projects cash flows based on a TEV (Total Enterprise Value) exit strategy, including investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, Capex, and cash flow.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B132, B134, B136
    - **Column Headers Location**: G121:L121 (Year 0 to Year 5)
    - **Data Range**: H125:L132, G134:L134
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5 (G121:L121, inferred from `date_series_definitions.ds_3`)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes calculations for unlevered IRR.
