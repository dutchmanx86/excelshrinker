## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level overview of chassis utilization metrics, including billed days, percentages of total, and utilization rates. This section helps assess the efficiency of chassis usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implicitly, years are across columns)
    - **Data Range**:
      - Annual data: G6:Q8, H10:Q10, G11:Q11, H12:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: Street - MH, Net Lease Billed Days, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentages calculated against different base values.

### Section Name: Cost and Revenue Drivers
- **Section Type**: Custom P&L
- **Description & Purpose**: This section models the key revenue and cost drivers for the business, projecting revenue from various sources (Trucker Street, Net Lease, Terminal) and associated costs. It's used for forecasting and scenario analysis.
- **Cell Range**: B16:Q46
- **Layout Structure**:
    - **Row Headers Location**: B17:C43
    - **Column Headers Location**: G21:Q21 (Years across columns)
    - **Data Range**:
      - Annual data: E17:Q17, H17:I17, H23:Q23, H24:Q26, H28:Q28, I29:Q29, H30:Q30, H32:Q32, H33:Q34, H36:Q38, H40:Q43, H45:Q46
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: M&R, Admin, Repo, Usage Days, Contr. Days, Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, Net Lease Days, Net Lease Rate, Net Lease Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Revenue.
- **Notes & Customizations**: Includes inflation assumptions for various cost and revenue components.

### Section Name: Per Usage Day Costs & Total Costs
- **Section Type**: Cost Analysis
- **Description & Purpose**: Breaks down costs on a per-usage-day basis and then calculates total costs. This provides insight into cost efficiency and profitability.
- **Cell Range**: B48:Q74
- **Layout Structure**:
    - **Row Headers Location**: B48:C73
    - **Column Headers Location**: G21:Q21 (Years across columns)
    - **Data Range**:
      - Annual data: H48:Q51, H57:Q63, H65:Q74
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Other Cost per Day, Lease Cost per Day, M&R Cost, Admin Expense, Repo Expense, Other Expense, Total Cost.
- **Notes & Customizations**: Includes lease costs on EVG-owned chassis and existing leases.

### Section Name: EBITDA and Margin Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Calculates EBITDA and related metrics, including EBITDA per usage day and EBITDA margin. This section assesses the overall profitability of the business.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76:C78
    - **Column Headers Location**: G21:Q21 (Years across columns)
    - **Data Range**:
      - Annual data: H77:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Focuses on EBITDA-related profitability metrics.

### Section Name: Chassis Acquisition & Initial Investment
- **Section Type**: Investment Analysis
- **Description & Purpose**: Details the costs associated with acquiring chassis, including the purchase price, reconditioning, and other related expenses. This section determines the initial investment required.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98, B100
    - **Column Headers Location**: None (Single Column)
    - **Data Range**: G83:G100
- **Time Series Details**:
    - **Date Range**: N/A (Upfront Costs)
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Less: Scrap Chassis, Transaction Expenses, Total Effective Purchase Price.
- **Notes & Customizations**: Includes adjustments for scrap chassis and transaction expenses.

### Section Name: Cash Flow Analysis - Depreciated Value Exit
- **Section Type**: Cash Flow Projection
- **Description & Purpose**: Projects the cash flows based on a depreciated value exit scenario, calculating the unlevered IRR and NPV. This section evaluates the financial viability of the investment.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Years across columns)
    - **Data Range**: H108:Q115
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G104:Q104)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes accelerated depreciation and working capital investment assumptions.

### Section Name: Cash Flow Analysis - TEV Exit
- **Section Type**: Cash Flow Projection
- **Description & Purpose**: Projects the cash flows based on a Total Enterprise Value (TEV) exit scenario, calculating the unlevered IRR and NPV. This section evaluates the financial viability of the investment under a different exit strategy.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Years across columns)
    - **Data Range**: H125:L132
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5 (G121:L121)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Uses a different exit multiple and a shorter time horizon (Year 0 to Year 5).
