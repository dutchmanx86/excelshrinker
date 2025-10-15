# Master Workbook Analysis

This document provides a comprehensive analysis of all sheets in the Excel workbook.

---

## Table of Contents

1. [Assumptions](#assumptions)
   - [Section Name: Utilization Assumptions](#assumptions-section-name-utilization-assumptions)
   - [Section Name: Purchase/Lease Assumptions](#assumptions-section-name-purchaselease-assumptions)
   - [Section Name: Upfront Investment](#assumptions-section-name-upfront-investment)
   - [Section Name: Operating Assumptions](#assumptions-section-name-operating-assumptions)
2. [Use_Summary](#use_summary)
   - [Section Name: Transaction Overview](#use_summary-section-name-transaction-overview)
   - [Section Name: Chassis Fleet Summary](#use_summary-section-name-chassis-fleet-summary)
   - [Section Name: EVG Pooled Chassis](#use_summary-section-name-evg-pooled-chassis)
   - [Section Name: Usage Agreement](#use_summary-section-name-usage-agreement)
   - [Section Name: Terminal Utilization](#use_summary-section-name-terminal-utilization)
   - [Section Name: Cost Summary (per Usage Day) - 2014](#use_summary-section-name-cost-summary-per-usage-day---2014)
   - [Section Name: Financial Performance Summary](#use_summary-section-name-financial-performance-summary)
3. [Region Assumptions](#region-assumptions)
   - [Header](#region-assumptions-header)
   - [Region Assumptions Table](#region-assumptions-region-assumptions-table)
   - [Region Assumptions Table (Repeated)](#region-assumptions-region-assumptions-table-repeated)
   - [Notes](#region-assumptions-notes)
4. [Deal Summary](#deal-summary)
   - [Fleet Summary](#deal-summary-fleet-summary)
   - [Usage and Fleet Sizing](#deal-summary-usage-and-fleet-sizing)
   - [Investment Overview](#deal-summary-investment-overview)
   - [Sensitivity Analysis](#deal-summary-sensitivity-analysis)
5. [TOTAL FFU](#total-ffu)
   - [Utilization Summary](#total-ffu-utilization-summary)
   - [Revenue and Cost Analysis](#total-ffu-revenue-and-cost-analysis)
   - [EBITDA Calculation](#total-ffu-ebitda-calculation)
   - [Chassis Acquisition Analysis](#total-ffu-chassis-acquisition-analysis)
   - [Cash Flow Projections](#total-ffu-cash-flow-projections)
6. [COCP](#cocp)
   - [Utilization Summary](#cocp-utilization-summary)
   - [Revenue and Cost Analysis](#cocp-revenue-and-cost-analysis)
   - [EBITDA Calculation](#cocp-ebitda-calculation)
   - [Upfront Investment Analysis](#cocp-upfront-investment-analysis)
   - [Cash Flow Projections - Depreciated Value Exit](#cocp-cash-flow-projections---depreciated-value-exit)
   - [Cash Flow Projections - TEV Exit](#cocp-cash-flow-projections---tev-exit)
   - [Annual Inflation Assumptions](#cocp-annual-inflation-assumptions)
7. [DCCP](#dccp)
   - [Utilization Summary](#dccp-utilization-summary)
   - [Revenue and Cost Analysis](#dccp-revenue-and-cost-analysis)
   - [EBITDA Calculation](#dccp-ebitda-calculation)
   - [Chassis Acquisition Analysis](#dccp-chassis-acquisition-analysis)
   - [Cash Flow Projections](#dccp-cash-flow-projections)
8. [GCCP](#gccp)
   - [Section Name: Utilization Summary](#gccp-section-name-utilization-summary)
   - [Section Name: Revenue and Cost Analysis](#gccp-section-name-revenue-and-cost-analysis)
   - [Section Name: EBITDA Calculation](#gccp-section-name-ebitda-calculation)
   - [Section Name: Chassis Acquisition Analysis](#gccp-section-name-chassis-acquisition-analysis)
   - [Section Name: Cash Flow Projections](#gccp-section-name-cash-flow-projections)
9. [MCCP](#mccp)
   - [Header/Title Section](#mccp-headertitle-section)
   - [Utilization Summary](#mccp-utilization-summary)
   - [Revenue and Cost Analysis](#mccp-revenue-and-cost-analysis)
   - [EBITDA Calculation](#mccp-ebitda-calculation)
   - [Chassis Acquisition Analysis](#mccp-chassis-acquisition-analysis)
   - [Cash Flow Projections - Depreciated Value Exit](#mccp-cash-flow-projections---depreciated-value-exit)
   - [Cash Flow Projections - TEV Exit](#mccp-cash-flow-projections---tev-exit)
10. [MWCP](#mwcp)
   - [Utilization Summary](#mwcp-utilization-summary)
   - [Revenue and Cost Analysis](#mwcp-revenue-and-cost-analysis)
   - [EBITDA Calculation](#mwcp-ebitda-calculation)
   - [Chassis Acquisition Analysis](#mwcp-chassis-acquisition-analysis)
   - [Cash Flow Projections (Depreciated Value Exit)](#mwcp-cash-flow-projections-depreciated-value-exit)
   - [Cash Flow Projections (TEV Exit)](#mwcp-cash-flow-projections-tev-exit)
   - [Annual Inflation Assumptions](#mwcp-annual-inflation-assumptions)
11. [SACP](#sacp)
   - [Utilization Summary](#sacp-utilization-summary)
   - [Revenue and Cost Analysis](#sacp-revenue-and-cost-analysis)
   - [EBITDA Calculation](#sacp-ebitda-calculation)
   - [Chassis Purchase Analysis](#sacp-chassis-purchase-analysis)
   - [Cash Flow Projections](#sacp-cash-flow-projections)
12. [PSW](#psw)
   - [Section Name: Utilization Summary](#psw-section-name-utilization-summary)
   - [Section Name: Revenue and Cost Analysis](#psw-section-name-revenue-and-cost-analysis)
   - [Section Name: EBITDA Calculation](#psw-section-name-ebitda-calculation)
   - [Section Name: Chassis Acquisition Analysis](#psw-section-name-chassis-acquisition-analysis)
   - [Section Name: Cash Flow Projections (Depreciated Value Exit)](#psw-section-name-cash-flow-projections-depreciated-value-exit)
   - [Section Name: Cash Flow Projections (TEV Exit)](#psw-section-name-cash-flow-projections-tev-exit)
   - [Section Name: Inflation Assumptions](#psw-section-name-inflation-assumptions)
13. [Customer Output - LA](#customer-output---la)
   - [Header](#customer-output---la-header)
   - [Assumptions](#customer-output---la-assumptions)
   - [Scenario Table](#customer-output---la-scenario-table)
14. [Customer Output - APMT](#customer-output---apmt)
   - [Section Name (Header)](#customer-output---apmt-section-name-header)
   - [Section Name (Assumptions)](#customer-output---apmt-section-name-assumptions)
   - [Section Name (Purchase Price Table)](#customer-output---apmt-section-name-purchase-price-table)
15. [PNW](#pnw)
   - [Utilization Summary](#pnw-utilization-summary)
   - [Revenue and Cost Analysis](#pnw-revenue-and-cost-analysis)
   - [EBITDA Calculation](#pnw-ebitda-calculation)
   - [Upfront Investment Analysis](#pnw-upfront-investment-analysis)
   - [Cash Flow Projections (Depreciated Value Exit)](#pnw-cash-flow-projections-depreciated-value-exit)
   - [Cash Flow Projections (TEV Exit)](#pnw-cash-flow-projections-tev-exit)
   - [Annual Inflation Assumptions](#pnw-annual-inflation-assumptions)
16. [Oakland](#oakland)
   - [Utilization Summary](#oakland-utilization-summary)
   - [Annual Inflation Assumptions](#oakland-annual-inflation-assumptions)
   - [Revenue and Cost Analysis](#oakland-revenue-and-cost-analysis)
   - [EBITDA Calculation](#oakland-ebitda-calculation)
   - [Chassis Acquisition Analysis](#oakland-chassis-acquisition-analysis)
   - [Cash Flow Projections](#oakland-cash-flow-projections)
17. [NE](#ne)
   - [Utilization Summary](#ne-utilization-summary)
   - [Revenue and Cost Analysis](#ne-revenue-and-cost-analysis)
   - [EBITDA Calculation](#ne-ebitda-calculation)
   - [Chassis Acquisition Analysis](#ne-chassis-acquisition-analysis)
   - [Cash Flow Projections](#ne-cash-flow-projections)
18. [HRCP](#hrcp)
   - [Utilization Summary](#hrcp-utilization-summary)
   - [Revenue & Cost Analysis](#hrcp-revenue-&-cost-analysis)
   - [Chassis Acquisition Analysis](#hrcp-chassis-acquisition-analysis)
   - [Cash Flow Projections](#hrcp-cash-flow-projections)
19. [Support Data -->](#support-data-)
   - [Section Name (e.g., "Header")](#support-data--section-name-eg-"header")
20. [PoP Usage Data](#pop-usage-data)
   - [Title/Header](#pop-usage-data-titleheader)
   - [Chassis Usage Data by Company](#pop-usage-data-chassis-usage-data-by-company)
   - [DCSZ and Unassigned Chassis Data](#pop-usage-data-dcsz-and-unassigned-chassis-data)
   - [Totals & Utilization Metrics](#pop-usage-data-totals-&-utilization-metrics)
   - [Footnotes](#pop-usage-data-footnotes)
21. [Fleet Summary - Pending](#fleet-summary---pending)
   - [Section Name: Header Information](#fleet-summary---pending-section-name-header-information)
   - [Section Name: Assumptions](#fleet-summary---pending-section-name-assumptions)
   - [Section Name: ASI/CSG Premium](#fleet-summary---pending-section-name-asicsg-premium)
   - [Section Name: Chassis Age Analysis](#fleet-summary---pending-section-name-chassis-age-analysis)
   - [Section Name: Chassis Age Analysis - Detail](#fleet-summary---pending-section-name-chassis-age-analysis---detail)
22. [Fleet Sizing](#fleet-sizing)
   - [Section Name: Fleet Sizing Calculation Table](#fleet-sizing-section-name-fleet-sizing-calculation-table)
   - [Section Name: Data Source & Assumptions](#fleet-sizing-section-name-data-source-&-assumptions)

---


====================================================================================================
# SHEET 1: Assumptions
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Assumptions
- **Key Sections Identified**:
    - Utilization Assumptions
    - Purchase/Lease Assumptions
    - Upfront Investment
    - Operating Assumptions

## 2. Detailed Section Analysis

### Section Name: Utilization Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines the assumptions related to the utilization of EVG chassis, including purchase, lease, and scrap quantities, as well as utilization rates. This section is used to calculate the total chassis required for EVG use.
- **Cell Range**: B5:F14
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**:
      - C6:C14 (numeric values)
      - E6:E14 (numeric values)
- **Time Series Details**:
    - No time series data detected.
- **Key Components**: Total EVG Chassis Purchased, Total EVG Chassis Leased, Total EVG Chassis for Scrap, Total EVG Leases, Total Excess Chassis Leased, Total DCLI Backfill, EVG Average Daily Usage, EVG Utilization Rate, Total Chassis Required for EVG Use.
- **Notes & Customizations**: Includes assumptions for different leasing scenarios (DCLI leases all excess vs. backfilling some excess).

### Section Name: Purchase/Lease Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines the assumptions related to the purchase and lease costs of chassis, including book value, premiums/discounts, and lease rates.
- **Cell Range**: B16:C24
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C17:C24 (numeric values)
- **Time Series Details**:
    - No time series data detected.
- **Key Components**: Average Book Value per Chassis, Premium / (Discount) to Book (Upfront), Premium / (Discount) to Book (PO), Purchase Price, Lease Cost per Day for EVG Chassis, Lease Cost per Day for EVG Leases, Lease Cost per Day for Add. Capacity.
- **Notes & Customizations**: None.

### Section Name: Upfront Investment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines the assumptions related to upfront investment costs, including repositioning, decoupling, reconditioning, retitling, stenciling, and offhire costs.
- **Cell Range**: B26:C43
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C27:C43 (numeric values)
- **Time Series Details**:
    - No time series data detected.
- **Key Components**: Repositioning, # of Chassis w/ Repositioning, Decouping Costs, Chassis to be Decouped, Reconditioning Costs, # of Chassis Requiring Reconditioning, Retitling Costs, Chassis to be Retitled, Stenciling Costs, Chassis to be Stenciled, Offhire Costs, Chassis to be Offhired.
- **Notes & Customizations**: Includes an "on/off" switch (E34) related to reconditioning costs.

### Section Name: Operating Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines the assumptions related to operating costs and revenue, including terminal percentages, billing thresholds, cost assumptions for M&R, Admin, Repo, and Other. Also includes PSW MH Rate, EVG CH Rate, Terminal Rate, MH Annual Conversion %, Gain Sharing % on Conversion, and Bad Debt.
- **Cell Range**: B47:I60
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E50:H50
    - **Data Range**:
      - C48:C60 (numeric values)
      - E51:H51 (numeric values)
- **Time Series Details**:
    - No time series data detected.
- **Key Components**: Terminal % Assumption Placeholder, Terminal Billing Threshold, M&R, Admin, Repo, Other, PSW MH Rate, EVG CH Rate, Terminal Rate, MH Annual Conversion %, Gain Sharing % on Conversion, Bad Debt (as % of Revenue).
- **Notes & Customizations**: Cost assumptions are provided by operations (I51).



====================================================================================================
# SHEET 2: Use_Summary
====================================================================================================

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



====================================================================================================
# SHEET 3: Region Assumptions
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Region Assumptions
- **Key Sections Identified**:
    - Header
    - Region Assumptions Table
    - Region Assumptions Table (Repeated)
    - Notes

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title and subtitle of the spreadsheet, providing context for the data.
- **Cell Range**: A1:A2
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: A1:A2
- **Time Series Details**: None
- **Key Components**: "Direct ChassisLink Inc.", "Evergreen Model Assumptions"
- **Notes & Customizations**: Basic header information.

### Region Assumptions Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains key assumptions and data points for different regions related to chassis management. It includes information on chassis ownership, leasing, scrap, costs, and utilization rates.
- **Cell Range**: B8:AF20
- **Layout Structure**:
    - **Row Headers Location**: A10:A20
    - **Column Headers Location**: B8:AF8
    - **Data Range**:
      - Numeric values: C10:K20, L10:L20, M10:M20, N10:N20, O10:O20, P10:R20, S10:W20, X10:Y20, Z10:AD20, AE10:AF20, C17:D19, E17:K19, E17:K19
- **Time Series Details**: None
- **Key Components**: Region, Total EVG Owned Chassis, Total EVG Leased Chassis, Total EVG Chassis for Scrap, Chassis Purchased by DCLI, EVG Owned Chassis Leased by DCLI, EVG Leases Taken on by DCLI, Additional Capacity Leased, Total DCLI Backfill, EVG Average Daily Usage, EVG Utilization Rate, Average Book Value per Chassis, Premium / (Discount) to Book, Purchase Price, Cost to Lease Owned EVG Chassis, Cost to Takeover EVG Existing Leases, Lease Cost per Day for Add. Capacity, Repo Cost per Chassis, Recon. Cost per Chassis, Decouping Cost per Chassis, Retitling & Stenciling Cost per Chassis, Offhire Cost per Chassis, Sales Tax, Terminal % of Daily Usage, M&R per Billed Day, Repo per Billed Day, Admin per Chassis per Day, Terminal Rate, Market MH Rate, MH Conversion per Year, Gain Sharing % on MH Transition.
- **Notes & Customizations**: Data is scaled by 1000 in some columns.

### Region Assumptions Table (Repeated)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section appears to be a summary or duplicate of some of the data from the first Region Assumptions Table, focusing on Total EVG Owned Chassis.
- **Cell Range**: B30:K40
- **Layout Structure**:
    - **Row Headers Location**: B10:B20
    - **Column Headers Location**: C8:K8
    - **Data Range**: C30:K35
- **Time Series Details**: None
- **Key Components**: COCP*, DCCP*, GCCP*, MCCP*, MWCP*, SACP*, LSA/LGB***, PNW**, Oakland**, Northeast** (NL), HRCP** (NL)
- **Notes & Customizations**: Data is scaled by 1000. The row labels are abbreviated.

### Notes
- **Section Type**: Notes
- **Description & Purpose**: Provides context and disclaimers for the data presented in the spreadsheet.
- **Cell Range**: B25:B28
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: B25:B28
- **Time Series Details**: None
- **Key Components**: Source, CCM, Estimated, Evergreen
- **Notes & Customizations**: Contains information about the data sources and estimations.


====================================================================================================
# SHEET 4: Deal Summary
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Deal Summary
- **Key Sections Identified**:
    - Fleet Summary
    - Usage and Fleet Sizing
    - Investment Overview
    - Sensitivity Analysis

## 2. Detailed Section Analysis

### Fleet Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the current and future fleet composition, including owned, leased, and scrapped chassis. It helps understand the current state and planned changes to the fleet.
- **Cell Range**: C5:G11
- **Layout Structure**:
    - **Row Headers Location**: C6:C11
    - **Column Headers Location**: C6:G6
    - **Data Range**:
      - Current EVG Fleet: D7:D11
      - Future: G7:G11
- **Time Series Details**:
    - **Date Range**: Current, Future
    - **Frequency**: N/A (Static data)
- **Key Components**: Current EVG Fleet, Purchased from EVG, Leased from EVG, Scrapped, EVG Leases Assumed, Backfilled by DCLI
- **Notes & Customizations**: Includes both the current fleet and a "Future" projection.

### Usage and Fleet Sizing
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the usage and fleet sizing metrics, including current and required fleet sizes, utilization rates, and related percentages.
- **Cell Range**: K5:L17
- **Layout Structure**:
    - **Row Headers Location**: K6:K17
    - **Column Headers Location**: K6:L6
    - **Data Range**: L7:L17
- **Time Series Details**:
    - **Date Range**: Current
    - **Frequency**: N/A (Static data)
- **Key Components**: Street, MH, CH, Terminal, Total Usage, Est. Utilization, Owned, Leased, Short/(Surpl)
- **Notes & Customizations**: Calculates fleet requirements based on utilization.

### Investment Overview
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides an overview of the investment required, including asset purchases, repositioning costs, working capital, and reconditioning expenses. Also includes financial returns metrics.
- **Cell Range**: N5:Q32
- **Layout Structure**:
    - **Row Headers Location**: N6:N32
    - **Column Headers Location**: N6:Q6
    - **Data Range**: P7:P32
- **Time Series Details**:
    - **Date Range**: Year 1
    - **Frequency**: Annual
- **Key Components**: Assets, Repositioning, Working Capital, Reconditioning, Decooping Costs, Sales tax, Re-title & stencil costs, Offhire costs, Value of Scrap Chassis, Total Investment, Financial Returns, CH Revenue, MH Revenue, Terminal revenue, Total Revenue, M&R Expense, EVG Lease Expense, Admin Expense, Adj. EBITDA, Margin %, Purchase Multiple, Depr. Value 10-year IRR, TEV 5x Exit Multiple IRR, NPV
- **Notes & Customizations**: Includes upfront costs and commentary/assumptions.

### Sensitivity Analysis
- **Section Type**: Sensitivity Table
- **Description & Purpose**: Analyzes the sensitivity of key outputs (e.g., Investment, EBITDA, IRR, NPV) to changes in model inputs (e.g., Lease Cost, Average Premium/Discount, Terminal Rate, MH Conversion).
- **Cell Range**: C34:R41
- **Layout Structure**:
    - **Row Headers Location**: C36:C41
    - **Column Headers Location**: C36:R36
    - **Data Range**: I37:R41
- **Time Series Details**:
    - **Date Range**: N/A (Scenario Analysis)
    - **Frequency**: N/A
- **Key Components**: Scenario, Lease Cost per Day to EVG, Average Prem/(Disc) per Chassis, Terminal Rate, MH Conversion, Total Investment, Investment Multiple, Purchase Price per Chassis, Average EBITDA, Average EBITDA Margin %, Average EBITDA per usage day, Average EBITDA per chassis per day, 10 year depreciated value IRR %, 5x EBITDA exit multiple IRR %, NPV $
- **Notes & Customizations**: Presents a matrix of different scenarios and their impact on key financial metrics.


====================================================================================================
# SHEET 5: TOTAL FFU
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: TOTAL FFU
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Chassis Acquisition Analysis
    - Cash Flow Projections

## 2. Detailed Section Analysis

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of assets (chassis) across different categories (Street - MH, Street - EVG, Terminal) and calculates utilization rates. It provides a high-level overview of asset performance.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C5:C13
    - **Column Headers Location**: G6:Q6
    - **Data Range**: G7:Q12
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the provided data, but implied to be annual from the column headers in the range G6:Q6.
    - **Frequency**: Annual
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: The data is presented in thousands ($000s).

### Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section details the revenue and cost components related to chassis usage, including costs per day, total costs, and revenue streams from different sources (Trucker, EVG Street, Terminal). It's used to understand the profitability drivers.
- **Cell Range**: B17:Q74
- **Layout Structure**:
    - **Row Headers Location**: B17:B74 and C19, C24, C29, C33, C37, C41, C42, C43, C57:C63
    - **Column Headers Location**: H16:Q16
    - **Data Range**: H17:Q74
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but implied to be annual from the column headers in the range H16:Q16.
    - **Frequency**: Annual
- **Key Components**: EVG Street Revenue, Terminal Revenue, Total Usage Days, M&R Cost, Admin Expense, Repo Expense, Other Expense, Total Cost, Revenue.
- **Notes & Customizations**: The data is presented in thousands ($000s). Includes calculations for cost per day. Includes inflation assumptions in columns U and V.

### EBITDA Calculation
- **Section Type**: Standard P&L (Partial)
- **Description & Purpose**: This section calculates EBITDA and related metrics (EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin). It provides a measure of operating profitability.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76, C77, C78, B79
    - **Column Headers Location**: H16:Q16
    - **Data Range**: H76:Q79
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but implied to be annual from the column headers in the range H16:Q16.
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: The data is presented in thousands ($000s) except for EBITDA Margin.

### Chassis Acquisition Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the costs associated with acquiring chassis, including the purchase price, reconditioning costs, and other related expenses. It's used to determine the total effective purchase price and related metrics.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: None (single period analysis)
    - **Data Range**: G83:G100
- **Time Series Details**:
    - **Date Range**: Single period (Upfront)
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: The data is presented in thousands ($000s) except for Premium / (Discount) to Book and Cash Multiple of 2014 EBITDA - Owned.

### Cash Flow Projections
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects the cash flows associated with the investment, including upfront investment, exit value, and annual cash flows. It's used to calculate the Unlevered IRR and NPV. Two scenarios are presented: "Cash Flows - Depreciated Value Exit" and "Cash Flows - TEV Exit".
- **Cell Range**: B104:Q136
- **Layout Structure**:
    - **Row Headers Location**: B104:B119 and B121:B136
    - **Column Headers Location**: G6:Q6 (for Depreciated Value Exit) and G6:L6 (for TEV Exit)
    - **Data Range**:
      - Annual data (Depreciated Value Exit): `H108:Q115`
      - Annual data (TEV Exit): `H125:L132`
- **Time Series Details**:
    - **Date Range**:
      - Depreciated Value Exit: Not explicitly defined, but implied to be annual from the column headers in the range H6:Q6.
      - TEV Exit: Not explicitly defined, but implied to be annual from the column headers in the range H6:L6.
    - **Frequency**: Annual
- **Key Components**: Investment, EBITDA, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: The data is presented in thousands ($000s) except for Cash Taxes @ and WC Investment @. There are two exit scenarios: Depreciated Value Exit and TEV Exit.


====================================================================================================
# SHEET 6: COCP
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: COCP
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Upfront Investment Analysis
    - Cash Flow Projections - Depreciated Value Exit
    - Cash Flow Projections - TEV Exit
    - Annual Inflation Assumptions

## 2. Detailed Section Analysis

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of assets (likely chassis) across different categories (Street-MH, Street-EVG, Terminal). It provides key metrics like utilization rates and percentages.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 6 (G6:Q6)
    - **Data Range**: G7:Q12
- **Time Series Details**:
    - **Date Range**: The data spans multiple years, but the exact years are not explicitly labeled. Based on the other sections, we can infer the range is likely 2015 to 2027.
    - **Frequency**: Annual
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate
- **Notes & Customizations**: The percentages provide a breakdown of utilization across different segments.

### Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section analyzes revenue and costs associated with the business, breaking them down by different categories like "Street" and "Terminal". It calculates costs on a per-usage-day basis.
- **Cell Range**: B17:Q74
- **Layout Structure**:
    - **Row Headers Location**: Column B and Column C
    - **Column Headers Location**: Row 16 (E16:I16) and Row 21 (G21:Q21)
    - **Data Range**:
      - Annual data: E17:G19 (costs)
      - Annual data: H23:Q74 (revenue, costs, days)
- **Time Series Details**:
    - **Date Range**: The data spans multiple years, but the exact years are not explicitly labeled. Based on the other sections, we can infer the range is likely 2015 to 2027.
    - **Frequency**: Annual
- **Key Components**: EVG Street Revenue, Terminal Revenue, Total Usage Days, Revenue, M&R Cost, Admin Expense, Repo Expense, Total Cost
- **Notes & Customizations**: This section includes calculations for both "Per Usage Day" and total costs. It also incorporates lease costs and gain sharing.

### EBITDA Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates EBITDA and related metrics, such as EBITDA per usage day and EBITDA margin.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: Column B and Column C
    - **Column Headers Location**: Row 21 (G21:Q21)
    - **Data Range**: H76:Q79
- **Time Series Details**:
    - **Date Range**: The data spans multiple years, but the exact years are not explicitly labeled. Based on the other sections, we can infer the range is likely 2015 to 2027.
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%)
- **Notes & Customizations**: This section provides key profitability metrics.

### Upfront Investment Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the upfront investment required for the project, including chassis acquisition costs, reconditioning costs, and working capital investment.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 82
    - **Data Range**: G83:G98
- **Time Series Details**:
    - **Date Range**: This section represents a single point in time, not a time series.
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned
- **Notes & Customizations**: This section focuses on the initial investment required.

### Cash Flow Projections - Depreciated Value Exit
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit scenario. It includes key line items like EBITDA, accelerated depreciation, cash taxes, and capex.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 21 (G21:Q21)
    - **Data Range**: G104:Q117
- **Time Series Details**:
    - **Date Range**: The data spans multiple years, but the exact years are not explicitly labeled. Based on the other sections, we can infer the range is likely 2015 to 2027.
    - **Frequency**: Annual
- **Key Components**: EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @ , Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR
- **Notes & Customizations**: This section calculates the Unlevered IRR based on the projected cash flows.

### Cash Flow Projections - TEV Exit
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit scenario. It includes key line items like EBITDA, accelerated depreciation, cash taxes, and capex.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 21 (G21:Q21)
    - **Data Range**: H125:L134
- **Time Series Details**:
    - **Date Range**: The data spans multiple years, but the exact years are not explicitly labeled. Based on the other sections, we can infer the range is likely 2015 to 2020.
    - **Frequency**: Annual
- **Key Components**: EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @ , Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR
- **Notes & Customizations**: This section calculates the Unlevered IRR based on the projected cash flows.

### Annual Inflation Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section lists the annual inflation assumptions used in the model.
- **Cell Range**: U32:V41
- **Layout Structure**:
    - **Row Headers Location**: Column U
    - **Column Headers Location**: None
    - **Data Range**: V33:V41
- **Time Series Details**:
    - **Date Range**: This section represents a single point in time, not a time series.
    - **Frequency**: N/A
- **Key Components**: Trucker Rate Inflation, EVG Rate Inflation, Terminal Rate Inflation, M&R Cost Inflation, Admin Cost Inflation, Repo Cost Inflation, Other Cost Inflation
- **Notes & Customizations**: This section is used as inputs for the model.


====================================================================================================
# SHEET 7: DCCP
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: DCCP
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Chassis Acquisition Analysis
    - Cash Flow Projections

## 2. Detailed Section Analysis

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of assets (chassis) across different segments (Street - MH, Street - EVG, Terminal) and calculates utilization rates. It provides a high-level overview of asset performance.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C5:C13
    - **Column Headers Location**: G6:Q6
    - **Data Range**: G7:Q12
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but columns G to Q represent different time periods. The specific years are not provided in the JSON, but are likely annual.
    - **Frequency**: Annual (assumed)
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: The section calculates percentages and rates based on the utilization data.

### Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section details the revenue and cost components related to the DCCP business. It breaks down revenue by source (Trucker, EVG Street, Terminal) and costs by type (M&R, Admin, Repo, Lease). The purpose is to analyze the profitability drivers of the business.
- **Cell Range**: B17:Q74
- **Layout Structure**:
    - **Row Headers Location**: B17:B74 and C19, C29, C33, C37, C41, C42, C43, C57:C63
    - **Column Headers Location**: H16:Q16
    - **Data Range**:
      - Annual data: H17:Q19, H23:Q30, H32:Q43, H45:Q74
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but columns H to Q represent different time periods. The specific years are not provided in the JSON, but are likely annual.
    - **Frequency**: Annual (assumed)
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, M&R Cost, Admin Expense, Repo Expense, Lease Cost.
- **Notes & Customizations**: The section includes calculations for "Per Usage Day" costs and various utilization metrics. It also incorporates inflation assumptions from columns U and V.

### EBITDA Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates EBITDA and related metrics based on the revenue and cost data from the previous section. It also includes EBITDA per usage day and EBITDA margin.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76, C77, C78, B79
    - **Column Headers Location**: H16:Q16
    - **Data Range**: H76:Q79
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but columns H to Q represent different time periods. The specific years are not provided in the JSON, but are likely annual.
    - **Frequency**: Annual (assumed)
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: The section calculates EBITDA and related profitability metrics.

### Chassis Acquisition Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the costs associated with acquiring chassis, including the purchase price, reconditioning costs, and other related expenses. It also calculates a cash multiple of EBITDA.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98, B100
    - **Column Headers Location**: G82
    - **Data Range**: G83:G98, G100
- **Time Series Details**:
    - **Date Range**: This section primarily focuses on upfront costs, with no explicit time series.
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Price per Chassis, Payment to EVG, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: This section focuses on a one-time acquisition cost analysis.

### Cash Flow Projections
- **Section Type**: Custom Cash Flow
- **Description & Purpose**: This section projects the cash flows associated with the DCCP business, including investments, EBITDA, taxes, working capital, and capex. It calculates the total cash flows, NPV, and unlevered IRR. There are two distinct cash flow scenarios: "Depreciated Value Exit" and "TEV Exit".
- **Cell Range**: B104:Q136
- **Layout Structure**:
    - **Row Headers Location**: B104:B115, F118, B119, B121:B134, B136
    - **Column Headers Location**: G104:Q104
    - **Data Range**:
      - Annual data (Depreciated Value Exit): G104:Q115, F119
      - Annual data (TEV Exit): G122:L134
- **Time Series Details**:
    - **Date Range**:
        - Depreciated Value Exit: Not explicitly defined, but columns G to Q represent different time periods. The specific years are not provided in the JSON, but are likely annual.
        - TEV Exit: Not explicitly defined, but columns G to L represent different time periods. The specific years are not provided in the JSON, but are likely annual.
    - **Frequency**: Annual (assumed)
- **Key Components**: Investment, EBITDA, Accelerated Depreciation, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: This section includes two different exit scenarios ("Depreciated Value Exit" and "TEV Exit") and calculates key financial metrics such as NPV and IRR.


====================================================================================================
# SHEET 8: GCCP
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: GCCP
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Chassis Acquisition Analysis
    - Cash Flow Projections

## 2. Detailed Section Analysis

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of assets (chassis) across different categories (Street - MH, Street - EVG, Terminal) and calculates utilization rates. It provides insights into how effectively the assets are being used.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C5:C13
    - **Column Headers Location**: G6:Q6
    - **Data Range**:
      - Annual data: G7:Q12
- **Time Series Details**:
    - **Date Range**: The data in G6:Q6 is not explicitly labeled with dates, but the context suggests an annual time series. Assuming the first column (G) represents 2015 and each subsequent column is a year, the range is 2015 to 2021.
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: The section calculates percentages and utilization rates based on the usage data.

### Section Name: Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section analyzes revenue and costs associated with different business activities (EVG Street, Terminal) to determine profitability. It breaks down revenue sources, cost components, and calculates per-day costs.
- **Cell Range**: B16:Q74
- **Layout Structure**:
    - **Row Headers Location**: B17:B74, C18:C19, C24, C29, C33, C37, C41, C42, C43, C57:C63
    - **Column Headers Location**: H16:Q16
    - **Data Range**:
      - Annual data: H17:Q74
- **Time Series Details**:
    - **Date Range**: The data in H16:Q16 is not explicitly labeled with dates, but the context suggests an annual time series. Assuming the first column (H) represents 2015 and each subsequent column is a year, the range is 2015 to 2021.
    - **Frequency**: Annual
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, M&R Cost, Admin Expense, Repo Expense, Other Expense, Lease Costs.
- **Notes & Customizations**: The section includes calculations for per-usage-day costs and incorporates various lease cost components. It also includes annual inflation assumptions in U32:V41.

### Section Name: EBITDA Calculation
- **Section Type**: Standard P&L
- **Description & Purpose**: This section calculates EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization) based on the revenue and cost analysis. It also calculates EBITDA per usage day and EBITDA margin.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76, C77, C78, B79
    - **Column Headers Location**: H16:Q16 (same as previous section)
    - **Data Range**:
      - Annual data: H76:Q79
- **Time Series Details**:
    - **Date Range**: The data in H16:Q16 is not explicitly labeled with dates, but the context suggests an annual time series. Assuming the first column (H) represents 2015 and each subsequent column is a year, the range is 2015 to 2021.
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: The section calculates EBITDA and related metrics based on the preceding revenue and cost analysis.

### Section Name: Chassis Acquisition Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the costs associated with acquiring chassis, including purchase price, reconditioning, decoupling, repositioning, and other related expenses. It calculates the total effective purchase price.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98, B100
    - **Column Headers Location**: None (single period analysis)
    - **Data Range**: G83:G98, G100
- **Time Series Details**:
    - **Date Range**: This section represents a single period or upfront analysis, not a time series.
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Working Capital Investment, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: This section focuses on the upfront costs associated with acquiring chassis.

### Section Name: Cash Flow Projections
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on the investment in chassis, including depreciation, EBIT, taxes, and Capex. It calculates total cash flows and unlevered IRR. There are two separate cash flow projections, one based on a depreciated value exit and another based on a TEV exit.
- **Cell Range**: B104:Q136
- **Layout Structure**:
    - **Row Headers Location**: B104:B119, B121:B136
    - **Column Headers Location**: G104:Q104, G121:L121
    - **Data Range**:
      - Annual data (Depreciated Value Exit): H108:Q115, G117
      - Annual data (TEV Exit): H125:L132, G134
- **Time Series Details**:
    - **Date Range**:
      - Annual (Depreciated Value Exit): 2015 to 2021 (assuming H represents 2015)
      - Annual (TEV Exit): 1979 to 1979 (based on date_series_definitions)
    - **Frequency**:
      - Annual (Depreciated Value Exit)
      - Annual (TEV Exit)
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: This section includes two different exit scenarios for cash flow projections. The TEV exit uses a repeating annual series from 1979.


====================================================================================================
# SHEET 9: MCCP
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: MCCP
- **Key Sections Identified**:
    - Header/Title Section
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Chassis Acquisition Analysis
    - Cash Flow Projections - Depreciated Value Exit
    - Cash Flow Projections - TEV Exit

## 2. Detailed Section Analysis

### Header/Title Section
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the analysis and potentially other high-level information.
- **Cell Range**: A1:G3
- **Layout Structure**:
    - **Row Headers Location**: A1:A3, F3
    - **Column Headers Location**: None
    - **Data Range**: G3 (MH Erosion value)
- **Time Series Details**: None
- **Key Components**: Evergreen, MCCP, MH Erosion
- **Notes & Customizations**: Basic header information.

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the utilization of assets (chassis) across different segments (Street - MH, Street - EVG, Terminal). Includes percentage breakdowns and utilization rates.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied years, but not explicitly labeled)
    - **Data Range**: G7:Q13
- **Time Series Details**:
    - **Date Range**: Implied annual series, likely 2015 to 2021 (based on column count).
    - **Frequency**: Annual
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate
- **Notes & Customizations**: Utilization metrics for different segments.

### Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the revenue and cost components related to chassis usage, broken down by segment (EVG Street, Terminal). Includes calculations of costs per usage day.
- **Cell Range**: B16:Q74
- **Layout Structure**:
    - **Row Headers Location**: B17:B74, C19, C24, C29, C33, C37, C41, C42, C43, C57:C63
    - **Column Headers Location**: H16:Q16 (Implied years, but not explicitly labeled)
    - **Data Range**: H17:Q74, E17:G19
- **Time Series Details**:
    - **Date Range**: Implied annual series, likely 2015 to 2021 (based on column count).
    - **Frequency**: Annual
- **Key Components**: EVG, Street - EVG, Terminal, Revenue, EVG Street Costs, Terminal Billings, M&R Cost, Admin Expense, Repo Expense, Total Cost
- **Notes & Customizations**: Detailed revenue and cost breakdown, including per-day metrics. Includes inflation assumptions in columns U and V.

### EBITDA Calculation
- **Section Type**: Standard P&L
- **Description & Purpose**: Calculates EBITDA and related metrics based on the revenue and cost analysis.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76, C77, C78, B79
    - **Column Headers Location**: H16:Q16 (Implied years, but not explicitly labeled)
    - **Data Range**: H76:Q79
- **Time Series Details**:
    - **Date Range**: Implied annual series, likely 2015 to 2021 (based on column count).
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%)
- **Notes & Customizations**: Standard EBITDA calculation.

### Chassis Acquisition Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes the costs associated with acquiring chassis, including purchase price, reconditioning, and other related expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: None
    - **Data Range**: G83:G100, F88
- **Time Series Details**: None
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Working Capital Investment, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned
- **Notes & Customizations**: One-time acquisition cost analysis.

### Cash Flow Projections - Depreciated Value Exit
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: Projects cash flows based on a depreciated value exit scenario.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B104:B119
    - **Column Headers Location**: G104:Q104 (Years)
    - **Data Range**: G105:Q119, E111, E113, E119, F119
- **Time Series Details**:
    - **Date Range**: 2015 to 2021 (based on column count).
    - **Frequency**: Annual
- **Key Components**: Investment, EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV
- **Notes & Customizations**: Cash flow projections with a depreciated value exit.

### Cash Flow Projections - TEV Exit
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: Projects cash flows based on a Total Enterprise Value (TEV) exit scenario.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B121:B136
    - **Column Headers Location**: G121:L121 (Years)
    - **Data Range**: G122:L136, E123, E128, E130, E136
- **Time Series Details**:
    - **Date Range**: 2015 to 2020 (based on column count).
    - **Frequency**: Annual
- **Key Components**: Investment, EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR
- **Notes & Customizations**: Cash flow projections with a TEV exit.


====================================================================================================
# SHEET 10: MWCP
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: MWCP
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Chassis Acquisition Analysis
    - Cash Flow Projections (Depreciated Value Exit)
    - Cash Flow Projections (TEV Exit)
    - Annual Inflation Assumptions

## 2. Detailed Section Analysis

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of assets (chassis) across different locations (Street - MH, Street - EVG, Terminal) and calculates utilization rates. It provides a high-level overview of asset usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C5:C13
    - **Column Headers Location**: G6:Q6
    - **Data Range**:
      - Annual data: G7:Q12
- **Time Series Details**:
    - **Date Range**: Not explicitly specified in the provided data, but based on the subsequent sections, it appears to cover a multi-year period. Assuming 2015-2027 based on the other sections.
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: The section calculates percentages and utilization rates based on the usage data.

### Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section details the revenue and cost components related to the business, broken down by different categories (e.g., EVG Street, Terminal). It calculates revenue, various costs (M&R, Admin, Repo, etc.), and provides per-day cost metrics.
- **Cell Range**: B17:Q74
- **Layout Structure**:
    - **Row Headers Location**: B17:B74, C19, C29, C33, C37, C41, C42, C43, C57:C63
    - **Column Headers Location**: H16:Q16
    - **Data Range**:
      - Annual data: H17:Q74 (with some exceptions like E17:G19)
- **Time Series Details**:
    - **Date Range**: Not explicitly specified in the provided data, but based on the subsequent sections, it appears to cover a multi-year period. Assuming 2015-2027 based on the other sections.
    - **Frequency**: Annual
- **Key Components**: EVG Street Revenue, Terminal Revenue, Total Revenue, M&R Cost, Admin Expense, Repo Expense, Total Cost.
- **Notes & Customizations**: This section includes calculations for "Per Usage Day" costs and "Per Contr. Day" costs, indicating a focus on daily operational metrics. It also includes lease costs and gain sharing.

### EBITDA Calculation
- **Section Type**: Standard P&L
- **Description & Purpose**: This section calculates EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization) based on the revenue and cost data from the previous section. It also calculates EBITDA per Usage Day and EBITDA Margin.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76, C77, C78, B79
    - **Column Headers Location**: H16:Q16
    - **Data Range**:
      - Annual data: H76:Q79
- **Time Series Details**:
    - **Date Range**: Not explicitly specified in the provided data, but based on the subsequent sections, it appears to cover a multi-year period. Assuming 2015-2027 based on the other sections.
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: This section focuses on profitability metrics related to asset utilization.

### Chassis Acquisition Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the costs associated with acquiring chassis, including the purchase price, reconditioning costs, and other related expenses. It calculates the total effective purchase price.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98, B100
    - **Column Headers Location**: G82
    - **Data Range**:
      - Single period data: G83:G98, G100
- **Time Series Details**:
    - **Date Range**: Single period (Upfront)
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: This section provides a detailed breakdown of the costs involved in acquiring chassis assets.

### Cash Flow Projections (Depreciated Value Exit)
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit scenario. It includes investments, EBITDA, depreciation, taxes, working capital investment, capex, and calculates the unlevered IRR and NPV.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B104:B119
    - **Column Headers Location**: G6:Q6
    - **Data Range**:
      - Annual data: G104:Q117
- **Time Series Details**:
    - **Date Range**: Not explicitly specified in the provided data, but based on the subsequent sections, it appears to cover a multi-year period. Assuming 2015-2027 based on the other sections.
    - **Frequency**: Annual
- **Key Components**: EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: This section models the financial performance of the business under a specific exit scenario.

### Cash Flow Projections (TEV Exit)
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit scenario. It includes investments, EBITDA, depreciation, taxes, working capital investment, capex, and calculates the unlevered IRR and NPV.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B121:B136
    - **Column Headers Location**: Not explicitly specified, but assumed to be similar to the previous section.
    - **Data Range**:
      - Annual data: H125:L134
- **Time Series Details**:
    - **Date Range**: Not explicitly specified in the provided data, but based on the subsequent sections, it appears to cover a multi-year period. Assuming 2015-2020 based on the column range.
    - **Frequency**: Annual
- **Key Components**: EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: This section models the financial performance of the business under a specific exit scenario.

### Annual Inflation Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the annual inflation assumptions used in the financial projections.
- **Cell Range**: U32:V41
- **Layout Structure**:
    - **Row Headers Location**: U33:U41
    - **Column Headers Location**: U32
    - **Data Range**:
      - Single period data: V33:V41
- **Time Series Details**:
    - **Date Range**: Single period (Current)
    - **Frequency**: N/A
- **Key Components**: Trucker Rate Inflation, EVG Rate Inflation, Terminal Rate Inflation, M&R Cost Inflation, Admin Cost Inflation, Repo Cost Inflation, Other Cost Inflation.
- **Notes & Customizations**: This section provides the key assumptions driving the cost and revenue projections.


====================================================================================================
# SHEET 11: SACP
====================================================================================================

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


====================================================================================================
# SHEET 12: PSW
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: PSW
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Chassis Acquisition Analysis
    - Cash Flow Projections (Depreciated Value Exit)
    - Cash Flow Projections (TEV Exit)
    - Inflation Assumptions

## 2. Detailed Section Analysis

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of utilization metrics for Street - MH, Street - EVG, and Terminal, including percentages and utilization rates. This section is used to understand the efficiency of chassis usage across different categories.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C5:C13
    - **Column Headers Location**: G6:Q6 (Implied years, but not explicitly stated)
    - **Data Range**: G7:Q12
- **Time Series Details**:
    - **Date Range**: Implied annual series, but the years are not explicitly stated in the data. Assuming 2015-2021 based on the number of columns.
    - **Frequency**: Annual
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: The percentages provide a comparative view of utilization across different segments.

### Section Name: Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the revenue and cost components related to EVG Street and Terminal operations. This section helps in understanding the drivers of revenue and costs.
- **Cell Range**: B16:Q74
- **Layout Structure**:
    - **Row Headers Location**: B17:B74, C19, C24, C29, C33, C37, C41, C43, C57:C63
    - **Column Headers Location**: H16:Q16 (Implied years, but not explicitly stated)
    - **Data Range**: H17:Q74
- **Time Series Details**:
    - **Date Range**: Implied annual series, but the years are not explicitly stated in the data. Assuming 2015-2021 based on the number of columns.
    - **Frequency**: Annual
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, M&R Cost, Admin Expense, Repo Expense, Other Expense, Lease Costs, Total Cost.
- **Notes & Customizations**: Includes calculations for costs per usage day and street day. Also includes inflation assumptions in columns U and V.

### Section Name: EBITDA Calculation
- **Section Type**: Standard P&L
- **Description & Purpose**: Calculates EBITDA and related metrics based on the revenue and cost analysis. This section provides a key profitability measure.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76, C77, C78, B79
    - **Column Headers Location**: H71:Q71 (Date series detected, but seemingly incorrect. It's an annual series from 2080, which is likely an error. Assuming 2015-2021 based on the number of columns.)
    - **Data Range**: H76:Q79
- **Time Series Details**:
    - **Date Range**: 2080-01-01 repeating 10 periods (as per `date_series_definitions`, but likely incorrect). Assuming 2015-2021 based on the number of columns.
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Uses the results from the Revenue and Cost Analysis section.

### Section Name: Chassis Acquisition Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes the costs associated with acquiring chassis, including reconditioning, decoupling, repositioning, and other related expenses. This section is used to determine the total effective purchase price.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98, B100
    - **Column Headers Location**: G82
    - **Data Range**: G83:G98, G100
- **Time Series Details**:
    - **Date Range**: Single point in time (Upfront).
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Price per Chassis, Payment to EVG, Total Chassis Price, Reconditioning Costs, Decouping Costs, Working Capital Investment, Total Effective Purchase Price.
- **Notes & Customizations**: This section focuses on upfront costs and does not involve a time series.

### Section Name: Cash Flow Projections (Depreciated Value Exit)
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: Projects cash flows based on a depreciated value exit strategy. This section is used to evaluate the financial viability of the investment under this exit scenario.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B104:B119
    - **Column Headers Location**: H108:Q108 (Implied years, but not explicitly stated)
    - **Data Range**: G104:Q119
- **Time Series Details**:
    - **Date Range**: Implied annual series, but the years are not explicitly stated in the data. Assuming 2015-2021 based on the number of columns.
    - **Frequency**: Annual
- **Key Components**: Investment, EBITDA, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes NPV and IRR calculations.

### Section Name: Cash Flow Projections (TEV Exit)
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: Projects cash flows based on a Total Enterprise Value (TEV) exit strategy. This section is used to evaluate the financial viability of the investment under this exit scenario.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B121:B136
    - **Column Headers Location**: H125:L125 (Implied years, but not explicitly stated)
    - **Data Range**: G121:L136
- **Time Series Details**:
    - **Date Range**: Implied annual series, but the years are not explicitly stated in the data. Assuming 2015-2019 based on the number of columns.
    - **Frequency**: Annual
- **Key Components**: Investment, EBITDA, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes NPV and IRR calculations.

### Section Name: Inflation Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines the annual inflation assumptions used in the model.
- **Cell Range**: U32:V41
- **Layout Structure**:
    - **Row Headers Location**: U32:U41
    - **Column Headers Location**: None
    - **Data Range**: V33:V41
- **Time Series Details**:
    - **Date Range**: N/A (Single point in time).
    - **Frequency**: N/A
- **Key Components**: Trucker Rate Inflation, EVG Rate Inflation, Terminal Rate Inflation, M&R Cost Inflation, Admin Cost Inflation, Repo Cost Inflation, Other Cost Inflation.
- **Notes & Customizations**: These assumptions drive the inflation adjustments in the Revenue and Cost Analysis section.


====================================================================================================
# SHEET 13: Customer Output - LA
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Customer Output - LA
- **Key Sections Identified**:
    - Header
    - Assumptions
    - Scenario Table

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the report.
- **Cell Range**: A1:A3
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: None
    - **Data Range**: A1:A3
- **Time Series Details**: None
- **Key Components**: Company Name, Report Title, Location
- **Notes & Customizations**: Simple header information.

### Assumptions
- **Section Type**: Assumptions
- **Description & Purpose**: Lists the key assumptions used in the calculations.
- **Cell Range**: C5:C10
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: None
    - **Data Range**: C5:C10
- **Time Series Details**: None
- **Key Components**: Chassis age, EVG usage, MH billing rate, Terminal usage.
- **Notes & Customizations**: Numbered list of assumptions.

### Scenario Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents different scenarios with varying purchase prices, MH percentages, and rates.
- **Cell Range**: B13:G33
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 13
    - **Data Range**: C14:G33
- **Time Series Details**: None
- **Key Components**: Purchase Price per Chassis, Total Purchase Price, MH %, CH Rate, Terminal Rate.
- **Notes & Customizations**: Data is scaled by 1000 in columns C, D, F, and G.



====================================================================================================
# SHEET 14: Customer Output - APMT
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Customer Output - APMT
- **Key Sections Identified**:
    - Header
    - Assumptions
    - Purchase Price Table

## 2. Detailed Section Analysis

### Section Name (Header)
- **Section Type**: Header
- **Description & Purpose**: Contains the title and subtitle of the report, specifying the customer and report type.
- **Cell Range**: A1:A3
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: A1:A3
- **Time Series Details**: N/A
- **Key Components**: "Direct ChassisLink Inc.", "Summary of Options for EVG", "APMT"
- **Notes & Customizations**: N/A

### Section Name (Assumptions)
- **Section Type**: Assumptions
- **Description & Purpose**: Lists the key assumptions used in the calculations and analysis presented in the spreadsheet.
- **Cell Range**: C5:C10
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: C5:C10
- **Time Series Details**: N/A
- **Key Components**: Assumptions related to chassis age, usage, and billing rates.
- **Notes & Customizations**: N/A

### Section Name (Purchase Price Table)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents key metrics related to purchase price, MH percentage, and rates.
- **Cell Range**: B13:G33
- **Layout Structure**:
    - **Row Headers Location**: B14:B33
    - **Column Headers Location**: C13:G13
    - **Data Range**: B14:B33 (Purchase Price per Chassis), D14:D33 (Total Purchase Price), E14:E33 (MH %), F14:F33 (CH Rate), G14:G33 (Terminal Rate)
- **Time Series Details**: N/A
- **Key Components**: Purchase Price per Chassis, Total Purchase Price, MH %, CH Rate, Terminal Rate
- **Notes & Customizations**: N/A



====================================================================================================
# SHEET 15: PNW
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: PNW
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Upfront Investment Analysis
    - Cash Flow Projections (Depreciated Value Exit)
    - Cash Flow Projections (TEV Exit)
    - Annual Inflation Assumptions

## 2. Detailed Section Analysis

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of assets (chassis) across different categories (Street - MH, Street - EVG, Terminal) and calculates utilization rates. It provides a high-level overview of asset usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (implied years)
    - **Data Range**: G7:Q12
- **Time Series Details**:
    - **Date Range**: Implied years, likely 2015 to 2021 (based on other sections).
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate
- **Notes & Customizations**: The percentages provide a breakdown of utilization across different categories.

### Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section analyzes revenue and costs related to EVG Street and Terminal operations. It breaks down revenue by source (Trucker, EVG, Terminal) and costs by type (M&R, Admin, Repo, etc.). It helps understand the profitability drivers of the business.
- **Cell Range**: B16:Q74
- **Layout Structure**:
    - **Row Headers Location**: B17:B74, C19, C24, C29, C33, C37, C41, C42, C43, C57:C63
    - **Column Headers Location**: H16:Q16 (implied years)
    - **Data Range**: H17:Q74, E17:G19
- **Time Series Details**:
    - **Date Range**: Implied years, likely 2015 to 2021 (based on other sections).
    - **Frequency**: Annual
- **Key Components**: EVG Street Revenue, Terminal Revenue, Total Revenue, M&R Cost, Admin Expense, Repo Expense, Other Expense, Total Cost
- **Notes & Customizations**: Includes calculations for cost per usage day and various lease costs.

### EBITDA Calculation
- **Section Type**: Standard P&L (EBITDA section)
- **Description & Purpose**: This section calculates EBITDA and related metrics (EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin). It provides a measure of operating profitability.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76, C77, C78, B79
    - **Column Headers Location**: H76:Q76 (implied years)
    - **Data Range**: H76:Q79
- **Time Series Details**:
    - **Date Range**: Implied years, likely 2015 to 2021 (based on other sections).
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%)
- **Notes & Customizations**: EBITDA is calculated based on the revenue and cost analysis above.

### Upfront Investment Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the upfront investment required for the transaction, including the purchase price of chassis, reconditioning costs, and working capital investment. It provides a summary of the initial cash outlay.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: G82 (Total (Upfront))
    - **Data Range**: G83:G100, F88
- **Time Series Details**:
    - **Date Range**: Single point in time (Upfront).
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Total Chassis Price, Reconditioning Costs, Working Capital Investment, Total Effective Purchase Price
- **Notes & Customizations**: Includes adjustments for scrap chassis and transaction expenses.

### Cash Flow Projections (Depreciated Value Exit)
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit scenario. It includes EBITDA, depreciation, taxes, working capital investment, and capex. It calculates total cash flows, NPV, and unlevered IRR.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B104:B119
    - **Column Headers Location**: H104:Q104 (implied years)
    - **Data Range**: G104:Q117, E111, E113, E119, F119
- **Time Series Details**:
    - **Date Range**: Implied years, likely 2015 to 2021 (based on other sections).
    - **Frequency**: Annual
- **Key Components**: EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR
- **Notes & Customizations**: Includes a calculation for NPV.

### Cash Flow Projections (TEV Exit)
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit scenario. It includes EBITDA, depreciation, taxes, working capital investment, and capex. It calculates total cash flows, and unlevered IRR.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B121:B136
    - **Column Headers Location**: H125:L125 (implied years)
    - **Data Range**: G122:L134, E128, E130, E136
- **Time Series Details**:
    - **Date Range**: Implied years, likely 2015 to 2020 (based on other sections).
    - **Frequency**: Annual
- **Key Components**: EBITDA, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR
- **Notes & Customizations**: Includes a calculation for exit value.

### Annual Inflation Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section lists the annual inflation assumptions used in the model for various cost and revenue components.
- **Cell Range**: U32:V41
- **Layout Structure**:
    - **Row Headers Location**: U33:U41
    - **Column Headers Location**: U32 (Annual Inflation Assumptions:)
    - **Data Range**: V33:V41
- **Time Series Details**:
    - **Date Range**: Single point in time (Assumptions).
    - **Frequency**: N/A
- **Key Components**: Trucker Rate Inflation, EVG Rate Inflation, Terminal Rate Inflation, M&R Cost Inflation, Admin Cost Inflation, Repo Cost Inflation, Other Cost Inflation
- **Notes & Customizations**: These assumptions drive the growth rates in the projected financials.


====================================================================================================
# SHEET 16: Oakland
====================================================================================================

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


====================================================================================================
# SHEET 17: NE
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: NE
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue and Cost Analysis
    - EBITDA Calculation
    - Chassis Acquisition Analysis
    - Cash Flow Projections

## 2. Detailed Section Analysis

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of utilization metrics for Street-MH, Street-EVG, and Terminal operations. It calculates utilization rates and percentages.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C5:C13
    - **Column Headers Location**: G6:Q6 (Implied years, likely 2015-2021 based on other sections)
    - **Data Range**: G7:Q12
- **Time Series Details**:
    - **Date Range**: 2015 to 2021 (inferred from other sections)
    - **Frequency**: Annual
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate
- **Notes & Customizations**: The section calculates percentages of different categories and utilization rates.

### Revenue and Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section analyzes revenue and costs related to EVG Street and Terminal operations. It calculates revenue, costs, and per-day metrics.
- **Cell Range**: B16:Q74
- **Layout Structure**:
    - **Row Headers Location**: B17:B74, C19, C24, C29, C33, C37, C41, C42, C43, C57:C63
    - **Column Headers Location**: H16:Q16 (Implied years, likely 2015-2021 based on other sections)
    - **Data Range**:
      - Annual data: H17:Q74
- **Time Series Details**:
    - **Date Range**: 2015 to 2021 (inferred from other sections)
    - **Frequency**: Annual
- **Key Components**: EVG Street Revenue, Terminal Revenue, Total Revenue, M&R Cost, Admin Expense, Repo Expense, Other Expense, Total Cost
- **Notes & Customizations**: This section includes calculations for revenue, costs, and per-day metrics for both EVG Street and Terminal operations. It also includes annual inflation assumptions in columns U and V.

### EBITDA Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates EBITDA and related metrics, such as EBITDA per Usage Day, EBITDA per Chassis per Day, and EBITDA Margin (%).
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76, C77, C78, B79
    - **Column Headers Location**: H16:Q16 (Implied years, likely 2015-2021 based on other sections)
    - **Data Range**: H76:Q79
- **Time Series Details**:
    - **Date Range**: 2015 to 2021 (inferred from other sections)
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%)
- **Notes & Customizations**: This section focuses on EBITDA-related metrics and their trends over time.

### Chassis Acquisition Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the costs associated with acquiring chassis, including the purchase price, reconditioning costs, and other related expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98, B100
    - **Column Headers Location**: G82
    - **Data Range**: G83:G98, G100
- **Time Series Details**:
    - **Date Range**: Single point in time (Upfront)
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Total Chassis Price, Reconditioning Costs, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned
- **Notes & Customizations**: This section provides a detailed breakdown of the costs associated with acquiring chassis.

### Cash Flow Projections
- **Section Type**: Cash Flow Projections
- **Description & Purpose**: This section projects cash flows based on depreciated value exit and TEV exit scenarios. It calculates key metrics such as Unlevered IRR and NPV.
- **Cell Range**: B104:Q136
- **Layout Structure**:
    - **Row Headers Location**: B104, B106, B105, B121, B123, B108:B117, B119, B125:B134, B136
    - **Column Headers Location**: G104:Q104 (Years, likely 2015-2021), G121:L121 (Years, likely 2015-2020)
    - **Data Range**:
      - Annual data (Depreciated Value Exit): H108:Q115, G117
      - Annual data (TEV Exit): H125:L132, G134
- **Time Series Details**:
    - **Date Range**: 2015 to 2021 (Depreciated Value Exit), 2015 to 2020 (TEV Exit)
    - **Frequency**: Annual
- **Key Components**: Investment, EBITDA, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV
- **Notes & Customizations**: This section includes two cash flow projection scenarios: one based on depreciated value exit and another based on TEV exit. It calculates key financial metrics such as Unlevered IRR and NPV.


====================================================================================================
# SHEET 18: HRCP
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: HRCP
- **Key Sections Identified**:
    - Utilization Summary
    - Revenue & Cost Analysis
    - Chassis Acquisition Analysis
    - Cash Flow Projections

## 2. Detailed Section Analysis

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of assets (presumably chassis) across different categories (Street-MH, Street-EVG, Terminal). It provides key metrics like utilization rates and percentages.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C5:C13
    - **Column Headers Location**: G6:Q6 (Implied years, but not explicitly labeled)
    - **Data Range**: G7:Q13
- **Time Series Details**:
    - **Date Range**: Implied years, but not explicitly labeled. Assuming 2015 to 2021 based on the number of columns.
    - **Frequency**: Annual
- **Key Components**: Net Lease Billed Days, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Utilization metrics are calculated for different categories of assets.

### Revenue & Cost Analysis
- **Section Type**: Custom P&L
- **Description & Purpose**: This section analyzes revenue and costs associated with chassis usage, breaking down revenue by source (Trucker Street, Net Lease, Terminal) and costs by type (M&R, Admin, Repo, etc.). It calculates revenue, costs, and per-day metrics.
- **Cell Range**: B16:Q79
- **Layout Structure**:
    - **Row Headers Location**: B17:B79 and C19, C24, C25, C29, C33, C37, C41, C42, C43, C57:C63, C77, C78
    - **Column Headers Location**: H16:Q16 (Implied years, but not explicitly labeled)
    - **Data Range**:
      - Annual data: H17:Q79
- **Time Series Details**:
    - **Date Range**: Implied years, but not explicitly labeled. Assuming 2015 to 2021 based on the number of columns.
    - **Frequency**: Annual
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, M&R Cost, Admin Expense, Repo Expense, EBITDA, EBITDA per Usage Day, EBITDA Margin (%).
- **Notes & Customizations**: The section includes calculations for per-usage-day costs and revenue.

### Chassis Acquisition Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the costs associated with acquiring chassis, including the purchase price, reconditioning costs, and other related expenses. It calculates the total effective purchase price and related metrics.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: G82
    - **Data Range**: G83:G100
- **Time Series Details**: This section does NOT contain a time series. It represents a one-time analysis.
- **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Total Chassis Price, Reconditioning Costs, Total Effective Purchase Price.
- **Notes & Customizations**: This section focuses on upfront costs associated with acquiring chassis.

### Cash Flow Projections
- **Section Type**: Standard P&L
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit and a Total Enterprise Value (TEV) exit. It calculates key metrics like Unlevered IRR and NPV.
- **Cell Range**: B104:Q136
- **Layout Structure**:
    - **Row Headers Location**: B105:B117, B119, B121, B123, B125:B134, B136
    - **Column Headers Location**: G6:Q6 (Implied years, but not explicitly labeled)
    - **Data Range**:
      - Annual data (Depreciated Value Exit): H108:Q115
      - Annual data (Total Enterprise Value Exit): H125:L132
- **Time Series Details**:
    - **Date Range**:
      - Depreciated Value Exit: Implied years, but not explicitly labeled. Assuming 2015 to 2021 based on the number of columns.
      - TEV Exit: Implied years, but not explicitly labeled. Assuming 2015 to 2019 based on the number of columns.
    - **Frequency**: Annual
- **Key Components**: EBITDA, Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: The section includes two different exit scenarios (depreciated value and TEV), each with its own set of cash flow projections.


====================================================================================================
# SHEET 19: Support Data -->
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Support Data -->
- **Key Sections Identified**: Header

## 2. Detailed Section Analysis

### Section Name (e.g., "Header")
- **Section Type**: Header
- **Description & Purpose**: Contains the sheet title.
- **Cell Range**: A1:A1
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: A1:A1
- **Time Series Details**:
    - N/A
- **Key Components**: Sheet Title
- **Notes & Customizations**: N/A



====================================================================================================
# SHEET 20: PoP Usage Data
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: PoP Usage Data
- **Key Sections Identified**:
    - Title/Header
    - Chassis Usage Data by Company
    - Totals & Utilization Metrics
    - Footnotes

## 2. Detailed Section Analysis

### Title/Header
- **Section Type**: Title/Header
- **Description & Purpose**: Contains the title of the report and a brief description.
- **Cell Range**: C2:F3
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: E3:F3
    - **Data Range**: N/A
- **Time Series Details**:
    - **Date Range**: W.E. 3/7/2015 to W.E. 3/14/2015
    - **Frequency**: Weekly
- **Key Components**: Pool of Pools Chassis on the Street* - WEEKLY AVERAGE, W.E. 3/7/2015, W.E. 3/14/2015
- **Notes & Customizations**: The title indicates that the data represents a weekly average of chassis on the street.

### Chassis Usage Data by Company
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the chassis usage data for various companies.
- **Cell Range**: C4:F33
- **Layout Structure**:
    - **Row Headers Location**: C4:C33
    - **Column Headers Location**: E3:F3
    - **Data Range**: E4:F33
- **Time Series Details**:
    - **Date Range**: W.E. 3/7/2015 to W.E. 3/14/2015
    - **Frequency**: Weekly
- **Key Components**: Horizon Lines, Hamburg Sud - SSA Piers A and J, Maersk, MSC, DCLP, APL, Evergreen - YTI, Hanjin - YTI, Hapag-Lloyd, Hyundai, MOL, NYK, OOCL, GACP, China Shipping, CMA-CGM, COSCO, Evergreen - All Other, Hamburg Sud - All Other, Hanjin - All Other, K Line, Pacific International, Polynesia Line, United Arab Shipping, Wan Hai Lines, Yang Ming Line, Zim Israel Navigation Co., LABP
- **Notes & Customizations**: The data is scaled by 1000.

### DCSZ and Unassigned Chassis Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the chassis usage data for DCSZ and Unassigned chassis.
- **Cell Range**: C35:F37
- **Layout Structure**:
    - **Row Headers Location**: C35:C37
    - **Column Headers Location**: E3:F3
    - **Data Range**: E35:F37
- **Time Series Details**:
    - **Date Range**: W.E. 3/7/2015 to W.E. 3/14/2015
    - **Frequency**: Weekly
- **Key Components**: DCSZ (bare outs, no SS SCAC)**, Unassigned (no SS SCAC or unauthorized)
- **Notes & Customizations**: The data is scaled by 1000.

### Totals & Utilization Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates totals and utilization metrics based on the chassis usage data.
- **Cell Range**: C39:F54
- **Layout Structure**:
    - **Row Headers Location**: C39:C54
    - **Column Headers Location**: E3:F3
    - **Data Range**: E39:F54
- **Time Series Details**:
    - **Date Range**: W.E. 3/7/2015 to W.E. 3/14/2015
    - **Frequency**: Weekly
- **Key Components**: Total Chassis on the Street, Pool of Pools Fleet, Total Street Utilization (incl. DCSZ and unassigned), DCLP Fleet, GACP Fleet, DCLI-GACP Fleet, TRAC-GACP Fleet, LABP Fleet, DCLP Street Utilization, GACP Street Utilization, DCLI-GACP Street Utilization, TRAC-GACP Street Utilization, LABP Street Utilization
- **Notes & Customizations**: Some data is scaled by 1000, while utilization is a percentage.

### Footnotes
- **Section Type**: Notes
- **Description & Purpose**: Provides additional context and explanations for the data.
- **Cell Range**: C56:C57
- **Layout Structure**:
    - **Row Headers Location**: C56:C57
    - **Column Headers Location**: N/A
    - **Data Range**: N/A
- **Time Series Details**: N/A
- **Key Components**: * Reflects chassis with gated-out status by day by steamship line scac, ** Generally, DCSZ is used as the steamship scac when the chassis gates out bare with no container
- **Notes & Customizations**: These footnotes clarify the meaning of certain data points and abbreviations used in the spreadsheet.



====================================================================================================
# SHEET 21: Fleet Summary - Pending
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Fleet Summary - Pending
- **Key Sections Identified**:
    - Header Information
    - Assumptions
    - Chassis Age Analysis

## 2. Detailed Section Analysis

### Section Name: Header Information
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the report.
- **Cell Range**: A1:A3
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: None
    - **Data Range**: A1:A3
- **Time Series Details**: None
- **Key Components**: Company Name, Report Title
- **Notes & Customizations**: Basic header information.

### Section Name: Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains key assumptions used in the analysis, such as Value New, Residual Value, and Useful Life.
- **Cell Range**: B5:C7
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C5:C7
- **Time Series Details**: None
- **Key Components**: Value New, Residual Value, Useful Life
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: ASI/CSG Premium
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains ASI/CSG Premium value.
- **Cell Range**: B8:D10
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: D10
- **Time Series Details**: None
- **Key Components**: Premium, ASI/CSG
- **Notes & Customizations**: Single value.

### Section Name: Chassis Age Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes chassis based on age, providing counts, percentages, and value calculations.
- **Cell Range**: B11:M13
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 11
    - **Data Range**: D12:M13
- **Time Series Details**: None
- **Key Components**: Year, Date Estimate, Count, % of total, Book Value Per, Purchase Per, Total Purchase, Age 10 years Later, Depreciated 10 year value per, Depreciated 10 year value total
- **Notes & Customizations**: Values are scaled by 1000. Contains calculations for 10-year depreciation.

### Section Name: Chassis Age Analysis - Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of chassis book values.
- **Cell Range**: B16:C38
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C19:C38
- **Time Series Details**: None
- **Key Components**: Book Value, PO
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 22: Fleet Sizing
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Fleet Sizing
- **Key Sections Identified**:
    - Fleet Sizing Calculation Table
    - Data Source & Assumptions

## 2. Detailed Section Analysis

### Section Name: Fleet Sizing Calculation Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the required chassis for Evergreen PSW LSA/LGB operations based on gate-outs, dwell times, and stress levels. It aims to determine the optimal fleet size under different utilization scenarios (85% and 95%).
- **Cell Range**: A1:D12
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 1 (Evergreen PSW LSA/LGB), Row 2 (at 85%, at 95%)
    - **Data Range**:
      - B3:C12 (data for 85% and 95% utilization)
      - D7:D12 (additional data, possibly a different calculation or scenario)
- **Time Series Details**:
    - **Date Range**: Not explicitly time-series data, but rather scenario-based calculations.
    - **Frequency**: N/A
- **Key Components**: gate-outs in period, dwell, chassis on the street in period, days in period, chassis on street, stress, chassis required for street, percentage of terminal chassis, chassis required for terminal, chassis required for Evergreen.
- **Notes & Customizations**: The calculations are performed for two different utilization rates (85% and 95%). The scale of some values is in thousands.

### Section Name: Data Source & Assumptions
- **Section Type**: Notes
- **Description & Purpose**: This section provides information about the data sources used for the calculations and the assumptions made in the analysis.
- **Cell Range**: A15:A17
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: None
    - **Data Range**: A15:A17
- **Time Series Details**:
    - **Date Range**: Refers to data from April, May, June 2015 for dwell time analysis.
    - **Frequency**: N/A
- **Key Components**: Data source (CMS-PC and Evergreen statement), OOS (out-of-service) consideration, Dwell analysis period.
- **Notes & Customizations**: This section contains textual descriptions of the data sources and assumptions.

