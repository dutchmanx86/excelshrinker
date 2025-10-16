# Master Workbook Analysis

This document provides a comprehensive analysis of all sheets in the Excel workbook.

---

## Table of Contents

1. [Summary](#summary)
   - [Change Log](#summary-change-log)
   - [Key Metrics - Monthly](#summary-key-metrics---monthly)
   - [Key Metrics - Annual](#summary-key-metrics---annual)
2. [Master Ctrl](#master-ctrl)
   - [Header](#master-ctrl-header)
   - [Control Scenarios](#master-ctrl-control-scenarios)
   - [Global Assumptions](#master-ctrl-global-assumptions)
   - [Productivity & Margin Cases](#master-ctrl-productivity-&-margin-cases)
3. [Dash Control](#dash-control)
   - [Section Name: Header](#dash-control-section-name-header)
   - [Section Name: Dashboard Control Parameters](#dash-control-section-name-dashboard-control-parameters)
4. [Dash](#dash)
   - [Income Statement Metrics](#dash-income-statement-metrics)
   - [ARR Summary](#dash-arr-summary)
   - [Bookings](#dash-bookings)
   - [Segment Summary](#dash-segment-summary)
   - [Headcount Summary](#dash-headcount-summary)
   - [Client & Subscriber Counts](#dash-client-&-subscriber-counts)
   - [Retention Metrics](#dash-retention-metrics)
   - [Key Performance Indicators Summary](#dash-key-performance-indicators-summary)
   - [Key Performance Indicators Detail](#dash-key-performance-indicators-detail)
   - [Key Performance Indicators by Segment](#dash-key-performance-indicators-by-segment)
   - [Debt Availability Build](#dash-debt-availability-build)
5. [CAC by Segment](#cac-by-segment)
   - [Summary Upsell Cost](#cac-by-segment-summary-upsell-cost)
   - [Summary CAC](#cac-by-segment-summary-cac)
   - [Summary Support Cost](#cac-by-segment-summary-support-cost)
   - [Detail Section](#cac-by-segment-detail-section)
   - [Adjusted Sales and Marketing Cost](#cac-by-segment-adjusted-sales-and-marketing-cost)
   - [Adjusted People Costs](#cac-by-segment-adjusted-people-costs)
   - [All-In Support Costs](#cac-by-segment-all-in-support-costs)
6. [Payback Period](#payback-period)
   - [Header](#payback-period-header)
   - [Payback Period - Total Company](#payback-period-payback-period---total-company)
   - [Cash Payback Calculation](#payback-period-cash-payback-calculation)
   - [Payback Period - Financial](#payback-period-payback-period---financial)
   - [Cash Payback Calculation - Financial](#payback-period-cash-payback-calculation---financial)
   - [Payback Period - Corporate](#payback-period-payback-period---corporate)
   - [Cash Payback Calculation - Corporate](#payback-period-cash-payback-calculation---corporate)
7. [Fin CTRL](#fin-ctrl)
   - [Section Name: Balance Sheet Support Assumptions](#fin-ctrl-section-name-balance-sheet-support-assumptions)
   - [Section Name: Interest Rate Assumptions](#fin-ctrl-section-name-interest-rate-assumptions)
   - [Section Name: Effective Commission Rate & Day Sales Outstanding](#fin-ctrl-section-name-effective-commission-rate-&-day-sales-outstanding)
8. [Fin](#fin)
   - [Income Statement](#fin-income-statement)
   - [Balance Sheet](#fin-balance-sheet)
   - [Cash Flow Statement](#fin-cash-flow-statement)
   - [Balance Sheet Support](#fin-balance-sheet-support)
   - [Long Term Liabilities](#fin-long-term-liabilities)
   - [Equity Investment](#fin-equity-investment)
   - [Income Statement Support - Income Taxes](#fin-income-statement-support---income-taxes)
9. [Debt Compliance](#debt-compliance)
   - [Revenue Growth Section](#debt-compliance-revenue-growth-section)
   - [Debt Compliance Check Section](#debt-compliance-debt-compliance-check-section)
   - [Liquidity Analysis Section](#debt-compliance-liquidity-analysis-section)
10. [ARR and Rev CTRL](#arr-and-rev-ctrl)
   - [Revenue by Segment and Scenario](#arr-and-rev-ctrl-revenue-by-segment-and-scenario)
   - [Quota by Role and Scenario](#arr-and-rev-ctrl-quota-by-role-and-scenario)
   - [Productivity Metrics](#arr-and-rev-ctrl-productivity-metrics)
   - [ARR Metrics](#arr-and-rev-ctrl-arr-metrics)
11. [Sales Prod Input](#sales-prod-input)
   - [Section Name: Input Parameters](#sales-prod-input-section-name-input-parameters)
   - [Section Name: Seasonality Adjustment](#sales-prod-input-section-name-seasonality-adjustment)
   - [Section Name: Productivity Calculation](#sales-prod-input-section-name-productivity-calculation)
12. [ARR and Revenue](#arr-and-revenue)
   - [Section Name: ARR Summary](#arr-and-revenue-section-name-arr-summary)
   - [Section Name: ARR by Segment](#arr-and-revenue-section-name-arr-by-segment)
   - [Section Name: Revenue by Segment](#arr-and-revenue-section-name-revenue-by-segment)
   - [Section Name: Revenue as % of MRR](#arr-and-revenue-section-name-revenue-as-%-of-mrr)
   - [Section Name: Sales Productivity](#arr-and-revenue-section-name-sales-productivity)
   - [Section Name: Total Bookings by Segment](#arr-and-revenue-section-name-total-bookings-by-segment)
   - [Section Name: New Bookings by Segment](#arr-and-revenue-section-name-new-bookings-by-segment)
   - [Section Name: Upsell by Segment](#arr-and-revenue-section-name-upsell-by-segment)
   - [Section Name: Financial ARR](#arr-and-revenue-section-name-financial-arr)
   - [Section Name: Corporate ARR](#arr-and-revenue-section-name-corporate-arr)
   - [Section Name: Other ARR](#arr-and-revenue-section-name-other-arr)
   - [Section Name: Combined](#arr-and-revenue-section-name-combined)
13. [Sales CTRL](#sales-ctrl)
   - [Header](#sales-ctrl-header)
   - [Quota Sales Reps Headcount](#sales-ctrl-quota-sales-reps-headcount)
   - [Account Manager Headcount](#sales-ctrl-account-manager-headcount)
   - [AE - Financial Headcount](#sales-ctrl-ae---financial-headcount)
   - [AE - Corporate Headcount](#sales-ctrl-ae---corporate-headcount)
   - [VP - Bus Dev Headcount](#sales-ctrl-vp---bus-dev-headcount)
   - [AE - Enterprise Headcount](#sales-ctrl-ae---enterprise-headcount)
   - [AE - Other Headcount](#sales-ctrl-ae---other-headcount)
   - [Other Sales - Headcount](#sales-ctrl-other-sales---headcount)
   - [Ratios and Metrics](#sales-ctrl-ratios-and-metrics)
   - [Old Assumptions (To Be Deleted)](#sales-ctrl-old-assumptions-to-be-deleted)
   - [Other Sales - Salary](#sales-ctrl-other-sales---salary)
14. [Sales Role Input](#sales-role-input)
   - [Section Name (Sales Role Input - Quota Bearing)](#sales-role-input-section-name-sales-role-input---quota-bearing)
   - [Section Name (Sales Role Input - Non-Quota (Non Formula))](#sales-role-input-section-name-sales-role-input---non-quota-non-formula)
   - [Section Name (Sales Role Input - Non-Quota (Formula))](#sales-role-input-section-name-sales-role-input---non-quota-formula)
15. [Sales Reps](#sales-reps)
   - [Header](#sales-reps-header)
   - [Quota Sales Rep Summary](#sales-reps-quota-sales-rep-summary)
   - [Non Quota'd Sales Team Summary](#sales-reps-non-quota'd-sales-team-summary)
   - [Quota Sales Rep Detail](#sales-reps-quota-sales-rep-detail)
   - [Other Sales Detail](#sales-reps-other-sales-detail)
   - [Total Sales Heads](#sales-reps-total-sales-heads)
   - [Quota Rep - Salary Summary](#sales-reps-quota-rep---salary-summary)
   - [Quota Rep - Bonus Summary](#sales-reps-quota-rep---bonus-summary)
   - [Quota Rep - Salary Detail](#sales-reps-quota-rep---salary-detail)
   - [Other Sales - Salary Detail](#sales-reps-other-sales---salary-detail)
16. [Clients CTRL](#clients-ctrl)
   - [Header](#clients-ctrl-header)
   - [Clients Control - Financial](#clients-ctrl-clients-control---financial)
   - [Clients Control - Corporate](#clients-ctrl-clients-control---corporate)
   - [Clients Control - Other](#clients-ctrl-clients-control---other)
17. [Clients](#clients)
   - [Header](#clients-header)
   - [Clients Summary](#clients-clients-summary)
   - [Clients Detail - Financial](#clients-clients-detail---financial)
   - [Client Detail - Corporate](#clients-client-detail---corporate)
   - [Client Detail - Other](#clients-client-detail---other)
18. [Retention CTRL](#retention-ctrl)
   - [Section Name: Header](#retention-ctrl-section-name-header)
   - [Section Name: Retention Rate Table - Base - $25mm](#retention-ctrl-section-name-retention-rate-table---base---$25mm)
   - [Section Name: Retention Rate Table - Growth - $25mm](#retention-ctrl-section-name-retention-rate-table---growth---$25mm)
   - [Section Name: Retention Rate Table - Base - $50mm](#retention-ctrl-section-name-retention-rate-table---base---$50mm)
   - [Section Name: Retention Rate Table - Base - $50mm (R&D)](#retention-ctrl-section-name-retention-rate-table---base---$50mm-r&d)
19. [Retention](#retention)
   - [Section Name: Retention Summary - Financial](#retention-section-name-retention-summary---financial)
   - [Section Name: Retention Detail - Financial](#retention-section-name-retention-detail---financial)
   - [Section Name: Retention Summary - Corporate](#retention-section-name-retention-summary---corporate)
   - [Section Name: Retention Detail - Other](#retention-section-name-retention-detail---other)
   - [Section Name: Summary](#retention-section-name-summary)
20. [Renewed](#renewed)
   - [Header](#renewed-header)
   - [Renewal Data](#renewed-renewal-data)
21. [Renewal Base](#renewal-base)
   - [Data Table](#renewal-base-data-table)
   - [Segment Key](#renewal-base-segment-key)
22. [Deferred Build](#deferred-build)
   - [Header](#deferred-build-header)
   - [Deferred Revenue Summary](#deferred-build-deferred-revenue-summary)
   - [Deferred Revenue Detail](#deferred-build-deferred-revenue-detail)
   - [Revenue Recognition Detail](#deferred-build-revenue-recognition-detail)
23. [Headcount and Salaries CTRL](#headcount-and-salaries-ctrl)
   - [Header](#headcount-and-salaries-ctrl-header)
   - [Headcount Summary](#headcount-and-salaries-ctrl-headcount-summary)
   - [ARR per Head Analysis](#headcount-and-salaries-ctrl-arr-per-head-analysis)
   - [Salary Analysis](#headcount-and-salaries-ctrl-salary-analysis)
24. [Headcount and Salaries](#headcount-and-salaries)
   - [Section Name: Headcount and Salaries Summary](#headcount-and-salaries-section-name-headcount-and-salaries-summary)
   - [Section Name: Memo: Average Headcount](#headcount-and-salaries-section-name-memo-average-headcount)
   - [Section Name: Salary](#headcount-and-salaries-section-name-salary)
   - [Section Name: Salary per Head](#headcount-and-salaries-section-name-salary-per-head)
   - [Section Name: Headcount Detail](#headcount-and-salaries-section-name-headcount-detail)
   - [Section Name: Salaries Detail](#headcount-and-salaries-section-name-salaries-detail)
25. [Opex CTRL](#opex-ctrl)
   - [Header](#opex-ctrl-header)
   - [Operating Expenses Inputs](#opex-ctrl-operating-expenses-inputs)
26. [Operating Expenses](#operating-expenses)
   - [Operating Expenses Summary](#operating-expenses-operating-expenses-summary)
   - [Operating Expenses Detail - People Costs](#operating-expenses-operating-expenses-detail---people-costs)
   - [Operating Expenses Detail - Other Employee Costs](#operating-expenses-operating-expenses-detail---other-employee-costs)
   - [Operating Expenses Detail - Travel](#operating-expenses-operating-expenses-detail---travel)
   - [Operating Expenses Detail - Facilities Costs](#operating-expenses-operating-expenses-detail---facilities-costs)
   - [Operating Expenses Detail - Marketing](#operating-expenses-operating-expenses-detail---marketing)
   - [Operating Expenses Detail - General and Administrative](#operating-expenses-operating-expenses-detail---general-and-administrative)
   - [Operating Expenses Detail - Legal](#operating-expenses-operating-expenses-detail---legal)
   - [Operating Expenses Detail - Other Costs](#operating-expenses-operating-expenses-detail---other-costs)
27. [Content](#content)
   - [Header](#content-header)
   - [Content Operating Expenses Summary](#content-content-operating-expenses-summary)
   - [Content People Costs Details](#content-content-people-costs-details)
   - [Content Other Employee Costs Details](#content-content-other-employee-costs-details)
   - [Content Travel Costs Details](#content-content-travel-costs-details)
   - [Content Facility Costs Details](#content-content-facility-costs-details)
   - [Content Marketing Costs Details](#content-content-marketing-costs-details)
   - [Content General & Admin Costs Details](#content-content-general-&-admin-costs-details)
   - [Content Other Costs Details](#content-content-other-costs-details)
28. [Engineering](#engineering)
   - [Header](#engineering-header)
   - [Engineering Operating Expenses Summary](#engineering-engineering-operating-expenses-summary)
   - [Engineering People Costs](#engineering-engineering-people-costs)
   - [Engineering Other Employee Costs](#engineering-engineering-other-employee-costs)
   - [Engineering Travel Costs](#engineering-engineering-travel-costs)
   - [Engineering Facility Costs](#engineering-engineering-facility-costs)
   - [Engineering Marketing](#engineering-engineering-marketing)
   - [Engineering General & Admin](#engineering-engineering-general-&-admin)
   - [Engineering Other Costs](#engineering-engineering-other-costs)
29. [Executive](#executive)
   - [Title and Context](#executive-title-and-context)
   - [Executive Operating Expenses Summary](#executive-executive-operating-expenses-summary)
   - [Executive People Costs](#executive-executive-people-costs)
   - [Executive Other Employee Costs](#executive-executive-other-employee-costs)
   - [Executive Travel Costs](#executive-executive-travel-costs)
   - [Executive Facility Costs](#executive-executive-facility-costs)
   - [Executive Marketing](#executive-executive-marketing)
   - [Executive General & Admin](#executive-executive-general-&-admin)
   - [Executive Other Costs](#executive-executive-other-costs)
30. [Finance & Admin](#finance-&-admin)
   - [Title & Scenario](#finance-&-admin-title-&-scenario)
   - [Finance & Admin Operating Expenses Summary](#finance-&-admin-finance-&-admin-operating-expenses-summary)
   - [Wages Breakdown](#finance-&-admin-wages-breakdown)
   - [Recruiting Fees Breakdown](#finance-&-admin-recruiting-fees-breakdown)
   - [Relocation Expenses](#finance-&-admin-relocation-expenses)
   - [Contractors Expenses](#finance-&-admin-contractors-expenses)
   - [Outsourced R&D Expenses](#finance-&-admin-outsourced-r&d-expenses)
   - [Capitalized Expenses](#finance-&-admin-capitalized-expenses)
   - [Other Employee Costs](#finance-&-admin-other-employee-costs)
   - [Travel Costs](#finance-&-admin-travel-costs)
   - [Internal Events](#finance-&-admin-internal-events)
   - [Facility Costs](#finance-&-admin-facility-costs)
   - [Rental Income](#finance-&-admin-rental-income)
   - [Marketing Expenses](#finance-&-admin-marketing-expenses)
   - [General & Admin Expenses](#finance-&-admin-general-&-admin-expenses)
   - [Other Costs](#finance-&-admin-other-costs)
   - [Bad Debt](#finance-&-admin-bad-debt)
31. [Marketing](#marketing)
   - [Header](#marketing-header)
   - [Section Name: Marketing Operating Expenses Summary](#marketing-section-name-marketing-operating-expenses-summary)
   - [Section Name: Marketing People Costs](#marketing-section-name-marketing-people-costs)
   - [Section Name: Marketing Other Employee Costs](#marketing-section-name-marketing-other-employee-costs)
   - [Section Name: Marketing Travel Costs](#marketing-section-name-marketing-travel-costs)
   - [Section Name: Marketing Facility Costs](#marketing-section-name-marketing-facility-costs)
   - [Section Name: Marketing Marketing](#marketing-section-name-marketing-marketing)
   - [Section Name: Marketing General & Admin](#marketing-section-name-marketing-general-&-admin)
   - [Section Name: Marketing Other Costs](#marketing-section-name-marketing-other-costs)
   - [Section Name: Marketing Performance Metrics](#marketing-section-name-marketing-performance-metrics)
32. [Product](#product)
   - [Section Name: Header](#product-section-name-header)
   - [Section Name: Product Operating Expenses Summary](#product-section-name-product-operating-expenses-summary)
33. [Sales](#sales)
   - [Header](#sales-header)
   - [Sales Operating Expenses Summary](#sales-sales-operating-expenses-summary)
   - [Sales People Costs](#sales-sales-people-costs)
   - [Sales Other Employee Costs](#sales-sales-other-employee-costs)
   - [Sales Travel Costs](#sales-sales-travel-costs)
   - [Sales Facility Costs](#sales-sales-facility-costs)
   - [Sales Marketing](#sales-sales-marketing)
   - [Sales General & Admin](#sales-sales-general-&-admin)
   - [Sales Other Costs](#sales-sales-other-costs)
34. [Commission Waterfall](#commission-waterfall)
   - [Header](#commission-waterfall-header)
   - [Commissions Expense Summary](#commission-waterfall-commissions-expense-summary)
   - [Financial Commission Waterfall](#commission-waterfall-financial-commission-waterfall)
   - [Corporate Commission Waterfall](#commission-waterfall-corporate-commission-waterfall)
   - [Other Commission Waterfall](#commission-waterfall-other-commission-waterfall)
   - [AE Commission Waterfall](#commission-waterfall-ae-commission-waterfall)
   - [Total Commission Expense](#commission-waterfall-total-commission-expense)
35. [Bad Debt](#bad-debt)
   - [Section Name: Reconciliation Header](#bad-debt-section-name-reconciliation-header)
   - [Section Name: AFDA Reconciliation Table](#bad-debt-section-name-afda-reconciliation-table)
36. [COGS CTRL](#cogs-ctrl)
   - [User Metrics Table](#cogs-ctrl-user-metrics-table)
   - [Product Cost Assumptions](#cogs-ctrl-product-cost-assumptions)
   - [International Filings Expenses](#cogs-ctrl-international-filings-expenses)
   - [Transcripts Expenses](#cogs-ctrl-transcripts-expenses)
   - [Dow Jones Expenses](#cogs-ctrl-dow-jones-expenses)
   - [News & Journals Expenses](#cogs-ctrl-news-&-journals-expenses)
   - [Web Service Expenses](#cogs-ctrl-web-service-expenses)
   - [Other Additional Data Sources](#cogs-ctrl-other-additional-data-sources)
   - [ASR Expenses](#cogs-ctrl-asr-expenses)
   - [Usage Metrics](#cogs-ctrl-usage-metrics)
   - [Revenue Share](#cogs-ctrl-revenue-share)
   - [Minimum Revenue](#cogs-ctrl-minimum-revenue)
   - [WSI FactSet Controls](#cogs-ctrl-wsi-factset-controls)
   - [WSI New User Additions](#cogs-ctrl-wsi-new-user-additions)
37. [Cost of Goods Sold](#cost-of-goods-sold)
   - [Cost of Goods Sold Summary](#cost-of-goods-sold-cost-of-goods-sold-summary)
   - [Product Summary](#cost-of-goods-sold-product-summary)
   - [Product Summary - % of Revenue](#cost-of-goods-sold-product-summary---%-of-revenue)
   - [Total User Count](#cost-of-goods-sold-total-user-count)
   - [Total User Net Adds](#cost-of-goods-sold-total-user-net-adds)
   - [Product Detail Net Adds - Live Users](#cost-of-goods-sold-product-detail-net-adds---live-users)
   - [Product Detail - Live Users](#cost-of-goods-sold-product-detail---live-users)
   - [Factset Research](#cost-of-goods-sold-factset-research)
   - [TR Research - New Contract](#cost-of-goods-sold-tr-research---new-contract)
   - [After Market Research Expense](#cost-of-goods-sold-after-market-research-expense)
   - [International Filings Expense](#cost-of-goods-sold-international-filings-expense)
   - [Transcripts Expense](#cost-of-goods-sold-transcripts-expense)
   - [Dow Jones News Expense](#cost-of-goods-sold-dow-jones-news-expense)
   - [News & Journals Expense](#cost-of-goods-sold-news-&-journals-expense)
   - [IDC Expense](#cost-of-goods-sold-idc-expense)
   - [Web Service COGS Allocation](#cost-of-goods-sold-web-service-cogs-allocation)
   - [COGS by Segment](#cost-of-goods-sold-cogs-by-segment)
   - [P&L](#cost-of-goods-sold-p&l)
   - [COGS Allocation](#cost-of-goods-sold-cogs-allocation)
   - [Upside Case](#cost-of-goods-sold-upside-case)
   - [S&P Transcripts](#cost-of-goods-sold-s&p-transcripts)
38. [Total FDS Cost](#total-fds-cost)
   - [Section Name: Summary FDS COGS Expense](#total-fds-cost-section-name-summary-fds-cogs-expense)
   - [Section Name: FDS Excess Expense](#total-fds-cost-section-name-fds-excess-expense)
   - [Section Name: Total FDS Spend & Minimum](#total-fds-cost-section-name-total-fds-spend-&-minimum)
   - [Section Name: Pool Contribution & Carryover](#total-fds-cost-section-name-pool-contribution-&-carryover)
   - [Section Name: Adjusted FDS COGS Expense](#total-fds-cost-section-name-adjusted-fds-cogs-expense)
39. [FDS AMR](#fds-amr)
   - [Header](#fds-amr-header)
   - [Key Metrics & Bookings](#fds-amr-key-metrics-&-bookings)
   - [Documents Purchased Analysis](#fds-amr-documents-purchased-analysis)
   - [Cost Analysis](#fds-amr-cost-analysis)
40. [Direct Broker](#direct-broker)
   - [Overview Section](#direct-broker-overview-section)
   - [Reads Consumption Section](#direct-broker-reads-consumption-section)
   - [WSI Broker Expense Section](#direct-broker-wsi-broker-expense-section)
   - [Direct Broker Expense Section](#direct-broker-direct-broker-expense-section)
41. [Additional FDS Content](#additional-fds-content)
   - [Section Name: FDS RT Expense by User Tier](#additional-fds-content-section-name-fds-rt-expense-by-user-tier)
   - [Section Name: FDS RT Excess Expense Calculation](#additional-fds-content-section-name-fds-rt-excess-expense-calculation)
   - [Section Name: Factset Transcripts Expense by User Tier](#additional-fds-content-section-name-factset-transcripts-expense-by-user-tier)
   - [Section Name: Factset M&A Expense by User Tier](#additional-fds-content-section-name-factset-m&a-expense-by-user-tier)
42. [FDS User Growth](#fds-user-growth)
   - [User Summary](#fds-user-growth-user-summary)
   - [New WSI Users Additions](#fds-user-growth-new-wsi-users-additions)
   - [Percent of New Users Added](#fds-user-growth-percent-of-new-users-added)
   - [New WSI Users Added by Sector](#fds-user-growth-new-wsi-users-added-by-sector)
   - [Non-WSI Users Converted](#fds-user-growth-non-wsi-users-converted)
   - [Percent of New Non-WSI Users Added by Sector](#fds-user-growth-percent-of-new-non-wsi-users-added-by-sector)
   - [Non-WSI Users Added](#fds-user-growth-non-wsi-users-added)
   - [Non-WSI Net User Change](#fds-user-growth-non-wsi-net-user-change)
   - [Non-WSI Users by Sector](#fds-user-growth-non-wsi-users-by-sector)
   - [WSI User Additions](#fds-user-growth-wsi-user-additions)
   - [Total Users](#fds-user-growth-total-users)
   - [Percent of Active Users](#fds-user-growth-percent-of-active-users)
   - [Total Active Users](#fds-user-growth-total-active-users)
   - [Document Consumption](#fds-user-growth-document-consumption)
   - [Consumpstion Reduction](#fds-user-growth-consumpstion-reduction)
   - [Total Docs - Reduction](#fds-user-growth-total-docs---reduction)
   - [Total Docs - Unadjusted](#fds-user-growth-total-docs---unadjusted)
   - [FDS RT Users Detail](#fds-user-growth-fds-rt-users-detail)
43. [FDS RT Minimums](#fds-rt-minimums)
   - [Section Name (e.g., "User Tier Pricing Table")](#fds-rt-minimums-section-name-eg-"user-tier-pricing-table")
44. [Product User Splits](#product-user-splits)
   - [Section Name: Product User Data](#product-user-splits-section-name-product-user-data)
   - [Section Name: BRM Data](#product-user-splits-section-name-brm-data)
   - [Section Name: FactSet RT Data](#product-user-splits-section-name-factset-rt-data)
   - [Section Name: FactSet AMR Data](#product-user-splits-section-name-factset-amr-data)
   - [Section Name: FactSet AMR Breakdown Data](#product-user-splits-section-name-factset-amr-breakdown-data)
   - [Section Name: FactSet AMR Docs Purchased Data](#product-user-splits-section-name-factset-amr-docs-purchased-data)
45. [TR BRM](#tr-brm)
   - [Tiered Pricing Data](#tr-brm-tiered-pricing-data)
   - [User Segmentation Data](#tr-brm-user-segmentation-data)
   - [Financial Segmentation Data](#tr-brm-financial-segmentation-data)
46. [AMR](#amr)
   - [Monthly Data Table](#amr-monthly-data-table)
   - [Cost Breakdown Table](#amr-cost-breakdown-table)
47. [LN](#ln)
   - [Header](#ln-header)
   - [Financial Data Section](#ln-financial-data-section)
48. [DJ](#dj)
   - [Header](#dj-header)
   - [Financial Data Section](#dj-financial-data-section)
49. [TR Transcripts](#tr-transcripts)
   - [Top Section (Quarterly Data)](#tr-transcripts-top-section-quarterly-data)
   - [Bottom Section (Monthly Data)](#tr-transcripts-bottom-section-monthly-data)
50. [FS Transcripts](#fs-transcripts)
   - [Revenue Breakdown (Quarterly)](#fs-transcripts-revenue-breakdown-quarterly)
   - [Revenue Breakdown (Monthly)](#fs-transcripts-revenue-breakdown-monthly)
51. [Filings](#filings)
   - [Section Name: Revenue Breakdown](#filings-section-name-revenue-breakdown)
52. [Detailed Income Statement](#detailed-income-statement)
   - [Header](#detailed-income-statement-header)
   - [Income Statement](#detailed-income-statement-income-statement)
   - [Personnel Cost Breakdown](#detailed-income-statement-personnel-cost-breakdown)
53. [Detailed Balance Sheet](#detailed-balance-sheet)
   - [Section Name: Header](#detailed-balance-sheet-section-name-header)
   - [Section Name: Assets](#detailed-balance-sheet-section-name-assets)
   - [Section Name: Liabilities](#detailed-balance-sheet-section-name-liabilities)
   - [Section Name: Equity](#detailed-balance-sheet-section-name-equity)
   - [Section Name: Liabilities & Equity Reconciliation](#detailed-balance-sheet-section-name-liabilities-&-equity-reconciliation)
54. [Detailed Cash Flow Satement](#detailed-cash-flow-satement)
   - [Section Name (Cash Flow Statement)](#detailed-cash-flow-satement-section-name-cash-flow-statement)
55. [Key Metrics](#key-metrics)
   - [Section Name: Annual Subscription Value](#key-metrics-section-name-annual-subscription-value)
   - [Section Name: ARR Added (Gross)](#key-metrics-section-name-arr-added-gross)
   - [Section Name: ARR Churn](#key-metrics-section-name-arr-churn)
   - [Section Name: ARR Churn Notifications](#key-metrics-section-name-arr-churn-notifications)
   - [Section Name: # of Client Firms](#key-metrics-section-name-#-of-client-firms)
   - [Section Name: # of Users](#key-metrics-section-name-#-of-users)
   - [Section Name: SaaS Metrics](#key-metrics-section-name-saas-metrics)
   - [Section Name: Contract Duration](#key-metrics-section-name-contract-duration)
   - [Section Name: Deal Metrics](#key-metrics-section-name-deal-metrics)
   - [Section Name: Raw Data](#key-metrics-section-name-raw-data)
   - [Section Name: Contract Length](#key-metrics-section-name-contract-length)
   - [Section Name: Client Counts](#key-metrics-section-name-client-counts)
   - [Section Name: User Counts](#key-metrics-section-name-user-counts)
   - [Section Name: Cancels](#key-metrics-section-name-cancels)
   - [Section Name: ARR New/Upsell/Increase $](#key-metrics-section-name-arr-newupsellincrease-$)
   - [Section Name: Monthly Recurring Revenue](#key-metrics-section-name-monthly-recurring-revenue)
56. [Revenue by Client](#revenue-by-client)
   - [Section Name: Revenue Summary by Client](#revenue-by-client-section-name-revenue-summary-by-client)
   - [Section Name: Income Statement (Fragment)](#revenue-by-client-section-name-income-statement-fragment)
   - [Section Name: Monthly Data (2015)](#revenue-by-client-section-name-monthly-data-2015)
   - [Section Name: Monthly Data (2016)](#revenue-by-client-section-name-monthly-data-2016)
   - [Section Name: Monthly Data (2017)](#revenue-by-client-section-name-monthly-data-2017)
57. [Client Support](#client-support)
   - [Section Name: Client Type Metrics (Corp)](#client-support-section-name-client-type-metrics-corp)
   - [Section Name: Client Type Metrics (Corporate)](#client-support-section-name-client-type-metrics-corporate)
   - [Section Name: Client Type Metrics (Other)](#client-support-section-name-client-type-metrics-other)
   - [Section Name: Churned CARR - Lost Clients](#client-support-section-name-churned-carr---lost-clients)
   - [Section Name: Totals](#client-support-section-name-totals)
58. [Subscriber Support](#subscriber-support)
   - [Section Name: Subscriber Rollforward - Financial](#subscriber-support-section-name-subscriber-rollforward---financial)
   - [Section Name: Subscriber Rollforward - Corp](#subscriber-support-section-name-subscriber-rollforward---corp)
   - [Section Name: Subscriber Rollforward - Other](#subscriber-support-section-name-subscriber-rollforward---other)
   - [Section Name: Cost Allocation](#subscriber-support-section-name-cost-allocation)
59. [Headcount Support](#headcount-support)
   - [Section Name (Department Headcount - Section 1)](#headcount-support-section-name-department-headcount---section-1)
   - [Section Name (Department Headcount - Section 2)](#headcount-support-section-name-department-headcount---section-2)
   - [Section Name (Sales Team Headcount)](#headcount-support-section-name-sales-team-headcount)
60. [Salary Support](#salary-support)
   - [Section Name: Department Salary Breakdown (High-Level)](#salary-support-section-name-department-salary-breakdown-high-level)
   - [Section Name: Department Salary Breakdown (Detailed)](#salary-support-section-name-department-salary-breakdown-detailed)
   - [Section Name: FX Rate](#salary-support-section-name-fx-rate)
   - [Section Name: Quota Sales Reps & Team Costs](#salary-support-section-name-quota-sales-reps-&-team-costs)
61. [Bonus Support](#bonus-support)
   - [Section Name: Department Salary Budget (2019 & 2020)](#bonus-support-section-name-department-salary-budget-2019-&-2020)
   - [Section Name: Adjustment Table](#bonus-support-section-name-adjustment-table)
   - [Section Name: Department Salary Budget (2019 & 2020) - Repeated](#bonus-support-section-name-department-salary-budget-2019-&-2020---repeated)
   - [Section Name: Sales Bonus Summary](#bonus-support-section-name-sales-bonus-summary)
   - [Section Name: Department Bonus Breakdown](#bonus-support-section-name-department-bonus-breakdown)
   - [Section Name: Department Bonus Breakdown (Repeated)](#bonus-support-section-name-department-bonus-breakdown-repeated)
62. [Bonus Support (Sales non Ops)](#bonus-support-(sales-non-ops))
   - [Salary & Bonus Budget](#bonus-support-(sales-non-ops)-salary-&-bonus-budget)
   - [Sales Team Bonus Calculation](#bonus-support-(sales-non-ops)-sales-team-bonus-calculation)
63. [Bonus Support (Sales Ops Only)](#bonus-support-(sales-ops-only))
   - [Section Name: Department Salary Budget (Annual)](#bonus-support-(sales-ops-only)-section-name-department-salary-budget-annual)
   - [Section Name: Department Salary Adjustment (Annual)](#bonus-support-(sales-ops-only)-section-name-department-salary-adjustment-annual)
   - [Section Name: Department Salary Budget (Annual - Repeated)](#bonus-support-(sales-ops-only)-section-name-department-salary-budget-annual---repeated)
   - [Section Name: Sales Bonus Summary (Multiple Time Series)](#bonus-support-(sales-ops-only)-section-name-sales-bonus-summary-multiple-time-series)
   - [Section Name: Sales Bonus by Role (Monthly)](#bonus-support-(sales-ops-only)-section-name-sales-bonus-by-role-monthly)
64. [Headcount Adds](#headcount-adds)
   - [Header](#headcount-adds-header)
   - [Headcount Additions by Department](#headcount-adds-headcount-additions-by-department)
   - [Headcount Counts by Category](#headcount-adds-headcount-counts-by-category)
65. [OpEx - Content](#opex---content)
   - [Header](#opex---content-header)
   - [Income Statement](#opex---content-income-statement)
66. [OpEx - Engineering](#opex---engineering)
   - [Header](#opex---engineering-header)
   - [Income Statement](#opex---engineering-income-statement)
67. [OpEx - Executive](#opex---executive)
   - [Header](#opex---executive-header)
   - [Income Statement](#opex---executive-income-statement)
68. [OpEx - Finance & Admin](#opex---finance-&-admin)
   - [Header](#opex---finance-&-admin-header)
   - [Income Statement](#opex---finance-&-admin-income-statement)
69. [OpEx - Marketing](#opex---marketing)
   - [Section Name: Header](#opex---marketing-section-name-header)
   - [Section Name: Income Statement (Marketing Department View)](#opex---marketing-section-name-income-statement-marketing-department-view)
70. [OpEx - Product](#opex---product)
   - [Header](#opex---product-header)
   - [Income Statement](#opex---product-income-statement)
71. [OpEx - Sales](#opex---sales)
   - [Header](#opex---sales-header)
   - [Income Statement](#opex---sales-income-statement)
72. [Historical Quota& Productivity](#historical-quota&-productivity)
   - [Section Name: Historical Quota](#historical-quota&-productivity-section-name-historical-quota)
   - [Section Name: Historical Productivity](#historical-quota&-productivity-section-name-historical-productivity)
73. [Fixed Asset Depreciation](#fixed-asset-depreciation)
   - [Section Name (Fixed Asset Depreciation - LTD)](#fixed-asset-depreciation-section-name-fixed-asset-depreciation---ltd)
   - [Section Name (Fixed Asset Depreciation - Mgmt)](#fixed-asset-depreciation-section-name-fixed-asset-depreciation---mgmt)
   - [Section Name (Fixed Asset Depreciation - Inc)](#fixed-asset-depreciation-section-name-fixed-asset-depreciation---inc)
74. [COGS vs. Marginal](#cogs-vs.-marginal)
   - [Section Name: Revenue and Seats Summary](#cogs-vs.-marginal-section-name-revenue-and-seats-summary)
   - [Section Name: COGS and Gross Profit Analysis](#cogs-vs.-marginal-section-name-cogs-and-gross-profit-analysis)
   - [Section Name: Cost Calculations](#cogs-vs.-marginal-section-name-cost-calculations)
75. [Benchmarking](#benchmarking)
   - [Section Name: Revenue and Expense Benchmarking](#benchmarking-section-name-revenue-and-expense-benchmarking)
   - [Section Name: Revenue(1) and Growth](#benchmarking-section-name-revenue1-and-growth)
   - [Section Name: 2017 Expenses](#benchmarking-section-name-2017-expenses)
   - [Section Name: Revenue Multiples](#benchmarking-section-name-revenue-multiples)
76. [Accrued Expenses](#accrued-expenses)
   - [Header Information](#accrued-expenses-header-information)
   - [Audit Accrual Details](#accrued-expenses-audit-accrual-details)
   - [Data Feeds Expenses](#accrued-expenses-data-feeds-expenses)
   - [Data Feeds Expenses (Continued)](#accrued-expenses-data-feeds-expenses-continued)
   - [Account 21000 (Oy) Expenses](#accrued-expenses-account-21000-oy-expenses)
   - [Total Accrued Expenses](#accrued-expenses-total-accrued-expenses)
77. [Prepaid Expenses](#prepaid-expenses)
   - [Vendor List](#prepaid-expenses-vendor-list)
   - [Prepaid Expenses Schedule](#prepaid-expenses-prepaid-expenses-schedule)
   - [Prepaid Expenses Rollforward](#prepaid-expenses-prepaid-expenses-rollforward)
78. [Accrued Wages](#accrued-wages)
   - [Section Name (Accrued Wages Calculation)](#accrued-wages-section-name-accrued-wages-calculation)
79. [Cap R&D Exisiting Runoff](#cap-r&d-exisiting-runoff)
   - [Monthly Data Section](#cap-r&d-exisiting-runoff-monthly-data-section)
   - [Annual Data Section](#cap-r&d-exisiting-runoff-annual-data-section)
   - [Exchange Rate](#cap-r&d-exisiting-runoff-exchange-rate)
80. [Deposits](#deposits)
   - [Section Name (Deposits Data)](#deposits-section-name-deposits-data)
81. [Tekes Loans](#tekes-loans)
   - [Section Name: Loan 1: Tekes -14223, 114850 €](#tekes-loans-section-name-loan-1-tekes--14223-114850-€)
   - [Section Name: Loan 2: Tekes -14560, 337265,82 €](#tekes-loans-section-name-loan-2-tekes--14560-33726582-€)
   - [Section Name: Loan 3: Tekes -14887, 343615 €](#tekes-loans-section-name-loan-3-tekes--14887-343615-€)
   - [Section Name: Loan 4: Tekes -15118, 186500 €](#tekes-loans-section-name-loan-4-tekes--15118-186500-€)
   - [Section Name: Loan 5: Tekes -15543, 159800 €](#tekes-loans-section-name-loan-5-tekes--15543-159800-€)
   - [Section Name: Accrued Interest Balance & FX Rate](#tekes-loans-section-name-accrued-interest-balance-&-fx-rate)

---


====================================================================================================
# SHEET 1: Summary
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Summary
- **Key Sections Identified**:
    - Change Log
    - Key Metrics - Monthly
    - Key Metrics - Annual

## 2. Detailed Section Analysis

### Change Log
- **Section Type**: Change Log
- **Description & Purpose**: Documents changes made to the model.
- **Cell Range**: B2:B6
- **Layout Structure**:
    - **Row Headers Location**: B2:B6
    - **Column Headers Location**: None
    - **Data Range**: B2:B6
- **Time Series Details**: None
- **Key Components**: Change descriptions.
- **Notes & Customizations**: Text descriptions of changes made.

### Key Metrics - Monthly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents key performance indicators (KPIs) on a monthly basis.
- **Cell Range**: C40:BK53
- **Layout Structure**:
    - **Row Headers Location**: C41:C53
    - **Column Headers Location**: D40:BK40, D43:BK43, D47:BK47, D49:BK49
    - **Data Range**:
      - Monthly data: D41:BK42, D44:BK46, D48:BK53
- **Time Series Details**:
    - **Date Range**: 2018-01-31 to 2022-12-31
    - **Frequency**: Monthly
- **Key Components**: Cash, Debt, ARR, Bookings, ARR TTM Growth, Margin, EBITDA, FCF, Reps, Eff Reps.
- **Notes & Customizations**: Data is scaled by 1000 in some rows.

### Key Metrics - Annual
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents key performance indicators (KPIs) on an annual basis.
- **Cell Range**: C57:H66
- **Layout Structure**:
    - **Row Headers Location**: C58:C66
    - **Column Headers Location**: D57:H57
    - **Data Range**:
      - Annual data: D58:H66
- **Time Series Details**:
    - **Date Range**: 2018-01-01 to 2022-01-01
    - **Frequency**: Annual
- **Key Components**: ARR, FCF, Avg FCF, Cash, Debt, Growth Rate, Avg Eff Reps, Bookings, Avg Bkgs.
- **Notes & Customizations**: Data is scaled by 1000 in some rows.



====================================================================================================
# SHEET 2: Master Ctrl
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Master Ctrl
- **Key Sections Identified**:
    - Header
    - Control Scenarios
    - Productivity & Margin Cases

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and sheet title for identification.
- **Cell Range**: `B2:B3`
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: `B2:B3`
- **Time Series Details**: N/A
- **Key Components**: "AlphaSense, Inc.", "Master CTRL"
- **Notes & Customizations**: Standard header information.

### Control Scenarios
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines different control scenarios and their corresponding values. Used for scenario analysis.
- **Cell Range**: `A12:C18`
- **Layout Structure**:
    - **Row Headers Location**: `B14:B18`
    - **Column Headers Location**: `A12:C12`
    - **Data Range**: `C14:C18`
- **Time Series Details**: N/A
- **Key Components**: "Master Case", "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: The 'x' in column A likely indicates a selection or active scenario.

### Global Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains global assumptions used in the model.
- **Cell Range**: `B20:E25`
- **Layout Structure**:
    - **Row Headers Location**: `B20`, `B22`, `B25`
    - **Column Headers Location**: N/A
    - **Data Range**: `E25`
- **Time Series Details**: N/A
- **Key Components**: "Global Assumptions", "Latest Actual Month", "Months Left in Year"
- **Notes & Customizations**: Contains a single numeric value for "Months Left in Year" scaled by 1000.

### Productivity & Margin Cases
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines different productivity and margin scenarios and their corresponding values. Used for scenario analysis.
- **Cell Range**: `B27:C33`
- **Layout Structure**:
    - **Row Headers Location**: `B27:B33`
    - **Column Headers Location**: N/A
    - **Data Range**: `C27:C33`
- **Time Series Details**: N/A
- **Key Components**: "Productivity Case", "Base", "Target", "Margin Case", "Base", "Target"
- **Notes & Customizations**: Contains numeric values for different productivity and margin scenarios.



====================================================================================================
# SHEET 3: Dash Control
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Dash Control
- **Key Sections Identified**:
    - Header
    - Dashboard Control Parameters

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and dashboard title.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: B2:B4
- **Time Series Details**: N/A
- **Key Components**: AlphaSense, Inc., Dashboard CTRL, 1 - Base - $25mm
- **Notes & Customizations**: Simple header information.

### Section Name: Dashboard Control Parameters
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains key parameters used to control the dashboard, including ARR Multipliers, Perpetuity Factors, and % Travel Costs, under different scenarios (Base, Growth) and financial assumptions.
- **Cell Range**: A7:FS66
- **Layout Structure**:
    - **Row Headers Location**: B7:B66
    - **Column Headers Location**: E7:FS8
    - **Data Range**:
      - Annual data: E9:Q66
      - Monthly data: T9:FS66
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Year, Month, Support Fees - % of CAC, ARR Multipler, Perpetuity Factor, % Travel Costs, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Contains both annual and monthly time series data. Values are scaled by 1000. The data is organized by different scenarios (Base, Growth) and financial assumptions.


====================================================================================================
# SHEET 4: Dash
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Dash
- **Key Sections Identified**:
    - Income Statement Metrics
    - ARR Summary
    - Bookings
    - Segment Summary
    - Headcount Summary
    - Client & Subscriber Counts
    - Retention Metrics
    - Key Performance Indicators Summary
    - Key Performance Indicators Detail
    - Key Performance Indicators by Segment
    - Debt Availability Build

## 2. Detailed Section Analysis

### Income Statement Metrics
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's income statement, showing revenue, cost of sales, gross profit, operating expenses, and EBITDA. It's used to track profitability and financial performance.
- **Cell Range**: A6:FS25
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E8:Q23` (numeric values for annual periods)
      - Monthly data: `T8:FS23` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: E3:I3 and J3:Q3 (Years not explicitly provided, but assumed to be consecutive years based on the structure)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Operating Expenses, EBITDA, Free Cashflow (FCF).
- **Notes & Customizations**: Includes a memo line for Free Cashflow. Values are scaled by 1000.

### ARR Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the company's Annual Recurring Revenue (ARR), including beginning and ending ARR, and bookings information.
- **Cell Range**: A27:FS31
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E29:Q30` (numeric values for annual periods)
      - Monthly data: `T29:FS30` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: E3:I3 and J3:Q3 (Years not explicitly provided, but assumed to be consecutive years based on the structure)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Beginning ARR, Ending ARR.
- **Notes & Customizations**: Values are scaled by 1000.

### Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the company's bookings, broken down by Financial, Corporate, and Other categories.
- **Cell Range**: B33:FS52
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E34:Q51` (numeric values for annual periods)
      - Monthly data: `T34:FS51` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: E3:I3 and J3:Q3 (Years not explicitly provided, but assumed to be consecutive years based on the structure)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial Bookings, Corporate Bookings, Other Bookings, Total Bookings, New Bookings, Total New Bookings, Upsell, Total Upsell.
- **Notes & Customizations**: Values are scaled by 1000.

### Segment Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes ARR by segment.
- **Cell Range**: A54:FS71
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E59:Q70` (numeric values for annual periods)
      - Monthly data: `T59:FS70` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: E3:I3 and J3:Q3 (Years not explicitly provided, but assumed to be consecutive years based on the structure)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Beginning ARR, Ending ARR.
- **Notes & Customizations**: Values are scaled by 1000.

### Headcount Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes headcount by department.
- **Cell Range**: A111:FS127
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E114:Q127` (numeric values for annual periods)
      - Monthly data: `T114:FS127` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: E3:I3 and J3:Q3 (Years not explicitly provided, but assumed to be consecutive years based on the structure)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Executive, Engineering, Product, Sales, Marketing, Content, Finance, HR, and Operations, Total Headcount, Avg Effective Quota Carrying Sales Reps, New ARR per Sales Rep, New Clients per Sales Rep.
- **Notes & Customizations**: Values are scaled by 1000.

### Client & Subscriber Counts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of clients and subscribers.
- **Cell Range**: A129:FS190
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E133:Q190` (numeric values for annual periods)
      - Monthly data: `T133:FS190` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: E3:I3 and J3:Q3 (Years not explicitly provided, but assumed to be consecutive years based on the structure)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Clients (End of Period), Users (End of Period), Clients, Beginning of Period, Added, Churned, Clients, End of Period, ARR Per Client, Users Added In Period, Total Users Added In Period, Total Users (End of Period).
- **Notes & Customizations**: Values are scaled by 1000.

### Retention Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays retention metrics.
- **Cell Range**: A192:FS206
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E194:Q206` (numeric values for annual periods)
      - Monthly data: `T194:FS206` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: E3:I3 and J3:Q3 (Years not explicitly provided, but assumed to be consecutive years based on the structure)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Upsells, Up for Renewal, Renewed, Churn, Ann. Net Dollar Retention, Ann. Gross Dollar Retention, Ann. Cohort Retention, Ann. Net Dollar Retention - TTM, Ann. Gross Dollar Retention - TTM, Ann. Cohort Retention - TTM.
- **Notes & Customizations**: Values are scaled by 1000 where applicable.

### Key Performance Indicators Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes key performance indicators.
- **Cell Range**: A208:FS213
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E211:Q213` (numeric values for annual periods)
      - Monthly data: `AR211:FS213` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: E3:I3 and J3:Q3 (Years not explicitly provided, but assumed to be consecutive years based on the structure)
      - Monthly: 2017-03-31 to 2020-12-31 (based on the data range AR211:FS213)
    - **Frequency**:
      - Annual
      - Quarterly (Inferred from the column headers in the data range AR211:FS213)
- **Key Components**: LTV / CAC.
- **Notes & Customizations**: Values are scaled by 1000.

### Key Performance Indicators Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed key performance indicators.
- **Cell Range**: A215:FS263
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E217:Q263` (numeric values for annual periods)
      - Monthly data: `T217:FS263` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: E3:I3 and J3:Q3 (Years not explicitly provided, but assumed to be consecutive years based on the structure)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Margin (end of Period), Avg Quota Carrying Salee Reps, Bookings per Sales Rep, ARR per Sales Rep, Avg. Users per Client, Annual Rev/Client (ARPC), Annual COS/Client, Annual Rev/Subscriber (ARPU), Annual COS/Subscriber, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback Period (Months).
- **Notes & Customizations**: Values are scaled by 1000.

### Key Performance Indicators by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents key performance indicators broken down by segment.
- **Cell Range**: A266:FS356
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E270:Q356` (numeric values for annual periods)
      - Monthly data: `T270:FS356` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: E3:I3 and J3:Q3 (Years not explicitly provided, but assumed to be consecutive years based on the structure)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Avg. Users per Client, Annual Rev/Client (ARPC), Annual COS/Client, Annual Rev/Subscriber (ARPU), Annual COS/Subscriber, Churn, Annual Gross Dollar Retention, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, LTV / CAC, Payback Period (Months).
- **Notes & Customizations**: Values are scaled by 1000.

### Debt Availability Build
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Calculates debt availability based on MRR and other factors.
- **Cell Range**: B360:DW373
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: `BW363:DW373`
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but implies a short-term horizon (T3M = Trailing 3 Months).
    - **Frequency**: Not explicitly defined.
- **Key Components**: Multiplier of MRR, T3M MRR, T3M Revenue Lost, T3M Churn, Annualized Retention Rate, Current MRR, Availability Amount.
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 5: CAC by Segment
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: CAC by Segment
- **Key Sections Identified**:
    - Summary Upsell Cost
    - Summary CAC
    - Summary Support Cost
    - Detail Section
    - Adjusted Sales and Marketing Cost
    - Adjusted People Costs
    - All-In Support Costs

## 2. Detailed Section Analysis

### Summary Upsell Cost
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of the upsell costs for the Total Company, Financial segment, and Corporate segment. It is used to understand the overall upsell cost and its distribution across different segments.
- **Cell Range**: B8:FS11
- **Layout Structure**:
    - **Row Headers Location**: B8:B11
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E9:Q11
      - Monthly data: T9:FS11, AR10:FS11
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Upsell Cost, Total Company, Financial, Corporate
- **Notes & Customizations**: The data is scaled by 1000.

### Summary CAC
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of the CAC (Customer Acquisition Cost) for the Total Company, Financial segment, and Corporate segment. It is used to understand the overall CAC and its distribution across different segments.
- **Cell Range**: B13:FS16
- **Layout Structure**:
    - **Row Headers Location**: B13:B16
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E14:Q16
      - Monthly data: T14:FS16, AR15:FS16, AR16:FS16
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: CAC, Total Company, Financial, Corporate
- **Notes & Customizations**: The data is scaled by 1000.

### Summary Support Cost
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of the support costs for the Total Company, Financial segment, and Corporate segment. It is used to understand the overall support cost and its distribution across different segments.
- **Cell Range**: B18:FS21
- **Layout Structure**:
    - **Row Headers Location**: B18:B21
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E19:Q21
      - Monthly data: T19:FS21, AR20:FS21, AR21:FS21
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Support Cost, Total Company, Financial, Corporate
- **Notes & Customizations**: The data is scaled by 1000.

### Detail Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of costs by different account managers and segments.
- **Cell Range**: B23:FS69
- **Layout Structure**:
    - **Row Headers Location**: B23:B69
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G26:Q69, H44:Q47, I44:Q47, G44:G47, H44:H47, I62:Q66, G62:G66, H62:H66
      - Monthly data: AR26:FS69, T42:FS47
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Account Manager - Corp, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise, Total, % Financial, % Corporate, Wages
- **Notes & Customizations**: The data is scaled by 1000.

### Adjusted Sales and Marketing Cost
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the adjusted sales and marketing cost.
- **Cell Range**: B72:FS80
- **Layout Structure**:
    - **Row Headers Location**: B72:B80
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E74:Q80
      - Monthly data: T74:FS80
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Total Company, Adjusted Sales and Marketing Cost, % to CAC, % to Upsell, $ to CAC, $ to Upsell
- **Notes & Customizations**: The data is scaled by 1000.

### Adjusted People Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the adjusted people costs.
- **Cell Range**: B82:FS91
- **Layout Structure**:
    - **Row Headers Location**: B82:B91
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E82:Q91, E86:Q91, E87:Q90, I87:Q90
      - Monthly data: T82:FS91, T87:FS90
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Total Wages, Product Specialist Salary, % of Total Wages, People Costs, Add: Capitalized Wages, Less: Wages, Less: Outsourced R&D, Less: Commission (Duplicative), Adjusted People Costs
- **Notes & Customizations**: The data is scaled by 1000.

### All-In Support Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the all-in support costs and related metrics.
- **Cell Range**: A98:FS141
- **Layout Structure**:
    - **Row Headers Location**: B98:B141
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G100:Q141, G102:Q141, G103:Q141, G105:Q141, G106:Q141, G108:Q141, I109:Q111, I128:Q128, I132:Q134
      - Monthly data: AR100:FS141, AR102:FS141, AR103:FS141, AR105:FS141, AR106:FS141, AR108:FS141, AR109:FS111, AR128:FS128, AR132:FS134
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Financial, Corporate, Adjusted Sales and Marketing Cost, % to CAC, % to Upsell, $ to CAC, $ to Upsell, People Costs, Less: Wages, Less: Outsourced R&D, Less: Commission (Duplicative), Adjusted People Costs, Other Support Related People Costs, All-In Support Costs, Total Users (excl. Other), Financial Users, % Financial, Financial Support Costs, Corporate Users, % Corporate, Corporate Support Costs
- **Notes & Customizations**: The data is scaled by 1000.


====================================================================================================
# SHEET 6: Payback Period
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Payback Period
- **Key Sections Identified**:
    - Header
    - Payback Period - Total Company
    - Cash Payback Calculation
    - Payback Period - Financial
    - Payback Period - Corporate

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Cell Range**: B2:Q4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3
    - **Data Range**: E3:Q3
- **Time Series Details**:
    - **Date Range**: Not Applicable (Header information)
    - **Frequency**: Not Applicable
- **Key Components**: Company Name, Report Title, Scenario Description
- **Notes & Customizations**: Contains the company name "AlphaSense, Inc." and the scenario "1 - Base - $25mm".

### Payback Period - Total Company
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the key metrics used to calculate the payback period for the total company.
- **Cell Range**: B6:Q44
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E8:Q8
    - **Data Range**:
      - Annual data: `E16:Q44`
- **Time Series Details**:
    - **Date Range**: 2021 to 2033
    - **Frequency**: Annual
- **Key Components**: LTV / CAC, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback
- **Notes & Customizations**: The data is scaled by 1000.

### Cash Payback Calculation
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the monthly cash payback calculation.
- **Cell Range**: B45:Q241
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E45:Q45
    - **Data Range**:
      - Annual data: `E48:Q241`
- **Time Series Details**:
    - **Date Range**: 2021 to 2033
    - **Frequency**: Annual
- **Key Components**: Month, Multiplier, Increase
- **Notes & Customizations**: The data is scaled by 1000.

### Payback Period - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the key metrics used to calculate the payback period for the Financial division.
- **Cell Range**: B345:Q377
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G349:Q349
    - **Data Range**:
      - Annual data: `G349:Q377`
- **Time Series Details**:
    - **Date Range**: 2023 to 2033
    - **Frequency**: Annual
- **Key Components**: LTV / CAC, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback
- **Notes & Customizations**: The data is scaled by 1000.

### Cash Payback Calculation - Financial
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the monthly cash payback calculation for the Financial division.
- **Cell Range**: B378:Q574
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G479:Q479
    - **Data Range**:
      - Annual data: `G381:Q574`
- **Time Series Details**:
    - **Date Range**: 2023 to 2033
    - **Frequency**: Annual
- **Key Components**: Month, Multiplier, Increase
- **Notes & Customizations**: The data is scaled by 1000.

### Payback Period - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the key metrics used to calculate the payback period for the Corporate division.
- **Cell Range**: B576:Q608
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G580:Q580
    - **Data Range**:
      - Annual data: `G580:Q608`
- **Time Series Details**:
    - **Date Range**: 2023 to 2033
    - **Frequency**: Annual
- **Key Components**: LTV / CAC, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback
- **Notes & Customizations**: The data is scaled by 1000.

### Cash Payback Calculation - Corporate
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the monthly cash payback calculation for the Corporate division.
- **Cell Range**: B609:Q805
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G710:Q710
    - **Data Range**:
      - Annual data: `G612:Q805`
- **Time Series Details**:
    - **Date Range**: 2023 to 2033
    - **Frequency**: Annual
- **Key Components**: Month, Multiplier, Increase
- **Notes & Customizations**: The data is scaled by 1000.


====================================================================================================
# SHEET 7: Fin CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Fin CTRL
- **Key Sections Identified**:
    - Balance Sheet Support Assumptions
    - Interest Rate Assumptions
    - Effective Commission Rate & Day Sales Outstanding

## 2. Detailed Section Analysis

### Section Name: Balance Sheet Support Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains assumptions used to calculate balance sheet items, such as Days Sales Outstanding, Prepaid Expenses, Capital Expenditures, Accounts Payable Days, Commissions Payable, Accrued Expenses, Accrued Commissions, Accrued Wages, Accrued Holiday Pay, Accrued Interest, Payroll Taxes Payable, Sales Taxes Payable, Deferred Commissions, and Tekes projects. These assumptions are used to project future balance sheet values.
- **Cell Range**: A12:FS137
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `E14:Q137`
      - Monthly data: `T14:FS137`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Days Sales Outstanding, Prepaid Expenses (Monthly % of Operating Expenses), Capital Expenditures - % of Revenue, Accounts Payable Days Payable Outstanding, Commissions Payable - % of ARR, Accrued Expenses Days Payable Outstanding, Accrued Commissions - % of ARR, Accrued Wages - % Growth, Accrued Holiday Pay - % of Wages, Accrued Interest - % Growth, Payroll Taxes Payable - % Growth, Sales Taxes Payable - % of Revenue, Deferred Commissions Growth, Tekes projects.
- **Notes & Customizations**: The section includes a mix of percentage-based assumptions and days outstanding calculations. Some rows have "na" values in columns E and T. The scale is 1000 for most numeric values.

### Section Name: Interest Rate Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains assumptions related to interest rates, including the base interest rate, interest rate including admin fees, and interest rate on cash accounts. These assumptions are used to calculate interest expense and income.
- **Cell Range**: A140:FS151
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I140:Q151`
      - Monthly data: `T140:FS151`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Interest Rate, Interest Rate - Admin Fee.
- **Notes & Customizations**: The scale is 1000 for most numeric values.

### Section Name: Effective Commission Rate & Day Sales Outstanding
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains assumptions related to the effective commission rate, day sales outstanding, credit card payable, target hit rate, and LIBOR.
- **Cell Range**: A153:FS189
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `E161:Q189` (with gaps)
      - Monthly data: `T161:FS189` (with gaps)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Interest Rate on Cash Account, Percent of Cash in Account, Effective Commission Rate, Day Sales Outstanding, Credit Card Payable - % of OpEx, Target Hit Rate - Accrued Commission, LIBOR.
- **Notes & Customizations**: The scale is 1000 for some numeric values.


====================================================================================================
# SHEET 8: Fin
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Fin
- **Key Sections Identified**:
    - Income Statement
    - Balance Sheet
    - Cash Flow Statement
    - Balance Sheet Support
    - Long Term Liabilities
    - Equity Investment
    - Income Statement Support - Income Taxes

## 2. Detailed Section Analysis

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, showing revenues, expenses, and profit.
- **Cell Range**: B6:FS55
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3.
    - **Data Range**:
      - Annual data: E9:Q55
      - Monthly data: T9:FS55
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Operating Expenses, EBITDA, Depreciation, Interest Expense, Net Income.
- **Notes & Customizations**: Includes Intercompany Revenue / (Expenses).

### Balance Sheet
- **Section Type**: Balance Sheet
- **Description & Purpose**: Shows the company's assets, liabilities, and equity at a specific point in time.
- **Cell Range**: B57:FS139
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3.
    - **Data Range**:
      - Annual data: E62:Q139
      - Monthly data: T62:FS139
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Current Assets, Fixed Assets, Total Assets, Current Liabilities, Long Term Liabilities, Total Liabilities, Equity, Total Liabilities & Equity.
- **Notes & Customizations**: Includes a note about budgeted values in yellow.

### Cash Flow Statement
- **Section Type**: Standard Cash Flow Statement
- **Description & Purpose**: Summarizes the movement of cash and cash equivalents into and out of the company.
- **Cell Range**: B143:FS224
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3.
    - **Data Range**:
      - Annual data: E147:Q224
      - Monthly data: T147:FS224
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Net Income, Decrease (Increase) in Operating Assets, (Decrease) Increase in Operating Liabilities, Net Cash Flows from Operating Activities, Net Cash Flows from Investing Activities, Net Cash Flows from Financing Activities, Cash, End of Period.
- **Notes & Customizations**: Standard structure.

### Balance Sheet Support
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides supporting calculations and metrics related to the Balance Sheet.
- **Cell Range**: B228:FS682
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3.
    - **Data Range**:
      - Annual data: E234:Q682
      - Monthly data: T234:FS682
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Days in Period, Total Billings, Total Bookings, Days Sales Outstanding, Accounts Receivable, Allowance for Doubtful Accounts, Prepaid Expenses, Fixed Assets, Depreciation, Capex, Revenue.
- **Notes & Customizations**: Includes calculations for Days Sales Outstanding, prepaid expenses, and depreciation.

### Long Term Liabilities
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides supporting calculations and metrics related to Long Term Liabilities.
- **Cell Range**: A692:FS729
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3.
    - **Data Range**:
      - Annual data: E696:Q729
      - Monthly data: T696:FS729
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Tekes - 14887, Tekes - 15118, Tekes - 14560, Tekes - 14223, Tekes - 15543, Starting Balance (Long Term), Ending Balance, Interest Rate, Total Payback.
- **Notes & Customizations**: Includes calculations for payback.

### Equity Investment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides supporting calculations and metrics related to Equity Investment.
- **Cell Range**: A731:FS789
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3.
    - **Data Range**:
      - Annual data: E735:Q789
      - Monthly data: T735:FS789
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Net Investment Amount, Investment - 1st Close/2nd Close, MRR, Multiplier, Retention, Total Availability, Debt, Leverage, Interest Rates.
- **Notes & Customizations**: Includes calculations for debt and leverage.

### Income Statement Support - Income Taxes
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides supporting calculations and metrics related to Income Taxes.
- **Cell Range**: B791:FS836
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3.
    - **Data Range**:
      - Annual data: E793:Q836
      - Monthly data: T793:FS836
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Pre Tax Income, Starting NOL, NOL (Use) Add, Ending NOL, Taxable Income, Tax Rate, Taxes Paid, FCF, EBITDA, EBIT, NOPAT, Unlevered FCF, Adjusted FCF.
- **Notes & Customizations**: Includes calculations for NOL and FCF.


====================================================================================================
# SHEET 9: Debt Compliance
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Debt Compliance
- **Key Sections Identified**:
    - Revenue Growth Section
    - Debt Compliance Check Section
    - Liquidity Analysis Section

## 2. Detailed Section Analysis

### Revenue Growth Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays revenue and its growth rate. It's used to track the company's top-line performance.
- **Cell Range**: B6:ED10
- **Layout Structure**:
    - **Row Headers Location**: B6:B10
    - **Column Headers Location**: D3:M4, O3:ED4
    - **Data Range**:
      - Annual data: D8:M10
      - Monthly data: O8:ED10
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2018 to 2027
      - Monthly: 2018-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Revenue, Growth Rate, T3M
- **Notes & Customizations**: Revenue is scaled by 1000.

### Debt Compliance Check Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks various financial metrics and compares them against covenants to ensure compliance with debt agreements.
- **Cell Range**: B12:ED45
- **Layout Structure**:
    - **Row Headers Location**: B12:B45
    - **Column Headers Location**: O3:ED4
    - **Data Range**:
      - Monthly data: AP12:ED45
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2018-01-31 to 2027-12-31
    - **Frequency**:
      - Monthly
- **Key Components**: Growth Covenant, Remaining Months Liquidity (RML), Total Borrowings, Total Availability, EBITDA, Adjusted EBITDA, Liquidity Threshold
- **Notes & Customizations**: Includes "OK" compliance checks.

### Liquidity Analysis Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the company's liquidity position, including cash, availability, and buffers.
- **Cell Range**: B16:ED53
- **Layout Structure**:
    - **Row Headers Location**: B16:B53
    - **Column Headers Location**: O3:ED4
    - **Data Range**:
      - Monthly data: O18:ED53
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2018-01-31 to 2027-12-31
    - **Frequency**:
      - Monthly
- **Key Components**: Remaining Months Liquidity (RML), Total Borrowings, Total Availability, Cash, Net Availability + Unrestricted Cash, Liquidity Threshold, Restricted Cash, Net Availability, Liquidity, $5m Liquidity Buffer, RML Liquidity Buffer, Overall Liqudity Buffer
- **Notes & Customizations**: Includes liquidity buffers and thresholds.


====================================================================================================
# SHEET 10: ARR and Rev CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: ARR and Rev CTRL
- **Key Sections Identified**:
    - Revenue by Segment and Scenario
    - Quota by Role and Scenario
    - Productivity Metrics
    - ARR Metrics

## 2. Detailed Section Analysis

### Revenue by Segment and Scenario
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the revenue projections for different segments (Financial, Corporate, Other) under various scenarios (Base, Growth). It helps in understanding the revenue breakdown and potential growth opportunities.
- **Cell Range**: A12:FS32
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I15:Q32`
      - Monthly data: `T15:FS32`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Rev % of MRR - Financial, Rev % of MRR - Corporate, Rev % of MRR - Other, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Revenue is broken down by different segments and scenarios. The values are scaled by 1000.

### Quota by Role and Scenario
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the quota targets for different roles (Account Manager, AE - Financial, AE - Corporate, AE - Enterprise, VP Bus Dev) under various scenarios (Active, Base, Upside). It is used for setting sales targets and measuring performance.
- **Cell Range**: A35:FS118
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I38:Q118`
      - Monthly data: `BX38:FS118`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Quota, Account Manager - Active, Account Manager - Base, Account Manager - Upside, Quota - AE - Financial, Quota - AE - Corporate, Quota - AE - Enterprise, Quota - VP - Bus Dev
- **Notes & Customizations**: Quota targets are defined for different roles and scenarios. The values are scaled by 1000.

### Productivity Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section focuses on productivity metrics, including % of Quota, Seasonality, and Total ARR - % New Bookings, % Upsell. It helps in analyzing the efficiency and effectiveness of the sales team.
- **Cell Range**: A120:FS156
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I123:Q156`
      - Monthly data: `BX123:FS156`, `CB129:CM129`, `CN129:FS129`, `CB135:CM135`, `CN135:FS135`, `CB141:CM141`, `CN141:FS141`, `CB147:CM147`, `CN147:FS147`, `CB153:CM153`, `CN153:FS153`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Productivity - % of Quota, Seasonality, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev
- **Notes & Customizations**: Productivity metrics are calculated based on quota and revenue. The values are scaled by 1000.

### ARR Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides ARR-related metrics for different segments (Financial, Corporate, Other), including % YoY Growth and ARR / User. It is used to track the overall growth and performance of the company's recurring revenue.
- **Cell Range**: A158:FS318
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I161:Q318`, `E252:Q252`, `E259:Q259`, `E266:Q266`, `E276:Q276`, `E283:Q283`, `E290:Q290`, `I300:Q300`, `I307:Q307`, `I314:Q314`
      - Monthly data: `BX161:FS318`, `BX252:FS252`, `BX259:FS259`, `BX266:FS266`, `BX276:FS276`, `BX283:FS283`, `BX290:FS290`, `BX300:FS300`, `BX307:FS307`, `BX314:FS314`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total ARR - % New Bookings, Total ARR - % Upsell, Financial, Corporate, Other, % YoY Growth, ARR / User - Active, ARR / User - Base, ARR / User - Target
- **Notes & Customizations**: ARR metrics are calculated for different segments and scenarios. The values are scaled by 1000.


====================================================================================================
# SHEET 11: Sales Prod Input
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Sales Prod Input
- **Key Sections Identified**:
    - Input Parameters
    - Seasonality Adjustment
    - Productivity Calculation

## 2. Detailed Section Analysis

### Section Name: Input Parameters
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the quota per person for different roles within the sales organization. It serves as a primary input for subsequent productivity calculations.
- **Cell Range**: B5:Q11
- **Layout Structure**:
    - **Row Headers Location**: Column B (B7:B11) contains the role names.
    - **Column Headers Location**: Row 5 (B5) contains the general description, and Row 3 (F3:Q3) contains the dates.
    - **Data Range**:
      - Annual data: Not Applicable
      - Monthly data: F7:Q11 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**: 2021-01-31 to 2021-12-31
    - **Frequency**: Monthly
- **Key Components**: Quota per Person for Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise.
- **Notes & Customizations**: Quota values are scaled by 1000.

### Section Name: Seasonality Adjustment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the seasonality factors that will be applied to the productivity calculations.
- **Cell Range**: B13:Q15
- **Layout Structure**:
    - **Row Headers Location**: Column B (B15) contains the label "All Roles".
    - **Column Headers Location**: Row 3 (F3:Q3) contains the dates.
    - **Data Range**:
      - Annual data: Not Applicable
      - Monthly data: F15:Q15 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**: 2021-01-31 to 2021-12-31
    - **Frequency**: Monthly
- **Key Components**: Seasonality factors for all roles.
- **Notes & Customizations**: This section applies the same seasonality factor to all roles.

### Section Name: Productivity Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the productivity for each role, both raw and adjusted for seasonality.
- **Cell Range**: B17:Q31
- **Layout Structure**:
    - **Row Headers Location**: Column B (B19:B23, B27:B31) contains the role names.
    - **Column Headers Location**: Row 3 (F3:Q3) contains the dates.
    - **Data Range**:
      - Annual data: Not Applicable
      - Monthly data: F19:Q23, F27:Q31 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**: 2021-01-31 to 2021-12-31
    - **Frequency**: Monthly
- **Key Components**: Productivity and Productivity (Adjusted for Seasonality) for Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise.
- **Notes & Customizations**: Productivity is calculated for each role, and then adjusted based on the seasonality factors defined in the "Seasonality" section.


====================================================================================================
# SHEET 12: ARR and Revenue
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: ARR and Revenue
- **Key Sections Identified**:
    - ARR Summary
    - ARR by Segment
    - Revenue by Segment
    - Sales Productivity
    - Total Bookings by Segment
    - Financial ARR
    - Corporate ARR
    - Other ARR
    - Combined

## 2. Detailed Section Analysis

### Section Name: ARR Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a high-level overview of the company's ARR, including starting ARR, new business, upsell, churn, ending ARR, growth rates, churn rate, renewal metrics, and revenue. It's used to track overall business performance.
- **Cell Range**: B6:FS23
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 3
    - **Data Range**:
      - Annual data: `E8:Q23`
      - Monthly data: `T8:FS23`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: ARR - Start, New Business, Upsell, Churn, ARR - End, % YoY Growth, % Churn Rate, Up for Renewal, Retention Rate, Renewed, ARR, Revenue, % Growth
- **Notes & Customizations**: Includes calculations for growth and churn rates.

### Section Name: ARR by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down ARR by different segments (Financial, Corporate, Other). It's used to understand the contribution of each segment to the overall ARR.
- **Cell Range**: B25:FS31
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E28:Q31`
      - Monthly data: `T28:FS31`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total ARR
- **Notes & Customizations**: Segmented ARR reporting.

### Section Name: Revenue by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down Revenue by different segments (Financial, Corporate, Other). It's used to understand the contribution of each segment to the overall Revenue.
- **Cell Range**: B33:FS37
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E34:Q37`
      - Monthly data: `T34:FS37`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total Revenue
- **Notes & Customizations**: Segmented Revenue reporting.

### Section Name: Revenue as % of MRR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the Revenue as a percentage of MRR by different segments (Financial, Corporate, Other). It's used to understand the relationship between revenue and monthly recurring revenue.
- **Cell Range**: B40:FS43
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E40:Q43`
      - Monthly data: `T40:FS43`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total Revenue as % of MRR
- **Notes & Customizations**: Segmented Revenue as % of MRR reporting.

### Section Name: Sales Productivity
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes sales productivity metrics, including sales headcount and quota attainment.
- **Cell Range**: B45:FS89
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E48:Q89`
      - Monthly data: `T48:FS89`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Sales Headcount, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other, Total Quota, Total Bookings, Total Sales Headcount, Effective Sales Headcount, Total Effective Sales Reps, Quota per Person, Productivity - % of Quota (Adjusted for Seasonality), Total Productivity - % of Quota
- **Notes & Customizations**: Includes calculations for quota per person and productivity percentages.

### Section Name: Total Bookings by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down total bookings by segment (Financial, Corporate, Other). It provides insights into which segments are driving the most bookings.
- **Cell Range**: B153:FS157
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E154:Q157`
      - Monthly data: `T154:FS157`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total Bookings
- **Notes & Customizations**: Segmented bookings reporting.

### Section Name: New Bookings by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down new bookings by segment (Financial, Corporate, Other). It provides insights into which segments are driving the most new bookings.
- **Cell Range**: B160:FS164
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E161:Q164`
      - Monthly data: `T161:FS164`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total New Bookings
- **Notes & Customizations**: Segmented new bookings reporting.

### Section Name: Upsell by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down upsell bookings by segment (Financial, Corporate, Other). It provides insights into which segments are driving the most upsell bookings.
- **Cell Range**: B167:FS171
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E168:Q171`
      - Monthly data: `T168:FS171`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total Upsell
- **Notes & Customizations**: Segmented upsell bookings reporting.

### Section Name: Financial ARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the ARR specifically for the Financial segment.
- **Cell Range**: B174:FS189
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E176:Q189`
      - Monthly data: `T176:FS189`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Beginning ARR, New Business, Upsell, Churn, Ending ARR, % YoY Growth, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Notes & Customizations**: Focuses on the Financial segment's ARR performance.

### Section Name: Corporate ARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the ARR specifically for the Corporate segment.
- **Cell Range**: B191:FS206
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E193:Q206`
      - Monthly data: `T193:FS206`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Beginning ARR, New Business, Upsell, Churn, Ending ARR, % YoY Growth, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Notes & Customizations**: Focuses on the Corporate segment's ARR performance.

### Section Name: Other ARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the ARR specifically for the Other segment.
- **Cell Range**: B208:FS223
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E210:Q223`
      - Monthly data: `T210:FS223`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Beginning ARR, New Business, Upsell, Churn, Ending ARR, % YoY Growth, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Notes & Customizations**: Focuses on the Other segment's ARR performance.

### Section Name: Combined
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the combined ARR metrics.
- **Cell Range**: B225:FS233
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E227:Q233`
      - Monthly data: `T227:FS233`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Notes & Customizations**: Combines all segments ARR performance.


====================================================================================================
# SHEET 13: Sales CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Sales CTRL
- **Key Sections Identified**:
    - Header
    - Quota Sales Reps Headcount
    - Account Manager Headcount
    - AE - Financial Headcount
    - AE - Corporate Headcount
    - VP - Bus Dev Headcount
    - AE - Enterprise Headcount
    - AE - Other Headcount
    - Other Sales - Headcount
    - Ratios and Metrics
    - Old Assumptions (To Be Deleted)
    - Other Sales - Salary

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the spreadsheet's purpose.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: Company Name, Spreadsheet Description
- **Notes & Customizations**: None

### Quota Sales Reps Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the total headcount of quota-carrying sales representatives and their associated compensation.
- **Cell Range**: A12:Q26
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E14:Q19`
      - Monthly data: `T15:FS15`, `T22:FS22`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Total Headcount, Headcount Added in Period, Headcount Removed in Period, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Headcount is tracked for different revenue tiers.

### Account Manager Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Account Managers and their associated compensation.
- **Cell Range**: A15:FS26
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E15:Q19`, `E22:Q26`
      - Monthly data: `T15:FS15`, `T22:FS22`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Account Manager Headcount Added in Period, Account Manager Headcount Removed in Period, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Headcount is tracked for different revenue tiers.

### AE - Financial Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Financial and their associated compensation.
- **Cell Range**: A30:FS46
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E30:Q34`, `E36:Q40`, `E42:Q46`
      - Monthly data: `T30:FS30`, `T36:FS36`, `T42:FS42`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: AE - Financial Headcount Added in Period - Active, AE - Financial Headcount Added in Period - Base, AE - Financial Headcount Added in Period - Target, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Headcount is tracked for different revenue tiers.

### AE - Corporate Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Corporate and their associated compensation.
- **Cell Range**: A72:FS88
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E72:Q76`, `E78:Q82`, `E84:Q88`
      - Monthly data: `T72:FS72`, `T78:FS78`, `T84:FS84`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: AE - Corporate Headcount Added in Period - Active, AE - Corporate Headcount Added in Period - Base, AE - Corporate Headcount Added in Period - Target, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Headcount is tracked for different revenue tiers.

### VP - Bus Dev Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of VP - Bus Dev and their associated compensation.
- **Cell Range**: A114:FS125
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E114:Q118`, `E121:Q125`
      - Monthly data: `T114:FS114`, `T121:FS121`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: VP - Bus Dev Headcount Added in Period, VP - Bus Dev Headcount Removed in Period, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Headcount is tracked for different revenue tiers.

### AE - Enterprise Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Enterprise and their associated compensation.
- **Cell Range**: A129:Q140
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E129:Q133`, `E136:Q140`
      - Monthly data: `T129:FS129`, `T136:FS136`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: AE - Enterprise Headcount Added in Period, AE - Enterprise Headcount Removed in Period, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Headcount is tracked for different revenue tiers.

### AE - Other Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Other and their associated compensation.
- **Cell Range**: A144:Q155
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E144:Q148`, `E151:Q155`
      - Monthly data: `T144:FS144`, `T151:FS151`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: AE Other - Headcount Added in Period, AE Other - Headcount Removed in Period, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Headcount is tracked for different revenue tiers.

### Other Sales - Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Other Sales roles and their associated compensation.
- **Cell Range**: A263:Q272
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E267:Q272`
      - Monthly data: `T268:FS268`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: CRO - Added in Period, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Headcount is tracked for different revenue tiers.

### Ratios and Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Calculates various ratios and metrics related to sales team performance and efficiency.
- **Cell Range**: A274:FS322
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E274:Q274`, `E280:Q280`, `E286:Q286`, `E292:Q292`, `E299:Q299`, `E305:Q305`, `E311:Q311`, `E318:Q318`
      - Monthly data: `T274:FS274`, `T280:FS280`, `T286:CA286`, `CB286:FS286`, `T292:FS292`, `T299:FS299`, `T305:FS305`, `T311:FS311`, `T318:FS318`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Sales Manager - Reps per Manager, SDR Manager - SDR per Manager, SDRs - AE per SDR, SDRs - SDR per Manager, Account Manager - Corp - Corporate ARR per Manager, Account Manager - Fin - Financial ARR per Manager, Product Specialist per Manager, PSs - PS per AE
- **Notes & Customizations**: Includes metrics for ARR per manager and AE per SDR.

### Old Assumptions (To Be Deleted)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains old assumptions that are marked for deletion.
- **Cell Range**: A335:BW350
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E339:H339`
      - Monthly data: `T339:BW339`
- **Time Series Details**:
    - Annual: 2015 to 2018
    - Monthly: 2015-01-31 to 2018-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Manager - Corporate - Added in Period (2018 Driver), Manager - Corporate - AE Corp per Manager Corporate (2019 and Beyond Annual Driver)
- **Notes & Customizations**: This section is marked for deletion.

### Other Sales - Salary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the salary of Other Sales roles.
- **Cell Range**: A477:FS575
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7
    - **Data Range**:
      - Annual data: `E480:Q480`, `E487:Q487`, `E494:Q494`, `E501:Q501`, `T508:FS508`, `E515:Q515`, `E522:Q522`, `E529:Q529`, `E536:Q536`, `E543:Q543`, `E550:Q550`, `E557:Q557`, `E564:Q564`
      - Monthly data: `T480:FS480`, `T487:FS487`, `T494:FS494`, `T501:FS501`, `T508:FS508`, `T515:FS515`, `T522:FS522`, `T529:FS529`, `T536:FS536`, `T543:FS543`, `T550:FS550`, `T557:FS557`, `T564:FS564`, `T571:FS571`
- **Time Series Details**:
    - Annual: 2015 to 2027
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: CRO, Sales Manager, SDR Manager, SDR, CS Manager, Account Manager - Corporate, Account Manager - Financial, Product Specialist - Mgr, Product Specialist, Enablement Manager, Sales - Admin, Sales Operations Manager, Sales Operations, GTM Strategy
- **Notes & Customizations**: Includes salary for various sales roles.


====================================================================================================
# SHEET 14: Sales Role Input
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Sales Role Input
- **Key Sections Identified**:
    - Sales Role Input - Quota Bearing
    - Sales Role Input - Non-Quota (Non Formula)
    - Sales Role Input - Non-Quota (Formula)

## 2. Detailed Section Analysis

### Section Name (Sales Role Input - Quota Bearing)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the headcount and budget for quota-bearing sales roles, including AE - Corporate, AE - Financial, Account Manager, and VP Bus Dev. It tracks the beginning headcount, additions, losses, and ending headcount for each role. It also includes budget information.
- **Cell Range**: A10:BA36
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row F, Row 8
    - **Data Range**:
      - Monthly data: `F13:BA15`, `F19:BA22`, `F26:BA29`, `F33:BA36`
- **Time Series Details**:
    - **Date Range**: 2018-01-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: AE - Corporate, AE - Financial, Account Manager, VP Bus Dev, Beginning, Added, Lost, Ending.
- **Notes & Customizations**: Headcount data is scaled by 1000.

### Section Name (Sales Role Input - Non-Quota (Non Formula))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the headcount and budget for non-quota-bearing sales roles, specifically those without formulas. It includes roles like CRO, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy, and AM - Financial (Quota) moved to (Non-Quota).
- **Cell Range**: A38:CK46
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row F, Row 8
    - **Data Range**:
      - Monthly data: `AM40:CK46`
- **Time Series Details**:
    - **Date Range**: 2018-01-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: CRO, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy, AM - Financial (Quota) moved to (Non-Quota).
- **Notes & Customizations**: Headcount data is scaled by 1000.

### Section Name (Sales Role Input - Non-Quota (Formula))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the headcount and budget for non-quota-bearing sales roles, specifically those *with* formulas. It includes roles like VP of Sales (Reports per VP), VP of Sales (Total AE Reports), Sales Manager (AEs per Manager), SDR Manager (SDRs per Manager), SDR (AEs per SDR), VP Customer Success (AMs + PS Managers per VP), Corporate AM (ARR per AM), Financial AM (ARR per AM), Product Specialist Manager (PS per Manager), and Product Specialist (ARR per PS).
- **Cell Range**: A48:CK59
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row F, Row 8
    - **Data Range**:
      - Monthly data: `AM50:CK59`, `AM51:DD51`
- **Time Series Details**:
    - **Date Range**: 2018-01-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: VP of Sales (Reports per VP), VP of Sales (Total AE Reports), Sales Manager (AEs per Manager), SDR Manager (SDRs per Manager), SDR (AEs per SDR), VP Customer Success (AMs + PS Managers per VP), Corporate AM (ARR per AM), Financial AM (ARR per AM), Product Specialist Manager (PS per Manager), Product Specialist (ARR per PS).
- **Notes & Customizations**: Headcount data is scaled by 1000.



====================================================================================================
# SHEET 15: Sales Reps
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Sales Reps
- **Key Sections Identified**:
    - Header
    - Quota Sales Rep Summary
    - Non Quota'd Sales Team Summary
    - Quota Sales Rep Detail
    - Other Sales Detail
    - Quota Rep - Salary Summary
    - Quota Rep - Bonus Summary
    - Quota Rep - Salary Detail
    - Other Sales - Salary Detail
    - Total Sales Salary

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the spreadsheet and other identifying information.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:FS3
    - **Data Range**: E3:H3, I3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: E3 to Q3
        - Date Range: Not specified, but likely represents years.
        - Frequency: Annual
    - Monthly: T3 to FS3
        - Date Range: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: AlphaSense, Inc., Sales Reps Detail, 1 - Base - $25mm
- **Notes & Customizations**: Contains both annual and monthly time series.

### Quota Sales Rep Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of quota'd sales rep headcount and related metrics.
- **Cell Range**: B6:FS24
- **Layout Structure**:
    - **Row Headers Location**: B8, B9, B10, B11, B12, B13, B14, B15, B17, B18, B19, B20, B21, B22, B23, B24
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E9:Q24
      - Monthly data: T9:FS24
- **Time Series Details**:
    - Annual: E3 to Q3
        - Date Range: Not specified, but likely represents years.
        - Frequency: Annual
    - Monthly: T3 to FS3
        - Date Range: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Quota Sales Rep Headcount, AM - Financial, AE - Financial, AE - Corporate, VP - Partnerships, AE - Enterprise, AE - Other, Total Quota Sales Rep Headcount, Average Effective Quota Headcount, Total Average Effective Quota Headcount
- **Notes & Customizations**: Contains both annual and monthly time series.

### Non Quota'd Sales Team Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of non-quota'd sales team headcount and related metrics.
- **Cell Range**: B26:FS42
- **Layout Structure**:
    - **Row Headers Location**: B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E27:Q42
      - Monthly data: T27:FS42
- **Time Series Details**:
    - Annual: E3 to Q3
        - Date Range: Not specified, but likely represents years.
        - Frequency: Annual
    - Monthly: T3 to FS3
        - Date Range: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: CRO, VP of Sales, Sales Manager, SDR Manager, SDR, CS Manager, AM - Corporate, AM - Financial, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy, Total Non Quota'd Sales Team
- **Notes & Customizations**: Contains both annual and monthly time series.

### Quota Sales Rep Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of quota'd sales rep metrics, including ramp and attrition.
- **Cell Range**: B44:FS190
- **Layout Structure**:
    - **Row Headers Location**: B47, B49, B50, B51, B52, B54, B55, B56, B57, B58, B59, B60, B61, B62, B63, B64, B66, B67, B68, B71, B73, B74, B75, B76, B78, B79, B80, B81, B82, B83, B84, B85, B86, B87, B88, B89, B91, B92, B93, B96, B98, B99, B100, B101, B103, B104, B105, B106, B107, B108, B109, B110, B111, B112, B113, B114, B116, B117, B118, B121, B123, B124, B125, B126, B128, B129, B130, B131, B132, B133, B134, B135, B136, B137, B138, B140, B141, B142, B145, B147, B148, B149, B150, B152, B153, B154, B155, B156, B157, B158, B159, B160, B161, B162, B164, B165, B166, B169, B171, B172, B173, B174, B176, B177, B178, B179, B180, B181, B182, B183, B184, B185, B186, B188, B189, B190
    - **Column Headers Location**: E3:Q3, T3:FS3, C54:D54
    - **Data Range**:
      - Annual data: E49:Q190
      - Monthly data: T49:FS190
      - Ramp/Efficiency data: C55:D185
- **Time Series Details**:
    - Annual: E3 to Q3
        - Date Range: Not specified, but likely represents years.
        - Frequency: Annual
    - Monthly: T3 to FS3
        - Date Range: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Beginning of Period, Added, Removed, End of Period, Ramp, Efficiency, Month 1, Month 2, Month 3, Month 4, Month 5, Month 6, Month 7, Month 8, Month 9, Month 10, Attrition, Effective Start, Add, Effective End, VP - Bus Dev
- **Notes & Customizations**: Contains both annual and monthly time series.

### Other Sales Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of other sales team metrics.
- **Cell Range**: B192:FS325
- **Layout Structure**:
    - **Row Headers Location**: B194, B196, B198, B199, B200, B202, B204, B205, B206, B207, B208, B209, B210, B211, B213, B215, B216, B217, B218, B219, B220, B222, B224, B225, B226, B227, B228, B229, B231, B233, B234, B235, B236, B237, B238, B240, B242, B244, B245, B246, B247, B248, B249, B251, B253, B254, B255, B256, B257, B258, B260, B262, B263, B264, B265, B266, B267, B268, B269, B271, B273, B274, B275, B276, B277, B278, B281, B283, B284, B285, B286, B287, B288, B290, B292, B294, B295, B296, B299, B301, B302, B303, B306, B308, B309, B310, B313, B315, B316, B317, B319, B321, B323, B324, B325
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E198:Q325
      - Monthly data: T198:FS325
- **Time Series Details**:
    - Annual: E3 to Q3
        - Date Range: Not specified, but likely represents years.
        - Frequency: Annual
    - Monthly: T3 to FS3
        - Date Range: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Sales Team, CRO, VP of Sales, Sales Manager, Min. Required Sales Managers, SDR Manager, SDR, Customer Success, Customer Success Manager, Account Manager - Corporate, Account Manager - Financial, Product Specialist - Mgr, Operations, Enablement Manager, Sales - Admin, Sales Operations Manager, Sales Operations, Business Development, GTM Strategy
- **Notes & Customizations**: Contains both annual and monthly time series.

### Total Sales Heads
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of total sales heads, including added, removed, and end of period counts.
- **Cell Range**: B328:FS333
- **Layout Structure**:
    - **Row Headers Location**: B328, B330, B331, B332, B333
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E330:Q333
      - Monthly data: T330:FS333
- **Time Series Details**:
    - Annual: E3 to Q3
        - Date Range: Not specified, but likely represents years.
        - Frequency: Annual
    - Monthly: T3 to FS3
        - Date Range: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Total Sales Heads, Beginning of Period, Added, Removed, End of Period
- **Notes & Customizations**: Contains both annual and monthly time series.

### Quota Rep - Salary Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of quota rep salaries by role.
- **Cell Range**: B335:FS343
- **Layout Structure**:
    - **Row Headers Location**: B335, B337, B338, B339, B340, B341, B342, B343
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E337:Q343
      - Monthly data: T337:FS343
- **Time Series Details**:
    - Annual: E3 to Q3
        - Date Range: Not specified, but likely represents years.
        - Frequency: Annual
    - Monthly: T3 to FS3
        - Date Range: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Quota Rep - Salary Summary, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other, Total
- **Notes & Customizations**: Contains both annual and monthly time series.

### Quota Rep - Bonus Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of quota rep bonuses by role.
- **Cell Range**: B345:FS353
- **Layout Structure**:
    - **Row Headers Location**: B345, B347, B348, B349, B350, B351, B352, B353
    - **Column Headers Location**: I3:Q3, CB3:FS3
    - **Data Range**:
      - Annual data: I347:Q353
      - Monthly data: CB347:FS353
- **Time Series Details**:
    - Annual: I3 to Q3
        - Date Range: Not specified, but likely represents years.
        - Frequency: Annual
    - Monthly: CB3 to FS3
        - Date Range: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Quota Rep - Bonus Summary, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other, Total
- **Notes & Customizations**: Contains both annual and monthly time series.

### Quota Rep - Salary Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed salary information for quota reps.
- **Cell Range**: B355:FS415
- **Layout Structure**:
    - **Row Headers Location**: B355, B358, B360, B361, B362, B364, B365, B368, B370, B371, B372, B374, B375, B376, B378, B380, B381, B382, B384, B385, B386, B388, B390, B391, B392, B394, B395, B398, B400, B401, B402, B404, B405, B408, B410, B411, B412, B414, B415
    - **Column Headers Location**: E3:Q3, T3:FS3, I3:Q3, CB3:FS3
    - **Data Range**:
      - Annual data: E360:Q415
      - Monthly data: T360:FS415
      - Bonus data: I364:Q415, CB364:FS415
- **Time Series Details**:
    - Annual: E3 to Q3
        - Date Range: Not specified, but likely represents years.
        - Frequency: Annual
    - Monthly: T3 to FS3
        - Date Range: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Quota Rep - Salary Detail, Employees, Average Salary, Total Wages, Sales Bonus per Head, Total Sales Bonus, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other
- **Notes & Customizations**: Contains both annual and monthly time series.

### Other Sales - Salary Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed salary information for other sales roles.
- **Cell Range**: B418:FS524
- **Layout Structure**:
    - **Row Headers Location**: B418, B420, B422, B424, B425, B426, B428, B430, B431, B432, B434, B436, B437, B438, B440, B442, B443, B444, B446, B448, B449, B450, B452, B454, B456, B457, B458, B461, B463, B464, B465, B467, B469, B470, B471, B473, B475, B476, B477, B479, B481, B482, B483, B485, B487, B489, B490, B491, B493, B495, B496, B497, B499, B501, B502, B503, B505, B507, B508, B509, B511, B513, B515, B516, B517, B520, B522, B523, B524
    - **Column Headers Location**: J3:Q3, CJ3:FS3
    - **Data Range**:
      - Annual data: J424:Q524
      - Monthly data: CJ424:FS524
      - Average Employees data: E425:Q524
- **Time Series Details**:
    - Annual: J3 to Q3
        - Date Range: Not specified, but likely represents years.
        - Frequency: Annual
    - Monthly: CJ3 to FS3
        - Date Range: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Other Sales - Salary Detail, Sales Team, Non Quota'd Sales Team Summary, Average Employees, Average Salary, Total Wages, CRO, VP of Sales, Sales Manager, SDR Manager, SDR, Customer Success Manager, Account Manager - Corporate, Account Manager - Financial, Product Specialist - Mgr, Operations, Enablement Manager, Sales - Admin, Sales Operations Manager, Sales Operations, Business Development, GTM Strategy, Total Sales Salary
- **Notes & Customizations**: Contains both annual and monthly time series.


====================================================================================================
# SHEET 16: Clients CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Clients CTRL
- **Key Sections Identified**:
    - Header
    - Clients Control - Financial
    - Clients Control - Corporate
    - Clients Control - Other

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and sheet name for identification.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: Company Name, Sheet Name, Scenario Name.
- **Notes & Customizations**: Basic header information.

### Clients Control - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays financial metrics related to client acquisition and churn, broken down by different client segments.
- **Cell Range**: A7:FS32
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8 (Year and Month)
    - **Data Range**:
      - Annual data: E9:Q32
      - Monthly data: T9:FS32
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Year, Month, New Booked ARR per New Client, Churned ARR per Lost Client, % ARR Churn Attributable to Lost Clients, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: The annual data is scaled by 1000. The monthly data is also scaled by 1000. The data is segmented by different client revenue tiers.

### Clients Control - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays corporate metrics related to client acquisition and churn, broken down by different client segments.
- **Cell Range**: A35:FS55
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8 (Year and Month)
    - **Data Range**:
      - Annual data: E37:Q55
      - Monthly data: T37:FS55
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: New Booked ARR per New Client, Churned ARR per Lost Client, % ARR Churn Attributable to Lost Clients, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: The annual data is scaled by 1000. The monthly data is also scaled by 1000. The data is segmented by different client revenue tiers.

### Clients Control - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays other metrics related to client acquisition and churn, broken down by different client segments.
- **Cell Range**: A58:FS78
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8 (Year and Month)
    - **Data Range**:
      - Annual data: E60:Q78
      - Monthly data: T60:FS78
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: New Booked ARR per New Client, Churned ARR per Lost Client, % ARR Churn Attributable to Lost Clients, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: The annual data is scaled by 1000. The monthly data is also scaled by 1000. The data is segmented by different client revenue tiers.



====================================================================================================
# SHEET 17: Clients
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Clients
- **Key Sections Identified**:
    - Header
    - Clients Summary
    - Clients Detail - Financial
    - Client Detail - Corporate
    - Client Detail - Other

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and report title.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: B2:B4
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: Company Name, Report Title, Report Scope
- **Notes & Customizations**: None

### Clients Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of client metrics over time.
- **Cell Range**: B6:FS11
- **Layout Structure**:
    - **Row Headers Location**: B6:B11
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E8:Q11
      - Monthly data: T8:FS11
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Clients Summary, Beginning Clients, New Added, Churned, Ending Clients
- **Notes & Customizations**: Values are scaled by 1000.

### Clients Detail - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of financial client metrics over time.
- **Cell Range**: B13:FS30
- **Layout Structure**:
    - **Row Headers Location**: B13:B30
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E15:Q30
      - Monthly data: T15:FS30
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Clients Detail - Financial, Beginning Clients, New Added, Churned , Ending Clients, New Booked ARR - New Clients, Clients Added, New Booked ARR per New Client, Churned ARR - Lost Clients, Clients Lost, Churned ARR per Lost Client, Total Churned ARR, Churned ARR Attributable to Lost Clients, % of Churned ARR Attributable to Lost Clients
- **Notes & Customizations**: Values are scaled by 1000.

### Client Detail - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of corporate client metrics over time.
- **Cell Range**: B32:FS49
- **Layout Structure**:
    - **Row Headers Location**: B32:B49
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E34:Q49
      - Monthly data: T34:FS49
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Client Detail - Corporate, Beginning Clients, New Added, Churned, Ending Clients, New Booked ARR - New Clients, Clients Added, New Booked ARR per New Client, Churned ARR - Lost Clients, Clients Lost, Churned ARR per Lost Client, Total Churned ARR, Churned ARR Attributable to Lost Clients, % of Churned ARR Attributable to Lost Clients
- **Notes & Customizations**: Values are scaled by 1000.

### Client Detail - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of other client metrics over time.
- **Cell Range**: B51:FS68
- **Layout Structure**:
    - **Row Headers Location**: B51:B68
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E53:Q68
      - Monthly data: T53:FS68
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but implied to be a range of years.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Client Detail - Other, Beginning Clients, New Added, Churned, Ending Clients, New Booked ARR - New Clients, Clients Added, New Booked ARR per New Client, Churned ARR - Lost Clients, Clients Lost, Churned ARR per Lost Client, Total Churned ARR, Churned ARR Attributable to Lost Clients, % of Churned ARR Attributable to Lost Clients
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 18: Retention CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Retention CTRL
- **Key Sections Identified**:
    - Header
    - Retention Rate Table - Base - $25mm
    - Retention Rate Table - Growth - $25mm
    - Retention Rate Table - Base - $50mm
    - Retention Rate Table - Base - $50mm (R&D)

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and the title of the report.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: AlphaSense, Inc., Retention CTRL, 1 - Base - $25mm
- **Notes & Customizations**: None

### Section Name: Retention Rate Table - Base - $25mm
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual and monthly retention rates for the "Base - $25mm" scenario.
- **Cell Range**: B14:DV15
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7, Row 8
    - **Data Range**:
      - Annual data: I15:Q15
      - Monthly data: BX14:DV14
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Annual Retention % - Financial, Base - $25mm
- **Notes & Customizations**: Retention rates are scaled by 1000.

### Section Name: Retention Rate Table - Growth - $25mm
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention rates for the "Growth - $25mm" scenario.
- **Cell Range**: B14:DV16
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7, Row 8
    - **Data Range**:
      - Annual data: I16:Q16
      - Monthly data: None
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
    - **Frequency**:
      - Annual
- **Key Components**: Annual Retention % - Financial, Growth - $25mm
- **Notes & Customizations**: Retention rates are scaled by 1000.

### Section Name: Retention Rate Table - Base - $50mm
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention rates for the "Base - $50mm" scenario.
- **Cell Range**: B14:DV17
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7, Row 8
    - **Data Range**:
      - Annual data: I17:Q17
      - Monthly data: None
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
    - **Frequency**:
      - Annual
- **Key Components**: Annual Retention % - Financial, Base - $50mm
- **Notes & Customizations**: Retention rates are scaled by 1000.

### Section Name: Retention Rate Table - Base - $50mm (R&D)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention rates for the "Base - $50mm (R&D)" scenario.
- **Cell Range**: B14:DV18
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7, Row 8
    - **Data Range**:
      - Annual data: I18:Q18
      - Monthly data: None
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
    - **Frequency**:
      - Annual
- **Key Components**: Annual Retention % - Financial, Base - $50mm (R&D)
- **Notes & Customizations**: Retention rates are scaled by 1000.



====================================================================================================
# SHEET 19: Retention
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Retention
- **Key Sections Identified**:
    - Retention Summary - Financial
    - Retention Detail - Financial
    - Retention Summary - Corporate
    - Retention Detail - Corporate
    - Retention Summary - Other
    - Retention Detail - Other
    - Summary

## 2. Detailed Section Analysis

### Section Name: Retention Summary - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of financial retention metrics, including churn and retention rates. It helps track the overall financial health of customer retention.
- **Cell Range**: B8:FS18
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 3
    - **Data Range**:
      - Annual data: `E9:Q11`, `E12:Q12`, `E15:Q17`, `E18:Q18`
      - Monthly data: `T9:FS11`, `T12:FS12`, `T15:FS17`, `T18:FS18`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Churn, Total Churn, Blended Retention %
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Retention Detail - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of financial retention metrics, focusing on renewals and churn. It helps understand the dynamics of customer retention.
- **Cell Range**: B25:FS40
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E25:Q28`, `E30:Q31`, `J33:Q33`, `J39:Q39`, `E40:Q40`
      - Monthly data: `T25:FS28`, `CJ30:FS31`, `CI33:FS33`, `CJ34:FS38`, `CJ39:FS40`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal, Still Open in Previous Month, Renewal (default), Pending Cancel (notice given), Renewal - Won, Renewal - Lost
- **Notes & Customizations**: Values are scaled by 1000. There is a gap in the monthly data for some rows, starting at column `CJ`.

### Section Name: Retention Summary - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of corporate retention metrics, including churn and retention rates. It helps track the overall corporate health of customer retention.
- **Cell Range**: B44:FS59
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E44:Q47`, `E49:Q50`, `J52:Q52`, `J58:Q58`, `E59:Q59`
      - Monthly data: `T44:FS47`, `CJ49:FS50`, `CI52:FS52`, `CJ53:FS57`, `CJ58:FS59`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total Corporate Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal, Annual Up for Renewal
- **Notes & Customizations**: Values are scaled by 1000. There is a gap in the monthly data for some rows, starting at column `CJ`.

### Section Name: Retention Detail - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of "Other" retention metrics, focusing on renewals and churn. It helps understand the dynamics of customer retention for this specific category.
- **Cell Range**: B63:FS78
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E63:Q66`, `E68:Q69`, `J71:Q71`, `J77:Q77`, `E78:Q78`
      - Monthly data: `T63:FS66`, `CJ68:FS69`, `CI71:FS71`, `CJ72:FS76`, `CJ77:FS78`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total Other Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal, Annual Other Up for Renewal
- **Notes & Customizations**: Values are scaled by 1000. There is a gap in the monthly data for some rows, starting at column `CJ`.

### Section Name: Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a high-level summary of retention metrics.
- **Cell Range**: B82:FS86
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E82:Q84`
      - Monthly data: `T82:FS84`, `CJ86:FS86`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Up for Renewal, Retention %, Renewed, Churned
- **Notes & Customizations**: Values are scaled by 1000. There is a gap in the monthly data for some rows, starting at column `CJ`.


====================================================================================================
# SHEET 20: Renewed
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Renewed
- **Key Sections Identified**: 
    - Header
    - Renewal Data

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains column headers describing the data in the table below.
- **Cell Range**: A1:J1
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: A1:J1
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage
- **Notes & Customizations**: Standard header row.

### Renewal Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains the detailed data for each renewal, including account type, ASV, dates, segment, and stage.
- **Cell Range**: A2:J7599
- **Layout Structure**:
    - **Row Headers Location**: A2:A7599 (Account Type, etc.)
    - **Column Headers Location**: A1:J1 (ASV, Effective Date, etc.)
    - **Data Range**: 
      - Effective Date: C2:C5759 (date values)
      - EOM Effective Date: F2:F7599 (date values)
      - ASV: B2:B7599 (numeric values)
      - H2:H7599 (AlphaSense Opp #, string values)
      - I2:I7599 (Renewal Type, string values)
      - J2:J7599 (Stage, string values)
- **Time Series Details**:
    - **Date Range**: 
      - Effective Date: 2011-01-18 to 2022-01-01
      - EOM Effective Date: 1900-01-31 to 2022-01-31
    - **Frequency**: Unordered Column
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage
- **Notes & Customizations**: Contains a mix of string, numeric, and date data. The Effective Date and EOM Effective Date columns are date series. The "Stage" column contains information about the renewal stage (e.g., Renewal - Won, Renewal - Lost, etc.). There are multiple categories of Renewal Type and Stage.


====================================================================================================
# SHEET 21: Renewal Base
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Renewal Base
- **Key Sections Identified**: Data Table, Segment Key

## 2. Detailed Section Analysis

### Data Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains data on customer renewals, including account type, ASV (Annual Subscription Value), effective dates, close dates, and other relevant information. It is used to track and manage the renewal process.
- **Cell Range**: A1:J1858
- **Layout Structure**:
    - **Row Headers Location**: A1:A1858
    - **Column Headers Location**: A1:J1
    - **Data Range**:
      - ASV data: B2:B1858
      - AlphaSense Opp #: H2:H1858
      - Effective Date: C2:C1858
      - Close Date: D2:D1858
      - EOM Effective Date: F2:F1858
      - EOM Close Date: G2:G1858
- **Time Series Details**:
    - **Date Range**: 2019-02-01 to 2023-07-01
    - **Frequency**: Unordered
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage.
- **Notes & Customizations**: The "Note" in M1 indicates that the ASV data should be updated from the Sales Worksheet.

### Segment Key
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a key or legend for the "Segment" column in the Data Table. It explains what each segment represents.
- **Cell Range**: M2:N275
- **Layout Structure**:
    - **Row Headers Location**: M2:M275
    - **Column Headers Location**: M1
    - **Data Range**: N2:N275
- **Time Series Details**:
    - **Date Range**: N/A
    - **Frequency**: N/A
- **Key Components**: Segement Key, Account Type
- **Notes & Customizations**: This section is a lookup table, not a time series.


====================================================================================================
# SHEET 22: Deferred Build
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Deferred Build
- **Key Sections Identified**:
    - Header
    - Deferred Revenue Summary
    - Deferred Revenue Detail
    - Revenue Recognition Detail

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and scenario information.
- **Cell Range**: B2:Q4
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: E3:H3, I3:Q3
    - **Data Range**: E3:Q3
- **Time Series Details**:
    - Annual: Not explicitly defined, but E3:H3 and I3:Q3 suggest annual data. No specific date range is available.
    - Frequency: Annual (implied)
- **Key Components**: AlphaSense, Inc., Deferred Revenue Detail, 1 - Base - $25mm
- **Notes & Customizations**: Contains the title and scenario assumption.

### Deferred Revenue Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the deferred revenue balance, ARR, and related metrics over time.
- **Cell Range**: B6:DV14
- **Layout Structure**:
    - **Row Headers Location**: B6:B14
    - **Column Headers Location**: E8:Q8, T8:DV8
    - **Data Range**:
      - Annual data: E8:Q14
      - Monthly data: T8:DV14
- **Time Series Details**:
    - Annual: No specific date range is available.
    - Monthly: 2015-01-31 to 2027-12-31
    - Frequency:
      - Annual (implied)
      - Monthly
- **Key Components**: ARR, Deferred Beginning Balance, Add (Projected), Recognized as Revenue (Projected), Deferred Ending Balance, % of ARR
- **Notes & Customizations**: Contains both annual and monthly time series data. Values are scaled by 1000.

### Deferred Revenue Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of how ARR is added to the deferred revenue balance.
- **Cell Range**: B19:DV29
- **Layout Structure**:
    - **Row Headers Location**: B19:B29
    - **Column Headers Location**: BP22:DV22, BP23:DV23, BP24:DV24, BP27:DV27, BP28:DV28, BP29:DV29
    - **Data Range**:
      - Monthly data: BP22:DV24, BP27:DV29
- **Time Series Details**:
    - Monthly: 2015-01-31 to 2027-12-31
    - Frequency: Monthly
- **Key Components**: ARR Added, Renewals, Bookings, Total ARR Added Previous Month, Added to Deferred Revenue Balance, Total Added to Deferred Revenue Balance
- **Notes & Customizations**: Values are scaled by 1000.

### Revenue Recognition Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows how deferred revenue is recognized as revenue over time.
- **Cell Range**: B31:DV34
- **Layout Structure**:
    - **Row Headers Location**: B31:B34
    - **Column Headers Location**: BP32:DV32, BP33:DV33, BP34:DV34
    - **Data Range**:
      - Monthly data: BP32:DV34
- **Time Series Details**:
    - Monthly: 2015-01-31 to 2027-12-31
    - Frequency: Monthly
- **Key Components**: Revenue, Bookings Revenue Recognized, Renewal Revenue Recognized, Revenue from Deferred Revenue Balance
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 23: Headcount and Salaries CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Headcount and Salaries CTRL
- **Key Sections Identified**:
    - Header
    - Headcount Summary
    - ARR per Head Analysis
    - Salary Analysis

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and the report title.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: B2:B4
- **Time Series Details**: N/A
- **Key Components**: AlphaSense, Inc., Headcount and Salaries CTRL, 1 - Base - $25mm
- **Notes & Customizations**: Basic header information.

### Headcount Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the total headcount for each department over time.
- **Cell Range**: B12:FS18
- **Layout Structure**:
    - **Row Headers Location**: B12, B15, B17, B18
    - **Column Headers Location**: E7:Q7 (Year), T7:FS7 (Month)
    - **Data Range**:
      - Annual data: E17:Q17, E18:Q18
      - Monthly data: T18:FS18
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Headcount, Executive, Total Headcount, Executive Headcount Added in Period
- **Notes & Customizations**: Headcount data is scaled by 1000.

### ARR per Head Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes the ARR generated per headcount for different departments.
- **Cell Range**: B25:FS94
- **Layout Structure**:
    - **Row Headers Location**: B25, B28, B29, B30, B31, B32, B35, B38, B39, B40, B41, B42, B45, B48, B49, B50, B51, B52, B55, B58, B59, B60, B61, B62, B65, B68, B75, B76, B77, B78, B79, B82, B84, B85, B86, B87, B88, B90, B91, B92, B93, B94
    - **Column Headers Location**: E7:Q7 (Year), T7:FS7 (Month)
    - **Data Range**:
      - Annual data: E28:Q28, K29:Q29, K30:Q30, K31:Q31, K32:Q32, E38:Q38, K39:Q39, K40:Q40, K41:Q41, K42:Q42, E48:Q48, K49:Q49, K50:Q50, K51:Q51, K52:Q52, E58:Q58, K59:Q59, K60:Q60, K61:Q61, K62:Q62, E68:Q68, E75:Q75, K76:Q76, K77:Q77, K78:Q78, K79:Q79, J84:Q84, L85:Q85, L86:Q86, L87:Q87, L88:Q88, E90:Q90, E91:Q91, E92:Q92, E93:Q93, E94:Q94
      - Monthly data: T28:FS28, T38:FS38, T48:FS48, T58:FS58, T68:FS68, T75:FS75
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Engineering, ARR per Engineer - 2019+ Driver, Product, ARR per Product - 2019+ Driver, Marketing, ARR per Marketing Head, Content, ARR per Content Head, Finance, HR, and Operations, Finance, HR, and Operations Headcount Added in Period (2018 Driver), ARR per Finance, HR, and Operations Head (2019+ Driver), Engineering/Ops - India, Engineering/Ops - India - Added Heads, Average Engineering/Ops - India Salary
- **Notes & Customizations**: ARR per head data is scaled by 1000.

### Salary Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes the salary expenses for different departments.
- **Cell Range**: B96:FS152
- **Layout Structure**:
    - **Row Headers Location**: B96, B100, B101, B102, B103, B104, B108, B109, B110, B111, B112, B116, B117, B118, B119, B120, B124, B125, B126, B127, B128, B132, B133, B134, B135, B136, B140, B141, B142, B143, B144, B148, B149, B150, B151, B152
    - **Column Headers Location**: E7:Q7 (Year), T7:FS7 (Month)
    - **Data Range**:
      - Annual data: E100:Q100, I101:Q101, K102:Q102, K103:Q103, K104:Q104, E108:Q108, J109:Q109, K110:Q110, K111:Q111, K112:Q112, E116:Q116, J117:Q117, K118:Q118, K119:Q119, K120:Q120, E124:Q124, J125:Q125, K126:Q126, K127:Q127, K128:Q128, E132:Q132, J133:Q133, K134:Q134, K135:Q135, K136:Q136, E140:Q140, J141:Q141, K142:Q142, K143:Q143, K144:Q144, E148:Q148, J149:Q149, K150:Q150, K151:Q151, K152:Q152
      - Monthly data: T100:FS100, T108:FS108, T116:FS116, T124:FS124, T132:FS132, T140:FS140, T148:FS148
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Salary, Executive Salary, Engineering Salary, Product Salary, Marketing Salary, Content Salary, Finance, HR, Operations Salary, Engineering/Ops - India Salary, Annual Increase
- **Notes & Customizations**: Salary data is scaled by 1000.


====================================================================================================
# SHEET 24: Headcount and Salaries
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Headcount and Salaries
- **Key Sections Identified**:
    - Headcount and Salaries Summary
    - Memo: Average Headcount
    - Salary
    - Salary per Head
    - Headcount Detail
    - Salaries Detail

## 2. Detailed Section Analysis

### Section Name: Headcount and Salaries Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of headcount and salary information by department. This section is used to track overall staffing levels and compensation costs.
- **Cell Range**: B6:FS17
- **Layout Structure**:
    - **Row Headers Location**: B8:B17
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E9:Q17
      - Monthly data: T9:FS17
- **Time Series Details**:
    - **Date Range**:
      - Annual: Years are not explicitly provided in the JSON, but the range E3:H3 and I3:Q3 suggest a multi-year range.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Headcount for Executive, Engineering, Product, Sales, Marketing, Content, Finance & Admin, Engineering/Ops - India, Total Headcount.
- **Notes & Customizations**: Values are scaled by 1000. There are two distinct time series: annual and monthly.

### Section Name: Memo: Average Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides average headcount information by department. This section is used to track average staffing levels.
- **Cell Range**: B20:FS29
- **Layout Structure**:
    - **Row Headers Location**: B21:B29
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E21:Q29
      - Monthly data: T21:FS29
- **Time Series Details**:
    - **Date Range**:
      - Annual: Years are not explicitly provided in the JSON, but the range E3:H3 and I3:Q3 suggest a multi-year range.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Average Headcount for Executive, Engineering, Product, Sales, Marketing, Content, Finance, HR, and Operations, Engineering/Ops - India, Total Headcount.
- **Notes & Customizations**: Values are scaled by 1000. There are two distinct time series: annual and monthly.

### Section Name: Salary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides salary information by department. This section is used to track compensation costs.
- **Cell Range**: B31:FS41
- **Layout Structure**:
    - **Row Headers Location**: B32:B41
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E32:Q41
      - Monthly data: T32:FS41
- **Time Series Details**:
    - **Date Range**:
      - Annual: Years are not explicitly provided in the JSON, but the range E3:H3 and I3:Q3 suggest a multi-year range.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Salary for Executive, Engineering, Product, Sales, Marketing, Content, Finance & Admin, Engineering/Ops - India, Total Salary, Total Salary (excl. India).
- **Notes & Customizations**: Values are scaled by 1000. There are two distinct time series: annual and monthly.

### Section Name: Salary per Head
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides salary per headcount information by department. This section is used to track compensation costs per employee.
- **Cell Range**: B43:FS52
- **Layout Structure**:
    - **Row Headers Location**: B44:B52
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E44:Q52
      - Monthly data: T44:FS52
- **Time Series Details**:
    - **Date Range**:
      - Annual: Years are not explicitly provided in the JSON, but the range E3:H3 and I3:Q3 suggest a multi-year range.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Salary per Head for Executive, Engineering, Product, Sales, Marketing, Content, Finance & Admin, Engineering/Ops - India, Total Salary per Head.
- **Notes & Customizations**: Values are scaled by 1000. There are two distinct time series: annual and monthly.

### Section Name: Headcount Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed headcount information by department, tracking changes in headcount over time.
- **Cell Range**: B54:FS118
- **Layout Structure**:
    - **Row Headers Location**: B57:B118
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E59:Q63, E68:Q72, E77:Q81, E86:Q91, E96:Q100, E105:Q109, E114:Q118
      - Monthly data: U59:FS61, T62:FS63, U68:FS70, T71:FS72, U77:FS79, T80:FS81, T86:FS91, U96:FS98, T99:FS100, U105:FS107, T108:FS109, U114:FS116, T117:FS118
- **Time Series Details**:
    - **Date Range**:
      - Annual: Years are not explicitly provided in the JSON, but the range E3:H3 and I3:Q3 suggest a multi-year range.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Beginning of Period, Added, End of Period, ARR per Head, ARR, Net Added, Gross Added, Removed.
- **Notes & Customizations**: Values are scaled by 1000. There are two distinct time series: annual and monthly.

### Section Name: Salaries Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed salary information by department, including average employees, average salary, and total wages.
- **Cell Range**: B121:FS194
- **Layout Structure**:
    - **Row Headers Location**: B124:B194
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E126:Q128, E134:Q136, E142:Q144, E150:Q152, E158:Q160, E166:Q168, E174:Q176, G182:Q185, E188:Q194
      - Monthly data: T126:FS128, T134:FS136, T142:FS144, T150:FS152, T158:FS160, T166:FS168, T174:FS176, T182:FS185, T188:FS194
- **Time Series Details**:
    - **Date Range**:
      - Annual: Years are not explicitly provided in the JSON, but the range E3:H3 and I3:Q3 suggest a multi-year range.
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Average Employees, Average Salary, Total Wages, Added Employees, Total Salary (excluding Engineering / Ops - India), Plug, Wages (Income Statement), Wages (Income Statement) - PLUG.
- **Notes & Customizations**: Values are scaled by 1000. There are two distinct time series: annual and monthly.


====================================================================================================
# SHEET 25: Opex CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Opex CTRL
- **Key Sections Identified**: 
    - Header
    - Operating Expenses Inputs

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: AlphaSense, Inc., Operating Expenses CTRL, Scenario Description.
- **Notes & Customizations**: None

### Operating Expenses Inputs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the inputs and assumptions used to calculate operating expenses. It includes various cost categories and their associated drivers or growth rates.
- **Cell Range**: A7:FS610
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: E9:Q610
      - Monthly data: T9:FS610
- **Time Series Details**:
    - **Annual**: 2015 to 2027
    - **Monthly**: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Other Employee Costs, Travel, Other Costs, Other Facilities Cost, Marketing Cost, Non-Salary G&A Costs per Head, Legal Fees, Engineering Headcount Growth, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Benefits, Payroll Taxes, Relocation, Outsourced R&D, Capitalized Outsourced R&D, Capitalized R&D, Rent, Insurance, Payroll & Benefit Admin, Postage & Delivery, Bank Fees, Fundraising, DataFeeds, Bad Debt, Depreciation Expense, Amortization of Capitalized R&D, Subsidy Received, Other Income, Income Taxes, Other Taxes, Interest Income, Interest Expense, Gain / (Loss) on FX, Bonus, Contractors, Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions, Airfar/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment, SKO, President's Club, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, SWAG, Conferences & Meetings, Software, Audit & Tax, Professional Services, Legal Fees, Web Service, Intern Cost, Number of Interns, Other Contractors Cost, Percent of HC with T/E.
- **Notes & Customizations**: Many rows are defined as a percentage of wages or rent. Some rows have a "Buffer" designation.


====================================================================================================
# SHEET 26: Operating Expenses
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Operating Expenses
- **Key Sections Identified**:
    - Operating Expenses Summary
    - Operating Expenses Detail - People Costs
    - Operating Expenses Detail - Other Employee Costs
    - Operating Expenses Detail - Travel
    - Operating Expenses Detail - Facilities Costs
    - Operating Expenses Detail - Marketing
    - Operating Expenses Detail - General and Administrative
    - Operating Expenses Detail - Legal
    - Operating Expenses Detail - Other Costs

## 2. Detailed Section Analysis

### Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a high-level summary of the operating expenses. It's used to track overall spending trends.
- **Cell Range**: A6:FS21
- **Layout Structure**:
    - **Row Headers Location**: B6:B20
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E11:Q20
      - Monthly data: T11:FS20
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Operating Expenses, People Costs, Other Employee Costs, Travel, Facilities Costs, Rental Income, Marketing, General and Administrative, Legal, Other Costs, Total Operating Expenses, % YoY Growth
- **Notes & Customizations**: The values are scaled by 1000.

### Operating Expenses Detail - People Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: This section provides a detailed breakdown of people-related costs. It's used to understand the components of employee expenses.
- **Cell Range**: A23:FS43
- **Layout Structure**:
    - **Row Headers Location**: B23:B43
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E26:Q43
      - Monthly data: T26:FS43
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Commission, Stock Based Compensation, Bonus, Benefits, Worker Compensation, Finnish Side Costs, Recruiting Fees, Relocation, Contractors, Outsourced R&D, Capitalized Wages, Total People Costs
- **Notes & Customizations**: The values are scaled by 1000.

### Operating Expenses Detail - Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: This section provides a detailed breakdown of other employee-related costs. It's used to understand the components of employee expenses beyond salary.
- **Cell Range**: A45:FS53
- **Layout Structure**:
    - **Row Headers Location**: B45:B52
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E46:Q53
      - Monthly data: T46:FS53
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Cellular Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions, Total Other Employee Costs, % of Wages
- **Notes & Customizations**: The values are scaled by 1000.

### Operating Expenses Detail - Travel
- **Section Type**: Standard P&L
- **Description & Purpose**: This section provides a detailed breakdown of travel-related costs. It's used to understand the components of travel expenses.
- **Cell Range**: A55:FS67
- **Layout Structure**:
    - **Row Headers Location**: B55:B67
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E56:Q67
      - Monthly data: T56:FS67
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals, Daily Meal Allowance When Abroad, Business Meals, Internal Events, Total Travel Costs, % of Wages, Airfare % of Wages
- **Notes & Customizations**: The values are scaled by 1000.

### Operating Expenses Detail - Facilities Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: This section provides a detailed breakdown of facilities-related costs. It's used to understand the components of facilities expenses.
- **Cell Range**: A69:FS78
- **Layout Structure**:
    - **Row Headers Location**: B69:B78
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E70:Q78
      - Monthly data: T70:FS78
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Rent, CAM, Repairs & Maintenance, Utilities, Telephone, Computer & Internet, Total Facilities Costs, % YoY Growth, Other Facilities Costs - % of Rent
- **Notes & Customizations**: The values are scaled by 1000.

### Operating Expenses Detail - Marketing
- **Section Type**: Standard P&L
- **Description & Purpose**: This section provides a detailed breakdown of marketing-related costs. It's used to understand the components of marketing expenses.
- **Cell Range**: A80:FS95
- **Layout Structure**:
    - **Row Headers Location**: B80:B95
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E84:Q95
      - Monthly data: T84:FS95
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Rental Income, Total Rental Income, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG, Total Marketing Costs, Marketing Cost per Booking, Total Bookings
- **Notes & Customizations**: The values are scaled by 1000.

### Operating Expenses Detail - General and Administrative
- **Section Type**: Standard P&L
- **Description & Purpose**: This section provides a detailed breakdown of general and administrative-related costs. It's used to understand the components of G&A expenses.
- **Cell Range**: A97:FS113
- **Layout Structure**:
    - **Row Headers Location**: B97:B113
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E98:Q113
      - Monthly data: T98:FS113
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising Fees, Miscellaneous, Total General & Administrative Costs, $ per Headcount, Total Headcount
- **Notes & Customizations**: The values are scaled by 1000.

### Operating Expenses Detail - Legal
- **Section Type**: Standard P&L
- **Description & Purpose**: This section provides a detailed breakdown of legal-related costs. It's used to understand the components of legal expenses.
- **Cell Range**: A115:FS117
- **Layout Structure**:
    - **Row Headers Location**: B115:B117
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E116:Q117
      - Monthly data: T116:FS117
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Legal Fees, Total Legal Costs
- **Notes & Customizations**: The values are scaled by 1000.

### Operating Expenses Detail - Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: This section provides a detailed breakdown of other costs. It's used to understand the components of other expenses.
- **Cell Range**: A119:FS126
- **Layout Structure**:
    - **Row Headers Location**: B119:B126
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E120:Q126
      - Monthly data: T120:FS126
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: DataFeeds, Web Service, Penalties, Bad Debt, Total Other Costs, % YoY Growth, Other Costs (excl. Bad Debt)
- **Notes & Customizations**: The values are scaled by 1000.


====================================================================================================
# SHEET 27: Content
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Content
- **Key Sections Identified**:
    - Header
    - Content Operating Expenses Summary
    - Content People Costs Details
    - Content Other Employee Costs Details
    - Content Travel Costs Details
    - Content Facility Costs Details
    - Content Marketing Costs Details
    - Content General & Admin Costs Details
    - Content Other Costs Details

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description. Provides context for the entire spreadsheet.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 2015-01-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: AlphaSense, Inc., Operating Expenses Reorganization, 1 - Base - $25mm
- **Notes & Customizations**: Contains the scenario description "1 - Base - $25mm".

### Content Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of content operating expenses.
- **Cell Range**: A6:Q11
- **Layout Structure**:
    - **Row Headers Location**: B6, B8, B10, B11
    - **Column Headers Location**: E3:I3 (Implied Annual), J3:Q3 (Implied Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: I8:Q8, I10:Q11
- **Time Series Details**:
    - **Date Range**: 2015-01-31 to 2027-12-31
      - Annual: Implied (based on column headers)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Content Operating Expenses Summary, Total Content Expense, Total Content People Costs, Total Engineering People Costs (excl Cap Wages)
- **Notes & Customizations**: Values are scaled by 1000.

### Content People Costs Details
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the various components of content people costs, including wages, benefits, and other related expenses.
- **Cell Range**: A13:Q62
- **Layout Structure**:
    - **Row Headers Location**: B13:B62 (every other row)
    - **Column Headers Location**: E3:I3 (Implied Annual), J3:Q3 (Implied Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: I14:Q15, I19:Q19, I24:Q24, I28:Q28, I34:Q34, I36:Q36, I40:Q40, I44:Q44, I48:Q48, I52:Q52, I57:Q57, I62:Q62
- **Time Series Details**:
    - **Date Range**: 2015-01-31 to 2027-12-31
      - Annual: Implied (based on column headers)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Commission Expense, Bonus, Benefits, Work Compensation, Payroll Taxes, Finnish Side Costs, Share Based Compensation
- **Notes & Customizations**: Values are scaled by 1000. Includes "% of Wages" calculations.

### Content Other Employee Costs Details
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the various components of other employee costs, including recruiting fees, relocation, contractors, capitalized wages, and other related expenses.
- **Cell Range**: A64:Q113
- **Layout Structure**:
    - **Row Headers Location**: B64:B113 (every other row)
    - **Column Headers Location**: E3:I3 (Implied Annual), J3:Q3 (Implied Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: I81:Q81, I86:Q86, I92:Q92, I98:Q98, I101:Q101, I106:Q106, I111:Q111, I113:Q113
- **Time Series Details**:
    - **Date Range**: 2015-01-31 to 2027-12-31
      - Annual: Implied (based on column headers)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Recruiting Fees, Relocation, Contractors, Outsourced R&D, Capitalized Wages, Capitalized Outsourced R&D, Capitalized R&D, Total Content Other Employee Costs
- **Notes & Customizations**: Values are scaled by 1000.

### Content Travel Costs Details
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the various components of content travel costs, including airfare, lodging, meals, and other related expenses.
- **Cell Range**: A115:Q217
- **Layout Structure**:
    - **Row Headers Location**: B115:B217 (every other row)
    - **Column Headers Location**: E3:I3 (Implied Annual), J3:Q3 (Implied Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: I118:Q118, I123:Q123, I128:Q128, I133:Q133, I138:Q138, I143:Q143, I145:Q145, I154:Q154, I163:Q163, I172:Q172, I181:Q181, I190:Q190, I199:Q199, I208:Q208, I217:Q217
- **Time Series Details**:
    - **Date Range**: 2015-01-31 to 2027-12-31
      - Annual: Implied (based on column headers)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions, Total Content Travel Costs, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment
- **Notes & Customizations**: Values are scaled by 1000.

### Content Facility Costs Details
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the various components of content facility costs, including rent, utilities, and other related expenses.
- **Cell Range**: A220:Q264
- **Layout Structure**:
    - **Row Headers Location**: B220:B264 (every other row)
    - **Column Headers Location**: E3:I3 (Implied Annual), J3:Q3 (Implied Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: I227:Q227, I229:Q229, I234:Q234, I239:Q239, I244:Q244, I249:Q249, I254:Q254, I259:Q259, I264:Q264
- **Time Series Details**:
    - **Date Range**: 2015-01-31 to 2027-12-31
      - Annual: Implied (based on column headers)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Internal Events, Total Content Facility Costs, Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet
- **Notes & Customizations**: Values are scaled by 1000.

### Content Marketing Costs Details
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the various components of content marketing costs, including advertising, research, events, and other related expenses.
- **Cell Range**: A266:Q311
- **Layout Structure**:
    - **Row Headers Location**: B266:B311 (every other row)
    - **Column Headers Location**: E3:I3 (Implied Annual), J3:Q3 (Implied Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: I271:Q271, I276:Q276, I281:Q281, I286:Q286, I291:Q291, I296:Q296, I301:Q301, I306:Q306, I311:Q311
- **Time Series Details**:
    - **Date Range**: 2015-01-31 to 2027-12-31
      - Annual: Implied (based on column headers)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Total Content Marketing, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Values are scaled by 1000.

### Content General & Admin Costs Details
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the various components of content general and administrative costs, including insurance, payroll administration, and other related expenses.
- **Cell Range**: A313:Q372
- **Layout Structure**:
    - **Row Headers Location**: B313:B372 (every other row)
    - **Column Headers Location**: E3:I3 (Implied Annual), J3:Q3 (Implied Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: I316:Q316, I321:Q321, I326:Q326, I329:Q329, I334:Q334, I339:Q339, I344:Q344, I349:Q349, I352:Q352, I357:Q357, I362:Q362, I367:Q367, I372:Q372
- **Time Series Details**:
    - **Date Range**: 2015-01-31 to 2027-12-31
      - Annual: Implied (based on column headers)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Total Content General & Admin, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising, Miscellaneous
- **Notes & Customizations**: Values are scaled by 1000.

### Content Other Costs Details
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the various components of content other costs, including legal fees, data feeds, web service, and other related expenses.
- **Cell Range**: A374:Q399
- **Layout Structure**:
    - **Row Headers Location**: B374:B399 (every other row)
    - **Column Headers Location**: E3:I3 (Implied Annual), J3:Q3 (Implied Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: I379:Q379, I384:Q384, I389:Q389, I394:Q394, I399:Q399
- **Time Series Details**:
    - **Date Range**: 2015-01-31 to 2027-12-31
      - Annual: Implied (based on column headers)
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual: Annual
      - Monthly: Monthly
- **Key Components**: Total Content Other Costs, Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 28: Engineering
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Engineering
- **Key Sections Identified**:
    - Header
    - Engineering Operating Expenses Summary
    - Engineering People Costs
    - Engineering Other Employee Costs
    - Engineering Travel Costs
    - Engineering Facility Costs
    - Engineering Marketing
    - Engineering General & Admin
    - Engineering Other Costs

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:FS3 (Years and Months)
    - **Data Range**: E3:Q3, J3:Q3, T3:FS3
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not explicitly defined, but implied from E3:Q3 and J3:Q3. Assuming 2015 to 2027 based on other sections.
        - **Frequency**: Annual
    - **Monthly**:
        - **Date Range**: 2015-01-31 to 2027-12-31
        - **Frequency**: Monthly
- **Key Components**: Company Name, Report Title, Scenario Description
- **Notes & Customizations**: Contains both annual and monthly time series data.

### Engineering Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of total engineering expenses.
- **Cell Range**: A6:Q11
- **Layout Structure**:
    - **Row Headers Location**: A6:B11
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I8:Q8, I10:Q10, I11:Q11
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Assuming 2015 to 2027 based on other sections.
        - **Frequency**: Annual
- **Key Components**: Total Engineering Expense, Total Engineering People Costs, Total Engineering People Costs (excl Cap Wages)
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering People Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering people costs.
- **Cell Range**: B13:Q62
- **Layout Structure**:
    - **Row Headers Location**: B13:B62
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I14:Q14, I15:Q15, I19:Q19, I24:Q24, I29:Q29, I34:Q34, I36:Q36, I40:Q40, I44:Q44, I48:Q48, I52:Q52, I56:K56, I57:Q57, I62:Q62
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Assuming 2015 to 2027 based on other sections.
        - **Frequency**: Annual
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finnish Side Costs, Share Based Compensation
- **Notes & Customizations**: Values are scaled by 1000. Contains "% of Wages" and "% of Headcount (Finland)" metrics.

### Engineering Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of other employee costs.
- **Cell Range**: A113:Q143
- **Layout Structure**:
    - **Row Headers Location**: B113:B143
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I113:Q113, I118:Q118, I123:Q123, I128:Q128, I133:Q133, I138:Q138, I143:Q143
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Assuming 2015 to 2027 based on other sections.
        - **Frequency**: Annual
- **Key Components**: Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Travel Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of travel costs.
- **Cell Range**: A145:Q217
- **Layout Structure**:
    - **Row Headers Location**: B145:B217
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I145:Q145, I154:Q154, I163:Q163, I172:Q172, I181:Q181, I190:Q190, I199:Q199, I217:Q217
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Assuming 2015 to 2027 based on other sections.
        - **Frequency**: Annual
- **Key Components**: Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Business Meals / Entertainment
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Facility Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of facility costs.
- **Cell Range**: A229:Q264
- **Layout Structure**:
    - **Row Headers Location**: B229:B264
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I229:Q229, I234:Q234, I239:Q239, I244:Q244, I249:Q249, I254:Q254, I259:Q259, I264:Q264
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Assuming 2015 to 2027 based on other sections.
        - **Frequency**: Annual
- **Key Components**: Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Marketing
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of marketing expenses.
- **Cell Range**: A266:Q311
- **Layout Structure**:
    - **Row Headers Location**: B266:B311
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I266:Q266, I271:Q271, I276:Q276, I281:Q281, I286:Q286, I291:Q291, I296:Q296, I301:Q301, I306:Q306, I311:Q311
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Assuming 2015 to 2027 based on other sections.
        - **Frequency**: Annual
- **Key Components**: Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering General & Admin
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of general and administrative expenses.
- **Cell Range**: A313:Q357
- **Layout Structure**:
    - **Row Headers Location**: B313:B357
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I313:Q313, I316:Q316, I321:Q321, I326:Q326, I329:Q329, I334:Q334, I339:Q339, I344:Q344, I349:Q349, I352:Q352, I357:Q357
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Assuming 2015 to 2027 based on other sections.
        - **Frequency**: Annual
- **Key Components**: Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of other costs.
- **Cell Range**: A372:Q397
- **Layout Structure**:
    - **Row Headers Location**: B372:B397
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I372:Q372, I377:Q377, I382:Q382, I387:Q387, I392:Q392, I397:Q397
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Assuming 2015 to 2027 based on other sections.
        - **Frequency**: Annual
- **Key Components**: Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 29: Executive
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Executive
- **Key Sections Identified**:
    - Title and Context
    - Executive Operating Expenses Summary
    - Executive People Costs
    - Executive Other Employee Costs
    - Executive Travel Costs
    - Executive Facility Costs
    - Executive Marketing
    - Executive General & Admin
    - Executive Other Costs

## 2. Detailed Section Analysis

### Title and Context
- **Section Type**: Title and Context
- **Description & Purpose**: Provides the title of the report, the company name, and context about the operating expenses reorganization.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: E3:FS3 (Annual and Monthly)
    - **Data Range**: E3:Q3 (Annual), T3:FS3 (Monthly)
- **Time Series Details**:
    - **Annual**: Not explicitly defined, but implied from E3:Q3. Years are not provided in the JSON.
    - **Monthly**: 2015-01-31 to 2027-12-31
    - **Frequency**:
        - Annual: Annual (Implied)
        - Monthly: Monthly
- **Key Components**: AlphaSense, Inc., Operating Expenses Reorganization, 1 - Base - $25mm
- **Notes & Customizations**: Contains both annual and monthly time series in the same row.

### Executive Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the total executive expenses.
- **Cell Range**: A6:Q8
- **Layout Structure**:
    - **Row Headers Location**: A6, B6, B8
    - **Column Headers Location**: I3:Q3 (Annual)
    - **Data Range**: I8:Q8
- **Time Series Details**:
    - **Annual**: Not explicitly defined, but implied from I3:Q3. Years are not provided in the JSON.
    - **Frequency**: Annual (Implied)
- **Key Components**: Executive Operating Expenses Summary, Total Executive Expense
- **Notes & Customizations**: Values are scaled by 1000.

### Executive People Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the total executive people costs.
- **Cell Range**: A10:Q62
- **Layout Structure**:
    - **Row Headers Location**: A10:B62
    - **Column Headers Location**: I3:Q3 (Annual)
    - **Data Range**: I10:Q62
- **Time Series Details**:
    - **Annual**: Not explicitly defined, but implied from I3:Q3. Years are not provided in the JSON.
    - **Frequency**: Annual (Implied)
- **Key Components**: Total Executive People Costs, Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Commission Expense, Bonus, Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation, Headcount, Cost Per Head
- **Notes & Customizations**: Values are scaled by 1000. Includes "% of Wages" calculations.

### Executive Other Employee Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the total executive other employee costs.
- **Cell Range**: A113:Q143
- **Layout Structure**:
    - **Row Headers Location**: A113:B143
    - **Column Headers Location**: I3:Q3 (Annual)
    - **Data Range**: I113:Q143
- **Time Series Details**:
    - **Annual**: Not explicitly defined, but implied from I3:Q3. Years are not provided in the JSON.
    - **Frequency**: Annual (Implied)
- **Key Components**: Total Executive Other Employee Costs, Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions
- **Notes & Customizations**: Values are scaled by 1000.

### Executive Travel Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the total executive travel costs.
- **Cell Range**: A145:Q227
- **Layout Structure**:
    - **Row Headers Location**: A145:B227
    - **Column Headers Location**: I3:Q3 (Annual)
    - **Data Range**: I145:Q227
- **Time Series Details**:
    - **Annual**: Not explicitly defined, but implied from I3:Q3. Years are not provided in the JSON.
    - **Frequency**: Annual (Implied)
- **Key Components**: Total Executive Travel Costs, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment, Internal Events
- **Notes & Customizations**: Values are scaled by 1000. Includes SKO and President's Club costs.

### Executive Facility Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the total executive facility costs.
- **Cell Range**: A229:Q264
- **Layout Structure**:
    - **Row Headers Location**: A229:B264
    - **Column Headers Location**: I3:Q3 (Annual)
    - **Data Range**: I229:Q264
- **Time Series Details**:
    - **Annual**: Not explicitly defined, but implied from I3:Q3. Years are not provided in the JSON.
    - **Frequency**: Annual (Implied)
- **Key Components**: Total Executive Facility Costs, Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet, Headcount
- **Notes & Customizations**: Values are scaled by 1000. Rent is calculated based on % of Headcount.

### Executive Marketing
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the total executive marketing expenses.
- **Cell Range**: A266:Q311
- **Layout Structure**:
    - **Row Headers Location**: A266:B311
    - **Column Headers Location**: I3:Q3 (Annual)
    - **Data Range**: I266:Q311
- **Time Series Details**:
    - **Annual**: Not explicitly defined, but implied from I3:Q3. Years are not provided in the JSON.
    - **Frequency**: Annual (Implied)
- **Key Components**: Total Executive Marketing, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Values are scaled by 1000.

### Executive General & Admin
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the total executive general and admin expenses.
- **Cell Range**: A313:Q374
- **Layout Structure**:
    - **Row Headers Location**: A313:B374
    - **Column Headers Location**: I3:Q3 (Annual)
    - **Data Range**: I313:Q374
- **Time Series Details**:
    - **Annual**: Not explicitly defined, but implied from I3:Q3. Years are not provided in the JSON.
    - **Frequency**: Annual (Implied)
- **Key Components**: Total Executive General & Admin, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising, Miscellaneous
- **Notes & Customizations**: Values are scaled by 1000.

### Executive Other Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the total executive other costs.
- **Cell Range**: A376:Q399
- **Layout Structure**:
    - **Row Headers Location**: A376:B399
    - **Column Headers Location**: I3:Q3 (Annual)
    - **Data Range**: I376:Q399
- **Time Series Details**:
    - **Annual**: Not explicitly defined, but implied from I3:Q3. Years are not provided in the JSON.
    - **Frequency**: Annual (Implied)
- **Key Components**: Total Executive Other Costs, Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 30: Finance & Admin
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Finance & Admin
- **Key Sections Identified**:
    - Title & Scenario
    - Finance & Admin Operating Expenses Summary
    - Wages Breakdown
    - Recruiting Fees Breakdown
    - Relocation Expenses
    - Contractors Expenses
    - Outsourced R&D Expenses
    - Capitalized Expenses
    - Other Employee Costs
    - Travel Costs
    - Internal Events
    - Facility Costs
    - Rental Income
    - Marketing Expenses
    - General & Admin Expenses
    - Other Costs
    - Bad Debt

## 2. Detailed Section Analysis

### Title & Scenario
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the spreadsheet and the scenario being modeled.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:H3, I3:Q3, T3:FS3
    - **Data Range**: None
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
    - **Monthly**:
        - **Date Range**: 2015-01-31 to 2027-12-31
        - **Frequency**: Monthly
- **Key Components**: AlphaSense, Inc., Operating Expenses Reorganization, 1 - Base - $25mm
- **Notes & Customizations**: Contains both annual and monthly time series.

### Finance & Admin Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the total Finance & Admin expenses, excluding capitalized wages.
- **Cell Range**: A6:Q11
- **Layout Structure**:
    - **Row Headers Location**: B6:B11
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I8:Q11
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Total Finance & Admin Expense, Total Finance & Admin Expense (excl Cap Wages), Total Finance & Admin Admin Costs, Total Engineering Admin Costs (excl Cap Wages)
- **Notes & Customizations**: Values are scaled by 1000.

### Wages Breakdown
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of wages for the Finance & Admin department.
- **Cell Range**: B13:Q52
- **Layout Structure**:
    - **Row Headers Location**: B13:B52
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I14:Q52
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes
- **Notes & Customizations**: Values are scaled by 1000. Includes "% of Wages" calculations.

### Recruiting Fees Breakdown
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of recruiting fees for the Finance & Admin department.
- **Cell Range**: B64:Q81
- **Layout Structure**:
    - **Row Headers Location**: B64:B81
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I81:Q81
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Recruiting Fees, Greenhouse PRO, Jopwell, Underdog, Linkedin Enterprise, Lusha, HackerRank, Built in NYC, Hirist, Glassdoor, Mercer, Docusign, Event & Meetups, Swag, Career Fairs, Other Costs, Finance & Admin Recruiting Fees
- **Notes & Customizations**: Values are scaled by 1000.

### Relocation Expenses
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the relocation expenses for the Finance & Admin department.
- **Cell Range**: B83:Q86
- **Layout Structure**:
    - **Row Headers Location**: B83:B86
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I86:Q86
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Relocation, Finance & Admin Relocation, Headcount, Cost Per Head
- **Notes & Customizations**: Values are scaled by 1000.

### Contractors Expenses
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the contractor expenses for the Finance & Admin department.
- **Cell Range**: B88:Q92
- **Layout Structure**:
    - **Row Headers Location**: B88:B92
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I92:Q92
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Contractors, Finance & Admin Contractors
- **Notes & Customizations**: Values are scaled by 1000.

### Outsourced R&D Expenses
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the outsourced R&D expenses for the Finance & Admin department.
- **Cell Range**: B95:Q98
- **Layout Structure**:
    - **Row Headers Location**: B95:B98
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I98:Q98
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Outsourced R&D, Finance & Admin Outsourced R&D
- **Notes & Customizations**: Values are scaled by 1000.

### Capitalized Expenses
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the capitalized wages and outsourced R&D expenses for the Finance & Admin department.
- **Cell Range**: B100:Q107
- **Layout Structure**:
    - **Row Headers Location**: B100:B107
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I101:Q107
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Capitalized Wages, Capitalized Outsourced R&D, Capitalized R&D, Finance & Admin Capitalized Wages, Finance & Admin Capitalized Outsourced R&D, Finance & Admin Capitalized R&D
- **Notes & Customizations**: Values are scaled by 1000.

### Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other employee costs for the Finance & Admin department.
- **Cell Range**: A113:Q143
- **Layout Structure**:
    - **Row Headers Location**: B113:B143
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I118:Q143
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Total Finance & Admin Other Employee Costs, Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions, Headcount, Cost Per Head
- **Notes & Customizations**: Values are scaled by 1000.

### Travel Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details travel costs for the Finance & Admin department.
- **Cell Range**: A145:Q217
- **Layout Structure**:
    - **Row Headers Location**: B145:B217
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I154:Q217
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Total Finance & Admin Travel Costs, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Business Meals / Entertainment, Daily Meal Allowance When Abroad, Headcount, Cost Per Head
- **Notes & Customizations**: Values are scaled by 1000.

### Internal Events
- **Section Type**: Standard P&L
- **Description & Purpose**: Details internal event costs for the Finance & Admin department.
- **Cell Range**: B219:Q227
- **Layout Structure**:
    - **Row Headers Location**: B219:B227
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I227:Q227
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Internal Events, SKO Cost Per Head, Total SKO Cost, President's Club Cost Per Head, % of Finance & Admin Attendees, Total Presiden's Club Cost, Other Internal Events, Finance & Admin Internal Events
- **Notes & Customizations**: Values are scaled by 1000.

### Facility Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details facility costs for the Finance & Admin department.
- **Cell Range**: A229:Q264
- **Layout Structure**:
    - **Row Headers Location**: B229:B264
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I234:Q264
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Total Finance & Admin Facility Costs, Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet, Headcount
- **Notes & Customizations**: Values are scaled by 1000.

### Rental Income
- **Section Type**: Standard P&L
- **Description & Purpose**: Details rental income for the Finance & Admin department.
- **Cell Range**: A266:Q269
- **Layout Structure**:
    - **Row Headers Location**: B266:B269
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I269:Q269
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Total Finance & Admin Rental Income, Rental Income, Finance & Admin Rental Income
- **Notes & Customizations**: Values are scaled by 1000.

### Marketing Expenses
- **Section Type**: Standard P&L
- **Description & Purpose**: Details marketing expenses for the Finance & Admin department.
- **Cell Range**: A271:Q316
- **Layout Structure**:
    - **Row Headers Location**: B271:B316
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I276:Q316
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Total Finance & Admin Marketing, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG, Headcount, Cost Per Head
- **Notes & Customizations**: Values are scaled by 1000.

### General & Admin Expenses
- **Section Type**: Standard P&L
- **Description & Purpose**: Details general & admin expenses for the Finance & Admin department.
- **Cell Range**: A318:Q359
- **Layout Structure**:
    - **Row Headers Location**: B318:B359
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I326:Q359
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Total Finance & Admin General & Admin, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Headcount, Cost Per Head
- **Notes & Customizations**: Values are scaled by 1000.

### Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other costs for the Finance & Admin department.
- **Cell Range**: A380:Q398
- **Layout Structure**:
    - **Row Headers Location**: B380:B398
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I383:Q398
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Total Finance & Admin Other Costs, Legal Fees, DataFeeds, Web Service, Penalties, Headcount, Cost Per Head
- **Notes & Customizations**: Values are scaled by 1000.

### Bad Debt
- **Section Type**: Standard P&L
- **Description & Purpose**: Details bad debt for the Finance & Admin department.
- **Cell Range**: B400:Q405
- **Layout Structure**:
    - **Row Headers Location**: B400:B405
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I403:Q405
- **Time Series Details**:
    - **Annual**:
        - **Date Range**: Not specified, but likely represents years based on the column headers.
        - **Frequency**: Annual
- **Key Components**: Bad Debt, Finance & Admin Bad Debt
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 31: Marketing
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Marketing
- **Key Sections Identified**:
    - Header
    - Marketing Operating Expenses Summary
    - Marketing People Costs
    - Marketing Other Employee Costs
    - Marketing Travel Costs
    - Marketing Facility Costs
    - Marketing Marketing
    - Marketing General & Admin
    - Marketing Other Costs
    - Marketing Performance Metrics

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: E3:FS3
    - **Data Range**: E3:Q3, I3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: Start Year Unknown, End Year Unknown
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Company Name, Report Title, Scenario Description
- **Notes & Customizations**: Contains both annual and monthly time series.

### Section Name: Marketing Operating Expenses Summary
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents a summary of the total marketing expenses.
- **Cell Range**: A6:Q8
- **Layout Structure**:
    - **Row Headers Location**: B6:B8
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I8:Q8
- **Time Series Details**:
    - Annual: Start Year Unknown, End Year Unknown
    - **Frequency**: Annual
- **Key Components**: Total Marketing Expense
- **Notes & Customizations**: Scaled by 1000.

### Section Name: Marketing People Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various costs associated with marketing personnel.
- **Cell Range**: A10:Q62
- **Layout Structure**:
    - **Row Headers Location**: B10:B62
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I10:Q10, I14:Q14, I15:Q15, I19:Q19, I24:Q24, I28:Q28, I34:Q34, I36:Q36, I40:Q40, I44:Q44, I48:Q48, I52:Q52, I57:Q57, I62:Q62
- **Time Series Details**:
    - Annual: Start Year Unknown, End Year Unknown
    - **Frequency**: Annual
- **Key Components**: Total Marketing People Costs, Wages, Salaries Working Abroad, Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation.
- **Notes & Customizations**: Scaled by 1000. Includes percentage of wages calculations.

### Section Name: Marketing Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other employee related costs.
- **Cell Range**: A113:Q133
- **Layout Structure**:
    - **Row Headers Location**: B113:B133
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I113:Q113, I118:Q118, I123:Q123, I128:Q128, I133:Q133
- **Time Series Details**:
    - Annual: Start Year Unknown, End Year Unknown
    - **Frequency**: Annual
- **Key Components**: Total Marketing Other Employee Costs, Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office
- **Notes & Customizations**: Scaled by 1000.

### Section Name: Marketing Travel Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details travel related costs.
- **Cell Range**: A145:Q217
- **Layout Structure**:
    - **Row Headers Location**: B145:B217
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I145:Q145, I154:Q154, I163:Q163, I172:Q172, I181:Q181, I190:Q190, I199:Q199, I217:Q217
- **Time Series Details**:
    - Annual: Start Year Unknown, End Year Unknown
    - **Frequency**: Annual
- **Key Components**: Total Marketing Travel Costs, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Business Meals / Entertainment
- **Notes & Customizations**: Scaled by 1000.

### Section Name: Marketing Facility Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details facility related costs.
- **Cell Range**: A229:Q264
- **Layout Structure**:
    - **Row Headers Location**: B229:B264
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I229:Q229, I234:Q234, I239:Q239, I244:Q244, I249:Q249, I254:Q254, I259:Q259, I264:Q264
- **Time Series Details**:
    - Annual: Start Year Unknown, End Year Unknown
    - **Frequency**: Annual
- **Key Components**: Total Marketing Facility Costs, Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet.
- **Notes & Customizations**: Scaled by 1000.

### Section Name: Marketing Marketing
- **Section Type**: Standard P&L
- **Description & Purpose**: Details marketing specific costs.
- **Cell Range**: A266:Q299
- **Layout Structure**:
    - **Row Headers Location**: B266:B299
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I266:Q266, I271:Q271, I274:Q274, I277:Q277, I280:Q280, I283:Q283, I288:Q288, I291:Q291, I294:Q294, I299:Q299
- **Time Series Details**:
    - Annual: Start Year Unknown, End Year Unknown
    - **Frequency**: Annual
- **Key Components**: Total Marketing Marketing, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG.
- **Notes & Customizations**: Scaled by 1000.

### Section Name: Marketing General & Admin
- **Section Type**: Standard P&L
- **Description & Purpose**: Details general and administrative costs.
- **Cell Range**: A301:Q335
- **Layout Structure**:
    - **Row Headers Location**: B301:B335
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I301:Q301, I304:Q304, I309:Q309, I314:Q314, I317:Q317, I322:Q322, I327:Q327, I330:Q330, I335:Q335
- **Time Series Details**:
    - Annual: Start Year Unknown, End Year Unknown
    - **Frequency**: Annual
- **Key Components**: Total Marketing General & Admin, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies.
- **Notes & Customizations**: Scaled by 1000.

### Section Name: Marketing Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other costs.
- **Cell Range**: A360:Q385
- **Layout Structure**:
    - **Row Headers Location**: B360:B385
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I360:Q360, I365:Q365, I370:Q370, I375:Q375, I380:Q380, I385:Q385
- **Time Series Details**:
    - Annual: Start Year Unknown, End Year Unknown
    - **Frequency**: Annual
- **Key Components**: Total Marketing Other Costs, Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt.
- **Notes & Customizations**: Scaled by 1000.

### Section Name: Marketing Performance Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks key marketing performance indicators.
- **Cell Range**: B268:B270, B285:B287
- **Layout Structure**:
    - **Row Headers Location**: B268:B270, B285:B287
    - **Column Headers Location**: None
    - **Data Range**: None
- **Time Series Details**:
    - None
- **Key Components**: Advertising & Promotion, 2-Mo Lead Bookings, $ Spend to 2-Mo Lead Bookings, Paid Search, 2-Mo Lead Bookings, $ Spend to 2-Mo Lead Bookings
- **Notes & Customizations**: No time series data in this section.


====================================================================================================
# SHEET 32: Product
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Product
- **Key Sections Identified**:
    - Header
    - Product Operating Expenses Summary

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: Company Name, Report Title, Scenario Description
- **Notes & Customizations**: None

### Section Name: Product Operating Expenses Summary
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the product operating expenses, broken down by various cost categories. It includes both total expenses and specific "Product" related expenses for each category.
- **Cell Range**: A6:Q398
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I:Q
    - **Data Range**:
      - Annual data: I8:Q398 (numeric values for annual periods)
      - Monthly data: None
- **Time Series Details**:
    - **Date Range**: Not explicitly specified in the provided data, but based on the `format_ranges` and the `date_series_definitions`, the annual data spans an implied range based on the number of columns. The monthly data is not present in this section.
    - **Frequency**: Annual
- **Key Components**: Total Product Expense, Total Product People Costs, Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Commission Expense, Bonus, Benefits, Work Compensation, Payroll Taxes, Finnish Side Costs, Share Based Compensation, Recruiting Fees, Relocation, Contractors, Outsourced R&D, Capitalized Wages, Capitalized Outsourced R&D, Capitalized R&D, Total Product Other Employee Costs, Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions, Total Product Travel Costs, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment, Internal Events, Total Product Facility Costs, Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet, Total Product Marketing, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG, Total Product General & Admin, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising, Miscellaneous, Total Product Other Costs, Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt.
- **Notes & Customizations**: The report focuses specifically on "Product" related expenses, providing a detailed breakdown of operating costs for the product division. The values in columns I:Q are scaled by 1000.


====================================================================================================
# SHEET 33: Sales
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Sales
- **Key Sections Identified**:
    - Header
    - Sales Operating Expenses Summary
    - Sales People Costs
    - Sales Other Employee Costs
    - Sales Travel Costs
    - Sales Facility Costs
    - Sales Marketing
    - Sales General & Admin
    - Sales Other Costs

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and a brief description of the data.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: E3:FS3
    - **Data Range**: E3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: Start year is implied from the data in E3:Q3, End year is implied from the data in E3:Q3. Frequency is Annual.
    - Monthly: 2015-01-31 to 2027-12-31
    - Frequency: Monthly
- **Key Components**: Company Name, Report Title, Description
- **Notes & Customizations**: The header contains both annual and monthly time series data.

### Sales Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of total sales expenses.
- **Cell Range**: A6:Q8
- **Layout Structure**:
    - **Row Headers Location**: A6, B6, B8
    - **Column Headers Location**: E3:Q3
    - **Data Range**: I8:Q8
- **Time Series Details**:
    - Annual: Start year is implied from the data in E3:Q3, End year is implied from the data in E3:Q3. Frequency is Annual.
- **Frequency**: Annual
- **Key Components**: Total Sales Expense
- **Notes & Customizations**: Includes a scale factor of 1000 for the values.

### Sales People Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various costs associated with sales personnel, including wages, benefits, and other compensation.
- **Cell Range**: A10:Q62
- **Layout Structure**:
    - **Row Headers Location**: B10:B62
    - **Column Headers Location**: E3:Q3
    - **Data Range**: I10:Q62
- **Time Series Details**:
    - Annual: Start year is implied from the data in E3:Q3, End year is implied from the data in E3:Q3. Frequency is Annual.
- **Frequency**: Annual
- **Key Components**: Total Sales People Costs, Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Commission Expense, Bonus, Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation
- **Notes & Customizations**: Includes a scale factor of 1000 for the values.

### Sales Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other employee costs such as cellular phone service, home internet service, home office phone, home office, membership dues and subscriptions.
- **Cell Range**: A113:Q143
- **Layout Structure**:
    - **Row Headers Location**: B113:B143
    - **Column Headers Location**: E3:Q3
    - **Data Range**: I113:Q143
- **Time Series Details**:
    - Annual: Start year is implied from the data in E3:Q3, End year is implied from the data in E3:Q3. Frequency is Annual.
- **Frequency**: Annual
- **Key Components**: Total Sales Other Employee Costs, Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions
- **Notes & Customizations**: Includes a scale factor of 1000 for the values.

### Sales Travel Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various travel-related costs for the sales team.
- **Cell Range**: A145:Q217
- **Layout Structure**:
    - **Row Headers Location**: B145:B217
    - **Column Headers Location**: E3:Q3
    - **Data Range**: I145:Q217
- **Time Series Details**:
    - Annual: Start year is implied from the data in E3:Q3, End year is implied from the data in E3:Q3. Frequency is Annual.
- **Frequency**: Annual
- **Key Components**: Total Sales Travel Costs, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment
- **Notes & Customizations**: Includes a scale factor of 1000 for the values.

### Sales Facility Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the costs associated with sales facilities, such as rent, CAM, and utilities.
- **Cell Range**: A229:Q264
- **Layout Structure**:
    - **Row Headers Location**: B229:B264
    - **Column Headers Location**: E3:Q3
    - **Data Range**: I229:Q264
- **Time Series Details**:
    - Annual: Start year is implied from the data in E3:Q3, End year is implied from the data in E3:Q3. Frequency is Annual.
- **Frequency**: Annual
- **Key Components**: Total Sales Facility Costs, Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet
- **Notes & Customizations**: Includes a scale factor of 1000 for the values.

### Sales Marketing
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the marketing expenses for the sales team.
- **Cell Range**: A266:Q311
- **Layout Structure**:
    - **Row Headers Location**: B266:B311
    - **Column Headers Location**: E3:Q3
    - **Data Range**: I266:Q311
- **Time Series Details**:
    - Annual: Start year is implied from the data in E3:Q3, End year is implied from the data in E3:Q3. Frequency is Annual.
- **Frequency**: Annual
- **Key Components**: Total Sales Marketing, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Includes a scale factor of 1000 for the values.

### Sales General & Admin
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the general and administrative expenses for the sales team.
- **Cell Range**: A313:Q350
- **Layout Structure**:
    - **Row Headers Location**: B313:B350
    - **Column Headers Location**: E3:Q3
    - **Data Range**: I313:Q350
- **Time Series Details**:
    - Annual: Start year is implied from the data in E3:Q3, End year is implied from the data in E3:Q3. Frequency is Annual.
- **Frequency**: Annual
- **Key Components**: Total Sales General & Admin, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software
- **Notes & Customizations**: Includes a scale factor of 1000 for the values.

### Sales Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other costs for the sales team.
- **Cell Range**: A380:Q405
- **Layout Structure**:
    - **Row Headers Location**: B380:B405
    - **Column Headers Location**: E3:Q3
    - **Data Range**: I380:Q405
- **Time Series Details**:
    - Annual: Start year is implied from the data in E3:Q3, End year is implied from the data in E3:Q3. Frequency is Annual.
- **Frequency**: Annual
- **Key Components**: Total Sales Other Costs, Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt
- **Notes & Customizations**: Includes a scale factor of 1000 for the values.


====================================================================================================
# SHEET 34: Commission Waterfall
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Commission Waterfall
- **Key Sections Identified**:
    - Header
    - Commissions Expense Summary
    - Financial Commission Waterfall
    - Corporate Commission Waterfall
    - Other Commission Waterfall
    - AE Commission Waterfall
    - Total Commission Expense

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and report title.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: Company Name, Report Title, Scenario Description
- **Notes & Customizations**: None

### Commissions Expense Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of commissions expense.
- **Cell Range**: A6:FS24
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G6:Q6 (Annual), AR6:FS6 (Monthly)
    - **Data Range**:
      - Annual data: `G8:Q24`
      - Monthly data: `AR8:FS24`
- **Time Series Details**:
    - Annual: Unknown start year to Unknown end year (based on column headers G6:Q6, but headers are not provided)
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Commissions Expense, Bonus Expense, Financial Bookings, Corporate Bookings, Commission Percentages, Financial Commission, Corporate Commission.
- **Notes & Customizations**: Values are scaled by 1000.

### Financial Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the financial commission calculation over time.
- **Cell Range**: B26:FS162
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: C27 (Months), AR27:FS27 (Months)
    - **Data Range**:
      - Monthly data: `AR30:FS162`
- **Time Series Details**:
    - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Values are scaled by 1000.

### Corporate Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the corporate commission calculation over time.
- **Cell Range**: B165:FS301
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: C166 (Months), AR166:FS166 (Months)
    - **Data Range**:
      - Monthly data: `AR169:FS301`
- **Time Series Details**:
    - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Values are scaled by 1000.

### Other Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the other commission calculation over time.
- **Cell Range**: B304:FS440
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: C305 (Months), AR305:FS305 (Months)
    - **Data Range**:
      - Monthly data: `AR308:FS440`
- **Time Series Details**:
    - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Values are scaled by 1000.

### AE Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the AE commission calculation over time.
- **Cell Range**: B443:FS579
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: C444 (Months), AR444:FS444 (Months)
    - **Data Range**:
      - Monthly data: `AR447:FS579`
- **Time Series Details**:
    - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Values are scaled by 1000.

### Total Commission Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of total commissions expense.
- **Cell Range**: B581:FS583
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G580:Q580 (Annual), AR580:FS580 (Monthly)
    - **Data Range**:
      - Annual data: `G581:Q583`
      - Monthly data: `AR581:FS583`
- **Time Series Details**:
    - Annual: Unknown start year to Unknown end year (based on column headers G580:Q580, but headers are not provided)
    - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Commissions Expense, Bonus Expense, Total Commission Expense.
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 35: Bad Debt
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Bad Debt
- **Key Sections Identified**:
    - Reconciliation Header
    - AFDA Reconciliation Table

## 2. Detailed Section Analysis

### Section Name: Reconciliation Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the reconciliation.
- **Cell Range**: B2:B2
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: B2:B2
- **Time Series Details**: N/A
- **Key Components**: ADFDA Reconciliation 2020
- **Notes & Customizations**: Simple title for the sheet.

### Section Name: AFDA Reconciliation Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section reconciles the Allowance for Doubtful Accounts (AFDA) balance between a working paper (WP) and Intacct (accounting software), calculating the necessary adjustment to the AFDA.
- **Cell Range**: B5:CT21
- **Layout Structure**:
    - **Row Headers Location**: B6:B21
    - **Column Headers Location**: C5:CT5
    - **Data Range**: C6:CT21
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: ADFA beg balance per WP, ADFA beg balance per Intacct, Invoices written-off/collected, AFDA balance before adj, A/R ending balance per Intacct, AFDA as % of A/R to be maintained, 3.18% of current A/R, Less: AFDA balance before adj, Amount to be added to AFDA, AFDA end balance per WP, ADFA end balance per Intacct, Difference
- **Notes & Customizations**: The table calculates the difference between the required AFDA balance (based on a percentage of A/R) and the existing balance, determining the necessary adjustment. Values are scaled by 1000.



====================================================================================================
# SHEET 36: COGS CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: COGS CTRL
- **Key Sections Identified**:
    - User Metrics Table
    - Product Cost Assumptions
    - International Filings Expenses
    - Transcripts Expenses
    - Dow Jones Expenses
    - News & Journals Expenses
    - Web Service Expenses
    - Other Additional Data Sources
    - ASR Expenses
    - WSI FactSet Controls
    - WSI New User Additions
    - Revenue Share
    - Minimum Revenue
    - Usage Metrics

## 2. Detailed Section Analysis

### User Metrics Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the trend of net add users and the percentage of users in different categories (Financial, Corporate, Other) across various products (BRM, TR Transcripts, FactSet Transcripts, DJ). It aims to monitor user adoption and product penetration within different user segments.
- **Cell Range**: A12:CJ198
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I15:Q198` (numeric values for annual periods)
      - Monthly data: `CB15:CJ198` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Trend of Net Add Users, Financial BRM Users - % of Total Financial Users, Corporate BRM Users - % of Total Corporate Users, Other BRM Users - % of Total Other Users, Financial TR Transcripts Users - % of Total Financial Users, Corporate TR Transcripts Users - % of Total Corporate Users, Other TR Transcripts Users - % of Total Other Users, Financial FactSet Transcripts Users - % of Total Financial Users, Corporate FactSet Transcripts Users - % of Total Corporate Users, Other FactSet Transcripts Users - % of Total Other Users, Financial DJ Users - % of Total Financial, Corporate DJ Users - % of Total Corporate, Other DJ Users - % of Total Other, Financial AMR ($15k Users) - % of Total Financial, Corporate AMR ($15k Users) - % of Total Corporate, Other AMR ($15k Users) - % of Total Other, Financial AMR ($30k Users) - % of Total Financial, Corporate AMR ($30k Users) - % of Total Corporate, Other AMR ($30k Users) - % of Total Other, Financial Lexis Nexis Users - % of Total Financial, Corporate Lexis Nexis Users - % of Total Corporate, Other Lexis Nexis Users - % of Total Other, Financial International Filings Users - % of Total Financial, Corporate International Filings Users - % of Total Corporate, Other International Filings Users - % of Total Other, FactSet RT Users - % of Total Financial, FactSet RT Users - % of Total Corporate, FactSet RT Users - % of Total Other, FactSet AMR Users - % of Total Financial, FactSet AMR Users - % of Total Corporate, FactSet AMR Users - % of Total Other, Broker Partners - % Growth
- **Notes & Customizations**: The percentages are scaled by 1000. Some rows have "na" values in columns G and H.

### Product Cost Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the ramp assumptions and cost per user for various products and user tiers. It's used to project the cost of goods sold based on user growth and product usage.
- **Cell Range**: A212:CJ461
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I258:Q461` (numeric values for annual periods)
      - Monthly data: `BX217:CJ461` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Ramp Assumption - Global Users, Ramp Assumption - Global Users Base, Ramp Assumption - Global Users Upside, Ramp Assumption - Single Region Users, Ramp Assumption - Single Region Users Base, Ramp Assumption - Single Region Users Upside, Global Research (1-10) Cost Per User, Global Research (11-50) Cost Per User, Global Research (50+) Cost Per User, Global Research (1-10) % Cost Per User, Global Research (11-50) % Cost Per User, Global Research (50+) % Cost Per User, Single Research (1-10) Cost Per User, Single Research (11-25) Cost Per User, Single Research (26-50) Cost Per User, Single Research (51+) Cost Per User, Single Research (1-10) % Cost Per User, Single Research (11-25) % Cost Per User, Single Research (26-50) % Cost Per User, Single Research (51+) % Cost Per User, TR Minimum, TR New Contract - Minimum Payment, TR New Contract - Minimum Payment Base, TR New Contract - Minimum Payment Upside, TR New Contract - Minimum Users, TR New Contract - Price per Additional User, FactSet Minimum, AMR $15k Cost per User, AMR $30k Cost per User, AMR - % on TR, AMR - % on TR Base, AMR - % on TR Upside, TR AMR Minimum Fee, AMR TR Alternative Cost per User, AMR TR Alternative Cost - Minimum, TR to FactSet AMR Conversion
- **Notes & Customizations**: The percentages are scaled by 1000.

### International Filings Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the cost structure for International Filings, including user limits and prices for different tiers. It's used to calculate the cost of providing International Filings access to users.
- **Cell Range**: A467:CJ552
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I469:Q552` (numeric values for annual periods)
      - Monthly data: `BX469:CJ552` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: International Filing Expense - % of Non Paying Brokers, International Filing Expense - Tier 1 User Limit, International Filing Expense - Tier 1 Price, International Filing Expense - Tier 2 User Limit, International Filing Expense - Tier 2 Price, International Filing Expense - Tier 3 User Limit, International Filing Expense - Tier 3 Price, International Filing Expense - Tier 4 User Limit, International Filing Expense - Tier 4 Price, International Filing Expense - Tier 5 User Limit, International Filing Expense - Tier 5 Price, International Filing Expense - Price Per User in Excess
- **Notes & Customizations**: The percentages are scaled by 1000.

### Transcripts Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the cost structure for Transcripts, including user limits and prices for different tiers. It's used to calculate the cost of providing transcript access to users.
- **Cell Range**: A555:CJ730
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I557:Q730` (numeric values for annual periods)
      - Monthly data: `BX557:CJ730` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: TR Transcript Expense - % of Non Paying Brokers, TR Transcript Expense - Tier 1 User Limit, TR Transcript Expense - Tier 1 Price, TR Transcript Expense - Tier 2 User Limit, TR Transcript Expense - Tier 2 Price, TR Transcript Expense - Tier 3 User Limit, TR Transcript Expense - Tier 3 Price, TR Transcript Expense - Tier 4 User Limit, TR Transcript Expense - Tier 4 Price, TR Transcript Expense - Tier 5 User Limit, TR Transcript Expense - Tier 5 Price, TR Transcript Expense - Tier 6 User Limit, TR Transcript Expense - Tier 6 Price, TR Transcript Expense - Tier 7 User Limit, TR Transcript Expense - Tier 7 Price, TR Transcript Expense - Tier 8 User Limit, TR Transcript Expense - Tier 8 Price, TR Transcript Expense - Excess Price, FactSet Transcript Expense - % of Non Paying Brokers, FactSet Transcript Expense - User Limit, FactSet Transcript Expense - Fee Minimum, FactSet Transcript Expense - Global % of Excess Users, FactSet Transcript Expense - Fee per Excess Global User, FactSet Transcript Expense - Regional % of Excess Users, FactSet Transcript Expense - Fee per Excess Regional User
- **Notes & Customizations**: The percentages are scaled by 1000.

### Dow Jones Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the cost structure for Dow Jones data, including user limits, prices, and fees for different tiers. It's used to calculate the cost of providing Dow Jones access to users.
- **Cell Range**: A732:CJ984
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I734:Q984` (numeric values for annual periods)
      - Monthly data: `BP734:CJ984` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Dow Jones - Base, Dow Jones Expense - Fee Minimum, Dow Jones Expense - Tier 1 User Limit, Dow Jones Expense - Tier 1 Price, Dow Jones Expense - Tier 2 User Limit, Dow Jones Expense - Tier 2 Price, Dow Jones Expense - Tier 3 User Limit, Dow Jones Expense - Tier 3 Price, Dow Jones Expense - Admin Fee, Dow Jones Expense - Tier 1 Monthly Fee, Dow Jones Expense - Tier 2 Monthly Fee, Dow Jones Expense - Tier 3 Monthly Fee, Dow Jones Expense - Tier 4 User Limit, Dow Jones Expense - Tier 4 Monthly Fee, Dow Jones Expense - Tier 5 User Limit, Dow Jones Expense - Tier 5 Monthly Fee, Dow Jones Expense - Tier 6 User Limit, Dow Jones Expense - Tier 6 Monthly Fee, Dow Jones Expense - Tier 7 User Limit, Dow Jones Expense - Tier 7 Monthly Fee, Dow Jones Expense - Tier 8 User Limit, Dow Jones Expense - Tier 8 Monthly Fee, Dow Jones Expense - Tier 9 User Limit, Dow Jones Expense - Tier 9 Monthly Fee, Dow Jones Expense - Tier 10 User Limit, Dow Jones Expense - Tier 10 Monthly Fee, Dow Jones Expense - Tier 11 User Limit, Dow Jones Expense - Tier 11 Monthly Fee, Dow Jones Expense - Tier 12 User Limit, Dow Jones Expense - Tier 12 Monthly Fee, Dow Jones Expense - Tier 13 User Limit, Dow Jones Expense - Tier 13 Monthly Fee, Dow Jones Expense - Tier 14 User Limit, Dow Jones Expense - Tier 14 Monthly Fee
- **Notes & Customizations**: The percentages are scaled by 1000.

### News & Journals Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the cost structure for News & Journals data, including base fees, user tiers, and prices per user. It's used to calculate the cost of providing News & Journals access to users.
- **Cell Range**: A986:CJ1041
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I988:Q1041` (numeric values for annual periods)
      - Monthly data: `BP988:CJ1041` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Lexis Nexis - Base Fee, Lexis Nexis - Base Users, Lexis Nexis - Tier 1 Users, Lexis Nexis - Tier 1 Price per User, Lexis Nexis - Tier 2 Users, Lexis Nexis - Tier 2 Price per User, Lexis Nexis - Tier 3 Price per User, Acquire 2 News Expense
- **Notes & Customizations**: The percentages are scaled by 1000.

### Web Service Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the cost per user for Web Services.
- **Cell Range**: A1053:CJ1059
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I1055:Q1059` (numeric values for annual periods)
      - Monthly data: `BX1055:CJ1055` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Web Service per User
- **Notes & Customizations**: The percentages are scaled by 1000.

### Other Additional Data Sources
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the cost structure for other additional data sources.
- **Cell Range**: A1061:CJ1081
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I1063:Q1081` (numeric values for annual periods)
      - Monthly data: `BX1063:CJ1081` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Other Additional Data Sources - Cost per Year, Other Additional Data Sources - Cost per Year Base, Other Additional Data Sources - Cost per Year Upside
- **Notes & Customizations**: The percentages are scaled by 1000.

### ASR Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the cost structure for ASR.
- **Cell Range**: A1083:CJ1095
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I1085:Q1095` (numeric values for annual periods)
      - Monthly data: `BX1085:CJ1095` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Pool Contribution per User, Direct Consumption Cost
- **Notes & Customizations**: The percentages are scaled by 1000.

### Usage Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the usage metrics for various brokers.
- **Cell Range**: A1097:CJ1288
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I1097:Q1288` (numeric values for annual periods)
      - Monthly data: `BX1097:CJ1288` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Bernstein Usage, Deutsche Bank Usage, Barclays Usage, HSBC Usage, BOA Usage, UBS Usage, Morgan Stanley Usage, Cowen Usage, Autonomous Usage, Evercore Usage, Citi Usage, Credit Suisse Usage, JP Morgan Usage, Raymond James Usage, RBC Usage
- **Notes & Customizations**: The percentages are scaled by 1000.

### Revenue Share
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the revenue share for various brokers.
- **Cell Range**: A1198:CJ1288
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I1200:Q1288` (numeric values for annual periods)
      - Monthly data: `BX1200:CJ1288` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Bernstein Revenue Share, Deutsche Bank Revenue Share, Barclays Revenue Share, HSBC Revenue Share, BOA Revenue Share, UBS Revenue Share, Morgan Stanley Revenue Share, Cowen Revenue Share, Autonomous Revenue Share, Evercore Revenue Share, Citi Revenue Share, Credit Suisse Revenue Share, JP Morgan Revenue Share, Raymond James Revenue Share, RBC Revenue Share
- **Notes & Customizations**: The percentages are scaled by 1000.

### Minimum Revenue
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the minimum revenue for various brokers.
- **Cell Range**: A1290:CJ1378
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `I1290:Q1378` (numeric values for annual periods)
      - Monthly data: `BX1290:CJ1378` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Bernstein Minimum, Deutsche Bank Minimum, Barclays Minimum, HSBC Minimum, BOA Minimum, UBS Minimum, Morgan Stanley Minimum, Cowen Minimum, Autonomous Minimum, Evercore Minimum, Citi Minimum, Credit Suisse Minimum, JP Morgan Minimum, Raymond James Minimum, RBC Minimum
- **Notes & Customizations**: The percentages are scaled by 1000.

### WSI FactSet Controls
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the WSI FactSet Controls.
- **Cell Range**: A1380:CJ1590
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `J1380:Q1590` (numeric values for annual periods)
      - Monthly data: `BX1380:CJ1590` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: WSI New User Additions - Corporate, WSI New User Additions - Financial, % of WSI New User Additions - Corporate (Professional Services), % of WSI New User Additions - Corporate (Pharma & Life Sciences), % of WSI New User Additions - Corporate (Tech, Media & Telecom), % of WSI New User Additions - Corporate (Energy & Utilities), % of WSI New User Additions - Corporate (Retail & Consumer Products), % of WSI New User Additions - Financial (Financial), % of Non-WSI Corporate Users Converted, % of WSI Users Active - Corporate (Professional Services), % of WSI Users Active - Corporate (Pharma & Life Sciences), % of WSI Users Active - Corporate (Tech, Media & Telecom), % of WSI Users Active - Corporate (Energy & Utilities), % of WSI Users Active - Corporate (Retail & Consumer Products), % of WSI Users Active - Financial (Financial), Docs per Active User per Month - (Professional Services), Docs per Active User per Month - (Pharma & Life Sciences), Docs per Active User per Month - (Tech, Media & Telecom), Docs per Active User per Month - (Energy & Utilities), Docs per Active User per Month - (Retail & Consumer Products), Docs per Active User per Month - (Financial), Consumption Reduction, Users Active, Bookings per Active Trialer, Bookings per Internal User, Docs per Active User, Docs per Trail User, Docs per Internal User, Internal Docs Minimum, Reduction, Total Document Minimum, Document Cost - Minimum, Document Cost - Excess, FactSet AMR Minimum, Total FactSet Minimum
- **Notes & Customizations**: The percentages are scaled by 1000.

### WSI New User Additions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the WSI New User Additions.
- **Cell Range**: A1380:CJ1426
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: `J1380:Q1426` (numeric values for annual periods)
      - Monthly data: `BX1380:CJ1426` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: WSI New User Additions - Corporate, WSI New User Additions - Financial, % of WSI New User Additions - Corporate (Professional Services), % of WSI New User Additions - Corporate (Pharma & Life Sciences), % of WSI New User Additions - Corporate (Tech, Media & Telecom), % of WSI New User Additions - Corporate (Energy & Utilities), % of WSI New User Additions - Corporate (Retail & Consumer Products), % of WSI New User Additions - Financial (Financial)
- **Notes & Customizations**: The percentages are scaled by 1000.


====================================================================================================
# SHEET 37: Cost of Goods Sold
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Cost of Goods Sold
- **Key Sections Identified**:
    - Cost of Goods Sold Summary
    - Product Summary
    - Product Summary - % of Revenue
    - Total User Count
    - Total User Net Adds
    - Product Detail Net Adds - Live Users
    - Product Detail - Live Users
    - Factset Research
    - TR Research - New Contract
    - After Market Research Expense
    - International Filings Expense
    - Transcripts Expense
    - Dow Jones News Expense
    - News & Journals Expense
    - IDC Expense
    - Web Service COGS Allocation
    - COGS by Segment
    - P&L
    - COGS Allocation

## 2. Detailed Section Analysis

### Cost of Goods Sold Summary
- **Section Type**: Standard P&L
- **Description & Purpose**: Summarizes the various components of the Cost of Goods Sold. Provides a high-level overview of expenses related to delivering products and services.
- **Cell Range**: A6:FS18
- **Layout Structure**:
    - **Row Headers Location**: B8:B17
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E9:Q17
      - Monthly data: T9:FS17
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Cost of Goods Sold, Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, IDC, Web Service - Production, Other Data, Total Cost of Goods Sold
- **Notes & Customizations**: Data is scaled by 1000.

### Product Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the costs associated with different products.
- **Cell Range**: A26:FS70
- **Layout Structure**:
    - **Row Headers Location**: B29:B68
    - **Column Headers Location**: G3:Q3, AR3:FS3
    - **Data Range**:
      - Annual data: G29:Q70
      - Monthly data: AR29:FS70
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total News, News and Journals, Total Other Data, Total
- **Notes & Customizations**: Data is scaled by 1000.

### Product Summary - % of Revenue
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows product costs as a percentage of revenue.
- **Cell Range**: A72:FS81
- **Layout Structure**:
    - **Row Headers Location**: B74:B80
    - **Column Headers Location**: G3:Q3, AR3:FS3
    - **Data Range**:
      - Annual data: G74:Q80
      - Monthly data: AR74:FS80
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, Other Data, Total COGS
- **Notes & Customizations**: Data is scaled by 1000.

### Total User Count
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the total number of users.
- **Cell Range**: A85:FS91
- **Layout Structure**:
    - **Row Headers Location**: B87:B91
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E88:Q91
      - Monthly data: T88:FS91
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Users, Corporate , Other, Total Users
- **Notes & Customizations**: Data is scaled by 1000.

### Total User Net Adds
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the total number of user net adds.
- **Cell Range**: A93:FS99
- **Layout Structure**:
    - **Row Headers Location**: B95:B99
    - **Column Headers Location**: G3:Q3, U3:FS3
    - **Data Range**:
      - Annual data: G96:Q99
      - Monthly data: U96:FS99
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2016-07-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate , Other, Total Users
- **Notes & Customizations**: Data is scaled by 1000.

### Product Detail Net Adds - Live Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the product detail net adds for live users.
- **Cell Range**: A101:FS191
- **Layout Structure**:
    - **Row Headers Location**: B103:B191
    - **Column Headers Location**: G3:Q3, AS3:FS3
    - **Data Range**:
      - Annual data: G103:Q191
      - Monthly data: AS103:FS191
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: TR Broker Research, Financial , % of  Financial Net Adds, % of  Corporate Net Adds, % of  Other Net Adds, TR Transcripts, Factset Transcripts, Dow Jones, AMR ($15k), AMR ($30k), Lexis Nexis, FactSet RT, FactSet AMR
- **Notes & Customizations**: Data is scaled by 1000.

### Product Detail - Live Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the product detail for live users.
- **Cell Range**: A193:FS283
- **Layout Structure**:
    - **Row Headers Location**: B195:B283
    - **Column Headers Location**: G3:Q3, AR3:FS3
    - **Data Range**:
      - Annual data: G195:Q283
      - Monthly data: AR195:FS283
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: TR Broker Research, Financial , % of Total Financial , % of Total Corporate, % of Total Other, TR Transcripts, Factset Transcripts, Dow Jones, AMR ($15k), AMR ($30k), Lexis Nexis, FactSet RT, FactSet AMR
- **Notes & Customizations**: Data is scaled by 1000.

### Factset Research
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the Factset Research data.
- **Cell Range**: B315:CH376
- **Layout Structure**:
    - **Row Headers Location**: B317:B376
    - **Column Headers Location**: I3:Q3, BP3:CH3
    - **Data Range**:
      - Annual data: I317:Q376
      - Monthly data: BP317:CH376
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: <500 Users, 500-750 Users, 750-1,000 Users, 1,000-1,500 Users, 1,500-2,500 Users, 2,500-3,500 Users, 3500-4500, 4500-7500, 7500-10000, 10000-12500, 12500-15000, 15000-20000, 20000-25000, 25000-35000, 35000-50000, 50000-75000, >75,000 Users, Converted from TR, FS RT users, FactSet Users (Average), FS BRM Expense, FactSet Minimum, Total FactSet Expense, Total Broker Research Expense, After Market Research Expense, TR Alt - Expense
- **Notes & Customizations**: Data is scaled by 1000.

### TR Research - New Contract
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the TR Research - New Contract data.
- **Cell Range**: B297:FS313
- **Layout Structure**:
    - **Row Headers Location**: B299:B312
    - **Column Headers Location**: I3:Q3, BP3:FS3
    - **Data Range**:
      - Annual data: I299:Q312
      - Monthly data: BP299:FS312
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Minimum Payment, Minimum Users, Minimum Price per User, Excess Over Minimum, Converted to FactSet, Additional TR Users, Price per Additional User, Additional TR Cost, Total TR Research, Total FS RT Users, % of Total Users
- **Notes & Customizations**: Data is scaled by 1000.

### After Market Research Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the After Market Research Expense data.
- **Cell Range**: B347:CH367
- **Layout Structure**:
    - **Row Headers Location**: B349:B367
    - **Column Headers Location**: I3:Q3, BD3:CH3
    - **Data Range**:
      - Annual data: I349:Q367
      - Monthly data: BD349:CH367
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: User count - $15k package, User count - $30k package, TR AMR, TR - User count - $15k package, $15k - % TR, TR - User count - $30k package, $30k - % TR, TR - Co-Sell, AMR - $15k, Cost per User, AMR - $30k, Total TR Expense
- **Notes & Customizations**: Data is scaled by 1000.

### International Filings Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the International Filings Expense data.
- **Cell Range**: B389:FS420
- **Layout Structure**:
    - **Row Headers Location**: B391:B420
    - **Column Headers Location**: I3:Q3, BP3:FS3
    - **Data Range**:
      - Annual data: I392:Q420
      - Monthly data: BP392:FS420
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: TR International Filings, Tier 1 - Post 6/1/19, User Limit, Price, Tier 2, Tier 3, Tier 4, Tier 5, Excess User Fee, Excess Fees, Total International Filings Expense
- **Notes & Customizations**: Data is scaled by 1000.

### Transcripts Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the Transcripts Expense data.
- **Cell Range**: B423:FS466
- **Layout Structure**:
    - **Row Headers Location**: B425:B466
    - **Column Headers Location**: I3:Q3, BP3:FS3
    - **Data Range**:
      - Annual data: I428:Q466
      - Monthly data: BP428:FS466
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Corporate, Tier 1, User Limit, Price, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6, Tier 7, Tier 8, Excess Over Tier 5 User Limit, Excess User Fee, Excess Fees, Total TR Expense
- **Notes & Customizations**: Data is scaled by 1000.

### Dow Jones News Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the Dow Jones News Expense data.
- **Cell Range**: B531:FS555
- **Layout Structure**:
    - **Row Headers Location**: B535:B555
    - **Column Headers Location**: I3:Q3, BP3:FS3
    - **Data Range**:
      - Annual data: I537:Q555
      - Monthly data: BP537:FS555
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Base Case, Minimum Fee, User count, Tier 1, Tier 2, Tier 3, Admin Fee, Base Case Total
- **Notes & Customizations**: Data is scaled by 1000.

### News & Journals Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the News & Journals Expense data.
- **Cell Range**: B609:FS633
- **Layout Structure**:
    - **Row Headers Location**: B612:B633
    - **Column Headers Location**: I3:Q3, BP3:FS3
    - **Data Range**:
      - Annual data: I612:Q633
      - Monthly data: BP612:FS633
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: User count, Base Fees, Base Users, Tier 1, Price per User, Tier 2, Tier 3, Total Lexis Nexis, Acquire 2 News, Total News & Journal
- **Notes & Customizations**: Data is scaled by 1000.

### IDC Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the IDC Expense data.
- **Cell Range**: B636:FS640
- **Layout Structure**:
    - **Row Headers Location**: B640
    - **Column Headers Location**: I3:Q3, BP3:FS3
    - **Data Range**:
      - Annual data: I640:Q640
      - Monthly data: BP640:FS640
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total IDC
- **Notes & Customizations**: Data is scaled by 1000.

### Web Service COGS Allocation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the Web Service COGS Allocation data.
- **Cell Range**: B643:FS648
- **Layout Structure**:
    - **Row Headers Location**: B646:B648
    - **Column Headers Location**: I3:Q3, BP3:FS3
    - **Data Range**:
      - Annual data: I646:Q648
      - Monthly data: BP646:FS648
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total Users, Web Service
- **Notes & Customizations**: Data is scaled by 1000.

### COGS by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the COGS by Segment data.
- **Cell Range**: B655:FS667
- **Layout Structure**:
    - **Row Headers Location**: B657:B666
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E658:Q666
      - Monthly data: T658:FS666
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Cost of Goods Sold, Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, IDC, Web Service - Production, Other Data
- **Notes & Customizations**: Data is scaled by 1000.

### P&L
- **Section Type**: Standard P&L
- **Description & Purpose**: Displays the P&L data.
- **Cell Range**: B675:FS676
- **Layout Structure**:
    - **Row Headers Location**: B675:B676
    - **Column Headers Location**: G3:Q3, AR3:FS3
    - **Data Range**:
      - Annual data: G675:Q676
      - Monthly data: AR675:FS676
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: P&L, Check
- **Notes & Customizations**: Data is scaled by 1000.

### COGS Allocation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the COGS Allocation data.
- **Cell Range**: B679:FS817
- **Layout Structure**:
    - **Row Headers Location**: B681:B816
    - **Column Headers Location**: G3:Q3, AR3:FS3
    - **Data Range**:
      - Annual data: G682:Q816
      - Monthly data: AR682:FS816
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: BRM Users, % of BRM Users, AMR Users, % of AMR Users, International Filings Users, % of Filings Users, Transcripts Users, % of Transcripts Users, DJ Users, % of Dow Jones Users, News and Journals Users, % of News and Journals Users, Other COGS, User Allocation, COGS Allocation
- **Notes & Customizations**: Data is scaled by 1000.

### Upside Case
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the Upside Case data.
- **Cell Range**: B558:FS603
- **Layout Structure**:
    - **Row Headers Location**: B560:B603
    - **Column Headers Location**: I3:Q3, BP3:FS3
    - **Data Range**:
      - Annual data: I560:Q603
      - Monthly data: BP560:FS603
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2000-01-01 to 2000-01-01
    - **Frequency**:
      - Annual
      - Annual
- **Key Components**: Tier 1, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6, Tier 7, Tier 8, Tier 9, Tier 10, Tier 11, Tier 12, Tier 13, Tier 14, Total Upside Case
- **Notes & Customizations**: Data is scaled by 1000.

### S&P Transcripts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the S&P Transcripts data.
- **Cell Range**: B510:FS528
- **Layout Structure**:
    - **Row Headers Location**: B512:B528
    - **Column Headers Location**: I3:Q3, CK3:FS3
    - **Data Range**:
      - Annual data: I526:Q528
      - Monthly data: CK512:FS528
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Up to 4999, 5000 to 5999, 6000 to 6999, 7000 to 7999, 8000 to 8999, 9000 to 9999, Total Users, User Limit, Minimum, Total S&P Expense, Total Transcript Expense
- **Notes & Customizations**: Data is scaled by 1000.


====================================================================================================
# SHEET 38: Total FDS Cost
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Total FDS Cost
- **Key Sections Identified**:
    - Summary FDS COGS Expense
    - FDS Excess Expense
    - Total FDS Spend & Minimum
    - Pool Contribution & Carryover
    - Adjusted FDS COGS Expense

## 2. Detailed Section Analysis

### Section Name: Summary FDS COGS Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the FDS Content COGS expense across different categories. It provides a breakdown of the costs associated with different content types.
- **Cell Range**: B6:DD13
- **Layout Structure**:
    - **Row Headers Location**: B8:B13
    - **Column Headers Location**: D2:K2 (Annual), M2:DD2 (Monthly)
    - **Data Range**:
      - Annual data: D8:K13
      - Monthly data: M8:DD13
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Pool Floor, BRM, AMR, Transcripts, M&A, Total
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: FDS Excess Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the FDS Excess expense, breaking it down by different categories. It helps in understanding the excess spending beyond the pool floor.
- **Cell Range**: B17:DD23
- **Layout Structure**:
    - **Row Headers Location**: B19:B23
    - **Column Headers Location**: D2:K2 (Annual), M2:DD2 (Monthly)
    - **Data Range**:
      - Annual data: D19:K23
      - Monthly data: M19:DD23
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: BRM, AMR, Transcripts, M&A, Total Excess
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Total FDS Spend & Minimum
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the total FDS spend and the minimum FDS spend. It provides a comparison between the actual spend and the required minimum.
- **Cell Range**: B25:DD26
- **Layout Structure**:
    - **Row Headers Location**: B25:B26
    - **Column Headers Location**: D2:K2 (Annual), M2:DD2 (Monthly)
    - **Data Range**:
      - Annual data: D25:K26
      - Monthly data: M25:DD26
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS Spend, Total FDS Minimum
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Pool Contribution & Carryover
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the pool contribution, paid amount, carryover, excess, and carryover balance. It tracks the movement of funds related to the pool.
- **Cell Range**: B28:DD35
- **Layout Structure**:
    - **Row Headers Location**: B30:B35
    - **Column Headers Location**: D2:K2 (Annual), M2:DD2 (Monthly)
    - **Data Range**:
      - Annual data: D30:K35
      - Monthly data: M30:DD35
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Paid, Carryover, Excess, Carryover Balance, Change in Carryover
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Adjusted FDS COGS Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the adjusted FDS COGS expense, taking into account AMR expense and changes in carryover.
- **Cell Range**: B37:DD47
- **Layout Structure**:
    - **Row Headers Location**: B37:B47
    - **Column Headers Location**: D2:K2 (Annual), M2:DD2 (Monthly)
    - **Data Range**:
      - Annual data: D43:K47
      - Monthly data: M43:DD47
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: AMR Expense, Change in Carryover, Adjusted AMR Expense, BRM, AMR, Transcripts, M&A, Total
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 39: FDS AMR
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: FDS AMR
- **Key Sections Identified**:
    - Header
    - Key Metrics & Bookings
    - Documents Purchased Analysis
    - Cost Analysis

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time periods covered.
- **Cell Range**: A2:DD3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: D2:K2, M2:DD2, D3:K3, M3:DD3
    - **Data Range**: None
- **Time Series Details**:
    - Annual: 2020 to 2027
        - **Date Range**: 2020 to 2027
        - **Frequency**: Annual
    - Repeating Annual: 2020 to 2027 (repeating 12 times)
        - **Date Range**: 2020 to 2027
        - **Frequency**: Annual
    - Monthly: 2020-01 to 2027-12
        - **Date Range**: 2020-01-31 to 2027-12-31
        - **Frequency**: Monthly
- **Key Components**: Years, Months
- **Notes & Customizations**: Contains multiple time series: annual and monthly.

### Key Metrics & Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents key metrics related to users and bookings.
- **Cell Range**: B5:DD24
- **Layout Structure**:
    - **Row Headers Location**: B5:B24
    - **Column Headers Location**: D2:K2, M2:DD2, D3:K3, M3:DD3
    - **Data Range**:
      - Annual data: D6:K24
      - Monthly data: M6:DD24
- **Time Series Details**:
    - Annual: 2020 to 2027
        - **Date Range**: 2020 to 2027
        - **Frequency**: Annual
    - Repeating Annual: 2020 to 2027 (repeating 12 times)
        - **Date Range**: 2020 to 2027
        - **Frequency**: Annual
    - Monthly: 2020-01 to 2027-12
        - **Date Range**: 2020-01-31 to 2027-12-31
        - **Frequency**: Monthly
- **Key Components**: FDS AMR, % Active, Total Bookings, Active Users, Active Trialer Users, Bookings per Active Trialer, Bookings per Internal User, Active Internal Users.
- **Notes & Customizations**: Includes metrics on different user types and bookings per user.

### Documents Purchased Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes documents purchased by different user types.
- **Cell Range**: B26:DD59
- **Layout Structure**:
    - **Row Headers Location**: B26:B59
    - **Column Headers Location**: D2:K2, M2:DD2, D3:K3, M3:DD3
    - **Data Range**:
      - Annual data: D28:K59
      - Monthly data: M28:DD59
- **Time Series Details**:
    - Annual: 2020 to 2027
        - **Date Range**: 2020 to 2027
        - **Frequency**: Annual
    - Repeating Annual: 2020 to 2027 (repeating 12 times)
        - **Date Range**: 2020 to 2027
        - **Frequency**: Annual
    - Monthly: 2020-01 to 2027-12
        - **Date Range**: 2020-01-31 to 2027-12-31
        - **Frequency**: Monthly
- **Key Components**: Docs Purchased per User Type, Active Users, Active - Documents Purchased, Trialers - Documents Purchased, Internal - Documents Purchased, Total Docs Purchased, Adjusted Documents Purchased.
- **Notes & Customizations**: Includes analysis of unadjusted pages purchased and pages per document.

### Cost Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes document costs and total FactSet AMR costs.
- **Cell Range**: B61:DD89
- **Layout Structure**:
    - **Row Headers Location**: B61:B89
    - **Column Headers Location**: D2:K2, M2:DD2, D3:K3, M3:DD3
    - **Data Range**:
      - Annual data: D61:K89
      - Monthly data: M61:DD89
- **Time Series Details**:
    - Annual: 2020 to 2027
        - **Date Range**: 2020 to 2027
        - **Frequency**: Annual
    - Repeating Annual: 2020 to 2027 (repeating 12 times)
        - **Date Range**: 2020 to 2027
        - **Frequency**: Annual
    - Monthly: 2020-01 to 2027-12
        - **Date Range**: 2020-01-31 to 2027-12-31
        - **Frequency**: Monthly
- **Key Components**: Annual Documents Read, Total Document Minimum, Total Document Read, Document Cost, Total Document Cost, FactSet AMR Minimum, Total FactSet AMR Cost, Rollover Balance, Excess Over Minimum, Adjusted Excess, Total Adjusted FactSet AMR Cost.
- **Notes & Customizations**: Includes analysis of costs by tier and excess costs.


====================================================================================================
# SHEET 40: Direct Broker
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Direct Broker
- **Key Sections Identified**:
    - Overview Section
    - Reads Consumption Section
    - WSI Broker Expense Section
    - Direct Broker Expense Section

## 2. Detailed Section Analysis

### Overview Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides an overview of key metrics related to AlphaSense's cost of goods sold, including expenses, user activity, and page consumption. It allows for tracking performance and identifying trends over time.
- **Cell Range**: B6:Q47
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**:
      - Annual data: `E8:Q23`, `E25:Q27`, `E29:Q29`, `J31:Q31`, `E33:Q33`, `J34:Q34`, `E38:Q40`, `E42:Q43`, `E45:Q47`
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Bernstein Expense, Deutsche Bank Expense, Barclays Expense, HSBC Expense, BOA Expense, UBS Expense, Morgan Stanley Expense, Cowen Expense, Autonomous Expense, Evercore Expense, Citi Expense, Credit Suisse Expense, JP Morgan Expense, Raymond James Expense, RBC Expense, Direct Consumption Expense, FS AMR Expense, Total WSI, Total Active Users, Cost per User, FS BRM Expense, Total Users, Active Users, Active (%), Total Page Reads, Page Reads per Active User, Contribution per User, Total Pool Contribution ($)
- **Notes & Customizations**: The data is scaled by 1000.

### Reads Consumption Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down the reads consumption by different brokers and direct sources, showing both the absolute consumption and the percentage contribution.
- **Cell Range**: B49:Q95
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**:
      - Annual data: `E51:Q71`, `E75:Q95`
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Bernstein, Deutsche Bank, Barclays, HSBC, BOA, UBS, Morgan Stanley, Cowen, Autonomous, Evercore, Citi , Credit Suisse , JP Morgan , Raymond James, RBC, Direct Broker, FactSet AMR, FactSet RT, Total, Reads Consumption (%), FactSet AMR, FactSet RT, Total
- **Notes & Customizations**: The data is scaled by 1000 for reads consumption and is a percentage for reads consumption (%).

### WSI Broker Expense Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the total pool contribution and the direct broker expense.
- **Cell Range**: B97:Q105
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**:
      - Annual data: `E101:Q105`
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Total Pool Contribution, Direct Broker Expense, Adjusted Direct Broker Expense
- **Notes & Customizations**: The data is scaled by 1000.

### Direct Broker Expense Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of the direct broker expense, including strategic investment, usage, consumption, revenue share, expense, minimum, and adjusted expense for each broker.
- **Cell Range**: B103:Q255
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**:
      - Annual data: `E104:Q104`, `E105:Q105`, `E110:Q115`, `E120:Q125`, `E130:Q135`, `E140:Q145`, `E150:Q155`, `E160:Q165`, `E170:Q175`, `E180:Q185`, `E190:Q195`, `E200:Q205`, `E210:Q215`, `E220:Q225`, `E230:Q235`, `E240:Q245`, `E250:Q255`
    - **Data Range**:
      - Monthly data: `J109:Q109`, `J119:Q119`, `J129:Q129`, `J139:Q139`, `J149:Q149`, `J159:Q159`, `J169:Q169`, `J179:Q179`, `J189:Q189`, `J199:Q199`, `J209:Q209`, `J219:Q219`, `J229:Q229`, `J239:Q239`, `J249:Q249`
- **Time Series Details**:
    - **Date Range**: 2015 to 2027 (Annual)
    - **Frequency**: Annual
    - **Date Range**: 2015-01-31 to 2027-12-31 (Monthly)
    - **Frequency**: Monthly
- **Key Components**: Strategic Investment, Usage, Consumption, Revenue Share, Expense, Minimum, Adjusted Expense (repeated for each broker: Bernstein, Deutsche Bank, Barclays, HSBC, BOA, UBS, Morgan Stanley, Cowen, Autonomous, Evercore, Citi, Credit Suisse, JP Morgan, Raymond James, RBC)
- **Notes & Customizations**: The data is scaled by 1000. Some rows have monthly data from column J onwards.


====================================================================================================
# SHEET 41: Additional FDS Content
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Additional FDS Content
- **Key Sections Identified**:
    - FDS RT Expense by User Tier
    - FDS RT Excess Expense Calculation
    - Factset Transcripts Expense by User Tier
    - Factset M&A Expense by User Tier

## 2. Detailed Section Analysis

### Section Name: FDS RT Expense by User Tier
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the number of users and associated costs for FactSet Real-Time (RT) data, broken down by user tiers. It helps analyze the distribution of users across different tiers and the corresponding cost implications.
- **Cell Range**: B7:DF34
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Up to 1500", "2000 - 425000", etc.)
    - **Column Headers Location**: Row 7 (e.g., "Total FDS RT Users" in B7, and dates in F3:M3 and O3:DF3)
    - **Data Range**:
      - Annual data: C11:D34 (numeric values for annual periods)
      - Monthly data: V11:DF34 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS RT Users, User Tiers, Users, Cost
- **Notes & Customizations**: The number values are scaled by 1000.

### Section Name: FDS RT Excess Expense Calculation
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section calculates the excess expense related to FactSet Real-Time (RT) data, applying discounts and considering a pool floor. It aims to determine the adjusted expense after accounting for these factors.
- **Cell Range**: B36:DF49
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Total FDS RT Excess Expense", "Pool Floor", "Discount (%)", etc.)
    - **Column Headers Location**: Row 36 and O3:DF3
    - **Data Range**:
      - Annual data: F36:M49 (numeric values for annual periods)
      - Monthly data: O36:DF49 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS RT Excess Expense, Pool Floor, Discount (%), Discount Adjusted FDS RT Excess Expense, Minimum Excess Spend (Bucket), Minimum Excess Spend
- **Notes & Customizations**: The number values are scaled by 1000, except for Discount (%) in O40:DF40 and Pool Floor in O37:U37.

### Section Name: Factset Transcripts Expense by User Tier
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the number of users and associated costs for FactSet Transcripts data, broken down by user tiers. It helps analyze the distribution of users across different tiers and the corresponding cost implications.
- **Cell Range**: B51:DF80
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Up to 6000", "7001 - 65000", etc.)
    - **Column Headers Location**: Row 53 and O3:DF3
    - **Data Range**:
      - Annual data: C57:D78 (numeric values for annual periods)
      - Monthly data: V57:DF78 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS Transcript Users, User Tiers, Users, Cost, % of Total Users, Total FDS Transcripts Excess Expense
- **Notes & Customizations**: The number values are scaled by 1000, except for Cost in D57:D78.

### Section Name: Factset M&A Expense by User Tier
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the number of users and associated costs for FactSet M&A data, broken down by user tiers. It helps analyze the distribution of users across different tiers and the corresponding cost implications.
- **Cell Range**: B83:DF112
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "TBD")
    - **Column Headers Location**: Row 85 and O3:DF3
    - **Data Range**:
      - Annual data: C89:D89 (numeric values for annual periods)
      - Monthly data: V89:DF110 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS M&A Users, User Tiers, Users, Cost, % of Total Users, Total FDS M&A Excess Expense
- **Notes & Customizations**: The number values are scaled by 1000, except for Total FDS M&A Users in O85:U85.


====================================================================================================
# SHEET 42: FDS User Growth
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: FDS User Growth
- **Key Sections Identified**:
    - User Summary
    - New WSI Users Additions
    - Non-WSI Users Converted
    - Non-WSI Users Added
    - Non-WSI Net User Change
    - Non-WSI Users by Sector
    - WSI User Additions
    - Total Users
    - FDS RT Users Detail

## 2. Detailed Section Analysis

### User Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a high-level overview of user growth metrics, including ARR, average users, and year-end users, broken down by corporate and financial segments. It serves as a summary dashboard for key performance indicators.
- **Cell Range**: B6:DD30
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D8:K30`
      - Monthly data: `M8:DD30`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Corporate ARR, Financial ARR, Total ARR, Average Corporate Users, Average Financial Users, Total Average Users, Corporate Users at Year End, Financial Users at Year End, Total Users at Year End, Corporate Users (Added), Financial Users (Added), Total Users (Added), Corporate Enabled WSI Users, Financial Enabled WSI Users, Total Enabled WSI Users, % of Corporate Users, % of Financial Users, % of Total Users.
- **Notes & Customizations**: ARR values are scaled by 1000.

### New WSI Users Additions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes new WSI user additions, breaking them down by product and calculating the percentage of new users added by each product.
- **Cell Range**: B33:DD57
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D38:K57`
      - Monthly data: `S38:DD57`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Corporate, WSI, Non-WSI, Total Corporate, Financial, Total Financial.
- **Notes & Customizations**: Values are scaled by 1000.

### Percent of New Users Added
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the percentage of new users added by sector.
- **Cell Range**: B59:DD71
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D62:K71`
      - Monthly data: `M62:DD71`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total, Financial - Other.
- **Notes & Customizations**: This section calculates percentages.

### New WSI Users Added by Sector
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the number of new WSI users added, broken down by sector.
- **Cell Range**: B73:DD85
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D76:K85`
      - Monthly data: `N76:DD85`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total, Financial - Other.
- **Notes & Customizations**: Values are scaled by 1000.

### Non-WSI Users Converted
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the conversion of Non-WSI users to WSI, showing the percentage converted by sector.
- **Cell Range**: B88:DD106
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D92:K106`
      - Monthly data: `S92:DD106`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total.
- **Notes & Customizations**: Values are scaled by 1000.

### Percent of New Non-WSI Users Added by Sector
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the percentage of new Non-WSI users added by sector.
- **Cell Range**: B108:DD115
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D110:K115`
      - Monthly data: `S110:DD115`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total.
- **Notes & Customizations**: This section calculates percentages.

### Non-WSI Users Added
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the number of Non-WSI users added, broken down by sector.
- **Cell Range**: B117:DD124
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D119:K124`
      - Monthly data: `S119:DD124`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total.
- **Notes & Customizations**: Values are scaled by 1000.

### Non-WSI Net User Change
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the net change in Non-WSI users, broken down by sector.
- **Cell Range**: B126:DD133
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D128:K133`
      - Monthly data: `S128:DD133`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total.
- **Notes & Customizations**: Values are scaled by 1000.

### Non-WSI Users by Sector
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the total number of Non-WSI users by sector.
- **Cell Range**: B135:DD142
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D137:K142`
      - Monthly data: `R137:DD142`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total.
- **Notes & Customizations**: Values are scaled by 1000.

### WSI User Additions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes WSI user additions, breaking them down by sector.
- **Cell Range**: B145:DD159
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D150:K159`
      - Monthly data: `M150:DD159`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total, Financial.
- **Notes & Customizations**: Values are scaled by 1000.

### Total Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of total users, including average users and year-end users, by product type (WSI and Non-WSI) and segment (Corporate and Financial).
- **Cell Range**: B162:DD184
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D167:K184`
      - Monthly data: `M167:DD184`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Average Corporate Users, Average Financial Users, Total Average Corporate Users, Total Average Financial Users, WSI Enabled Users at Year End, Non-WSI Users at Year End, Total Corporate Users at Year End, Total Financial Users at Year End.
- **Notes & Customizations**: Values are scaled by 1000.

### Percent of Active Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the percentage of active users by sector.
- **Cell Range**: B196:DD204
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D198:K204`
      - Monthly data: `M198:DD204`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial, Total.
- **Notes & Customizations**: This section calculates percentages.

### Total Active Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the total number of active users by sector.
- **Cell Range**: B206:DD214
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D208:K214`
      - Monthly data: `M208:DD214`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial, Total.
- **Notes & Customizations**: Values are scaled by 1000.

### Document Consumption
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes document consumption metrics, including documents per active user per month.
- **Cell Range**: B217:DD226
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D221:K226`
      - Monthly data: `M221:DD226`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Financial.
- **Notes & Customizations**: Values are scaled by 1000.

### Consumpstion Reduction
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes document consumption reduction metrics, including documents per active user per month reduction.
- **Cell Range**: B228:DD238
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D232:K238`
      - Monthly data: `M232:DD238`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Financial - Other, Total Docs - Reduction.
- **Notes & Customizations**: Values are scaled by 1000.

### Total Docs - Reduction
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total document reduction metrics.
- **Cell Range**: B240:DD248
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D242:K248`
      - Monthly data: `M242:DD248`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial - Other, Total.
- **Notes & Customizations**: Values are scaled by 1000.

### Total Docs - Unadjusted
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total document consumption metrics, unadjusted.
- **Cell Range**: B250:DD258
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D252:K258`
      - Monthly data: `M252:DD258`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial - Other, Total.
- **Notes & Customizations**: Values are scaled by 1000.

### FDS RT Users Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of FDS RT (Real-Time) users, including users added, enabled users, and active users, by product type and segment.
- **Cell Range**: B261:DD297
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3. Row 2 contains years (2020-2027) for annual data. Row 3 contains monthly dates.
    - **Data Range**:
      - Annual data: `D265:K297`
      - Monthly data: `M265:DD297`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027
      - Monthly: 2020-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Users Added, Percent of New FDS RT Users Added, New FDS RT Users Added by Product, Enabled FDS RT Users, Total Enabled RT Users, Active FDS RT Users, Total Active RT Users, Percent of Active FDS RT Users, Total Percent of Active RT Users.
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 43: FDS RT Minimums
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: FDS RT Minimums
- **Key Sections Identified**:
    - User Tier Pricing Table

## 2. Detailed Section Analysis

### Section Name (e.g., "User Tier Pricing Table")
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the pricing structure for different user tiers, including incremental users, fee per user, and minimum/maximum total fees. It's used to determine the cost based on the number of users.
- **Cell Range**: B2:J26
- **Layout Structure**:
    - **Row Headers Location**: Column B (User Tiers)
    - **Column Headers Location**: Row 2 (User Tiers, Incremental Users, Fee Per User, Total, Max Discount, Min Total (Annual), Max Total, Min Total (Monthly))
    - **Data Range**:
      - B3:B26 (User Tier)
      - C3:C26 (Incremental Users)
      - D3:E26 (Fee Per User and Total)
      - G3:J26 (Max Discount, Min Total (Annual), Max Total, Min Total (Monthly))
- **Time Series Details**:
    - No time series data is present in this section.
- **Key Components**: User Tiers, Incremental Users, Fee Per User, Total, Max Discount, Min Total (Annual), Max Total, Min Total (Monthly)
- **Notes & Customizations**: The fee per user is reset at each tier. All monetary values are scaled by 1000 (likely representing thousands of dollars).


====================================================================================================
# SHEET 44: Product User Splits
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Product User Splits
- **Key Sections Identified**:
    - Product User Data (Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR)
    - BRM Data (BRM - Global, BRM - Single)
    - FactSet RT Data
    - FactSet AMR Data
    - FactSet AMR Breakdown Data (FactSet AMR / Active, FactSet AMR / Trailers, FactSet AMR / Internal)
    - FactSet AMR Docs Purchased Data (FactSet AMR Active Docs Purchased, FactSet AMR Trialer Docs Purchased, FactSet AMR Internal Docs Purchased)

## 2. Detailed Section Analysis

### Section Name: Product User Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the user counts for various products (Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR). It provides a breakdown of user data for each product across different time periods.
- **Cell Range**: B5:BP73
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data (First Series): `D7:AT73`
      - Monthly data (Second Series): `AV7:BP73`
- **Time Series Details**:
    - **Date Range**:
      - Monthly (First Series): 2017-01-31 to 2020-07-31
      - Monthly (Second Series): 2017-01-31 to 2018-09-30
    - **Frequency**: Monthly
- **Key Components**: Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR ($15k), AMR ($30k), AMR.
- **Notes & Customizations**: The data is scaled by 1000. There are two distinct monthly time series. Column AK contains an "x" for each product.

### Section Name: BRM Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the user counts for BRM products, broken down into Global and Single versions.
- **Cell Range**: B75:BP87
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data (First Series): `D76:AT87`
      - Monthly data (Second Series): `AV76:BP87`
- **Time Series Details**:
    - **Date Range**:
      - Monthly (First Series): 2017-01-31 to 2020-07-31
      - Monthly (Second Series): 2017-01-31 to 2018-09-30
    - **Frequency**: Monthly
- **Key Components**: BRM - Global, BRM - Single.
- **Notes & Customizations**: The data is scaled by 1000. There are two distinct monthly time series.

### Section Name: FactSet RT Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the user counts for FactSet RT.
- **Cell Range**: B89:AT94
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data: `AB90:AT94`
- **Time Series Details**:
    - **Date Range**: 2017-02-28 to 2020-07-31
    - **Frequency**: Monthly
- **Key Components**: FactSet RT
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: FactSet AMR Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the user counts for FactSet AMR.
- **Cell Range**: B96:AR101
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data: `AK97:AR101`
- **Time Series Details**:
    - **Date Range**: 2017-09-30 to 2018-04-30
    - **Frequency**: Monthly
- **Key Components**: FactSet AMR
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: FactSet AMR Breakdown Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the user counts for FactSet AMR, broken down by Active, Trailers, and Internal.
- **Cell Range**: B103:AR110
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data: `AB104:AR110`
- **Time Series Details**:
    - **Date Range**: 2017-02-28 to 2018-04-30
    - **Frequency**: Monthly
- **Key Components**: FactSet AMR / Active, FactSet AMR / Trailers, FactSet AMR / Internal
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: FactSet AMR Docs Purchased Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the number of documents purchased for FactSet AMR, broken down by Active, Trailers, and Internal.
- **Cell Range**: B112:AR119
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data: `AB113:AR119`
- **Time Series Details**:
    - **Date Range**: 2017-02-28 to 2018-04-30
    - **Frequency**: Monthly
- **Key Components**: FactSet AMR Active Docs Purchased, FactSet AMR Trialer Docs Purchased, FactSet AMR Internal Docs Purchased
- **Notes & Customizations**: The data is scaled by 1000.


====================================================================================================
# SHEET 45: TR BRM
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: TR BRM
- **Key Sections Identified**:
    - Tiered Pricing Data
    - User Segmentation Data
    - Financial Segmentation Data

## 2. Detailed Section Analysis

### Tiered Pricing Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows pricing and usage data broken down by different tiers of users. It's used to track revenue and usage across different customer segments.
- **Cell Range**: A2:AB9
- **Layout Structure**:
    - **Row Headers Location**: A3:A9, D3:D9
    - **Column Headers Location**: D2:E2, F2:W2, AA2:AB2
    - **Data Range**:
      - Monthly data: `F3:W9`
      - Mix/AB data: `AA3:AB9`
- **Time Series Details**:
    - **Date Range**: Jan 17 to Jun 18
    - **Frequency**: Monthly
- **Key Components**: Tier (Global Users (1-10), Global Users (11-50), Global Users (51+), Single Region 1-10, Single Region 11-25, Single Region 26-50, Single Region 50+), Pricing, Jan 17 - Jun 18, Mix, AB.
- **Notes & Customizations**: Pricing data is scaled by 1000.

### User Segmentation Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides aggregated user data segmented by global vs. single region users. It's used to understand the overall user base distribution.
- **Cell Range**: D36:W37
- **Layout Structure**:
    - **Row Headers Location**: D36:D37
    - **Column Headers Location**: F2:W2
    - **Data Range**:
      - Monthly data: `F36:W37`
- **Time Series Details**:
    - **Date Range**: Jan 17 to Jun 18
    - **Frequency**: Monthly
- **Key Components**: Global research users, Single region users.
- **Notes & Customizations**: Data is scaled by 1000.

### Financial Segmentation Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows financial data segmented by Financial, Corporate, and Other categories. It's used to track revenue and usage across different financial segments.
- **Cell Range**: C3:W31
- **Layout Structure**:
    - **Row Headers Location**: C3:C30
    - **Column Headers Location**: F2:W2
    - **Data Range**:
      - Monthly data: `F3:W31`
- **Time Series Details**:
    - **Date Range**: Jan 17 to Jun 18
    - **Frequency**: Monthly
- **Key Components**: Financial, Corporate, Other.
- **Notes & Customizations**: Data is scaled by 1000.


====================================================================================================
# SHEET 46: AMR
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: AMR
- **Key Sections Identified**:
    - Monthly Data Table
    - Cost Breakdown Table

## 2. Detailed Section Analysis

### Monthly Data Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays monthly data for key metrics related to firms, users, and fees. It allows for tracking performance trends over time.
- **Cell Range**: A1:AA18
- **Layout Structure**:
    - **Row Headers Location**: A1:A18
    - **Column Headers Location**: B1:AA2
    - **Data Range**:
      - Monthly data: `B3:AA18`
- **Time Series Details**:
    - **Date Range**: Jan'17 to Jun'18
    - **Frequency**: Monthly
- **Key Components**: Month, Total Firms, Total users, Fees
- **Notes & Customizations**: Fees are scaled by 1000.

### Cost Breakdown Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down costs into different categories: Corporate, Financial, and Other. It provides a summary of cost allocation.
- **Cell Range**: G3:H23
- **Layout Structure**:
    - **Row Headers Location**: G3:G23
    - **Column Headers Location**: H2:H23
    - **Data Range**: `H3:H23`
- **Time Series Details**:
    - **Date Range**: Not Applicable (Static data)
    - **Frequency**: Not Applicable
- **Key Components**: Corporate, Financial, Other, $15k, $30k
- **Notes & Customizations**: The data is static and doesn't represent a time series.



====================================================================================================
# SHEET 47: LN
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: LN
- **Key Sections Identified**:
    - Header
    - Financial Data Section

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the date series headers for the financial data section.
- **Cell Range**: D1:T1
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: D1:T1
    - **Data Range**: D1:T1
- **Time Series Details**:
    - **Date Range**: 2017-02 to 2018-06
    - **Frequency**: Monthly
- **Key Components**: Month-Year labels (e.g., "2017-2 Feb", "2017-3 Mar")
- **Notes & Customizations**: The header row contains month-year strings.

### Financial Data Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains financial data, potentially representing revenue or expenses, broken down by category and time period.
- **Cell Range**: B3:T9
- **Layout Structure**:
    - **Row Headers Location**: B3:B7, B9
    - **Column Headers Location**: C3:T3
    - **Data Range**:
      - Monthly data: C4:T7, C9:T9
- **Time Series Details**:
    - **Date Range**: 2017-01-31 to 2018-06-30
    - **Frequency**: Monthly
- **Key Components**: Corporate, Other
- **Notes & Customizations**: The section contains numerical data associated with the monthly time series.


====================================================================================================
# SHEET 48: DJ
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: DJ
- **Key Sections Identified**:
    - Header
    - Financial Data Section

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the sheet title and potentially other high-level information.
- **Cell Range**: B3:B3
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: B3
- **Time Series Details**: N/A
- **Key Components**: "Financial"
- **Notes & Customizations**: This section is very small, containing only the word "Financial".

### Financial Data Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section appears to contain financial data, potentially broken down by corporate and other categories, across a monthly time series.
- **Cell Range**: B4:T7
- **Layout Structure**:
    - **Row Headers Location**: B4:B6
    - **Column Headers Location**: C2
    - **Data Range**:
      - Monthly data: C4:T7
- **Time Series Details**:
    - **Date Range**: 2017-01-01 to 2018-06-01
    - **Frequency**: Monthly
- **Key Components**: Corporate, Other
- **Notes & Customizations**: The data is broken down into "Corporate" and "Other" categories. The dates are in row 2 from C2:T2. The values are in number format.


====================================================================================================
# SHEET 49: TR Transcripts
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: TR Transcripts
- **Key Sections Identified**:
    - Top Section (Quarterly Data)
    - Bottom Section (Monthly Data)

## 2. Detailed Section Analysis

### Top Section (Quarterly Data)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents key financial and operational metrics for various entities (Corporate, Financial, Other, Broker Partner) on a quarterly basis. It allows for tracking performance trends over time.
- **Cell Range**: B2:H8
- **Layout Structure**:
    - **Row Headers Location**: B3:B7
    - **Column Headers Location**: C2:H2
    - **Data Range**: C3:H7
- **Time Series Details**:
    - **Date Range**: 2017-Q1 to 2018-Q2
    - **Frequency**: Quarterly
- **Key Components**: Corporate, Financial, Other, Broker Partner. The specific metrics are not labeled in the provided data, but are represented by the numeric values in rows C3:H7.
- **Notes & Customizations**: The metrics are not explicitly labeled, so the exact meaning of the numbers is unknown without further context.

### Bottom Section (Monthly Data)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents key financial and operational metrics for various entities (Corporate, Financial, Other, Broker Partner) on a monthly basis. It allows for tracking performance trends over time.
- **Cell Range**: B11:T17
- **Layout Structure**:
    - **Row Headers Location**: B13:B16
    - **Column Headers Location**: C11:T11
    - **Data Range**: C13:T16
- **Time Series Details**:
    - **Date Range**: 2017-01-01 to 2018-06-01
    - **Frequency**: Monthly
- **Key Components**: Corporate, Financial, Other, Broker Partner. The specific metrics are not labeled in the provided data, but are represented by the numeric values in rows C13:T16.
- **Notes & Customizations**: The metrics are not explicitly labeled, so the exact meaning of the numbers is unknown without further context.


====================================================================================================
# SHEET 50: FS Transcripts
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: FS Transcripts
- **Key Sections Identified**:
    - Revenue Breakdown (Quarterly)
    - Revenue Breakdown (Monthly)

## 2. Detailed Section Analysis

### Revenue Breakdown (Quarterly)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a breakdown of revenue by different categories (Financial, Corporate, Other, Broker Partner) on a quarterly basis. It allows for tracking revenue performance over time.
- **Cell Range**: B5:H9
- **Layout Structure**:
    - **Row Headers Location**: B5:B9
    - **Column Headers Location**: C4:H4
    - **Data Range**: C5:H9
- **Time Series Details**:
    - **Date Range**: 2017-Q1 to 2018-Q2
    - **Frequency**: Quarterly
- **Key Components**: Financial, Corporate, Other, Broker Partner revenue.
- **Notes & Customizations**: Revenue is categorized into four segments.

### Revenue Breakdown (Monthly)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a breakdown of revenue by different categories (Financial, Corporate, Other, Broker Partner) on a monthly basis. It allows for tracking revenue performance over time.
- **Cell Range**: B13:T17
- **Layout Structure**:
    - **Row Headers Location**: B13:B17
    - **Column Headers Location**: C12:T12
    - **Data Range**: C13:T17
- **Time Series Details**:
    - **Date Range**: 2017-01-01 to 2018-06-01
    - **Frequency**: Monthly
- **Key Components**: Financial, Corporate, Other, Broker Partner revenue.
- **Notes & Customizations**: Revenue is categorized into four segments.


====================================================================================================
# SHEET 51: Filings
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Filings
- **Key Sections Identified**:
    - Revenue Breakdown

## 2. Detailed Section Analysis

### Section Name: Revenue Breakdown
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a breakdown of revenue by different categories (Other, Corporate, Broker Partner) over a monthly time series. It allows for analysis of revenue streams and their trends.
- **Cell Range**: B2:T8
- **Layout Structure**:
    - **Row Headers Location**: B4:B7
    - **Column Headers Location**: C2:T2
    - **Data Range**:
      - Monthly data: C4:T7
- **Time Series Details**:
    - **Date Range**: 2017-01-01 to 2018-06-01
    - **Frequency**: Monthly
- **Key Components**: Other, Corporate, Broker Partner, Financial
- **Notes & Customizations**: The numbers in columns L to N are scaled by 1000.


====================================================================================================
# SHEET 52: Detailed Income Statement
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Detailed Income Statement
- **Key Sections Identified**:
    - Header
    - Income Statement
    - Personnel Cost Breakdown

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and column headers.
- **Cell Range**: A1:E3
- **Layout Structure**:
    - **Row Headers Location**: A1:D3
    - **Column Headers Location**: E3
    - **Data Range**: N/A
- **Time Series Details**: None
- **Key Components**: "Income Statement", "Account Group", "Account Number", "Account Name", "Account Type"
- **Notes & Customizations**: Standard header information.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, detailing revenue, cost of service, expenses, and ultimately, net income.
- **Cell Range**: A5:BV157
- **Layout Structure**:
    - **Row Headers Location**: Column A and D
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `F6:R157`
      - Monthly data: `S6:BV157`
- **Time Series Details**:
    - **Date Range**:
      - Annual: Assuming F3:R3 represents a range of years, e.g., 2015 to 2027. The exact years are not specified in the provided data.
      - Monthly: Assuming S3:BV3 represents a range of months. The exact months are not specified in the provided data, but based on the "Actual" label in S2:BV2, it's likely a series of monthly "Actual" values.
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Revenue, Total Revenue, Cost of Service, Total COS, Gross Profit, Expenses, Total Expenses, Other Income, Total Other Income, Taxes, Total Taxes, Interest, Interest Net, Net Income/(loss)
- **Notes & Customizations**: The data is presented in thousands (scale = 1000). There are sections for "People Costs", "Travel Costs", "Facilities Costs", "Marketing Costs", "General and Administrative Costs", "Legal Costs", "Other Costs", and "Depreciation & Amortization" within the Expenses section.

### Personnel Cost Breakdown
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of personnel costs, including salaries, commission, bonus, benefits, recruiting fees, relocation, contractors, and outsourced R&D.
- **Cell Range**: D158:AM167
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: Row 158
    - **Data Range**: `F159:AM167`
- **Time Series Details**:
    - **Date Range**: Assuming F158:AM158 represents a range of months. The exact months are not specified in the provided data.
    - **Frequency**: Monthly
- **Key Components**: Salaries, Commission, Bonus, Benefits, Recruiting Fees, Relocation, Contractors, Outsourced R&D, Payroll Taxes, Worker Comp
- **Notes & Customizations**: The data is presented in thousands (scale = 1000).



====================================================================================================
# SHEET 53: Detailed Balance Sheet
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Detailed Balance Sheet
- **Key Sections Identified**:
    - Header
    - Assets
    - Liabilities
    - Equity
    - Liabilities & Equity Reconciliation

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report.
- **Cell Range**: A1:E3
- **Layout Structure**:
    - **Row Headers Location**: A1, A3, C3, D3, E3
    - **Column Headers Location**: None
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Balance Sheet, Account Group, Account Number, Account Name, Account Type
- **Notes & Customizations**: Basic header information.

### Section Name: Assets
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's assets, broken down into current, long-term, and fixed assets.
- **Cell Range**: A4:BV32
- **Layout Structure**:
    - **Row Headers Location**: A4, B6, D7:D18, B19, B21, D22, B23, B25, D26:D29, B30, A32
    - **Column Headers Location**: F2:BV2 (Implied "Actual" for each period)
    - **Data Range**:
      - Monthly data: F7:BV19, F22:BV23, F26:BV30, F32:BV32
      - AE9:BV9, AE12:BV12
- **Time Series Details**:
    - **Date Range**: Dates are not explicitly provided, but the column headers from F2 to BV2 imply a monthly time series. The exact dates are not available in the provided JSON.
    - **Frequency**: Monthly
- **Key Components**: Current Assets (Cash, Accounts Receivable, Prepaid Expenses), Long Term Assets, Fixed Assets (Capitalized R&D), Total Assets.
- **Notes & Customizations**: Data is scaled by 1000. Includes contra-asset accounts like Accumulated Depreciation.

### Section Name: Liabilities
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's liabilities, broken down into current and long-term liabilities.
- **Cell Range**: A34:BV83
- **Layout Structure**:
    - **Row Headers Location**: A34, B36, D37:D50, D52, D54:D69, B70, B72, D73:D79, D80, D82, B83
    - **Column Headers Location**: F2:BV2 (Implied "Actual" for each period)
    - **Data Range**:
      - Monthly data: F37:BV70, F73:BV83
      - G53:BV53
      - AE80:BV82
- **Time Series Details**:
    - **Date Range**: Dates are not explicitly provided, but the column headers from F2 to BV2 imply a monthly time series. The exact dates are not available in the provided JSON.
    - **Frequency**: Monthly
- **Key Components**: Current Liabilities (Accounts Payable, Accrued Expenses, Deferred Revenue), Long Term Liabilities (Long-term loans, Convertible Notes).
- **Notes & Customizations**: Data is scaled by 1000. Includes intercompany accounts.

### Section Name: Equity
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's equity accounts.
- **Cell Range**: A87:BV98
- **Layout Structure**:
    - **Row Headers Location**: A87, D88:D90, D92:D93, D96:D97, A98
    - **Column Headers Location**: F2:BV2 (Implied "Actual" for each period)
    - **Data Range**:
      - Monthly data: F88:BV98
      - F91:BV91
      - F94:BV94
      - F95:AD95
- **Time Series Details**:
    - **Date Range**: Dates are not explicitly provided, but the column headers from F2 to BV2 imply a monthly time series. The exact dates are not available in the provided JSON.
    - **Frequency**: Monthly
- **Key Components**: Common Stock, Preferred Stock, Net Income, Retained Earnings, Total Equity.
- **Notes & Customizations**: Data is scaled by 1000.

### Section Name: Liabilities & Equity Reconciliation
- **Section Type**: Balance Sheet
- **Description & Purpose**: Reconciles total liabilities and equity.
- **Cell Range**: A100:BV101
- **Layout Structure**:
    - **Row Headers Location**: A100, A101
    - **Column Headers Location**: F2:BV2 (Implied "Actual" for each period)
    - **Data Range**:
      - Monthly data: F100:BV101
- **Time Series Details**:
    - **Date Range**: Dates are not explicitly provided, but the column headers from F2 to BV2 imply a monthly time series. The exact dates are not available in the provided JSON.
    - **Frequency**: Monthly
- **Key Components**: Total Liabilities & Equity, Check
- **Notes & Customizations**: Data is scaled by 1000. Includes a "Check" row, likely to verify that Assets = Liabilities + Equity.


====================================================================================================
# SHEET 54: Detailed Cash Flow Satement
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Detailed Cash Flow Satement
- **Key Sections Identified**:
    - Cash Flow Statement

## 2. Detailed Section Analysis

### Section Name (Cash Flow Statement)
- **Section Type**: Standard Cash Flow Statement
- **Description & Purpose**: This section presents the company's cash inflows and outflows, categorized into operating, investing, and financing activities. It reconciles net income to the ending cash balance.
- **Cell Range**: A1:BV85
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data: G6:BV85
- **Time Series Details**:
    - **Date Range**: 2015-01-01 to 2020-08-31
    - **Frequency**: Monthly
- **Key Components**:
    - Net Income
    - Decrease (Increase) in Operating Assets (e.g., Accounts Receivable, Prepaid Expenses)
    - (Decrease) Increase in Operating Liabilities (e.g., Accounts Payable, Accrued Expenses)
    - Net Cash Flows from Operating Activities
    - Fixed Assets
    - Capitalized R&D
    - Net Cash Flows from Investing Activities
    - Unrealized Subsidy
    - Short Term Loans
    - Capital Loans
    - Long-term loans
    - Common Stock
    - Preferred Series A
    - Net Cash Flows from Financing Activities
    - Cash, Beginning of Period
    - Net Change in Cash
    - Cash, End of Period
- **Notes & Customizations**: The values are scaled by 1000. The statement includes specific loan items (Tekes loans, SVB Line of Credit). There is a "Check" row at the end.



====================================================================================================
# SHEET 55: Key Metrics
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Key Metrics
- **Key Sections Identified**:
    - Annual Subscription Value
    - ARR Added (Gross)
    - ARR Churn
    - ARR Churn Notifications
    - # of Client Firms
    - # of Users
    - SaaS Metrics
    - Contract Duration
    - Client Counts
    - User Counts
    - Cancels
    - ARR New/Upsell/Increase $
    - Monthly Recurring Revenue

## 2. Detailed Section Analysis

### Section Name: Annual Subscription Value
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the annual subscription value, providing a high-level overview of the company's recurring revenue.
- **Cell Range**: A4:CG4
- **Layout Structure**:
    - **Row Headers Location**: A4
    - **Column Headers Location**: C4:CG4
    - **Data Range**: C4:BB4, BC4:BT4, BV4:CG4
- **Time Series Details**:
    - **Date Range**: 2015 to Sales Plan (Implied from I1, O1, AA1, BV1)
    - **Frequency**: Annual
- **Key Components**: Annual Subscription Value
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: ARR Added (Gross)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the gross annual recurring revenue added, broken down by new sales, upsells, and increases.
- **Cell Range**: A6:CG16
- **Layout Structure**:
    - **Row Headers Location**: A6:B16
    - **Column Headers Location**: C4:CG4
    - **Data Range**: C6:BT16, BV6:CG6
- **Time Series Details**:
    - **Date Range**: 2015 to Sales Plan (Implied from I1, O1, AA1, BV1)
    - **Frequency**: Annual
- **Key Components**: ARR Added (Gross), New Sales, Upsells, Increases, Financial, Corporate, Other
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: ARR Churn
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the annual recurring revenue churn, broken down by controllable and uncontrollable factors.
- **Cell Range**: A17:BT21
- **Layout Structure**:
    - **Row Headers Location**: A17:B21
    - **Column Headers Location**: C4:BT4
    - **Data Range**: C17:BT21
- **Time Series Details**:
    - **Date Range**: 2015 to 2017 Actuals (Implied from I1, O1, AA1)
    - **Frequency**: Annual
- **Key Components**: ARR Churn, Uncontrollable, Controllable, % Controllable, % YTD Controllable
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: ARR Churn Notifications
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the annual recurring revenue churn notifications, broken down by reasons such as downsizing, competitor, insufficient value, low use, and users leaving.
- **Cell Range**: A27:BT33
- **Layout Structure**:
    - **Row Headers Location**: A27:B33
    - **Column Headers Location**: C4:BT4
    - **Data Range**: O27:BT33
- **Time Series Details**:
    - **Date Range**: 2016 to 2017 Actuals (Implied from O1, AA1)
    - **Frequency**: Annual
- **Key Components**: ARR Churn Notifications, Budget/Firm Downsizing, Competitor, Insufficient value, Low use/engagement, User(s) left firm, Other
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: # of Client Firms
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the number of client firms, including additions and losses.
- **Cell Range**: A35:BT38
- **Layout Structure**:
    - **Row Headers Location**: A35:A37
    - **Column Headers Location**: C4:BT4
    - **Data Range**: C35:BT38
- **Time Series Details**:
    - **Date Range**: 2015 to 2017 Actuals (Implied from I1, O1, AA1)
    - **Frequency**: Annual
- **Key Components**: # of Client Firms, # of Client Firms Added, # of Client Firms Lost
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: # of Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the number of users, including additions and losses.
- **Cell Range**: A39:BT41
- **Layout Structure**:
    - **Row Headers Location**: A39:A41
    - **Column Headers Location**: C4:BT4
    - **Data Range**: C39:BT41
- **Time Series Details**:
    - **Date Range**: 2015 to 2017 Actuals (Implied from I1, O1, AA1)
    - **Frequency**: Annual
- **Key Components**: # of Users, # of Gross Users Added, # of Gross Users Lost
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: SaaS Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks various SaaS metrics, including ARR, churn, and contract duration.
- **Cell Range**: A46:BT68
- **Layout Structure**:
    - **Row Headers Location**: A46:B68
    - **Column Headers Location**: C4:BT4
    - **Data Range**: C47:BT68
- **Time Series Details**:
    - **Date Range**: 2015 to 2017 Actuals (Implied from I1, O1, AA1)
    - **Frequency**: Annual
- **Key Components**: ARR, Churn, Total Churn $, Total Churn %, Rolling 12 Month Churn %, Customer Churn %, Net Churn % (Rolling 12m), Net Retention % (Rolling 12m)
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Contract Duration
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks contract duration metrics.
- **Cell Range**: A70:BT94
- **Layout Structure**:
    - **Row Headers Location**: A70:B94
    - **Column Headers Location**: C4:BT4
    - **Data Range**: O72:BT94
- **Time Series Details**:
    - **Date Range**: 2016 to 2017 Actuals (Implied from O1, AA1)
    - **Frequency**: Annual
- **Key Components**: New Contracts, Average contract Length, Weighted average contract Length, Existing Clients
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Deal Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks deal metrics, including average client size and ARPU.
- **Cell Range**: A96:BT119
- **Layout Structure**:
    - **Row Headers Location**: A96:B119
    - **Column Headers Location**: C4:BT4
    - **Data Range**: C97:BT119
- **Time Series Details**:
    - **Date Range**: 2015 to 2017 Actuals (Implied from I1, O1, AA1)
    - **Frequency**: Annual
- **Key Components**: Total Average Client Size, New Client Average Size, New Sales ARPU, Total User Base ARPU
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Raw Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains raw data related to renewal opportunities.
- **Cell Range**: A123:BT142
- **Layout Structure**:
    - **Row Headers Location**: A123:B142
    - **Column Headers Location**: C4:BT4
    - **Data Range**: C124:BT142
- **Time Series Details**:
    - **Date Range**: 2015 to 2017 Actuals (Implied from I1, O1, AA1)
    - **Frequency**: Annual
- **Key Components**: Renewal Opportunities $, Renewal Opportunities (Count), Renewal Opp's Check, ARR
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Contract Length
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks contract length metrics.
- **Cell Range**: A144:BT168
- **Layout Structure**:
    - **Row Headers Location**: A144:B168
    - **Column Headers Location**: C4:BT4
    - **Data Range**: O146:BT168
- **Time Series Details**:
    - **Date Range**: 2016 to 2017 Actuals (Implied from O1, AA1)
    - **Frequency**: Annual
- **Key Components**: New Contracts, Average contract Length, Weighted average contract Length, Existing Clients
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Client Counts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks client counts, including new and existing firms.
- **Cell Range**: A169:BT180
- **Layout Structure**:
    - **Row Headers Location**: A169:B180
    - **Column Headers Location**: C4:BT4
    - **Data Range**: O170:BT180
- **Time Series Details**:
    - **Date Range**: 2016 to 2017 Actuals (Implied from O1, AA1)
    - **Frequency**: Annual
- **Key Components**: New firms, Existing Firms, Total Firms
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: User Counts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks user counts, broken down by various categories.
- **Cell Range**: A182:AU255
- **Layout Structure**:
    - **Row Headers Location**: A182:B255
    - **Column Headers Location**: C4:AU4
    - **Data Range**: T183:AU255
- **Time Series Details**:
    - **Date Range**: 2016 to 2017 Actuals (Implied from O1, AA1)
    - **Frequency**: Annual
- **Key Components**: Financial, Corporate, Other, BRM (PRM Global), BRM Global, BRM Single, PRM Global, PRM Single region, Empty Container, AMR $30K (PRM Single region), AMR $30K (PRM Global), Inactive, AMR $15K (PRM Global), AMR $15K (PRM Single), Check
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Cancels
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks cancels, including cancels dollar amount, cancels count, and cancels users.
- **Cell Range**: A256:BT274
- **Layout Structure**:
    - **Row Headers Location**: A256:B274
    - **Column Headers Location**: C4:BT4
    - **Data Range**: C257:BT274
- **Time Series Details**:
    - **Date Range**: 2015 to 2017 Actuals (Implied from I1, O1, AA1)
    - **Frequency**: Annual
- **Key Components**: Cancels $, Cancels Count, Cancels Users, Financial, Corporate, Other
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: ARR New/Upsell/Increase $
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks ARR from new sales, upsells, and increases.
- **Cell Range**: A276:BT334
- **Layout Structure**:
    - **Row Headers Location**: A276:B334
    - **Column Headers Location**: C4:BT4
    - **Data Range**: C276:BT334
- **Time Series Details**:
    - **Date Range**: 2015 to 2017 Actuals (Implied from I1, O1, AA1)
    - **Frequency**: Annual
- **Key Components**: ARR New $, ARR Upsell/Increase $, Deal Count, User Count, Financial, Corporate, Other
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Monthly Recurring Revenue
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks monthly recurring revenue.
- **Cell Range**: A354:AU499
- **Layout Structure**:
    - **Row Headers Location**: A354
    - **Column Headers Location**: C4:AU4
    - **Data Range**: C354:AU499
- **Time Series Details**:
    - **Date Range**: 2015 to 2017 Actuals (Implied from I1, O1, AA1)
    - **Frequency**: Annual
- **Key Components**: Monthly Recurring Revenue
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 56: Revenue by Client
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Revenue by Client
- **Key Sections Identified**:
    - Revenue Summary by Client
    - Income Statement (Fragment)
    - Monthly Data (2015)
    - Monthly Data (2016)
    - Monthly Data (2017)

## 2. Detailed Section Analysis

### Section Name: Revenue Summary by Client
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes revenue data by client (Corporate, Other, and a blank category), providing a high-level overview of revenue streams.
- **Cell Range**: A3:BT11
- **Layout Structure**:
    - **Row Headers Location**: A5:A11
    - **Column Headers Location**: B3:BT4
    - **Data Range**:
      - Annual data: C7:AA8
      - Monthly data: C6:Z6, AB6:AG6, AI6:BT6, C9:AR9, C11:BD11, BE11:BI11, BK11:BU11
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2017
      - Monthly: Jan 2015 to Dec 2017 (implied from monthly column headers)
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Sum of Current Rev, Row Labels, Column Labels, Corporate, Other, (blank), Grand Total.
- **Notes & Customizations**: The data is presented in thousands (scale = 1000). There are multiple time series present: annual summaries (2015, 2016, 2017) and monthly data.

### Section Name: Income Statement (Fragment)
- **Section Type**: Standard P&L
- **Description & Purpose**: This section appears to be a fragment of an Income Statement, potentially showing some key financial metrics.
- **Cell Range**: AM15:BJ22
- **Layout Structure**:
    - **Row Headers Location**: Not explicitly defined, but implied to be in column AM.
    - **Column Headers Location**: Not explicitly defined, but implied to be in row 15 or 16.
    - **Data Range**: AM15:BJ16, AM17:BJ17, AM19:AX19, AY19:BD19, BE19:BG19, BH19:BJ19, AM20:AX20, AY20:BD20, BE20:BG20, BH20:BJ20, AM21:AX21, AY21:BD21, BE21:BG21, BH21:BJ21, AM22:AR22
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but likely represents a single period or a small number of periods.
    - **Frequency**: Unknown.
- **Key Components**: Income Statement (label in Y17).
- **Notes & Customizations**: This appears to be an incomplete Income Statement section. Some values are scaled by 1000.

### Section Name: Monthly Data (2015)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains monthly revenue data for the year 2015.
- **Cell Range**: C5:N11
- **Layout Structure**:
    - **Row Headers Location**: A5:A11
    - **Column Headers Location**: C5:N5
    - **Data Range**: C6:N11
- **Time Series Details**:
    - **Date Range**: Jan 2015 to Dec 2015
    - **Frequency**: Monthly
- **Key Components**: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec, Row Labels.
- **Notes & Customizations**: The data is presented in thousands (scale = 1000).

### Section Name: Monthly Data (2016)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains monthly revenue data for the year 2016.
- **Cell Range**: O5:Z11
- **Layout Structure**:
    - **Row Headers Location**: A5:A11
    - **Column Headers Location**: O5:Z5
    - **Data Range**: O6:Z11
- **Time Series Details**:
    - **Date Range**: Jan 2016 to Dec 2016
    - **Frequency**: Monthly
- **Key Components**: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec, Row Labels.
- **Notes & Customizations**: The data is presented in thousands (scale = 1000).

### Section Name: Monthly Data (2017)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains monthly revenue data for the year 2017.
- **Cell Range**: AA5:AL11
- **Layout Structure**:
    - **Row Headers Location**: A5:A11
    - **Column Headers Location**: AA5:AL5
    - **Data Range**: AA6:AL11
- **Time Series Details**:
    - **Date Range**: Jan 2017 to Dec 2017
    - **Frequency**: Monthly
- **Key Components**: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec, Row Labels.
- **Notes & Customizations**: The data is presented in thousands (scale = 1000).



====================================================================================================
# SHEET 57: Client Support
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Client Support
- **Key Sections Identified**:
    - Client Type Metrics (Corp, Corporate, Other)
    - Churned CARR - Lost Clients
    - Totals

## 2. Detailed Section Analysis

### Section Name: Client Type Metrics (Corp)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of clients of type "Corp" over time, showing beginning count, additions, churn, and ending count.
- **Cell Range**: C10:DU14
- **Layout Structure**:
    - **Row Headers Location**: C11:C14 (Beginning, Added, Churn, End)
    - **Column Headers Location**: E2:DU2 (Monthly Dates)
    - **Data Range**:
      - Monthly data: `F11:DU14`
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-10-31
    - **Frequency**: Monthly
- **Key Components**: Beginning, Added, Churn, End
- **Notes & Customizations**: Values are scaled by 1000 in columns G:DU.

### Section Name: Client Type Metrics (Corporate)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of clients of type "Corporate" over time, showing beginning count, additions, churn, and ending count.
- **Cell Range**: C16:DU20
- **Layout Structure**:
    - **Row Headers Location**: C17:C20 (Beginning, Added, Churn, End)
    - **Column Headers Location**: E2:DU2 (Monthly Dates)
    - **Data Range**:
      - Monthly data: `F17:DU20`
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-10-31
    - **Frequency**: Monthly
- **Key Components**: Beginning, Added, Churn, End
- **Notes & Customizations**: Values are scaled by 1000 in columns G:DU.

### Section Name: Client Type Metrics (Other)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of clients of type "Other" over time, showing beginning count, additions, churn, and ending count.
- **Cell Range**: C4:DU8
- **Layout Structure**:
    - **Row Headers Location**: C5:C8 (Beginning, Added, Churn, End)
    - **Column Headers Location**: E2:DU2 (Monthly Dates)
    - **Data Range**:
      - Monthly data: `F5:DU8`
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-10-31
    - **Frequency**: Monthly
- **Key Components**: Beginning, Added, Churn, End
- **Notes & Customizations**: Values are scaled by 1000 in columns G:DD.

### Section Name: Churned CARR - Lost Clients
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the Churned CARR for Lost Clients over time.
- **Cell Range**: C22:DF23
- **Layout Structure**:
    - **Row Headers Location**: C22
    - **Column Headers Location**: E2:DF2 (Monthly Dates)
    - **Data Range**:
      - Monthly data: `F23:DF23`
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2019-12-31 (inferred from data range DF23)
    - **Frequency**: Monthly
- **Key Components**: Churned CARR - Lost Clients
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Totals
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the total values over time.
- **Cell Range**: C24:DF26
- **Layout Structure**:
    - **Row Headers Location**: C24:C26 (Corporate, Other, Total)
    - **Column Headers Location**: E2:DF2 (Monthly Dates)
    - **Data Range**:
      - Monthly data: `F24:DF26`
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2019-12-31 (inferred from data range DF26)
    - **Frequency**: Monthly
- **Key Components**: Corporate, Other, Total
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 58: Subscriber Support
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Subscriber Support
- **Key Sections Identified**:
    - Subscriber Rollforward - Financial
    - Subscriber Rollforward - Corp
    - Subscriber Rollforward - Other
    - Cost Allocation

## 2. Detailed Section Analysis

### Section Name: Subscriber Rollforward - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the rollforward of subscriber counts for the "Financial" segment, showing the beginning count, additions, churn, and ending count over time.
- **Cell Range**: C4:DS8
- **Layout Structure**:
    - **Row Headers Location**: C5:C8
    - **Column Headers Location**: E2:DS2
    - **Data Range**:
      - Monthly data: F5:DS8
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-08-01
    - **Frequency**: Monthly
- **Key Components**: Beginning, Added, Churn, End
- **Notes & Customizations**: Values are scaled by 1000 in most of the data range, except for DA6:DS6 and DA18:DS18.

### Section Name: Subscriber Rollforward - Corp
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the rollforward of subscriber counts for the "Corp" segment, showing the beginning count, additions, churn, and ending count over time.
- **Cell Range**: C10:DS14
- **Layout Structure**:
    - **Row Headers Location**: C11:C14
    - **Column Headers Location**: E2:DS2
    - **Data Range**:
      - Monthly data: F11:DS14
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-08-01
    - **Frequency**: Monthly
- **Key Components**: Beginning, Added, Churn, End
- **Notes & Customizations**: Values are scaled by 1000 in most of the data range, except for DA12:DS12.

### Section Name: Subscriber Rollforward - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the rollforward of subscriber counts for the "Other" segment, showing the beginning count, additions, churn, and ending count over time.
- **Cell Range**: C16:DS20
- **Layout Structure**:
    - **Row Headers Location**: C17:C20
    - **Column Headers Location**: E2:DS2
    - **Data Range**:
      - Monthly data: F17:DS20
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-08-01
    - **Frequency**: Monthly
- **Key Components**: Beginning, Added, Churn, End
- **Notes & Customizations**: Values are scaled by 1000 in most of the data range, except for DA18:DS18.

### Section Name: Cost Allocation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the allocation of costs, specifically "Admin" costs, related to "Soros / Cap Group - Internal Content".
- **Cell Range**: CM25:CY26
- **Layout Structure**:
    - **Row Headers Location**: CM25:CM26
    - **Column Headers Location**: None (implicit time series)
    - **Data Range**:
      - Monthly data: CN25:CY26
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but implied to be a monthly series based on the column range E2:DS2 which has the date series "2010-10-01 to 2020-08-01"
    - **Frequency**: Monthly
- **Key Components**: Total, Admin, Soros / Cap Group - Internal Content
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 59: Headcount Support
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Headcount Support
- **Key Sections Identified**:
    - Department Headcount (Section 1)
    - Department Headcount (Section 2)
    - Sales Team Headcount

## 2. Detailed Section Analysis

### Section Name (Department Headcount - Section 1)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for various departments over time. It appears to have two separate time series: one with monthly data and another with budget data.
- **Cell Range**: A1:CI10
- **Layout Structure**:
    - **Row Headers Location**: Column A and B
    - **Column Headers Location**: Row 1
    - **Data Range**:
      - Monthly data: `D4:AV9`
      - Budget data: `AW4:CI10`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-01 to 2021-12-01
    - **Frequency**:
      - Monthly
- **Key Components**: Department, Headcount, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, VP Bus Dev, Engineering (India)
- **Notes & Customizations**: The data is presented in thousands (scale: 1000) for the monthly data. There is a "2020 Budget" column (BW2) which seems to be a separate time series or a specific budget target.

### Section Name (Department Headcount - Section 2)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for various departments over time. It appears to have two separate time series: one with monthly data and another with budget data.
- **Cell Range**: A23:BW30
- **Layout Structure**:
    - **Row Headers Location**: Column A and B
    - **Column Headers Location**: Row 1
    - **Data Range**:
      - Monthly data: `D24:AV29`
      - Budget data: `AW24:BW30`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-01 to 2021-12-01
    - **Frequency**:
      - Monthly
- **Key Components**: Department, Headcount, Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, VP Bus Dev, Engineering (India)
- **Notes & Customizations**: The data is presented in thousands (scale: 1000) for the monthly data. There is a "2020 Budget" column (BW2) which seems to be a separate time series or a specific budget target.

### Section Name (Sales Team Headcount)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for various roles within the sales team.
- **Cell Range**: B34:BW77
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 1
    - **Data Range**:
      - Monthly data: `D34:BH48`
      - Other data: `BI51:BW77`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-01 to 2021-12-01
    - **Frequency**:
      - Monthly
- **Key Components**: Account Manager, Account Manager - Corp, Account Executive - Financial, Account Executive - Corporate, Account Executive - Enterprise, Account Executive - Other, CRO, Sales Manager, Sales Team, Customer Success, Business Development
- **Notes & Customizations**: The data is presented in thousands (scale: 1000) for the monthly data. The data in columns BI:BW is not scaled. There are some headcount targets in columns BM and BN.



====================================================================================================
# SHEET 60: Salary Support
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Salary Support
- **Key Sections Identified**:
    - Department Salary Breakdown (High-Level)
    - Department Salary Breakdown (Detailed)
    - FX Rate
    - Quota Sales Reps & Team Costs

## 2. Detailed Section Analysis

### Section Name: Department Salary Breakdown (High-Level)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level breakdown of salary expenses by department. This is used to understand the overall allocation of salary budget across different functional areas.
- **Cell Range**: A1:CV10
- **Layout Structure**:
    - **Row Headers Location**: Column A (Department), Column B (Department)
    - **Column Headers Location**: Row 1 (Department, R&D, G&A, Mktg), Row 2 (Salary), Row 3 (Implied FTE)
    - **Data Range**:
      - Monthly data: `D3:CI10` (Monthly data series 1)
      - Monthly data: `CK3:CV10` (Monthly data series 2)
- **Time Series Details**:
    - **Date Range**:
      - Monthly (D3:CI10): 2015-01-01 to 2021-12-31
      - Monthly (CK3:CV10): 2021-01-31 to 2027-12-31
    - **Frequency**:
      - Monthly
      - Monthly
- **Key Components**: Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, VP Bus Dev, Engineering (India)
- **Notes & Customizations**: Salary expenses are shown in thousands. There are two distinct monthly time series.

### Section Name: Department Salary Breakdown (Detailed)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of salary expenses by specific roles within the sales and operations departments. This is used to understand the composition of salary expenses at a more granular level.
- **Cell Range**: B38:BW54
- **Layout Structure**:
    - **Row Headers Location**: Column B (Role)
    - **Column Headers Location**: Row 1 (Monthly Dates), Row 2 (2020 Budget)
    - **Data Range**:
      - Monthly data: `D38:BH54`
      - Monthly data: `BL40:BW40`
- **Time Series Details**:
    - **Date Range**: 2015-01-01 to 2021-06-01 (based on the first date series)
    - **Frequency**: Monthly
- **Key Components**: Account Manager, Account Manager - Corp, Account Executive - Financial, Account Executive - Corporate, Account Executive - Enterprise, Account Executive - Other, CRO, Manager - Corporate, Product Specialist, Product Specialist - Manager, Admin, Sales Operations Manager, Sales Development Rep, Sales Manager, Sales Recruiter, Operations
- **Notes & Customizations**: Salary expenses are shown in thousands.

### Section Name: FX Rate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the foreign exchange (FX) rates used for currency conversion.
- **Cell Range**: B57:BD57
- **Layout Structure**:
    - **Row Headers Location**: Column B (FX RATE)
    - **Column Headers Location**: Implicit based on date series
    - **Data Range**:
      - Monthly data: `AL57:AV57`
      - Monthly data: `AW57:BD57`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2016-12-01 to 2017-09-01 (inferred from data range)
      - Monthly: 2017-10-01 to 2018-01-01 (inferred from data range)
    - **Frequency**: Monthly
- **Key Components**: FX RATE
- **Notes & Customizations**: This section shows FX rates over time.

### Section Name: Quota Sales Reps & Team Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides details on quota-bearing sales representatives and related team costs. This allows for analysis of sales team compensation and performance.
- **Cell Range**: B60:BM86
- **Layout Structure**:
    - **Row Headers Location**: Column B (Role)
    - **Column Headers Location**: Implicit based on date series
    - **Data Range**:
      - Monthly data: `BI61:BM86`
- **Time Series Details**:
    - **Date Range**: 2015-09-01 to 2015-12-01 (inferred from data range)
    - **Frequency**: Monthly
- **Key Components**: Quota Sales Reps, AE - Financial (Quota), AE - Corporate (Quota), AM - Financial (Quota), VP Partnerships (Quota), Sales Team, CRO, Sales Manager, SDR Manager, SDR, Customer Success, CS Manager, AM - Financial, AM - Corporate, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, Business Development, GTM Strategy
- **Notes & Customizations**: Salary expenses are shown in thousands.


====================================================================================================
# SHEET 61: Bonus Support
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Bonus Support
- **Key Sections Identified**:
    - Department Salary Budget (2019 & 2020)
    - Adjustment Table
    - Department Salary Budget (2019 & 2020) - Repeated
    - Sales Bonus Summary
    - Department Bonus Breakdown

## 2. Detailed Section Analysis

### Section Name: Department Salary Budget (2019 & 2020)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the salary budget for each department for 2019 and 2020. It allows for comparison of budgets across departments and years.
- **Cell Range**: A1:AD10
- **Layout Structure**:
    - **Row Headers Location**: A1:B10
    - **Column Headers Location**: A1:AD2
    - **Data Range**:
      - 2019 Budget: D4:F10
      - 2020 Budget: G4:AD10
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2019-10-01 to 2020-12-01 (based on D1:AD1)
    - **Frequency**: Monthly
- **Key Components**: Department (Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, Engineering (India), Sales), Salary, 2019 Budget, 2020 Budget.
- **Notes & Customizations**: Budget numbers are scaled by 1000.

### Section Name: Adjustment Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows adjustments made to the salary budget for each department.
- **Cell Range**: B12:R20
- **Layout Structure**:
    - **Row Headers Location**: B13:B19
    - **Column Headers Location**: G12:R12 (Implicitly contains the months)
    - **Data Range**: G13:R19
- **Time Series Details**:
    - **Date Range**:
      - Monthly: Not explicitly defined, but likely corresponds to a subset of the monthly series in D1:CX1. Assuming G12 represents a month within 2020.
    - **Frequency**: Monthly
- **Key Components**: Adjustment, Department (Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, Engineering (India)), Monthly Adjustments.
- **Notes & Customizations**: Adjustment numbers are scaled by 1000.

### Section Name: Department Salary Budget (2019 & 2020) - Repeated
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section repeats the salary budget for each department for 2019 and 2020, likely for comparison or calculation purposes.
- **Cell Range**: A24:R31
- **Layout Structure**:
    - **Row Headers Location**: A24:B31
    - **Column Headers Location**: D24:R24 (Implicitly contains the months)
    - **Data Range**: D25:R31
- **Time Series Details**:
    - **Date Range**:
      - Monthly: Likely a subset of the monthly series in D1:CX1.
    - **Frequency**: Monthly
- **Key Components**: Department (Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, Engineering (India), Sales), Salary, Monthly Budgets.
- **Notes & Customizations**: Budget numbers are scaled by 1000.

### Section Name: Sales Bonus Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the sales bonus information, including total bonus and average attainment.
- **Cell Range**: B34:CX38
- **Layout Structure**:
    - **Row Headers Location**: B36, B38
    - **Column Headers Location**: D1:CX1 (Monthly)
    - **Data Range**: F36:CX36, F38:CX38
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2019-10-01 to 2027-12-01 (based on D1:CX1)
    - **Frequency**: Monthly
- **Key Components**: Total Sales Bonus, AVERAGE BONUS ATTAINMENT.
- **Notes & Customizations**: Total Sales Bonus is scaled by 1000.

### Section Name: Department Bonus Breakdown
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down the bonus information by department, providing details on count, total, and average bonus amounts.
- **Cell Range**: B41:CX56
- **Layout Structure**:
    - **Row Headers Location**: B42:B56
    - **Column Headers Location**: D41:CX41 (Monthly)
    - **Data Range**: D42:CX56
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2019-10-01 to 2027-12-01 (based on D1:CX1)
    - **Frequency**: Monthly
- **Key Components**: Count, Total, Avg, Department (CRO, VP of Sales, Sales Manager, SDR Manager, SDR, CS Manager, AM - Corporate, AM - Financial, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy).
- **Notes & Customizations**: Bonus numbers are scaled by 1000.

### Section Name: Department Bonus Breakdown (Repeated)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section repeats the bonus breakdown by department.
- **Cell Range**: B60:CX75
- **Layout Structure**:
    - **Row Headers Location**: B61:B75
    - **Column Headers Location**: F60:CX60 (Monthly)
    - **Data Range**: F61:CX75
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2019-12-31 to 2027-12-31 (based on F60:CX60)
    - **Frequency**: Monthly
- **Key Components**: Department (CRO, VP of Sales, Sales Manager, SDR Manager, SDR, CS Manager, AM - Corporate, AM - Financial, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy).
- **Notes & Customizations**: Bonus numbers are not scaled.


====================================================================================================
# SHEET 62: Bonus Support (Sales non Ops)
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Bonus Support (Sales non Ops)
- **Key Sections Identified**:
    - Salary & Bonus Budget
    - Sales Team Bonus Calculation

## 2. Detailed Section Analysis

### Salary & Bonus Budget
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the salary and bonus budget for the sales department. It provides a high-level overview of the allocated funds for salaries, adjustments, and total sales bonus.
- **Cell Range**: A1:CX14
- **Layout Structure**:
    - **Row Headers Location**: Column A and B
    - **Column Headers Location**: Row 1 and Row 3
    - **Data Range**:
      - Monthly data: `D4:CX4` (2019 Budget), `D9:CX9` (Adjustment), `D12:CX12` (Total Sales Bonus), `G13:CV13` (Quarterly Bonus Paid), `G14:CV14` (Quarterly Bonus Paid (Adj Kiva))
- **Time Series Details**:
    - **Date Range**: 2019-10-01 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: Department, Salary, 2019 Budget, 2020 Budget, Adjustment, Total Sales Bonus, Quarterly Bonus Paid, Quarterly Bonus Paid (Adj Kiva)
- **Notes & Customizations**: The budget data is scaled by 1000.

### Sales Team Bonus Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the bonus calculation for various sales team roles. It includes the count, total, and average bonus amounts for each role.
- **Cell Range**: A17:CX54
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 20 and Row 39
    - **Data Range**:
      - Monthly data: `F17:CX17` (AVERAGE BONUS ATTAINMENT), `F21:CX35` (Bonus Calculation by Role), `F40:CX54` (Bonus Calculation by Role)
- **Time Series Details**:
    - **Date Range**: 2019-12-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: AVERAGE BONUS ATTAINMENT, Count, Total, Avg, CRO, VP of Sales, Sales Manager, SDR Manager, SDR, CS Manager, AM - Corporate, AM - Financial, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy, TOTAL SALES BONUS
- **Notes & Customizations**: The bonus calculation data is scaled by 1000 for some rows. There are two date series, one starting in October 2019 and the other in December 2019.


====================================================================================================
# SHEET 63: Bonus Support (Sales Ops Only)
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Bonus Support (Sales Ops Only)
- **Key Sections Identified**:
    - Department Salary Budget (Annual)
    - Department Salary Adjustment (Annual)
    - Department Salary Budget (Annual - Repeated)
    - Sales Bonus Summary (Multiple Time Series)
    - Sales Bonus by Role (Monthly)

## 2. Detailed Section Analysis

### Section Name: Department Salary Budget (Annual)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the salary budget for each department across multiple years. It's used to track and manage departmental expenses.
- **Cell Range**: A1:R10
- **Layout Structure**:
    - **Row Headers Location**: Column A and B (Department, Salary)
    - **Column Headers Location**: Row 1 and 2 (Department, 2019 Budget, 2020 Budget)
    - **Data Range**:
      - Annual data: D4:R10
- **Time Series Details**:
    - **Date Range**: 2019 to 2020
    - **Frequency**: Annual
- **Key Components**: Department, Salary, 2019 Budget, 2020 Budget
- **Notes & Customizations**: Budgets are scaled by 1000.

### Section Name: Department Salary Adjustment (Annual)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the salary adjustments for each department across multiple years. It's used to track and manage changes to departmental expenses.
- **Cell Range**: A12:R20
- **Layout Structure**:
    - **Row Headers Location**: Column A and B (Adjustment, Department)
    - **Column Headers Location**: Row 12 (Adjustment)
    - **Data Range**:
      - Annual data: G13:R20
- **Time Series Details**:
    - **Date Range**: 2020
    - **Frequency**: Annual
- **Key Components**: Adjustment, Department
- **Notes & Customizations**: Adjustments are scaled by 1000.

### Section Name: Department Salary Budget (Annual - Repeated)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section, similar to the first, shows the salary budget for each department across multiple years. It's likely a repeated section for a different scenario or version.
- **Cell Range**: A24:R31
- **Layout Structure**:
    - **Row Headers Location**: Column A and B (Department, Salary)
    - **Column Headers Location**: Row 24 (Department)
    - **Data Range**:
      - Annual data: D25:R31
- **Time Series Details**:
    - **Date Range**: 2019 to 2020
    - **Frequency**: Annual
- **Key Components**: Department, Salary
- **Notes & Customizations**: Budgets are scaled by 1000.

### Section Name: Sales Bonus Summary (Multiple Time Series)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the sales bonus information, including total and quarterly bonuses. It provides an overview of bonus payouts.
- **Cell Range**: B34:CX40
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., Total Sales Bonus, Quarterly Sales Bonus, AVERAGE BONUS ATTAINMENT)
    - **Column Headers Location**: Row 1 (Monthly Dates), Row 2 (2019 Budget, 2020 Budget)
    - **Data Range**:
      - Annual data: G34:R34
      - Monthly data: D36:CX36, G37, J37, M37, P37, S37, V37, Y37, AB37, AE37, AH37, AK37, AN37, AQ37, AT37, AW37, AZ37, BC37, BF37, BI37, BL37, BO37, BR37, BU37, BX37, CA37, CD37, CG37, CJ37, CM37, CP37, CS37, CV37, F40:CX40
- **Time Series Details**:
    - **Date Range**:
        - Annual: 2020
        - Monthly: 2019-10-01 to 2027-12-31
    - **Frequency**:
        - Annual
        - Monthly
- **Key Components**: Total Sales Bonus, Quarterly Sales Bonus, AVERAGE BONUS ATTAINMENT
- **Notes & Customizations**: Budgets are scaled by 1000. Quarterly bonus values are sparsely populated across the monthly time series.

### Section Name: Sales Bonus by Role (Monthly)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down the sales bonus by role, showing the bonus amounts for each role over time. It allows for detailed analysis of bonus distribution.
- **Cell Range**: B43:CX75
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., CRO, Sales Manager, SDR Manager, SDR, CS Manager, AM - Corporate, AM - Financial, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy)
    - **Column Headers Location**: Row 43 (Count, Total, Avg), Row 61 (Monthly Dates)
    - **Data Range**:
      - Monthly data: F44:CX57, F62:CX75
- **Time Series Details**:
    - **Date Range**: 2019-12-31 to 2027-12-31
    - **Frequency**: Monthly
- **Key Components**: CRO, Sales Manager, SDR Manager, SDR, CS Manager, AM - Corporate, AM - Financial, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy
- **Notes & Customizations**: Budgets are scaled by 1000.



====================================================================================================
# SHEET 64: Headcount Adds
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Headcount Adds
- **Key Sections Identified**:
    - Header
    - Headcount Additions by Department
    - Headcount Counts by Category

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the column headers defining the data in the table.
- **Cell Range**: B2:V2
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B2:V2
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 2019-12-31 to 2020-12-31
    - **Frequency**: Monthly
- **Key Components**: Department, Type, Employee Name, Title, Office, Hire Date, Monthly Headcount Adds (Dec 2019 - Dec 2020)
- **Notes & Customizations**: Contains column labels for headcount data.

### Headcount Additions by Department
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows headcount additions by department, type, and title, along with associated data like office location and hire date. It also includes monthly headcount add numbers.
- **Cell Range**: B3:V72
- **Layout Structure**:
    - **Row Headers Location**: B3:E72
    - **Column Headers Location**: B2:V2
    - **Data Range**:
      - Monthly data: `J3:V72`
- **Time Series Details**:
    - **Date Range**: 2019-12-31 to 2020-12-31
    - **Frequency**: Monthly
- **Key Components**: Marketing, Product, Engineering (India), Finance & Admin, Salary, Bonus, Employee Name, Title, Office, Hire Date
- **Notes & Customizations**: Headcount data is scaled by 1000. Hire Date is also a date series, but appears to be unordered.

### Headcount Counts by Category
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows headcount counts by different categories.
- **Cell Range**: B75:V100
- **Layout Structure**:
    - **Row Headers Location**: B75:B100
    - **Column Headers Location**: J2:V2
    - **Data Range**:
      - Monthly data: `J76:V100`
- **Time Series Details**:
    - **Date Range**: 2019-12-31 to 2020-12-31
    - **Frequency**: Monthly
- **Key Components**: Counts, Content, Engineering (ex India), Executive, Marketing, Product, Engineering (India), Finance & Admin
- **Notes & Customizations**: Headcount data is scaled by 1000.


====================================================================================================
# SHEET 65: OpEx - Content
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Content
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title and date labels for the report.
- **Cell Range**: A2:U4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: C3:U3, D4:U4
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 03/31/2019 to Unknown (based on last date in the provided data)
    - **Frequency**: Monthly
- **Key Components**: Content, Month Ending, Year To Date, Dates
- **Notes & Customizations**: Contains the title of the report and the month-ending dates.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, including revenue, cost of sales, expenses, and profit.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: A5:A138
    - **Column Headers Location**: C3:U3, D4:U4
    - **Data Range**:
      - Monthly data: B7:U15, B20:M30, B37:U137, B138:U138
- **Time Series Details**:
    - **Date Range**: 03/31/2019 to Unknown (based on last date in the provided data)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses.
- **Notes & Customizations**: The report is scaled by 1000. There are multiple levels of subtotals for revenue, cost of sales, and expenses.


====================================================================================================
# SHEET 66: OpEx - Engineering
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Engineering
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title and time series context for the report.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: C3:U3
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on the last column U)
    - **Frequency**: Monthly
- **Key Components**: Engineering, Month Ending, Year To Date
- **Notes & Customizations**: The header provides the context for the entire sheet.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the financial performance of the Engineering department over a period of time. It includes revenue, cost of sales, gross profit, expenses, and other income/expenses to arrive at total expenses.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: A5:A138
    - **Column Headers Location**: C4:U4
    - **Data Range**: B7:U137
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on the last column U)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization, Other Income, Taxes, Interest Net, Other, Total Expenses.
- **Notes & Customizations**: The report is scaled by 1000. The time series is monthly, starting from 02/28/2019.



====================================================================================================
# SHEET 67: OpEx - Executive
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Executive
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period covered.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: Row 3
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on the last column)
    - **Frequency**: Monthly
- **Key Components**: "Executive", "Month Ending", "Year To Date"
- **Notes & Customizations**: This section is very brief and serves as a title and date range indicator for the report.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period, detailing revenue, cost of sales, expenses, and ultimately, profitability.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 4
    - **Data Range**: B7:U137
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on the last column)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, People Costs, Expenses, Depreciation & Amortization, Other Income, Taxes, Interest Net, Total Expenses.
- **Notes & Customizations**: The report is in thousands (scale = 1000). The "Month Ending" header in row 3 suggests that the columns represent monthly data.



====================================================================================================
# SHEET 68: OpEx - Finance & Admin
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Finance & Admin
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period covered.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B3:U3
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on the last date in the provided data)
    - **Frequency**: Monthly
- **Key Components**: "Finance & Admin", "Month Ending", "Year To Date"
- **Notes & Customizations**: This section provides context for the rest of the sheet.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the financial performance of the "Finance & Admin" department over a period of time, showing revenue, cost of sales, gross profit, expenses, and other income/expenses.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: Column A, rows 5 to 138
    - **Column Headers Location**: Row 4, columns C to U
    - **Data Range**: B7:U137
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on the last date in the provided data)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization, Other Income, Taxes, Interest Net, Other, Total Expenses
- **Notes & Customizations**: The data is scaled by 1000 (likely representing thousands of dollars). The "Subsidy Received" line item (A123:R123) only spans up to column R, while other line items extend to column U.


====================================================================================================
# SHEET 69: OpEx - Marketing
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Marketing
- **Key Sections Identified**:
    - Header
    - Income Statement (Marketing Department View)

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period label.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: B2:U3
- **Time Series Details**: None
- **Key Components**: "Marketing", "Month Ending", "Year To Date"
- **Notes & Customizations**: This section is a simple header for the report.

### Section Name: Income Statement (Marketing Department View)
- **Section Type**: Custom P&L
- **Description & Purpose**: This section presents a profit and loss statement specifically for the Marketing department, detailing revenue, cost of sales, expenses, and other financial metrics. It allows for tracking the financial performance of the marketing activities over time.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: Column A (A5:A138)
    - **Column Headers Location**: Row 4 (C4:U4) and Row 3 (B3:U3)
    - **Data Range**:
      - Monthly data: B7:U137
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (U4)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, People Costs, Travel Costs, Facility Costs, Marketing Expenses, General & Admin Expenses, Legal Costs, Depreciation & Amortization, Other Income, Taxes, Interest Net, Total Expenses.
- **Notes & Customizations**: The report is scaled by 1000. The report includes detailed breakdowns of revenue streams and expense categories relevant to the marketing department.


====================================================================================================
# SHEET 70: OpEx - Product
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Product
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the product name and month-ending labels, providing context for the data below.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B2:U2, C3:U3
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to 09/30/2019
    - **Frequency**: Monthly
- **Key Components**: Product, Month Ending
- **Notes & Customizations**: Includes "Year To Date" label.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the financial performance of the product, including revenue, cost of sales, expenses, and other income/expenses.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: B3:U3, C4:U4
    - **Data Range**: B7:U138
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to 09/30/2019
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, People Costs, Marketing, General & Admin, Legal Costs, Depreciation & Amortization, Other Income, Taxes, Interest Net, Total Expenses.
- **Notes & Customizations**: Numbers are scaled by 1000. Includes detailed breakdowns of revenue, cost of sales, and various expense categories.



====================================================================================================
# SHEET 71: OpEx - Sales
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Sales
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period covered.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: C3:U3
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on the last date provided)
    - **Frequency**: Monthly
- **Key Components**: Sales, Month Ending, Year To Date
- **Notes & Customizations**: The header provides context for the data presented below.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, detailing revenue, cost of sales, expenses, and ultimately, profit.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: C4:U4
    - **Data Range**:
      - Monthly data: B7:U137
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on the last date provided)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses
- **Notes & Customizations**: All monetary values are scaled by 1000. The report includes detailed breakdowns of various expense categories.


====================================================================================================
# SHEET 72: Historical Quota& Productivity
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Historical Quota& Productivity
- **Key Sections Identified**:
    - Historical Quota
    - Historical Productivity

## 2. Detailed Section Analysis

### Section Name: Historical Quota
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the historical quota for different account manager roles. It provides a view of the target revenue or sales expected from each role over time.
- **Cell Range**: B6:H12
- **Layout Structure**:
    - **Row Headers Location**: B7:B12
    - **Column Headers Location**: E5:H5
    - **Data Range**:
      - Annual data: F7:H12
- **Time Series Details**:
    - **Date Range**: 2016 to 2018
    - **Frequency**: Annual
- **Key Components**: Account Manager, AE - Financial, AE - Corporate, AE - Enterprise, AE - Other, VP Bus Dev
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Historical Productivity
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the historical productivity for different account manager roles. It provides a view of the actual revenue or sales achieved by each role over time.
- **Cell Range**: B15:BH23
- **Layout Structure**:
    - **Row Headers Location**: B16:B23
    - **Column Headers Location**: E5:BH5
    - **Data Range**:
      - Annual data: E16:G23
      - Monthly data: J16:BH23
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2016 to 2018
      - Monthly: 2015-01-31 to 2019-03-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: AE - Financial, AE - Corporate, AE - Enterprise, AE - Other, VP Bus Dev, Other, Total
- **Notes & Customizations**: Values are scaled by 1000. There are both annual and monthly time series data present.



====================================================================================================
# SHEET 73: Fixed Asset Depreciation
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Fixed Asset Depreciation
- **Key Sections Identified**:
    - Fixed Asset Depreciation - LTD
    - Fixed Asset Depreciation - Mgmt
    - Fixed Asset Depreciation - Inc

## 2. Detailed Section Analysis

### Section Name (Fixed Asset Depreciation - LTD)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the fixed asset depreciation schedule for LTD, showing the starting balance, conversion, starting balance in USD, and monthly depreciation expenses.
- **Cell Range**: B5:DV10
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., LTD, Oy, Total)
    - **Column Headers Location**: Row 3 (Account, Starting Balance, Conversion, Starting Balance (USD))
    - **Data Range**:
      - Monthly data: `G6:DV10` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**: The exact dates are not provided, but the data spans from column G to DV, implying a monthly time series. The number of months is dependent on the number of columns between G and DV.
    - **Frequency**: Monthly
- **Key Components**: LTD, Account, Starting Balance, Conversion, Starting Balance (USD), Oy, Total
- **Notes & Customizations**: Values in column F and from column G onwards are scaled by 1000.

### Section Name (Fixed Asset Depreciation - Mgmt)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the fixed asset depreciation schedule for Mgmt, showing the starting balance, conversion, starting balance in USD, and monthly depreciation expenses.
- **Cell Range**: B13:DV18
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., Mgmt, Oy, Total)
    - **Column Headers Location**: Row 3 (Account, Starting Balance, Conversion, Starting Balance (USD))
    - **Data Range**:
      - Monthly data: `H14:DV18` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**: The exact dates are not provided, but the data spans from column H to DV, implying a monthly time series. The number of months is dependent on the number of columns between H and DV.
    - **Frequency**: Monthly
- **Key Components**: Mgmt, Account, Starting Balance, Conversion, Starting Balance (USD), Oy, Total
- **Notes & Customizations**: Values from column G onwards are scaled by 1000.

### Section Name (Fixed Asset Depreciation - Inc)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the fixed asset depreciation schedule for Inc, showing the monthly depreciation expenses.
- **Cell Range**: B15:DV17
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., Inc, Oy)
    - **Column Headers Location**: Row 3 (Account, Starting Balance, Conversion, Starting Balance (USD))
    - **Data Range**:
      - Monthly data: `H15:DV17` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**: The exact dates are not provided, but the data spans from column H to DV, implying a monthly time series. The number of months is dependent on the number of columns between H and DV.
    - **Frequency**: Monthly
- **Key Components**: Inc, Account, Oy
- **Notes & Customizations**: Values from column G onwards are scaled by 1000.



====================================================================================================
# SHEET 74: COGS vs. Marginal
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: COGS vs. Marginal
- **Key Sections Identified**:
    - Revenue and Seats Summary
    - COGS and Gross Profit Analysis
    - Cost Calculations

## 2. Detailed Section Analysis

### Section Name: Revenue and Seats Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a summary of revenue and seats for 2017, along with the calculated revenue per seat. This provides a high-level overview of the company's performance.
- **Cell Range**: B4:D10
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 4
    - **Data Range**:
      - Current data: `C6:C10`
      - Marginal data: `D6:D10`
- **Time Series Details**:
    - **Date Range**: 2017
    - **Frequency**: Annual
- **Key Components**: 2017 Revenue, 2017 Seats, Revenue / Seat
- **Notes & Customizations**: Includes both "Current" and "Marginal" values for comparison.

### Section Name: COGS and Gross Profit Analysis
- **Section Type**: Standard P&L
- **Description & Purpose**: Analyzes the Cost of Goods Sold (COGS) and calculates the resulting Gross Profit per Seat and % Margin. This section provides insights into the profitability of each seat.
- **Cell Range**: B12:B35
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: `C12` and `D27:E33` (Note: Data is scattered, not a contiguous block)
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but implied to be current and marginal scenarios.
    - **Frequency**: Annual
- **Key Components**: COGS, Gross Profit per Seat, % Margin
- **Notes & Customizations**: The data range is not contiguous, indicating that some calculations might be performed elsewhere and referenced here.

### Section Name: Cost Calculations
- **Section Type**: Custom P&L
- **Description & Purpose**: This section details various cost components and calculations, including costs related to Broker Research, After Market Research, International Filings, Transcripts, News, IDC, and Web Services. It calculates the marginal price and considers various user tiers and associated fees.
- **Cell Range**: A41:D105
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: `D27, E27, D31, E31, D32, E32, E33, D50:D52, D54, D56, D66, D100, D105` (Note: Data is scattered, not a contiguous block)
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but implied to be current and marginal scenarios.
    - **Frequency**: Annual
- **Key Components**: Broker Research, After Market Research, International Filings, Transcripts, News, IDC, Web Service - Production, AMR - $15k, AMR - $30k, Cost per User, Marginal Price, Percent of Users, Price per User - Tier 1.
- **Notes & Customizations**: This section appears to be a collection of cost calculations related to various services and user tiers. The data range is highly scattered, suggesting that the calculations are complex and interconnected.


====================================================================================================
# SHEET 75: Benchmarking
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Benchmarking
- **Key Sections Identified**:
    - Revenue and Expense Benchmarking
    - Revenue Multiples

## 2. Detailed Section Analysis

### Section Name: Revenue and Expense Benchmarking
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section compares revenue, expenses, and profitability metrics across different companies (AlphaSense, Workday, Salesforce, ServiceNow, Splunk, Atlassian, Box, Tableau). It provides a basis for benchmarking performance against industry peers.
- **Cell Range**: C5:O26
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: D6:G26 (numeric values for years)
      - Peer data: I6:O26 (numeric values for peers)
- **Time Series Details**:
    - **Date Range**: Not explicitly stated, but implied to be current year and potentially prior years.
    - **Frequency**: Annual
- **Key Components**: Revenue, % Growth, COGS, % Margin, Sales and Marketing, G&A, R&D, EBITDA.
- **Notes & Customizations**: Values are scaled by 1000. "na" values appear in some cells, likely indicating "not available" data.

### Section Name: Revenue(1) and Growth
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section compares Revenue and Growth metrics across different companies (AlphaSense, Workday, Salesforce, ServiceNow, Splunk, Atlassian, Box, Tableau). It provides a basis for benchmarking performance against industry peers.
- **Cell Range**: A29:O43
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: D29:G43 (numeric values for years)
      - Peer data: I29:O43 (numeric values for peers)
- **Time Series Details**:
    - **Date Range**: Not explicitly stated, but implied to be current year and potentially prior years.
    - **Frequency**: Annual
- **Key Components**: Revenue(1), % LTM Growth, 2018E % Growth, Gross Profit, EBITDA.
- **Notes & Customizations**: Values are scaled by 1000. "na" values appear in some cells, likely indicating "not available" data.

### Section Name: 2017 Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section compares expense metrics across different companies (AlphaSense, Workday, Salesforce, ServiceNow, Splunk, Atlassian, Box, Tableau). It provides a basis for benchmarking performance against industry peers.
- **Cell Range**: C45:O63
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Peer data: D48:O63 (numeric values for peers)
- **Time Series Details**:
    - **Date Range**: Not explicitly stated, but implied to be 2017.
    - **Frequency**: Annual
- **Key Components**: COGS, Sales and Marketing, G&A, R&D.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Revenue Multiples
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates and compares revenue multiples (EV / Revenue, EV / Revenue / Growth) across different companies (AlphaSense, Workday, Salesforce, ServiceNow, Splunk, Atlassian, Box, Tableau). It provides a basis for valuation benchmarking.
- **Cell Range**: C65:O80
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Peer data: H68:O80 (numeric values for peers)
- **Time Series Details**:
    - **Date Range**: Not explicitly stated, but implied to be current year.
    - **Frequency**: Annual
- **Key Components**: EV / Revenue, EV / Revenue / Growth, Employees, Revenue per Employee.
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 76: Accrued Expenses
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Accrued Expenses
- **Key Sections Identified**:
    - Header Information
    - Audit Accrual Details
    - Data Feeds Expenses
    - Account 21000 (Oy) Expenses
    - Total Accrued Expenses

## 2. Detailed Section Analysis

### Header Information
- **Section Type**: Header
- **Description & Purpose**: Contains currency information and a label for Deloitte.
- **Cell Range**: C1:E4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: C1:AC4
- **Time Series Details**: None
- **Key Components**: Currency types (Euro, GBP), "Deloitte", "Monthly audit accrual"
- **Notes & Customizations**: Contains scaling factors for some values.

### Audit Accrual Details
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details of audit accruals for different years and regions.
- **Cell Range**: E7:AC12
- **Layout Structure**:
    - **Row Headers Location**: E7:E12
    - **Column Headers Location**: F1:AC1
    - **Data Range**:
      - Monthly data: `G7:AC12`
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2021-12-31
    - **Frequency**: Monthly
- **Key Components**: "UK", "2019 Audit accrual", "2020 Monthly audit accrual", "In USD"
- **Notes & Customizations**: Contains scaling factors for some values.

### Data Feeds Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Lists expenses related to various data feeds.
- **Cell Range**: B15:G32
- **Layout Structure**:
    - **Row Headers Location**: B15:B32
    - **Column Headers Location**: None
    - **Data Range**: E15:G32
- **Time Series Details**: None
- **Key Components**: "66100--DataFeeds", "LexisNexis", "AWS", "Factset Sell side research", "MSCI", "TR Transcripts"
- **Notes & Customizations**: Contains scaling factors for some values.

### Data Feeds Expenses (Continued)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Continues listing expenses related to various data feeds.
- **Cell Range**: B33:AC42
- **Layout Structure**:
    - **Row Headers Location**: B33:B42
    - **Column Headers Location**: F1:AC1
    - **Data Range**: F34:AC42
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2021-12-31
    - **Frequency**: Monthly
- **Key Components**: "TR Transcripts", "Six Financials", "Factset Sell side research"
- **Notes & Customizations**: Contains scaling factors for some values.

### Account 21000 (Oy) Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Expenses related to Account 21000 (Oy).
- **Cell Range**: B47:AC47
- **Layout Structure**:
    - **Row Headers Location**: B47
    - **Column Headers Location**: F1:AC1
    - **Data Range**: F47:AC47
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2021-12-31
    - **Frequency**: Monthly
- **Key Components**: "Account 21000 (Oy)", "In USD"
- **Notes & Customizations**: Contains scaling factors for some values.

### Total Accrued Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Total accrued expenses in USD.
- **Cell Range**: E49:F49
- **Layout Structure**:
    - **Row Headers Location**: E49
    - **Column Headers Location**: None
    - **Data Range**: F49
- **Time Series Details**: None
- **Key Components**: "Total Accrued Expenses (USD)"
- **Notes & Customizations**: Contains scaling factors for some values.


====================================================================================================
# SHEET 77: Prepaid Expenses
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Prepaid Expenses
- **Key Sections Identified**:
    - Vendor List
    - Prepaid Expenses Schedule
    - Prepaid Expenses Rollforward

## 2. Detailed Section Analysis

### Vendor List
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section lists the vendors for which prepaid expenses are tracked. It provides a reference for the expenses detailed in the following sections.
- **Cell Range**: B4:B65
- **Layout Structure**:
    - **Row Headers Location**: B4:B65
    - **Column Headers Location**: None
    - **Data Range**: B4:B65
- **Time Series Details**: None
- **Key Components**: List of vendors (e.g., Outreach Corporation, Salesforce.com Inc, HackerRank).
- **Notes & Customizations**: This is a static list of vendors, not a time series.

### Prepaid Expenses Schedule
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the prepaid expenses for each vendor over a monthly time series. It shows the amount of prepaid expense for each vendor for each month.
- **Cell Range**: A3:Z65
- **Layout Structure**:
    - **Row Headers Location**: B3:B65
    - **Column Headers Location**: C2:Z2
    - **Data Range**:
      - Monthly data: `D5:Z65`
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2021-12-31
    - **Frequency**: Monthly
- **Key Components**: Unit Price, Vendors, Amount, and monthly expenses for each vendor.
- **Notes & Customizations**: The amounts are scaled by 1000.

### Prepaid Expenses Rollforward
- **Section Type**: Custom P&L
- **Description & Purpose**: This section provides a rollforward of the total prepaid expenses, showing the opening balance, increases, decreases (Intacct Diff), and the resulting total prepaid balance. It also breaks down the total prepaids by currency.
- **Cell Range**: B67:Z81
- **Layout Structure**:
    - **Row Headers Location**: B67:B81
    - **Column Headers Location**: C2:Z2
    - **Data Range**:
      - Monthly data: `D67:Z81`
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2021-12-31
    - **Frequency**: Monthly
- **Key Components**: Opening balance, Inc Prepaids, Intacct Diff, Total Inc Prepaids, Total Mgmt Prepaids, Total India Prepaids, Total Oy Prepaids, Total Prepaids (USD).
- **Notes & Customizations**: Includes currency conversions for India and Oy prepaids. The amounts are scaled by 1000.


====================================================================================================
# SHEET 78: Accrued Wages
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Accrued Wages
- **Key Sections Identified**:
    - Accrued Wages Calculation

## 2. Detailed Section Analysis

### Section Name (Accrued Wages Calculation)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates accrued wages and related costs, including pension and insurance fees, and pre-payments. It provides a breakdown of these costs over time.
- **Cell Range**: A2:Z13
- **Layout Structure**:
    - **Row Headers Location**: B2:B13
    - **Column Headers Location**: C1:Z1
    - **Data Range**:
      - Monthly data: C2:Z13
- **Time Series Details**:
    - **Date Range**: 2020-01-31 to 2021-12-31
    - **Frequency**: Monthly
- **Key Components**: Acc. of pension insurance fees(accruals), Accrual of employer's statutory ins. pmt, Pension pre-payments, Unemployment pre-payment, Accident insurance pre-payment, Life insurance pre-payment, Calculated social costs, Pension held from workers, Unemployment held from workers, Total 21225 Accured finish side costs, USD
- **Notes & Customizations**: The values in the data range are scaled by 1000.


====================================================================================================
# SHEET 79: Cap R&D Exisiting Runoff
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Cap R&D Exisiting Runoff
- **Key Sections Identified**:
    - Monthly Data Section
    - Annual Data Section
    - Exchange Rate

## 2. Detailed Section Analysis

### Monthly Data Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains monthly data, likely related to R&D runoff. It provides a time series view of key metrics for analysis and forecasting.
- **Cell Range**: C3:BJ12
- **Layout Structure**:
    - **Row Headers Location**: A column (likely Column A, but not explicitly defined in the JSON) contains row labels.
    - **Column Headers Location**: Row 3 (C3:BJ3) contains monthly dates.
    - **Data Range**:
      - Monthly data: C11:BJ12
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2024-12-31
    - **Frequency**: Monthly
- **Key Components**: The specific metrics are not listed in the JSON, but the data is scaled by 1000.
- **Notes & Customizations**: The data is scaled by 1000.

### Annual Data Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains annual data, likely related to R&D runoff. It provides a time series view of key metrics for analysis and forecasting.
- **Cell Range**: G18:L19
- **Layout Structure**:
    - **Row Headers Location**: Column G contains row labels.
    - **Column Headers Location**: Row 18 (G18:L18) contains annual dates.
    - **Data Range**:
      - Annual data: G19:L19
- **Time Series Details**:
    - **Date Range**: 2015-01-01 to 2020-01-01 (interpreted as 2015 to 2020)
    - **Frequency**: Annual
- **Key Components**: The specific metrics are not listed in the JSON.
- **Notes & Customizations**: The data is annual.

### Exchange Rate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains the exchange rate for a specific date.
- **Cell Range**: A13:B13
- **Layout Structure**:
    - **Row Headers Location**: Cell A13 contains the row label.
    - **Column Headers Location**: None
    - **Data Range**:
      - Single value: B13
- **Time Series Details**:
    - **Date Range**: Not applicable, single point in time.
    - **Frequency**: Not applicable.
- **Key Components**: 1/31/20 Exchange Rate
- **Notes & Customizations**: This is a single value, not a time series.



====================================================================================================
# SHEET 80: Deposits
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Deposits
- **Key Sections Identified**:
    - Deposits Data

## 2. Detailed Section Analysis

### Section Name (Deposits Data)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the deposit data over a monthly time series, scaled by 1000. It allows for tracking and analysis of deposit trends.
- **Cell Range**: A3:Y3
- **Layout Structure**:
    - **Row Headers Location**: A3
    - **Column Headers Location**: B2:Y2
    - **Data Range**: B3:Y3
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2021-12-01
    - **Frequency**: Monthly
- **Key Components**: Deposits
- **Notes & Customizations**: The deposit values are scaled by 1000.


====================================================================================================
# SHEET 81: Tekes Loans
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Tekes Loans
- **Key Sections Identified**:
    - Loan 1: Tekes -14223, 114850 €
    - Loan 2: Tekes -14560, 337265,82 €
    - Loan 3: Tekes -14887, 343615 €
    - Loan 4: Tekes -15118, 186500 €
    - Loan 5: Tekes -15543, 159800 €
    - Accrued Interest Balance & FX Rate

## 2. Detailed Section Analysis

### Section Name: Loan 1: Tekes -14223, 114850 €
- **Section Type**: Loan Amortization Schedule
- **Description & Purpose**: Details the amortization schedule for a specific loan, showing principal and interest payments over time.
- **Cell Range**: B3:AZ8
- **Layout Structure**:
    - **Row Headers Location**: C3:C8 (e.g., "Opening Principal Balance", "Principal Payment", etc.)
    - **Column Headers Location**: D2:AZ2 (Dates)
    - **Data Range**:
      - Monthly data: D3:AZ8
- **Time Series Details**:
    - **Date Range**: 2019-12-01 to 2023-12-31
    - **Frequency**: Monthly
- **Key Components**: Opening Principal Balance, Principal Payment, Accrued Interest, Interest Payment, Principal Payment FX Rate.
- **Notes & Customizations**: Loan details are in cell B3.

### Section Name: Loan 2: Tekes -14560, 337265,82 €
- **Section Type**: Loan Amortization Schedule
- **Description & Purpose**: Details the amortization schedule for a specific loan, showing principal and interest payments over time.
- **Cell Range**: B13:AZ18
- **Layout Structure**:
    - **Row Headers Location**: C13:C18 (e.g., "Opening Principal Balance", "Principal Payment", etc.)
    - **Column Headers Location**: D2:AZ2 (Dates)
    - **Data Range**:
      - Monthly data: D13:AZ18
- **Time Series Details**:
    - **Date Range**: 2019-12-01 to 2023-12-31
    - **Frequency**: Monthly
- **Key Components**: Opening Principal Balance, Principal Payment, Accrued Interest, Interest Payment, Principal Payment FX Rate.
- **Notes & Customizations**: Loan details are in cell B13.

### Section Name: Loan 3: Tekes -14887, 343615 €
- **Section Type**: Loan Amortization Schedule
- **Description & Purpose**: Details the amortization schedule for a specific loan, showing principal and interest payments over time.
- **Cell Range**: B24:AZ29
- **Layout Structure**:
    - **Row Headers Location**: C24:C29 (e.g., "Opening Principal Balance", "Principal Payment", etc.)
    - **Column Headers Location**: D2:AZ2 (Dates)
    - **Data Range**:
      - Monthly data: D24:AZ29
- **Time Series Details**:
    - **Date Range**: 2019-12-01 to 2023-12-31
    - **Frequency**: Monthly
- **Key Components**: Opening Principal Balance, Principal Payment, Accrued Interest, Interest Payment, Principal Payment FX Rate.
- **Notes & Customizations**: Loan details are in cell B24.

### Section Name: Loan 4: Tekes -15118, 186500 €
- **Section Type**: Loan Amortization Schedule
- **Description & Purpose**: Details the amortization schedule for a specific loan, showing principal and interest payments over time.
- **Cell Range**: B37:AZ42
- **Layout Structure**:
    - **Row Headers Location**: C37:C42 (e.g., "Opening Principal Balance", "Principal Payment", etc.)
    - **Column Headers Location**: D2:AZ2 (Dates)
    - **Data Range**:
      - Monthly data: D37:AZ42
- **Time Series Details**:
    - **Date Range**: 2019-12-01 to 2023-12-31
    - **Frequency**: Monthly
- **Key Components**: Opening Principal Balance, Principal Payment, Accrued Interest, Interest Payment, Principal Payment FX Rate.
- **Notes & Customizations**: Loan details are in cell B37.

### Section Name: Loan 5: Tekes -15543, 159800 €
- **Section Type**: Loan Amortization Schedule
- **Description & Purpose**: Details the amortization schedule for a specific loan, showing principal and interest payments over time.
- **Cell Range**: B48:AZ53
- **Layout Structure**:
    - **Row Headers Location**: C48:C53 (e.g., "Opening Principal Balance", "Principal Payment", etc.)
    - **Column Headers Location**: D2:AZ2 (Dates)
    - **Data Range**:
      - Monthly data: D48:AZ53
- **Time Series Details**:
    - **Date Range**: 2019-12-01 to 2023-12-31
    - **Frequency**: Monthly
- **Key Components**: Opening Principal Balance, Principal Payment, Accrued Interest, Interest Payment, Principal Payment FX Rate.
- **Notes & Customizations**: Loan details are in cell B48.

### Section Name: Accrued Interest Balance & FX Rate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the accrued interest balance and FX rate over time.
- **Cell Range**: C57:AV59
- **Layout Structure**:
    - **Row Headers Location**: C57:C59 (e.g., "Accrued Interest Balance", "1/31/20 FX Rate")
    - **Column Headers Location**: D2:AZ2 (Dates)
    - **Data Range**:
      - Monthly data: E57:AV59
- **Time Series Details**:
    - **Date Range**: 2019-12-01 to 2023-12-31
    - **Frequency**: Monthly
- **Key Components**: Accrued Interest Balance, 1/31/20 FX Rate
- **Notes & Customizations**: The FX rate is labeled as "1/31/20 FX Rate", but the data spans the same monthly time series as the loan amortization schedules.

