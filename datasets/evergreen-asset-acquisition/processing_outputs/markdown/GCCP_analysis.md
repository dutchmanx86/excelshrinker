## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of chassis across different categories (Street-MH, Street-EVG, Terminal) and calculates utilization rates. It provides a high-level overview of asset usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied: Years based on later sections)
    - **Data Range**: G6:Q8, H10:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (based on `date_series_definitions` and `G21:Q21`)
    - **Frequency**: Annual
- **Key Components**: Street-MH, Street-EVG, Terminal, Grand Total, % of Street-MH, % of Street-EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on the different categories.

### Section Name: Revenue and Cost Drivers
- **Section Type**: Custom P&L - Revenue and Cost Driver Analysis
- **Description & Purpose**: This section models the revenue and costs associated with chassis usage, including street and terminal operations. It projects revenue based on usage days, rates, and inflation assumptions. It also calculates per-day costs for various expense categories.
- **Cell Range**: B16:Q79
- **Layout Structure**:
    - **Row Headers Location**: B17:C79
    - **Column Headers Location**: H16, G21:Q21 (Years)
    - **Data Range**: E17:G19, H17:Q79 (excluding row headers)
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: M&R, Admin, Repo (upfront costs), Usage Days, Chassis Used per Day, Trucker Street Usage Days, EVG Street Rental Days, Terminal Usage Days, Revenue, EVG Street Costs, Terminal Billings, Per Usage Day Costs (M&R, Admin, Repo, Other), Total Cost, EBITDA, EBITDA Margin.
- **Notes & Customizations**: Includes inflation assumptions for various cost and revenue drivers. Calculates costs on both a total and per-usage-day basis.

### Section Name: Chassis Acquisition & Investment Analysis
- **Section Type**: Investment Analysis
- **Description & Purpose**: This section analyzes the costs associated with acquiring chassis, including the purchase price, reconditioning, and other related expenses. It calculates the total effective purchase price and provides metrics like cash multiple of EBITDA.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: None explicitly; single-column analysis.
    - **Data Range**: G83:G100
- **Time Series Details**:
    - **Date Range**: None. This is a static analysis.
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decoupling Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Scrap Chassis, Transaction Expenses, Total Effective Purchase Price.
- **Notes & Customizations**: Calculates the total investment required for chassis acquisition.

### Section Name: Cash Flow Projections - Depreciated Value Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit strategy. It calculates the investment and subsequent cash flows over a 10-year period.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Years)
    - **Data Range**: H108:Q117, E119
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G104:Q104)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes accelerated depreciation and working capital investment assumptions.

### Section Name: Cash Flow Projections - TEV Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit strategy. It calculates the investment and subsequent cash flows over a 5-year period.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Years)
    - **Data Range**: H125:L134, E136
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5 (G121:L121)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes accelerated depreciation and working capital investment assumptions. The exit multiple is specified.

### Section Name: Repeating Cash Flow Projections - TEV Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit strategy. It calculates the investment and subsequent cash flows over a 5-year period, repeating the same values.
- **Cell Range**: H129:L131
- **Layout Structure**:
    - **Row Headers Location**: None.
    - **Column Headers Location**: H129:L129 (Years)
    - **Data Range**: H130:L131
- **Time Series Details**:
    - **Date Range**: 1979-01-01 to 1979-01-01 (H129:L129)
    - **Frequency**: Annual values repeating 5 times from 1979 to 1979
- **Key Components**: Cash Flow.
- **Notes & Customizations**: Repeating values.
