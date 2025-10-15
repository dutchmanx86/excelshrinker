```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: SACP
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Chassis Purchase Analysis
    - Cash Flow Projections

## 2. Detailed Section Analysis

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of street and terminal assets, providing key performance indicators related to usage and contribution.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C5:C13
    - **Column Headers Location**: G6:Q6 (implicit annual time series)
    - **Data Range**: G7:Q12
- **Time Series Details**:
    - **Date Range**: 1922 to 1922 (based on `date_series_definitions`, but likely incorrect. The headers in G6:Q6 are numbers, not dates, so it's likely a 2015-2021 or similar range. Needs manual verification.)
    - **Frequency**: Annual (but inferred, given the repeating annual pattern)
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: The date series definition is incorrect. The data in G6:Q6 is likely representing years, not repeating values from 1922.

### Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section details the revenue and cost components associated with EVG's street and terminal operations, providing a breakdown of expenses and revenue streams.
- **Cell Range**: B17:Q74
- **Layout Structure**:
    - **Row Headers Location**: B17:B74, C19, C24, C29, C33, C37, C41, C42, C43, C57:C63
    - **Column Headers Location**: H16:Q16 (implicit annual time series)
    - **Data Range**: H17:Q74
- **Time Series Details**:
    - **Date Range**: 1922 to 1922 (based on `date_series_definitions`, but likely incorrect. The headers in H16:Q16 are numbers, not dates, so it's likely a 2015-2021 or similar range. Needs manual verification.)
    - **Frequency**: Annual (but inferred, given the repeating annual pattern)
- **Key Components**: EVG Street Revenue, Terminal Revenue, M&R Cost, Admin Expense, Repo Expense, Other Expense, Total Cost, Revenue, Per Usage Day.
- **Notes & Customizations**: Includes calculations for revenue, costs, and per-day metrics.

### EBITDA Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates EBITDA and related metrics based on the revenue and cost analysis.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76, C77, C78, B79
    - **Column Headers Location**: H16:Q16 (implicit annual time series)
    - **Data Range**: H76:Q79
- **Time Series Details**:
    - **Date Range**: 1922 to 1922 (based on `date_series_definitions`, but likely incorrect. The headers in H16:Q16 are numbers, not dates, so it's likely a 2015-2021 or similar range. Needs manual verification.)
    - **Frequency**: Annual (but inferred, given the repeating annual pattern)
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Calculates EBITDA and related metrics.

### Chassis Purchase Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the costs associated with purchasing chassis, including reconditioning, decoupling, and other related expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98, B100
    - **Column Headers Location**: G82
    - **Data Range**: G83:G98, G100
- **Time Series Details**:
    - **Date Range**: Not Applicable (one-time purchase analysis)
    - **Frequency**: Not Applicable
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Total Effective Purchase Price.
- **Notes & Customizations**: Details the costs associated with a one-time chassis purchase.

### Cash Flow Projections
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on the operating performance and investment assumptions, including an analysis of IRR and NPV.
- **Cell Range**: B104:Q136
- **Layout Structure**:
    - **Row Headers Location**: B104:B117, B119, B121, B123, B125:B134, B136
    - **Column Headers Location**: G104:Q104 (annual), G121:L121 (annual)
    - **Data Range**: G105:Q117, H108:Q115, F119, H125:L134
- **Time Series Details**:
    - **Date Range**: G104:Q104 (Annual): 2015 to 2021 (inferred, needs verification)
    - **Date Range**: G121:L121 (Annual): 2015 to 2020 (inferred, needs verification)
    - **Frequency**: Annual
- **Key Components**: EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Projects cash flows, calculates NPV and IRR, and includes exit assumptions. There are two separate annual time series in this section.
```