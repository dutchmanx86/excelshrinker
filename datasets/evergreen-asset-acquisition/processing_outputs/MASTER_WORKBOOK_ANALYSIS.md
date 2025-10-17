# Master Workbook Analysis

This document provides a comprehensive analysis of all sheets in the Excel workbook.

---

## Table of Contents

1. [(Sheet name is not provided in the JSON. Assuming "Assumptions")](#(sheet-name-is-not-provided-in-the-json.-assuming-"assumptions"))
   - [Utilization & Purchase Assumptions](#(sheet-name-is-not-provided-in-the-json.-assuming-"assumptions")-utilization-&-purchase-assumptions)
   - [Purchase/Lease Cost Assumptions](#(sheet-name-is-not-provided-in-the-json.-assuming-"assumptions")-purchaselease-cost-assumptions)
   - [Upfront Investment Assumptions](#(sheet-name-is-not-provided-in-the-json.-assuming-"assumptions")-upfront-investment-assumptions)
   - [Operating Assumptions](#(sheet-name-is-not-provided-in-the-json.-assuming-"assumptions")-operating-assumptions)
2. [Summary](#summary)
   - [Transaction Overview](#summary-transaction-overview)
   - [Chassis Fleet Summary](#summary-chassis-fleet-summary)
   - [EVG Pooled Chassis](#summary-evg-pooled-chassis)
   - [Usage Agreement](#summary-usage-agreement)
   - [Utilization Percentages](#summary-utilization-percentages)
   - [Rates (2014)](#summary-rates-2014)
   - [Cost Summary (per Usage Day) - 2014](#summary-cost-summary-per-usage-day---2014)
   - [Summary (2014E)](#summary-summary-2014e)
3. [Evergreen Model Assumptions](#evergreen-model-assumptions)
   - [Section Name: Evergreen Model Assumptions - Region Specific Data](#evergreen-model-assumptions-section-name-evergreen-model-assumptions---region-specific-data)
4. [(Sheet name is not provided in the JSON, assuming it's "Sheet1")](#(sheet-name-is-not-provided-in-the-json,-assuming-it's-"sheet1"))
   - [Fleet Summary and Investment Overview](#(sheet-name-is-not-provided-in-the-json,-assuming-it's-"sheet1")-fleet-summary-and-investment-overview)
   - [Sensitivity Analysis](#(sheet-name-is-not-provided-in-the-json,-assuming-it's-"sheet1")-sensitivity-analysis)
   - [Rate Sensitivity](#(sheet-name-is-not-provided-in-the-json,-assuming-it's-"sheet1")-rate-sensitivity)
5. [Evergreen](#evergreen)
   - [Section Name: Utilization Summary](#evergreen-section-name-utilization-summary)
   - [Section Name: Cost & Revenue Projections](#evergreen-section-name-cost-&-revenue-projections)
   - [Section Name: Chassis Acquisition & Total Purchase Price](#evergreen-section-name-chassis-acquisition-&-total-purchase-price)
   - [Section Name: Cash Flow Analysis - Depreciated Value Exit](#evergreen-section-name-cash-flow-analysis---depreciated-value-exit)
   - [Section Name: Cash Flow Analysis - TEV Exit](#evergreen-section-name-cash-flow-analysis---tev-exit)
6. [Evergreen](#evergreen)
   - [Utilization Summary](#evergreen-utilization-summary)
   - [Cost and Revenue Drivers](#evergreen-cost-and-revenue-drivers)
   - [Chassis Usage and Revenue Projections](#evergreen-chassis-usage-and-revenue-projections)
   - [Revenue and Cost Analysis](#evergreen-revenue-and-cost-analysis)
   - [Chassis Acquisition Cost](#evergreen-chassis-acquisition-cost)
   - [Cash Flow Projections (Depreciated Value Exit)](#evergreen-cash-flow-projections-depreciated-value-exit)
   - [Cash Flow Projections (TEV Exit)](#evergreen-cash-flow-projections-tev-exit)
7. [(Sheet name not provided in JSON, assuming "Sheet1")](#(sheet-name-not-provided-in-json,-assuming-"sheet1"))
   - [Section Name: Utilization Summary](#(sheet-name-not-provided-in-json,-assuming-"sheet1")-section-name-utilization-summary)
   - [Section Name: Cost and Revenue Drivers](#(sheet-name-not-provided-in-json,-assuming-"sheet1")-section-name-cost-and-revenue-drivers)
   - [Section Name: Revenue Projections](#(sheet-name-not-provided-in-json,-assuming-"sheet1")-section-name-revenue-projections)
   - [Section Name: Revenue Summary](#(sheet-name-not-provided-in-json,-assuming-"sheet1")-section-name-revenue-summary)
   - [Section Name: Cost Projections](#(sheet-name-not-provided-in-json,-assuming-"sheet1")-section-name-cost-projections)
   - [Section Name: EBITDA Analysis](#(sheet-name-not-provided-in-json,-assuming-"sheet1")-section-name-ebitda-analysis)
   - [Section Name: Initial Investment](#(sheet-name-not-provided-in-json,-assuming-"sheet1")-section-name-initial-investment)
   - [Section Name: Cash Flows - Depreciated Value Exit](#(sheet-name-not-provided-in-json,-assuming-"sheet1")-section-name-cash-flows---depreciated-value-exit)
   - [Section Name: Cash Flows - TEV Exit](#(sheet-name-not-provided-in-json,-assuming-"sheet1")-section-name-cash-flows---tev-exit)
8. [Evergreen](#evergreen)
   - [Section Name: Utilization Summary](#evergreen-section-name-utilization-summary)
   - [Section Name: Revenue and Cost Drivers](#evergreen-section-name-revenue-and-cost-drivers)
   - [Section Name: Chassis Acquisition & Investment Analysis](#evergreen-section-name-chassis-acquisition-&-investment-analysis)
   - [Section Name: Cash Flow Projections - Depreciated Value Exit](#evergreen-section-name-cash-flow-projections---depreciated-value-exit)
   - [Section Name: Cash Flow Projections - TEV Exit](#evergreen-section-name-cash-flow-projections---tev-exit)
   - [Section Name: Repeating Cash Flow Projections - TEV Exit](#evergreen-section-name-repeating-cash-flow-projections---tev-exit)
9. [Sheet1](#sheet1)
   - [Utilization Summary](#sheet1-utilization-summary)
   - [Cost Breakdown (EVG)](#sheet1-cost-breakdown-evg)
   - [Chassis Usage and Revenue Forecast](#sheet1-chassis-usage-and-revenue-forecast)
   - [Cost Analysis per Usage Day](#sheet1-cost-analysis-per-usage-day)
   - [Expense Forecast](#sheet1-expense-forecast)
   - [EBITDA and Margin Analysis](#sheet1-ebitda-and-margin-analysis)
   - [Chassis Acquisition Costs](#sheet1-chassis-acquisition-costs)
   - [Cash Flow Analysis - Depreciated Value Exit](#sheet1-cash-flow-analysis---depreciated-value-exit)
   - [Cash Flow Analysis - TEV Exit](#sheet1-cash-flow-analysis---tev-exit)
10. [Evergreen](#evergreen)
   - [Section Name: Utilization Summary](#evergreen-section-name-utilization-summary)
   - [Section Name: EVG Cost Analysis](#evergreen-section-name-evg-cost-analysis)
   - [Section Name: Revenue and Usage Days Forecast](#evergreen-section-name-revenue-and-usage-days-forecast)
   - [Section Name: Cost per Usage Day Analysis](#evergreen-section-name-cost-per-usage-day-analysis)
   - [Section Name: Expense Forecast](#evergreen-section-name-expense-forecast)
   - [Section Name: EBITDA Analysis](#evergreen-section-name-ebitda-analysis)
   - [Section Name: Chassis Acquisition Costs](#evergreen-section-name-chassis-acquisition-costs)
   - [Section Name: Cash Flows - Depreciated Value Exit](#evergreen-section-name-cash-flows---depreciated-value-exit)
   - [Section Name: Cash Flows - TEV Exit](#evergreen-section-name-cash-flows---tev-exit)
11. [(Assumed Sheet1, as the JSON doesn't explicitly name the sheet)](#(assumed-sheet1,-as-the-json-doesn't-explicitly-name-the-sheet))
   - [Section Name: Utilization Summary](#(assumed-sheet1,-as-the-json-doesn't-explicitly-name-the-sheet)-section-name-utilization-summary)
   - [Section Name: Cost and Revenue Assumptions](#(assumed-sheet1,-as-the-json-doesn't-explicitly-name-the-sheet)-section-name-cost-and-revenue-assumptions)
   - [Section Name: Chassis Usage and Revenue Projections](#(assumed-sheet1,-as-the-json-doesn't-explicitly-name-the-sheet)-section-name-chassis-usage-and-revenue-projections)
   - [Section Name: Cost Analysis](#(assumed-sheet1,-as-the-json-doesn't-explicitly-name-the-sheet)-section-name-cost-analysis)
   - [Section Name: EBITDA and Margin Analysis](#(assumed-sheet1,-as-the-json-doesn't-explicitly-name-the-sheet)-section-name-ebitda-and-margin-analysis)
   - [Section Name: Chassis Acquisition Costs](#(assumed-sheet1,-as-the-json-doesn't-explicitly-name-the-sheet)-section-name-chassis-acquisition-costs)
   - [Section Name: Cash Flow Analysis - Depreciated Value Exit](#(assumed-sheet1,-as-the-json-doesn't-explicitly-name-the-sheet)-section-name-cash-flow-analysis---depreciated-value-exit)
   - [Section Name: Cash Flow Analysis - TEV Exit](#(assumed-sheet1,-as-the-json-doesn't-explicitly-name-the-sheet)-section-name-cash-flow-analysis---tev-exit)
12. [Evergreen](#evergreen)
   - [Section Name: Utilization Summary](#evergreen-section-name-utilization-summary)
   - [Section Name: Cost and Revenue Drivers](#evergreen-section-name-cost-and-revenue-drivers)
   - [Section Name: Revenue and Cost Analysis](#evergreen-section-name-revenue-and-cost-analysis)
   - [Section Name: Chassis Acquisition](#evergreen-section-name-chassis-acquisition)
   - [Section Name: Investment Analysis - Depreciated Value Exit](#evergreen-section-name-investment-analysis---depreciated-value-exit)
   - [Section Name: Investment Analysis - TEV Exit](#evergreen-section-name-investment-analysis---tev-exit)
13. [(Sheet name is not provided in the JSON, assuming it is "Sheet1")](#(sheet-name-is-not-provided-in-the-json,-assuming-it-is-"sheet1"))
   - [Section Name: Chassis Purchase Options Analysis](#(sheet-name-is-not-provided-in-the-json,-assuming-it-is-"sheet1")-section-name-chassis-purchase-options-analysis)
14. [Sheet1](#sheet1)
   - [Section Name: Assumptions](#sheet1-section-name-assumptions)
   - [Section Name: Input Parameters](#sheet1-section-name-input-parameters)
15. [Evergreen](#evergreen)
   - [Section Name: Utilization Summary](#evergreen-section-name-utilization-summary)
   - [Section Name: Cost and Revenue Drivers](#evergreen-section-name-cost-and-revenue-drivers)
   - [Section Name: Revenue and Cost Summary](#evergreen-section-name-revenue-and-cost-summary)
   - [Section Name: Initial Investment](#evergreen-section-name-initial-investment)
   - [Section Name: Cash Flow Analysis - Depreciated Value Exit](#evergreen-section-name-cash-flow-analysis---depreciated-value-exit)
   - [Section Name: Cash Flow Analysis - TEV Exit](#evergreen-section-name-cash-flow-analysis---tev-exit)
16. [Evergreen](#evergreen)
   - [Section Name: Utilization Summary](#evergreen-section-name-utilization-summary)
   - [Section Name: Cost and Revenue Assumptions](#evergreen-section-name-cost-and-revenue-assumptions)
   - [Section Name: Purchase Price Calculation](#evergreen-section-name-purchase-price-calculation)
   - [Section Name: Cash Flow Analysis - Depreciated Value Exit](#evergreen-section-name-cash-flow-analysis---depreciated-value-exit)
   - [Section Name: Cash Flow Analysis - TEV Exit](#evergreen-section-name-cash-flow-analysis---tev-exit)
17. [Evergreen](#evergreen)
   - [Section Name: Utilization Summary](#evergreen-section-name-utilization-summary)
   - [Section Name: Cost and Revenue Drivers](#evergreen-section-name-cost-and-revenue-drivers)
   - [Section Name: Cost Analysis](#evergreen-section-name-cost-analysis)
   - [Section Name: Chassis Acquisition & Investment Analysis](#evergreen-section-name-chassis-acquisition-&-investment-analysis)
   - [Section Name: Cash Flow Analysis - Depreciated Value Exit](#evergreen-section-name-cash-flow-analysis---depreciated-value-exit)
   - [Section Name: Cash Flow Analysis - TEV Exit](#evergreen-section-name-cash-flow-analysis---tev-exit)
18. [Evergreen](#evergreen)
   - [Section Name: Utilization Summary](#evergreen-section-name-utilization-summary)
   - [Section Name: Cost and Revenue Drivers](#evergreen-section-name-cost-and-revenue-drivers)
   - [Section Name: Per Usage Day Costs & Total Costs](#evergreen-section-name-per-usage-day-costs-&-total-costs)
   - [Section Name: EBITDA and Margin Analysis](#evergreen-section-name-ebitda-and-margin-analysis)
   - [Section Name: Chassis Acquisition & Initial Investment](#evergreen-section-name-chassis-acquisition-&-initial-investment)
   - [Section Name: Cash Flow Analysis - Depreciated Value Exit](#evergreen-section-name-cash-flow-analysis---depreciated-value-exit)
   - [Section Name: Cash Flow Analysis - TEV Exit](#evergreen-section-name-cash-flow-analysis---tev-exit)
19. [(Sheet name is not provided in the JSON. Assuming it's "Sheet1") Sheet1](#(sheet-name-is-not-provided-in-the-json.-assuming-it's-"sheet1")-sheet1)
   - [Support Data Section](#(sheet-name-is-not-provided-in-the-json.-assuming-it's-"sheet1")-sheet1-support-data-section)
20. [(Assumed to be Sheet1 based on common convention, since the JSON doesn't explicitly name the sheet)](#(assumed-to-be-sheet1-based-on-common-convention,-since-the-json-doesn't-explicitly-name-the-sheet))
   - [Chassis On-Street Analysis](#(assumed-to-be-sheet1-based-on-common-convention,-since-the-json-doesn't-explicitly-name-the-sheet)-chassis-on-street-analysis)
21. [(Assumed to be the default "Sheet1" since the JSON doesn't specify)](#(assumed-to-be-the-default-"sheet1"-since-the-json-doesn't-specify))
   - [Chassis Valuation Analysis](#(assumed-to-be-the-default-"sheet1"-since-the-json-doesn't-specify)-chassis-valuation-analysis)
   - [Chassis Age Distribution](#(assumed-to-be-the-default-"sheet1"-since-the-json-doesn't-specify)-chassis-age-distribution)
22. [(Assumed to be "Sheet1" as the JSON doesn't explicitly name it)](#(assumed-to-be-"sheet1"-as-the-json-doesn't-explicitly-name-it))
   - [Chassis Requirement Analysis](#(assumed-to-be-"sheet1"-as-the-json-doesn't-explicitly-name-it)-chassis-requirement-analysis)

---


====================================================================================================
# SHEET 1: (Sheet name is not provided in the JSON. Assuming "Assumptions")
====================================================================================================

## 1. **Sheet Name**: (Sheet name is not provided in the JSON. Assuming "Assumptions")

### Utilization & Purchase Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the key assumptions used in the financial model, including utilization rates, purchase/lease costs, and operating expenses. It allows users to adjust these assumptions to see the impact on the overall financial results.
- **Cell Range**: B5:F14
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C6:C14, E6:E14
- **Time Series Details**: None. This section contains static assumptions.
- **Key Components**: Total EVG Chassis Purchased, Total EVG Chassis Leased, Total EVG Chassis for Scrap, Total EVG Leases, Total Excess Chassis Leased, Total DCLI Backfill, EVG Average Daily Usage, EVG Utilization Rate, Total Chassis Required for EVG Use.
- **Notes & Customizations**: Includes assumptions for different leasing scenarios (DCLI leases vs. purchases).

### Purchase/Lease Cost Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the cost assumptions related to purchasing and leasing chassis, including book value, premiums/discounts, and lease costs.
- **Cell Range**: B16:C24
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C17:C24
- **Time Series Details**: None. This section contains static assumptions.
- **Key Components**: Average Book Value per Chassis, Premium / (Discount) to Book (Upfront), Premium / (Discount) to Book (PO), Purchase Price, Lease Cost per Day for EVG Chassis, Lease Cost per Day for EVG Leases, Lease Cost per Day for Add. Capacity.
- **Notes & Customizations**: Includes assumptions for both upfront and purchase order (PO) premiums/discounts.

### Upfront Investment Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the upfront investment costs associated with the chassis, including repositioning, decoupling, reconditioning, retitling, stenciling, and offhire costs.
- **Cell Range**: B26:C43, E34:F34
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C27:C43, E34:E34
- **Time Series Details**: None. This section contains static assumptions.
- **Key Components**: Repositioning, # of Chassis w/ Repositioning, Decouping Costs, Chassis to be Decouped, Reconditioning Costs, # of Chassis Requiring Reconditioning, Retitling Costs, Chassis to be Retitled, Stenciling Costs, Chassis to be Stenciled, Offhire Costs, Chassis to be Offhired.
- **Notes & Customizations**: Includes a toggle for reconditioning costs (on/off).

### Operating Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the operating assumptions used in the model, including terminal percentages, billing thresholds, and cost assumptions for M&R, Admin, Repo, and Other expenses.
- **Cell Range**: B45:I51, B53:C60
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E50:H50
    - **Data Range**: C45:C49, F51, C53:C60, G51:H51
- **Time Series Details**: None. This section contains static assumptions.
- **Key Components**: Sales Tax, Terminal % Assumption Placeholder, Terminal Billing Threshold, Cost Assumptions (M&R, Admin, Repo, Other), PSW MH Rate, EVG CH Rate, Terminal Rate, MH Annual Conversion %, Gain Sharing % on Conversion, Bad Debt (as % of Revenue).
- **Notes & Customizations**: Cost assumptions are referenced as being provided by operations.



====================================================================================================
# SHEET 2: Summary
====================================================================================================

## 1. **Sheet Name**: Summary

### Transaction Overview
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the key assumptions and costs associated with the chassis transaction, including purchase price, reconditioning costs, and working capital investment. It provides a summary of the total transaction cost.
- **Cell Range**: B6:F17
- **Layout Structure**:
    - **Row Headers Location**: B7:B17
    - **Column Headers Location**: D4 (Yr. 1 PF), F3 (Total)
    - **Data Range**: D7:F17
- **Time Series Details**:
    - **Date Range**: Year 1 Projected, Total
    - **Frequency**: Single Period
- **Key Components**: Purchase Price/Chassis, Reconditioning Costs, Working Capital Investment, Total Transaction Cost
- **Notes & Customizations**: Includes costs and savings related to reconditioning, decoupling, repositioning, and retitling.

### Chassis Fleet Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of the chassis fleet, including the number of chassis acquired, retained, and scrapped.
- **Cell Range**: B19:F23
- **Layout Structure**:
    - **Row Headers Location**: B20:B22
    - **Column Headers Location**: D4 (Yr. 1 PF), F3 (Total)
    - **Data Range**: D21:F23
- **Time Series Details**:
    - **Date Range**: Year 1 Projected, Total
    - **Frequency**: Single Period
- **Key Components**: Chassis Acquired, Retained, Scrapped
- **Notes & Customizations**: Includes formatting for negative numbers.

### EVG Pooled Chassis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the chassis usage and availability for EVG, including chassis decoupled, used for FFU, and any surplus or shortage.
- **Cell Range**: B25:F31
- **Layout Structure**:
    - **Row Headers Location**: B26:B31
    - **Column Headers Location**: D4 (Yr. 1 PF), F3 (Total)
    - **Data Range**: D26:F31
- **Time Series Details**:
    - **Date Range**: Year 1 Projected, Total
    - **Frequency**: Single Period
- **Key Components**: Chassis Decouped at Close, Chassis to be Used for EVG FFU, Surplus (Shortage) of Chassis, DCLI Chassis Backfill
- **Notes & Customizations**: Includes DCLI chassis backfill information.

### Usage Agreement
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the chassis contribution and usage per day, providing insights into utilization rates.
- **Cell Range**: B33:F43
- **Layout Structure**:
    - **Row Headers Location**: B34:B43
    - **Column Headers Location**: D4 (Yr. 1 PF), F3 (Total)
    - **Data Range**: D34:F43
- **Time Series Details**:
    - **Date Range**: Year 1 Projected, Total
    - **Frequency**: Single Period
- **Key Components**: Chassis Contributed per Day, Chassis Used per Day, Total Utilization (Chassis per Day), Total Utilization (%), Street Utilization (%), MH % of Street
- **Notes & Customizations**: Includes utilization percentages and breakdowns.

### Utilization Percentages
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the breakdown of utilization percentages across different categories (MH, CH, Terminal, Net Lease).
- **Cell Range**: B45:D47
- **Layout Structure**:
    - **Row Headers Location**: B46:B47
    - **Column Headers Location**: D4 (Yr. 1 PF)
    - **Data Range**: D46:D47
- **Time Series Details**:
    - **Date Range**: Year 1 Projected
    - **Frequency**: Single Period
- **Key Components**: MH%, CH%, Terminal %
- **Notes & Customizations**: Shows the percentage breakdown of utilization.

### Rates (2014)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the rates for MH and CH in 2014.
- **Cell Range**: B50:D53
- **Layout Structure**:
    - **Row Headers Location**: B51:B52
    - **Column Headers Location**: D4 (Yr. 1 PF)
    - **Data Range**: D51:D53
- **Time Series Details**:
    - **Date Range**: 2014
    - **Frequency**: Single Period
- **Key Components**: MH, CH
- **Notes & Customizations**: Shows the rates for different chassis types.

### Cost Summary (per Usage Day) - 2014
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the costs per usage day for various categories such as M&R, repositioning, and storage.
- **Cell Range**: B55:F69
- **Layout Structure**:
    - **Row Headers Location**: B57:B69
    - **Column Headers Location**: D4 (Yr. 1 PF), F3 (Total)
    - **Data Range**: D57:F69
- **Time Series Details**:
    - **Date Range**: 2014
    - **Frequency**: Single Period
- **Key Components**: Usage Days, $ M&R, $ Repositioning, $ Storage, $ Overhead, M&R, Admin, Repo, Storage, Lease Expense, Revenue Sharing, Other
- **Notes & Customizations**: Includes costs related to M&R, repositioning, storage, overhead, lease expense, and revenue sharing.

### Summary (2014E)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of contributed days, revenue, expense, and EBITDA for 2014E.
- **Cell Range**: B71:F86
- **Layout Structure**:
    - **Row Headers Location**: B73:B86
    - **Column Headers Location**: D4 (Yr. 1 PF), F3 (Total)
    - **Data Range**: D73:F86
- **Time Series Details**:
    - **Date Range**: 2014E
    - **Frequency**: Single Period
- **Key Components**: Contributed Days, Revenue (2014E), Expense (2014E), EBITDA (2014E), EBITDA Margin (2014E), EBITDA per Usage Day (2014E), EBITDA per Contributed Day (2014E), Depreciated Value 10-year Unlevered IRR, TEV 10x Exit Multiple Unlevered IRR, NPV - 10-year, Total Investment (incl. WC), Purchase Multiple1
- **Notes & Customizations**: Includes key financial metrics and IRR calculations.



====================================================================================================
# SHEET 3: Evergreen Model Assumptions
====================================================================================================

## 1. **Sheet Name**: Evergreen Model Assumptions

### Section Name: Evergreen Model Assumptions - Region Specific Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains key assumptions and data points related to Evergreen chassis, broken down by region. It includes information on chassis ownership, leasing, scrap, purchase, usage, and various cost factors. This data is used to model the financial impact of Evergreen chassis on DCLI's operations.
- **Cell Range**: A1:AF20
- **Layout Structure**:
    - **Row Headers Location**: Column A (A10:A20) lists the regions.
    - **Column Headers Location**: Row 8 (B8:AF8) describes the data points for each region.
    - **Data Range**:
      - Numeric data: C10:AF20
- **Time Series Details**:
    - There is no explicit time series in this section. The data appears to represent a single snapshot in time or a static set of assumptions.
- **Key Components**:
    - Regions (MW, PNW, GUL, SE, etc.)
    - Total EVG Owned Chassis
    - Total EVG Leased Chassis
    - Total EVG Chassis for Scrap
    - Chassis Purchased by DCLI
    - EVG Average Daily Usage
    - EVG Utilization Rate
    - Average Book Value per Chassis
    - Purchase Price
    - Cost to Lease Owned EVG Chassis
    - Cost to Takeover EVG Existing Leases
    - Lease Cost per Day for Add. Capacity
    - Repo Cost per Chassis
    - Recon. Cost per Chassis
    - Decouping Cost per Chassis
    - Retitling & Stenciling Cost per Chassis
    - Offhire Cost per Chassis
    - Sales Tax
    - Terminal % of Daily Usage
    - M&R per Billed Day
    - Repo per Billed Day
    - Admin per Chassis per Day
    - Terminal Rate
    - Market MH Rate
    - MH Conversion per Year
    - Gain Sharing % on MH Transition
- **Notes & Customizations**: The section includes notes indicating the data sources and estimations used (B25:B28). The "Purhcase (1) / Lease (0)" field in B4/C4 allows for switching between purchase and lease scenarios.



====================================================================================================
# SHEET 4: (Sheet name is not provided in the JSON, assuming it's "Sheet1")
====================================================================================================

## 1. **Sheet Name**: (Sheet name is not provided in the JSON, assuming it's "Sheet1")

### Fleet Summary and Investment Overview
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of the current fleet, usage and fleet sizing, and an investment overview for Evergreen Nationwide. It includes key assumptions, financial returns, and sensitivity analysis.
- **Cell Range**: C5:Q32
- **Layout Structure**:
    - **Row Headers Location**: Column C and N
    - **Column Headers Location**: Row 6
    - **Data Range**:
      - Numeric values and formulas are scattered throughout the range, including D7:D11, G7:G12, P7:P16, etc.
- **Time Series Details**:
    - **Date Range**: Year 1 (P19)
    - **Frequency**: Annual
- **Key Components**: Current EVG Fleet (Owned, Leased, Scrapped), Fleet Required, Cost per Usage Day, Investment Overview (Assets, Repositioning, Working Capital, Reconditioning), Financial Returns (CH Revenue, MH Revenue, Total Revenue, Adj. EBITDA, NPV).
- **Notes & Customizations**: Includes commentary/assumptions for various investment components.

### Sensitivity Analysis
- **Section Type**: Sensitivity Analysis Table
- **Description & Purpose**: This section presents a sensitivity analysis of the model, showing how different input parameters affect key output metrics.
- **Cell Range**: C34:R42
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 36
    - **Data Range**: D38:R41
- **Time Series Details**:
    - None explicitly defined, but the analysis is based on a single point in time or an average across the investment horizon.
- **Key Components**: Scenario, Lease Cost per Day to EVG, Average Prem/(Disc) per Chassis, Terminal Rate, MH Conversion, Total Investment, Investment Multiple, Purchase Price per Chassis, Average EBITDA, Average EBITDA Margin %, 10 year depreciated value IRR %, 5x EBITDA exit multiple IRR %, NPV.
- **Notes & Customizations**: Includes notes on the model inputs and outputs.

### Rate Sensitivity
- **Section Type**: Sensitivity Analysis Table
- **Description & Purpose**: This section presents a sensitivity analysis of the CH and Terminal rates.
- **Cell Range**: C46:H59
- **Layout Structure**:
    - **Row Headers Location**: Column E
    - **Column Headers Location**: Row 46, 55
    - **Data Range**: D47:E54, F56:H59
- **Time Series Details**:
    - None explicitly defined, but the analysis is based on a single point in time or an average across the investment horizon.
- **Key Components**: % MH, CH Rate, Change in Rate, Purchase Price Per Chassis, CH Rate per day, Terminal Rate per day.
- **Notes & Customizations**: Includes different options for the rates.



====================================================================================================
# SHEET 5: Evergreen
====================================================================================================

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



====================================================================================================
# SHEET 6: Evergreen
====================================================================================================

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



====================================================================================================
# SHEET 7: (Sheet name not provided in JSON, assuming "Sheet1")
====================================================================================================

## 1. **Sheet Name**: (Sheet name not provided in JSON, assuming "Sheet1")

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of utilization metrics, including percentages of street and terminal usage, and overall utilization rates. This section provides a high-level overview of asset utilization.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implicitly, based on data structure)
    - **Data Range**: G6:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (based on `ds_1` referenced in `G21:Q21`)
    - **Frequency**: Annual
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate
- **Notes & Customizations**: Includes percentage calculations based on street and terminal usage.

### Section Name: Cost and Revenue Drivers
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the key cost and revenue drivers, including M&R, Admin, and Repo costs, as well as usage days and contribution days. This section provides insight into the factors influencing profitability.
- **Cell Range**: B16:Q19
- **Layout Structure**:
    - **Row Headers Location**: B17:C19
    - **Column Headers Location**: H16:Q16 (Implicitly, based on data structure)
    - **Data Range**: E17:Q19
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (based on `ds_1` referenced in `G21:Q21`)
    - **Frequency**: Annual
- **Key Components**: EVG, Per Usage Day, Per Contr. Day, M&R, Admin, Repo, Usage Days, Contr. Days
- **Notes & Customizations**: Includes costs per usage and contribution day.

### Section Name: Revenue Projections
- **Section Type**: Custom P&L (Revenue Section)
- **Description & Purpose**: Projects revenue based on various factors such as chassis usage, rental rates, and inflation assumptions. This section is crucial for forecasting future income.
- **Cell Range**: B21:Q46
- **Layout Structure**:
    - **Row Headers Location**: B23:C43
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**: H23:Q43
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Usage, Street Utilization
- **Notes & Customizations**: Includes annual inflation assumptions for various rates and costs.

### Section Name: Revenue Summary
- **Section Type**: Custom P&L (Revenue Summary)
- **Description & Purpose**: Summarizes the revenue projections, including total revenue and average costs per usage day. This section provides a consolidated view of revenue performance.
- **Cell Range**: B45:Q54
- **Layout Structure**:
    - **Row Headers Location**: B45:B54
    - **Column Headers Location**: H46:Q46 (Years)
    - **Data Range**: H46:Q54
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, EVG Average Cost per EVG Usage Day, EVG Average Cost per EVG Street Day, EVG Terminal Cost per Terminal Day
- **Notes & Customizations**: Includes calculations for average costs per usage day.

### Section Name: Cost Projections
- **Section Type**: Custom P&L (Cost Section)
- **Description & Purpose**: Projects costs based on per-usage-day costs, lease costs, and other expenses. This section is critical for forecasting future expenses.
- **Cell Range**: B56:Q74
- **Layout Structure**:
    - **Row Headers Location**: B56:C73
    - **Column Headers Location**: H57:Q57 (Years)
    - **Data Range**: H57:Q74
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Per Usage Day Costs, M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Other Cost per Day, Lease Cost per Day on EVG Chassis, Lease Cost per Day on EVG Leases, Incremental Pool Overuse Cost per Day, M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Lease Cost on EVG Owned Chassis, Lease Cost on EVG Existing Leases, Lease Cost for Additional Capactiy, Gain Sharing with EVG on MH Conversion, Total Cost
- **Notes & Customizations**: Includes various lease cost components and gain sharing arrangements.

### Section Name: EBITDA Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes EBITDA, including EBITDA per usage day and EBITDA margin. This section provides key profitability metrics.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76:C78
    - **Column Headers Location**: H77:Q77 (Years)
    - **Data Range**: H77:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%)
- **Notes & Customizations**: Includes EBITDA margin calculation.

### Section Name: Initial Investment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the initial investment required, including chassis acquisition costs, reconditioning costs, and working capital investment. This section provides a summary of upfront costs.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98
    - **Column Headers Location**: G82 (Single Column)
    - **Data Range**: G83:G98
- **Time Series Details**:
    - **Date Range**: Not Time Series
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Premium / (Discount) to Book, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Less: Scrap Chassis at $1,000 per Chassis, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned
- **Notes & Customizations**: Includes calculations for total effective purchase price and cash multiple of EBITDA.

### Section Name: Cash Flows - Depreciated Value Exit
- **Section Type**: Cash Flow Projection
- **Description & Purpose**: Projects cash flows based on a depreciated value exit strategy. This section is used to estimate the return on investment.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B117, F118
    - **Column Headers Location**: G104:Q104 (Years)
    - **Data Range**: H108:Q117, E119
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV
- **Notes & Customizations**: Includes calculations for unlevered IRR and NPV.

### Section Name: Cash Flows - TEV Exit
- **Section Type**: Cash Flow Projection
- **Description & Purpose**: Projects cash flows based on a Total Enterprise Value (TEV) exit strategy. This section is used to estimate the return on investment under a different exit scenario.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B134, F118
    - **Column Headers Location**: G121:L121 (Years)
    - **Data Range**: H125:L134, E136
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV
- **Notes & Customizations**: Includes calculations for unlevered IRR and NPV.


====================================================================================================
# SHEET 8: Evergreen
====================================================================================================

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



====================================================================================================
# SHEET 9: Sheet1
====================================================================================================

## 1. **Sheet Name**: Sheet1

### Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of utilization metrics for different categories (Street - MH, Street - EVG, Terminal, Grand Total) and their respective percentages. It helps to understand the efficiency of chassis usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied "Year 0" to "Year 10" from date series)
    - **Data Range**:
      - Annual data: G7:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on different categories.

### Cost Breakdown (EVG)
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: Breaks down the costs associated with EVG (Evergreen) operations, including M&R, Admin, and Repo costs, both in total and per usage day/contributed day.
- **Cell Range**: B16:Q19
- **Layout Structure**:
    - **Row Headers Location**: B17:C19
    - **Column Headers Location**: H16:Q16 (Implied "Year 0" to "Year 10" from date series)
    - **Data Range**:
      - Annual data: E17:Q19
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: M&R, Admin, Repo, Per Usage Day, Per Contr. Day.
- **Notes & Customizations**: The table shows both total costs and costs per usage/contributed day.

### Chassis Usage and Revenue Forecast
- **Section Type**: Revenue and Usage Forecast
- **Description & Purpose**: Forecasts chassis usage, rates, and revenue for different segments (Trucker Street, EVG Street, Terminal) over a 10-year period. Also includes inflation assumptions.
- **Cell Range**: B21:Q46
- **Layout Structure**:
    - **Row Headers Location**: B23:C43
    - **Column Headers Location**: G21:Q21 (Year 0 to Year 10)
    - **Data Range**:
      - Annual data: H23:Q43
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Usage, Street Utilization, Revenue.
- **Notes & Customizations**: Includes annual inflation assumptions for various rates and costs.

### Cost Analysis per Usage Day
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: Analyzes costs per usage day for various expense categories.
- **Cell Range**: B45:Q63
- **Layout Structure**:
    - **Row Headers Location**: B45:C63
    - **Column Headers Location**: H46:Q46 (Implied "Year 0" to "Year 10" from date series)
    - **Data Range**:
      - Annual data: H46:Q63
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, EVG Average Cost per EVG Usage Day, Per Usage Day Costs, M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Other Cost per Day, Lease Cost per Day on EVG Chassis, Lease Cost per Day on EVG Leases, Incremental Pool Overuse Cost per Day.
- **Notes & Customizations**: Includes calculations for average costs per usage day.

### Expense Forecast
- **Section Type**: Expense Forecast
- **Description & Purpose**: Forecasts various expenses including M&R, Admin, Repo, Other, Bad Debt, and Lease Costs.
- **Cell Range**: B65:Q74
- **Layout Structure**:
    - **Row Headers Location**: B65:B74
    - **Column Headers Location**: H66:Q66 (Implied "Year 0" to "Year 10" from date series)
    - **Data Range**:
      - Annual data: H65:Q74
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Lease Cost on EVG Owned Chassis, Lease Cost on EVG Existing Leases, Lease Cost for Additional Capactiy, Gain Sharing with EVG on MH Conversion, Total Cost.
- **Notes & Customizations**: Includes different types of lease costs.

### EBITDA and Margin Analysis
- **Section Type**: Profitability Analysis
- **Description & Purpose**: Calculates EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, and EBITDA Margin.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76:C79
    - **Column Headers Location**: H77:Q77 (Implied "Year 0" to "Year 10" from date series)
    - **Data Range**:
      - Annual data: H77:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes calculations for EBITDA per usage day and per chassis per day.

### Chassis Acquisition Costs
- **Section Type**: Investment Analysis
- **Description & Purpose**: Calculates the total cost of acquiring chassis, including purchase price, reconditioning costs, and other related expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98
    - **Column Headers Location**: G82 (Single Column)
    - **Data Range**:
      - Annual data: G83:G98
- **Time Series Details**:
    - **Date Range**: Not time series, but related to upfront investment.
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Less: Scrap Chassis, Transaction Expenses, Total Effective Purchase Price.
- **Notes & Customizations**: Includes various costs associated with chassis acquisition.

### Cash Flow Analysis - Depreciated Value Exit
- **Section Type**: Cash Flow Projection
- **Description & Purpose**: Projects cash flows based on a depreciated value exit scenario.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Year 0 to Year 10)
    - **Data Range**:
      - Annual data: H108:Q117
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for Unlevered IRR and NPV.

### Cash Flow Analysis - TEV Exit
- **Section Type**: Cash Flow Projection
- **Description & Purpose**: Projects cash flows based on a Total Enterprise Value (TEV) exit scenario.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Year 0 to Year 5)
    - **Data Range**:
      - Annual data: H125:L134
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes @, Cash Income, WC Investment @, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes calculations for Unlevered IRR.


====================================================================================================
# SHEET 10: Evergreen
====================================================================================================

## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization rates and related metrics for different categories (Street - MH, Street - EVG, Terminal, Grand Total). It provides a high-level overview of asset usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H10:Q10, G11:Q11, H12:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on different categories.

### Section Name: EVG Cost Analysis
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: This section analyzes the costs associated with EVG operations, breaking them down by M&R, Admin, and Repo. It also includes calculations for per-usage-day costs.
- **Cell Range**: B16:Q19
- **Layout Structure**:
    - **Row Headers Location**: B17:B19, C18:C19
    - **Column Headers Location**: H16:Q16 (Usage Days, Contr. Days) and G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H17:I17
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG, M&R, Admin, Repo, Usage Days, Contr. Days, Per Usage Day, Per Contr. Day.
- **Notes & Customizations**: Includes cost breakdowns and per-day calculations.

### Section Name: Revenue and Usage Days Forecast
- **Section Type**: Revenue and Usage Forecast
- **Description & Purpose**: This section forecasts revenue based on usage days, rates, and inflation assumptions for Trucker Street, EVG Street, and Terminal operations.
- **Cell Range**: B21:Q46
- **Layout Structure**:
    - **Row Headers Location**: B23:B41, C24:C43
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H23:Q23, H24:Q26, H28:Q28, I29:Q29, H30:Q30, H32:Q32, H33, H34, H36:Q36, H37, H38, H40:Q41, H42:Q43, H45:Q45, H46:Q46
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Revenue.
- **Notes & Customizations**: Includes annual inflation assumptions for various rates and costs.

### Section Name: Cost per Usage Day Analysis
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: This section analyzes the cost per usage day for EVG Street and Terminal operations, including M&R, Admin, Repo, and other costs.
- **Cell Range**: B48:Q63
- **Layout Structure**:
    - **Row Headers Location**: B48:B54, C57:C63
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H48:Q49, H50:Q51, H52:Q54, H57:Q57, H58:Q60, I61:Q63
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, EVG Average Cost per EVG Usage Day, M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Lease Cost per Day.
- **Notes & Customizations**: Includes calculations for average costs per usage day.

### Section Name: Expense Forecast
- **Section Type**: Expense Forecast
- **Description & Purpose**: This section forecasts various expenses, including M&R, Admin, Repo, Other, Bad Debt, and Lease Costs.
- **Cell Range**: B65:Q74
- **Layout Structure**:
    - **Row Headers Location**: B65:B74
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H65:Q65, H66:Q68, H69:Q69, H70:Q73, H74:Q74
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Lease Cost, Total Cost.
- **Notes & Customizations**: Includes different types of lease costs and gain sharing.

### Section Name: EBITDA Analysis
- **Section Type**: Profitability Analysis
- **Description & Purpose**: This section calculates EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, and EBITDA Margin.
- **Cell Range**: B76:Q79
- **Layout Structure**:
    - **Row Headers Location**: B76:B79, C77:C78
    - **Column Headers Location**: G21:Q21 (Years)
    - **Data Range**:
      - Annual data: H77:Q78, H79:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes profitability metrics.

### Section Name: Chassis Acquisition Costs
- **Section Type**: Investment Analysis
- **Description & Purpose**: This section details the costs associated with acquiring chassis, including the price per chassis, reconditioning costs, and other related expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B98, B100
    - **Column Headers Location**: None (Single Column)
    - **Data Range**: G83, G84, G85, G86, G87, G88, G89, G90, G91, G92, G93, G94, G95, G96, G97, G98, G100
- **Time Series Details**: None (Upfront Costs)
- **Key Components**: Chassis to be Acquired, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Scrap Chassis, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: Includes a breakdown of various acquisition-related costs.

### Section Name: Cash Flows - Depreciated Value Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit scenario.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Years)
    - **Data Range**:
      - Annual data: H108:Q108, H109:Q109, H110:Q110, H111:Q114, H115:Q115, G117:Q117
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for IRR and NPV.

### Section Name: Cash Flows - TEV Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit scenario.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B121:B136
    - **Column Headers Location**: G121:L121 (Years)
    - **Data Range**:
      - Annual data: H125:L125, H126:L126, H127:L127, H128:L131, H132:L132, G134:L134
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes calculations for IRR and NPV.



====================================================================================================
# SHEET 11: (Assumed Sheet1, as the JSON doesn't explicitly name the sheet)
====================================================================================================

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



====================================================================================================
# SHEET 12: Evergreen
====================================================================================================

## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of utilization metrics, including percentages of street and terminal usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied Years based on later time series)
    - **Data Range**: G6:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (based on `date_series_definitions` and G21:Q21)
    - **Frequency**: Annual
- **Key Components**: Street - MH, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on street and terminal usage.

### Section Name: Cost and Revenue Drivers
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the key drivers of cost and revenue, including rates, usage days, and resulting revenue/costs.
- **Cell Range**: B16:Q46
- **Layout Structure**:
    - **Row Headers Location**: B17:C43
    - **Column Headers Location**: H16:Q16, G21:Q21 (Years)
    - **Data Range**: E17:Q46
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: M&R, Admin, Repo costs, Usage Days, Trucker Street Usage Days, EVG Street Rental Days, Terminal Usage Days, Total Usage Days, Revenue.
- **Notes & Customizations**: Includes annual inflation assumptions in U32:V41.

### Section Name: Revenue and Cost Analysis
- **Section Type**: Standard P&L (Partial)
- **Description & Purpose**: Analyzes revenue, costs, and profitability metrics.
- **Cell Range**: B45:Q79
- **Layout Structure**:
    - **Row Headers Location**: B45:C79
    - **Column Headers Location**: H46:Q46, G21:Q21 (Years)
    - **Data Range**: H46:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G21:Q21)
    - **Frequency**: Annual
- **Key Components**: Revenue, EVG Street Costs, Terminal Billings, M&R Cost, Admin Expense, Repo Expense, Total Cost, EBITDA, EBITDA Margin (%).
- **Notes & Customizations**: Includes per usage day costs and profitability metrics. Contains a repeating annual series from 2080 to 2080 in H71:Q71.

### Section Name: Chassis Acquisition
- **Section Type**: Investment Analysis
- **Description & Purpose**: Details the costs associated with chassis acquisition.
- **Cell Range**: B82:G98
- **Layout Structure**:
    - **Row Headers Location**: B83:B98
    - **Column Headers Location**: G82
    - **Data Range**: G83:G98
- **Time Series Details**:
    - **Date Range**: Not applicable (Upfront costs)
    - **Frequency**: Not applicable
- **Key Components**: Chassis to be Acquired, Price per Chassis, Total Chassis Price, Reconditioning Costs, Transaction Expenses, Total Effective Purchase Price.
- **Notes & Customizations**: Calculates the total cost of acquiring chassis, including various related expenses.

### Section Name: Investment Analysis - Depreciated Value Exit
- **Section Type**: Investment Analysis
- **Description & Purpose**: Analyzes cash flows with a depreciated value exit strategy.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Years)
    - **Data Range**: H108:Q117
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10 (G104:Q104)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Calculates IRR and NPV based on projected cash flows and a depreciated value exit.

### Section Name: Investment Analysis - TEV Exit
- **Section Type**: Investment Analysis
- **Description & Purpose**: Analyzes cash flows with a Total Enterprise Value (TEV) exit strategy.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Years)
    - **Data Range**: H125:L134
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5 (G121:L121)
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Calculates IRR based on projected cash flows and a TEV exit.



====================================================================================================
# SHEET 13: (Sheet name is not provided in the JSON, assuming it is "Sheet1")
====================================================================================================

## 1. **Sheet Name**: (Sheet name is not provided in the JSON, assuming it is "Sheet1")

### Section Name: Chassis Purchase Options Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes different options for purchasing chassis, likely for EVG (Electric Vehicle Group) usage. It presents purchase prices, potential MH (Market Housing?) percentages, CH (Chassis Housing?) rates, and terminal rates for each option. The purpose is to compare the financial implications of various chassis acquisition strategies.
- **Cell Range**: B13:G33
- **Layout Structure**:
    - **Row Headers Location**: B14:B33 (e.g., different chassis purchase options)
    - **Column Headers Location**: C13:G13 (Purchase Price per Chassis, Total Purchase Price, MH %, CH Rate, Terminal Rate)
    - **Data Range**:
      - C14:G33 (numeric values and percentages for each option)
- **Time Series Details**:
    - There is no explicit time series in this section. It appears to be a static comparison of different purchase options at a single point in time.
- **Key Components**: Purchase Price per Chassis, Total Purchase Price, MH %, CH Rate, Terminal Rate.
- **Notes & Customizations**: The section includes assumptions (C5:C10) that are critical for understanding the context and limitations of the analysis. The MH and CH abbreviations are not explicitly defined, but context suggests they relate to different types of chassis usage or billing. The formatting suggests that some values may be negative (red formatting).



====================================================================================================
# SHEET 14: Sheet1
====================================================================================================

## 1. **Sheet Name**: Sheet1

### Section Name: Assumptions
- **Section Type**: Assumptions List
- **Description & Purpose**: This section outlines the key assumptions used in the financial model. It provides context for understanding the calculations and projections.
- **Cell Range**: C5:C10
- **Layout Structure**:
    - **Row Headers Location**: C5:C10
    - **Column Headers Location**: None
    - **Data Range**: C5:C10 (text values)
- **Time Series Details**: None
- **Key Components**: Assumptions related to chassis age, EVG usage, MH billing rate, and terminal usage.
- **Notes & Customizations**: Numbered list format.

### Section Name: Input Parameters
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the input parameters used for the financial calculations, such as purchase price, MH percentage, CH rate, and terminal rate.
- **Cell Range**: C13:G33 (inferred from remaining ranges and format_index)
- **Layout Structure**:
    - **Row Headers Location**: B14:B33 (inferred from format_index)
    - **Column Headers Location**: C13:G13
    - **Data Range**: D14:G33 (numeric and text values)
- **Time Series Details**: None
- **Key Components**: Purchase Price per Chassis, Total Purchase Price, MH %, CH Rate, Terminal Rate.
- **Notes & Customizations**: The "Purchase Price per Chassis" and "Total Purchase Price" columns likely contain numeric values, while "MH %", "CH Rate", and "Terminal Rate" could be percentages or rates. The format_index indicates that cells B14:B33 contain values, likely labels for the input parameters.



====================================================================================================
# SHEET 15: Evergreen
====================================================================================================

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



====================================================================================================
# SHEET 16: Evergreen
====================================================================================================

## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the utilization of chassis across different categories (Street - MH, Street - EVG, Terminal, Grand Total) and calculates utilization rates. It provides a high-level overview of how effectively the chassis are being used.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied Year 0 to Year 10 from date_series_definitions)
    - **Data Range**: G6:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations based on the different categories.

### Section Name: Cost and Revenue Assumptions
- **Section Type**: Custom P&L
- **Description & Purpose**: This section projects revenue and costs associated with chassis usage, including M&R, Admin, and Repo costs. It calculates revenue based on usage days and rates, and projects costs based on per-day costs.
- **Cell Range**: B16:Q79
- **Layout Structure**:
    - **Row Headers Location**: B17:B79, C18:C19, C24, C29, C33, C37, C41, C57:C63
    - **Column Headers Location**: G21:Q21 (Year 0 to Year 10)
    - **Data Range**:
      - Annual data: H17:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG, M&R, Admin, Repo, Usage Days, Contr. Days, Chassis Used per Day, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Revenue, EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, Per Usage Day Costs, M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Other Cost per Day, Lease Cost per Day, M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Lease Cost, Total Cost, EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes per-day cost calculations, lease costs, and gain sharing. Contains inflation assumptions in column U.

### Section Name: Purchase Price Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the total effective purchase price for the chassis acquisition, including chassis price, reconditioning costs, decoupling costs, repositioning, retitling & stenciling costs, working capital investment, offhire costs, scrap chassis value, and transaction expenses.
- **Cell Range**: B82:G100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: None (Single Point in Time)
    - **Data Range**: G83:G100
- **Time Series Details**:
    - **Date Range**: N/A
    - **Frequency**: N/A
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Premium / (Discount) to Book, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Less: Scrap Chassis, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: Includes a calculation of the cash multiple of 2014 EBITDA.

### Section Name: Cash Flow Analysis - Depreciated Value Exit
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit scenario. It includes investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, capex, and cash flow. It calculates the unlevered IRR and NPV.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Year 0 to Year 10)
    - **Data Range**: H108:Q117, E111:E113, E119
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for accelerated depreciation and working capital investment.

### Section Name: Cash Flow Analysis - TEV Exit
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit scenario. It includes investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, capex, and cash flow. It calculates the unlevered IRR.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Year 0 to Year 5)
    - **Data Range**: H125:L134, E128, E130, E136
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes an exit multiple calculation.



====================================================================================================
# SHEET 17: Evergreen
====================================================================================================

## 1. **Sheet Name**: Evergreen

### Section Name: Utilization Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of utilization metrics for different categories (Street - MH, Street - EVG, Terminal, Grand Total) and calculates utilization rates. It helps in understanding the efficiency of chassis usage.
- **Cell Range**: C5:Q13
- **Layout Structure**:
    - **Row Headers Location**: C6:C13
    - **Column Headers Location**: G6:Q6 (Implied Year 0 to Year 10 from G21:Q21)
    - **Data Range**: G6:Q13
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Street - MH, Street - EVG, Terminal, Grand Total, % of Street - MH, % of Street - EVG, % of Total - Terminal, Utilization Rate.
- **Notes & Customizations**: Includes percentage calculations and grand totals.

### Section Name: Cost and Revenue Drivers
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the key cost and revenue drivers related to EVG operations, including M&R, Admin, Repo costs, and usage days. It's used to project revenue and costs based on usage and rates.
- **Cell Range**: B16:Q46
- **Layout Structure**:
    - **Row Headers Location**: B17:B46, C18:C43
    - **Column Headers Location**: G21:Q21 (Years 0 to 10)
    - **Data Range**: E17:Q46
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG, M&R, Admin, Repo, Usage Days, Contr. Days, Per Usage Day, Per Contr. Day, Chassis Used per Day, Street - Trucker, Trucker Street Usage Days, Trucker Rate, Trucker Street Revenue, EVG Street Rental Days, EVG Street Rate, EVG Street Revenue, Terminal Usage Days, Terminal Rate, Terminal Revenue, Total Usage Days, Contributed Days, Usage, Street Utilization, Revenue.
- **Notes & Customizations**: Includes annual inflation assumptions for various rates and costs, located in column U.

### Section Name: Cost Analysis
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: This section breaks down costs related to EVG operations, including per-usage-day costs, M&R, Admin, Repo, Lease costs, and total costs. It is used to calculate EBITDA and EBITDA margins.
- **Cell Range**: B48:Q79
- **Layout Structure**:
    - **Row Headers Location**: B48:B79, C57:C63, C77:C78
    - **Column Headers Location**: H21:Q21 (Years 0 to 10)
    - **Data Range**: H46:Q79
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: EVG Street Costs, Terminal Billings, EVG Street Days, Terminal Days, Per Usage Day Costs, M&R Cost per Day, Admin Cost per Day, Repo Cost per Day, Other Cost per Day, Lease Costs, M&R Cost, Admin Expense, Repo Expense, Other Expense, Bad Debt Expense, Total Cost, EBITDA, EBITDA per Usage Day, EBITDA per Chassis per Day, EBITDA Margin (%).
- **Notes & Customizations**: Includes calculations for average costs per usage day and EBITDA margin.

### Section Name: Chassis Acquisition & Investment Analysis
- **Section Type**: Investment Analysis
- **Description & Purpose**: This section analyzes the costs associated with acquiring chassis, including purchase price, reconditioning, decoupling, repositioning, retitling, working capital investment, offhire costs, and scrap chassis. It calculates the total effective purchase price and provides metrics like cash multiple of EBITDA.
- **Cell Range**: B82:Q100
- **Layout Structure**:
    - **Row Headers Location**: B83:B100
    - **Column Headers Location**: G21:Q21 (Years 0 to 10)
    - **Data Range**: G83:Q98
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Chassis to be Acquired, Average Book Value / Owned Chassis, Price per Chassis, Payment to EVG, Sales Tax, Total Chassis Price, Reconditioning Costs, Decouping Costs, Repositioning, Retitling & Stenciling Costs, Working Capital Investment, Offhire Costs, Scrap Chassis, Transaction Expenses, Total Effective Purchase Price, Cash Multiple of 2014 EBITDA - Owned.
- **Notes & Customizations**: Includes calculations for total effective purchase price and cash multiple of EBITDA.

### Section Name: Cash Flow Analysis - Depreciated Value Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a depreciated value exit scenario. It includes investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, Capex, and cash flow. It calculates NPV and Unlevered IRR.
- **Cell Range**: B104:Q119
- **Layout Structure**:
    - **Row Headers Location**: B105:B119
    - **Column Headers Location**: G104:Q104 (Years 0 to 10)
    - **Data Range**: H108:Q117, E111:E119
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 10
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR, NPV.
- **Notes & Customizations**: Includes calculations for NPV and Unlevered IRR.

### Section Name: Cash Flow Analysis - TEV Exit
- **Section Type**: Cash Flow Analysis
- **Description & Purpose**: This section projects cash flows based on a Total Enterprise Value (TEV) exit scenario. It includes investment, accelerated depreciation, EBIT, cash taxes, cash income, WC investment, Capex, and cash flow. It calculates NPV and Unlevered IRR.
- **Cell Range**: B121:L136
- **Layout Structure**:
    - **Row Headers Location**: B122:B136
    - **Column Headers Location**: G121:L121 (Years 0 to 5)
    - **Data Range**: H125:L134, E128:E136
- **Time Series Details**:
    - **Date Range**: Year 0 to Year 5
    - **Frequency**: Annual
- **Key Components**: Investment, Accelerated Depreciation, EBIT, Cash Taxes, Cash Income, WC Investment, Capex, Cash Flow, Total Cash Flows, Unlevered IRR.
- **Notes & Customizations**: Includes calculations for NPV and Unlevered IRR.



====================================================================================================
# SHEET 18: Evergreen
====================================================================================================

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



====================================================================================================
# SHEET 19: (Sheet name is not provided in the JSON. Assuming it's "Sheet1") Sheet1
====================================================================================================

## 1. **Sheet Name**: (Sheet name is not provided in the JSON. Assuming it's "Sheet1") Sheet1

### Support Data Section
- **Section Type**: `Support Data`
- **Description & Purpose**: This section likely contains supporting data or metadata for the spreadsheet. The "-->" suggests that more data is located to the right. Without further information, it's impossible to determine the exact purpose.
- **Cell Range**: `A1:ZZ1000` (Assuming the section extends to the right and down, since only A1 is specified. A more precise range would require more data.)
- **Layout Structure**:
    - **Row Headers Location**: Not specified in the provided data.
    - **Column Headers Location**: Not specified in the provided data.
    - **Data Range**: Not specified in the provided data.
- **Time Series Details**:
    - No time series data detected.
- **Key Components**: Not specified in the provided data.
- **Notes & Customizations**: The data is incomplete. More data is needed to determine the full scope and purpose of this section. The "-->" suggests that the data continues to the right.



====================================================================================================
# SHEET 20: (Assumed to be Sheet1 based on common convention, since the JSON doesn't explicitly name the sheet)
====================================================================================================

## 1. **Sheet Name**: (Assumed to be Sheet1 based on common convention, since the JSON doesn't explicitly name the sheet)

### Chassis On-Street Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the number of chassis on the street (i.e., in use) by various steamship lines and aggregates them to calculate total chassis on the street and utilization rates. It provides insights into chassis usage and fleet management.
- **Cell Range**: C2:F57
- **Layout Structure**:
    - **Row Headers Location**: Column C (C4:C54)
    - **Column Headers Location**: Row 3 (E3:F3)
    - **Data Range**: E4:F54
- **Time Series Details**:
    - **Date Range**: 2015-03-07 to 2015-03-14
    - **Frequency**: Weekly
- **Key Components**:
    - Chassis counts for various steamship lines (Horizon Lines, Hamburg Sud, Maersk, MSC, etc.)
    - Total Chassis on the Street
    - Pool of Pools Fleet
    - Total Street Utilization
    - DCLP/GACP Fleet and Utilization
- **Notes & Customizations**:
    - The data reflects chassis with a gated-out status by steamship line.
    - DCSZ is used as the steamship SCAC when the chassis gates out bare with no container.
    - There are some italicized values in the data range.



====================================================================================================
# SHEET 21: (Assumed to be the default "Sheet1" since the JSON doesn't specify)
====================================================================================================

## 1. **Sheet Name**: (Assumed to be the default "Sheet1" since the JSON doesn't specify)

### Chassis Valuation Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates and displays the depreciated value of chassis assets based on their age and purchase price. It provides insights into the current book value and projected depreciated value after a specified number of years.
- **Cell Range**: B5:M13
- **Layout Structure**:
    - **Row Headers Location**: B5:B8, B10:B13
    - **Column Headers Location**: B11:M11
    - **Data Range**:
      - C5:C7 (Value New, Residual Value, Useful Life)
      - D10, D12:D13 (ASI/CSG, Age)
      - E12:F13 (Count, % of Total)
      - G12:I13 (Book Value Per, Purchase Per, Total Purchase)
      - K12:M13 (Age 10 years Later, Depreciated 10 year value per, Depreciated 10 year value total)
- **Time Series Details**:
    - **Date Range**: Not explicitly a time series, but "Age" in D11 and K11 implies a time-dependent calculation. The "10 Years Later" in K11 suggests a single point in the future relative to the "Age" in D11.
    - **Frequency**: N/A
- **Key Components**: Value New, Residual Value, Useful Life, Age, Count, % of Total, Book Value Per, Purchase Per, Total Purchase, Depreciated 10 year value per, Depreciated 10 year value total.
- **Notes & Customizations**: The calculation projects the depreciated value 10 years into the future. The formatting of the "Value New" and "Residual Value" fields (C5, C6) is distinct, indicating potential emphasis or a specific data source.

### Chassis Age Distribution
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the distribution of chassis by age.
- **Cell Range**: B16:C38
- **Layout Structure**:
    - **Row Headers Location**: B16, B18:B38
    - **Column Headers Location**: B18, C18
    - **Data Range**:
      - C19:C38
- **Time Series Details**:
    - **Date Range**: B20:B38 contains age in "Years", implying a time series. The specific years are not provided in the JSON extract.
    - **Frequency**: Annual
- **Key Components**: Age, Book Value
- **Notes & Customizations**: The values in column B are formatted as "# \"Years\"", indicating the age of the chassis.



====================================================================================================
# SHEET 22: (Assumed to be "Sheet1" as the JSON doesn't explicitly name it)
====================================================================================================

## 1. **Sheet Name**: (Assumed to be "Sheet1" as the JSON doesn't explicitly name it)

### Chassis Requirement Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates and displays the chassis requirements for Evergreen PSW LSA/LGB operations under different stress levels (85% and 95%). It uses gate-out data, dwell times, and days in the period to determine the number of chassis needed on the street and in the terminal.
- **Cell Range**: A1:D13
- **Layout Structure**:
    - **Row Headers Location**: Column A (A3:A12)
    - **Column Headers Location**: Row 2 (B2:C2)
    - **Data Range**:
      - B3:C10 (numeric values related to chassis requirements at 85% and 95% stress)
      - D11 (chassis required for terminal)
      - B12:D12 (chassis required for Evergreen)
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the provided data, but the notes mention "April, May, June 2015" for dwell analysis. This suggests a potential, but limited, time series context.
    - **Frequency**: Not applicable, as the primary focus is on a static calculation based on period data, not a time series.
- **Key Components**: gate-outs in period, dwell, chassis on the street in period, days in period, chassis on street, chassis required for street, percentage of terminal chassis, chassis required for terminal, chassis required for Evergreen.
- **Notes & Customizations**: The analysis considers out-of-service (OOS) chassis and uses a data source of CMS-PC and Evergreen statement of 36k gate moves at Seaside per month. Dwell times are based on analysis of April, May, and June 2015 data.

