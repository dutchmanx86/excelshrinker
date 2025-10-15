## 1. Spreadsheet Overview
- **Sheet Name**: Use_Summary
- **Key Sections Identified**:
    - Transaction Overview
    - Chassis Fleet Summary
    - EVG Pooled Chassis
    - Usage Agreement
    - Terminal Utilization
    - Cost Summary (per Usage Day) - 2014
    - Financial Performance Summary

## 2. Detailed Section Analysis

### Section Name: Transaction Overview
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the key assumptions and costs associated with a potential chassis transaction, including purchase price, reconditioning costs, and other related expenses. It aims to provide a summary of the total transaction cost.
- **Cell Range**: B6:F17
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 6 (Transaction Overview)
    - **Data Range**:
      - Yr. 1 PF: `D7:D17`
      - Yr. 1 PF: `F7:F17`
- **Time Series Details**:
    - **Date Range**: Yr. 1 PF (Implied, but not explicitly a date)
    - **Frequency**: Single Period
- **Key Components**: Purchased Chassis, Purchase Price/Chassis, Payment for New Chassis ($000s), Reconditioning Costs, Decouping Costs, Repositioning Savings, Retitling Costs, Stenciling Costs, Working Capital Investment, Offhire Costs, Total Transaction Cost.
- **Notes & Customizations**: All monetary values are scaled by 1000.

### Section Name: Chassis Fleet Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the chassis fleet composition after the transaction, including the number of chassis acquired, retained, and scrapped. It provides an overview of the fleet's structure.
- **Cell Range**: B19:F23
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 19 (Chassis Fleet Summary)
    - **Data Range**:
      - Yr. 1 PF: `D21:D23`
      - Yr. 1 PF: `F21:F23`
- **Time Series Details**:
    - **Date Range**: Yr. 1 PF (Implied, but not explicitly a date)
    - **Frequency**: Single Period
- **Key Components**: Chassis Acquired, Retained, Scrapped, Total.
- **Notes & Customizations**: All values are scaled by 1000.

### Section Name: EVG Pooled Chassis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the allocation of chassis within the EVG (presumably a company) pool, including chassis decoupled at close and those used for EVG FFU (likely a specific project). It helps understand the internal distribution of chassis.
- **Cell Range**: B25:F29
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 25 (EVG Pooled Chassis)
    - **Data Range**:
      - Yr. 1 PF: `D26:D29`
      - Yr. 1 PF: `F26:F29`
- **Time Series Details**:
    - **Date Range**: Yr. 1 PF (Implied, but not explicitly a date)
    - **Frequency**: Single Period
- **Key Components**: Chassis Decouped at Close, Chassis to be Used for EVG FFU, Surplus (Shortage) of Chassis.
- **Notes & Customizations**: All values are scaled by 1000.

### Section Name: Usage Agreement
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the terms of a usage agreement, including chassis contributed per day and chassis used per day, broken down by MH and CH (likely different types of chassis or usage categories). It helps understand the daily chassis utilization.
- **Cell Range**: B33:F43
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 33 (Usage Agreement)
    - **Data Range**:
      - Yr. 1 PF: `D34:D43`
      - Yr. 1 PF: `F34:F43`
- **Time Series Details**:
    - **Date Range**: Yr. 1 PF (Implied, but not explicitly a date)
    - **Frequency**: Single Period
- **Key Components**: Chassis Contributed per Day, Chassis Used per Day (MH, CH), Total Utilization (Chassis per Day), Total Utilization (%), Street Utilization (% of Total), MH % of Street.
- **Notes & Customizations**: Values in D41, F41, D42, and D43 are percentages. Other values are scaled by 1000.

### Section Name: Terminal Utilization
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the utilization percentages for different categories: MH%, CH%, Terminal %, and Net Lease %. It provides insights into the distribution of chassis usage across various channels. Also includes rates for MH and CH.
- **Cell Range**: B39:F53
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 39 (Terminal)
    - **Data Range**:
      - Yr. 1 PF: `D39:D53`
      - Yr. 1 PF: `F39:F53`
- **Time Series Details**:
    - **Date Range**: Yr. 1 PF (Implied, but not explicitly a date)
    - **Frequency**: Single Period
- **Key Components**: Terminal, Total Utilization (Chassis per Day), Total Utilization (%), Street Utilization (% of Total), MH % of Street, MH%, CH%, Terminal %, Net Lease %, Rates (2014) for MH and CH.
- **Notes & Customizations**: Values in D46, D47 are percentages. Values in D51, D52, and D53 are scaled by 1000.

### Section Name: Cost Summary (per Usage Day) - 2014
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the costs associated with chassis usage on a per-day basis for the year 2014. It includes costs for M&R, repositioning, storage, and overhead. It provides a breakdown of the operational expenses.
- **Cell Range**: B55:F69
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 55 (Cost Summary (per Usage Day) - 2014)
    - **Data Range**:
      - Yr. 1 PF: `D57:D69`
      - Yr. 1 PF: `F57:F69`
- **Time Series Details**:
    - **Date Range**: Yr. 1 PF (Implied, but not explicitly a date)
    - **Frequency**: Single Period
- **Key Components**: Usage Days, $ M&R, $ Repositioning, $ Storage, $ Overhead, M&R, Admin, Repo, Storage, Lease Expense ($2.65/every day), Revenue Sharing ($1.00/street day), Other.
- **Notes & Customizations**: Values in D57:D60, D63:D66, and D69 are scaled by 1000.

### Section Name: Financial Performance Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents a summary of the financial performance, including contributed days, revenue, expense, EBITDA, and various financial metrics like EBITDA margin and IRR. It provides a high-level overview of the investment's profitability.
- **Cell Range**: B71:F88
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 71 (Summary)
    - **Data Range**:
      - Yr. 1 PF: `D73:D86`
      - Yr. 1 PF: `F73:F81`
- **Time Series Details**:
    - **Date Range**: Yr. 1 PF (Implied, but not explicitly a date)
    - **Frequency**: Single Period
- **Key Components**: Contributed Days, Revenue (2014E), Expense (2014E), EBITDA (2014E), EBITDA Margin (2014E), EBITDA per Usage Day (2014E), EBITDA per Contributed Day (2014E), Depreciated Value 10-year Unlevered IRR, TEV 10x Exit Multiple Unlevered IRR, NPV - 10-year, Total Investment (incl. WC), Purchase Multiple1.
- **Notes & Customizations**: Values in D73:D76, D79, D80, D83, and D85 are scaled by 1000. Values in D77, D81, D82, and D86 are percentages. F81 contains the string "nm". Row B88 contains a footnote.
