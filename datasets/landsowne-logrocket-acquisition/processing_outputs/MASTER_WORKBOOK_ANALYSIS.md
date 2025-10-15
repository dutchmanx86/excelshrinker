# Master Workbook Analysis

This document provides a comprehensive analysis of all sheets in the Excel workbook.

---

## Table of Contents

1. [Merger Model](#merger-model)
   - [Section Name: Assumptions & Purchase Price Overview](#merger-model-section-name-assumptions-&-purchase-price-overview)
   - [Section Name: Consideration Schedule](#merger-model-section-name-consideration-schedule)
   - [Section Name: Sources and Uses](#merger-model-section-name-sources-and-uses)
   - [Section Name: Financial Summary (ARR)](#merger-model-section-name-financial-summary-arr)
   - [Section Name: GAAP P&L](#merger-model-section-name-gaap-p&l)
   - [Section Name: Key Metrics](#merger-model-section-name-key-metrics)
   - [Section Name: Cash Burn](#merger-model-section-name-cash-burn)
   - [Section Name: Valuation & Shares Outstanding](#merger-model-section-name-valuation-&-shares-outstanding)
   - [Section Name: PF Share Price Accretion / Dilution to Standalone](#merger-model-section-name-pf-share-price-accretion--dilution-to-standalone)
   - [Section Name: Customer Counts](#merger-model-section-name-customer-counts)
   - [Section Name: Headcount](#merger-model-section-name-headcount)
2. [Founder Waterfall](#founder-waterfall)
   - [Assumptions](#founder-waterfall-assumptions)
   - [Founder Consideration](#founder-waterfall-founder-consideration)
   - [Cash Payout Summary](#founder-waterfall-cash-payout-summary)
   - [Stock Value Increase Scenarios](#founder-waterfall-stock-value-increase-scenarios)
   - [Founder Ownership & Stock Value](#founder-waterfall-founder-ownership-&-stock-value)
3. [Detailed Cap Table 11.12.21 (wi](#detailed-cap-table-11.12.21-(wi)
   - [Header](#detailed-cap-table-11.12.21-(wi-header)
   - [Capitalization Table](#detailed-cap-table-11.12.21-(wi-capitalization-table)
   - [Summary Statistics](#detailed-cap-table-11.12.21-(wi-summary-statistics)
4. [LogRocket>](#logrocket)
   - [Header](#logrocket-header)
5. [MD&A](#md&a)
   - [Section Name (Header)](#md&a-section-name-header)
6. [Assumptions](#assumptions)
   - [Section Name (Inbound Lead Assumptions)](#assumptions-section-name-inbound-lead-assumptions)
   - [Section Name (Outbound Lead Assumptions)](#assumptions-section-name-outbound-lead-assumptions)
   - [Section Name (Headcount Assumptions)](#assumptions-section-name-headcount-assumptions)
   - [Section Name (Tradeshow Assumptions)](#assumptions-section-name-tradeshow-assumptions)
   - [Section Name (Expense Assumptions)](#assumptions-section-name-expense-assumptions)
   - [Section Name (ARR Waterfall & Summary P&L)](#assumptions-section-name-arr-waterfall-&-summary-p&l)
7. [Functional P&L](#functional-p&l)
   - [Header](#functional-p&l-header)
   - [Income Statement](#functional-p&l-income-statement)
   - [Key Metrics & Growth Rates](#functional-p&l-key-metrics-&-growth-rates)
8. [Bookings Build](#bookings-build)
   - [Header](#bookings-build-header)
   - [ARR Bookings Summary](#bookings-build-arr-bookings-summary)
   - [Inbound Leads Assumptions](#bookings-build-inbound-leads-assumptions)
   - [Outbound Leads Assumptions](#bookings-build-outbound-leads-assumptions)
   - [Enterprise Headcount Assumptions](#bookings-build-enterprise-headcount-assumptions)
   - [Commercial Assumptions](#bookings-build-commercial-assumptions)
   - [Tradeshows Leads Assumptions](#bookings-build-tradeshows-leads-assumptions)
9. [Revenue Build](#revenue-build)
   - [Header](#revenue-build-header)
   - [Revenue Summary](#revenue-build-revenue-summary)
   - [ARR Waterfall - All Lead Types](#revenue-build-arr-waterfall---all-lead-types)
   - [ARR Waterfall - Inbound](#revenue-build-arr-waterfall---inbound)
   - [ARR Waterfall - Enterprise](#revenue-build-arr-waterfall---enterprise)
   - [ARR Waterfall - Commercial](#revenue-build-arr-waterfall---commercial)
   - [ARR Waterfall - Total Outbound](#revenue-build-arr-waterfall---total-outbound)
   - [ARR Waterfall - Tradeshow](#revenue-build-arr-waterfall---tradeshow)
   - [Revenue Reconciliation](#revenue-build-revenue-reconciliation)
10. [Expense Build](#expense-build)
   - [Expense Summary](#expense-build-expense-summary)
   - [Headcount Summary](#expense-build-headcount-summary)
   - [Headcount Expense Assumptions](#expense-build-headcount-expense-assumptions)
   - [Non-Headcount Expense Assumptions](#expense-build-non-headcount-expense-assumptions)
11. [Cash Summary](#cash-summary)
   - [Section Name (Header)](#cash-summary-section-name-header)
   - [Section Name (Cash Balance Waterfall)](#cash-summary-section-name-cash-balance-waterfall)
12. [Overview](#overview)
   - [ARR Metrics](#overview-arr-metrics)
   - [P&L Statement (Base Case)](#overview-p&l-statement-base-case)
   - [P&L Statement (% Revenue)](#overview-p&l-statement-%-revenue)
   - [Harpoon Assumption Adjustments](#overview-harpoon-assumption-adjustments)
   - [Harpoon Assumptions - Cashflow](#overview-harpoon-assumptions---cashflow)
13. [Model](#model)
   - [ARR Build - Harpoon](#model-arr-build---harpoon)
   - [Revenue & Contribution](#model-revenue-&-contribution)
   - [New Bookings Assumptions](#model-new-bookings-assumptions)
   - [Customer Size & Count](#model-customer-size-&-count)
   - [ARR Build - LT Model](#model-arr-build---lt-model)
14. [Bookings Waterfall](#bookings-waterfall)
   - [Bookings Waterfall Table](#bookings-waterfall-bookings-waterfall-table)
   - [Sum Cash-in Row](#bookings-waterfall-sum-cash-in-row)
   - [GRR Calculation](#bookings-waterfall-grr-calculation)
   - [Month Multiplier](#bookings-waterfall-month-multiplier)
15. [Presentation](#presentation)
   - [Slide Titles](#presentation-slide-titles)
   - [Key Metrics Table](#presentation-key-metrics-table)
   - [S&M Spend Analysis](#presentation-s&m-spend-analysis)
   - [Headcount Analysis](#presentation-headcount-analysis)
   - [Quarterly Cash & Equity Waterfall](#presentation-quarterly-cash-&-equity-waterfall)
16. [Q Preso](#q-preso)
   - [Section Name: Header (Slides)](#q-preso-section-name-header-slides)
   - [Section Name: ARR and Related Metrics](#q-preso-section-name-arr-and-related-metrics)
   - [Section Name: Headcount and Expense Analysis](#q-preso-section-name-headcount-and-expense-analysis)
   - [Section Name: Cash and Equity Waterfall](#q-preso-section-name-cash-and-equity-waterfall)
17. [Forecast](#forecast)
   - [ARR Rollforward](#forecast-arr-rollforward)
   - [Bookings Drivers](#forecast-bookings-drivers)
   - [GAAP P&L](#forecast-gaap-p&l)
   - [Key Metrics](#forecast-key-metrics)
   - [Cash Burn](#forecast-cash-burn)
   - [Efficiency Metrics](#forecast-efficiency-metrics)
   - [Customer Counts](#forecast-customer-counts)
   - [Headcount](#forecast-headcount)
18. [ARR](#arr)
   - [Section Name: ARR by Customer Segment (Corporate)](#arr-section-name-arr-by-customer-segment-corporate)
   - [Section Name: ARR by Customer Segment (Commercial)](#arr-section-name-arr-by-customer-segment-commercial)
   - [Section Name: ARR by Customer Segment (Strategic)](#arr-section-name-arr-by-customer-segment-strategic)
   - [Section Name: ARR by Customer Segment (Total)](#arr-section-name-arr-by-customer-segment-total)
   - [Section Name: Growth Rates and Retention Metrics](#arr-section-name-growth-rates-and-retention-metrics)
   - [Section Name: Gross Bookings by Customer Segment](#arr-section-name-gross-bookings-by-customer-segment)
   - [Section Name: Initial Sale Analysis](#arr-section-name-initial-sale-analysis)
   - [Section Name: Expansion Analysis](#arr-section-name-expansion-analysis)
   - [Section Name: Downgrade and Churn Analysis](#arr-section-name-downgrade-and-churn-analysis)
19. [Expenses](#expenses)
   - [ARR, Gross Bookings](#expenses-arr-gross-bookings)
   - [Total Expenses Breakdown](#expenses-total-expenses-breakdown)
   - [Sales & Marketing Expenses](#expenses-sales-&-marketing-expenses)
   - [Research & Development Expenses](#expenses-research-&-development-expenses)
   - [General & Administrative Expenses](#expenses-general-&-administrative-expenses)
   - [Headcount Summary](#expenses-headcount-summary)
20. [Products](#products)
   - [ARR by Product Segment](#products-arr-by-product-segment)
   - [Product Mix Analysis](#products-product-mix-analysis)
   - [ARR Rollforward by Segment](#products-arr-rollforward-by-segment)
   - [Mix Percentages by Segment](#products-mix-percentages-by-segment)
   - [ARR Rollforward ($) by Segment](#products-arr-rollforward-$-by-segment)
21. [Geo](#geo)
   - [Bookings by Geography and Product](#geo-bookings-by-geography-and-product)
   - [YoY Bookings Growth](#geo-yoy-bookings-growth)
   - [% Total Bookings](#geo-%-total-bookings)
   - [Channel Bookings](#geo-channel-bookings)
   - [% Channel](#geo-%-channel)
   - [Bookings by Segment (AMER, EMEA, APAC)](#geo-bookings-by-segment-amer-emea-apac)
22. [Pendo - Balance Sheet](#pendo---balance-sheet)
   - [Header](#pendo---balance-sheet-header)
   - [Balance Sheet](#pendo---balance-sheet-balance-sheet)
23. [Product Mix](#product-mix)
   - [Product Mix - Budget vs Actual/Forecast](#product-mix-product-mix---budget-vs-actualforecast)
   - [Team Performance - Budget vs Actual/Forecast](#product-mix-team-performance---budget-vs-actualforecast)
   - [Level Four Grouping - Inferred ARR](#product-mix-level-four-grouping---inferred-arr)
24. [ASC606](#asc606)
   - [Revenue and Commission Calculation](#asc606-revenue-and-commission-calculation)
   - [3 Year Depreciation Schedule](#asc606-3-year-depreciation-schedule)
   - [5 Year Depreciation Schedule](#asc606-5-year-depreciation-schedule)
25. [Expense Details](#expense-details)
   - [Section Name: COGS Section](#expense-details-section-name-cogs-section)
   - [Section Name: Operating Expenses Section](#expense-details-section-name-operating-expenses-section)
   - [Section Name: Detailed Expense Breakdown](#expense-details-section-name-detailed-expense-breakdown)
26. [ARR Looker](#arr-looker)
   - [Header](#arr-looker-header)
   - [Quarterly ARR Data by Segment](#arr-looker-quarterly-arr-data-by-segment)
27. [Prod Looker](#prod-looker)
   - [Header](#prod-looker-header)
   - [Data Table](#prod-looker-data-table)
28. [Region Looker](#region-looker)
   - [Initial Sale Bookings by Region (Monthly)](#region-looker-initial-sale-bookings-by-region-monthly)
   - [Expansion Bookings by Region (Monthly)](#region-looker-expansion-bookings-by-region-monthly)
   - [Total Gross Bookings (Monthly)](#region-looker-total-gross-bookings-monthly)
   - [Total per ARR (Monthly)](#region-looker-total-per-arr-monthly)
   - [Bookings Summary by Region](#region-looker-bookings-summary-by-region)
29. [22 Fcst ARR](#22-fcst-arr)
   - [Section Name: ARR Forecast by Customer Segment](#22-fcst-arr-section-name-arr-forecast-by-customer-segment)
   - [Section Name: ARR Forecast by Customer Sub-Segment](#22-fcst-arr-section-name-arr-forecast-by-customer-sub-segment)
   - [Section Name: ARR Adjustment Details](#22-fcst-arr-section-name-arr-adjustment-details)
   - [Section Name: Downgrade Analysis](#22-fcst-arr-section-name-downgrade-analysis)
30. [Historical P&L Adj](#historical-p&l-adj)
   - [Section Name: ASC 606 Adjustment - Quarterly](#historical-p&l-adj-section-name-asc-606-adjustment---quarterly)
   - [Section Name: ASC 606 Adjustment - Monthly](#historical-p&l-adj-section-name-asc-606-adjustment---monthly)
   - [Section Name: Cash Burn - Quarterly](#historical-p&l-adj-section-name-cash-burn---quarterly)
   - [Section Name: Cash Burn - Monthly (Implied)](#historical-p&l-adj-section-name-cash-burn---monthly-implied)
   - [Section Name: Cash Burn - Monthly](#historical-p&l-adj-section-name-cash-burn---monthly)
   - [Section Name: Fix - Quarterly](#historical-p&l-adj-section-name-fix---quarterly)
31. [Products - Old](#products---old)
   - [ARR Summary](#products---old-arr-summary)
   - [Product ARR and Bookings](#products---old-product-arr-and-bookings)
   - [Churn Analysis](#products---old-churn-analysis)
   - [Bookings](#products---old-bookings)
   - [Churn](#products---old-churn)
   - [Ending ARR by Product](#products---old-ending-arr-by-product)
   - [Ending ARR Growth Rate](#products---old-ending-arr-growth-rate)

---


====================================================================================================
# SHEET 1: Merger Model
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Merger Model
- **Key Sections Identified**:
    - Assumptions & Purchase Price Overview
    - Consideration Schedule
    - Sources and Uses
    - Financial Summary (ARR)
    - GAAP P&L
    - Cash Burn
    - Valuation & Shares Outstanding
    - PF Share Price Accretion / Dilution to Standalone
    - Key Metrics
    - Customer Counts
    - Headcount

## 2. Detailed Section Analysis

### Section Name: Assumptions & Purchase Price Overview
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the key assumptions driving the merger model and provides an overview of the purchase price calculation. It's used to determine the initial valuation and consideration for the acquisition.
- **Cell Range**: D7:I18
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: None
    - **Data Range**: H13:I18
- **Time Series Details**: None
- **Key Components**: CY'21E Revenue / ARR, Enterprise Value, Equity Value, Debt, Cash.
- **Notes & Customizations**: Purchase price overview is in $MM.

### Section Name: Consideration Schedule
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the schedule of payments (cash and equity) to the founders and other shareholders as part of the acquisition. It's used to understand the timing and structure of the consideration.
- **Cell Range**: D20:Q28
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: Columns F-K, M-Q
    - **Data Range**: F22:K28, N23:Q23
- **Time Series Details**:
    - Annual: 12 mos., 18 mos., 24 mos., 36 mos.
    - Frequency: Annual
    - Date Range: At Close, 12 mos., 18 mos., 24 mos., 36 mos.
- **Key Components**: Cash to Founders, Equity to Founders, Cash to Other S/H, Equity to Other S/H, Total Cash, Total Equity.
- **Notes & Customizations**: Consideration schedule is in $MM.

### Section Name: Sources and Uses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the sources of funds used to finance the acquisition and how those funds are allocated. It's used to ensure the sources and uses are balanced.
- **Cell Range**: D31:I45
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: Column H, I
    - **Data Range**: H32:I39, H42:I45
- **Time Series Details**: None
- **Key Components**: Cash from LR B/S, Cash from Pendo B/S, Cash Earnout Payments, New Equity, Total Sources, Cash to B/S, Equity Purchase Price, Fees and Expenses, Total Uses.
- **Notes & Customizations**: Sources and uses are in $MM.

### Section Name: Financial Summary (ARR)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of the Annual Recurring Revenue (ARR) for Pendo, LogRocket, and the combined entity. It's used to track the growth and performance of the business.
- **Cell Range**: D48:AZ87
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: G50:O50 (Historical FYE Jan. 31,), Q48:AZ48
    - **Data Range**: G54:O59, Q54:AZ59, G62:O68, Q62:AZ68, K71:O75, AG71:AZ75, G78:O83, Q78:AZ83, I86:O87, Q86:AZ87
- **Time Series Details**:
    - Annual: 2019-01-31 to 2027-01-31
    - Frequency: Annual
    - Quarterly: Q1 2019 to Q4 2027
    - Frequency: Quarterly
- **Key Components**: Pendo BOP ARR, New Customer ARR, Expansion ARR, Churn, Pendo EOP ARR, YoY Growth, LogRocket, LR EOP ARR, Total BOP ARR, Initial Sale, Expansion, Synergy EOP ARR, Consolidated EOP ARR.
- **Notes & Customizations**: ARR is in $MM.

### Section Name: GAAP P&L
- **Section Type**: Standard P&L
- **Description & Purpose**: This section presents the pro forma GAAP Profit and Loss statement, showing revenue, cost of goods sold (COGS), gross profit, operating expenses, and EBITDA. It's used to project the financial performance of the combined entity.
- **Cell Range**: D89:AZ164
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: G91:O91 (Historical FYE Jan. 31,), Q48:AZ48
    - **Data Range**: G94:O101, Q94:AZ101, G103:O104, Q103:AZ104, G107:O112, Q107:AZ112, K96:O96, AG96:AZ96, K109:O109, AG109:AZ109, G114:O114, Q114:AZ114, G118:O126, Q118:AZ126, G130:O134, Q130:AZ134, G137:O141, Q137:AZ141, K149:O153, AG149:AZ153, G156:O164, Q156:AZ164
- **Time Series Details**:
    - Annual: 2019-01-31 to 2027-01-31
    - Frequency: Annual
    - Quarterly: Q1 2019 to Q4 2027
    - Frequency: Quarterly
- **Key Components**: Revenue, Pendo Subscription Rev., LR Standalone Revenue, Total Subscription, PS, Other, Total Revenue, COGS, Pendo Subscription COGS, LR COGS, Total Subscription COGS, PS COGS, Total COGS, Gross Profit, Pendo Subscription GP, LR GP, Synergy GP, Total Gross Profit, Operating Expenses, Sales & Marketing, ASC 606 Adjustment, R&D, G&A, Total Pendo OpEx, Standalone LR OpEx, Total LR OpEx, Synergy LR OpEx, Consolidated Opex, Pendo Standalone EBITDA, LR + Synergy EBITDA, PF Consolidated EBITDA.
- **Notes & Customizations**: P&L is in $MM.

### Section Name: Key Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates key financial metrics and ratios, such as revenue growth, COGS percentage, S&M percentage, and efficiency metrics. It's used to assess the overall health and performance of the business.
- **Cell Range**: D166:AZ299
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: G91:O91 (Historical FYE Jan. 31,), Q48:AZ48
    - **Data Range**: G167:O172, Q167:AZ172, G170:O171, Q170:AZ171, G266:O270, Q266:AZ270, G273:O279, Q273:AZ279, G282:O287, Q282:AZ287, G291:O299, Q291:AZ299
- **Time Series Details**:
    - Annual: 2019-01-31 to 2027-01-31
    - Frequency: Annual
    - Quarterly: Q1 2019 to Q4 2027
    - Frequency: Quarterly
- **Key Components**: Sub Rev % ARR (per mo), PS Rev % PS Bookings, ASC 606 Adjustment % S&M, Subscription COGS % Rev, PS COGS % Rev, Total Bookings / S&M Excl 606, Net New ARR, Cash Burn per Net New ARR $, The Rule of 40%, Cash Burn % Rev, CAC Ratio, Payback Period (Mo), Magic Number, NRR (Annual), GRR (Annual), Logo Churn %, ARR per Employee, LTM Rev per Employee, Op Burn % Revenue, BOP Customer, Acquisition, New Customer, Churn Customer, EOP Customer, ARPA New, ARPA Base, Churn ARPA.
- **Notes & Customizations**: Metrics are in $MM where applicable.

### Section Name: Cash Burn
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the cash burn rate of the company, showing the beginning cash balance, incoming cash, total expenses, and ending cash balance. It's used to monitor the company's cash flow and runway.
- **Cell Range**: D176:AZ189
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: G179:O179 (Historical FYE Jan. 31,), Q48:AZ48
    - **Data Range**: G181:O187, Q181:AZ187, G189:O189, Q189:AZ189
- **Time Series Details**:
    - Annual: 2019-01-31 to 2027-01-31
    - Frequency: Annual
    - Quarterly: Q1 2019 to Q4 2027
    - Frequency: Quarterly
- **Key Components**: Cash BOP, Incoming Cash, Total Expenses, Other Non-Recurring, Equity, Cash EOP, Check to Model, Operating Cash Burn.
- **Notes & Customizations**: Cash burn is in $MM.

### Section Name: Valuation & Shares Outstanding
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the valuation of the company based on implied ARR multiples and also details the shares outstanding.
- **Cell Range**: D191:O232
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: None
    - **Data Range**: I192:O196, J198:O202, G206:O215, J218:O222, J224:O232
- **Time Series Details**:
    - Annual: 2023-01-31 to 2027-01-31
    - Frequency: Annual
- **Key Components**: EOP Public-Style Implied ARR, Enterprise Value, Equity Value, Less: Net Debt, Shares Outstanding, IPO Primary Shares Issued, Total Shares Oustanding, $ / Share, Acc / (Dil.) to Standalone
- **Notes & Customizations**: Valuation is in $MM.

### Section Name: PF Share Price Accretion / Dilution to Standalone
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the pro forma share price accretion or dilution compared to the standalone scenario. It's used to assess the impact of the merger on shareholder value.
- **Cell Range**: G235:U260
- **Layout Structure**:
    - **Row Headers Location**: Columns D, E, G, H
    - **Column Headers Location**: P238:P260
    - **Data Range**: H237, I237:M237, Q237:U237, D238, E238, H238, I238:M238, Q238:U238, D239, E239, H239, I239:M239, Q239:U239, D240, E240, H240, I240:M240, Q240:U240, D241, E241, H241, I241:M241, Q241:U241, D242, E242, H242, I242:M242, Q242:U242, H246, I246:M246, Q246:U246, H247, I247:M247, Q247:U247, H248, I248:M248, Q248:U248, H249, I249:M249, Q249:U249, H250, I250:M250, Q250:U250, H251, I251:M251, Q251:U251, H255, I255:M255, Q255:U255, H256, I256:M256, Q256:U256, H257, I257:M257, Q257:U257, H258, I258:M258, Q258:U258, H259, I259:M259, Q259:U259, H260, I260:M260, Q260:U260
- **Time Series Details**:
    - Annual: 2023-01-31 to 2027-01-31
    - Frequency: Annual
- **Key Components**: Standalone, ARR, Multiple, Enterprise Value, Equity Value, PF Accretion / Dilution to Standalone
- **Notes & Customizations**: PF Share Price Accretion / Dilution to Standalone

### Section Name: Customer Counts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the number of customers at different stages, including beginning of period (BOP), acquisition, new, churned, and end of period (EOP). It's used to understand customer acquisition and retention trends.
- **Cell Range**: D289:AZ299
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: G91:O91 (Historical FYE Jan. 31,), Q48:AZ48
    - **Data Range**: G291:O299, Q291:AZ299
- **Time Series Details**:
    - Annual: 2019-01-31 to 2027-01-31
    - Frequency: Annual
    - Quarterly: Q1 2019 to Q4 2027
    - Frequency: Quarterly
- **Key Components**: BOP Customer, Acquisition, New Customer, Churn Customer, EOP Customer, ARPA New, ARPA Base, Churn ARPA.
- **Notes & Customizations**: Customer Counts

### Section Name: Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount across different departments, including Marketing, Sales, CS/TS, PS, R&D, Product, G&A, and People. It's used to monitor staffing levels and efficiency.
- **Cell Range**: D301:AZ312
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: G91:O91 (Historical FYE Jan. 31,), Q48:AZ48
    - **Data Range**: G304:O312, Q304:AZ312
- **Time Series Details**:
    - Annual: 2019-01-31 to 2027-01-31
    - Frequency: Annual
    - Quarterly: Q1 2019 to Q4 2027
    - Frequency: Quarterly
- **Key Components**: Marketing, Sales, CS/TS, PS, R&D, Product, G&A, People, Grand Total.
- **Notes & Customizations**: Headcount


====================================================================================================
# SHEET 2: Founder Waterfall
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Founder Waterfall
- **Key Sections Identified**:
    - Assumptions
    - Founder Consideration
    - Cash Payout Summary
    - Stock Value Increase Scenarios
    - Founder Ownership & Stock Value

## 2. Detailed Section Analysis

### Assumptions
- **Section Type**: Assumptions
- **Description & Purpose**: This section contains assumptions used in the model, specifically a note about box colors representing assumptions.
- **Cell Range**: B3:B3
- **Layout Structure**:
    - **Row Headers Location**: B3
    - **Column Headers Location**: N/A
    - **Data Range**: B3
- **Time Series Details**: N/A
- **Key Components**: "Any box color is an assumption"
- **Notes & Customizations**: Single cell containing a note.

### Founder Consideration
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the sale price, founder consideration, and stock details.
- **Cell Range**: B5:E11
- **Layout Structure**:
    - **Row Headers Location**: B5:B11
    - **Column Headers Location**: C5:E5 (implied)
    - **Data Range**: C5:E11
- **Time Series Details**: N/A
- **Key Components**: Sale Price, Founder Consideration, Stock
- **Notes & Customizations**: Includes calculations for stock value and percentages.

### Cash Payout Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the cash payout to founders, including day 1 cash, holdback amount, and percentage of holdback.
- **Cell Range**: F6:I11
- **Layout Structure**:
    - **Row Headers Location**: F7:F10
    - **Column Headers Location**: G7:I7
    - **Data Range**: G8:I10
- **Time Series Details**: N/A
- **Key Components**: Founders, Day 1 Cash, Holdback Amount, % of holdback, Total
- **Notes & Customizations**: Summarizes cash payouts based on founder.

### Stock Value Increase Scenarios
- **Section Type**: Scenario Analysis
- **Description & Purpose**: This section shows the stock value at purchase and how it changes with different percentage increases.
- **Cell Range**: B13:C16
- **Layout Structure**:
    - **Row Headers Location**: B13:B16
    - **Column Headers Location**: C13 (implied)
    - **Data Range**: C13:C16
- **Time Series Details**: N/A
- **Key Components**: Stock Value at Purchase, .50% Increase, 100% Increase, 150% Increase
- **Notes & Customizations**: Presents different scenarios for stock value increases.

### Founder Ownership & Stock Value
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the founder's ownership percentage and the corresponding stock value under different increase scenarios.
- **Cell Range**: B19:J26
- **Layout Structure**:
    - **Row Headers Location**: B20:B26
    - **Column Headers Location**: C20:J20
    - **Data Range**: C21:F23, H21:J23, C25:D26
- **Time Series Details**: N/A
- **Key Components**: Key Shareholders (founders), FD Ownership, Stock Value ($12.13), 50% Increase, 100% Increase, 150% Increase, Total, Matt, Ben
- **Notes & Customizations**: Shows stock value changes for different founders.



====================================================================================================
# SHEET 3: Detailed Cap Table 11.12.21 (wi
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Detailed Cap Table 11.12.21 (wi
- **Key Sections Identified**:
    - Header
    - Capitalization Table
    - Summary Statistics

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the "As of" date. Provides context for the entire sheet.
- **Cell Range**: A1:A2
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: A1:A2
- **Time Series Details**: None
- **Key Components**: Report Title, "As of" Date
- **Notes & Customizations**: None

### Capitalization Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Detailed breakdown of ownership by individual and investor, showing shares held across different classes of stock, outstanding shares, fully diluted shares, and ownership percentages.
- **Cell Range**: A4:M126
- **Layout Structure**:
    - **Row Headers Location**: Column A (A4:A126) - "Anonymized Employee ID / Investor"
    - **Column Headers Location**: Row 4 (B4:M4) - Share classes (Common, Series A Preferred, Series B Preferred, Series Seed Preferred, Options), Outstanding Shares, Fully Diluted Shares, Outstanding Ownership
    - **Data Range**: B5:K126 (share counts), L5:L126 (Outstanding Ownership), M5:M126 (Fully Diluted Ownership)
- **Time Series Details**: None
- **Key Components**: Investor/Employee Names, Common Shares, Preferred Shares (Series A, B, Seed), Options, Outstanding Shares, Fully Diluted Shares, Outstanding Ownership, Fully Diluted Ownership.
- **Notes & Customizations**: Share counts are scaled by 1000.

### Summary Statistics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides summary statistics on shares outstanding, percentage outstanding, and price per share.
- **Cell Range**: A127:M133
- **Layout Structure**:
    - **Row Headers Location**: Column A (A127:A133) - Descriptions of share statistics
    - **Column Headers Location**: Row 4 (B4:M4) - Share classes (Common, Series A Preferred, Series B Preferred, Series Seed Preferred, Options), Outstanding Shares, Fully Diluted Shares, Outstanding Ownership
    - **Data Range**: B129:K133, L131, M128:M129 (various share statistics and prices)
- **Time Series Details**: None
- **Key Components**: Options and RSU's issued and outstanding, Shares available for issuance under the plan, Fully diluted shares, Total Shares Outstanding, Percentage Outstanding, Price per share
- **Notes & Customizations**: Share counts are scaled by 1000.


====================================================================================================
# SHEET 4: LogRocket>
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: LogRocket>
- **Key Sections Identified**: Header

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the financial model and the time period covered.
- **Cell Range**: B13:B14
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: B13:B14
- **Time Series Details**:
    - **Date Range**: CY2018A - CY2023E
    - **Frequency**: Annual
- **Key Components**: Project Title, Time Horizon
- **Notes & Customizations**: The time horizon is explicitly stated as "CY2018A - CY2023E", indicating actuals for 2018 and estimates through 2023.



====================================================================================================
# SHEET 5: MD&A
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: MD&A
- **Key Sections Identified**:
    - Header

## 2. Detailed Section Analysis

### Section Name (Header)
- **Section Type**: Header
- **Description & Purpose**: Contains the title and company name for the document.
- **Cell Range**: A1:B3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: A1:B3
- **Time Series Details**:
    - None
- **Key Components**: "LogRocket", "MD&A"
- **Notes & Customizations**: Basic header information.



====================================================================================================
# SHEET 6: Assumptions
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Assumptions
- **Key Sections Identified**:
    - Inbound Lead Assumptions
    - Outbound Lead Assumptions
    - Headcount Assumptions
    - Tradeshow Assumptions
    - Expense Assumptions
    - ARR Waterfall & Summary P&L

## 2. Detailed Section Analysis

### Section Name (Inbound Lead Assumptions)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the assumptions used to forecast inbound leads, including total MQLs, YoY growth, and conversion rates. It's used to project future revenue based on inbound marketing efforts.
- **Cell Range**: B13:I20
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns D to I represent years.
    - **Data Range**:
      - Annual data: `E16:I19`
- **Time Series Details**:
    - **Date Range**: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: Total MQLs from Website and Blogs, % YoY Growth, MQL to Paying Conversion %, Avg. Initial ARR, New Bookings, Upsell % of Beginning ARR.
- **Notes & Customizations**: Includes assumptions for MQLs, conversion rates, and ARR, which are critical for revenue forecasting.

### Section Name (Outbound Lead Assumptions)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the assumptions used to forecast outbound leads.
- **Cell Range**: B22:I28
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns G to I represent years.
    - **Data Range**:
      - Annual data: `G26:I28`
- **Time Series Details**:
    - **Date Range**: 2021 to 2023
    - **Frequency**: Annual
- **Key Components**: New AEs, Fully Ramped Equivalent Reps (avg.), Total AEs.
- **Notes & Customizations**: Includes assumptions for outbound sales team size and ramp-up, which are critical for revenue forecasting.

### Section Name (Headcount Assumptions)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the assumptions used to forecast headcount.
- **Cell Range**: K13:R36
- **Layout Structure**:
    - **Row Headers Location**: Column K, B
    - **Column Headers Location**: Columns M to R represent years.
    - **Data Range**:
      - Annual data: `M15:R36`
- **Time Series Details**:
    - **Date Range**: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: Sales, Marketing, Customer Success, R&D, G&A, Headcount Expense by Function.
- **Notes & Customizations**: Includes assumptions for headcount and related expenses, which are critical for expense forecasting.

### Section Name (Tradeshow Assumptions)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the assumptions used to forecast revenue from tradeshows.
- **Cell Range**: B46:I51
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns D to I represent years.
    - **Data Range**:
      - Annual data: `D49:I51`
- **Time Series Details**:
    - **Date Range**: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: # of Events, Converted Logos From Events, Avg. Initial ARR, New Bookings.
- **Notes & Customizations**: Includes assumptions for tradeshow performance, which are critical for revenue forecasting.

### Section Name (Expense Assumptions)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the assumptions used to forecast expenses.
- **Cell Range**: K38:R74
- **Layout Structure**:
    - **Row Headers Location**: Column K
    - **Column Headers Location**: Columns O to R represent years.
    - **Data Range**:
      - Annual data: `O40:R74`
- **Time Series Details**:
    - **Date Range**: 2020 to 2023
    - **Frequency**: Annual
- **Key Components**: Credit Card Fees, Hosting, Software Subscriptions, Computer Equipment, Other, Contractors.
- **Notes & Customizations**: Includes assumptions for various operating expenses, which are critical for expense forecasting.

### Section Name (ARR Waterfall & Summary P&L)
- **Section Type**: Standard P&L
- **Description & Purpose**: This section presents the ARR waterfall analysis and a summary Profit & Loss statement, projecting revenue, expenses, and profitability.
- **Cell Range**: T8:AA76
- **Layout Structure**:
    - **Row Headers Location**: Column T
    - **Column Headers Location**: Columns V to AA represent years.
    - **Data Range**:
      - Annual data: `V14:AA76`
- **Time Series Details**:
    - **Date Range**: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: Bookings (Inbound, Outbound, Tradeshow, Total), Consolidated ARR Snowball (Beginning Balance, New, Returning, Upsell, Churn, Lapsed, Downsell, Other, Ending Balance), Revenue, COS, Total COGS, Gross Profit, Operating Expenses (Sales & Marketing, Research & Development, General & Administrative, Total Operating Expenses), Stock Compensation, EBITDA, Change in Deferred Revenue, Cash EBITDA, D&A, EBIT, Interest Income, Net Profit.
- **Notes & Customizations**: Combines ARR waterfall and P&L, providing a comprehensive view of financial performance. Includes calculations for key metrics like EBITDA and Cash EBITDA.


====================================================================================================
# SHEET 7: Functional P&L
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Functional P&L
- **Key Sections Identified**:
    - Header
    - Income Statement
    - Key Metrics & Growth Rates

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and currency denomination. Provides context for the entire spreadsheet.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: B2:B4
    - **Column Headers Location**: N/A
    - **Data Range**: B2:B4
- **Time Series Details**: N/A
- **Key Components**: Company Name (LogRocket), Report Title (Functional P&L), Currency ($ in 000s).
- **Notes & Customizations**: Standard header information.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over time, including revenue, cost of goods sold, operating expenses, and profitability metrics.
- **Cell Range**: B7:AA55
- **Layout Structure**:
    - **Row Headers Location**: B7:B55
    - **Column Headers Location**: D7:AA8
    - **Data Range**:
      - Annual data: D10:AA10, D14:AA14, D15:AA15, H11:AA11, H16:AA16, D19:AA19, D20:AA20, D21:AA21, D23:AA23, D24:AA24, D27:AA27, D28:AA28, D29:AA29, D30:AA30, D31:AA31, D32:AA32, D33:AA33, D34:AA34, D36:AA36, D37:AA37, D39:AA39, D40:AA40, L42:AA42, L43:AA43, D45:AA45, D46:AA46, D48:AA48, L49:AA49, D51:AA51, D53:AA53, D55:AA55
- **Time Series Details**:
    - **Date Range**: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: Ending ARR, Revenue, Total Revenue, COS, Credit Card Fees, Hosting, Total COGS, Gross Profit, Operating Expenses, Sales & Marketing, Research & Development, General & Administrative, Total Operating Expenses, EBITDA, Change in Deferred Revenue, Cash EBITDA - Change in Deferred Revenue, D&A, EBIT, Interest Income, Net Profit.
- **Notes & Customizations**: Includes both actual (A) and estimated (E) values. Stock Compensation and Transaction Expense Add Back are split into different ranges.

### Key Metrics & Growth Rates
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents key financial metrics and growth rates alongside the Income Statement data, providing a summary of performance and future projections.
- **Cell Range**: AC7:AK55
- **Layout Structure**:
    - **Row Headers Location**: B7:B55 (same as Income Statement, but data is in columns AC:AK)
    - **Column Headers Location**: AC7:AK8
    - **Data Range**:
      - Annual data: AC10:AH10, AC14:AH14, AC15:AH15, AD11:AH11, AD16:AH16, AC19:AH19, AC20:AH20, AC21:AH21, AC23:AH23, AC24:AH24, AC27:AH27, AC28:AH28, AC29:AH29, AC30:AH30, AC31:AH31, AC32:AH32, AC33:AH33, AC34:AH34, AC36:AH36, AC37:AH37, AC39:AH39, AC40:AH40, AE42:AH42, AE43:AH43, AC45:AH45, AC46:AH46, AC48:AH48, AC49:AH49, AF49:AH49, AC51:AH51, AC53:AH53, AC55:AH55, AJ10:AK10, AJ15:AK15, AJ19:AK19, AJ20:AK20, AJ21:AK21, AJ23:AK23, AJ27:AK27, AJ29:AK29, AJ31:AK31, AJ33:AK33, AJ39:AK39, AK42, AJ45:AK45, AJ51:AK51, AJ55:AK55
- **Time Series Details**:
    - **Date Range**: 2018 to 2023
    - **Frequency**: Annual
- **Time Series Details**:
    - **Date Range**: 2018-2020 and 2020-2023
    - **Frequency**: CAGR (Compound Annual Growth Rate)
- **Key Components**: Same metrics as the Income Statement, plus CAGR values.
- **Notes & Customizations**: Includes CAGR calculations for certain periods.


====================================================================================================
# SHEET 8: Bookings Build
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Bookings Build
- **Key Sections Identified**:
    - Header
    - ARR Bookings Summary
    - Inbound Leads Assumptions
    - Outbound Leads Assumptions
    - Tradeshows Leads Assumptions
    - Enterprise Headcount Assumptions
    - Commercial Assumptions

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report name, and currency denomination.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: B2:B4
- **Time Series Details**: N/A
- **Key Components**: LogRocket, Bookings Build, $ in 000s
- **Notes & Customizations**: N/A

### ARR Bookings Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes ARR bookings by lead type (Inbound, Outbound, Tradeshow) and provides related calculations such as % YoY Growth and % of Total ARR by lead source.
- **Cell Range**: B10:AI43
- **Layout Structure**:
    - **Row Headers Location**: B12:B43
    - **Column Headers Location**: E7:AB7, AD7:AI7, E8:AB8, AD8:AI8
    - **Data Range**:
      - Annual data: E13:AB43
      - Annual data: AD13:AI43
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: Bookings Summary by Lead Type, New ARR Summary, Upsell ARR Summary, Inbound, Outbound, Tradeshow, % YoY Growth, Total New + Upsell ARR.
- **Notes & Customizations**: Data is presented in thousands of dollars. Includes calculations for percentage of total ARR by lead source.

### Inbound Leads Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details assumptions and calculations related to inbound leads, including MQLs, conversion rates, and logo metrics.
- **Cell Range**: B47:AI68
- **Layout Structure**:
    - **Row Headers Location**: B47:B68
    - **Column Headers Location**: E7:AB7, AD7:AI7, E8:AB8, AD8:AI8
    - **Data Range**:
      - Annual data: E50:AB68
      - Annual data: AD50:AI68
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: New ARR, Upsell ARR, Total Bookings, Beginning ARR, Total MQLs from Website and Blogs, MQL to Paying Conversion %, Avg. Initial ARR, New Bookings, BoP Logos, # of New Logos, # of Returning Logos, # of Churned Logos, # of Lapsed Logos, Total Logos, Upsell % of Beginning ARR.
- **Notes & Customizations**: Includes calculations for logo metrics and conversion rates.

### Outbound Leads Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details assumptions and calculations related to outbound leads, including metrics for enterprise bookings and rep productivity.
- **Cell Range**: B70:AI90
- **Layout Structure**:
    - **Row Headers Location**: B70:B90
    - **Column Headers Location**: E7:AB7, AD7:AI7, E8:AB8, AD8:AI8
    - **Data Range**:
      - Annual data: E74:AB90
      - Annual data: AD74:AI90
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: New ARR, Upsell ARR, Total Bookings, Beginning ARR, Avg. Initial ARR, New Bookings, BoP Logos, # of New Logos, # of Returning Logos, # of Churned Logos, # of Lapsed Logos, Total Logos, Upsell % of Beginning ARR, Avg. # of Closed Outbound Deals per Rep.
- **Notes & Customizations**: Includes metrics specific to enterprise bookings and rep productivity.

### Enterprise Headcount Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details assumptions related to enterprise headcount, including total AEs, new AEs, rep ramp times, and quota fulfillment.
- **Cell Range**: B92:AI103
- **Layout Structure**:
    - **Row Headers Location**: B92:B103
    - **Column Headers Location**: E7:AB7, AD7:AI7, E8:AB8, AD8:AI8
    - **Data Range**:
      - Annual data: S93:AB103
      - Annual data: AG93:AI103
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: Total Enterprise AEs, New Enterprise AEs, Rep Ramp, 3 Months, Rep Ramp, 6 Months, Fully Ramped Reps, Fully Ramped Equivalent Reps (avg.), Annual Quota for Fully Ramped Enterprise Reps, Fully Ramped Rep Productivity - $, Fully ramped Rep Productivity - %.
- **Notes & Customizations**: Focuses on headcount and productivity metrics for enterprise sales reps.

### Commercial Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details assumptions related to commercial bookings and headcount.
- **Cell Range**: B105:AI139
- **Layout Structure**:
    - **Row Headers Location**: B105:B139
    - **Column Headers Location**: E7:AB7, AD7:AI7, E8:AB8, AD8:AI8
    - **Data Range**:
      - Annual data: E106:AB139
      - Annual data: AD106:AI139
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: New ARR, Upsell ARR, Total Bookings, Beginning ARR, Avg. Initial ARR, New Bookings, BoP Logos, # of New Logos, # of Returning Logos, # of Churned Logos, # of Lapsed Logos, Total Logos, Upsell % of Beginning ARR, Avg. # of Closed Outbound Deals per Rep, Total AEs, New AEs, Rep Ramp, 3 Months, Rep Ramp, 6 Months, Fully Ramped Reps, Fully Ramped Equivalent Reps (avg.), (+) Sales-Led Inbound Bookings, (+) Historical Enterprise Bookings, (+) Commercial Bookings, Total Bookings Fulfilling Quota, Annual Quota for Fully Ramped Commercial Reps, Fully Ramped Rep Productivity - $, Fully ramped Rep Productivity - %.
- **Notes & Customizations**: Focuses on bookings and headcount metrics for commercial sales.

### Tradeshows Leads Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details assumptions related to tradeshow leads, including number of events, converted logos per event, and logo metrics.
- **Cell Range**: B141:AI161
- **Layout Structure**:
    - **Row Headers Location**: B141:B161
    - **Column Headers Location**: E7:AB7, AD7:AI7, E8:AB8, AD8:AI8
    - **Data Range**:
      - Annual data: E144:AB161
      - Annual data: AD144:AI161
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: New ARR, Upsell ARR, Total Bookings, Beginning ARR, # of Events, Converted Logos Per Event, BoP Logos, # of New Logos, # of Returning Logos, # of Churned Logos, # of Lapsed Logos, Total Logos, Upsell % of Beginning ARR.
- **Notes & Customizations**: Includes metrics specific to tradeshow leads.


====================================================================================================
# SHEET 9: Revenue Build
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Revenue Build
- **Key Sections Identified**:
    - Header
    - Revenue Summary
    - ARR Waterfall - All Lead Types
    - ARR Waterfall - Inbound
    - ARR Waterfall - Enterprise
    - ARR Waterfall - Commercial
    - Revenue Reconciliation

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and units. Provides context for the entire sheet.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: B2:B4
- **Time Series Details**: N/A
- **Key Components**: LogRocket, Revenue Build, $ in 000s
- **Notes & Customizations**: None

### Revenue Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the revenue by lead type and provides a reconciliation to the P&L.
- **Cell Range**: B10:AH18
- **Layout Structure**:
    - **Row Headers Location**: B12:B18
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D13:R18
      - Monthly data: S13:AA18
      - Annual data: AC13:AH18
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S13:AA18)
        - Frequency: Monthly
- **Key Components**: Revenue, Revenue Reconciliation to P&L, Total Revenue, % growth
- **Notes & Customizations**: Revenue is scaled by 1000.

### ARR Waterfall - All Lead Types
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for all lead types, breaking down the components of growth and churn.
- **Cell Range**: A20:AH41
- **Layout Structure**:
    - **Row Headers Location**: B23:B31, B33, B36, B38:B41
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D24:R41
      - Monthly data: S24:AA41
      - Annual data: AC24:AH41
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S24:AA41)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### ARR Waterfall - Inbound
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for Inbound leads, breaking down the components of growth and churn.
- **Cell Range**: A43:AH60
- **Layout Structure**:
    - **Row Headers Location**: B44:B52, B55, B57:B60
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D45:R60
      - Monthly data: S45:AA60
      - Annual data: AC45:AH60
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S45:AA60)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### ARR Waterfall - Enterprise
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for Enterprise leads, breaking down the components of growth and churn.
- **Cell Range**: A62:AH80
- **Layout Structure**:
    - **Row Headers Location**: B63:B72, B75, B77:B80
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D65:R80
      - Monthly data: S65:AA80
      - Annual data: AC65:AH80
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S65:AA80)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### ARR Waterfall - Commercial
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for Commercial leads, breaking down the components of growth and churn.
- **Cell Range**: A82:AH99
- **Layout Structure**:
    - **Row Headers Location**: B82:B91, B94, B96:B99
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D84:R99
      - Monthly data: S84:AA99
      - Annual data: AC84:AH99
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S84:AA99)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### ARR Waterfall - Total Outbound
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for Total Outbound leads, breaking down the components of growth and churn.
- **Cell Range**: A101:AH118
- **Layout Structure**:
    - **Row Headers Location**: B101:B110, B113, B115:B118
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D103:R118
      - Monthly data: S103:AA118
      - Annual data: AC103:AH118
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S103:AA118)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### ARR Waterfall - Tradeshow
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the waterfall of ARR changes for Tradeshow leads, breaking down the components of growth and churn.
- **Cell Range**: A120:AH137
- **Layout Structure**:
    - **Row Headers Location**: B120:B129, B132, B134:B137
    - **Column Headers Location**: D7:AA7, AC7, X7, T7, P7, L7, H7, D8:AH8
    - **Data Range**:
      - Annual data: D122:R137
      - Monthly data: S122:AA137
      - Annual data: AC122:AH137
- **Time Series Details**:
    - Annual: 2018 to 2023
        - Frequency: Annual
    - Monthly: CY2022E, CY2023E (Implies monthly from S122:AA137)
        - Frequency: Monthly
- **Key Components**: Beginning, (+) New, (+) Returning, (+) Upsell, (-) Churn, (-) Lapsed, (-) Downsell, Ending, % YoY Growth, Recognized Revenue, Upsell % of Beginning, Gross $ Retention (cancellations), Gross $ Retention (cancellations + downsell), Net $ Retention
- **Notes & Customizations**: ARR data is scaled by 1000.

### Revenue Reconciliation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Reconciles the revenue to the P&L.
- **Cell Range**: B139:AH140
- **Layout Structure**:
    - **Row Headers Location**: B139:B140
    - **Column Headers Location**: D7:R7, AC7:AH7
    - **Data Range**:
      - Annual data: D140:R140
      - Annual data: AC140:AH140
- **Time Series Details**:
    - Annual: 2018 to 2021
        - Frequency: Annual
    - Annual: 2018 to 2023
        - Frequency: Annual
- **Key Components**: Revenue Reconcilitaion to P&L
- **Notes & Customizations**: Revenue is scaled by 1000.


====================================================================================================
# SHEET 10: Expense Build
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Expense Build
- **Key Sections Identified**:
    - Expense Summary
    - Headcount Summary
    - Headcount Expense Assumptions
    - Non-Headcount Expense Assumptions

## 2. Detailed Section Analysis

### Expense Summary
- **Section Type**: Custom P&L
- **Description & Purpose**: This section provides a summary of expenses by function, including both headcount and non-headcount related costs. It allows for tracking total expenses across different departments and categories.
- **Cell Range**: B10:AH36
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: D7:AA8 and AC7:AH8
    - **Data Range**:
      - Annual data: D13:AA36
      - Annual data: AC13:AH36
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2023
      - Annual: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: Total Expense by Function, Cost of Sales, Sales, Marketing, Customer Success, R&D, G&A, Total Expenses, Non-Headcount Expenses, Total Non-Headcount Expenses.
- **Notes & Customizations**: Expenses are presented in $000s. There are two sets of annual data side-by-side.

### Headcount Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes headcount data, including average headcount by function and total headcount. It helps in understanding the staffing levels across different departments.
- **Cell Range**: A38:AH54
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: D7:AA8 and AC7:AH8
    - **Data Range**:
      - Annual data: E41:AA54
      - Annual data: AC41:AH54
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2023
      - Annual: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: Average Headcount by Function, Average Headcount, Total Headcount by Function, Total Headcount.
- **Notes & Customizations**: Headcount data is presented in $000s.

### Headcount Expense Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the assumptions used for calculating headcount expenses. It provides a breakdown of average quarterly headcount expense by function.
- **Cell Range**: A56:AH66
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: D7:AA8 and AC7:AH8
    - **Data Range**:
      - Annual data: E61:AA66
      - Annual data: AC61:AH66
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2023
      - Annual: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: Average Qtrly Headcount Expense by Function (EoP), Total Average Employee Headcount Expense.
- **Notes & Customizations**: Headcount expense data is presented in $000s.

### Non-Headcount Expense Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the assumptions for non-headcount expenses, providing a breakdown of various expense categories such as Credit Card Fees, Hosting, Travel, Software Subscriptions, Computer Equipment, and Other.
- **Cell Range**: A68:AH116
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: D7:AA8 and AC7:AH8
    - **Data Range**:
      - Annual data: D71:AA116
      - Annual data: AC71:AH116
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2023
      - Annual: 2018 to 2023
    - **Frequency**: Annual
- **Key Components**: Cost of Sales, Sales, Marketing, Customer Success, R&D, G&A, Software Subscriptions, Computer Equipment, Other, Contractors, Rent & Lease.
- **Notes & Customizations**: Non-headcount expense data is presented in $000s.


====================================================================================================
# SHEET 11: Cash Summary
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Cash Summary
- **Key Sections Identified**:
    - Header
    - Cash Balance Waterfall

## 2. Detailed Section Analysis

### Section Name (Header)
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and units for the data presented.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: B2:B4
    - **Column Headers Location**: N/A
    - **Data Range**: N/A
- **Time Series Details**: N/A
- **Key Components**: LogRocket, $ in 000s
- **Notes & Customizations**: This section provides context for the entire sheet.

### Section Name (Cash Balance Waterfall)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a waterfall analysis of the cash balance, showing the beginning balance, net cash burn, and ending balance. It includes both actual (A) and estimated (E) values.
- **Cell Range**: B12:AH15
- **Layout Structure**:
    - **Row Headers Location**: B13:B15
    - **Column Headers Location**: D7:AH8 (multiple time series)
    - **Data Range**:
      - Annual data: R13:AA15
      - Annual data: AF13:AH15
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018A to 2021E (using CY2018A, CY2019A, CY2020A, CY2021E headers)
      - Annual: 2022E to 2023E (using CY2022E, CY2023E headers)
    - **Frequency**: Annual
- **Key Components**: Beginning Cash Balance, Net Cash Burn From Operations, Ending Cash Balance
- **Notes & Customizations**: The data is presented in thousands of dollars. There are two separate blocks of annual data, one from columns R to AA, and another from columns AF to AH.


====================================================================================================
# SHEET 12: Overview
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Overview
- **Key Sections Identified**:
    - ARR Metrics
    - P&L Statement (Base Case)
    - P&L Statement (% Revenue)
    - Harpoon Assumption Adjustments
    - Harpoon Assumptions - Cashflow

## 2. Detailed Section Analysis

### ARR Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays key ARR (Annual Recurring Revenue) metrics, including Total BOP ARR, Initial Sale, Expansion, Churn, and EOP ARR. It provides a summary of the company's recurring revenue performance.
- **Cell Range**: B8:AB13
- **Layout Structure**:
    - **Row Headers Location**: B8:B13
    - **Column Headers Location**: C4:G4, I4:AB4
    - **Data Range**:
      - Annual data: C8:G12
      - Quarterly data: I8:AB12
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2023 to 2027
      - Quarterly: Q1 2023 to Q4 2027
    - **Frequency**:
      - Annual
      - Quarterly
- **Key Components**: Total BOP ARR, Initial Sale, Expansion, Churn, EOP ARR, GRR %
- **Notes & Customizations**: Values are scaled by 1000.

### P&L Statement (Base Case)
- **Section Type**: Standard P&L
- **Description & Purpose**: This section presents the core P&L (Profit and Loss) statement, showing Revenue, COGS, Gross Margin, Operating Expenses, and Operating Income. It provides a financial overview of the company's profitability.
- **Cell Range**: B15:AB35
- **Layout Structure**:
    - **Row Headers Location**: B15:B35
    - **Column Headers Location**: C4:G4, I4:AB4
    - **Data Range**:
      - Annual data: C15:G35
      - Quarterly data: I15:AB35
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2023 to 2027
      - Quarterly: Q1 2023 to Q4 2027
    - **Frequency**:
      - Annual
      - Quarterly
- **Key Components**: Revenue, COGS, Gross Margin, Sales, Marketing, CS/TS, ASC 606, R&D, G&A, Total Op Ex, Total Op Income, Cash In, Cash Out, Cash Generated
- **Notes & Customizations**: Values are scaled by 1000. Includes a "CHECK" row (B54) which may be a validation check.

### P&L Statement (% Revenue)
- **Section Type**: Custom P&L
- **Description & Purpose**: This section presents the P&L statement as a percentage of revenue. This allows for comparison of profitability and expense ratios over time.
- **Cell Range**: B57:AB69
- **Layout Structure**:
    - **Row Headers Location**: B57:B69
    - **Column Headers Location**: C4:G4, I4:AB4
    - **Data Range**:
      - Annual data: C59:G69
      - Quarterly data: I59:AB69
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2023 to 2027
      - Quarterly: Q1 2023 to Q4 2027
    - **Frequency**:
      - Annual
      - Quarterly
- **Key Components**: Revenue, COGS, Gross Margin, Sales, Marketing, CS/TS, ASC 606, R&D, G&A, Total Op Ex
- **Notes & Customizations**: Values are percentages of revenue.

### Harpoon Assumption Adjustments
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section allows for adjustments to key assumptions related to the Harpoon model.
- **Cell Range**: B72:AB88
- **Layout Structure**:
    - **Row Headers Location**: B72:B88
    - **Column Headers Location**: C4:G4, I4:AB4
    - **Data Range**:
      - Annual data: C74:G88
      - Quarterly data: I74:AB88
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2023 to 2027
      - Quarterly: Q1 2023 to Q4 2027
    - **Frequency**:
      - Annual
      - Quarterly
- **Key Components**: COGS, Sales, Marketing, CS/TS, ASC 606, R&D, G&A, COGS, Sales, Marketing, CS/TS, ASC 606, R&D, G&A
- **Notes & Customizations**: This section appears to be for manual adjustments to specific expense line items.

### Harpoon Assumptions - Cashflow
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays cash flow related assumptions for the Harpoon model.
- **Cell Range**: B91:AB95
- **Layout Structure**:
    - **Row Headers Location**: B91:B95
    - **Column Headers Location**: C4:G4, I4:AB4
    - **Data Range**:
      - Annual data: C94:G95
      - Quarterly data: I94:AB95
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2023 to 2027
      - Quarterly: Q1 2023 to Q4 2027
    - **Frequency**:
      - Annual
      - Quarterly
- **Key Components**: Pendo (Cash In), Cash Out
- **Notes & Customizations**: This section shows cash inflow and outflow assumptions.



====================================================================================================
# SHEET 13: Model
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Model
- **Key Sections Identified**:
    - ARR Build - Harpoon
    - Revenue & Contribution
    - New Bookings Assumptions
    - Customer Size & Count
    - ARR Build - LT Model

## 2. Detailed Section Analysis

### ARR Build - Harpoon
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section forecasts the ARR (Annual Recurring Revenue) build for the "Harpoon" product, broken down by customer segment (Corporate, Commercial, Enterprise) and tracks key metrics like Initial Sale, Expansion, Churn, and Gross Revenue Retention (GRR).
- **Cell Range**: C7:FB35
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data: `D10:L14`, `D17:L21`, `D24:L28`, `D31:L35`
      - Quarterly data: `N10:AW14`, `N17:AW21`, `N24:AW28`, `N31:AW35`
      - Monthly data: `AY10:FB14`, `AY17:FB21`, `AY24:FB28`, `AY31:FB35`
- **Time Series Details**:
    - Annual: 2019 to 2027
        - **Frequency**: Annual
    - Quarterly: Q1 2019 to Q4 2027
        - **Frequency**: Quarterly
    - Monthly: 2018-02 to 2027-01
        - **Frequency**: Monthly
- **Key Components**: Corporate BOP ARR, Initial Sale, Expansion, Churn, EOP ARR, GRR %, Total BOP ARR.
- **Notes & Customizations**: ARR is broken down by Corporate, Commercial, and Enterprise segments. Values are scaled by 1000.

### Revenue & Contribution
- **Section Type**: Custom P&L
- **Description & Purpose**: This section projects revenue, cost of goods sold (COGS), commission, and calculates the net harpoon contribution and cash contribution. It also includes calculations for subscription revenue percentage of ARR, gross margin, and commission rate.
- **Cell Range**: C37:FB47
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data: `D37:L40`, `D42:L43`, `H45:L47`
      - Quarterly data: `N37:AW40`, `N42:AW43`
      - Monthly data: `AY37:FB39`, `DG42:FB42`, `CI45:FB47`
- **Time Series Details**:
    - Annual: 2019 to 2027
        - **Frequency**: Annual
    - Quarterly: Q1 2019 to Q4 2027
        - **Frequency**: Quarterly
    - Monthly: 2018-02 to 2027-01
        - **Frequency**: Monthly
- **Key Components**: Revenue, COGS, Commission, Net Harpoon Contribution, NWC Impact - Deferred Revenue, Net Harpoon Cash Contribution, Subscription Revenue % of ARR (per Mo.), Gross Margin %, Commission Rate (% Bookings).
- **Notes & Customizations**: Values are scaled by 1000, except for percentages.

### New Bookings Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the assumptions used to forecast new bookings, including harpoon selling months, attach rate, ASP increase, and bookings by customer segment (Corporate, Commercial, Enterprise).
- **Cell Range**: C49:FB70
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data: `D51:L51`, `D55:L55`, `D58:L58`, `D60:L60`, `D63:L63`, `D65:L65`, `G70:L70`
      - Quarterly data: `N51:AW51`, `N55:AW55`, `N58:AW58`, `N60:AW60`, `N63:AW63`, `N65:AW65`, `N70:AW70`
      - Monthly data: `AY51:FB51`, `AY55:FB55`, `AY58:FB58`, `AY60:FB60`, `AY63:FB63`, `AY65:FB65`, `AY70:FB70`
- **Time Series Details**:
    - Annual: 2019 to 2027
        - **Frequency**: Annual
    - Quarterly: Q1 2019 to Q4 2027
        - **Frequency**: Quarterly
    - Monthly: 2018-02 to 2027-01
        - **Frequency**: Monthly
- **Key Components**: Harpoon Selling Months, New Bookings, Corporate Bookings, Attach Rate, ASP Increase (%), Corporate Harpoon Bookings, Commercial, Commercial Harpoon Bookings, Enterprise, Enterprise Harpoon Bookings, Total New Bookings.
- **Notes & Customizations**: Values are scaled by 1000, except for percentages.

### Customer Size & Count
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the customer size and count assumptions for each customer segment (Corporate, Commercial, Enterprise), along with price point and penetration of existing customers.
- **Cell Range**: C133:L170
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 2
    - **Data Range**:
      - Annual data: `G134:L136`, `G139:L142`, `H144:L146`, `H149:L151`, `G154:L157`, `G160:L163`, `I164:L165`, `G167:L167`, `G170:L170`
- **Time Series Details**:
    - Annual: 2019 to 2027
        - **Frequency**: Annual
- **Key Components**: Customer Size Avg, Customer Count, Price Point, Penetration of Existing, Base, Harpoon, LogRocket, Total Bookings, Worst Case, Best Case.
- **Notes & Customizations**: Values are scaled by 1000.

### ARR Build - LT Model
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section projects the ARR build using a long-term model, broken down by customer segment (Corporate, Commercial, Enterprise) and tracks key metrics like Initial Sale, Expansion, Churn, and Gross Revenue Retention (GRR).
- **Cell Range**: C90:FB118
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data: `D91:L96`, `D101:L106`, `D111:L116`
      - Quarterly data: `N91:AW96`, `N101:AW106`, `N111:AW116`
      - Monthly data: `AY91:FB96`, `AY101:FB106`, `AY111:FB116`
- **Time Series Details**:
    - Annual: 2019 to 2027
        - **Frequency**: Annual
    - Quarterly: Q1 2019 to Q4 2027
        - **Frequency**: Quarterly
    - Monthly: 2018-02 to 2027-01
        - **Frequency**: Monthly
- **Key Components**: Corporate BOP ARR, Initial Sale, Expansion, Churn, EOP ARR, GRR - Corp, Commercial BOP ARR, GRR - Comm, Enterprise BOP ARR, GRR - Ent.
- **Notes & Customizations**: ARR is broken down by Corporate, Commercial, and Enterprise segments. Values are scaled by 1000.


====================================================================================================
# SHEET 14: Bookings Waterfall
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Bookings Waterfall
- **Key Sections Identified**:
    - Bookings Waterfall Table
    - Sum Cash-in Row
    - GRR Calculation
    - Month Multiplier

## 2. Detailed Section Analysis

### Bookings Waterfall Table
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section represents the data used to create a bookings waterfall chart. It tracks initial sales, expansion bookings, churn, running total ATR bookings, and total bookings for collections on a monthly basis.
- **Cell Range**: A1:BC49
- **Layout Structure**:
    - **Row Headers Location**: Column A (Month), Columns B:F (Booking Types)
    - **Column Headers Location**: Row 1 (Booking Types), Row H1:BC1 (Dates)
    - **Data Range**:
      - Monthly data: `H2:BC49` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**: 2023-02-01 to 2027-01-01
    - **Frequency**: Monthly
- **Key Components**: Month, Initial Sale Bookings, Expansion Bookings, Churn, Running Total ATR Bookings, Total Bookings for Collections.
- **Notes & Customizations**: Values are scaled by 1000.

### Sum Cash-in Row
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section represents the sum of cash-in for each month.
- **Cell Range**: G51:BC51
- **Layout Structure**:
    - **Row Headers Location**: Column G
    - **Column Headers Location**: Row H50:BC50 (Dates)
    - **Data Range**:
      - Monthly data: `H51:BC51` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**: 2023-02-01 to 2027-01-01
    - **Frequency**: Monthly
- **Key Components**: Sum Cash-in
- **Notes & Customizations**: Values are scaled by 1000.

### GRR Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section represents the calculation of GRR (Gross Revenue Retention).
- **Cell Range**: C52:D52
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: None
    - **Data Range**: `D52` (numeric value)
- **Time Series Details**:
    - No time series
- **Key Components**: GRR
- **Notes & Customizations**: None

### Month Multiplier
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section represents the multiplier for each month.
- **Cell Range**: H53:V54
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: Row H53:V53 (Month Numbers)
    - **Data Range**: `H54:V54` (numeric values)
- **Time Series Details**:
    - No time series
- **Key Components**: Month 1, Month 2, Month 3, Month 4, Month 5, Month 6, Month 7, Month 8, Month 9, Month 10, Month 11, Month 12, Month 13, Month 14, Month 15
- **Notes & Customizations**: None


====================================================================================================
# SHEET 15: Presentation
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Presentation
- **Key Sections Identified**:
    - Slide Titles
    - Key Metrics Table
    - S&M Spend Analysis
    - Headcount Analysis
    - Quarterly Cash & Equity Waterfall

## 2. Detailed Section Analysis

### Slide Titles
- **Section Type**: Header
- **Description & Purpose**: Identifies the slide number associated with different sections of the spreadsheet.
- **Cell Range**: B2:BV2
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B2, M2, W2, AG2, AQ2, BK2, BA2, BV2
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Slide 1, Slide 2, Slide 3, Slide 4, Slide 5, Appendix 1, Slide 7, Slide 6
- **Notes & Customizations**: This section acts as a table of contents for the spreadsheet.

### Key Metrics Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of key performance indicators (KPIs) and financial metrics over time.
- **Cell Range**: C4:GI11
- **Layout Structure**:
    - **Row Headers Location**: C5:C11, M6:M11, W6:W11, AG6:AG11
    - **Column Headers Location**: C4:J4, N4:U4, X4:AE4, AH4:AO4, AR4:AY4, BB4:BI4, BL4:BS4, BW4:CD4, CH4:CO4, CS4:CZ4, DC4:DJ4, DM4:DT4, DW4:ED4, FA4:FH4, FK4:FR4, FU4:GB4, GE4:GL4, GO4:GV4
    - **Data Range**:
      - Annual data: C6:J11, N7:U11, X7:AE11, AH7:AO11, AR7:AY11, BB7:BI11, BL7:BS11, BW7:CD11, CH7:CO11, CS7:CZ11, DC7:DJ11, DM7:DT11, DW7:ED11, FA7:FH11, FK7:FR11, FU7:GB11, GE7:GL11, GO7:GV11
- **Time Series Details**:
    - **Date Range**: 2019 to 2026
    - **Frequency**: Annual
- **Key Components**: Gross Bookings, EOP ARR, YoY Growth, Churn, Churn % BOP ARR, NRR (Annual), GRR (Annual), Logo Churn %, Rule of 40%, Cash Burn % Rev
- **Notes & Customizations**: Includes both absolute values and percentage-based metrics. Some values are scaled by 1000.

### S&M Spend Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes Sales and Marketing (S&M) spending and its impact on bookings and ARR.
- **Cell Range**: W13:CD20
- **Layout Structure**:
    - **Row Headers Location**: W13:W20, BK13:BK20, BV13:BV20
    - **Column Headers Location**: BW4:CD4
    - **Data Range**:
      - Annual data: BW13:CD20
- **Time Series Details**:
    - **Date Range**: 2019 to 2026
    - **Frequency**: Annual
- **Key Components**: Net ARR Growth, S&M Spend1, Efficiency Ratio, CAC Ratio, Payback Period (mo), Magic Number, Operating Expenses, Sales & Marketing, % Gross Bookings
- **Notes & Customizations**: Focuses on S&M efficiency metrics.

### Headcount Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of headcount across different departments and related metrics.
- **Cell Range**: EF6:EX31
- **Layout Structure**:
    - **Row Headers Location**: EF7:EF31, EP7:EP31
    - **Column Headers Location**: EG6:EN6, EQ6:EX6
    - **Data Range**:
      - Annual data: EG7:EN31, EQ7:EX31
- **Time Series Details**:
    - **Date Range**: 2019 to 2026
    - **Frequency**: Annual
- **Key Components**: R&D, Product, Other, Headcount & Related, Engineering, Legal, People, Total Research & Development, Total General & Administrative, Product Headcount (EOP), Product Headcount (Avg), G&A Headcount (EOP), G&A Headcount (Avg), People Headcount (EOP), People Headcount (Avg)
- **Notes & Customizations**: Includes headcount numbers, ARR per head, and related ratios.

### Quarterly Cash & Equity Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Shows the quarterly changes in cash and equity balances.
- **Cell Range**: B43:CO46
- **Layout Structure**:
    - **Row Headers Location**: B44:B46
    - **Column Headers Location**: C43:AH43
    - **Data Range**:
      - Quarterly data: C44:AH46, CI44:CO44
- **Time Series Details**:
    - **Date Range**: Q1 2019 to Q4 2026
    - **Frequency**: Quarterly
- **Key Components**: Cash, Equity, Operating Burn
- **Notes & Customizations**: Data is presented in thousands.


====================================================================================================
# SHEET 16: Q Preso
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Q Preso
- **Key Sections Identified**:
    - Header (Slides)
    - ARR and Related Metrics
    - Headcount and Expense Analysis
    - Cash and Equity Waterfall

## 2. Detailed Section Analysis

### Section Name: Header (Slides)
- **Section Type**: Header
- **Description & Purpose**: This section identifies the slide number associated with the data presented in the corresponding columns.
- **Cell Range**: B2:CR2
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B2, M2, W2, AG2, AQ2, BA2, BV2, CG2, CR2
    - **Data Range**: N/A
- **Time Series Details**: None
- **Key Components**: Slide numbers.
- **Notes & Customizations**: This is a header section, not a data section.

### Section Name: ARR and Related Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents key performance indicators (KPIs) related to Annual Recurring Revenue (ARR), growth, and sales & marketing efficiency.
- **Cell Range**: C4:AE19
- **Layout Structure**:
    - **Row Headers Location**: M6:M19, W6:W19, AG6:AG8, AG10:AG12, W13:W15, M16:M19
    - **Column Headers Location**: C4:AE4 (Quarterly)
    - **Data Range**:
      - Quarterly data: C6:AE19
- **Time Series Details**:
    - **Date Range**: 2022-Q1 to 2023-Q4
    - **Frequency**: Quarterly
- **Key Components**: Revenue, PS, Sub, Gross Bookings, EOP ARR, Churn, NRR, GRR, S&M Spend, Efficiency Ratio, CAC Ratio, Payback Period, Magic Number.
- **Notes & Customizations**: Includes both absolute values and percentage metrics. Some metrics are scaled by 1000.

### Section Name: Headcount and Expense Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of headcount, related expenses, and efficiency metrics across different departments.
- **Cell Range**: EF2:GH31
- **Layout Structure**:
    - **Row Headers Location**: EF2:EF31, EP2:EP31, EZ2:EZ24, BK6:BK27, BV6:BV20
    - **Column Headers Location**: EG6:EN6, EQ6:EX6, CH6:CO6
    - **Data Range**:
      - Quarterly data: CH7:CO19, CH37:CO40, CI44:CO44
      - Monthly data: EG8:EN24, EQ8:EX31
- **Time Series Details**:
    - **Date Range**:
        - Quarterly: 2022-Q1 to 2023-Q4
        - Monthly: EG6:EN6 and EQ6:EX6 are date series, but the start and end dates are not clear from the provided JSON.
    - **Frequency**:
        - Quarterly
        - Monthly
- **Key Components**: R&D, G&A, S&M, Product, Engineering, People, Total Headcount, Operating Expenses, Cost per Head, ARR per Head.
- **Notes & Customizations**: Includes both headcount numbers and related expense metrics.

### Section Name: Cash and Equity Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section tracks the changes in cash and equity over time, showing the impact of operating burn.
- **Cell Range**: B41:AH46
- **Layout Structure**:
    - **Row Headers Location**: B44:B46
    - **Column Headers Location**: C43:AH43 (Quarterly)
    - **Data Range**: C44:AH46
- **Time Series Details**:
    - **Date Range**: 2019-Q1 to 2026-Q4
    - **Frequency**: Quarterly
- **Key Components**: Cash, Equity, Operating Burn.
- **Notes & Customizations**: This section provides a high-level overview of cash flow and equity changes.


====================================================================================================
# SHEET 17: Forecast
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Forecast
- **Key Sections Identified**:
    - ARR Rollforward
    - Bookings Drivers
    - GAAP P&L
    - Key Metrics
    - Cash Burn
    - Efficiency Metrics
    - Customer Counts
    - Headcount

## 2. Detailed Section Analysis

### ARR Rollforward
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the rollforward of Annual Recurring Revenue (ARR), showing the components that contribute to changes in ARR over time. It's used to understand the drivers of ARR growth.
- **Cell Range**: C7:FB15
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 4 and 5
    - **Data Range**:
      - Annual data: D9:L15
      - Quarterly data: N9:AW15
      - Monthly data: AY9:FB15
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: BOP ARR, Acquisitions, New Customer ARR, Expansion ARR, Churn, EOP ARR, YoY Growth.
- **Notes & Customizations**: ARR is presented in thousands. There are three time series: Annual, Quarterly, and Monthly.

### Bookings Drivers
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section focuses on the drivers behind bookings, including PS (Professional Services) bookings and overall gross bookings. It helps in understanding the sources and seasonality of bookings.
- **Cell Range**: C17:FB23
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 4 and 5
    - **Data Range**:
      - Annual data: D17:L23
      - Quarterly data: N17:AW23
      - Monthly data: AY17:FB23
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: PS Bookings, PS % Total Bookings, Gross Bookings, Seasonality of Churn, Seasonality of Bookings.
- **Notes & Customizations**: Bookings are presented in thousands. There are three time series: Annual, Quarterly, and Monthly.

### GAAP P&L
- **Section Type**: Standard P&L
- **Description & Purpose**: This section presents the standard GAAP Profit and Loss statement, showing revenue, cost of goods sold (COGS), gross margin, operating expenses, and operating EBITDA. It's used to assess the company's profitability.
- **Cell Range**: C26:FB49
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 4 and 5
    - **Data Range**:
      - Annual data: D28:L49
      - Quarterly data: N28:AW49
      - Monthly data: AY28:FB49
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Revenue, Subscription, PS, COGS, Subscription COGS, PS COGS, Gross Margin, Operating Expenses, Sales & Marketing, R&D, G&A, Operating EBITDA Income/(Loss).
- **Notes & Customizations**: Values are presented in thousands. There are three time series: Annual, Quarterly, and Monthly. There is a "CHECK" row which likely contains a formula to validate the model.

### Key Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays key performance indicators (KPIs) related to revenue, cost, and efficiency. It provides insights into the company's operational performance.
- **Cell Range**: C51:FB57
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 4 and 5
    - **Data Range**:
      - Annual data: D52:L57
      - Quarterly data: N52:AW57
      - Monthly data: AY52:FB57
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Sub Rev % ARR (per mo), PS Rev % PS Bookings, ASC 606 Adjustment % S&M, Subscription COGS % Rev, PS COGS % Rev, Total Bookings / S&M Excl 606.
- **Notes & Customizations**: Values are a mix of percentages and thousands. There are three time series: Annual, Quarterly, and Monthly.

### Cash Burn
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section focuses on cash flow metrics, including cash burn, incoming cash, total expenses, and equity. It's used to monitor the company's cash position.
- **Cell Range**: C61:FB76
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 4 and 5
    - **Data Range**:
      - Annual data: D63:L76
      - Quarterly data: N63:AW76
      - Monthly data: AY63:FB76
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Cash BOP, Incoming Cash, Total Expenses, Other Non-Recurring, Equity, Cash EOP, Operating Cash Burn, Incoming Cash % Revenue, Outgoing Cash % Op Ex + COGS.
- **Notes & Customizations**: Values are presented in thousands. There are three time series: Annual, Quarterly, and Monthly. There is a "Check to Model" row which likely contains a formula to validate the model.

### Efficiency Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents metrics related to efficiency, such as revenue percentages, net new ARR, cash burn per net new ARR, and the Rule of 40%. It's used to assess the company's efficiency in generating revenue and managing costs.
- **Cell Range**: C78:FB94
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 4 and 5
    - **Data Range**:
      - Annual data: D81:L94
      - Quarterly data: N81:AW94
      - Monthly data: AY81:FB94
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Revenue %, COGS, S&M, R&D, G&A, S&M incl 606, Net New ARR, Cash Burn per Net New ARR $, The Rule of 40%, Cash Burn % Rev, CAC Ratio, Payback Period (Mo), Magic Number.
- **Notes & Customizations**: Values are a mix of percentages and thousands. There are three time series: Annual, Quarterly, and Monthly.

### Customer Counts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks customer-related metrics, including BOP Customer, Acquisition, New Customer, Churn Customer, and EOP Customer. It's used to monitor customer growth and churn.
- **Cell Range**: C104:FB114
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 4 and 5
    - **Data Range**:
      - Annual data: D106:L114
      - Quarterly data: N106:AW114
      - Monthly data: AY106:FB114
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: BOP Customer, Acquisition, New Customer, Churn Customer, EOP Customer, ARPA New, ARPA Base, Churn ARPA.
- **Notes & Customizations**: Values are presented in thousands. There are three time series: Annual, Quarterly, and Monthly.

### Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks headcount across different departments, including Marketing, Sales, CS/TS, PS, R&D, Product, G&A, and People. It's used to monitor staffing levels and related expenses.
- **Cell Range**: C116:FB127
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 4 and 5
    - **Data Range**:
      - Annual data: D119:L127
      - Quarterly data: N119:AW127
      - Monthly data: AY119:FB127
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Marketing, Sales, CS/TS, PS, R&D, Product, G&A, People, Grand Total.
- **Notes & Customizations**: Values are presented in thousands. There are three time series: Annual, Quarterly, and Monthly.


====================================================================================================
# SHEET 18: ARR
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: ARR
- **Key Sections Identified**:
    - ARR by Customer Segment (Corporate, Commercial, Strategic, Total)
    - Growth Rates and Retention Metrics
    - Gross Bookings by Customer Segment
    - Initial Sale Analysis
    - Downgrade and Churn Analysis

## 2. Detailed Section Analysis

### Section Name: ARR by Customer Segment (Corporate)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the Annual Recurring Revenue (ARR) for the Corporate customer segment, tracking changes due to initial sales, expansions, downgrades, and churn. It provides a view of ARR movement over time.
- **Cell Range**: A6:FB12
- **Layout Structure**:
    - **Row Headers Location**: A7:A12, C7:C12
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D7:L12
      - Quarterly data: N7:AW12
      - Monthly data: AY7:FB12
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: BOP ARR, Initial Sale, Expansion, Downgrade, Churn, EOP ARR
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: ARR by Customer Segment (Commercial)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the Annual Recurring Revenue (ARR) for the Commercial customer segment, tracking changes due to initial sales, expansions, downgrades, and churn. It provides a view of ARR movement over time.
- **Cell Range**: A17:FB23
- **Layout Structure**:
    - **Row Headers Location**: A18:A23, C18:C23
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D18:L23
      - Quarterly data: N18:AW23
      - Monthly data: AY18:FB23
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: BOP ARR, Initial Sale, Expansion, Downgrade, Churn, EOP ARR
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: ARR by Customer Segment (Strategic)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the Annual Recurring Revenue (ARR) for the Strategic customer segment, tracking changes due to initial sales, expansions, downgrades, and churn. It provides a view of ARR movement over time.
- **Cell Range**: A28:FB34
- **Layout Structure**:
    - **Row Headers Location**: A29:A34, C29:C34
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D29:L34
      - Quarterly data: N29:AW34
      - Monthly data: AY29:FB34
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: BOP ARR, Initial Sale, Expansion, Downgrade, Churn, EOP ARR
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: ARR by Customer Segment (Total)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the total Annual Recurring Revenue (ARR) across all customer segments, tracking changes due to initial sales, expansions, downgrades, and churn. It provides a consolidated view of ARR movement over time.
- **Cell Range**: A39:FB45
- **Layout Structure**:
    - **Row Headers Location**: C40:C45
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D40:L45
      - Quarterly data: N40:AW45
      - Monthly data: AY40:FB45
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: BOP ARR, Initial Sale, Expansion, Downgrade, Churn, EOP ARR
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Growth Rates and Retention Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the Gross Revenue Retention (GRR) and Net Revenue Retention (NRR) for each customer segment (Corporate, Commercial, Enterprise) and overall. It provides insight into customer retention and revenue growth.
- **Cell Range**: A14:FB15, A25:FB26, A36:FB37, A47:FB48, A90:FB92
- **Layout Structure**:
    - **Row Headers Location**: C14:C15, C25:C26, C36:C37, C47:C48, C90:C92
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D14:L15, D25:L26, D36:L37, D47:L48, D90:L92
      - Quarterly data: Q14:AW15, Q25:AW26, Q36:AW37, Q47:AW48, N90:AW92
      - Monthly data: AY14:FB15, AY25:FB26, AY36:FB37, AY47:FB48, AY90:FB92
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: GRR - Corp, NRR - Corp, GRR - Comm, NRR - Comm, GRR - Ent, NRR - Ent, GRR, NRR
- **Notes & Customizations**:

### Section Name: Gross Bookings by Customer Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the Gross Bookings for each customer segment (Corporate, Commercial, Enterprise, Total). It provides a view of new business acquired over time.
- **Cell Range**: A53:FB56, A58:FB62, A64:FB68
- **Layout Structure**:
    - **Row Headers Location**: A53:A56, C53:C56, C58:C62, C64:C68
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D53:L56, D59:L62, E65:L68
      - Quarterly data: N53:AW56, N59:AW62, R65:AW68
      - Monthly data: AY53:FB56, AY59:FB62, BK65:FB68
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Corporate, Commercial, Enterprise, Total, % of Total, YoY Growth
- **Notes & Customizations**: Values are scaled by 1000 for the first part of the section.

### Section Name: Initial Sale Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the Initial Sale performance by customer segment (Corporate, Commercial, Enterprise, Total), showing both percentages and dollar values.
- **Cell Range**: A70:FB80
- **Layout Structure**:
    - **Row Headers Location**: C70:C74, C76:C80
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D71:L74, D77:L80
      - Quarterly data: N71:AW74, N77:AW80
      - Monthly data: AY71:FB74, AY77:FB80
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Initial Sale %, Initial Sale $
- **Notes & Customizations**: Values are scaled by 1000 for the dollar values.

### Section Name: Expansion Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the Expansion performance by customer segment (Corporate, Commercial, Enterprise, Total), showing dollar values.
- **Cell Range**: A82:FB86
- **Layout Structure**:
    - **Row Headers Location**: C82:C86
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D83:L86
      - Quarterly data: N83:AW86
      - Monthly data: AY83:FB86
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Expansion $
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Downgrade and Churn Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes Downgrade and Churn, including seasonality, by customer segment (Corporate, Commercial, Enterprise, Total).
- **Cell Range**: A94:FB112
- **Layout Structure**:
    - **Row Headers Location**: C94:C112
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D94:L94, D97:L99, D100:L100, D103:L105, D106:L106, D109:L111, D112:L112
      - Quarterly data: N94:AW94, N97:AW99, N100:AW100, N103:AW105, N106:AW106, N109:AW111, N112:AW112
      - Monthly data: AY94:FB94, AY97:FB99, AY100:FB100, AY103:FB105, AY106:FB106, AY109:FB111, AY112:FB112
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Seasonality of Churn, Downgrade, Churn, Total, Downgrade %
- **Notes & Customizations**: Values are scaled by 1000 for the dollar values.


====================================================================================================
# SHEET 19: Expenses
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Expenses
- **Key Sections Identified**:
    - ARR, Gross Bookings
    - Total Expenses Breakdown
    - Sales & Marketing Expenses
    - Research & Development Expenses
    - General & Administrative Expenses
    - Headcount Summary

## 2. Detailed Section Analysis

### ARR, Gross Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents key revenue-related metrics, including ARR (Annual Recurring Revenue) and Gross Bookings. It's used to track the company's top-line performance.
- **Cell Range**: C7:FB11
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: D5:L5 (Annual), N5:AW5 (Quarterly), AY5:FB5 (Monthly)
    - **Data Range**:
      - Annual data: D9:L11
      - Quarterly data: N9:AW11
      - Monthly data: AY9:FB11
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: ARR, ARR (EOP), ARR (Avg), Gross Bookings
- **Notes & Customizations**: Values are scaled by 1000.

### Total Expenses Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: This section breaks down total expenses into various categories, providing insights into the cost structure.
- **Cell Range**: C14:FB46
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: D5:L5 (Annual), N5:AW5 (Quarterly), AY5:FB5 (Monthly)
    - **Data Range**:
      - Annual data: D16:L46
      - Quarterly data: N16:AW46
      - Monthly data: AY16:FB46
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Total Expenses, Subscription COGS, PS COGS, Operating Expenses, Subscription Revenue, Hosting Expenses, Subscription Margin ($), Subscription Margin (%), PS Revenue, PS Margin ($), PS Margin (%)
- **Notes & Customizations**: Values are scaled by 1000. Includes both dollar amounts and percentages.

### Sales & Marketing Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the expenses and headcount related to the Sales & Marketing department. It's used to monitor the efficiency and cost-effectiveness of sales and marketing efforts.
- **Cell Range**: C48:FB92
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: D5:L5 (Annual), N5:AW5 (Quarterly), AY5:FB5 (Monthly)
    - **Data Range**:
      - Annual data: D51:L92
      - Quarterly data: N51:AW92
      - Monthly data: AY51:FB92
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Sales & Marketing, Headcount & Related, Sales Headcount (EOP), Sales Headcount (Avg), Marketing Headcount (EOP), Marketing Headcount (Avg), CS/TS Headcount (EOP), CS/TS Headcount (Avg), Total Sales & Marketing
- **Notes & Customizations**: Values are scaled by 1000. Includes headcount metrics and expense allocations.

### Research & Development Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section focuses on the expenses and headcount associated with the Research & Development department. It's used to track investments in innovation and product development.
- **Cell Range**: C94:FB118
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: D5:L5 (Annual), N5:AW5 (Quarterly), AY5:FB5 (Monthly)
    - **Data Range**:
      - Annual data: D97:L118
      - Quarterly data: N97:AW118
      - Monthly data: AY97:FB118
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Research & Development, Product, Engineering, Total Research & Development, Product Headcount (EOP), Product Headcount (Avg), Engineering Headcount (EOP), Engineering Headcount (Avg)
- **Notes & Customizations**: Values are scaled by 1000. Includes headcount metrics and expense allocations.

### General & Administrative Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the expenses and headcount related to the General & Administrative functions. It's used to monitor overhead costs and administrative efficiency.
- **Cell Range**: C120:FB149
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: D5:L5 (Annual), N5:AW5 (Quarterly), AY5:FB5 (Monthly)
    - **Data Range**:
      - Annual data: D123:L149
      - Quarterly data: N123:AW149
      - Monthly data: AY123:FB149
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: General & Administrative, Rent, Legal, Total General & Administrative, G&A Headcount (EOP), G&A Headcount (Avg), People Headcount (EOP), People Headcount (Avg)
- **Notes & Customizations**: Values are scaled by 1000. Includes headcount metrics and expense allocations.

### Headcount Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of headcount across different departments.
- **Cell Range**: C152:L163
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: D5:L5 (Annual)
    - **Data Range**: D155:L163
- **Time Series Details**:
    - **Date Range**: 2019 to 2027
    - **Frequency**: Annual
- **Key Components**: Headcount, Marketing, Sales, CS/TS, PS, R&D, Product, G&A, People, Grand Total
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 20: Products
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Products
- **Key Sections Identified**:
    - ARR by Product Segment
    - Product Mix Analysis
    - ARR Rollforward by Segment
    - Mix Percentages by Segment
    - ARR Rollforward ($) by Segment

## 2. Detailed Section Analysis

### ARR by Product Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the ARR (Annual Recurring Revenue) for different product segments (Corporate, Commercial, Enterprise, and Total) over time. It allows for tracking the performance of each segment and the overall ARR.
- **Cell Range**: C7:FB31
- **Layout Structure**:
    - **Row Headers Location**: Column C (e.g., "Products", "ARR - Corp", "ARR - Comm", "ARR - Enterprise", "ARR - Total")
    - **Column Headers Location**: Rows 2 and 5 (containing date information)
    - **Data Range**:
      - Annual data: D10:L13, D16:L19, D22:L25, D28:L31 (numeric values for annual periods)
      - Quarterly data: N10:AW13, N16:AW19, N22:AW25, N28:AW31 (numeric values for quarterly periods)
      - Monthly data: AY10:FB13, AY16:FB19, AY22:FB25, AY28:FB31 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: ARR for Corporate, Commercial, Enterprise, and Total segments.
- **Notes & Customizations**: ARR values are scaled by 1000. There are three time series horizons: annual, quarterly, and monthly.

### Product Mix Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the product mix for different product segments (Corporate, Commercial, Enterprise, and Total) over time. It allows for tracking the percentage of each product segment and the overall product mix.
- **Cell Range**: C33:FB37
- **Layout Structure**:
    - **Row Headers Location**: Column C ("Product Mix")
    - **Column Headers Location**: Rows 2 and 5 (containing date information)
    - **Data Range**:
      - Annual data: D34:K37, L34:L37
      - Quarterly data: N34:AW37
      - Monthly data: AY34:FB37
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Product Mix percentages for each segment.
- **Notes & Customizations**: Total ARR is in column L, scaled by 1000. There are three time series horizons: annual, quarterly, and monthly.

### ARR Rollforward by Segment
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section shows the ARR rollforward for Corporate, Commercial, and Enterprise segments. It breaks down the changes in ARR from the beginning of the period to the end, including Initial Sale, Expansion, Downgrade, and Churn.
- **Cell Range**: A41:FB71
- **Layout Structure**:
    - **Row Headers Location**: Column C and Column A (e.g., "Corporate", "BOP ARR", "Initial Sale", "Expansion", "Downgrade", "Churn", "EOP ARR", "Commercial", "Enterprise", "Total")
    - **Column Headers Location**: Rows 2 and 5 (containing date information)
    - **Data Range**:
      - Annual data: D42:L47, D50:L55, D58:L63, D66:L71
      - Quarterly data: N42:AW47, N50:AW55, N58:AW63, N66:AW71
      - Monthly data: AY42:FB47, AY50:FB55, AY58:FB63, AY66:FB71
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: BOP ARR, Initial Sale, Expansion, Downgrade, Churn, EOP ARR.
- **Notes & Customizations**: ARR values are scaled by 1000. There are three time series horizons: annual, quarterly, and monthly.

### Mix Percentages by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the mix percentages for Corporate, Commercial, and Enterprise segments. It breaks down the percentage of Initial Sale, Expansion, Downgrade, and Churn.
- **Cell Range**: C73:FB97
- **Layout Structure**:
    - **Row Headers Location**: Column C (e.g., "Corporate Mix", "Initial Sale (%)", "Expansion (%)", "Downgrade (%)", "Churn (%)")
    - **Column Headers Location**: Rows 2 and 5 (containing date information)
    - **Data Range**:
      - Annual data: D76:L79, D82:L85, D88:L91, D94:L97
      - Quarterly data: N76:AW79, N82:AW85, N88:AW91, N94:AW97
      - Monthly data: AY76:FB79, AY82:FB85, AY88:FB91, AY94:FB97
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Initial Sale (%), Expansion (%), Downgrade (%), Churn (%).
- **Notes & Customizations**: There are three time series horizons: annual, quarterly, and monthly.

### ARR Rollforward ($) by Segment
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section shows the ARR rollforward in dollars for Corporate, Commercial, and Enterprise segments. It breaks down the changes in ARR from the beginning of the period to the end, including Initial Sale, Expansion, Downgrade, and Churn.
- **Cell Range**: C99:FB293
- **Layout Structure**:
    - **Row Headers Location**: Column C and Column A (e.g., "Initial Sale ($)", "Expansion ($)", "Downgrade ($)", "Churn ($)", "Starting ARR", "Net ARR", "Ending ARR", "Ending ARR (%)")
    - **Column Headers Location**: Rows 2 and 5 (containing date information)
    - **Data Range**:
      - Annual data: D99:L103, D105:L109, D111:L115, D117:L121, D123:L127, D129:L133, D135:L139, D141:L145, D150:L153, D156:L159, D162:L165, D168:L171, D173:L177, D179:L183, D185:L189, D191:L195, D197:L201, D203:L207, D209:L213, D215:L219, D224:L227, D230:L233, D236:L239, D242:L245, D247:L251, D253:L257, D259:L263, D265:L269, D271:L275, D277:L281, D283:L287, D289:L293
      - Quarterly data: N99:AW103, N105:AW109, N111:AW115, N117:AW121, N123:AW127, N129:AW133, N135:AW139, N141:AW145, N150:AW153, N156:AW159, N162:AW165, N168:AW171, N173:AW177, N179:AW183, N185:AW189, N191:AW195, N197:AW201, N203:AW207, N209:AW213, N215:AW219, N224:AW227, N230:AW233, N236:AW239, N242:AW245, N247:AW251, N253:AW257, N259:AW263, N265:AW269, N271:AW275, N277:AW281, N283:AW287, N289:AW293
      - Monthly data: AY99:FB103, AY105:FB109, AY111:FB115, AY117:FB121, AY123:FB127, AY129:FB133, AY135:FB139, AY141:FB145, AY150:FB153, AY156:FB159, AY162:FB165, AY168:FB171, AY173:FB177, AY179:FB183, AY185:FB189, AY191:FB195, AY197:FB201, AY203:FB207, AY209:FB213, AY215:FB219, AY224:FB227, AY230:FB233, AY236:FB239, AY242:FB245, AY247:FB251, AY253:FB257, AY259:FB263, AY265:FB269, AY271:FB275, AY277:FB281, AY283:FB287, AY289:FB293
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Initial Sale ($), Expansion ($), Downgrade ($), Churn ($), Starting ARR, Net ARR, Ending ARR.
- **Notes & Customizations**: ARR values are scaled by 1000. There are three time series horizons: annual, quarterly, and monthly.


====================================================================================================
# SHEET 21: Geo
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Geo
- **Key Sections Identified**:
    - Bookings by Geography and Product
    - YoY Bookings Growth
    - % Total Bookings
    - Channel Bookings
    - % Channel
    - Bookings by Segment (AMER, EMEA, APAC)

## 2. Detailed Section Analysis

### Bookings by Geography and Product
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the Gross Bookings data, broken down by geography (AMER, EMEA, APAC) and product. It provides a view of the company's sales performance across different regions and product lines.
- **Cell Range**: C9:FB12
- **Layout Structure**:
    - **Row Headers Location**: C9:C12
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D9:L12
      - Quarterly data: N9:AW12
      - Monthly data: AY9:FB12
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Gross Bookings, AMER, EMEA, APAC
- **Notes & Customizations**: Bookings data is scaled by 1000.

### YoY Bookings Growth
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the Year-over-Year (YoY) growth rate of bookings, providing insight into the growth trajectory of the business.
- **Cell Range**: C14:FB17
- **Layout Structure**:
    - **Row Headers Location**: C14
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: E14:L17
      - Quarterly data: R14:AW17
      - Monthly data: BK14:FB17
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: YoY Bookings Growth
- **Notes & Customizations**: There are some gaps in the monthly data for YoY Bookings Growth.

### % Total Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the percentage of total bookings for each geography, allowing for a comparison of regional contributions to overall sales.
- **Cell Range**: C19:FB22
- **Layout Structure**:
    - **Row Headers Location**: C19
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D20:L22
      - Quarterly data: N20:AW22
      - Monthly data: AY20:FB22
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: % Total Bookings, AMER, EMEA, APAC
- **Notes & Customizations**: None

### Channel Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the Gross Bookings data for Channel, broken down by geography (AMER, EMEA, APAC).
- **Cell Range**: C24:FB27
- **Layout Structure**:
    - **Row Headers Location**: C24
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D25:L27
      - Quarterly data: N25:AW27
      - Monthly data: AY25:FB27
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: $ Channel, AMER, EMEA, APAC
- **Notes & Customizations**: Bookings data is scaled by 1000.

### % Channel
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the percentage of Channel bookings for each geography, allowing for a comparison of regional contributions to overall sales.
- **Cell Range**: C29:FB32
- **Layout Structure**:
    - **Row Headers Location**: C29
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D30:L32
      - Quarterly data: N30:AW32
      - Monthly data: AY30:FB32
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: % Channel, AMER, EMEA, APAC
- **Notes & Customizations**: None

### Bookings by Segment (AMER, EMEA, APAC)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the Gross Bookings data, broken down by segments (Corporate, Commercial, Enterprise) for each geography (AMER, EMEA, APAC). It provides a view of the company's sales performance across different customer segments.
- **Cell Range**: C34:FB57
- **Layout Structure**:
    - **Row Headers Location**: C34:C37, C40:C42, C45:C47, C50:C52, C55:C57
    - **Column Headers Location**: D5:L5, N5:AW5, AY5:FB5
    - **Data Range**:
      - Annual data: D35:L37, D40:L42, D45:L47, D50:L52, D55:L57
      - Quarterly data: N35:AW37, N40:AW42, N45:AW47, N50:AW52, N55:AW57
      - Monthly data: AY35:FB37, AY40:FB42, AY45:FB47, AY50:FB52, AY55:FB57
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Gross Bookings, Corporate, Commercial, Enterprise, AMER Segments, EMEA Segments, APAC Segments
- **Notes & Customizations**: Bookings data is scaled by 1000.



====================================================================================================
# SHEET 22: Pendo - Balance Sheet
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Pendo - Balance Sheet
- **Key Sections Identified**:
    - Header
    - Balance Sheet

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, reporting book, and as-of date. Provides context for the entire spreadsheet.
- **Cell Range**: A1:F4
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: None
    - **Data Range**: F3:F4
- **Time Series Details**: None
- **Key Components**: Pendo.io Inc., Pendo - Consolidated Balance Sheet TTM (in USD), Reporting Book, CONS-USD, As of Date, 10/31/2019
- **Notes & Customizations**: None

### Balance Sheet
- **Section Type**: Balance Sheet
- **Description & Purpose**: Presents the company's assets, liabilities, and equity at a specific point in time (TTM - Trailing Twelve Months).
- **Cell Range**: A6:AR62
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 6, Row 7
    - **Data Range**:
      - Annual data: B12:D62 (values for 2019, 2020, 2021)
      - Monthly data: F12:AR62 (values for months from 02/28/2018 to 04/30/2021)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2021
      - Monthly: 02/28/2018 to 04/30/2021
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Assets, Current Assets, Cash and Cash Equivalents, Short Term Investments, Total Accounts Receivable, Net, Prepaid Expenses, Other Current Assets, Total Current Assets, Fixed Assets, Net, Intangible Assets, Net, Other Assets, Total Assets, Liabilities and Equity, Current Liabilities, Other Liabilities, Stockholders Equity, Total Liabilities and Equity.
- **Notes & Customizations**: Values are scaled by 1000. The sheet presents both a trailing twelve-month view (monthly) and a summary of the last three years (annual).


====================================================================================================
# SHEET 23: Product Mix
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Product Mix
- **Key Sections Identified**:
    - Product Mix - Budget vs Actual/Forecast
    - Team Performance - Budget vs Actual/Forecast
    - Level Four Grouping - Inferred ARR

## 2. Detailed Section Analysis

### Product Mix - Budget vs Actual/Forecast
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section compares budgeted and actual/forecasted performance for different product lines. It provides a view of product performance against targets.
- **Cell Range**: A3:W11
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Budget: `C5:G11`
      - Actual/Forecast: `I5:M11`
      - EOY FY23: `P5:P11`
      - S4:W11
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: Q1 to Q4 (Implied for FY22)
    - **Frequency**: Quarterly
- **Key Components**: Core, Mobile, VoC, DAP, Adopt, BD/MS, Total
- **Notes & Customizations**: Values are in millions except for column N and Q. There are two separate sections for Budget and Actual/Forecast.

### Team Performance - Budget vs Actual/Forecast
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section compares budgeted and actual/forecasted performance for different teams. It provides a view of team performance against targets.
- **Cell Range**: A15:Z27
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 15
    - **Data Range**:
      - Budget: `C17:G27`
      - Actual/Forecast: `I17:M27`
      - EOY FY23: `P17:P27`
      - Y18:Z23
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: Q1 to Q4 (Implied for FY22)
    - **Frequency**: Quarterly
- **Key Components**: Team, Corp, Comm, Enterprise, EMEA, Adopt, Sub Success, DAP, Japan, ANZ, BD/MS/Partner
- **Notes & Customizations**: Values are in millions except for column N and Q. There are two separate sections for Budget and Actual/Forecast. Columns X, Y, and Z contain additional forecast data.

### Level Four Grouping - Inferred ARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the inferred ARR (Annual Recurring Revenue) for different Level Four Groupings.
- **Cell Range**: A39:I54
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 39
    - **Data Range**: `B41:I54`
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: FY2021-Q3 to FY2022-Q3
    - **Frequency**: Quarterly
- **Key Components**: Level Four Grouping, Digital Adoption, Feedback, Guidance, Insights, Integration, Other, TAM/Support, Mobile, Web, Non Platform ARR
- **Notes & Customizations**: Values are in thousands.



====================================================================================================
# SHEET 24: ASC606
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: ASC606
- **Key Sections Identified**:
    - Revenue and Commission Calculation
    - 3 Year Depreciation Schedule
    - 5 Year Depreciation Schedule

## 2. Detailed Section Analysis

### Revenue and Commission Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates capitalized commissions and their amortization based on gross bookings and commission rates. It also includes ASC 606 adjustments and a check calculation.
- **Cell Range**: C7:FB16
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data (Actuals): D9:L11, D14:L15
      - Quarterly data (Forecast): N9:AW11, N15:AW15
      - Monthly data: AY9:FB11, AY13:FB15
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: Products, Gross Bookings, Commission Rate, Capitalized Commissions, Amortization, ASC 606 Adjustment, CHECK
- **Notes & Customizations**: The section includes a "CHECK" row, likely for validation purposes. Data is presented in thousands.

### 3 Year Depreciation Schedule
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section calculates the depreciation expense over a 3-year period based on the "Amount to Amortize". It shows the monthly depreciation expense.
- **Cell Range**: C24:FB61
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data: D25:L61
      - Quarterly data: N25:AW61
      - Monthly data: BK25:FB61
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: 3 Year Depreciation, Month 1 to Month 36, 36 mo Amortization
- **Notes & Customizations**: Data is presented in thousands.

### 5 Year Depreciation Schedule
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section calculates the depreciation expense over a 5-year period. It shows the monthly depreciation expense.
- **Cell Range**: C65:FB126
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data: D66:L126
      - Quarterly data: N66:AW126
      - Monthly data: CI66:FB126
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Quarterly: Q1 2019 to Q4 2027
      - Monthly: 2018-02 to 2027-01
    - **Frequency**:
      - Annual
      - Quarterly
      - Monthly
- **Key Components**: 5 Year Depreciation, Month 1 to Month 60, 60 mo Amortization
- **Notes & Customizations**: Data is presented in thousands.


====================================================================================================
# SHEET 25: Expense Details
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Expense Details
- **Key Sections Identified**:
    - COGS Section
    - Operating Expenses Section
    - Detailed Expense Breakdown

## 2. Detailed Section Analysis

### Section Name: COGS Section
- **Section Type**: Standard P&L
- **Description & Purpose**: This section outlines the Cost of Goods Sold (COGS), providing a breakdown of expenses directly related to the production and delivery of goods/services. It's used to calculate Gross Profit.
- **Cell Range**: A4:BC10
- **Layout Structure**:
    - **Row Headers Location**: A4:G10
    - **Column Headers Location**: H2:BC2
    - **Data Range**:
      - Monthly data: H4:BC6, H8:BC8
- **Time Series Details**:
    - **Date Range**: 2019-01-01 to 2022-12-01
    - **Frequency**: Monthly
- **Key Components**: COGSHosting, COGSPS, COGSCS, Total COGS
- **Notes & Customizations**: The values are scaled by 1000.

### Section Name: Operating Expenses Section
- **Section Type**: Standard P&L
- **Description & Purpose**: This section details the operating expenses of the business, which are the costs incurred to keep the business running.
- **Cell Range**: A11:BC60
- **Layout Structure**:
    - **Row Headers Location**: A11:G60
    - **Column Headers Location**: H2:BC2
    - **Data Range**:
      - Monthly data: H11:BC12, H15:BC17, H20:BC22, H25:BC26, H28:BC29, H31:BC31, H35:BC36, H39:BC40, H42:BC42, H46:BC49, H52:BC53, H55:BC55, H58:BC60
- **Time Series Details**:
    - **Date Range**: 2019-01-01 to 2022-12-01
    - **Frequency**: Monthly
- **Key Components**: SalesHC, SalesOther, MarketingHC, MarketingDiscretionary, MarketingOther, CS/PSHC, CS/PSOther, CS/PSAllocation, SalesOpsHC, SalesOpsOther, ProductHC, ProductOther, EngineeringHC, EngineeringOther, G&AHC, Rent, Legal, PeopleHC, PeopleOther, Total Operating Expenses, Total Expenses, CHECK
- **Notes & Customizations**: The values are scaled by 1000.

### Section Name: Detailed Expense Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: This section provides a detailed breakdown of various expense categories, offering a granular view of where money is being spent.
- **Cell Range**: A66:BC287
- **Layout Structure**:
    - **Row Headers Location**: A67:G287
    - **Column Headers Location**: H66:BC66
    - **Data Range**:
      - Monthly data: H69:BC287
- **Time Series Details**:
    - **Date Range**: 2019-01-01 to 2022-12-01
    - **Frequency**: Monthly
- **Key Components**: Hosting, Sales & Marketing , R&D & Product, Customer Success, Professional Services, G&A, HR , Marketing, Sales , Sales Enablement, Strategic Accounts Sales, BusDev, R&D EXPENSES, Financial Expenses.
- **Notes & Customizations**: The values are scaled by 1000. This section includes P&L codes, sub-departments, and Intacct GL codes for detailed tracking.


====================================================================================================
# SHEET 26: ARR Looker
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: ARR Looker
- **Key Sections Identified**:
    - Header
    - Quarterly ARR Data by Segment

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains labels for the data table, including segment names and date labels.
- **Cell Range**: A1:Q2
- **Layout Structure**:
    - **Row Headers Location**: A2, C2
    - **Column Headers Location**: C1, E1:I1, N1:Q1, D2:J2, O2:Q2
    - **Data Range**: None (Header only)
- **Time Series Details**:
    - **Date Range**: FY2017-Q4 to FY2022-Q3
    - **Frequency**: Quarterly
- **Key Components**: Segment, Date Fiscal Quarter, Total ARR, Churn, Downgrade, Expansion, Initial Sale, Partner, Corporate, Commercial, Strategic
- **Notes & Customizations**: The header defines the structure of the ARR data table below.

### Quarterly ARR Data by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains the quarterly ARR data broken down by segment (Corporate, Commercial, Strategic) and by closed transaction type.
- **Cell Range**: A3:Q177
- **Layout Structure**:
    - **Row Headers Location**: A3:A177
    - **Column Headers Location**: B2:Q2, C1:I1
    - **Data Range**:
      - Quarterly data (Segment): E3:I10, E12:I19, D20:I28, D29:I37, D38:I46, D47:I55, D56:I64, D65:I73, D74:I82, D83:I91, D92:I100, D101:I109, D110:I118, D119:I127, D128:I136, D137:I145, D146:I154, D155:I163, D164:I172, D173:I177
      - Quarterly data (Corporate/Commercial/Strategic): O3:Q10, O3:Q10, O3:Q10, O3:Q10, O3:Q10, O3:Q10, O3:Q10, O3:Q10
- **Time Series Details**:
    - **Date Range**: FY2017-Q4 to FY2022-Q3
    - **Frequency**: Quarterly
- **Key Components**: FY2017-Q4, FY2018-Q1, FY2018-Q2, FY2018-Q3, FY2018-Q4, FY2019-Q1, FY2019-Q2, FY2019-Q3, FY2019-Q4, FY2020-Q1, FY2020-Q2, FY2020-Q3, FY2020-Q4, FY2021-Q1, FY2021-Q2, FY2021-Q3, FY2021-Q4, FY2022-Q1, FY2022-Q2, FY2022-Q3, Corporate, Commercial, Strategic, Churn, Downgrade, Expansion, Initial Sale, Partner
- **Notes & Customizations**: Data is scaled by 1000. There are two distinct sections of data: one for the combined segments (Corporate, Commercial, Strategic) and another for the individual segments.



====================================================================================================
# SHEET 27: Prod Looker
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Prod Looker
- **Key Sections Identified**:
    - Header
    - Data Table

## 2. Detailed Section Analysis

### Header
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the column headers for the data table. It specifies the type of data contained in each column.
- **Cell Range**: B1:G1
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B1:G1
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Close Fiscal Quarter, Close Month, Segment, Level Four Grouping, Transaction Type, Inferred ARR
- **Notes & Customizations**: None

### Data Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains the core data, showing various metrics broken down by different segments and time periods. It appears to be focused on ARR (Annual Recurring Revenue) analysis.
- **Cell Range**: A2:Y501
- **Layout Structure**:
    - **Row Headers Location**: A2:A501
    - **Column Headers Location**: B1:Y1
    - **Data Range**:
      - Monthly data: C2:C501 (Close Month)
      - Quarterly data: M2:Y501 (FY2021-Q3, FY2021-Q4, FY2022-Q1, FY2022-Q2, FY2022-Q3)
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2020-08-01 to 2021-09-01
      - Quarterly: FY2021-Q3 to FY2022-Q3
    - **Frequency**:
      - Monthly
      - Quarterly
- **Key Components**: Close Fiscal Quarter, Close Month, Segment, Level Four Grouping, Transaction Type, Inferred ARR
- **Notes & Customizations**: The "Inferred ARR" column (G) has values scaled by 1000. Columns M:Y contain quarterly data, while column C contains monthly data. Some rows contain the string "DA" in column I, and "Total", "Per ARR", "Variance" in column L.


====================================================================================================
# SHEET 28: Region Looker
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Region Looker
- **Key Sections Identified**:
    - Initial Sale Bookings by Region (Monthly)
    - Expansion Bookings by Region (Monthly)
    - Total Gross Bookings (Monthly)
    - Total per ARR (Monthly)
    - Bookings Summary by Region

## 2. Detailed Section Analysis

### Initial Sale Bookings by Region (Monthly)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the initial sale bookings, broken down by region, for each month. It allows for tracking initial sales performance across different geographic areas.
- **Cell Range**: A4:CG12
- **Layout Structure**:
    - **Row Headers Location**: A6:A11
    - **Column Headers Location**: B5:CG6
    - **Data Range**:
      - Monthly data: B7:CG11
- **Time Series Details**:
    - **Date Range**: 2014-11-01 to 2021-07-01
    - **Frequency**: Monthly
- **Key Components**: APAC, EMEA, LATAM, North America, (blank), Grand Total, Nov, Dec, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct
- **Notes & Customizations**: The data is scaled by 1000.

### Expansion Bookings by Region (Monthly)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the expansion bookings, broken down by region, for each month. It allows for tracking expansion sales performance across different geographic areas.
- **Cell Range**: A15:CG25
- **Layout Structure**:
    - **Row Headers Location**: A17:A24
    - **Column Headers Location**: B18:CG19
    - **Data Range**:
      - Monthly data: B20:CG24
- **Time Series Details**:
    - **Date Range**: 2014-11-01 to 2021-07-01
    - **Frequency**: Monthly
- **Key Components**: APAC, EMEA, LATAM, North America, (blank), Grand Total, Nov, Dec, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct
- **Notes & Customizations**: The data is scaled by 1000.

### Total Gross Bookings (Monthly)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the total gross bookings over time.
- **Cell Range**: A28:CD34
- **Layout Structure**:
    - **Row Headers Location**: A32:A33
    - **Column Headers Location**: B30
    - **Data Range**:
      - Monthly data: B31:CD34
- **Time Series Details**:
    - **Date Range**: 2014-11-01 to 2021-07-01
    - **Frequency**: Monthly
- **Key Components**: AMER, APAC, EMEA
- **Notes & Customizations**: The data is scaled by 1000.

### Total per ARR (Monthly)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the total per ARR over time.
- **Cell Range**: A36:CJ43
- **Layout Structure**:
    - **Row Headers Location**: A40:A42
    - **Column Headers Location**: AO39
    - **Data Range**:
      - Monthly data: AO40:CJ43
- **Time Series Details**:
    - **Date Range**: 2018-02-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: AMER, APAC, EMEA
- **Notes & Customizations**: The data is scaled by 1000.

### Bookings Summary by Region
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of various booking metrics (Initial Sale, Expansion, Downgrade, Churn, Partner) by region.
- **Cell Range**: A45:J53
- **Layout Structure**:
    - **Row Headers Location**: A47:A53
    - **Column Headers Location**: B45
    - **Data Range**: B48:J53
- **Time Series Details**:
    - No time series detected.
- **Key Components**: Sum of Initial Sale, Sum of Expansion, Sum of Downgrade, Sum of Churn, Sum of Partner, APAC, EMEA, LATAM, North America, (blank), Grand Total
- **Notes & Customizations**: The data is scaled by 1000.



====================================================================================================
# SHEET 29: 22 Fcst ARR
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: 22 Fcst ARR
- **Key Sections Identified**:
    - ARR Forecast by Customer Segment
    - ARR Forecast by Customer Sub-Segment
    - ARR Adjustment Details
    - Downgrade Analysis

## 2. Detailed Section Analysis

### Section Name: ARR Forecast by Customer Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides the forecasted ARR (Annual Recurring Revenue) broken down by major customer segments: Corporate, Commercial, and Enterprise. It shows the progression of ARR over time for each segment, allowing for tracking and analysis of segment performance.
- **Cell Range**: B2:H12
- **Layout Structure**:
    - **Row Headers Location**: B2:B12
    - **Column Headers Location**: C1:H1
    - **Data Range**:
        - Monthly data: C3:H12
- **Time Series Details**:
    - **Date Range**: 2021-08-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Corporate, Commercial, Enterprise, Initial Sale, Expansion, Downgrade, Churn, Target, Adjustment
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: ARR Forecast by Customer Sub-Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a more granular view of the ARR forecast, breaking down the major customer segments into sub-segments. This allows for a deeper understanding of the drivers of ARR growth or decline within each segment.
- **Cell Range**: B23:AF40
- **Layout Structure**:
    - **Row Headers Location**: B23:B40, Z23:Z40, Q40
    - **Column Headers Location**: C22:H22, R34:W34
    - **Data Range**:
        - Monthly data: C24:H40
        - Monthly data: AA24:AF40
        - Monthly data: R35:W40
- **Time Series Details**:
    - **Date Range**: 2021-08-01 to 2022-01-01
    - **Frequency**: Monthly
- **Time Series Details**:
    - **Date Range**: 2021-08-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: New Customer, Corporate, Commercial, Sr. Commercial, Enterprise, Adopt, Other
- **Notes & Customizations**: Values are scaled by 1000. There are multiple time series in this section.

### Section Name: ARR Adjustment Details
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides details on adjustments made to the ARR forecast. It includes specific adjustments related to Commercial AEs and other factors, allowing for transparency and understanding of forecast modifications.
- **Cell Range**: B42:W55
- **Layout Structure**:
    - **Row Headers Location**: B42:B55
    - **Column Headers Location**: R34:W34
    - **Data Range**:
        - Monthly data: R41:W50
        - Monthly data: C43:H48
        - Monthly data: C52:H55
- **Time Series Details**:
    - **Date Range**: 2021-08-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Churn, Corporate, Commercial, Sr. Commercial, Enterprise, Adopt, Other, Total Adj
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Downgrade Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes downgrade percentages for different customer segments. It provides insights into the rate at which customers are downgrading their subscriptions, which is a key indicator of customer satisfaction and potential churn risk.
- **Cell Range**: B58:F69
- **Layout Structure**:
    - **Row Headers Location**: B58:B62, B65:B69, C66, D66, E66, F66
    - **Column Headers Location**: None
    - **Data Range**: C67:E69, F67:F69
- **Time Series Details**: No explicit time series.
- **Key Components**: Churn, Corporate, Commercial, Sr. Commercial, Enterprise, Downgrade % Total Churn - L4Q, Downgrade %
- **Notes & Customizations**: Values are scaled by 1000 for C67:E69.



====================================================================================================
# SHEET 30: Historical P&L Adj
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Historical P&L Adj
- **Key Sections Identified**:
    - ASC 606 Adjustment - Quarterly
    - ASC 606 Adjustment - Monthly
    - Cash Burn - Quarterly
    - Cash Burn - Monthly (Implied, overlapping with Quarterly)
    - Fix - Quarterly

## 2. Detailed Section Analysis

### Section Name: ASC 606 Adjustment - Quarterly
- **Section Type**: Custom P&L
- **Description & Purpose**: This section shows the quarterly ASC 606 adjustments, likely impacting revenue recognition. It's used to reconcile financial statements under the ASC 606 accounting standard.
- **Cell Range**: B5:V9
- **Layout Structure**:
    - **Row Headers Location**: B5
    - **Column Headers Location**: C4:V4
    - **Data Range**: C5:V5, C9:V9
- **Time Series Details**:
    - **Date Range**: Q1 FY19 to Q4 FY23 (C4:V4)
    - **Frequency**: Quarterly
- **Key Components**: ASC 606 Adjustment - Quarterly (B5)
- **Notes & Customizations**: Values are in thousands.

### Section Name: ASC 606 Adjustment - Monthly
- **Section Type**: Custom P&L
- **Description & Purpose**: This section shows the monthly ASC 606 adjustments, likely impacting revenue recognition. It's used to reconcile financial statements under the ASC 606 accounting standard.
- **Cell Range**: B10:BJ10
- **Layout Structure**:
    - **Row Headers Location**: B10
    - **Column Headers Location**: C9:BJ9
    - **Data Range**: C10:BJ10
- **Time Series Details**:
    - **Date Range**: 2018-02-01 to 2023-01-01
    - **Frequency**: Monthly
- **Key Components**: ASC 606 Adjustment - Monthly (B10)
- **Notes & Customizations**: Values are in thousands.

### Section Name: Cash Burn - Quarterly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the quarterly cash burn metrics, providing insights into the company's cash flow and spending.
- **Cell Range**: B13:F23
- **Layout Structure**:
    - **Row Headers Location**: B16:B20
    - **Column Headers Location**: C15:F15
    - **Data Range**: C16:F20, C23:F23
- **Time Series Details**:
    - **Date Range**: Q1 FY23 to Q4 FY23
    - **Frequency**: Quarterly
- **Key Components**: Cash BOP, Incoming Cash, Total Expenses, Equity, Cash EOP.
- **Notes & Customizations**: Values are in thousands. Only covers FY23.

### Section Name: Cash Burn - Monthly (Implied)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the monthly cash burn metrics, providing insights into the company's cash flow and spending.
- **Cell Range**: B25:N30
- **Layout Structure**:
    - **Row Headers Location**: B26:B30
    - **Column Headers Location**: C25:N25
    - **Data Range**: C26:N30
- **Time Series Details**:
    - **Date Range**: 2022-02-01 to 2023-01-01
    - **Frequency**: Monthly
- **Key Components**: Cash BOP, Incoming Cash, Total Expenses, Equity, Cash EOP.
- **Notes & Customizations**: Values are in thousands.

### Section Name: Cash Burn - Monthly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the monthly cash burn metrics, providing insights into the company's cash flow and spending.
- **Cell Range**: B38:AX57
- **Layout Structure**:
    - **Row Headers Location**: B39:B44, B47, B52:B57
    - **Column Headers Location**: C38:AX38, C51:AX51
    - **Data Range**: C39:AX44, C47:AX47, C52:AX57
- **Time Series Details**:
    - **Date Range**: 2018-02-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Cash BOP, Incoming Cash, Total Expenses, Other Non-Recurring, Equity, Cash EOP, Hedge.
- **Notes & Customizations**: Values are in thousands.

### Section Name: Fix - Quarterly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the quarterly "Fix" metrics, providing insights into the company's cash flow and spending.
- **Cell Range**: AR63:AV77
- **Layout Structure**:
    - **Row Headers Location**: AR66:AR69, AR73:AR77
    - **Column Headers Location**: AS65:AT65, AS72:AT72
    - **Data Range**: AS66:AT69, AV69, AS73:AT77, AV76
- **Time Series Details**:
    - **Date Range**: Q3 FYXX, Q4 FYXX (where XX is not specified, but implied to be the same year)
    - **Frequency**: Quarterly
- **Key Components**: Incoming Cash, Total Expenses, Other Non-Recurring, Equity.
- **Notes & Customizations**: Values are in thousands.


====================================================================================================
# SHEET 31: Products - Old
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Products - Old
- **Key Sections Identified**:
    - ARR Summary
    - Product ARR and Bookings
    - Churn Analysis
    - Ending ARR by Product
    - Ending ARR Growth Rate

## 2. Detailed Section Analysis

### ARR Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the overall ARR (Annual Recurring Revenue) performance, including beginning ARR, acquisitions, new customer ARR, expansion ARR, churn, and ending ARR. It provides a high-level overview of the company's revenue growth.
- **Cell Range**: B4:J9
- **Layout Structure**:
    - **Row Headers Location**: B4:B9
    - **Column Headers Location**: C2:J2
    - **Data Range**: C4:J9
- **Time Series Details**:
    - **Date Range**: 2019 to 2026
    - **Frequency**: Annual
- **Key Components**: BOP ARR, Acquisitions, New Customer ARR, Expansion ARR, Churn, EOP ARR.
- **Notes & Customizations**: Values are scaled by 1000.

### Product ARR and Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down ARR and Gross Bookings by product (Core, Mobile, VoC, DAP, Adopt). It allows for analysis of individual product performance and contribution to overall revenue.
- **Cell Range**: B11:J23
- **Layout Structure**:
    - **Row Headers Location**: B12:B17, C19, C22
    - **Column Headers Location**: E11:J11, C2:J2
    - **Data Range**: E13:J17, E19:J23
- **Time Series Details**:
    - **Date Range**: 2019 to 2026
    - **Frequency**: Annual
- **Key Components**: Product, ARR, Gross Bookings, Core, Mobile, VoC, DAP, Adopt, Engage, DA.
- **Notes & Customizations**: Values are scaled by 1000 for ARR and Gross Bookings.

### Churn Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes churn by product.
- **Cell Range**: B26:J31
- **Layout Structure**:
    - **Row Headers Location**: B26
    - **Column Headers Location**: C2:J2
    - **Data Range**: F26:J31
- **Time Series Details**:
    - **Date Range**: 2019 to 2026
    - **Frequency**: Annual
- **Key Components**: Starting ARR, Core, Mobile, VoC, DAP, Adopt
- **Notes & Customizations**: Values are scaled by 1000.

### Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes bookings by product.
- **Cell Range**: B33:J38
- **Layout Structure**:
    - **Row Headers Location**: B33
    - **Column Headers Location**: C2:J2
    - **Data Range**: F33:J38
- **Time Series Details**:
    - **Date Range**: 2019 to 2026
    - **Frequency**: Annual
- **Key Components**: Bookings, Core, Mobile, VoC, DAP, Adopt
- **Notes & Customizations**: Values are scaled by 1000.

### Churn
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes churn by product.
- **Cell Range**: B40:J45
- **Layout Structure**:
    - **Row Headers Location**: B40
    - **Column Headers Location**: C2:J2
    - **Data Range**: F40:J45
- **Time Series Details**:
    - **Date Range**: 2019 to 2026
    - **Frequency**: Annual
- **Key Components**: Churn, Core, Mobile, VoC, DAP, Adopt
- **Notes & Customizations**: Values are scaled by 1000.

### Ending ARR by Product
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the ending ARR for each product.
- **Cell Range**: D47:J54
- **Layout Structure**:
    - **Row Headers Location**: D49
    - **Column Headers Location**: E47:J47
    - **Data Range**: E49:J54
- **Time Series Details**:
    - **Date Range**: 2021 to 2026
    - **Frequency**: Annual
- **Key Components**: Ending ARR, Core, Mobile, VoC, DAP, Adopt
- **Notes & Customizations**: Values are scaled by 1000.

### Ending ARR Growth Rate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the ending ARR growth rate for each product.
- **Cell Range**: D56:J61
- **Layout Structure**:
    - **Row Headers Location**: D56
    - **Column Headers Location**: E47:J47
    - **Data Range**: E56:J61
- **Time Series Details**:
    - **Date Range**: 2021 to 2026
    - **Frequency**: Annual
- **Key Components**: Ending ARR (%), Core, Mobile, VoC, DAP, Adopt
- **Notes & Customizations**: Values are percentages.
