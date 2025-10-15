```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Oakland
- **Key Sections Identified**:
    - Utilization Summary
    - Annual Inflation Assumptions
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Chassis Acquisition Analysis
    - Cash Flow Projections

## 2. Detailed Section Analysis

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of street and terminal chassis, providing key metrics like utilization rates and percentages. It's used to understand how effectively the chassis are being used.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 6
    - **Data Range**: G7:Q12
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but assumed to be annual from 2015 to 2021 based on the "Revenue and Cost Analysis" section.
    - **Frequency**: Annual
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on different totals.

### Annual Inflation Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the annual inflation assumptions used in the model for various cost and revenue components.
- **Cell Range**: U32:V41
- **Layout Structure**:
    - **Row Headers Location**: Column U
    - **Column Headers Location**: None
    - **Data Range**: V33:V41
- **Time Series Details**:
    - **Date Range**: Not Applicable
    - **Frequency**: Not Applicable
- **Key Components**: Trucker Rate Inflation, EVG Rate Inflation, Terminal Rate Inflation, M&R Cost Inflation, Admin Cost Inflation, Repo Cost Inflation, Other Cost Inflation.
- **Notes & Customizations**: This section is a simple table of inflation rates.

### Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section details the revenue and cost components, calculating revenue, costs, and per-day metrics. It's used to analyze the profitability of the chassis operations.
- **Cell Range**: B17:Q74
- **Layout Structure**:
    - **Row Headers Location**: Column B and C
    - **Column Headers Location**: Row 16
    - **Data Range**:
      - Annual data: H17:Q74
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: EVG, M&R, Admin, Repo, Usage Days, Contr. Days, Revenue, EVG Street Costs, Terminal Billings, M&R Cost, Admin Expense, Repo Expense, Total Cost.
- **Notes & Customizations**: Includes per-day cost calculations and breakdowns of revenue and cost components.

### EBITDA Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates EBITDA and related metrics, providing a measure of the operational profitability of the business.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: Column B and C
    - **Column Headers Location**: Row 6
    - **Data Range**: H76:Q79
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Calculates EBITDA margin as a percentage.

### Chassis Acquisition Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the costs associated with acquiring chassis, including purchase price, reconditioning, and other related expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 82
    - **Data Range**: G83:G98
- **Time Series Details**:
    - **Date Range**: Not Applicable
    - **Frequency**: Not Applicable
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Price per Chassis, Payment to EVG, Total Chassis Price, Reconditioning Costs, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: This section focuses on upfront costs and a multiple calculation.

### Cash Flow Projections
- **Section Type**: Custom Cash Flow
- **Description & Purpose**: This section projects cash flows based on depreciated value exit and TEV exit, calculating NPV and IRR. It's used to assess the overall financial viability of the investment.
- **Cell Range**: B104:Q136
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 6
    - **Data Range**:
      - Annual data (Depreciated Value Exit): H108:Q115
      - Annual data (TEV Exit): H125:L132
- **Time Series Details**:
    - **Date Range**: 2015 to 2021 (Depreciated Value Exit), 2015 to 2020 (TEV Exit)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes calculations for NPV and IRR based on projected cash flows. Two exit scenarios are considered: Depreciated Value and TEV.
```