# Master Workbook Analysis

This document provides a comprehensive analysis of all sheets in the Excel workbook.

---

## Table of Contents

1. [Summary](#summary)
   - [Changes Log](#summary-changes-log)
   - [Key Metrics - Monthly](#summary-key-metrics---monthly)
   - [Key Metrics - Annual](#summary-key-metrics---annual)
2. [Master Ctrl](#master-ctrl)
   - [Header](#master-ctrl-header)
   - [Control Panel](#master-ctrl-control-panel)
   - [Global Assumptions](#master-ctrl-global-assumptions)
   - [Productivity Case](#master-ctrl-productivity-case)
3. [Dash Control](#dash-control)
   - [Dashboard Title/Scenario Selection](#dash-control-dashboard-titlescenario-selection)
   - [Time Series Headers](#dash-control-time-series-headers)
   - [Key Metrics Table](#dash-control-key-metrics-table)
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
   - [Title/Header](#cac-by-segment-titleheader)
   - [CAC Summary](#cac-by-segment-cac-summary)
   - [CAC Detail by Segment](#cac-by-segment-cac-detail-by-segment)
   - [Adjusted Sales and Marketing Cost Analysis](#cac-by-segment-adjusted-sales-and-marketing-cost-analysis)
6. [Payback Period](#payback-period)
   - [Header](#payback-period-header)
   - [Payback Period - Total Company](#payback-period-payback-period---total-company)
   - [Cash Payback - Monthly Detail](#payback-period-cash-payback---monthly-detail)
   - [Payback Period - Financial](#payback-period-payback-period---financial)
   - [Payback Period - Corporate](#payback-period-payback-period---corporate)
   - [Cash Payback - Monthly Detail (Financial)](#payback-period-cash-payback---monthly-detail-financial)
   - [Cash Payback - Monthly Detail (Corporate)](#payback-period-cash-payback---monthly-detail-corporate)
7. [Fin CTRL](#fin-ctrl)
   - [Header](#fin-ctrl-header)
   - [Balance Sheet Support](#fin-ctrl-balance-sheet-support)
8. [Fin](#fin)
   - [Header](#fin-header)
   - [Income Statement](#fin-income-statement)
   - [Balance Sheet](#fin-balance-sheet)
   - [Cash Flow Statement](#fin-cash-flow-statement)
   - [Balance Sheet Support](#fin-balance-sheet-support)
   - [Long Term Liabilities](#fin-long-term-liabilities)
   - [Equity Investment](#fin-equity-investment)
   - [SVB Debt](#fin-svb-debt)
   - [Income Statement Support - Income Taxes](#fin-income-statement-support---income-taxes)
9. [Debt Compliance](#debt-compliance)
   - [Revenue Growth Analysis](#debt-compliance-revenue-growth-analysis)
   - [Liquidity Compliance Check](#debt-compliance-liquidity-compliance-check)
   - [Liquidity Buffer Analysis](#debt-compliance-liquidity-buffer-analysis)
10. [ARR and Rev CTRL](#arr-and-rev-ctrl)
   - [Header](#arr-and-rev-ctrl-header)
   - [Revenue & Quota Assumptions](#arr-and-rev-ctrl-revenue-&-quota-assumptions)
   - [Productivity - % of Quota](#arr-and-rev-ctrl-productivity---%-of-quota)
   - [Total ARR - % New Bookings](#arr-and-rev-ctrl-total-arr---%-new-bookings)
   - [Total ARR - % Upsell](#arr-and-rev-ctrl-total-arr---%-upsell)
   - [Productivity - Allocation](#arr-and-rev-ctrl-productivity---allocation)
   - [ARR Metrics](#arr-and-rev-ctrl-arr-metrics)
11. [Sales Prod Input](#sales-prod-input)
   - [Assumptions](#sales-prod-input-assumptions)
   - [Productivity by Role](#sales-prod-input-productivity-by-role)
   - [Productivity (Adjusted for Seasonality)](#sales-prod-input-productivity-adjusted-for-seasonality)
12. [ARR and Revenue](#arr-and-revenue)
   - [ARR and Revenue Summary](#arr-and-revenue-arr-and-revenue-summary)
   - [ARR by Segment](#arr-and-revenue-arr-by-segment)
   - [Revenue by Segment](#arr-and-revenue-revenue-by-segment)
   - [Revenue as % of MRR](#arr-and-revenue-revenue-as-%-of-mrr)
   - [Sales Productivity](#arr-and-revenue-sales-productivity)
   - [Total Bookings](#arr-and-revenue-total-bookings)
   - [New Bookings](#arr-and-revenue-new-bookings)
   - [Upsell](#arr-and-revenue-upsell)
   - [New Bookings - % of Total Bookings](#arr-and-revenue-new-bookings---%-of-total-bookings)
   - [Upsell - % of Total Bookings](#arr-and-revenue-upsell---%-of-total-bookings)
   - [Total Bookings by Segment](#arr-and-revenue-total-bookings-by-segment)
   - [New Bookings by Segment](#arr-and-revenue-new-bookings-by-segment)
   - [Upsell by Segment](#arr-and-revenue-upsell-by-segment)
   - [Financial ARR](#arr-and-revenue-financial-arr)
   - [Corporate ARR](#arr-and-revenue-corporate-arr)
   - [Other ARR](#arr-and-revenue-other-arr)
   - [Combined](#arr-and-revenue-combined)
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
   - [Other Sales - Salary](#sales-ctrl-other-sales---salary)
   - [Old Assumptions (To Be Deleted)](#sales-ctrl-old-assumptions-to-be-deleted)
   - [Product Specialist Headcount](#sales-ctrl-product-specialist-headcount)
   - [Product Specialist Manager Headcount](#sales-ctrl-product-specialist-manager-headcount)
   - [Sales - Admin Headcount](#sales-ctrl-sales---admin-headcount)
   - [Sales Manager Headcount](#sales-ctrl-sales-manager-headcount)
   - [Sales Operations Manager Headcount](#sales-ctrl-sales-operations-manager-headcount)
   - [Sales Recruiter Headcount](#sales-ctrl-sales-recruiter-headcount)
   - [SDR Headcount](#sales-ctrl-sdr-headcount)
14. [Sales Role Input](#sales-role-input)
   - [Section Name (Sales Role Headcount Input - Quota Roles)](#sales-role-input-section-name-sales-role-headcount-input---quota-roles)
   - [Section Name (Sales Role Headcount Input - Non-Quota Roles)](#sales-role-input-section-name-sales-role-headcount-input---non-quota-roles)
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
   - [Total Sales Salary](#sales-reps-total-sales-salary)
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
   - [Header](#retention-ctrl-header)
   - [Annual Retention - Financial](#retention-ctrl-annual-retention---financial)
   - [Evergreen Retention - Financial (Annual Equivalent)](#retention-ctrl-evergreen-retention---financial-annual-equivalent)
   - [Annual Retention - Corporate](#retention-ctrl-annual-retention---corporate)
   - [Annual Retention - Other](#retention-ctrl-annual-retention---other)
   - [Evergreen Retention - Other (Annual Equivalent)](#retention-ctrl-evergreen-retention---other-annual-equivalent)
19. [Retention](#retention)
   - [Header](#retention-header)
   - [Financial Retention Detail](#retention-financial-retention-detail)
   - [Corporate Retention Detail](#retention-corporate-retention-detail)
   - [Corporate Retention Detail](#retention-corporate-retention-detail)
   - [Other Retention Detail](#retention-other-retention-detail)
   - [Summary Retention Detail](#retention-summary-retention-detail)
20. [Renewed](#renewed)
   - [Header](#renewed-header)
   - [Renewal Data](#renewed-renewal-data)
21. [Renewal Base](#renewal-base)
   - [Header](#renewal-base-header)
   - [Renewal Data](#renewal-base-renewal-data)
22. [Deferred Build](#deferred-build)
   - [Header](#deferred-build-header)
   - [Deferred Revenue Summary](#deferred-build-deferred-revenue-summary)
   - [Deferred Revenue Detail](#deferred-build-deferred-revenue-detail)
   - [Revenue Recognition](#deferred-build-revenue-recognition)
23. [Headcount and Salaries CTRL](#headcount-and-salaries-ctrl)
   - [Headcount and Salaries Assumptions](#headcount-and-salaries-ctrl-headcount-and-salaries-assumptions)
   - [Salary Calculations](#headcount-and-salaries-ctrl-salary-calculations)
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
   - [Section Name (Operating Expenses Summary)](#operating-expenses-section-name-operating-expenses-summary)
   - [Section Name (Operating Expenses Detail)](#operating-expenses-section-name-operating-expenses-detail)
27. [Content](#content)
   - [Header](#content-header)
   - [Content Operating Expenses Summary](#content-content-operating-expenses-summary)
   - [Total Content People Costs](#content-total-content-people-costs)
   - [Total Content Other Employee Costs](#content-total-content-other-employee-costs)
   - [Total Content Travel Costs](#content-total-content-travel-costs)
   - [Total Content Facility Costs](#content-total-content-facility-costs)
   - [Total Content Marketing](#content-total-content-marketing)
   - [Total Content General & Admin](#content-total-content-general-&-admin)
   - [Total Content Other Costs](#content-total-content-other-costs)
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
   - [Section Name: Header](#executive-section-name-header)
   - [Section Name: Executive Operating Expenses Summary](#executive-section-name-executive-operating-expenses-summary)
   - [Section Name: Executive People Costs](#executive-section-name-executive-people-costs)
   - [Section Name: Executive Other Employee Costs](#executive-section-name-executive-other-employee-costs)
   - [Section Name: Executive Travel Costs](#executive-section-name-executive-travel-costs)
   - [Section Name: Executive Facility Costs](#executive-section-name-executive-facility-costs)
   - [Section Name: Executive Marketing](#executive-section-name-executive-marketing)
   - [Section Name: Executive General & Admin](#executive-section-name-executive-general-&-admin)
   - [Section Name: Executive Other Costs](#executive-section-name-executive-other-costs)
30. [Finance & Admin](#finance-&-admin)
   - [Header](#finance-&-admin-header)
   - [Finance & Admin Operating Expenses Summary](#finance-&-admin-finance-&-admin-operating-expenses-summary)
   - [Finance & Admin Employee Costs](#finance-&-admin-finance-&-admin-employee-costs)
   - [Finance & Admin Recruiting Fees](#finance-&-admin-finance-&-admin-recruiting-fees)
   - [Finance & Admin Relocation](#finance-&-admin-finance-&-admin-relocation)
   - [Finance & Admin Contractors](#finance-&-admin-finance-&-admin-contractors)
   - [Finance & Admin Outsourced R&D](#finance-&-admin-finance-&-admin-outsourced-r&d)
   - [Finance & Admin Capitalized R&D](#finance-&-admin-finance-&-admin-capitalized-r&d)
   - [Finance & Admin Other Employee Costs](#finance-&-admin-finance-&-admin-other-employee-costs)
   - [Finance & Admin Travel Costs](#finance-&-admin-finance-&-admin-travel-costs)
   - [Finance & Admin Facility Costs](#finance-&-admin-finance-&-admin-facility-costs)
   - [Finance & Admin Rental Income](#finance-&-admin-finance-&-admin-rental-income)
   - [Finance & Admin Marketing](#finance-&-admin-finance-&-admin-marketing)
   - [Finance & Admin General & Admin](#finance-&-admin-finance-&-admin-general-&-admin)
   - [Finance & Admin Other Costs](#finance-&-admin-finance-&-admin-other-costs)
   - [Bad Debt](#finance-&-admin-bad-debt)
31. [Marketing](#marketing)
   - [Header](#marketing-header)
   - [Marketing Operating Expenses Summary](#marketing-marketing-operating-expenses-summary)
   - [Marketing People Costs Breakdown](#marketing-marketing-people-costs-breakdown)
   - [Marketing Other Employee Costs Breakdown](#marketing-marketing-other-employee-costs-breakdown)
   - [Marketing Travel Costs Breakdown](#marketing-marketing-travel-costs-breakdown)
   - [Marketing Facility Costs Breakdown](#marketing-marketing-facility-costs-breakdown)
   - [Marketing Expenses Breakdown](#marketing-marketing-expenses-breakdown)
   - [Marketing General & Admin Breakdown](#marketing-marketing-general-&-admin-breakdown)
   - [Marketing Other Costs Breakdown](#marketing-marketing-other-costs-breakdown)
32. [Product](#product)
   - [Header](#product-header)
   - [Product Operating Expenses Summary](#product-product-operating-expenses-summary)
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
   - [Commissions Expense](#commission-waterfall-commissions-expense)
35. [Bad Debt](#bad-debt)
   - [Section Name (Reconciliation Header)](#bad-debt-section-name-reconciliation-header)
   - [Section Name (AFDA Reconciliation)](#bad-debt-section-name-afda-reconciliation)
36. [COGS CTRL](#cogs-ctrl)
   - [Header](#cogs-ctrl-header)
   - [User Percentage Metrics](#cogs-ctrl-user-percentage-metrics)
   - [Product Cost Assumptions](#cogs-ctrl-product-cost-assumptions)
   - [International Filings Expenses](#cogs-ctrl-international-filings-expenses)
   - [Transcripts Expenses](#cogs-ctrl-transcripts-expenses)
   - [Dow Jones Expenses](#cogs-ctrl-dow-jones-expenses)
   - [News & Journals Expenses](#cogs-ctrl-news-&-journals-expenses)
   - [IDC Expenses](#cogs-ctrl-idc-expenses)
   - [Web Service Expenses](#cogs-ctrl-web-service-expenses)
   - [Other Expenses](#cogs-ctrl-other-expenses)
   - [ASR Expenses](#cogs-ctrl-asr-expenses)
   - [Bernstein, Deutsche Bank, Barclays, HSBC, BOA, UBS, Morgan Stanley, Cowen, Autonomous, Evercore, Citi, Credit Suisse, JP Morgan, Raymond James, RBC Revenue Share and Minimums](#cogs-ctrl-bernstein-deutsche-bank-barclays-hsbc-boa-ubs-morgan-stanley-cowen-autonomous-evercore-citi-credit-suisse-jp-morgan-raymond-james-rbc-revenue-share-and-minimums)
   - [WSI FactSet Controls](#cogs-ctrl-wsi-factset-controls)
37. [Cost of Goods Sold](#cost-of-goods-sold)
   - [Cost of Goods Sold Summary](#cost-of-goods-sold-cost-of-goods-sold-summary)
   - [Product Summary](#cost-of-goods-sold-product-summary)
   - [Product Summary - % of Revenue](#cost-of-goods-sold-product-summary---%-of-revenue)
   - [Total User Count](#cost-of-goods-sold-total-user-count)
   - [Total User Net Adds](#cost-of-goods-sold-total-user-net-adds)
   - [Product Detail Net Adds - Live Users](#cost-of-goods-sold-product-detail-net-adds---live-users)
   - [Product Detail - Live Users](#cost-of-goods-sold-product-detail---live-users)
   - [TR Research - New Contract](#cost-of-goods-sold-tr-research---new-contract)
   - [Factset Research](#cost-of-goods-sold-factset-research)
   - [Dow Jones News Expense](#cost-of-goods-sold-dow-jones-news-expense)
   - [COGS by Segment](#cost-of-goods-sold-cogs-by-segment)
   - [COGS Allocation](#cost-of-goods-sold-cogs-allocation)
   - [P&L](#cost-of-goods-sold-p&l)
   - [BRM](#cost-of-goods-sold-brm)
   - [AMR](#cost-of-goods-sold-amr)
   - [International Filings Expense](#cost-of-goods-sold-international-filings-expense)
   - [Transcripts Expense](#cost-of-goods-sold-transcripts-expense)
   - [News & Journals Expense](#cost-of-goods-sold-news-&-journals-expense)
   - [Dow Jones News Expense](#cost-of-goods-sold-dow-jones-news-expense)
   - [IDC Expense](#cost-of-goods-sold-idc-expense)
   - [Web Service](#cost-of-goods-sold-web-service)
   - [Other Additional Data Sources](#cost-of-goods-sold-other-additional-data-sources)
   - [Factset Research (Upside Case)](#cost-of-goods-sold-factset-research-upside-case)
   - [Lexis Nexis](#cost-of-goods-sold-lexis-nexis)
   - [S&P Transcripts](#cost-of-goods-sold-s&p-transcripts)
38. [Total FDS Cost](#total-fds-cost)
   - [Section Name (Summary FDS COGS Expense (FDS Content))](#total-fds-cost-section-name-summary-fds-cogs-expense-fds-content)
   - [Section Name (FDS Excess Expense)](#total-fds-cost-section-name-fds-excess-expense)
   - [Section Name (Total FDS Spend & Minimum)](#total-fds-cost-section-name-total-fds-spend-&-minimum)
   - [Section Name (Pool Contribution & Carryover Balance)](#total-fds-cost-section-name-pool-contribution-&-carryover-balance)
   - [Section Name (Adjusted FDS COGS Expense)](#total-fds-cost-section-name-adjusted-fds-cogs-expense)
39. [FDS AMR](#fds-amr)
   - [Header](#fds-amr-header)
   - [User Statistics](#fds-amr-user-statistics)
   - [Documents Purchased Statistics](#fds-amr-documents-purchased-statistics)
   - [Cost Analysis](#fds-amr-cost-analysis)
40. [Direct Broker](#direct-broker)
   - [Section Name: Overview Metrics](#direct-broker-section-name-overview-metrics)
   - [Section Name: Reads Consumption by Broker](#direct-broker-section-name-reads-consumption-by-broker)
   - [Section Name: WSI Broker Expense Detail](#direct-broker-section-name-wsi-broker-expense-detail)
41. [Additional FDS Content](#additional-fds-content)
   - [FDS RT Expense - User Tier Analysis](#additional-fds-content-fds-rt-expense---user-tier-analysis)
   - [FDS RT Excess Expense Calculation](#additional-fds-content-fds-rt-excess-expense-calculation)
   - [FDS Transcripts - User Tier Analysis](#additional-fds-content-fds-transcripts---user-tier-analysis)
   - [FDS M&A - User Tier Analysis](#additional-fds-content-fds-m&a---user-tier-analysis)
42. [FDS User Growth](#fds-user-growth)
   - [User Summary](#fds-user-growth-user-summary)
   - [New WSI Users Additions](#fds-user-growth-new-wsi-users-additions)
   - [Non-WSI Corporate Users Converted](#fds-user-growth-non-wsi-corporate-users-converted)
   - [Non-WSI Users Converted](#fds-user-growth-non-wsi-users-converted)
   - [Percent of New Non-WSI Users Added by Sector](#fds-user-growth-percent-of-new-non-wsi-users-added-by-sector)
   - [Non-WSI Users Added](#fds-user-growth-non-wsi-users-added)
   - [Non-WSI Net User Change](#fds-user-growth-non-wsi-net-user-change)
   - [Non-WSI Users by Sector](#fds-user-growth-non-wsi-users-by-sector)
   - [WSI User Additions](#fds-user-growth-wsi-user-additions)
   - [Total Users](#fds-user-growth-total-users)
   - [Total Enabled Users](#fds-user-growth-total-enabled-users)
   - [Document Consumption](#fds-user-growth-document-consumption)
   - [FDS RT Users Detail](#fds-user-growth-fds-rt-users-detail)
43. [FDS RT Minimums](#fds-rt-minimums)
   - [Section Name (User Tier Pricing Table)](#fds-rt-minimums-section-name-user-tier-pricing-table)
44. [Product User Splits](#product-user-splits)
   - [Product User Data (Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR ($15k), AMR ($30k), AMR)](#product-user-splits-product-user-data-lexis-nexis-dj-factset-transcripts-tr-transcripts-transcripts-tr-filings-tr-brm-amr-$15k-amr-$30k-amr)
   - [BRM Data (BRM - Global, BRM - Single)](#product-user-splits-brm-data-brm---global-brm---single)
   - [FactSet RT Data](#product-user-splits-factset-rt-data)
   - [FactSet AMR Data](#product-user-splits-factset-amr-data)
   - [FactSet AMR / Active Data](#product-user-splits-factset-amr--active-data)
   - [FactSet AMR / Trailers Data](#product-user-splits-factset-amr--trailers-data)
   - [FactSet AMR / Internal Data](#product-user-splits-factset-amr--internal-data)
   - [FactSet AMR Active Docs Purchased Data](#product-user-splits-factset-amr-active-docs-purchased-data)
   - [FactSet AMR Trialer Docs Purchased Data](#product-user-splits-factset-amr-trialer-docs-purchased-data)
   - [FactSet AMR Internal Docs Purchased Data](#product-user-splits-factset-amr-internal-docs-purchased-data)
45. [TR BRM](#tr-brm)
   - [Section Name: Tiered Pricing for Financials](#tr-brm-section-name-tiered-pricing-for-financials)
   - [Section Name: Tiered Pricing for Corporate](#tr-brm-section-name-tiered-pricing-for-corporate)
   - [Section Name: Tiered Pricing for Other](#tr-brm-section-name-tiered-pricing-for-other)
   - [Section Name: User Count Summary](#tr-brm-section-name-user-count-summary)
46. [AMR](#amr)
   - [Monthly Data Table](#amr-monthly-data-table)
   - [Cost Breakdown Table](#amr-cost-breakdown-table)
47. [LN](#ln)
   - [Header](#ln-header)
   - [Financial Data Section](#ln-financial-data-section)
48. [DJ](#dj)
   - [Section Name (Revenue Breakdown)](#dj-section-name-revenue-breakdown)
49. [TR Transcripts](#tr-transcripts)
   - [Header](#tr-transcripts-header)
   - [Corporate Financial Data](#tr-transcripts-corporate-financial-data)
   - [Corporate Financial Data (Monthly)](#tr-transcripts-corporate-financial-data-monthly)
50. [FS Transcripts](#fs-transcripts)
   - [Quarterly Data Section](#fs-transcripts-quarterly-data-section)
   - [Monthly Data Section](#fs-transcripts-monthly-data-section)
51. [Filings](#filings)
   - [Header](#filings-header)
   - [Revenue by Segment](#filings-revenue-by-segment)
52. [Detailed Income Statement](#detailed-income-statement)
   - [Header](#detailed-income-statement-header)
   - [Revenue Section](#detailed-income-statement-revenue-section)
   - [Cost of Service (COS) Section](#detailed-income-statement-cost-of-service-cos-section)
   - [Expenses Section](#detailed-income-statement-expenses-section)
   - [Depreciation & Amortization Section](#detailed-income-statement-depreciation-&-amortization-section)
   - [Other Income Section](#detailed-income-statement-other-income-section)
   - [Taxes Section](#detailed-income-statement-taxes-section)
   - [Interest Section](#detailed-income-statement-interest-section)
   - [Other Section](#detailed-income-statement-other-section)
   - [Net Income Section](#detailed-income-statement-net-income-section)
   - [Personnel Cost Breakdown](#detailed-income-statement-personnel-cost-breakdown)
53. [Detailed Balance Sheet](#detailed-balance-sheet)
   - [Section Name: Header](#detailed-balance-sheet-section-name-header)
   - [Section Name: Assets](#detailed-balance-sheet-section-name-assets)
   - [Section Name: Liabilities](#detailed-balance-sheet-section-name-liabilities)
   - [Section Name: Equity](#detailed-balance-sheet-section-name-equity)
   - [Section Name: Liabilities & Equity Total & Check](#detailed-balance-sheet-section-name-liabilities-&-equity-total-&-check)
54. [Detailed Cash Flow Satement](#detailed-cash-flow-satement)
   - [Section Name (Cash Flow Statement - Operating Activities)](#detailed-cash-flow-satement-section-name-cash-flow-statement---operating-activities)
   - [Section Name (Cash Flow Statement - Investing Activities)](#detailed-cash-flow-satement-section-name-cash-flow-statement---investing-activities)
   - [Section Name (Cash Flow Statement - Financing Activities)](#detailed-cash-flow-satement-section-name-cash-flow-statement---financing-activities)
   - [Section Name (Cash Flow Statement - Reconciliation)](#detailed-cash-flow-satement-section-name-cash-flow-statement---reconciliation)
55. [Key Metrics](#key-metrics)
   - [Section Name (Annual Subscription Value)](#key-metrics-section-name-annual-subscription-value)
   - [Section Name (ARR Added (Gross))](#key-metrics-section-name-arr-added-gross)
   - [Section Name (ARR Churn)](#key-metrics-section-name-arr-churn)
   - [Section Name (ARR Churn Notifications)](#key-metrics-section-name-arr-churn-notifications)
   - [Section Name (# of Client Firms)](#key-metrics-section-name-#-of-client-firms)
   - [Section Name (# of Users)](#key-metrics-section-name-#-of-users)
   - [Section Name (Cash & Debt)](#key-metrics-section-name-cash-&-debt)
   - [Section Name (SaaS Metrics)](#key-metrics-section-name-saas-metrics)
   - [Section Name (Contract Duration)](#key-metrics-section-name-contract-duration)
   - [Section Name (Deal Metrics)](#key-metrics-section-name-deal-metrics)
   - [Section Name (Client Counts)](#key-metrics-section-name-client-counts)
   - [Section Name (User Counts)](#key-metrics-section-name-user-counts)
   - [Section Name (Cancels)](#key-metrics-section-name-cancels)
   - [Section Name (ARR New/Upsell/Increase $)](#key-metrics-section-name-arr-newupsellincrease-$)
   - [Section Name (Monthly Recurring Revenue)](#key-metrics-section-name-monthly-recurring-revenue)
56. [Revenue by Client](#revenue-by-client)
   - [Section Name (Revenue by Client (Annual))](#revenue-by-client-section-name-revenue-by-client-annual)
   - [Section Name (Revenue by Client (Monthly))](#revenue-by-client-section-name-revenue-by-client-monthly)
   - [Section Name (Income Statement (Annual))](#revenue-by-client-section-name-income-statement-annual)
57. [Client Support](#client-support)
   - [Section Name: Client ARR Movement - Type 1](#client-support-section-name-client-arr-movement---type-1)
   - [Section Name: Client ARR Movement - Type 2](#client-support-section-name-client-arr-movement---type-2)
   - [Section Name: Client ARR Movement - Type 3](#client-support-section-name-client-arr-movement---type-3)
   - [Section Name: Churned CARR](#client-support-section-name-churned-carr)
58. [Subscriber Support](#subscriber-support)
   - [Section Name: Subscriber Counts by Type](#subscriber-support-section-name-subscriber-counts-by-type)
   - [Section Name: Expense Allocation](#subscriber-support-section-name-expense-allocation)
59. [Headcount Support](#headcount-support)
   - [Section Name: Department Headcount (Original)](#headcount-support-section-name-department-headcount-original)
   - [Section Name: Department Headcount (New)](#headcount-support-section-name-department-headcount-new)
   - [Section Name: Sales Team Headcount](#headcount-support-section-name-sales-team-headcount)
   - [Section Name: Customer Success, Operations, Business Development Headcount](#headcount-support-section-name-customer-success-operations-business-development-headcount)
60. [Salary Support](#salary-support)
   - [Section Name: Department Salary Breakdown (Departments)](#salary-support-section-name-department-salary-breakdown-departments)
   - [Section Name: Department Salary Breakdown (Job Titles)](#salary-support-section-name-department-salary-breakdown-job-titles)
   - [Section Name: Department Salary Breakdown (Detailed Job Titles)](#salary-support-section-name-department-salary-breakdown-detailed-job-titles)
   - [Section Name: FX Rate](#salary-support-section-name-fx-rate)
   - [Section Name: Quota Based Sales Reps](#salary-support-section-name-quota-based-sales-reps)
   - [Section Name: Sales Team & Customer Success](#salary-support-section-name-sales-team-&-customer-success)
61. [Bonus Support](#bonus-support)
   - [Section Name: Department Salary Budget (2019 & 2020)](#bonus-support-section-name-department-salary-budget-2019-&-2020)
   - [Section Name: Department Adjustment](#bonus-support-section-name-department-adjustment)
   - [Section Name: Department Salary Budget (2019 & 2020) - Adjusted](#bonus-support-section-name-department-salary-budget-2019-&-2020---adjusted)
   - [Section Name: Sales Bonus Summary](#bonus-support-section-name-sales-bonus-summary)
   - [Section Name: Sales Bonus Detail](#bonus-support-section-name-sales-bonus-detail)
62. [Bonus Support (Sales Ops Only)](#bonus-support-(sales-ops-only))
   - [Section Name: Department Salary and Adjustment Budget](#bonus-support-(sales-ops-only)-section-name-department-salary-and-adjustment-budget)
   - [Section Name: Sales Bonus Calculation](#bonus-support-(sales-ops-only)-section-name-sales-bonus-calculation)
   - [Section Name: Sales Bonus by Role](#bonus-support-(sales-ops-only)-section-name-sales-bonus-by-role)
63. [OpEx - Content](#opex---content)
   - [Section Name: Header](#opex---content-section-name-header)
   - [Section Name: Income Statement](#opex---content-section-name-income-statement)
64. [OpEx - Engineering](#opex---engineering)
   - [Header](#opex---engineering-header)
   - [Income Statement](#opex---engineering-income-statement)
65. [OpEx - Executive](#opex---executive)
   - [Section Name: Header](#opex---executive-section-name-header)
   - [Section Name: Income Statement](#opex---executive-section-name-income-statement)
66. [OpEx - Finance & Admin](#opex---finance-&-admin)
   - [Section Name: Header](#opex---finance-&-admin-section-name-header)
   - [Section Name: Income Statement](#opex---finance-&-admin-section-name-income-statement)
67. [OpEx - Marketing](#opex---marketing)
   - [Header](#opex---marketing-header)
   - [Income Statement](#opex---marketing-income-statement)
68. [OpEx - Product](#opex---product)
   - [Header](#opex---product-header)
   - [Income Statement](#opex---product-income-statement)
69. [OpEx - Sales](#opex---sales)
   - [Header](#opex---sales-header)
   - [Income Statement](#opex---sales-income-statement)
70. [Historical Quota& Productivity](#historical-quota&-productivity)
   - [Section Name (Historical Quota)](#historical-quota&-productivity-section-name-historical-quota)
   - [Section Name (Historical Productivity)](#historical-quota&-productivity-section-name-historical-productivity)
71. [Fixed Asset Depreciation](#fixed-asset-depreciation)
   - [Header](#fixed-asset-depreciation-header)
   - [Fixed Asset Depreciation Schedule](#fixed-asset-depreciation-fixed-asset-depreciation-schedule)
72. [COGS vs. Marginal](#cogs-vs.-marginal)
   - [Section Name: Revenue and Seats Calculation](#cogs-vs.-marginal-section-name-revenue-and-seats-calculation)
   - [Section Name: COGS Analysis](#cogs-vs.-marginal-section-name-cogs-analysis)
   - [Section Name: Marginal Cost Analysis](#cogs-vs.-marginal-section-name-marginal-cost-analysis)
73. [Accrued Wages](#accrued-wages)
   - [Section Name (e.g., "Accrued Wages Data")](#accrued-wages-section-name-eg-"accrued-wages-data")
74. [Deposits](#deposits)
   - [Section Name (Deposits Data)](#deposits-section-name-deposits-data)

---


====================================================================================================
# SHEET 1: Summary
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Summary
- **Key Sections Identified**:
    - Changes Log
    - Key Metrics - Monthly
    - Key Metrics - Annual

## 2. Detailed Section Analysis

### Changes Log
- **Section Type**: Documentation/Notes
- **Description & Purpose**: Documents changes made to the underlying model or data. Useful for understanding the evolution of the forecast.
- **Cell Range**: B2:B6
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B6
- **Time Series Details**: None
- **Key Components**: Change descriptions.
- **Notes & Customizations**: Free-form text.

### Key Metrics - Monthly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents key performance indicators (KPIs) and financial metrics on a monthly basis. Allows for tracking trends and performance over time.
- **Cell Range**: C40:BW53
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 40
    - **Data Range**:
      - Monthly data: `D41:BW42` (Cash, Debt)
      - Monthly data: `D44:BK46` (ARR, Bookings, ARR TTM Growth)
      - Monthly data: `D48:BK53` (Margin, EBITDA, FCF, Reps, Eff Reps)
- **Time Series Details**:
    - **Date Range**: 2018-01-31 to 2023-12-31 (D40:BW40). Anchor points: D40=2018-01-31, P40=2019-01-31, AB40=2020-01-31, AN40=2021-01-31, AZ40=2022-01-31, BL40=2023-01-31
    - **Date Range**: 2018-01-31 to 2022-12-31 (D43:BK43, D47:BK47, D49:BK49). Anchor points: D43=2018-01-31, P43=2019-01-31, AB43=2020-01-31, AN43=2021-01-31, AZ43=2022-01-31
    - **Frequency**: Monthly
- **Key Components**: Cash, Debt, ARR, Bookings, ARR TTM Growth, Margin, EBITDA, FCF, Reps, Eff Reps.
- **Notes & Customizations**: Values are scaled by 1000 in some rows.

### Key Metrics - Annual
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents key performance indicators (KPIs) and financial metrics on an annual basis. Provides a summary view of the company's performance over the years.
- **Cell Range**: C57:H66
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 57
    - **Data Range**: D58:H62, D64:H66
- **Time Series Details**:
    - **Date Range**: 2018 to 2022 (D57:H57)
    - **Frequency**: Annual
- **Key Components**: ARR, FCF, Avg FCF, Cash, Debt, Growth Rate, Avg Eff Reps, Bookings, Avg Bkgs.
- **Notes & Customizations**: Values are scaled by 1000 in some rows.



====================================================================================================
# SHEET 2: Master Ctrl
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Master Ctrl
- **Key Sections Identified**:
    - Header
    - Control Panel
    - Productivity Case

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and the name of the spreadsheet.
- **Cell Range**: B2:B3
- **Layout Structure**:
    - **Row Headers Location**: B2:B3
    - **Column Headers Location**: N/A
    - **Data Range**: B2:B3
- **Time Series Details**: N/A
- **Key Components**: AlphaSense, Inc., Master CTRL
- **Notes & Customizations**: Standard header information.

### Control Panel
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains key input assumptions and control variables for the model.
- **Cell Range**: A12:C18
- **Layout Structure**:
    - **Row Headers Location**: B14:B18
    - **Column Headers Location**: C12
    - **Data Range**: C14:C18
- **Time Series Details**: N/A
- **Key Components**: Master Case, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Contains different scenarios for the model.

### Global Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains global assumptions for the model, such as the latest actual month and months left in the year.
- **Cell Range**: A20:E25
- **Layout Structure**:
    - **Row Headers Location**: B22, B25
    - **Column Headers Location**: N/A
    - **Data Range**: E25
- **Time Series Details**: N/A
- **Key Components**: Latest Actual Month, Months Left in Year
- **Notes & Customizations**: Contains global assumptions for the model.

### Productivity Case
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains productivity case assumptions for the model.
- **Cell Range**: B27:C33
- **Layout Structure**:
    - **Row Headers Location**: B28, B29, B32, B33
    - **Column Headers Location**: N/A
    - **Data Range**: C28, C29, C32, C33
- **Time Series Details**: N/A
- **Key Components**: Base, Target
- **Notes & Customizations**: Contains different scenarios for the model.


====================================================================================================
# SHEET 3: Dash Control
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Dash Control
- **Key Sections Identified**:
    - Dashboard Title/Scenario Selection
    - Time Series Headers
    - Key Metrics Table

## 2. Detailed Section Analysis

### Dashboard Title/Scenario Selection
- **Section Type**: `Dashboard Configuration`
- **Description & Purpose**: This section contains the title of the dashboard and allows the user to select different scenarios. It's used to configure the dashboard's display.
- **Cell Range**: `B2:B4`
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: `B2:B4`
- **Time Series Details**: None
- **Key Components**: "AlphaSense, Inc.", "Dashboard CTRL", "1 - Base - $25mm"
- **Notes & Customizations**: This section is used to set the context for the rest of the dashboard.

### Time Series Headers
- **Section Type**: `Time Series Header`
- **Description & Purpose**: This section defines the time periods for the data displayed in the dashboard. It includes both annual and monthly time series.
- **Cell Range**: `B7:FS9`
- **Layout Structure**:
    - **Row Headers Location**: B7:B8
    - **Column Headers Location**: E7:Q7 (Year), T7:FS7 (Year), T8:FS8 (Month)
    - **Data Range**:
      - Annual data: `E7:Q7` (years)
      - Monthly data: `T7:FS7` (years), `T8:FS8` (months), `T9:FS9` (dates)
- **Time Series Details**:
    - **Annual**: 2015 to 2027 (E7:Q7)
        - **Frequency**: `Annual`
    - **Repeating Annual**: 2015 to 2027 (T7:FS7). Anchor points: T7=2015-01-01, AF7=2016-01-01, AR7=2017-01-01, BD7=2018-01-01, BP7=2019-01-01, CB7=2020-01-01, CN7=2021-01-01, CZ7=2022-01-01, DL7=2023-01-01, DX7=2024-01-01, EJ7=2025-01-01, EV7=2026-01-01, FH7=2027-01-01
        - **Frequency**: `Annual` (repeating)
    - **Monthly**: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
        - **Frequency**: `Monthly`
- **Key Components**: "Year", "Month", Years (2015-2027), Months (Jan-Dec)
- **Notes & Customizations**: Contains both annual and monthly time series data. The annual data in T7:FS7 is repeating.

### Key Metrics Table
- **Section Type**: `Key Metrics Table`
- **Description & Purpose**: This section displays key performance indicators (KPIs) and financial metrics for different scenarios. It includes metrics like "Support Fees - % of CAC", "ARR Multipler", and "Perpetuity Factor", across various base scenarios.
- **Cell Range**: `A12:FS66`
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., B14, B20, B27, B34, B41, B48, B55, B62)
    - **Column Headers Location**: E7:Q7 (Year), T7:FS7 (Year), T8:FS8 (Month)
    - **Data Range**:
      - Annual data: `J14:Q66` (with gaps)
      - Monthly data: `T14:FS66` (with gaps)
- **Time Series Details**:
    - **Annual**: 2015 to 2027 (E7:Q7)
        - **Frequency**: `Annual`
    - **Repeating Annual**: 2015 to 2027 (T7:FS7). Anchor points: T7=2015-01-01, AF7=2016-01-01, AR7=2017-01-01, BD7=2018-01-01, BP7=2019-01-01, CB7=2020-01-01, CN7=2021-01-01, CZ7=2022-01-01, DL7=2023-01-01, DX7=2024-01-01, EJ7=2025-01-01, EV7=2026-01-01, FH7=2027-01-01
        - **Frequency**: `Annual` (repeating)
    - **Monthly**: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
        - **Frequency**: `Monthly`
- **Key Components**: "Support Fees - % of CAC", "ARR Multipler ", "Perpetuity Factor", "ARR Multipler  - Financial", "Perpetuity Factor - Financial", "ARR Multipler - Corporate", "Perpetuity Factor - Corporate", "% Travel Costs", "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: The data is scaled by 1000. The table contains multiple scenarios (Base, Growth) and different calculation methods (Financial, Corporate).


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
- **Description & Purpose**: Presents the company's Income Statement, including Revenue, Cost of Sales, Gross Profit, Operating Expenses, and EBITDA. Used to assess profitability.
- **Cell Range**: A6:FS25
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E8:Q23
      - Monthly data: T8:FS23
- **Time Series Details**:
    - Annual: E3:I3, J3:Q3. Range is not specified, but based on data, it's likely 2011-2023.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Operating Expenses, EBITDA, Free Cashflow (FCF)
- **Notes & Customizations**: Includes a "Memo" line for Free Cashflow. Values are scaled by 1000.

### ARR Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the company's Annual Recurring Revenue (ARR) at the beginning and end of the period.
- **Cell Range**: A27:FS31
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E29:Q30
      - Monthly data: T29:FS30
- **Time Series Details**:
    - Annual: E3:I3, J3:Q3. Range is not specified, but based on data, it's likely 2011-2023.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Beginning ARR, Ending ARR
- **Notes & Customizations**: Values are scaled by 1000.

### Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the company's Bookings, broken down by Financial, Corporate, and Other categories.
- **Cell Range**: B33:FS52
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E34:Q51
      - Monthly data: T34:FS51
- **Time Series Details**:
    - Annual: E3:I3, J3:Q3. Range is not specified, but based on data, it's likely 2011-2023.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Financial Bookings, Corporate Bookings, Other Bookings, Total Bookings, New Bookings, Total New Bookings, Upsell, Total Upsell
- **Notes & Customizations**: Values are scaled by 1000.

### Segment Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes ARR by Segment.
- **Cell Range**: A54:FS71
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E59:Q70
      - Monthly data: T59:FS70
- **Time Series Details**:
    - Annual: E3:I3, J3:Q3. Range is not specified, but based on data, it's likely 2011-2023.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Beginning ARR, Ending ARR
- **Notes & Customizations**: Values are scaled by 1000.

### Headcount Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the company's Headcount by department.
- **Cell Range**: A111:FS127
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E114:Q127
      - Monthly data: T114:FS127
- **Time Series Details**:
    - Annual: E3:I3, J3:Q3. Range is not specified, but based on data, it's likely 2011-2023.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Executive, Engineering, Product, Sales, Marketing, Content, Finance, HR, and Operations, Total Headcount, Avg Effective Quota Carrying Sales Reps, New ARR per Sales Rep, New Clients per Sales Rep.
- **Notes & Customizations**: Values are scaled by 1000. Includes a "Memo" line for India Employees.

### Client & Subscriber Counts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the company's Client and Subscriber counts.
- **Cell Range**: A129:FS175
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E133:Q175
      - Monthly data: T133:FS175
- **Time Series Details**:
    - Annual: E3:I3, J3:Q3. Range is not specified, but based on data, it's likely 2011-2023.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Clients (End of Period), Users (End of Period), Clients, Beginning of Period, Added, Churned, Clients, End of Period, ARR Per Client
- **Notes & Customizations**: Values are scaled by 1000.

### Retention Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the company's Retention Metrics.
- **Cell Range**: A192:FS206
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E194:Q206
      - Monthly data: T194:FS206
- **Time Series Details**:
    - Annual: E3:I3, J3:Q3. Range is not specified, but based on data, it's likely 2011-2023.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Upsells, Up for Renewal, Renewed, Churn, Ann. Net Dollar Retention, Ann. Gross Dollar Retention, Ann. Cohort Retention, Ann. Net Dollar Retention - TTM, Ann. Gross Dollar Retention - TTM, Ann. Cohort Retention - TTM
- **Notes & Customizations**: Values are scaled by 1000 for some metrics.

### Key Performance Indicators Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes Key Performance Indicators.
- **Cell Range**: A208:FS213
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E211:Q213
      - Monthly data: AR211:FS213 (Note: Data starts at AR, not T)
- **Time Series Details**:
    - Annual: E3:I3, J3:Q3. Range is not specified, but based on data, it's likely 2011-2023.
    - Monthly: 2017-01-31 to 2027-12-31 (AR3:FS3). Anchor points: AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: LTV / CAC
- **Notes & Customizations**: Values are scaled by 1000.

### Key Performance Indicators Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details Key Performance Indicators.
- **Cell Range**: A215:FS263
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: E217:Q263
      - Monthly data: T217:FS263
- **Time Series Details**:
    - Annual: E3:I3, J3:Q3. Range is not specified, but based on data, it's likely 2011-2023.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Margin (end of Period), Avg Quota Carrying Salee Reps, Bookings per Sales Rep, ARR per Sales Rep, Avg. Users per Client, Annual Rev/Client (ARPC), Annual COS/Client, Annual Rev/Subscriber (ARPU), Annual COS/Subscriber, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback Period (Months)
- **Notes & Customizations**: Values are scaled by 1000.

### Key Performance Indicators by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details Key Performance Indicators by Segment.
- **Cell Range**: A266:FS356
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**:
      - Annual data: G270:Q356
      - Monthly data: T270:FS354, AR273:FS352, BP273:FS321
- **Time Series Details**:
    - Annual: E3:I3, J3:Q3. Range is not specified, but based on data, it's likely 2011-2023.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Avg. Users per Client, Annual Rev/Client (ARPC), Annual COS/Client, Annual Rev/Subscriber (ARPU), Annual COS/Subscriber, Churn, Annual Gross Dollar Retention, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, LTV / CAC
- **Notes & Customizations**: Values are scaled by 1000.

### Debt Availability Build
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Calculates Debt Availability based on MRR and other factors.
- **Cell Range**: B360:DW373
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: BW3:DW3 (Implied months, but not explicitly labeled)
    - **Data Range**: BW363:DW373
- **Time Series Details**:
    - Monthly: Implied 3-month period (T3M) in columns BW:DW. No specific dates are provided, but it's tied to the monthly series.
    - **Frequency**: Monthly (3-month trailing)
- **Key Components**: Multiplier of MRR, T3M MRR, T3M Revenue Lost, T3M Churn, Annualized Retention Rate, Current MRR, Availability Amount
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 5: CAC by Segment
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: CAC by Segment
- **Key Sections Identified**:
    - Title/Header
    - CAC Summary
    - CAC Detail by Segment
    - Adjusted Sales and Marketing Cost Analysis

## 2. Detailed Section Analysis

### Title/Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and other descriptive information.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: "AlphaSense, Inc.", "CAC by Segment", "1 - Base - $25mm"
- **Notes & Customizations**: None

### CAC Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of Upsell Cost, CAC, and Support Cost for Total Company, Financial, and Corporate segments.
- **Cell Range**: B6:FS21
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E9:Q21
      - Monthly data: T9:FS21
- **Time Series Details**:
    - Annual: 2013 to 2021 (E3:Q3). Note: 2013 to 2017 are not explicitly labeled, but the data is present.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Upsell Cost, CAC, Support Cost, Total Company, Financial, Corporate
- **Notes & Customizations**: Values are scaled by 1000.

### CAC Detail by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of CAC by segment, including Account Manager - Corp, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, and AE - Enterprise. Also includes Wages and Support Costs.
- **Cell Range**: A23:FS69
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G2:Q2 (Annual), AR2:FS2 (Quarterly)
    - **Data Range**:
      - Annual data: G26:Q69
      - Quarterly data: AR26:FS69
- **Time Series Details**:
    - Annual: 2015 to 2021 (G2:Q2). Note: 2015 to 2017 are not explicitly labeled, but the data is present.
    - Quarterly: 2018 1Q to 2020 1Q (AR2:CB2).
    - **Frequency**: Annual, Quarterly
- **Key Components**: Account Manager - Corp, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise, Total, % Financial, % Corporate, Wages
- **Notes & Customizations**: Values are scaled by 1000.

### Adjusted Sales and Marketing Cost Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes Adjusted Sales and Marketing Costs, including People Costs and All-In Support Costs.
- **Cell Range**: A72:FS141
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E74:Q141
      - Monthly data: T74:FS141
- **Time Series Details**:
    - Annual: 2013 to 2021 (E3:Q3). Note: 2013 to 2017 are not explicitly labeled, but the data is present.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Total Company, Adjusted Sales and Marketing Cost, % to CAC, % to Upsell, $ to CAC, $ to Upsell, People Costs, Adjusted People Costs, All-In Support Costs, Total Users (excl. Other), % Financial, % Corporate
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 6: Payback Period
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Payback Period
- **Key Sections Identified**:
    - Header
    - Payback Period - Total Company
    - Cash Payback - Monthly Detail
    - Payback Period - Financial
    - Payback Period - Corporate
    - Cash Payback - Monthly Detail (Financial)
    - Cash Payback - Monthly Detail (Corporate)

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Cell Range**: B2:Q4
- **Layout Structure**:
    - **Row Headers Location**: B2:B4
    - **Column Headers Location**: None
    - **Data Range**: E3:I3, J3:Q3
- **Time Series Details**:
    - **Date Range**: 2021 to 2027
    - **Frequency**: Annual
- **Key Components**: AlphaSense, Inc., Payback Period, 1 - Base - $25mm
- **Notes & Customizations**: Contains the company name, report title, and scenario description.

### Payback Period - Total Company
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summary of key metrics used to calculate the payback period for the total company.
- **Cell Range**: B6:Q44
- **Layout Structure**:
    - **Row Headers Location**: B8:B44
    - **Column Headers Location**: E8:Q8
    - **Data Range**:
      - Annual data: E16:Q44
- **Time Series Details**:
    - **Date Range**: 2021 to 2027
    - **Frequency**: Annual
- **Key Components**: LTV / CAC, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback
- **Notes & Customizations**: Values are scaled by 1000.

### Cash Payback - Monthly Detail
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Monthly detail of cash payback, likely used to create a waterfall chart.
- **Cell Range**: B45:Q241
- **Layout Structure**:
    - **Row Headers Location**: B47:B241
    - **Column Headers Location**: E45:Q45
    - **Data Range**:
      - Annual data: E48:Q241
- **Time Series Details**:
    - **Date Range**: 2021 to 2027
    - **Frequency**: Annual
- **Key Components**: Month, Multiplier, Increase
- **Notes & Customizations**: Values are scaled by 1000.

### Payback Period - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summary of key metrics used to calculate the payback period for the Financial division.
- **Cell Range**: B345:Q377
- **Layout Structure**:
    - **Row Headers Location**: B347:B377
    - **Column Headers Location**: G349:Q349
    - **Data Range**:
      - Annual data: G349:Q377
- **Time Series Details**:
    - **Date Range**: 2021 to 2027
    - **Frequency**: Annual
- **Key Components**: LTV / CAC, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback
- **Notes & Customizations**: Values are scaled by 1000.

### Payback Period - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summary of key metrics used to calculate the payback period for the Corporate division.
- **Cell Range**: B576:Q608
- **Layout Structure**:
    - **Row Headers Location**: B578:B608
    - **Column Headers Location**: G580:Q580
    - **Data Range**:
      - Annual data: G580:Q608
- **Time Series Details**:
    - **Date Range**: 2021 to 2027
    - **Frequency**: Annual
- **Key Components**: LTV / CAC, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback
- **Notes & Customizations**: Values are scaled by 1000.

### Cash Payback - Monthly Detail (Financial)
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Monthly detail of cash payback for the Financial division, likely used to create a waterfall chart.
- **Cell Range**: B378:Q574
- **Layout Structure**:
    - **Row Headers Location**: B380:B574
    - **Column Headers Location**: G381:Q381
    - **Data Range**:
      - Annual data: G381:Q574
- **Time Series Details**:
    - **Date Range**: 2021 to 2027
    - **Frequency**: Annual
- **Key Components**: Month, Multiplier, Increase
- **Notes & Customizations**: Values are scaled by 1000.

### Cash Payback - Monthly Detail (Corporate)
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Monthly detail of cash payback for the Corporate division, likely used to create a waterfall chart.
- **Cell Range**: B609:Q805
- **Layout Structure**:
    - **Row Headers Location**: B611:B805
    - **Column Headers Location**: G612:Q612
    - **Data Range**:
      - Annual data: G612:Q805
- **Time Series Details**:
    - **Date Range**: 2021 to 2027
    - **Frequency**: Annual
- **Key Components**: Month, Multiplier, Increase
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 7: Fin CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Fin CTRL
- **Key Sections Identified**:
    - Header
    - Balance Sheet Support

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description. Provides context for the financial data.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: AlphaSense, Inc., Financial Statements CTRL, 1 - Base - $25mm
- **Notes & Customizations**: None

### Balance Sheet Support
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides key metrics and assumptions used to support the balance sheet projections. Includes calculations and percentages related to various balance sheet accounts.
- **Cell Range**: A12:FS189
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: E14:Q189
      - Monthly data: T14:FS189
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
- **Key Components**: Days Sales Outstanding, Prepaid Expenses (Monthly % of Operating Expenses), Capital Expenditures - % of Revenue, Accounts Payable Days Payable Outstanding, Commissions Payable - % of ARR, Accrued Expenses Days Payable Outstanding, Accrued Commissions - % of ARR, Accrued Wages - % Growth, Accrued Holiday Pay - % of Wages, Accrued Interest - % Growth, Payroll Taxes Payable - % Growth, Sales Taxes Payable - % of Revenue, Deferred Commissions Growth, Tekes - 14887, Tekes - 15118, Tekes - 14560, Tekes - 14223, Tekes - 15543, Interest Rate, Interest Rate - Admin Fee, Interest Rate on Cash Account, Percent of Cash in Account, Effective Commission Rate, Day Sales Outstanding, Credit Card Payable - % of OpEx, Target Hit Rate - Accrued Commission, LIBOR
- **Notes & Customizations**: Contains both annual and monthly time series data. Some rows have "na" values for certain periods. The "x" in column A likely indicates a row that is used in calculations or is otherwise important.


====================================================================================================
# SHEET 8: Fin
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Fin
- **Key Sections Identified**:
    - Header
    - Income Statement
    - Balance Sheet
    - Cash Flow Statement
    - Balance Sheet Support
    - Long Term Liabilities
    - Equity Investment
    - SVB Debt
    - Income Statement Support - Income Taxes

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and scenario description.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: AlphaSense, Inc., Financial Statements, 1 - Base - $25mm
- **Notes & Customizations**: None

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time.
- **Cell Range**: A6:FS55
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows E2:Q2 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E9:Q55
      - Monthly data: T9:FS55
- **Time Series Details**:
    - Annual: 2015 to 2027 (E2:Q2)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Operating Expenses, EBITDA, Net Income
- **Notes & Customizations**: Includes intercompany revenue/expenses.

### Balance Sheet
- **Section Type**: Balance Sheet
- **Description & Purpose**: Presents a snapshot of the company's assets, liabilities, and equity at a specific point in time.
- **Cell Range**: A57:FS141
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows E2:Q2 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E62:Q141
      - Monthly data: T62:FS141
- **Time Series Details**:
    - Annual: 2015 to 2027 (E2:Q2)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Current Assets, Fixed Assets, Accounts Payable, Accrued Expenses, Deferred Revenue, Convertible Notes, Total Liabilities & Equity
- **Notes & Customizations**: Includes a note about budgeted values.

### Cash Flow Statement
- **Section Type**: Standard Cash Flow Statement
- **Description & Purpose**: Tracks the movement of cash both into and out of the company during a period of time.
- **Cell Range**: A143:FS224
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows E2:Q2 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E147:Q224
      - Monthly data: T147:FS224
- **Time Series Details**:
    - Annual: 2015 to 2027 (E2:Q2)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Net Income, Depreciation, Accounts Receivable, Accounts Payable, Net Cash Flows from Operating Activities, Net Cash Flows from Investing Activities, Net Cash Flows from Financing Activities, Cash, End of Period
- **Notes & Customizations**: None

### Balance Sheet Support
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides supporting calculations and metrics for the balance sheet.
- **Cell Range**: A228:FS608
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows E2:Q2 (Annual), T3:FS3 (Monthly), CJ1:FS1 (Monthly)
    - **Data Range**:
      - Annual data: E234:Q608
      - Monthly data: T234:FS608
- **Time Series Details**:
    - Annual: 2015 to 2027 (E2:Q2)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Days in Period, Total Billings, Total Bookings, Days Sales Outstanding, Allowance for Doubtful Accounts, Fixed Assets, Total
- **Notes & Customizations**: Includes calculations related to prepaid expenses, depreciation, and accounts receivable.

### Long Term Liabilities
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the calculations and projections for long-term liabilities.
- **Cell Range**: A692:FS729
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows E2:Q2 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E696:Q729
      - Monthly data: T698:FS729
- **Time Series Details**:
    - Annual: 2015 to 2027 (E2:Q2)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Tekes - 14887, Tekes - 15118, Tekes - 14560, Tekes - 14223, Tekes - 15543, Starting Balance, Ending Balance, Interest Rate, Total Interest / Admin Expense, Total Payback
- **Notes & Customizations**: Focuses on specific long-term loan details.

### Equity Investment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the calculations and projections for equity investment.
- **Cell Range**: A731:FS739
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows E2:Q2 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E735:Q739
      - Monthly data: T735:FS739
- **Time Series Details**:
    - Annual: 2015 to 2027 (E2:Q2)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Net Investment Amount, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Focuses on specific Equity Investment details.

### SVB Debt
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the calculations and projections for SVB Debt.
- **Cell Range**: B747:FS789
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows CJ1:FS1 (Monthly)
    - **Data Range**:
      - Monthly data: CJ749:FS789
- **Time Series Details**:
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Monthly
- **Key Components**: MRR, Multiplier, Retention, Total Availability, Debt, Leverage, Minimum Cash Balance, Cash from Operations, Cash from Investing Activities, Revolver, Cash from Financing Activities, Change in Cash, Cash, BoP, Change, Cash, EoP, Cash (Excluding Revolver), Revolver Drawn (Y/N), Cash Needed, Beginning, Add, Paid Down, End, Debt Issuance Amortization, Interest, LIBOR, Interest Rate
- **Notes & Customizations**: Focuses on specific SVB Debt details.

### Income Statement Support - Income Taxes
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides supporting calculations for income taxes in the income statement.
- **Cell Range**: B791:FS836
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows E2:Q2 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E793:Q836
      - Monthly data: T793:FS836
- **Time Series Details**:
    - Annual: 2015 to 2027 (E2:Q2)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Pre Tax Income, Starting NOL, NOL (Use) Add, Ending NOL, Taxable Income, Tax Rate, Taxes Paid, FCF, CFO, EBITDA
- **Notes & Customizations**: Includes NOL calculations and adjustments to EBITDA.


====================================================================================================
# SHEET 9: Debt Compliance
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Debt Compliance
- **Key Sections Identified**:
    - Revenue Growth Analysis
    - Liquidity Compliance Check
    - Liquidity Buffer Analysis

## 2. Detailed Section Analysis

### Revenue Growth Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes revenue growth and compares it against a growth covenant to ensure compliance.
- **Cell Range**: B6:ED13
- **Layout Structure**:
    - **Row Headers Location**: B6:B13
    - **Column Headers Location**: D3:M4, O3:ED4
    - **Data Range**:
      - Annual data: D8:M10
      - Monthly data: O8:ED10, AP12:ED12
- **Time Series Details**:
    - Annual: 2018 to 2027 (D3:M3).
    - Monthly: 2018-01-31 to 2027-12-31 (O4:ED4). Anchor points: O4=2018-01-31, AA4=2019-01-31, AM4=2020-01-31, AY4=2021-01-31, BK4=2022-01-31, BW4=2023-01-31, CI4=2024-01-31, CU4=2025-01-31, DG4=2026-01-31, DS4=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Revenue, T3M, Growth Rate, Growth Covenant, Compliance Check
- **Notes & Customizations**: Revenue is scaled by 1000. Compliance check shows "OK" if the covenant is met.

### Liquidity Compliance Check
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks various liquidity metrics, including EBITDA, cash, borrowings, and availability, to assess compliance with liquidity covenants.
- **Cell Range**: B16:ED45
- **Layout Structure**:
    - **Row Headers Location**: B16:B45
    - **Column Headers Location**: O3:ED4, D3:M4
    - **Data Range**:
      - Annual data: D25:M29, D26:M26, D27:M27, D28:M28, D29:M29
      - Monthly data: O18:ED18, AQ19:ED19, O21:ED21, AQ23:ED23, O25:ED29, O26:ED26, O27:ED27, O28:ED28, O29:ED29, AQ31:ED31, AQ32:BG32, BJ32:BK32, BU32:BW32, CB32:CD32, CG32:CJ32, CM32:CS32, CW32, AQ33:ED33, O38:AP38, AQ38:ED38, O39:AP39, AQ39:ED39, AQ40:ED40, AQ41:ED41, CD42, AQ43:ED43, CD44
- **Time Series Details**:
    - Annual: 2018 to 2027 (D3:M3).
    - Monthly: 2018-01-31 to 2027-12-31 (O4:ED4). Anchor points: O4=2018-01-31, AA4=2019-01-31, AM4=2020-01-31, AY4=2021-01-31, BK4=2022-01-31, BW4=2023-01-31, CI4=2024-01-31, CU4=2025-01-31, DG4=2026-01-31, DS4=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Remaining Months Liquidity (RML), Total Borrowings, Total Availability, Cash, Net Availability + Unrestricted Cash, EBITDA, Capitalized R&D, Capitalized Expenditures, Change in Deferred Revenue, Adjusted EBITDA, Liquidity Threshold, Restricted Cash, Net Availability, Liquidity, Thershold, Compliance Check
- **Notes & Customizations**: Values are scaled by 1000. "N/A" and "Breaks" are present in some cells. Compliance check shows "OK" if the covenant is met.

### Liquidity Buffer Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates different liquidity buffers to assess the company's financial cushion.
- **Cell Range**: B49:ED53
- **Layout Structure**:
    - **Row Headers Location**: B49:B53
    - **Column Headers Location**: O3:ED4
    - **Data Range**: AQ49:ED49, AQ51:ED51, AQ53:ED53
- **Time Series Details**:
    - Monthly: 2018-01-31 to 2027-12-31 (O4:ED4). Anchor points: O4=2018-01-31, AA4=2019-01-31, AM4=2020-01-31, AY4=2021-01-31, BK4=2022-01-31, BW4=2023-01-31, CI4=2024-01-31, CU4=2025-01-31, DG4=2026-01-31, DS4=2027-01-31
    - Frequency: Monthly
- **Key Components**: $5m Liquidity Buffer, RML Liquidity Buffer, Overall Liqudity Buffer
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 10: ARR and Rev CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: ARR and Rev CTRL
- **Key Sections Identified**:
    - Header
    - Revenue & Quota Assumptions
    - Productivity - % of Quota
    - Total ARR - % New Bookings
    - Total ARR - % Upsell
    - Productivity - Allocation
    - ARR Metrics

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and report title.
- **Cell Range**: B2:Q3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: B2:Q3
- **Time Series Details**: None
- **Key Components**: Company Name, Report Title
- **Notes & Customizations**: None

### Revenue & Quota Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines revenue assumptions and quota targets for different sales roles and scenarios (Base, Growth, Upside). It includes revenue percentages of MRR for various customer segments and quota attainment levels.
- **Cell Range**: A7:FS118
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8 (Year and Month)
    - **Data Range**:
      - Annual data: I15:Q18, I22:Q25, I29:Q32, I38:Q41, J43:Q43, I45:Q48, I51:Q54, I57:Q60, J62:Q62, I64:Q67, I70:Q73, I76:Q79, J81:Q81, I83:Q86, I89:Q92, I95:Q98, J100:Q100, I102:Q105, I108:Q111, J113:Q113, I115:Q118
      - Monthly data: BX15:FS18, BX22:FS25, BX29:FS32, BX38:FS41, BX45:FS48, BX51:FS54, BX57:FS60, BX64:FS67, BX70:FS73, BX76:FS79, BX83:FS86, BX89:FS92, BX95:FS98, BX102:FS105, BX108:FS111, BX115:FS118
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Rev % of MRR (Financial, Corporate, Other), Quota (Account Manager, AE - Financial, AE - Corporate, VP Bus Dev, AE - Enterprise)
- **Notes & Customizations**: Scenarios include "Base", "Growth", and "Base (R&D)". Quotas are split into "Active", "Base", and "Upside".

### Productivity - % of Quota
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates productivity as a percentage of quota, incorporating seasonality and adjustments.
- **Cell Range**: A120:FS156
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8 (Year and Month)
    - **Data Range**:
      - Annual data: I123:Q126, I129:Q132, I135:Q138, I141:Q144, I147:Q150, I153:Q156
      - Monthly data: BX122:FS122, BX123:CA123, CB124:CB124, BX128:FS128, BX129:CA129, CB129:CM129, CN129:FS129, BX134:FS134, BX135:CA135, CB135:CM135, CN135:FS135, BX140:FS140, BX141:CA141, CB141:CM141, CN141:FS141, BX146:FS146, CB147:CM147, CN147:FS147, BX152:FS152, CB153:CM153, CN153:FS153
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Productivity - % of Quota, Seasonality, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise
- **Notes & Customizations**: Includes adjustments and seasonality factors.

### Total ARR - % New Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the percentage of total ARR attributable to new bookings.
- **Cell Range**: A158:FS188
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8 (Year and Month)
    - **Data Range**:
      - Annual data: I161:Q164, I167:Q170, I173:Q176, I179:Q182, I185:Q188
      - Monthly data: BX160:FS160, BX166:FS166, BX172:FS172, BX178:FS178, BX184:FS184
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Total ARR - % New Bookings, Account Manager, AE - Financial, AE - Corporate, VP Bus Dev, AE - Enterprise
- **Notes & Customizations**: None

### Total ARR - % Upsell
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the percentage of total ARR attributable to upsells.
- **Cell Range**: A190:FS220
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8 (Year and Month)
    - **Data Range**:
      - Annual data: I193:Q196, I199:Q202, I205:Q208, I211:Q214, I217:Q220
      - Monthly data: BX192:FS192, BX198:FS198, BX204:FS204, BX210:FS210, BX216:FS216
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Total ARR - % Upsell, Account Manager, AE - Financial, AE - Corporate, VP Bus Dev, AE - Enterprise
- **Notes & Customizations**: None

### Productivity - Allocation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section focuses on the allocation of productivity across different segments.
- **Cell Range**: A222:FS246
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8 (Year and Month)
    - **Data Range**:
      - Annual data: I225:Q228, I231:Q234, I237:Q240, I243:Q246
      - Monthly data: BX224:FS224, BX230:FS230, BX236:FS236, BX242:FS242
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: VP - Bus Dev - % to Financial, VP - Bus Dev - % to Corporate, AE - Enterprise - % to Financial, AE - Enterprise - % to Corporate
- **Notes & Customizations**: None

### ARR Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents key ARR metrics, including year-over-year growth and ARR per user.
- **Cell Range**: A249:FS318
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8 (Year and Month)
    - **Data Range**:
      - Annual data: F251:Q251, E252:Q252, I253:Q256, F258:Q258, E259:Q259, I260:Q263, F265:K265, E266:Q266, I267:Q270, F275:Q275, E276:Q276, I277:Q280, F282:Q282, E283:Q283, I284:Q287, F289:K289, E290:Q290, I291:Q294, F299:Q299, E300:H300, I300:Q300, I301:Q304, F306:Q306, E307:H307, I307:Q307, I308:Q311, F313:K313, E314:H314, I314:Q314, I315:Q318
      - Monthly data: T252:BW252, BX252:FS252, T259:BW259, BX259:FS259, T266:BW266, BX266:FS266, T276:BW276, BX276:FS276, T283:BW283, BX283:FS283, T290:BW290, BX290:FS290, T300:BW300, BX300:FS300, T307:BW307, BX307:FS307, T314:BW314, BX314:FS314
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: % YoY Growth, ARR / User - Active, ARR / User - Base, ARR / User - Target
- **Notes & Customizations**: Metrics are categorized by Financial, Corporate, and Other segments.


====================================================================================================
# SHEET 11: Sales Prod Input
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Sales Prod Input
- **Key Sections Identified**:
    - Assumptions
    - Productivity by Role
    - Productivity (Adjusted for Seasonality)

## 2. Detailed Section Analysis

### Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the quota per person and seasonality assumptions used in the sales productivity calculations.
- **Cell Range**: B3:Q15
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: N/A
      - Monthly data: F15:Q15
- **Time Series Details**:
    - **Date Range**: 2021-01-31 to 2021-12-31 (F3:Q3)
    - **Frequency**: Monthly
- **Key Components**: Quota per Person, Seasonality, All Roles
- **Notes & Customizations**: Quota is scaled by 1000.

### Productivity by Role
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the productivity of different roles within the sales organization.
- **Cell Range**: B17:Q23
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: N/A
      - Monthly data: F19:Q23
- **Time Series Details**:
    - **Date Range**: 2021-01-31 to 2021-12-31 (F3:Q3)
    - **Frequency**: Monthly
- **Key Components**: Productivity, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise
- **Notes & Customizations**: None.

### Productivity (Adjusted for Seasonality)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the productivity of different roles adjusted for seasonality.
- **Cell Range**: B25:Q31
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: N/A
      - Monthly data: F27:Q31
- **Time Series Details**:
    - **Date Range**: 2021-01-31 to 2021-12-31 (F3:Q3)
    - **Frequency**: Monthly
- **Key Components**: Productivity (Adjusted for Seasonality), Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise
- **Notes & Customizations**: None.



====================================================================================================
# SHEET 12: ARR and Revenue
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: ARR and Revenue
- **Key Sections Identified**:
    - ARR and Revenue Summary
    - ARR by Segment
    - Revenue by Segment
    - Revenue as % of MRR
    - Sales Productivity
    - Total Bookings
    - New Bookings
    - Upsell
    - New Bookings - % of Total Bookings
    - Upsell - % of Total Bookings
    - Total Bookings by Segment
    - Financial ARR
    - Corporate ARR
    - Other ARR
    - Combined

## 2. Detailed Section Analysis

### ARR and Revenue Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a high-level overview of ARR, Revenue, and related metrics. It tracks the company's overall performance.
- **Cell Range**: A6:FS23
- **Layout Structure**:
    - **Row Headers Location**: B6:B23
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E8:Q23
      - Monthly data: T8:FS23
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: ARR - Start, New Business, Upsell, Churn, ARR - End, % Churn Rate, Up for Renewal, Retention Rate, ARR, Revenue, % Growth
- **Notes & Customizations**: The "% YoY Growth" in cell E13 is marked as "na" for the first year.

### ARR by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down ARR by different segments (Financial, Corporate, Other) to analyze performance across customer groups.
- **Cell Range**: A25:FS31
- **Layout Structure**:
    - **Row Headers Location**: B27:B31
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E28:Q31
      - Monthly data: T28:FS31
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total ARR
- **Notes & Customizations**: None

### Revenue by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down Revenue by different segments (Financial, Corporate, Other) to analyze performance across customer groups.
- **Cell Range**: B33:FS37
- **Layout Structure**:
    - **Row Headers Location**: B33:B37
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E34:Q37
      - Monthly data: T34:FS37
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total Revenue
- **Notes & Customizations**: None

### Revenue as % of MRR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the percentage of revenue relative to monthly recurring revenue (MRR) by segment.
- **Cell Range**: B39:FS43
- **Layout Structure**:
    - **Row Headers Location**: B40:B43
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E40:Q43
      - Monthly data: T40:FS43
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total Revenue as % of MRR
- **Notes & Customizations**: None

### Sales Productivity
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks sales headcount and productivity metrics.
- **Cell Range**: A45:FS70
- **Layout Structure**:
    - **Row Headers Location**: B45:B70
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E48:Q70
      - Monthly data: T48:FS70
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
- **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Sales Headcount, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other, Total Sales Headcount, Effective Sales Headcount, Total Effective Sales Reps, Quota per Person
- **Notes & Customizations**: The "Quota per Person" has a different column structure (F66:H66, I66:Q66, BD66:CI66, CJ66:FS66).

### Total Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks total bookings.
- **Cell Range**: B73:FS99
- **Layout Structure**:
    - **Row Headers Location**: B73:B99
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E74:Q99
      - Monthly data: T74:FS99
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total Quota, Productivity - % of Quota (Adjusted for Seasonality), Total Bookings, Account Manager, Other, New Bookings
- **Notes & Customizations**: The "Productivity - % of Quota (Adjusted for Seasonality)" has a different column structure (F83:Q83, CB83:CI83, CJ83:FS83).

### New Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks new bookings.
- **Cell Range**: B101:FS109
- **Layout Structure**:
    - **Row Headers Location**: B101:B109
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I102:Q106, E109:Q109
      - Monthly data: CJ102:FS106, T109:FS109
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: New Bookings, Account Manager, Total New Bookings
- **Notes & Customizations**: None

### Upsell
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks upsell bookings.
- **Cell Range**: B111:FS119
- **Layout Structure**:
    - **Row Headers Location**: B111:B119
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I112:Q116, E119:Q119
      - Monthly data: CJ112:FS116, T119:FS119
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Upsell, Account Manager, Total Upsell
- **Notes & Customizations**: None

### New Bookings - % of Total Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks new bookings as a percentage of total bookings.
- **Cell Range**: B121:FS129
- **Layout Structure**:
    - **Row Headers Location**: B121:B129
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I122:Q126, E129:Q129
      - Monthly data: CJ122:FS126, T129:FS129
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: New Bookings - % of Total Bookings, Account Manager, Total New Bookings
- **Notes & Customizations**: None

### Upsell - % of Total Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks upsell bookings as a percentage of total bookings.
- **Cell Range**: B131:FS139
- **Layout Structure**:
    - **Row Headers Location**: B131:B139
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I132:Q136, E139:Q139
      - Monthly data: CJ132:FS136, T139:FS139
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Upsell - % of Total Bookings, Account Manager, Total Upsell
- **Notes & Customizations**: None

### Total Bookings by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks total bookings by segment.
- **Cell Range**: B141:FS157
- **Layout Structure**:
    - **Row Headers Location**: B141:B157
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E141:Q157
      - Monthly data: BS141:FS141, CJ142:FS151, T154:FS157
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: VP - Bus Dev, % Financial, Amount to Financial, % Corporate, Amount to Corporate, AE - Enterprise, Financial, Corporate, Other, Total Bookings
- **Notes & Customizations**: The "% YoY Growth" in cell E158 is marked as "na" for the first year.

### New Bookings by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks new bookings by segment.
- **Cell Range**: B160:FS165
- **Layout Structure**:
    - **Row Headers Location**: B160:B165
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E161:Q164
      - Monthly data: T161:FS165
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: New Bookings by Segment, Financial, Corporate, Other, Total New Bookings
- **Notes & Customizations**: The "% YoY Growth" in cell E165 is marked as "na" for the first year.

### Upsell by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks upsell bookings by segment.
- **Cell Range**: B167:FS172
- **Layout Structure**:
    - **Row Headers Location**: B167:B172
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E168:Q171
      - Monthly data: T168:FS172
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Upsell by Segment, Financial, Corporate, Other, Total Upsell
- **Notes & Customizations**: The "% YoY Growth" in cell E172 is marked as "na" for the first year.

### Financial ARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks financial ARR.
- **Cell Range**: A174:FS189
- **Layout Structure**:
    - **Row Headers Location**: B174:B189
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E176:Q189
      - Monthly data: T176:FS189
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial ARR, Beginning ARR, New Business, Upsell, Churn, Ending ARR, % YoY Growth, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Notes & Customizations**: None

### Corporate ARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks corporate ARR.
- **Cell Range**: A191:FS206
- **Layout Structure**:
    - **Row Headers Location**: B191:B206
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E193:Q206
      - Monthly data: T193:FS206
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Corporate ARR, Beginning ARR, New Business, Upsell, Churn, Ending ARR, % YoY Growth, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Notes & Customizations**: None

### Other ARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks other ARR.
- **Cell Range**: A208:FS223
- **Layout Structure**:
    - **Row Headers Location**: B208:B223
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E210:Q223
      - Monthly data: T210:FS223
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Other ARR, Beginning ARR, New Business, Upsell, Churn, Ending ARR, % YoY Growth, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Notes & Customizations**: None

### Combined
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks combined metrics.
- **Cell Range**: A225:FS233
- **Layout Structure**:
    - **Row Headers Location**: B225:B233
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E227:Q233
      - Monthly data: T227:FS233
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Combined, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Notes & Customizations**: None


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
    - Other Sales - Salary
    - Old Assumptions (To Be Deleted)
    - Product Specialist Headcount
    - Product Specialist Manager Headcount
    - Sales - Admin Headcount
    - Sales Manager Headcount
    - Sales Operations Manager Headcount
    - Sales Recruiter Headcount
    - SDR Headcount

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the spreadsheet's purpose.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: AlphaSense, Inc., Sales Representatives CTRL, 1 - Base - $25mm
- **Notes & Customizations**: Standard header information.

### Quota Sales Reps Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of quota-carrying sales representatives and related metrics.
- **Cell Range**: A12:FS26
- **Layout Structure**:
    - **Row Headers Location**: B12:B26
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E14:Q26
      - Monthly data: T15:FS26
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Total Headcount, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Includes headcount added and removed in the period.

### Account Manager Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Account Managers and related metrics.
- **Cell Range**: A158:FS175
- **Layout Structure**:
    - **Row Headers Location**: B158:B175
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E164:Q175
      - Monthly data: T164:FS175
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Account Manager, Annual Increase, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Includes salary and sales bonus information.

### AE - Financial Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Financial and related metrics.
- **Cell Range**: A30:FS68
- **Layout Structure**:
    - **Row Headers Location**: B30:B68
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E30:Q68
      - Monthly data: T30:FS68
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: AE - Financial, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D), % of Total Headcount
- **Notes & Customizations**: Includes headcount added and removed in the period, broken down by base, target, and upside.

### AE - Corporate Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Corporate and related metrics.
- **Cell Range**: A72:FS110
- **Layout Structure**:
    - **Row Headers Location**: B72:B110
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E72:Q110
      - Monthly data: T72:FS110
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: AE - Corporate, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D), % of Total Headcount
- **Notes & Customizations**: Includes headcount added and removed in the period, broken down by base, target, and upside.

### VP - Bus Dev Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of VP - Bus Dev and related metrics.
- **Cell Range**: A114:FS125
- **Layout Structure**:
    - **Row Headers Location**: B114:B125
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E114:Q125
      - Monthly data: T114:FS125
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: VP - Bus Dev, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D), % of Total Headcount
- **Notes & Customizations**: Includes headcount added and removed in the period.

### AE - Enterprise Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Enterprise and related metrics.
- **Cell Range**: A129:FS140
- **Layout Structure**:
    - **Row Headers Location**: B129:B140
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E129:Q140
      - Monthly data: T129:FS140
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: AE - Enterprise, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D), % of Total Headcount
- **Notes & Customizations**: Includes headcount added and removed in the period.

### AE - Other Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Other and related metrics.
- **Cell Range**: A144:FS155
- **Layout Structure**:
    - **Row Headers Location**: B144:B155
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E144:Q155
      - Monthly data: T144:FS155
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: AE Other - Headcount Added in Period, AE Other - Headcount Removed in Period, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Includes headcount added and removed in the period.

### Other Sales - Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of CRO and related metrics.
- **Cell Range**: A263:FS272
- **Layout Structure**:
    - **Row Headers Location**: B263:B272
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E267:Q272
      - Monthly data: T268:FS268
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: CRO, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Includes headcount added in the period.

### Other Sales - Salary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the salary of CRO and related metrics.
- **Cell Range**: A477:FS484
- **Layout Structure**:
    - **Row Headers Location**: B477:B484
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E480:Q484
      - Monthly data: T480:FS480
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: CRO, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Includes annual increase.

### Old Assumptions (To Be Deleted)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the assumptions for Manager - Corporate and related metrics.
- **Cell Range**: A335:BW350
- **Layout Structure**:
    - **Row Headers Location**: B335:B350
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E339:H350
      - Monthly data: T339:BW350
- **Time Series Details**:
    - Annual: 2015 to 2018 (E7:H7)
    - Monthly: 2015-01-31 to 2019-12-31 (T9:BW9).
    - Frequency: Annual, Monthly
- **Key Components**: Manager - Corporate, Manager - Corporate - Added in Period (2018 Driver), Manager - Corporate - AE Corp per Manager Corporate (2019 and Beyond Annual Driver)
- **Notes & Customizations**: Includes assumptions for 2018 and beyond.

### Product Specialist Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Product Specialist and related metrics.
- **Cell Range**: A353:FS367
- **Layout Structure**:
    - **Row Headers Location**: B353:B367
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E355:Q367
      - Monthly data: T355:FS367
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Product Specialist, AE per Product Specialist (2019 and Beyond Annual Driver)
- **Notes & Customizations**: Includes Product Specialist Added (2018 Driver).

### Product Specialist Manager Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Product Specialist Manager and related metrics.
- **Cell Range**: A370:FS384
- **Layout Structure**:
    - **Row Headers Location**: B370:B384
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E372:Q384
      - Monthly data: T372:FS384
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Product Specialist - Mgr, Product Specialist per Product Specialist Manager (2019 and Beyond Annual Driver)
- **Notes & Customizations**: Includes Product Specialist Manager Added (2018 Driver).

### Sales - Admin Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Sales - Admin and related metrics.
- **Cell Range**: A387:FS401
- **Layout Structure**:
    - **Row Headers Location**: B387:B401
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E389:Q401
      - Monthly data: T389:FS401
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Sales - Admin, AE per Sales Admin (2019 and Beyond Annual Driver)
- **Notes & Customizations**: Includes Sales Admin Added (2018 Driver).

### Sales Manager Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Sales Manager and related metrics.
- **Cell Range**: A404:FS418
- **Layout Structure**:
    - **Row Headers Location**: B404:B418
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E406:Q418
      - Monthly data: T406:FS418
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Sales Manager, Quota'd Rep per Sales Manager (2019 and Beyond Annual Driver)
- **Notes & Customizations**: Includes Sales Manager Added (2018 Driver).

### Sales Operations Manager Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Sales Operations Manager and related metrics.
- **Cell Range**: A421:FS435
- **Layout Structure**:
    - **Row Headers Location**: B421:B435
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E423:Q435
      - Monthly data: T423:FS435
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Sales Operations Manager, AE per Sales Operations Manager (2019 and Beyond Annual Driver)
- **Notes & Customizations**: Includes Sales Operations Manager Added (2018 Driver).

### Sales Recruiter Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Sales Recruiter and related metrics.
- **Cell Range**: A438:FS445
- **Layout Structure**:
    - **Row Headers Location**: B438:B445
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E440:Q445
      - Monthly data: T440:FS445
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Sales Recruiter, Sales Recruiter Added
- **Notes & Customizations**: Includes headcount added in the period.

### SDR Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of SDR and related metrics.
- **Cell Range**: A448:FS474
- **Layout Structure**:
    - **Row Headers Location**: B448:B474
    - **Column Headers Location**: E7:Q8 (Year), T7:FS8 (Month)
    - **Data Range**:
      - Annual data: E450:Q474
      - Monthly data: T450:FS474
- **Time Series Details**:
    - Annual: 2015 to 2027 (E7:Q7)
    - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: SDR, AE per SDR (2019 and Beyond Annual Driver) - Active, Base, Upside
- **Notes & Customizations**: Includes SDR Added (2018 Driver).


====================================================================================================
# SHEET 14: Sales Role Input
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Sales Role Input
- **Key Sections Identified**:
    - Sales Role Headcount Input - Quota Roles
    - Sales Role Headcount Input - Non-Quota Roles

## 2. Detailed Section Analysis

### Section Name (Sales Role Headcount Input - Quota Roles)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the headcount requirements for quota-carrying sales roles. It allows users to input the number of sales roles required, and the system calculates the associated costs.
- **Cell Range**: A10:BA36
- **Layout Structure**:
    - **Row Headers Location**: Column A and C
    - **Column Headers Location**: F8:BA8
    - **Data Range**: F13:BA15, F19:BA22, F26:BA29, F33:BA36
- **Time Series Details**:
    - **Date Range**: 2018-01-31 to 2027-12-31 (F8:BA8). Anchor points: F8=2018-01-31, R8=2019-01-31, AD8=2020-01-31, AP8=2021-01-31, BB8=2022-01-31, BN8=2023-01-31, BZ8=2024-01-31, CL8=2025-01-31, CX8=2026-01-31, DJ8=2027-01-31
    - **Frequency**: Monthly
- **Key Components**: AE - Corporate, AE - Financial, Account Manager, VP Bus Dev, Beginning, Added, Lost, Ending.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name (Sales Role Headcount Input - Non-Quota Roles)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the headcount requirements for non-quota-carrying sales roles. It allows users to input the number of sales roles required, and the system calculates the associated costs. There are two sub-sections, one for roles where the headcount is directly input, and another where the headcount is derived from a formula.
- **Cell Range**: A38:CK59
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: AM8:CK8 (implicit, no explicit date series for this range)
    - **Data Range**: AM40:CK46, AM50:CK59
- **Time Series Details**:
    - **Date Range**: No explicit date series, but likely represents a single year or budget period.
    - **Frequency**: Annual (inferred)
- **Key Components**: CRO, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy, AM - Financial (Quota) moved to (Non-Quota), VP of Sales (Reports per VP), VP of Sales (Total AE Reports), Sales Manager (AEs per Manager), SDR Manager (SDRs per Manager), SDR (AEs per SDR), VP Customer Success (AMs + PS Managers per VP), Corporate AM (ARR per AM), Financial AM (ARR per AM), Product Specialist Manager (PS per Manager), Product Specialist (ARR per PS).
- **Notes & Customizations**: The data is scaled by 1000. The VP of Sales (Total AE Reports) section spans a larger range (AM51:DD51) than the other non-quota roles.


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
- **Description & Purpose**: Contains the company name and report title.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:H3, I3:Q3, T3:FS3
    - **Data Range**: E3:H3, I3:Q3, T3:FS3
- **Time Series Details**:
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Monthly
- **Key Components**: AlphaSense, Inc., Sales Reps Detail, 1 - Base - $25mm
- **Notes & Customizations**: Contains the company name, report title, and a scenario description.

### Quota Sales Rep Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the quota'd sales rep headcount.
- **Cell Range**: B6:FS24
- **Layout Structure**:
    - **Row Headers Location**: B6:B24
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E9:Q24
      - Monthly data: T9:FS24
- **Time Series Details**:
    - Annual: 2015 to 2027 (E3:Q3)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Quota Sales Rep Headcount, Total Quota Sales Rep Headcount, Average Effective Quota Headcount, AM - Financial, AE - Corporate, VP - Partnerships, AE - Enterprise, AE - Other, Total Average Effective Quota Headcount
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Non Quota'd Sales Team Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the non-quota'd sales team headcount.
- **Cell Range**: B26:FS42
- **Layout Structure**:
    - **Row Headers Location**: B26:B42
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E27:Q42
      - Monthly data: T27:FS42
- **Time Series Details**:
    - Annual: 2015 to 2027 (E3:Q3)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: CRO, VP of Sales, Sales Manager, SDR Manager, SDR, CS Manager, AM - Corporate, AM - Financial, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy, Total Non Quota'd Sales Team
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Quota Sales Rep Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed information on quota'd sales reps, including ramp, efficiency, and attrition.
- **Cell Range**: A44:FS190
- **Layout Structure**:
    - **Row Headers Location**: B44:B190
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E49:Q68, E73:Q93, E98:Q118, E123:Q142, E147:Q166, E171:Q190
      - Monthly data: T49:FS68, T73:FS93, T98:FS118, T123:FS142, T147:FS166, T171:FS190
- **Time Series Details**:
    - Annual: 2015 to 2027 (E3:Q3)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Beginning of Period, Added, Removed, End of Period, Ramp, Efficiency, Month 1, Month 2, Month 3, Month 4, Month 5, Month 6, Month 7, Month 8, Month 9, Month 10, Attrition, Effective Start, Add, Effective End, VP - Bus Dev
- **Notes & Customizations**: Includes both annual and monthly time series data. Contains ramp-up and attrition metrics.

### Other Sales Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed information on other sales roles, including sales team size and required managers.
- **Cell Range**: A192:FS325
- **Layout Structure**:
    - **Row Headers Location**: B194:B325
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E198:Q200, E204:Q206, E215:Q217, E224:Q226, E233:Q235, E244:Q246, E253:Q255, E262:Q264, E273:Q275, E283:Q285, E294:Q296, E301:Q303, E308:Q310, E315:Q317, E323:Q325
      - Monthly data: U198:FS200, T204:FS206, U215:FS217, U224:FS226, U233:FS235, U244:FS246, U253:FS255, U262:FS264, U273:FS275, U283:FS285, U294:FS296, U301:FS303, U308:FS310, U315:FS317, U323:FS325
- **Time Series Details**:
    - Annual: 2015 to 2027 (E3:Q3)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Sales Team, CRO, VP of Sales, Reports per VP of Sales, AEs, Sales Managers, Reports, Min. Required Sales Managers, SDRs per SDR Manager, SDRs, Min. Required SDR Managers, AE per SDR, AE, Min. Required SDRs, Customer Success, Customer Success Manager, AM + PS Manager per CS Manager, Ams + PS Manager, Min. Required AMs, Account Manager - Corporate, Corporate ARR - End of Period, Corporate ARR per Account Manager - Corp, Min. Required Account Manager - Corp, Account Manager - Financial, Financial ARR - End of Period, Financial ARR per Account Manager - FS, Min Required Account Manager - FS, Quota Carrying AMs, Quota Carrying AMs Moved, Product Specialist per Product Specialist Manager, Product Specialist, Min. Required PS - Mgrs, Operations, Enablement Manager, Sales - Admin, Sales Operations Manager, Sales Operations, Business Development
- **Notes & Customizations**: Includes both annual and monthly time series data. Contains ratios and minimum required headcount calculations.

### Total Sales Heads
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides total sales headcount information.
- **Cell Range**: A328:FS333
- **Layout Structure**:
    - **Row Headers Location**: B328:B333
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E330:Q333
      - Monthly data: T330:FS333
- **Time Series Details**:
    - Annual: 2015 to 2027 (E3:Q3)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Total Sales Heads
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Quota Rep - Salary Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the salaries for quota'd sales reps.
- **Cell Range**: B335:FS343
- **Layout Structure**:
    - **Row Headers Location**: B335:B343
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E337:Q343
      - Monthly data: T337:FS343
- **Time Series Details**:
    - Annual: 2015 to 2027 (E3:Q3)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Quota Rep - Salary Summary, Account Manager, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other, Total
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Quota Rep - Bonus Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the bonus amounts for quota'd sales reps.
- **Cell Range**: B345:FS353
- **Layout Structure**:
    - **Row Headers Location**: B345:B353
    - **Column Headers Location**: I3:Q3, CB3:FS3
    - **Data Range**:
      - Annual data: I347:Q353
      - Monthly data: CB347:FS353
- **Time Series Details**:
    - Annual: 2019 to 2027 (I3:Q3)
    - Monthly: 2020-01-31 to 2027-12-31 (CB3:FS3). Anchor points: CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Quota Rep - Bonus Summary, Account Manager, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other, Total
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Quota Rep - Salary Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed salary information for quota'd sales reps.
- **Cell Range**: A355:FS415
- **Layout Structure**:
    - **Row Headers Location**: B355:B415
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E360:Q362, I364:Q365, E370:Q372, I374:Q375, E380:Q382, I384:Q385, E390:Q392, I394:Q395, E400:Q402, I404:Q405, E410:Q412, I414:Q415
      - Monthly data: T360:FS362, CB364:FS365, T370:FS372, CB374:FS375, T380:FS382, CB384:FS385, T390:FS392, CB394:FS395, T400:FS402, CB404:FS405, T410:FS412, CB414:FS415
- **Time Series Details**:
    - Annual: 2015 to 2027 (E3:Q3)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Employees, Average Salary, Total Wages, Sales Bonus per Head, Total Sales Bonus, Account Manager, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Other Sales - Salary Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed salary information for other sales roles.
- **Cell Range**: A418:FS524
- **Layout Structure**:
    - **Row Headers Location**: B420:B524
    - **Column Headers Location**: J3:Q3, CJ3:FS3
    - **Data Range**:
      - Annual data: J424:Q524
      - Monthly data: CJ424:FS524
- **Time Series Details**:
    - Annual: 2020 to 2027 (J3:Q3)
    - Monthly: 2020-01-31 to 2027-12-31 (CJ3:FS3). Anchor points: CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Sales Team, CRO, VP of Sales, Sales Manager, SDR Manager, SDR, Customer Success, Customer Success Manager, Account Manager - Corporate, Account Manager - Financial, Product Specialist - Mgr, Product Specialist, Enablement Manager, Sales - Admin, Sales Operations Manager, Sales Operations, GTM Strategy, Total Sales Salary, Average Employees
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Total Sales Salary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides total sales salary information.
- **Cell Range**: A520:FS524
- **Layout Structure**:
    - **Row Headers Location**: B520:B524
    - **Column Headers Location**: J3:Q3, CJ3:FS3
    - **Data Range**:
      - Annual data: J522:Q524
      - Monthly data: CJ522:FS524
- **Time Series Details**:
    - Annual: 2020 to 2027 (J3:Q3)
    - Monthly: 2020-01-31 to 2027-12-31 (CJ3:FS3). Anchor points: CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Total Sales Salary, Average Employees, Average Salary, Total Wages
- **Notes & Customizations**: Includes both annual and monthly time series data.



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
- **Description & Purpose**: Contains the company name and sheet title.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: Company Name, Sheet Name, Scenario Description
- **Notes & Customizations**: Simple header information.

### Clients Control - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays financial metrics related to client acquisition and churn, broken down by different client size segments.
- **Cell Range**: A7:FS32
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8. Row 7 contains the year, and row 8 contains the month.
    - **Data Range**:
      - Annual data: `E14:Q32`
      - Monthly data: `T14:FS32`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: New Booked ARR per New Client, Churned ARR per Lost Client, % ARR Churn Attributable to Lost Clients, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Data is scaled by 1000. The "x" in column A seems to be a placeholder or indicator.

### Clients Control - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays financial metrics related to client acquisition and churn, broken down by different client size segments.
- **Cell Range**: A35:FS55
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8. Row 7 contains the year, and row 8 contains the month.
    - **Data Range**:
      - Annual data: `E37:Q55`
      - Monthly data: `T37:FS55`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: New Booked ARR per New Client, Churned ARR per Lost Client, % ARR Churn Attributable to Lost Clients, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Data is scaled by 1000. The "x" in column A seems to be a placeholder or indicator.

### Clients Control - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays financial metrics related to client acquisition and churn, broken down by different client size segments.
- **Cell Range**: A58:FS78
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8. Row 7 contains the year, and row 8 contains the month.
    - **Data Range**:
      - Annual data: `E60:Q78`
      - Monthly data: `T60:FS78`
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: New Booked ARR per New Client, Churned ARR per Lost Client, % ARR Churn Attributable to Lost Clients, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Data is scaled by 1000. The "x" in column A seems to be a placeholder or indicator.



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
- **Description & Purpose**: Contains the company name, report title, and scenario.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:Q3, J3:Q3, T3:FS3
    - **Data Range**: E3:I3, J3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: Not explicitly defined, but implied in E3:Q3 and J3:Q3. Date range is not specified in the provided data. Frequency is Annual.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Company Name, Report Title, Scenario
- **Notes & Customizations**: Contains both annual and monthly time series.

### Clients Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes key client metrics like beginning clients, new clients, churned clients, and ending clients.
- **Cell Range**: B6:FS11
- **Layout Structure**:
    - **Row Headers Location**: B6:B11
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E8:Q11
      - Monthly data: T8:FS11
- **Time Series Details**:
    - Annual: Date range is not specified in the provided data. Frequency is Annual.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Beginning Clients, New Added, Churned, Ending Clients
- **Notes & Customizations**: Contains both annual and monthly time series.

### Clients Detail - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of client metrics related to financial performance, such as new booked ARR and churned ARR.
- **Cell Range**: B13:FS30
- **Layout Structure**:
    - **Row Headers Location**: B15:B30
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E15:Q30
      - Monthly data: T15:FS30
- **Time Series Details**:
    - Annual: Date range is not specified in the provided data. Frequency is Annual.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: New Booked ARR - New Clients, Clients Added, New Booked ARR per New Client, Churned ARR - Lost Clients, Clients Lost, Churned ARR per Lost Client, Total Churned ARR, Churned ARR Attributable to Lost Clients, % of Churned ARR Attributable to Lost Clients
- **Notes & Customizations**: Contains both annual and monthly time series.

### Client Detail - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of client metrics related to corporate clients.
- **Cell Range**: B32:FS49
- **Layout Structure**:
    - **Row Headers Location**: B34:B49
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E34:Q49
      - Monthly data: T34:FS49
- **Time Series Details**:
    - Annual: Date range is not specified in the provided data. Frequency is Annual.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Beginning Clients, New Added, Churned, Ending Clients, New Booked ARR - New Clients, Clients Added, New Booked ARR per New Client, Churned ARR - Lost Clients, Clients Lost, Churned ARR per Lost Client, Total Churned ARR, Churned ARR Attributable to Lost Clients, % of Churned ARR Attributable to Lost Clients
- **Notes & Customizations**: Contains both annual and monthly time series.

### Client Detail - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of client metrics related to other client types.
- **Cell Range**: B51:FS68
- **Layout Structure**:
    - **Row Headers Location**: B53:B68
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E53:Q68
      - Monthly data: T53:FS68
- **Time Series Details**:
    - Annual: Date range is not specified in the provided data. Frequency is Annual.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Beginning Clients, New Added, Churned, Ending Clients, New Booked ARR - New Clients, Clients Added, New Booked ARR per New Client, Churned ARR - Lost Clients, Clients Lost, Churned ARR per Lost Client, Total Churned ARR, Churned ARR Attributable to Lost Clients, % of Churned ARR Attributable to Lost Clients
- **Notes & Customizations**: Contains both annual and monthly time series. The range `T64:CI64` and `CJ64:FS64` are separate monthly data ranges for "Churned ARR per Lost Client".



====================================================================================================
# SHEET 18: Retention CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Retention CTRL
- **Key Sections Identified**:
    - Header
    - Annual Retention - Financial
    - Evergreen Retention - Financial (Annual Equivalent)
    - Annual Retention - Corporate
    - Annual Retention - Other
    - Evergreen Retention - Other (Annual Equivalent)

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains company name, report name, and scenario description.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: Company Name, Report Name, Scenario Description
- **Notes & Customizations**: Contains the scenario name, such as "1 - Base - $25mm".

### Annual Retention - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention percentages for different revenue scenarios.
- **Cell Range**: A12:Q18
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E7:Q7
    - **Data Range**:
      - Annual data: I15:Q18
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Revenue, Annual Retention % - Financial, "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Evergreen Retention - Financial (Annual Equivalent)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays evergreen retention percentages (annual equivalent) for different revenue scenarios.
- **Cell Range**: A21:Q25
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E7:Q7
    - **Data Range**:
      - Annual data: I22:Q25
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Evergreen Retention % - Financial (Annual Equivalent), "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Annual Retention - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention percentages for different revenue scenarios.
- **Cell Range**: A28:DV32
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E7:Q7, T7:FS7
    - **Data Range**:
      - Annual data: I29:Q32
      - Monthly data: BX28:DV28
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-01 to 2027-12-01 (T7:FS7). Anchor points: T7=2015-01-01, AF7=2016-01-01, AR7=2017-01-01, BD7=2018-01-01, BP7=2019-01-01, CB7=2020-01-01, CN7=2021-01-01, CZ7=2022-01-01, DL7=2023-01-01, DX7=2024-01-01, EJ7=2025-01-01, EV7=2026-01-01, FH7=2027-01-01
    - **Frequency**:
      - Annual
      - Repeating Annual (12 times)
- **Key Components**: Annual Retention % - Corporate, "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Annual Retention - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention percentages for different revenue scenarios.
- **Cell Range**: A35:DV39
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E7:Q7, T7:FS7
    - **Data Range**:
      - Annual data: I36:Q39
      - Monthly data: BX35:DV35
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-01 to 2027-12-01 (T7:FS7). Anchor points: T7=2015-01-01, AF7=2016-01-01, AR7=2017-01-01, BD7=2018-01-01, BP7=2019-01-01, CB7=2020-01-01, CN7=2021-01-01, CZ7=2022-01-01, DL7=2023-01-01, DX7=2024-01-01, EJ7=2025-01-01, EV7=2026-01-01, FH7=2027-01-01
    - **Frequency**:
      - Annual
      - Repeating Annual (12 times)
- **Key Components**: Annual Retention % - Other, "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Evergreen Retention - Other (Annual Equivalent)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays evergreen retention percentages (annual equivalent) for different revenue scenarios.
- **Cell Range**: A42:DV46
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E7:Q7, T7:FS7
    - **Data Range**:
      - Annual data: I43:Q46
      - Monthly data: BX42:DV42
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-01 to 2027-12-01 (T7:FS7). Anchor points: T7=2015-01-01, AF7=2016-01-01, AR7=2017-01-01, BD7=2018-01-01, BP7=2019-01-01, CB7=2020-01-01, CN7=2021-01-01, CZ7=2022-01-01, DL7=2023-01-01, DX7=2024-01-01, EJ7=2025-01-01, EV7=2026-01-01, FH7=2027-01-01
    - **Frequency**:
      - Annual
      - Repeating Annual (12 times)
- **Key Components**: Evergreen Retention % - Other (Annual Equivalent), "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.


====================================================================================================
# SHEET 19: Retention
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Retention
- **Key Sections Identified**:
    - Header
    - Financial Retention Detail
    - Corporate Retention Detail
    - Other Retention Detail
    - Summary Retention Detail

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the data.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:FS3 (Time series data)
    - **Data Range**: E3:I3, J3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: Not explicitly defined in a single range, but implied by the data structure in E3:I3 and J3:Q3. Likely represents 2010-2014 and 2015-2021.
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
        - Frequency: Monthly
- **Key Components**: Company Name, Data Description, Time Series Headers.
- **Notes & Customizations**: Contains both annual and monthly time series data.

### Financial Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Financial segment, including churn and retention percentages.
- **Cell Range**: B8:FS18
- **Layout Structure**:
    - **Row Headers Location**: B8:B18
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E9:Q11, E12:Q12, E15:Q17, E18:Q18
      - Monthly data: T9:FS11, T12:FS12, T15:FS17, T18:FS18
- **Time Series Details**:
    - Annual: E3:Q3 (likely representing 2010-2021)
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
        - Frequency: Monthly
- **Key Components**: Churn, Total Churn, Financial, Blended Retention %.
- **Notes & Customizations**: Data is scaled by 1000.

### Corporate Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Corporate segment.
- **Cell Range**: B23:FS40
- **Layout Structure**:
    - **Row Headers Location**: B25:B40
    - **Column Headers Location**: E3:Q3, T3:FS3, CJ3:FS3
    - **Data Range**:
      - Annual data: E25:Q28, E30:Q31, J33:Q33, J39:Q39, E40:Q40
      - Monthly data: T25:FS28, CJ30:FS31, CI33:FS33, CJ34:FS38, CJ39:FS40, T40:FS40
- **Time Series Details**:
    - Annual: E3:Q3 (likely representing 2010-2021)
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
        - Frequency: Monthly
- **Key Components**: Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal.
- **Notes & Customizations**: Data is scaled by 1000. Contains "Annual Financial Up for Renewal" section with data in J33:Q33 and CI33:FS33.

### Corporate Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Corporate segment.
- **Cell Range**: A42:FS59
- **Layout Structure**:
    - **Row Headers Location**: B44:B59
    - **Column Headers Location**: E3:Q3, T3:FS3, CJ3:FS3
    - **Data Range**:
      - Annual data: E44:Q47, E49:Q50, J52:Q52, J58:Q58, E59:Q59
      - Monthly data: T44:FS47, CJ49:FS50, CI52:FS52, CJ53:FS57, CJ58:FS59, T59:FS59
- **Time Series Details**:
    - Annual: E3:Q3 (likely representing 2010-2021)
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
        - Frequency: Monthly
- **Key Components**: Total Corporate Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal.
- **Notes & Customizations**: Data is scaled by 1000. Contains "Annual Up for Renewal" section with data in J52:Q52 and CI52:FS52.

### Other Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Other segment.
- **Cell Range**: A61:FS78
- **Layout Structure**:
    - **Row Headers Location**: B63:B78
    - **Column Headers Location**: E3:Q3, T3:FS3, CJ3:FS3
    - **Data Range**:
      - Annual data: E63:Q66, E68:Q69, J71:Q71, J77:Q77, E78:Q78
      - Monthly data: T63:FS66, CJ68:FS69, CI71:FS71, CJ72:FS76, CJ77:FS78, T78:FS78
- **Time Series Details**:
    - Annual: E3:Q3 (likely representing 2010-2021)
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-12-31
        - Frequency: Monthly
- **Key Components**: Total Other Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal.
- **Notes & Customizations**: Data is scaled by 1000. Contains "Annual Other Up for Renewal" section with data in J71:Q71 and CI71:FS71.

### Summary Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of retention metrics.
- **Cell Range**: A80:FS86
- **Layout Structure**:
    - **Row Headers Location**: B82:B86
    - **Column Headers Location**: E3:Q3, T3:FS3, CJ3:FS3
    - **Data Range**:
      - Annual data: E82:Q84
      - Monthly data: T82:FS84, CJ86:FS86
- **Time Series Details**:
    - Annual: E3:Q3 (likely representing 2010-2021)
        - Date Range: 2010 to 2021 (estimated)
        - Frequency: Annual
    - Monthly: T3:FS3
        - Date Range: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
        - Frequency: Monthly
- **Key Components**: Up for Renewal, Retention %, Renewed, Churned.
- **Notes & Customizations**: Data is scaled by 1000.



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
- **Description & Purpose**: Contains header information like account type, ASV, effective date, close date, segment, and notes.
- **Cell Range**: A1:M19
- **Layout Structure**:
    - **Row Headers Location**: A1:A19
    - **Column Headers Location**: B1:M1
    - **Data Range**:
      - Annual data: N/A
      - Monthly data: N/A
- **Time Series Details**:
    - **Date Range**: 2011-01-18 to 2022-01-01 (C2:C5759), 1900-01-31 to 2022-01-31 (F2:F7599)
    - **Frequency**: Unordered_column, Unordered_column
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage, Segement Key, Hedge Fund, Financial, Renewal, Renewal - Won, Independent Research Firm, Other, Corporate, Research & Advisory, Broker Partner, Renewal - Lost, Investment Manager (long only), Private Equity, Law Firm, Family Office, Corporate - Agency, Financial (Research/IB), Bank, Regulator, Private Wealth, Endowment, Sell Side (Research/IB), Renewal (contract/email required), Evergreen, Renewal (full term), Renewal (default), Pending Cancel (notice given), Pending Partial Cancel, Renewal (low probability)
- **Notes & Customizations**: Contains a note to update the information by taking the ASV tab on the Sales Worksheet.

### Renewal Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains the actual renewal data, including account type, ASV, effective date, close date, segment, and other related information.
- **Cell Range**: A2:J7599
- **Layout Structure**:
    - **Row Headers Location**: A2:A7599
    - **Column Headers Location**: A1:J1
    - **Data Range**:
      - Annual data: B2:B7599
      - Monthly data: C2:C5759, F2:F7599, H2:H7599, I2:I7599, J2:J7599
- **Time Series Details**:
    - **Date Range**: 2011-01-18 to 2022-01-01 (C2:C5759), 1900-01-31 to 2022-01-31 (F2:F7599)
    - **Frequency**: Unordered_column, Unordered_column
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage
- **Notes & Customizations**: The data is related to the renewal process and includes information about the stage of the renewal.


====================================================================================================
# SHEET 21: Renewal Base
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Renewal Base
- **Key Sections Identified**:
    - Header
    - Renewal Data

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the column headers for the renewal data.
- **Cell Range**: A1:J1
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: A1:J1
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage
- **Notes & Customizations**: None

### Renewal Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains the renewal data for each account, including ASV, effective dates, close dates, and other relevant information.
- **Cell Range**: A2:J1858
- **Layout Structure**:
    - **Row Headers Location**: A2:A1858 (Account Type)
    - **Column Headers Location**: A1:J1
    - **Data Range**:
      - ASV data: B2:B1858
      - AlphaSense Opp #: H2:H1858
      - Effective Date: C2:C1858
      - Close Date: D2:D1858
      - EOM Effective Date: F2:F1858
      - EOM Close Date: G2:G1858
- **Time Series Details**:
    - **Date Range**:
      - Effective Date: 2019-02-01 to 2023-07-01 (C2:C1858)
      - Close Date: 2019-02-01 to 2023-07-01 (D2:D1858)
      - EOM Effective Date: 2019-02-28 to 2023-07-31 (F2:F1858)
      - EOM Close Date: 2019-02-28 to 2023-07-31 (G2:G1858)
    - **Frequency**: Unordered
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage
- **Notes & Customizations**: Effective Date, Close Date, EOM Effective Date, and EOM Close Date are unordered date series.


====================================================================================================
# SHEET 22: Deferred Build
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Deferred Build
- **Key Sections Identified**:
    - Header
    - Deferred Revenue Summary
    - Deferred Revenue Detail
    - Revenue Recognition

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and report title.
- **Cell Range**: B2:FS3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:H3, I3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**: E3:H3, I3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: Not explicitly defined, but implied by the presence of number formatting in E3:H3 and I3:Q3. The years are not explicitly stated in the JSON.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31.
    - **Frequency**: Annual, Monthly
- **Key Components**: Company Name, Report Title, Dates
- **Notes & Customizations**: Contains both annual and monthly time series.

### Deferred Revenue Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the deferred revenue balance and its components.
- **Cell Range**: B6:DV14
- **Layout Structure**:
    - **Row Headers Location**: B6:B14
    - **Column Headers Location**: E3:Q3 (Annual), T3:FS3 (Monthly)
    - **Data Range**:
      - Annual data: E8:Q14
      - Monthly data: T8:DV14
- **Time Series Details**:
    - Annual: Not explicitly defined, but implied by the presence of number formatting in E3:Q3. The years are not explicitly stated in the JSON.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31.
    - **Frequency**: Annual, Monthly
- **Key Components**: ARR, Deferred Beginning Balance, Add (Projected), Recognized as Revenue (Projected), Deferred Ending Balance, % of ARR
- **Notes & Customizations**: Contains both annual and monthly time series. Values are scaled by 1000.

### Deferred Revenue Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of the additions to the deferred revenue balance.
- **Cell Range**: B19:DV29
- **Layout Structure**:
    - **Row Headers Location**: B19:B29
    - **Column Headers Location**: BP3:DV3 (Monthly) - Implied from the monthly date series in the header.
    - **Data Range**: BP22:DV29
- **Time Series Details**:
    - Monthly: 2019-01-31 to 2027-12-31 (BP3:DV3). Anchor points: BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31.
    - **Frequency**: Monthly
- **Key Components**: ARR Added (Bookings, Renewals), Total ARR Added Previous Month, Added to Deferred Revenue Balance (Bookings, Renewals), Total Added to Deferred Revenue Balance
- **Notes & Customizations**: Values are scaled by 1000.

### Revenue Recognition
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the revenue recognized from various sources.
- **Cell Range**: B31:DV34
- **Layout Structure**:
    - **Row Headers Location**: B31:B34
    - **Column Headers Location**: BP3:DV3 (Monthly) - Implied from the monthly date series in the header.
    - **Data Range**: BP32:DV34
- **Time Series Details**:
    - Monthly: 2019-01-31 to 2027-12-31 (BP3:DV3). Anchor points: BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31.
    - **Frequency**: Monthly
- **Key Components**: Revenue, Bookings Revenue Recognized, Renewal Revenue Recognized, Revenue from Deferred Revenue Balance
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 23: Headcount and Salaries CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Headcount and Salaries CTRL
- **Key Sections Identified**:
    - Headcount and Salaries Assumptions
    - Salary Calculations

## 2. Detailed Section Analysis

### Headcount and Salaries Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the headcount and ARR assumptions for various departments within AlphaSense, Inc. It provides a breakdown of headcount added in each period and ARR generated per head, serving as a basis for financial projections.
- **Cell Range**: A12:FS88
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., B12, B15, B17, B18, B19, B20, B21, B22, B25, B28, B29, B30, B31, B32, B35, B38, B39, B40, B41, B42, B45, B48, B49, B50, B51, B52, B55, B58, B59, B60, B61, B62, B65, B67, B68, B75, B76, B77, B78, B79, B82, B84, B85, B86, B87, B88, B90)
    - **Column Headers Location**: Rows 7 and 8. Row 7 contains the years, and Row 8 contains the months.
    - **Data Range**:
      - Annual data: `E17:Q88` (numeric values for annual periods)
      - Monthly data: `T18:FS88` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total Headcount, Executive, Engineering, Product, Marketing, Content, Finance, HR, and Operations, Engineering/Ops - India, ARR per head.
- **Notes & Customizations**: ARR per head is calculated for different departments. Some calculations are based on 2018 or 2019 drivers, indicating a change in methodology over time.

### Salary Calculations
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the salary calculations for various departments within AlphaSense, Inc. It includes average salaries and annual increases, providing a basis for expense projections.
- **Cell Range**: A90:FS152
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., B90, B91, B92, B93, B94, B96, B100, B101, B102, B103, B104, B108, B109, B110, B111, B112, B116, B117, B118, B119, B120, B124, B125, B126, B127, B128, B132, B133, B134, B135, B136, B140, B141, B142, B143, B144, B148, B149, B150, B151, B152)
    - **Column Headers Location**: Rows 7 and 8. Row 7 contains the years, and Row 8 contains the months.
    - **Data Range**:
      - Annual data: `E90:Q152` (numeric values for annual periods)
      - Monthly data: `T100:FS152` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Average Salaries, Annual Increase, Executive Salary, Engineering Salary, Product Salary, Marketing Salary, Content Salary, Finance, HR, Operations Salary, Engineering/Ops - India Salary.
- **Notes & Customizations**: Salary calculations are provided for different departments, with annual increases factored in.



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
- **Description & Purpose**: Provides a summary of headcount across different departments. It's used to track the overall size and composition of the workforce.
- **Cell Range**: B6:FS17
- **Layout Structure**:
    - **Row Headers Location**: B8:B17
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E9:Q17
      - Monthly data: T9:FS17
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Headcount for Executive, Engineering, Product, Sales, Marketing, Content, Finance & Admin, Engineering/Ops - India, Total Headcount.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Memo: Average Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides average headcount across different departments.
- **Cell Range**: B20:FS29
- **Layout Structure**:
    - **Row Headers Location**: B21:B29
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E21:Q29
      - Monthly data: T21:FS29
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Average Headcount for Executive, Engineering, Product, Sales, Marketing, Content, Finance, HR, and Operations, Engineering/Ops - India, Total Headcount.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Salary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides salary information for different departments.
- **Cell Range**: B31:FS41
- **Layout Structure**:
    - **Row Headers Location**: B32:B41
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E32:Q41
      - Monthly data: T32:FS41
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Salary for Executive, Engineering, Product, Sales, Marketing, Content, Finance & Admin, Engineering/Ops - India, Total Salary, Total Salary (excl. India).
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Salary per Head
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides salary per head information for different departments.
- **Cell Range**: B43:FS52
- **Layout Structure**:
    - **Row Headers Location**: B44:B52
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E44:Q52
      - Monthly data: T44:FS52
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Salary per Head for Executive, Engineering, Product, Sales, Marketing, Content, Finance & Admin, Engineering/Ops - India, Total Salary per Head.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Headcount Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed headcount information, including beginning of period, added, and end of period counts.
- **Cell Range**: A54:FS118
- **Layout Structure**:
    - **Row Headers Location**: B59:B118
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E59:Q63, E68:Q72, E77:Q81, E86:Q91, E96:Q100, E105:Q109, E114:Q118
      - Monthly data: U59:FS63, U68:FS72, U77:FS81, T86:FS91, U96:FS100, U105:FS109, U114:FS118
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Beginning of Period, Added, End of Period, ARR per Head, ARR, Net Added.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Salaries Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed salary information, including average employees, average salary, and total wages.
- **Cell Range**: A121:FS194
- **Layout Structure**:
    - **Row Headers Location**: B126:B194
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E126:Q128, E134:Q136, E142:Q144, E150:Q152, E158:Q160, E166:Q168, E174:Q176, G182:Q185, E188:Q194
      - Monthly data: T126:FS128, T134:FS136, T142:FS144, T150:FS152, T158:FS160, T166:FS168, T174:FS176, T182:FS185, T188:FS194
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Average Employees, Average Salary, Total Wages.
- **Notes & Customizations**: Values are scaled by 1000.



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
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: AlphaSense, Inc., Operating Expenses CTRL, 1 - Base - $25mm
- **Notes & Customizations**: None

### Operating Expenses Inputs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains the operating expense inputs, including various cost categories and their corresponding values over time. It allows for scenario planning and expense forecasting.
- **Cell Range**: A7:FS2492
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 7 and 8
    - **Data Range**:
      - Annual data: E9:Q2492 (numeric values for annual periods)
      - Monthly data: T9:FS2492 (numeric values for monthly periods)
- **Time Series Details**:
    - **Annual**: 2015 to 2027 (E7:Q7).
    - **Monthly**: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31, BD9=2018-01-31, BP9=2019-01-31, CB9=2020-01-31, CN9=2021-01-31, CZ9=2022-01-31, DL9=2023-01-31, DX9=2024-01-31, EJ9=2025-01-31, EV9=2026-01-31, FH9=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Other Employee Costs - % of Wages, Travel - % of Wages, Other Costs (Airplane) - % of Wages, Other Facilities Cost - % of Rent, Marketing Cost - Spend per Booked Dollar, Non-Salary G&A Costs per Head, Legal Fees - Yearly $ Amount, Engineering Headcount Growth - 2018B, Other Costs - % YoY Growth, Salaries Working Abroad - % of Wages, Holiday Pay - % of Wages, Additional Holiday Pay - % of Wages, Sick Leave - % of Wages, President's Club - Annual Fee, Other Incentives, Commissions %, Bonus per Head, Benefits - % of Wages, Payroll Taxes - % of Wages, Relocation Fee - Buffer, Contractors, Capitalized Wages - % of Engineering Salaries, Workers Compensation per Employee, Recruiter Fees  - $ per Added Head, Stock Based Compensaiton, Rent Expense per Employee, Professional Services Growth Rate, Web Service Expense per Engineering Employee per Month, Bad Debt Expense % of Revenue, Company Wide Opex Inputs, Rent - Buffer, Rent - Park 215, Rent - NYC - 5th Floor, Rent - NYC - 6th Floor, Rent - Helsinki, Rent - Pune, Rent - Mumbai, Rent - Stamford, Rent - SF, Rent - Boston WeWork, Rent - Chicago WeWork, Rent - London WeWork, Rent - Charleston WeWork, Rent - North Carolina WeWork, CAM, Repairs & Maintenance, Amoritzation of Leasehold Improvements, Utilities, Telephone, Computer & Internet, Insurance, Payroll & Benefit Admin, Postage & Delivery, Furniture, Hardware, Office Supplies, Bank Fees, Fundraising, Miscellaneous, DataFeeds, Penalties, Bad Debt, Depreciation Expense, Amortization of Capitalized R&D, Subsidy Received, Other Income, Income Taxes, Other Taxes, Other Taxes - Non Deductible, Interest Income, Interest Expense, Gain / (Loss) on FX, Sales Opex Monthly Inputs, Product Opex Monthly Inputs, Marketing Opex Monthly Inputs, Finance & People Opex Monthly Inputs, Executive Opex Monthly Inputs, Engineering Opex Monthly Inputs
- **Notes & Customizations**: The section contains both annual and monthly time series data, with many rows representing percentages or cost per employee metrics. Several rows also have "Buffer" in their name, indicating they are used for scenario planning.


====================================================================================================
# SHEET 26: Operating Expenses
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Operating Expenses
- **Key Sections Identified**:
    - Operating Expenses Summary
    - Operating Expenses Detail

## 2. Detailed Section Analysis

### Section Name (Operating Expenses Summary)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of operating expenses, including key categories like People Costs, Travel, Facilities Costs, Marketing, and General & Administrative. It allows for quick overview and comparison of expense trends over time.
- **Cell Range**: B6:FS21
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E11:Q21` (numeric values for annual periods)
      - Monthly data: `T11:FS21` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Operating Expenses, People Costs, Other Employee Costs, Travel, Facilities Costs, Rental Income, Marketing, General and Administrative, Legal, Other Costs, Total Operating Expenses, % YoY Growth.
- **Notes & Customizations**: Expenses are presented in thousands. The "% YoY Growth" calculation starts from column F (2016) for annual data and AF (2016-01-31) for monthly data.

### Section Name (Operating Expenses Detail)
- **Section Type**: Custom P&L
- **Description & Purpose**: Provides a detailed breakdown of operating expenses, drilling down into sub-categories within each major expense area (e.g., People Costs broken down into Salaries, Benefits, Payroll Taxes, etc.). This section allows for granular analysis of cost drivers.
- **Cell Range**: B23:FS231
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E26:Q231` (numeric values for annual periods)
      - Monthly data: `T26:FS231` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Commission, Stock Based Compensation, Bonus, Benefits, Payroll Taxes, Recruiting Fees, Contractors, Capitalized Wages, Cellular Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals, Daily Meal Allowance When Abroad, Business Meals, Internal Events, Rent, CAM, Repairs & Maintenance, Utilities, Telephone, Computer & Internet, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising Fees, Miscellaneous, DataFeeds, Web Service, Penalties, Bad Debt, Headcount.
- **Notes & Customizations**: Expenses are presented in thousands. Some rows have additional calculations or percentages (e.g., "% of Wages", "Marketing Cost per Booking"). There are some rows with split monthly data (e.g. E27:Q27, T27:CI27, CJ27:FS27).


====================================================================================================
# SHEET 27: Content
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Content
- **Key Sections Identified**:
    - Header
    - Content Operating Expenses Summary
    - Total Content People Costs
    - Total Content Other Employee Costs
    - Total Content Travel Costs
    - Total Content Facility Costs
    - Total Content Marketing
    - Total Content General & Admin
    - Total Content Other Costs

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:I3, J3:Q3, T3:FS3
    - **Data Range**: E3:I3, J3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: No explicit annual series, but E3:I3 and J3:Q3 likely represent annual data. No specific date range available. Frequency: Annual (Likely)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31. Frequency: Monthly
- **Key Components**: AlphaSense, Inc., Operating Expenses Reorganization, 1 - Base - $25mm
- **Notes & Customizations**: Contains both annual and monthly time series data.

### Content Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of total content expenses.
- **Cell Range**: A6:Q8
- **Layout Structure**:
    - **Row Headers Location**: A6:B8
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I8:Q8
- **Time Series Details**:
    - Annual: J3:Q3 likely represents annual data. No specific date range available. Frequency: Annual (Likely)
- **Key Components**: Total Content Expense
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content People Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes total people costs associated with content creation.
- **Cell Range**: A10:Q62
- **Layout Structure**:
    - **Row Headers Location**: A10:B62
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I10:Q62
- **Time Series Details**:
    - Annual: J3:Q3 likely represents annual data. No specific date range available. Frequency: Annual (Likely)
- **Key Components**: Total Content People Costs, Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finnish Side Costs, Share Based Compensation
- **Notes & Customizations**: Values are scaled by 1000. Includes various sub-categories of people costs.

### Total Content Other Employee Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes other employee costs associated with content creation.
- **Cell Range**: A113:Q143
- **Layout Structure**:
    - **Row Headers Location**: A113:B143
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I113:Q143
- **Time Series Details**:
    - Annual: J3:Q3 likely represents annual data. No specific date range available. Frequency: Annual (Likely)
- **Key Components**: Total Content Other Employee Costs, Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content Travel Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes travel costs associated with content creation.
- **Cell Range**: A145:Q217
- **Layout Structure**:
    - **Row Headers Location**: A145:B217
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I145:Q217
- **Time Series Details**:
    - Annual: J3:Q3 likely represents annual data. No specific date range available. Frequency: Annual (Likely)
- **Key Components**: Total Content Travel Costs, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content Facility Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes facility costs associated with content creation.
- **Cell Range**: A229:Q264
- **Layout Structure**:
    - **Row Headers Location**: A229:B264
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I229:Q264
- **Time Series Details**:
    - Annual: J3:Q3 likely represents annual data. No specific date range available. Frequency: Annual (Likely)
- **Key Components**: Total Content Facility Costs, Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content Marketing
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes marketing costs associated with content creation.
- **Cell Range**: A266:Q311
- **Layout Structure**:
    - **Row Headers Location**: A266:B311
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I266:Q311
- **Time Series Details**:
    - Annual: J3:Q3 likely represents annual data. No specific date range available. Frequency: Annual (Likely)
- **Key Components**: Total Content Marketing, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content General & Admin
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes general and administrative costs associated with content creation.
- **Cell Range**: A313:Q372
- **Layout Structure**:
    - **Row Headers Location**: A313:B372
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I313:Q372
- **Time Series Details**:
    - Annual: J3:Q3 likely represents annual data. No specific date range available. Frequency: Annual (Likely)
- **Key Components**: Total Content General & Admin, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising, Miscellaneous
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content Other Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes other costs associated with content creation.
- **Cell Range**: A374:Q399
- **Layout Structure**:
    - **Row Headers Location**: A374:B399
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I374:Q399
- **Time Series Details**:
    - Annual: J3:Q3 likely represents annual data. No specific date range available. Frequency: Annual (Likely)
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
- **Description & Purpose**: Contains the company name, report title, and scenario information.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:Q3 (Years), T3:FS3 (Months)
    - **Data Range**: E3:Q3, J3:Q3 (numeric values for annual periods), T3:FS3 (date values for monthly periods)
- **Time Series Details**:
    - Annual: Not specified, but implied by the range E3:Q3 and J3:Q3.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Company Name, Report Title, Scenario.
- **Notes & Customizations**: Contains both annual and monthly time series.

### Engineering Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of total engineering expenses.
- **Cell Range**: A6:Q11
- **Layout Structure**:
    - **Row Headers Location**: B6:B11
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I8:Q11
- **Time Series Details**:
    - Annual: 2019 to 2027 (implied from I3:Q3)
    - **Frequency**: Annual
- **Key Components**: Total Engineering Expense, Total Engineering People Costs, Total Engineering People Costs (excl Cap Wages).
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering People Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering people costs.
- **Cell Range**: A13:Q62
- **Layout Structure**:
    - **Row Headers Location**: B13:B62
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I14:Q15, I19:Q19, I24:Q24, I29:Q29, I34:Q34, I36:Q36, I40:Q40, I44:Q44, I48:Q48, I52:Q52, I56:K56, I57:Q57, I62:Q62
- **Time Series Details**:
    - Annual: 2019 to 2027 (implied from I3:Q3)
    - **Frequency**: Annual
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finnish Side Costs, Share Based Compensation.
- **Notes & Customizations**: Values are scaled by 1000, except for I56:K56.

### Engineering Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of other engineering employee costs.
- **Cell Range**: A113:Q143
- **Layout Structure**:
    - **Row Headers Location**: B113:B143
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I113:Q113, I118:Q118, I123:Q123, I128:Q128, I133:Q133, I138:Q138, I143:Q143
- **Time Series Details**:
    - Annual: 2019 to 2027 (implied from I3:Q3)
    - **Frequency**: Annual
- **Key Components**: Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions.
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Travel Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering travel costs.
- **Cell Range**: A145:Q217
- **Layout Structure**:
    - **Row Headers Location**: B145:B217
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I154:Q154, I163:Q163, I172:Q172, I181:Q181, I190:Q190, I199:Q199, I217:Q217
- **Time Series Details**:
    - Annual: 2019 to 2027 (implied from I3:Q3)
    - **Frequency**: Annual
- **Key Components**: Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Business Meals / Entertainment.
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Facility Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering facility costs.
- **Cell Range**: A229:Q264
- **Layout Structure**:
    - **Row Headers Location**: B229:B264
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I234:Q234, I239:Q239, I244:Q244, I249:Q249, I254:Q254, I259:Q259, I264:Q264
- **Time Series Details**:
    - Annual: 2019 to 2027 (implied from I3:Q3)
    - **Frequency**: Annual
- **Key Components**: Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet.
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Marketing
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering marketing expenses.
- **Cell Range**: A266:Q311
- **Layout Structure**:
    - **Row Headers Location**: B266:B311
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I271:Q271, I276:Q276, I281:Q281, I286:Q286, I291:Q291, I296:Q296, I301:Q301, I306:Q306, I311:Q311
- **Time Series Details**:
    - Annual: 2019 to 2027 (implied from I3:Q3)
    - **Frequency**: Annual
- **Key Components**: Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG.
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering General & Admin
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering general and administrative expenses.
- **Cell Range**: A313:Q357
- **Layout Structure**:
    - **Row Headers Location**: B313:B357
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I316:Q316, I321:Q321, I326:Q326, I329:Q329, I334:Q334, I339:Q339, I344:Q344, I349:Q349, I352:Q352, I357:Q357
- **Time Series Details**:
    - Annual: 2019 to 2027 (implied from I3:Q3)
    - **Frequency**: Annual
- **Key Components**: Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees.
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of other engineering expenses.
- **Cell Range**: A372:Q397
- **Layout Structure**:
    - **Row Headers Location**: B372:B397
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I377:Q377, I382:Q382, I387:Q387, I392:Q392, I397:Q397
- **Time Series Details**:
    - Annual: 2019 to 2027 (implied from I3:Q3)
    - **Frequency**: Annual
- **Key Components**: Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt.
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 29: Executive
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Executive
- **Key Sections Identified**:
    - Header
    - Executive Operating Expenses Summary
    - Executive People Costs
    - Executive Other Employee Costs
    - Executive Travel Costs
    - Executive Facility Costs
    - Executive Marketing
    - Executive General & Admin
    - Executive Other Costs

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description. Provides context for the entire spreadsheet.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:I3, J3:Q3, T3:FS3
    - **Data Range**: E3:I3, J3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: No annual time series detected.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Monthly
- **Key Components**: AlphaSense, Inc., Operating Expenses Reorganization, 1 - Base - $25mm
- **Notes & Customizations**: Contains the title of the report and a scenario description.

### Section Name: Executive Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of total executive expenses.
- **Cell Range**: B6:Q8
- **Layout Structure**:
    - **Row Headers Location**: B6, B8
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I8:Q8
- **Time Series Details**:
    - Annual: No annual time series detected.
    - Monthly: No monthly time series detected in this section.
    - **Frequency**: Annual
- **Date Range**: No explicit dates, but implicitly aligns with the annual columns in I3:Q3.
- **Key Components**: Executive Operating Expenses Summary, Total Executive Expense
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive People Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of executive people costs, including wages, benefits, and other related expenses.
- **Cell Range**: B10:Q62
- **Layout Structure**:
    - **Row Headers Location**: B10, B13:B15, B17, B19, B22, B24, B26, B28, B32, B34, B36, B38, B40, B42, B44, B46, B48, B50, B52, B54, B57, B59, B62
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I14:Q14, I15:Q15, I19:Q19, I24:Q24, I28:Q28, I34:Q34, I36:Q36, I40:Q40, I44:Q44, I48:Q48, I52:Q52, I57:Q57, I62:Q62
- **Time Series Details**:
    - Annual: No annual time series detected.
    - Monthly: No monthly time series detected in this section.
    - **Frequency**: Annual
- **Date Range**: No explicit dates, but implicitly aligns with the annual columns in I3:Q3.
- **Key Components**: Total Executive People Costs, Wages, Executive Wages, Salaries Working Abroad, Executive Salaries Working Abroad, Holiday Pay, Executive Holiday Pay, Additional Holiday Pay, Executive Additional Holiday Pay, Sick Leave, Executive Sick Leave, Commission Expense, Bonus, Executive Bonus, Benefits, Executive Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation, Headcount, Cost Per Head.
- **Notes & Customizations**: Values are scaled by 1000. Includes calculations for % of Wages.

### Section Name: Executive Other Employee Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of other employee costs, including cell phone service, internet, and home office expenses.
- **Cell Range**: B113:Q143
- **Layout Structure**:
    - **Row Headers Location**: B113, B115, B118, B120, B123, B125, B128, B130, B133, B135, B138, B140, B143
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I118:Q118, I123:Q123, I128:Q128, I133:Q133, I138:Q138, I143:Q143
- **Time Series Details**:
    - Annual: No annual time series detected.
    - Monthly: No monthly time series detected in this section.
    - **Frequency**: Annual
- **Date Range**: No explicit dates, but implicitly aligns with the annual columns in I3:Q3.
- **Key Components**: Total Executive Other Employee Costs, Celluar Phone Service, Executive Celluar Phone Service, Home Internet Service, Executive Home Internet Service, Home Office Phone, Executive Home Office Phone, Home Office, Executive Home Office, Membership Dues, Executive Membership Dues, Subscriptions, Executive Subscriptions.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive Travel Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of executive travel costs, including airfare, auto/cab, lodging, and meals.
- **Cell Range**: B145:Q217
- **Layout Structure**:
    - **Row Headers Location**: B145, B151, B154, B160, B163, B169, B172, B178, B181, B187, B190, B196, B199, B205, B208, B214, B217
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I154:Q154, I163:Q163, I172:Q172, I181:Q181, I190:Q190, I199:Q199, I217:Q217
- **Time Series Details**:
    - Annual: No annual time series detected.
    - Monthly: No monthly time series detected in this section.
    - **Frequency**: Annual
- **Date Range**: No explicit dates, but implicitly aligns with the annual columns in I3:Q3.
- **Key Components**: Total Executive Travel Costs, Airfare/Train, Executive Airfare/Train, Auto/Cab, Executive Auto/Cab, Mileage, Executive Mileage, Lodging, Executive Lodging, Travel Internet, Executive Travel Internet, Employee Meals / Entertainment, Executive Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Content Daily Mail Allowance When Abroad, Business Meals / Entertainment, Executive Business Meals / Entertainment.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive Facility Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of executive facility costs, including rent, CAM, and utilities.
- **Cell Range**: B229:Q264
- **Layout Structure**:
    - **Row Headers Location**: B229, B231, B234, B236, B239, B241, B244, B246, B249, B251, B254, B256, B259, B261, B264
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I234:Q234, I239:Q239, I244:Q244, I249:Q249, I254:Q254, I259:Q259, I264:Q264
- **Time Series Details**:
    - Annual: No annual time series detected.
    - Monthly: No monthly time series detected in this section.
    - **Frequency**: Annual
- **Date Range**: No explicit dates, but implicitly aligns with the annual columns in I3:Q3.
- **Key Components**: Total Executive Facility Costs, Rent, Executive Rent, CAM, Executive CAM, Repairs & Maintenance, Executive Repairs & Maintenance, Amortization of Leasehold Improvements, Executive Amortization of Leasehold Improvements, Utilities, Executive Utilities, Telephone, Executive Telephone, Computer & Internet, Executive Computer & Internet.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive Marketing
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of executive marketing expenses, including advertising, research, and events.
- **Cell Range**: B266:Q311
- **Layout Structure**:
    - **Row Headers Location**: B266, B271, B276, B281, B286, B291, B296, B301, B306, B311
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I271:Q271, I276:Q276, I281:Q281, I286:Q286, I291:Q291, I296:Q296, I301:Q301, I306:Q306, I311:Q311
- **Time Series Details**:
    - Annual: No annual time series detected.
    - Monthly: No monthly time series detected in this section.
    - **Frequency**: Annual
- **Date Range**: No explicit dates, but implicitly aligns with the annual columns in I3:Q3.
- **Key Components**: Total Executive Marketing, Advertising & Promotion, Executive Advertising & Promotion, Other Marketing, Executive Other Marketing, Omarketing Research, Executive Omarketing Research, Marketing Events, Executive Marketing Events, Public Relations, Executive Public Relations, Paid Search, Executive Paid Search, Paid Social, Executive Paid Social, Paid Display, Executive Paid Display, Paid SWAG, Executive SWAG.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive General & Admin
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of executive general and administrative expenses, including insurance, payroll admin, and office supplies.
- **Cell Range**: B313:Q353
- **Layout Structure**:
    - **Row Headers Location**: B313, B321, B326, B333, B338, B343, B348, B353
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I321:Q321, I326:Q326, I333:Q333, I338:Q338, I343:Q343, I348:Q348, I353:Q353
- **Time Series Details**:
    - Annual: No annual time series detected.
    - Monthly: No monthly time series detected in this section.
    - **Frequency**: Annual
- **Date Range**: No explicit dates, but implicitly aligns with the annual columns in I3:Q3.
- **Key Components**: Total Executive General & Admin, Payroll & Benefit Admin, Executive Payroll & Benefit Admin, Postage & Delivery, Executive Postage & Delivery, Conference & Meetings, Executive Conference & Meetings, Furniture, Executive Furniture, Hardware, Executive Hardware, Software, Executive Software, Office Supplies, Executive Office Supplies.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive Other Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of other executive costs, including legal fees, data feeds, and web services.
- **Cell Range**: B376:Q399
- **Layout Structure**:
    - **Row Headers Location**: B376, B384, B389, B394, B399
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I384:Q384, I389:Q389, I394:Q394, I399:Q399
- **Time Series Details**:
    - Annual: No annual time series detected.
    - Monthly: No monthly time series detected in this section.
    - **Frequency**: Annual
- **Date Range**: No explicit dates, but implicitly aligns with the annual columns in I3:Q3.
- **Key Components**: Total Executive Other Costs, DataFeeds, Executive DataFeeds, Web Service, Executive Web Service, Penalties, Executive Penalties, Bad Debt, Executive Bad Debt.
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 30: Finance & Admin
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Finance & Admin
- **Key Sections Identified**:
    - Header
    - Finance & Admin Operating Expenses Summary
    - Finance & Admin Employee Costs
    - Finance & Admin Recruiting Fees
    - Finance & Admin Relocation
    - Finance & Admin Contractors
    - Finance & Admin Outsourced R&D
    - Finance & Admin Capitalized R&D
    - Finance & Admin Other Employee Costs
    - Finance & Admin Travel Costs
    - Finance & Admin Facility Costs
    - Finance & Admin Rental Income
    - Finance & Admin Marketing
    - Finance & Admin General & Admin
    - Finance & Admin Other Costs
    - Bad Debt

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the report.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Company Name, Report Title, Scenario Description.
- **Notes & Customizations**: None

### Finance & Admin Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of the total Finance & Admin expenses.
- **Cell Range**: B6:Q11
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I8:Q11`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Total Finance & Admin Expense, Total Finance & Admin Expense (excl Cap Wages), Total Finance & Admin Admin Costs, Total Engineering Admin Costs (excl Cap Wages)
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various employee-related costs for the Finance & Admin department.
- **Cell Range**: B13:Q62
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I14:Q62`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Recruiting Fees
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various recruiting fees for the Finance & Admin department.
- **Cell Range**: B64:Q81
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I81:Q81`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Recruiting Fees, Finance & Admin Recruiting Fees
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Relocation
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the relocation costs for the Finance & Admin department.
- **Cell Range**: B83:Q86
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I86:Q86`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Relocation, Finance & Admin Relocation
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Contractors
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the contractor costs for the Finance & Admin department.
- **Cell Range**: B88:Q92
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I92:Q92`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Contractors, Finance & Admin Contractors
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Outsourced R&D
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the outsourced R&D costs for the Finance & Admin department.
- **Cell Range**: B95:Q98
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I98:Q98`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Outsourced R&D, Finance & Admin Outsourced R&D
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Capitalized R&D
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the capitalized R&D costs for the Finance & Admin department.
- **Cell Range**: B100:Q107
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I101:Q107`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Capitalized Wages, Capitalized Outsourced R&D, Capitalized R&D
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the other employee costs for the Finance & Admin department.
- **Cell Range**: B113:Q143
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I113:Q143`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Travel Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the travel costs for the Finance & Admin department.
- **Cell Range**: B145:Q217
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I154:Q217`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Facility Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the facility costs for the Finance & Admin department.
- **Cell Range**: B229:Q264
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I234:Q264`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Rental Income
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the rental income for the Finance & Admin department.
- **Cell Range**: B266:Q269
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I269:Q269`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Rental Income, Finance & Admin Rental Income
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Marketing
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the marketing expenses for the Finance & Admin department.
- **Cell Range**: B271:Q316
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I276:Q316`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin General & Admin
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the general and administrative expenses for the Finance & Admin department.
- **Cell Range**: B318:Q359
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I321:Q359`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the other costs for the Finance & Admin department.
- **Cell Range**: B361:Q398
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I362:Q398`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
    - **Frequency**: Annual
- **Key Components**: Audit & Tax, Bank Fees, Professional Services, Fundraising, Miscellaneous, Legal Fees, DataFeeds, Web Service, Penalties
- **Notes & Customizations**: Values are scaled by 1000.

### Bad Debt
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the bad debt expenses for the Finance & Admin department.
- **Cell Range**: B400:Q405
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns I through Q
    - **Data Range**:
      - Annual data: `I403:Q405`
- **Time Series Details**:
    - **Date Range**: 2015 to 2021
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
    - Marketing People Costs Breakdown
    - Marketing Other Employee Costs Breakdown
    - Marketing Travel Costs Breakdown
    - Marketing Facility Costs Breakdown
    - Marketing Expenses Breakdown
    - Marketing General & Admin Breakdown
    - Marketing Other Costs Breakdown

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and budget information.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:FS3 (Years and Months)
    - **Data Range**: E3:H3, I3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: E3 to Q3 (Years not specified in JSON, but present)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Company Name, Report Title, Budget Amount
- **Notes & Customizations**: Contains both annual and monthly time series.

### Marketing Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of total marketing expenses.
- **Cell Range**: A6:Q10
- **Layout Structure**:
    - **Row Headers Location**: A6, B6, A10, B10
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I8:Q8, I10:Q10
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Total Marketing Expense, Total Marketing People Costs
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing People Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of marketing people costs, including wages, benefits, and related expenses.
- **Cell Range**: A10:Q62
- **Layout Structure**:
    - **Row Headers Location**: B13:B62
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I14:Q14, I15:Q15, I19:Q19, I24:Q24, I28:Q28, I34:Q34, I36:Q36, I40:Q40, I44:Q44, I48:Q48, I52:Q52, I57:Q57, I62:Q62
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation
- **Notes & Customizations**: Uses a scale of 1000 for the values. Includes "% of Wages" calculations.

### Marketing Other Employee Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of other employee costs, such as phone service, internet, and home office expenses.
- **Cell Range**: A113:Q133
- **Layout Structure**:
    - **Row Headers Location**: B115:B133
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I118:Q118, I123:Q123, I128:Q128, I133:Q133
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Travel Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of travel costs, including airfare, auto, lodging, and meals.
- **Cell Range**: A145:Q217
- **Layout Structure**:
    - **Row Headers Location**: B151:B217
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I154:Q154, I163:Q163, I172:Q172, I181:Q181, I190:Q190, I199:Q199, I217:Q217
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Business Meals / Entertainment
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Facility Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of facility costs, including rent, CAM, and utilities.
- **Cell Range**: A229:Q264
- **Layout Structure**:
    - **Row Headers Location**: B231:B264
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I234:Q234, I239:Q239, I244:Q244, I249:Q249, I254:Q254, I259:Q259, I264:Q264
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Expenses Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of marketing expenses, including advertising, research, and events.
- **Cell Range**: A266:Q299
- **Layout Structure**:
    - **Row Headers Location**: B268:B299
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I271:Q271, I274:Q274, I277:Q277, I280:Q280, I283:Q283, I288:Q288, I291:Q291, I294:Q294, I299:Q299
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing General & Admin Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of general and administrative expenses.
- **Cell Range**: A301:Q330
- **Layout Structure**:
    - **Row Headers Location**: B303:B330
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I304:Q304, I309:Q309, I314:Q314, I322:Q322, I327:Q327, I330:Q330
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Insurance, Payroll & Benefit Admin, Postage & Delivery, Furniture, Hardware, Software
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Other Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of other costs, including legal fees, data feeds, and web services.
- **Cell Range**: A360:Q385
- **Layout Structure**:
    - **Row Headers Location**: B362:B385
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I365:Q365, I370:Q370, I375:Q375, I380:Q380, I385:Q385
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt
- **Notes & Customizations**: Uses a scale of 1000 for the values.



====================================================================================================
# SHEET 32: Product
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Product
- **Key Sections Identified**:
    - Header
    - Product Operating Expenses Summary

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None.
    - **Column Headers Location**: E3:Q3 and T3:FS3
    - **Data Range**: E3:H3, I3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: No annual time series detected in this section.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Monthly
- **Key Components**: Company Name, Report Title, Scenario Description.
- **Notes & Customizations**: Includes a scenario description "1 - Base - $25mm".

### Product Operating Expenses Summary
- **Section Type**: Custom P&L
- **Description & Purpose**: Detailed breakdown of Product Operating Expenses, including people costs, facility costs, marketing expenses, and other costs.
- **Cell Range**: A6:Q398
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: I3:Q3
    - **Data Range**:
      - Annual data: I8:Q398 (numeric values for annual periods)
- **Time Series Details**:
    - Annual: 2019 to 2027
    - **Frequency**: Annual
- **Key Components**: Total Product Expense, Total Product People Costs, Wages, Salaries Working Abroad, Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finnish Side Costs, Share Based Compensation, Recruiting Fees, Relocation, Contractors, Outsourced R&D, Capitalized Wages, Capitalized Outsourced R&D, Capitalized R&D, Total Product Other Employee Costs, Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Total Product Travel Costs, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment, Internal Events, Total Product Facility Costs, Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet, Total Product Marketing, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG, Total Product General & Admin, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising, Miscellaneous, Total Product Other Costs, Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt.
- **Notes & Customizations**: Expenses are broken down by category (People Costs, Facility Costs, Marketing, etc.) and then further broken down into specific line items. Many line items have a "Product" prefix, indicating the allocation of costs to the Product department. Values are scaled by 1000.



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
- **Description & Purpose**: Contains the company name, report title, and date information. Provides context for the entire spreadsheet.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:I3, J3:Q3, T3:FS3
    - **Data Range**: E3:I3, J3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: Not explicitly defined, but ranges E3:I3 and J3:Q3 likely represent annual data.
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
        - Annual: Annual (inferred)
        - Monthly: Monthly
- **Key Components**: AlphaSense, Inc., Operating Expenses Reorganization, 1 - Base - $25mm
- **Notes & Customizations**: Contains both annual and monthly time series data.

### Sales Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of total sales expenses.
- **Cell Range**: A6:Q8
- **Layout Structure**:
    - **Row Headers Location**: B6, B8
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I8:Q8
- **Time Series Details**:
    - Annual: Data spans from I8:Q8
    - **Date Range**: Annual (likely, based on column headers in I3:Q3, but actual years are not provided in the JSON)
    - **Frequency**: Annual (likely)
- **Key Components**: Sales Operating Expenses Summary, Total Sales Expense
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales People Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the costs associated with sales personnel, including wages, benefits, and payroll taxes.
- **Cell Range**: A10:Q62
- **Layout Structure**:
    - **Row Headers Location**: B10:B62
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I10:Q10, I14:Q15, I19:Q19, I24:Q24, I28:Q28, I34:Q34, I36:Q36, I40:Q40, I44:Q44, I48:Q48, I52:Q52, I57:Q57, I62:Q62
- **Time Series Details**:
    - Annual: Data spans from I10:Q62
    - **Date Range**: Annual (likely, based on column headers in I3:Q3, but actual years are not provided in the JSON)
    - **Frequency**: Annual (likely)
- **Key Components**: Total Sales People Costs, Wages, Sales Wages, Salaries Working Abroad, Sales Salaries Working Abroad, Holiday Pay, Sales Holiday Pay, Additional Holiday Pay, Sales Additional Holiday Pay, Sick Leave, Sales Sick Leave, Commission Expense, Bonus, Sales Bonus, Benefits, Sales Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation, Cost Per Head, Sales Worker Compensation
- **Notes & Customizations**: Totals are scaled by 1000. Includes calculations based on "% of Wages".

### Sales Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other employee costs such as cell phone service, home internet, home office expenses, and subscriptions.
- **Cell Range**: A113:Q143
- **Layout Structure**:
    - **Row Headers Location**: B113:B143
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I113:Q113, I118:Q118, I123:Q123, I128:Q128, I133:Q133, I138:Q138, I143:Q143
- **Time Series Details**:
    - Annual: Data spans from I113:Q143
    - **Date Range**: Annual (likely, based on column headers in I3:Q3, but actual years are not provided in the JSON)
    - **Frequency**: Annual (likely)
- **Key Components**: Total Sales Other Employee Costs, Celluar Phone Service, Sales Celluar Phone Service, Home Internet Service, Sales Home Internet Service, Home Office Phone, Sales Home Office Phone, Home Office, Sales Home Office, Membership Dues, Sales Membership Dues, Subscriptions, Sales Subscriptions
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales Travel Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details travel-related costs for the sales team.
- **Cell Range**: A145:Q217
- **Layout Structure**:
    - **Row Headers Location**: B145:B217
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I145:Q145, I154:Q154, I163:Q163, I172:Q172, I181:Q181, I190:Q190, I199:Q199, I208:Q208, I217:Q217
- **Time Series Details**:
    - Annual: Data spans from I145:Q217
    - **Date Range**: Annual (likely, based on column headers in I3:Q3, but actual years are not provided in the JSON)
    - **Frequency**: Annual (likely)
- **Key Components**: Total Sales Travel Costs, Airfare/Train, Sales Airfare/Train, Auto/Cab, Sales Auto/Cab, Mileage, Sales Mileage, Lodging, Sales Lodging, Travel Internet, Sales Travel Internet, Employee Meals / Entertainment, Sales Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Content Daily Mail Allowance When Abroad, Business Meals / Entertainment, Sales Business Meals / Entertainment
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales Facility Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details facility-related costs allocated to the sales team.
- **Cell Range**: A229:Q264
- **Layout Structure**:
    - **Row Headers Location**: B229:B264
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I229:Q229, I234:Q234, I239:Q239, I244:Q244, I249:Q249, I254:Q254, I259:Q259, I264:Q264
- **Time Series Details**:
    - Annual: Data spans from I229:Q264
    - **Date Range**: Annual (likely, based on column headers in I3:Q3, but actual years are not provided in the JSON)
    - **Frequency**: Annual (likely)
- **Key Components**: Total Sales Facility Costs, Rent, Sales Rent, CAM, Sales CAM, Repairs & Maintenance, Sales Repairs & Maintenance, Amortization of Leasehold Improvements, Sales Amortization of Leasehold Improvements, Utilities, Sales Utilities, Telephone, Sales Telephone, Computer & Internet, Sales Computer & Internet
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales Marketing
- **Section Type**: Standard P&L
- **Description & Purpose**: Details marketing expenses for the sales team.
- **Cell Range**: A266:Q311
- **Layout Structure**:
    - **Row Headers Location**: B266:B311
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I266:Q266, I271:Q271, I276:Q276, I281:Q281, I286:Q286, I291:Q291, I296:Q296, I301:Q301, I306:Q306, I311:Q311
- **Time Series Details**:
    - Annual: Data spans from I266:Q311
    - **Date Range**: Annual (likely, based on column headers in I3:Q3, but actual years are not provided in the JSON)
    - **Frequency**: Annual (likely)
- **Key Components**: Total Sales Marketing, Advertising & Promotion, Sales Advertising & Promotion, Other Marketing, Sales Other Marketing, Omarketing Research, Sales Omarketing Research, Marketing Events, Sales Marketing Events, Public Relations, Sales Public Relations, Paid Search, Sales Paid Search, Paid Social, Sales Paid Social, Paid Display, Sales Paid Display, Paid SWAG, Sales SWAG
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales General & Admin
- **Section Type**: Standard P&L
- **Description & Purpose**: Details general and administrative expenses allocated to the sales team.
- **Cell Range**: A313:Q350
- **Layout Structure**:
    - **Row Headers Location**: B313:B350
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I313:Q313, I321:Q321, I326:Q326, I329:Q329, I334:Q334, I339:Q339, I350:Q350
- **Time Series Details**:
    - Annual: Data spans from I313:Q350
    - **Date Range**: Annual (likely, based on column headers in I3:Q3, but actual years are not provided in the JSON)
    - **Frequency**: Annual (likely)
- **Key Components**: Total Sales General & Admin, Insurance, Sales Insurance, Payroll & Benefit Admin, Sales Payroll & Benefit Admin, Postage & Delivery, Sales Postage & Delivery, Conferences & Meetings, Sales Conference & Meetings, Furniture, Sales Furniture, Hardware, Sales Hardware, Software, Sales Software
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other costs allocated to the sales team.
- **Cell Range**: A380:Q405
- **Layout Structure**:
    - **Row Headers Location**: B380:B405
    - **Column Headers Location**: I3:Q3
    - **Data Range**: I380:Q380, I385:Q385, I390:Q390, I395:Q395, I400:Q400, I405:Q405
- **Time Series Details**:
    - Annual: Data spans from I380:Q405
    - **Date Range**: Annual (likely, based on column headers in I3:Q3, but actual years are not provided in the JSON)
    - **Frequency**: Annual (likely)
- **Key Components**: Total Sales Other Costs, Legal Fees, Sales Legal Fees, DataFeeds, Sales DataFeeds, Web Service, Sales Web Service, Penalties, Sales Penalties, Bad Debt, Sales Bad Debt
- **Notes & Customizations**: Totals are scaled by 1000.


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
    - Commissions Expense

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
- **Description & Purpose**: Provides a summary of commissions expense, including bonus expense and total commission expense. It also includes bookings data and commission percentages.
- **Cell Range**: A6:FS24
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G6:Q6 (Annual), AR6:FS6 (Monthly)
    - **Data Range**:
      - Annual data: `G8:Q24`
      - Monthly data: `AR8:FS24`
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but likely 2015 to 2021 based on column count.
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Commissions Expense, Bonus Expense, Total Commission Expense, Financial Bookings, Corporate Bookings, Other Bookings, Commission Percentages, Financial Commission, Corporate Commission, Other Commission, Sales Manager Commission.
- **Notes & Customizations**: Data is scaled by 1000.

### Financial Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of financial commissions over time.
- **Cell Range**: B26:FS162
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Column C, AR3:FS3 (Monthly)
    - **Data Range**:
      - Monthly data: `AR30:FS161`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Data is scaled by 1000.

### Corporate Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of corporate commissions over time.
- **Cell Range**: B165:FS301
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Column C, AR3:FS3 (Monthly)
    - **Data Range**:
      - Monthly data: `AR169:FS300`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Data is scaled by 1000.

### Other Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of other commissions over time.
- **Cell Range**: B304:FS440
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Column C, AR3:FS3 (Monthly)
    - **Data Range**:
      - Monthly data: `AR308:FS439`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Data is scaled by 1000.

### AE Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of AE commissions over time.
- **Cell Range**: B443:FS579
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Column C, AR3:FS3 (Monthly)
    - **Data Range**:
      - Monthly data: `AR447:FS578`
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: Months, Commission values
- **Notes & Customizations**: Data is scaled by 1000.

### Commissions Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of commissions expense, including bonus expense and total commission expense.
- **Cell Range**: B581:FS583
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: G6:Q6 (Annual), AR6:FS6 (Monthly)
    - **Data Range**:
      - Annual data: `G581:Q583`
      - Monthly data: `AR581:FS583`
- **Time Series Details**:
    - **Date Range**:
      - Annual: Not explicitly defined, but likely 2015 to 2021 based on column count.
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Commissions Expense, Bonus Expense, Total Commission Expense
- **Notes & Customizations**: Data is scaled by 1000.



====================================================================================================
# SHEET 35: Bad Debt
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Bad Debt
- **Key Sections Identified**:
    - Reconciliation Header
    - AFDA Reconciliation

## 2. Detailed Section Analysis

### Section Name (Reconciliation Header)
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the reconciliation.
- **Cell Range**: B2:CT2
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: B2
- **Time Series Details**: None
- **Key Components**: Title: "ADFDA Reconciliation 2020"
- **Notes & Customizations**: None

### Section Name (AFDA Reconciliation)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section reconciles the Allowance for Doubtful Accounts (AFDA) balance between two sources (WP and Intacct) over a monthly time series.
- **Cell Range**: B5:CT21
- **Layout Structure**:
    - **Row Headers Location**: B6:B21
    - **Column Headers Location**: C5:CT5
    - **Data Range**: C6:CT21
- **Time Series Details**:
    - **Date Range**: 2020-01-01 to 2027-12-01 (C5:CT5). Anchor points: C5=2020-01-01, O5=2021-01-01, AA5=2022-01-01, AM5=2023-01-01, AY5=2024-01-01, BK5=2025-01-01, BW5=2026-01-01, CI5=2027-01-01
    - **Frequency**: Monthly
- **Key Components**: ADFA beg balance per WP, ADFA beg balance per Intacct, Invoices written-off/collected, AFDA balance before adj, A/R ending balance per Intacct, AFDA as % of A/R to be maintained, Amount to be added to AFDA, AFDA end balance per WP, ADFA end balance per Intacct, Difference.
- **Notes & Customizations**: Values are scaled by 1000. Includes a calculation for "AFDA as % of A/R to be maintained" and an adjustment to the AFDA balance.



====================================================================================================
# SHEET 36: COGS CTRL
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: COGS CTRL
- **Key Sections Identified**:
    - Header
    - User Percentage Metrics
    - Product Cost Assumptions
    - International Filings Expenses
    - Transcripts Expenses
    - Dow Jones Expenses
    - News & Journals Expenses
    - IDC Expenses
    - Web Service Expenses
    - Other Expenses
    - ASR Expenses
    - Bernstein, Deutsche Bank, Barclays, HSBC, BOA, UBS, Morgan Stanley, Cowen, Autonomous, Evercore, Citi, Credit Suisse, JP Morgan, Raymond James, RBC Revenue Share and Minimums
    - WSI FactSet Controls

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and the title of the spreadsheet.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: AlphaSense, Inc., Cost of Goods Sold CTRL, 1 - Base - $25mm
- **Notes & Customizations**: None

### User Percentage Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the percentage of users for various categories (Financial, Corporate, Other) across different products and user segments.
- **Cell Range**: A12:Q198
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I15:Q198
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Trend of Net Add Users, Financial BRM Users - % of Total Financial Users, Corporate BRM Users - % of Total Corporate Users, Other BRM Users - % of Total Other Users, Financial TR Transcripts Users - % of Total Financial Users, Corporate TR Transcripts Users - % of Total Corporate Users, Other TR Transcripts Users - % of Total Other Users, Financial FactSet Transcripts Users - % of Total Financial Users, Corporate FactSet Transcripts Users - % of Total Corporate Users, Other FactSet Transcripts Users - % of Total Other Users, Financial DJ Users - % of Total Financial, Corporate DJ Users - % of Total Corporate, Other DJ Users - % of Total Other, Financial AMR ($15k Users) - % of Total Financial, Corporate AMR ($15k Users) - % of Total Corporate, Other AMR ($15k Users) - % of Total Other, Financial AMR ($30k Users) - % of Total Financial, Corporate AMR ($30k Users) - % of Total Corporate, Other AMR ($30k Users) - % of Total Other, Financial Lexis Nexis Users - % of Total Financial, Corporate Lexis Nexis Users - % of Total Corporate, Other Lexis Nexis Users - % of Total Other, Financial International Filings Users - % of Total Financial, Corporate International Filings Users - % of Total Corporate, Other International Filings Users - % of Total Other, FactSet RT Users - % of Total Financial, FactSet RT Users - % of Total Corporate, FactSet RT Users - % of Total Other, FactSet AMR Users - % of Total Financial, FactSet AMR Users - % of Total Corporate, FactSet AMR Users - % of Total Other, Broker Partners - % Growth
- **Notes & Customizations**: Data is scaled by 1000.

### Product Cost Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the assumptions used for product costs, including ramp assumptions for global and single-region users, and cost per user for global and single research.
- **Cell Range**: A212:Q459
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I258:Q459
      - Monthly data: BX217:CJ459
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Broker Research Module, Ramp Assumption - Global Users, Ramp Assumption - Global Users Base, Ramp Assumption - Global Users Upside, Ramp Assumption - Single Region Users, Ramp Assumption - Single Region Users Base, Ramp Assumption - Single Region Users Upside, Global Research (1-10) Cost Per User, Global Research (11-50) Cost Per User, Global Research (50+) Cost Per User, Global Research (1-10) % Cost Per User, Global Research (11-50) % Cost Per User, Global Research (50+) % Cost Per User, Single Research (1-10) Cost Per User, Single Research (11-25) Cost Per User, Single Research (26-50) Cost Per User, Single Research (51+) Cost Per User, Single Research (1-10) % Cost Per User, Single Research (11-25) % Cost Per User, Single Research (26-50) % Cost Per User, Single Research (51+) % Cost Per User, TR Minimum, TR New Contract - Minimum Payment, TR New Contract - Minimum Payment Base, TR New Contract - Minimum Payment Upside, TR New Contract - Minimum Users, TR New Contract - Price per Additional User, FactSet Minimum, After Market Research, AMR $15k Cost per User, AMR $30k Cost per User, AMR - % on TR, AMR - % on TR Base, AMR - % on TR Upside, TR AMR Minimum Fee, AMR TR Alternative Cost per User, AMR TR Alternative Cost - Minimum, TR to FactSet AMR Conversion
- **Notes & Customizations**: Data is scaled by 1000.

### International Filings Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with international filings, including percentages, user limits, and prices for different tiers.
- **Cell Range**: A467:CJ552
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I469:Q552
      - Monthly data: BX469:CJ552
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: International Filing Expense - % of Non Paying Brokers, International Filing Expense - Tier 1 User Limit, International Filing Expense - Tier 1 Price, International Filing Expense - Tier 2 User Limit, International Filing Expense - Tier 2 Price, International Filing Expense - Tier 3 User Limit, International Filing Expense - Tier 3 Price, International Filing Expense - Tier 4 User Limit, International Filing Expense - Tier 4 Price, International Filing Expense - Tier 5 User Limit, International Filing Expense - Tier 5 Price, International Filing Expense - Price Per User in Excess
- **Notes & Customizations**: Data is scaled by 1000.

### Transcripts Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with transcripts, including percentages, user limits, and prices for different tiers.
- **Cell Range**: A555:CJ729
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I557:Q729
      - Monthly data: BX557:CJ729
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: TR Transcript Expense - % of Non Paying Brokers, TR Transcript Expense - Tier 1 User Limit, TR Transcript Expense - Tier 1 Price, TR Transcript Expense - Tier 2 User Limit, TR Transcript Expense - Tier 2 Price, TR Transcript Expense - Tier 3 User Limit, TR Transcript Expense - Tier 3 Price, TR Transcript Expense - Tier 4 User Limit, TR Transcript Expense - Tier 4 Price, TR Transcript Expense - Tier 5 User Limit, TR Transcript Expense - Tier 5 Price, TR Transcript Expense - Tier 6 User Limit, TR Transcript Expense - Tier 6 Price, TR Transcript Expense - Tier 7 User Limit, TR Transcript Expense - Tier 7 Price, TR Transcript Expense - Tier 8 User Limit, TR Transcript Expense - Tier 8 Price, TR Transcript Expense - Excess Price, FactSet Transcript Expense - % of Non Paying Brokers, FactSet Transcript Expense - User Limit, FactSet Transcript Expense - Fee Minimum, FactSet Transcript Expense - Global % of Excess Users, FactSet Transcript Expense - Fee per Excess Global User, FactSet Transcript Expense - Regional % of Excess Users, FactSet Transcript Expense - Fee per Excess Regional User
- **Notes & Customizations**: Data is scaled by 1000.

### Dow Jones Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with Dow Jones, including user limits, prices for different tiers, and admin fees.
- **Cell Range**: A732:CJ893
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I734:Q893
      - Monthly data: BP734:CJ893
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Dow Jones - Base, Dow Jones Expense - Fee Minimum, Dow Jones Expense - Tier 1 User Limit, Dow Jones Expense - Tier 1 Price, Dow Jones Expense - Tier 2 User Limit, Dow Jones Expense - Tier 2 Price, Dow Jones Expense - Tier 3 User Limit, Dow Jones Expense - Tier 3 Price, Dow Jones Expense - Admin Fee, Dow Jones Expense - Tier 1 Monthly Fee, Dow Jones Expense - Tier 2 Monthly Fee, Dow Jones Expense - Tier 3 Monthly Fee, Dow Jones Expense - Tier 4 User Limit, Dow Jones Expense - Tier 4 Monthly Fee, Dow Jones Expense - Tier 5 User Limit, Dow Jones Expense - Tier 5 Monthly Fee, Dow Jones Expense - Tier 6 User Limit, Dow Jones Expense - Tier 6 Monthly Fee, Dow Jones Expense - Tier 7 User Limit, Dow Jones Expense - Tier 7 Monthly Fee, Dow Jones Expense - Tier 8 User Limit, Dow Jones Expense - Tier 8 Monthly Fee, Dow Jones Expense - Tier 9 User Limit, Dow Jones Expense - Tier 9 Monthly Fee, Dow Jones Expense - Tier 10 User Limit, Dow Jones Expense - Tier 10 Monthly Fee, Dow Jones Expense - Tier 11 User Limit, Dow Jones Expense - Tier 11 Monthly Fee, Dow Jones Expense - Tier 12 User Limit, Dow Jones Expense - Tier 12 Monthly Fee, Dow Jones Expense - Tier 13 User Limit, Dow Jones Expense - Tier 13 Monthly Fee, Dow Jones Expense - Tier 14 User Limit, Dow Jones Expense - Tier 14 Monthly Fee
- **Notes & Customizations**: Data is scaled by 1000.

### News & Journals Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with News & Journals, including Lexis Nexis fees and user tiers, and Acquire 2 News expenses.
- **Cell Range**: A986:CJ1041
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I988:Q1041
      - Monthly data: BP988:CJ1041
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Lexis Nexis - Base Fee, Lexis Nexis - Base Users, Lexis Nexis - Tier 1 Users, Lexis Nexis - Tier 1 Price per User, Lexis Nexis - Tier 2 Users, Lexis Nexis - Tier 2 Price per User, Lexis Nexis - Tier 3 Price per User, Acquire 2 News Expense
- **Notes & Customizations**: Data is scaled by 1000.

### IDC Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with IDC.
- **Cell Range**: A1044:CJ1050
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I1046:Q1050
      - Monthly data: BP1046:CJ1050
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: IDC Expense
- **Notes & Customizations**: Data is scaled by 1000.

### Web Service Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with Web Service per user.
- **Cell Range**: A1053:CJ1059
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I1055:Q1059
      - Monthly data: BX1055:CJ1059
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Web Service per User
- **Notes & Customizations**: Data is scaled by 1000.

### Other Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with Other Additional Data Sources, including cost per year.
- **Cell Range**: A1061:CJ1081
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I1063:Q1081
      - Monthly data: BX1063:CJ1081
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Other Additional Data Sources - Cost per Year, Other Additional Data Sources - Cost per Year Base, Other Additional Data Sources - Cost per Year Upside
- **Notes & Customizations**: Data is scaled by 1000.

### ASR Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with ASR, including pool contribution per user and direct consumption cost.
- **Cell Range**: A1083:CJ1095
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I1085:Q1095
      - Monthly data: BX1085:CJ1095
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Pool Contribution per User, Direct Consumption Cost
- **Notes & Customizations**: Data is scaled by 1000.

### Bernstein, Deutsche Bank, Barclays, HSBC, BOA, UBS, Morgan Stanley, Cowen, Autonomous, Evercore, Citi, Credit Suisse, JP Morgan, Raymond James, RBC Revenue Share and Minimums
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the usage, revenue share, and minimums for various brokers.
- **Cell Range**: A1097:CJ1378
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I1098:Q1378
      - Monthly data: BX1098:CJ1378
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Bernstein Usage, Deutsche Bank Usage, Barclays Usage, HSBC Usage, BOA Usage, UBS Usage, Morgan Stanley Usage, Cowen Usage, Autonomous Usage, Evercore Usage, Citi Usage, Credit Suisse Usage, JP Morgan Usage, Raymond James Usage, RBC Usage, FactSet AMR Usage, FactSet RT Usage, Bernstein Revenue Share, Deutsche Bank Revenue Share, Barclays Revenue Share, HSBC Revenue Share, BOA Revenue Share, UBS Revenue Share, Morgan Stanley Revenue Share, Cowen Revenue Share, Autonomous Revenue Share, Evercore Revenue Share, Citi Revenue Share, Credit Suisse Revenue Share, JP Morgan Revenue Share, Raymond James Revenue Share, RBC Revenue Share, Bernstein Minimum, Deutsche Bank Minimum, Barclays Minimum, HSBC Minimum, BOA Minimum, UBS Minimum, Morgan Stanley Minimum, Cowen Minimum, Autonomous Minimum, Evercore Minimum, Citi Minimum, Credit Suisse Minimum, JP Morgan Minimum, Raymond James Minimum, RBC Minimum
- **Notes & Customizations**: Data is scaled by 1000.

### WSI FactSet Controls
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the WSI FactSet controls, including new user additions, active users, bookings per user, docs per user, and document costs.
- **Cell Range**: A1380:CJ1590
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 7 (Year), Row 8 (Month)
    - **Data Range**:
      - Annual data: I1380:Q1590
      - Monthly data: BX1380:CJ1590
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T9:FS9). Anchor points: T9=2015-01-31, AF9=2016-01-31, AR9=2017-01-31...
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: WSI New User Additions - Corporate, WSI New User Additions - Financial, % of WSI New User Additions - Corporate (Professional Services), % of WSI New User Additions - Corporate (Pharma & Life Sciences), % of WSI New User Additions - Corporate (Tech, Media & Telecom), % of WSI New User Additions - Corporate (Energy & Utilities), % of WSI New User Additions - Corporate (Retail & Consumer Products), % of WSI New User Additions - Financial (Financial), % of Non-WSI Corporate Users Converted, % of WSI Users Active - Corporate (Professional Services), % of WSI Users Active - Corporate (Pharma & Life Sciences), % of WSI Users Active - Corporate (Tech, Media & Telecom), % of WSI Users Active - Corporate (Energy & Utilities), % of WSI Users Active - Corporate (Retail & Consumer Products), % of WSI Users Active - Financial (Financial), Docs per Active User per Month - (Professional Services), Docs per Active User per Month - (Pharma & Life Sciences), Docs per Active User per Month - (Tech, Media & Telecom), Docs per Active User per Month - (Energy & Utilities), Docs per Active User per Month - (Retail & Consumer Products), Docs per Active User per Month - (Financial), Consumption Reduction, Users Active, Bookings per Active Trialer, Bookings per Internal User, Docs per Active User, Docs per Trail User, Docs per Internal User, Internal Docs Minimum, Reduction, Total Document Minimum, Document Cost - Minimum, Document Cost - Excess, FactSet AMR Minimum, Total FactSet Minimum
- **Notes & Customizations**: Data is scaled by 1000.


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
    - Dow Jones News Expense
    - COGS by Segment
    - COGS Allocation
    - P&L
    - BRM
    - AMR
    - International Filings Expense
    - Transcripts Expense
    - News & Journals Expense
    - IDC Expense
    - Web Service
    - Other Additional Data Sources

## 2. Detailed Section Analysis

### Cost of Goods Sold Summary
- **Section Type**: Standard P&L
- **Description & Purpose**: Summarizes the various components contributing to the Cost of Goods Sold. It provides a high-level overview of expenses related to delivering the company's products and services.
- **Cell Range**: A6:FS24
- **Layout Structure**:
    - **Row Headers Location**: B8:B18
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E8:Q18
      - Monthly data: T8:FS18
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Cost of Goods Sold, Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, IDC, Web Service - Production, Other Data, Total Cost of Goods Sold.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Product Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of various product-related metrics. This section likely breaks down COGS by product category.
- **Cell Range**: A26:FS70
- **Layout Structure**:
    - **Row Headers Location**: B29:B68
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G29:Q70
      - Monthly data: AR29:FS70
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Broker Research, After Market Research, International Filings, Transcripts, News, News and Journals, Other Data, Total.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Product Summary - % of Revenue
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows product-related metrics as a percentage of revenue. This helps in understanding the relative contribution of each product to the overall cost structure.
- **Cell Range**: A72:FS81
- **Layout Structure**:
    - **Row Headers Location**: B74:B81
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G74:Q81
      - Monthly data: AR74:FS81
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, Other Data, Total COGS.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Total User Count
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the total number of users, broken down by category (Financial, Corporate, Other).
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
- **Key Components**: Users, Corporate , Other, Total Users.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Total User Net Adds
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the net additions of users, broken down by category (Financial, Corporate, Other).
- **Cell Range**: A93:FS99
- **Layout Structure**:
    - **Row Headers Location**: B95:B99
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G96:Q99
      - Monthly data: U96:FS99
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Financial, Corporate, Other, Total Users.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Product Detail Net Adds - Live Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of net user additions for live users, categorized by product.
- **Cell Range**: A101:FS191
- **Layout Structure**:
    - **Row Headers Location**: B103:B191
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G103:Q191
      - Monthly data: AS103:FS191 (Note: some rows have data split across multiple ranges, e.g., AS110:AZ110, BB110:BL110, BN110:CH110, CI110:FS110)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: TR Broker Research, Financial , % of  Financial Net Adds, % of  Corporate Net Adds, % of  Other Net Adds, TR Transcripts, Factset Transcripts, Dow Jones, AMR ($15k), AMR ($30k), Lexis Nexis, FactSet RT, FactSet AMR.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series. Monthly data is split across multiple ranges in some rows.

### Product Detail - Live Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of live users, categorized by product.
- **Cell Range**: A193:FS283
- **Layout Structure**:
    - **Row Headers Location**: B195:B283
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G195:Q283
      - Monthly data: AR195:FS283
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: TR Broker Research, Financial , % of Total Financial , % of Total Corporate, % of Total Other, TR Transcripts, Factset Transcripts, Dow Jones, AMR ($15k), AMR ($30k), Lexis Nexis, FactSet RT, FactSet AMR.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### TR Research - New Contract
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the terms and user counts associated with a new contract for TR Research.
- **Cell Range**: B297:FS313
- **Layout Structure**:
    - **Row Headers Location**: B299:B313
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I299:Q313
      - Monthly data: BP299:FS313
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Monthly: 2019-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Minimum Payment, Minimum Users, Minimum Price per User, Excess Over Minimum, Converted to FactSet, Additional TR Users, Price per Additional User, Additional TR Cost, Total TR Research, Total FS RT Users, % of Total Users.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Factset Research
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a breakdown of Factset Research costs and user counts across different user tiers.
- **Cell Range**: B315:CH376
- **Layout Structure**:
    - **Row Headers Location**: B317:B376
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: J317:Q376
      - Monthly data: BP317:CH376 (Note: Some rows have data in C317:D317 and I319:Q319)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Monthly: 2019-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: User Tiers, Cost, <500 Users, 500-750 Users, 750-1,000 Users, 1,000-1,500 Users, 1,500-2,500 Users, 2,500-3,500 Users, 3500-4500, 4500-7500, 7500-10000, 10000-12500, 12500-15000, 15000-20000, 20000-25000, 25000-35000, 35000-50000, 50000-75000, >75,000 Users, Converted from TR, FS RT users, FactSet Users (Average), FS BRM Expense, FactSet Minimum, Total FactSet Expense, Total Broker Research Expense, After Market Research Expense, User count - $15k package, User count - $30k package, TR AMR, TR - User count - $15k package, $15k - % TR, TR - User count - $30k package, $30k - % TR, TR - Co-Sell, Conversion %, AMR - $15k, Cost per User, AMR - $30k, Total TR Expense, FactSet, FS Minimum, FS - User Count, Check, TR Alt - Expense.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Dow Jones News Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses related to Dow Jones News.
- **Cell Range**: B531:FS555
- **Layout Structure**:
    - **Row Headers Location**: B535:B555
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I537:Q555
      - Monthly data: BP537:FS555
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Monthly: 2019-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Base Case, Minimum Fee, User count, Tier 1, Price per User, Tier 2, Tier 3, Tier 4, Tier 5, Admin Fee, Base Case Total.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### COGS by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Breaks down the Cost of Goods Sold by different segments.
- **Cell Range**: B655:FS667
- **Layout Structure**:
    - **Row Headers Location**: B657:B667
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: E658:Q667
      - Monthly data: T658:FS667
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Cost of Goods Sold, Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, IDC, Web Service - Production, Other Data, Total Cost of Goods Sold.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### COGS Allocation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Allocates COGS across different categories or segments.
- **Cell Range**: B693:FS817
- **Layout Structure**:
    - **Row Headers Location**: B693:B817
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G694:Q817
      - Monthly data: AR694:FS817
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: COGS Allocation, AMR Users, % of AMR Users, International Filings Users, % of Filings Users, Transcripts Users, % of Transcripts Users, DJ Users, % of Dow Jones Users, News and Journals Users, % of News and Journals Users, Other COGS, User Allocation, Total COGS.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### P&L
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a simplified Profit & Loss statement.
- **Cell Range**: B675:FS676
- **Layout Structure**:
    - **Row Headers Location**: B675:B676
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G675:Q676
      - Monthly data: AR675:FS676
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: P&L, Check.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### BRM
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to Broker Research Module (BRM).
- **Cell Range**: B679:FS691
- **Layout Structure**:
    - **Row Headers Location**: B681:B691
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G682:Q691
      - Monthly data: AR682:FS691
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: BRM Users, Corporate, Other, Total, % of BRM Users.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### AMR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to After Market Research (AMR).
- **Cell Range**: B699:FS711
- **Layout Structure**:
    - **Row Headers Location**: B701:B711
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G702:Q711
      - Monthly data: AR702:FS711
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: AMR Users, Corporate, Other, Total, % of AMR Users.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### International Filings Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to International Filings.
- **Cell Range**: B721:FS731
- **Layout Structure**:
    - **Row Headers Location**: B721:B731
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G722:Q731
      - Monthly data: AR722:FS731
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: International Filings Users, Corporate, Other, Total, % of Filings Users.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Transcripts Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to Transcripts.
- **Cell Range**: B741:FS751
- **Layout Structure**:
    - **Row Headers Location**: B741:B751
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G742:Q751
      - Monthly data: AR742:FS751
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Transcripts Users, Corporate, Other, Total, % of Transcripts Users.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### News & Journals Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to News & Journals.
- **Cell Range**: B781:FS791
- **Layout Structure**:
    - **Row Headers Location**: B781:B791
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G782:Q791
      - Monthly data: AR782:FS791
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: News and Journals Users, Corporate, Other, Total, % of News and Journals Users.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Dow Jones News Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to Dow Jones News.
- **Cell Range**: B761:FS771
- **Layout Structure**:
    - **Row Headers Location**: B761:B771
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: G762:Q771
      - Monthly data: AR762:FS771
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017 to 2027
      - Monthly: 2017-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: DJ Users, Corporate, Other, Total, % of Dow Jones Users.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### IDC Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to IDC.
- **Cell Range**: B636:FS640
- **Layout Structure**:
    - **Row Headers Location**: B640
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I640:Q640
      - Monthly data: BP640:FS640
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Monthly: 2019-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total IDC.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Web Service
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to Web Service.
- **Cell Range**: B643:FS648
- **Layout Structure**:
    - **Row Headers Location**: B643:B648
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I646:Q648
      - Monthly data: BP646:FS648
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Monthly: 2019-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Web Service.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Other Additional Data Sources
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to Other Additional Data Sources.
- **Cell Range**: B652:FS653
- **Layout Structure**:
    - **Row Headers Location**: B652:B653
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I652:Q653
      - Monthly data: BP652:FS653
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Monthly: 2019-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Other Additional Data Sources.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Factset Research (Upside Case)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a breakdown of Factset Research costs and user counts across different user tiers under an Upside Case scenario.
- **Cell Range**: B558:FS603
- **Layout Structure**:
    - **Row Headers Location**: B560:B603
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I560:Q603
      - Monthly data: BP560:FS603
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Monthly: 2019-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Upside Case, Tier 1, Price, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6, Tier 7, Tier 8, Tier 9, Tier 10, Tier 11, Tier 12, Tier 13, Tier 14, Total Upside Case.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Lexis Nexis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a breakdown of Lexis Nexis costs and user counts across different user tiers.
- **Cell Range**: B609:FS628
- **Layout Structure**:
    - **Row Headers Location**: B612:B628
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I612:Q628
      - Monthly data: BP612:FS628
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Monthly: 2019-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: News & Journals Expense, User count, Base Fees, Base Users, Tier 1, Price per User, Tier 2, Tier 3, Total Lexis Nexis.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### S&P Transcripts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a breakdown of S&P Transcripts costs and user counts across different user tiers.
- **Cell Range**: B510:FS528
- **Layout Structure**:
    - **Row Headers Location**: B512:B528
    - **Column Headers Location**: E3:Q3, T3:FS3
    - **Data Range**:
      - Annual data: I526:Q528
      - Monthly data: CK512:FS528
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2019 to 2027
      - Monthly: 2021-01-31 to 2027-12-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: S&P Transcripts, Up to 4999, 5000 to 5999, 6000 to 6999, 7000 to 7999, 8000 to 8999, 9000 to 9999, >25000, Total Users, User Limit, Minimum, Total S&P Expense, Total Transcript Expense.
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.


====================================================================================================
# SHEET 38: Total FDS Cost
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Total FDS Cost
- **Key Sections Identified**:
    - Summary FDS COGS Expense (FDS Content)
    - FDS Excess Expense
    - Total FDS Spend & Minimum
    - Pool Contribution & Carryover Balance
    - Adjusted FDS COGS Expense

## 2. Detailed Section Analysis

### Section Name (Summary FDS COGS Expense (FDS Content))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the FDS Content expenses, broken down by category. It provides a summary of the costs associated with FDS content creation and management.
- **Cell Range**: B6:DD13
- **Layout Structure**:
    - **Row Headers Location**: B8:B13
    - **Column Headers Location**: D2:K2, M2:DD2
    - **Data Range**:
      - Annual data: D8:K13
      - Monthly data: M8:DD13
- **Time Series Details**:
    - Annual: 2020 to 2027 (D2:K2)
    - Monthly: 2020-01-31 to 2027-12-31 (M2:DD2). Anchor points: M2=2020-01-31, Y2=2021-01-31, AK2=2022-01-31, AW2=2023-01-31, BI2=2024-01-31, BU2=2025-01-31, CG2=2026-01-31, CS2=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Pool Floor, BRM, AMR, Transcripts, M&A, Total
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (FDS Excess Expense)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the FDS Excess expenses, broken down by category. It provides a summary of the costs associated with FDS excess expense.
- **Cell Range**: B15:DD23
- **Layout Structure**:
    - **Row Headers Location**: B15, B17, B19:B22, B23
    - **Column Headers Location**: D2:K2, M2:DD2
    - **Data Range**:
      - Annual data: D15, D19:D23
      - Monthly data: M15, M19:DD23
- **Time Series Details**:
    - Annual: 2020 to 2027 (D2:K2)
    - Monthly: 2020-01-31 to 2027-12-31 (M2:DD2). Anchor points: M2=2020-01-31, Y2=2021-01-31, AK2=2022-01-31, AW2=2023-01-31, BI2=2024-01-31, BU2=2025-01-31, CG2=2026-01-31, CS2=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Pool Floor, BRM, AMR, Transcripts, M&A, Total Excess
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Total FDS Spend & Minimum)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the Total FDS Spend and Minimum.
- **Cell Range**: B25:DD26
- **Layout Structure**:
    - **Row Headers Location**: B25, B26
    - **Column Headers Location**: D2:K2, M2:DD2
    - **Data Range**:
      - Annual data: D25:K26
      - Monthly data: M25:DD26
- **Time Series Details**:
    - Annual: 2020 to 2027 (D2:K2)
    - Monthly: 2020-01-31 to 2027-12-31 (M2:DD2). Anchor points: M2=2020-01-31, Y2=2021-01-31, AK2=2022-01-31, AW2=2023-01-31, BI2=2024-01-31, BU2=2025-01-31, CG2=2026-01-31, CS2=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Total FDS Spend, Total FDS Minimum
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Pool Contribution & Carryover Balance)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the Pool Contribution and Carryover Balance, including Paid, Carryover, and Excess amounts.
- **Cell Range**: B28:DD35
- **Layout Structure**:
    - **Row Headers Location**: B28, B30:B32, B34, B35
    - **Column Headers Location**: D2:K2, M2:DD2
    - **Data Range**:
      - Annual data: D30:K32, D34:K35
      - Monthly data: M30:DD32, M34:DD35
- **Time Series Details**:
    - Annual: 2020 to 2027 (D2:K2)
    - Monthly: 2020-01-31 to 2027-12-31 (M2:DD2). Anchor points: M2=2020-01-31, Y2=2021-01-31, AK2=2022-01-31, AW2=2023-01-31, BI2=2024-01-31, BU2=2025-01-31, CG2=2026-01-31, CS2=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Paid, Carryover, Excess, Carryover Balance, Change in Carryover
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Adjusted FDS COGS Expense)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the Adjusted FDS COGS Expense and related components like AMR Expense.
- **Cell Range**: B37:DD47
- **Layout Structure**:
    - **Row Headers Location**: B37:B39, B41, B43:B47
    - **Column Headers Location**: D2:K2, M2:DD2
    - **Data Range**:
      - Annual data: D37:K39, D43:K47
      - Monthly data: M37:DD39, M43:DD47
- **Time Series Details**:
    - Annual: 2020 to 2027 (D2:K2)
    - Monthly: 2020-01-31 to 2027-12-31 (M2:DD2). Anchor points: M2=2020-01-31, Y2=2021-01-31, AK2=2022-01-31, AW2=2023-01-31, BI2=2024-01-31, BU2=2025-01-31, CG2=2026-01-31, CS2=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: AMR Expense, Change in Carryover, Adjusted AMR Expense, BRM, AMR, Transcripts, M&A, Total
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 39: FDS AMR
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: FDS AMR
- **Key Sections Identified**:
    - Header
    - User Statistics
    - Documents Purchased Statistics
    - Cost Analysis

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report.
- **Cell Range**: B5:DD5
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: D5:K5, M5:DD5
    - **Data Range**: D5:K5, M5:DD5
- **Time Series Details**:
    - **Date Range**: 2020 to 2027 (D5:K5), 2020 to 2027 (M5:DD5)
    - **Frequency**: Annual (D5:K5), Annual (M5:DD5)
- **Key Components**: "FDS AMR"
- **Notes & Customizations**: Scale is in thousands.

### User Statistics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays key user statistics, including total bookings, active users, and active trialer users.
- **Cell Range**: B6:DD24
- **Layout Structure**:
    - **Row Headers Location**: B6:B24
    - **Column Headers Location**: D2:K3, M2:DD3
    - **Data Range**:
      - Annual data: D6:K24
      - Monthly data: M6:DD24
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (D2:K2)
      - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: "% Active", "Total Bookings", "Active Users", "Active Trialer Users", "FDS Entitled AMR Users"
- **Notes & Customizations**: Some values are scaled in thousands.

### Documents Purchased Statistics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents data related to documents purchased by different user types.
- **Cell Range**: B26:DD59
- **Layout Structure**:
    - **Row Headers Location**: B26:B59
    - **Column Headers Location**: D2:K3, M2:DD3
    - **Data Range**:
      - Annual data: D28:K59
      - Monthly data: M28:DD59
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (D2:K2)
      - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: "Active Users", "Active - Documents Purchased", "Trialers - Documents Purchased", "Internal - Documents Purchased", "Total Docs Purchased"
- **Notes & Customizations**: Some values are scaled in thousands.

### Cost Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes document costs, including costs per tier and total costs.
- **Cell Range**: B61:DD89
- **Layout Structure**:
    - **Row Headers Location**: B61:B89
    - **Column Headers Location**: D2:K3, M2:DD3
    - **Data Range**:
      - Annual data: D61:K89
      - Monthly data: M61:DD89
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (D2:K2)
      - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: "Annual Documents Read", "Document Cost - Tier 1", "Total Document Cost", "FactSet AMR Minimum", "Total FactSet AMR Cost", "Rollover Balance", "Excess Over Minimum", "Adjusted Excess", "Total Adjusted FactSet AMR Cost"
- **Notes & Customizations**: Some values are scaled in thousands.



====================================================================================================
# SHEET 40: Direct Broker
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Direct Broker
- **Key Sections Identified**:
    - Overview Metrics
    - Reads Consumption by Broker
    - WSI Broker Expense Detail

## 2. Detailed Section Analysis

### Section Name: Overview Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a high-level overview of key metrics related to AlphaSense's cost of goods sold, including expenses, user activity, and consumption data. It helps track overall performance and efficiency.
- **Cell Range**: B6:Q47
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**: E8:Q47
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**:
    - Bernstein Expense, Deutsche Bank Expense, Barclays Expense, HSBC Expense, BOA Expense, UBS Expense, Morgan Stanley Expense, Cowen Expense, Autonomous Expense, Evercore Expense, Citi Expense, Credit Suisse Expense, JP Morgan Expense, Raymond James Expense, RBC Expense, Direct Consumption Expense, Total WSI, Total Active Users, Cost per User, FS BRM Expense, Total Users, Active Users, Active (%), Total Page Reads, Page Reads per Active User, Contribution per User, Total Pool Contribution ($)
- **Notes & Customizations**: Expenses are scaled by 1000. Cost per user is calculated from column J onwards.

### Section Name: Reads Consumption by Broker
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the reads consumption and percentage of reads consumption by broker. This helps understand which brokers are driving the most usage.
- **Cell Range**: B49:Q95
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**: E51:Q95
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**:
    - Bernstein, Deutsche Bank, Barclays, HSBC, BOA, UBS, Morgan Stanley, Cowen, Autonomous, Evercore, Citi , Credit Suisse , JP Morgan , Raymond James, RBC, Direct Broker, FactSet AMR, FactSet RT, Total
- **Notes & Customizations**: Reads Consumption is displayed in absolute numbers and as a percentage.

### Section Name: WSI Broker Expense Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of expenses associated with each broker, including strategic investment, usage, consumption, revenue share, expense, minimum, and adjusted expense. It helps in understanding the cost structure for each broker.
- **Cell Range**: B97:Q255
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q and T to FS
    - **Data Range**: E101:Q255
- **Time Series Details**:
    - **Date Range**:
        - Annual: 2015 to 2027 (E101:Q255)
        - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
        - Annual
        - Monthly
- **Key Components**:
    - Total Pool Contribution, Direct Broker Expense, Strategic Investment, Usage, Consumption, Revenue Share, Expense, Minimum, Adjusted Expense
- **Notes & Customizations**: Expenses are scaled by 1000. There are two time series: annual data in columns E:Q and monthly data in columns T:FS.


====================================================================================================
# SHEET 41: Additional FDS Content
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Additional FDS Content
- **Key Sections Identified**:
    - FDS RT Expense - User Tier Analysis
    - FDS RT Excess Expense Calculation
    - FDS Transcripts - User Tier Analysis
    - FDS M&A - User Tier Analysis

## 2. Detailed Section Analysis

### FDS RT Expense - User Tier Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total FDS RT (Real-Time) users, their associated costs, and percentage of total users, broken down by user tiers. It provides a snapshot of user distribution and cost allocation across different user segments.
- **Cell Range**: B5:DF34
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Up to 1500", "2000 - 425000", etc.)
    - **Column Headers Location**: C2:DF3. C2 contains "Users", D2 contains "Cost". F3:M3 contains annual dates, O3:DF3 contains monthly dates.
    - **Data Range**:
      - Annual data: C11:D34 (numeric values for annual periods)
      - Monthly data: V11:DF34 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (F3:M3)
      - Monthly: 2020-01-31 to 2027-12-31 (O3:DF3). Anchor points: O3=2020-01-31, AA3=2021-01-31, AM3=2022-01-31, AY3=2023-01-31, BK3=2024-01-31, BW3=2025-01-31, CI3=2026-01-31, CU3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS RT Users, User Tiers, Users, Cost, % of Total Users.
- **Notes & Customizations**: Costs are scaled by 1000.

### FDS RT Excess Expense Calculation
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section calculates the Total FDS RT Excess Expense, adjusting for discounts and pool floors. It aims to determine the minimum excess spend based on user buckets.
- **Cell Range**: B36:DF49
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Total FDS RT Excess Expense", "Pool Floor", "Total Adjusted FDS RT Excess Expense", etc.)
    - **Column Headers Location**: F3:M3 contains annual dates, O3:DF3 contains monthly dates.
    - **Data Range**:
      - Annual data: F36:M49 (numeric values for annual periods)
      - Monthly data: O36:DF49 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (F3:M3)
      - Monthly: 2020-01-31 to 2027-12-31 (O3:DF3). Anchor points: O3=2020-01-31, AA3=2021-01-31, AM3=2022-01-31, AY3=2023-01-31, BK3=2024-01-31, BW3=2025-01-31, CI3=2026-01-31, CU3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS RT Excess Expense, Pool Floor, Discount (%), Discount Adjusted FDS RT Excess Expense, Minimum Excess Spend.
- **Notes & Customizations**: Expenses are scaled by 1000.

### FDS Transcripts - User Tier Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total FDS Transcript users, broken down by user tiers. It provides a snapshot of user distribution across different user segments.
- **Cell Range**: B51:DF80
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Up to 6000", "7001 - 65000", etc.)
    - **Column Headers Location**: C2:DF3. C2 contains "Users", D2 contains "Cost". O3:DF3 contains monthly dates.
    - **Data Range**:
      - Annual data: C57:D78 (numeric values for annual periods)
      - Monthly data: V57:DF78 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (O2:DF2). Anchor points: O2=2020-01-01, AA2=2021-01-01, AM2=2022-01-01, AY2=2023-01-01, BK2=2024-01-01, BW2=2025-01-01, CI2=2026-01-01, CU2=2027-01-01
      - Monthly: 2020-01-31 to 2027-12-31 (O3:DF3). Anchor points: O3=2020-01-31, AA3=2021-01-31, AM3=2022-01-31, AY3=2023-01-31, BK3=2024-01-31, BW3=2025-01-31, CI3=2026-01-31, CU3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS Transcript Users, User Tiers, Users, Cost, % of Total Users, Total FDS Transcripts Excess Expense.
- **Notes & Customizations**: Users are scaled by 1000.

### FDS M&A - User Tier Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total FDS M&A users, broken down by user tiers. It provides a snapshot of user distribution across different user segments.
- **Cell Range**: B83:DF112
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Up to 6000", "TBD")
    - **Column Headers Location**: C2:DF3. C2 contains "Users", D2 contains "Cost". O3:DF3 contains monthly dates.
    - **Data Range**:
      - Annual data: C89:D110 (numeric values for annual periods)
      - Monthly data: V89:DF110 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2020 to 2027 (O2:DF2). Anchor points: O2=2020-01-01, AA2=2021-01-01, AM2=2022-01-01, AY2=2023-01-01, BK2=2024-01-01, BW2=2025-01-01, CI2=2026-01-01, CU2=2027-01-01
      - Monthly: 2020-01-31 to 2027-12-31 (O3:DF3). Anchor points: O3=2020-01-31, AA3=2021-01-31, AM3=2022-01-31, AY3=2023-01-31, BK3=2024-01-31, BW3=2025-01-31, CI3=2026-01-31, CU3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Total FDS M&A Users, User Tiers, Users, Cost, % of Total Users, Total FDS M&A Excess Expense.
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 42: FDS User Growth
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: FDS User Growth
- **Key Sections Identified**:
    - User Summary
    - New WSI Users Additions
    - Non-WSI Corporate Users Converted
    - Non-WSI Users Converted
    - Non-WSI Users Added
    - Non-WSI Net User Change
    - Non-WSI Users by Sector
    - WSI User Additions
    - FDS RT Users Detail

## 2. Detailed Section Analysis

### User Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level overview of user growth and ARR for Corporate and Financial user segments. This section is used to track overall business performance.
- **Cell Range**: B6:DD30
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D8:K30 (numeric values for annual periods)
      - Monthly data: M8:DD30 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Corporate ARR, Financial ARR, Total ARR, Average Corporate Users, Average Financial Users, Total Average Users, Corporate Users at Year End, Financial Users at Year End, Total Users at Year End, Corporate Users (Added), Financial Users (Added), Total Users (Added), Corporate Enabled WSI Users, Financial Enabled WSI Users, Total Enabled WSI Users, % of Corporate Users, % of Financial Users, % of Total Users.
- **Notes & Customizations**: ARR values are scaled by 1000.

### New WSI Users Additions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Breaks down new WSI user additions by product and sector. This section helps understand the drivers of WSI user growth.
- **Cell Range**: B33:DD85
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D38:K85 (numeric values for annual periods)
      - Monthly data: S38:DD85 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Percent of New Users Added by Product (WSI, Non-WSI, Total Corporate, Financial, Total Financial), New Users Added by Product (WSI, Non-WSI, Total Corporate, Financial, Total Financial), Percent of New Users Added (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total), New WSI Users Added by Sector (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Financial - Other, Total), Financial - Other, Total Financial.
- **Notes & Customizations**: User counts are scaled by 1000.

### Non-WSI Corporate Users Converted
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the conversion of Non-WSI Corporate users, providing insights into user migration.
- **Cell Range**: B88:DD97
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D92:K97 (numeric values for annual periods)
      - Monthly data: S92:DD97 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Percent Converted by Sector (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Notes & Customizations**: None.

### Non-WSI Users Converted
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the conversion of Non-WSI users, providing insights into user migration.
- **Cell Range**: B99:DD106
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D101:K106 (numeric values for annual periods)
      - Monthly data: S101:DD106 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Non-WSI Users Converted (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Notes & Customizations**: User counts are scaled by 1000.

### Percent of New Non-WSI Users Added by Sector
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the percentage of new Non-WSI users added by sector.
- **Cell Range**: B108:DD115
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D110:K115 (numeric values for annual periods)
      - Monthly data: S110:DD115 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Percent of New Non-WSI Users Added by Sector (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Notes & Customizations**: None.

### Non-WSI Users Added
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of Non-WSI users added by sector.
- **Cell Range**: B117:DD124
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D119:K124 (numeric values for annual periods)
      - Monthly data: S119:DD124 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Non-WSI Users Added (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Notes & Customizations**: User counts are scaled by 1000.

### Non-WSI Net User Change
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the net change in Non-WSI users by sector.
- **Cell Range**: B126:DD133
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D128:K133 (numeric values for annual periods)
      - Monthly data: S128:DD133 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Non-WSI Net User Change (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Notes & Customizations**: User counts are scaled by 1000.

### Non-WSI Users by Sector
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the total number of Non-WSI users by sector.
- **Cell Range**: B135:DD142
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D137:K142 (numeric values for annual periods)
      - Monthly data: R137:DD142 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Non-WSI Users by Sector (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Notes & Customizations**: User counts are scaled by 1000.

### WSI User Additions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of WSI user additions by sector.
- **Cell Range**: B145:DD159
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D150:K159 (numeric values for annual periods)
      - Monthly data: M150:DD159 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Total Users Added by Sector (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total), Total Users.
- **Notes & Customizations**: User counts are scaled by 1000.

### Total Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the total number of users by product.
- **Cell Range**: B162:DD184
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D167:K184 (numeric values for annual periods)
      - Monthly data: M167:DD184 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Users by Product (Average WSI Enabled Users, Average Non-WSI Users, Total Average Corporate Users, Total Average Financial Users, WSI Enabled Users at Year End, Non-WSI Users at Year End, Total Corporate Users at Year End, Total Financial Users at Year End).
- **Notes & Customizations**: User counts are scaled by 1000.

### Total Enabled Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the total number of enabled users by sector.
- **Cell Range**: B186:DD214
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D188:K214 (numeric values for annual periods)
      - Monthly data: M188:DD214 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Total Enabled Users (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial, Total), Percent of Active Users (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial, Total), Total Active Users (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial, Total).
- **Notes & Customizations**: User counts are scaled by 1000.

### Document Consumption
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks document consumption metrics.
- **Cell Range**: B217:DD258
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D221:K258 (numeric values for annual periods)
      - Monthly data: M221:DD258 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Docs Per Active User per Month (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Financial), Consumpstion Reduction, Docs Per Active User per Month - Reduction (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Financial - Other, Total Docs - Reduction (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial - Other, Total), Total Docs - Unadjusted (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial - Other, Total).
- **Notes & Customizations**: User counts are scaled by 1000.

### FDS RT Users Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks details about FDS RT (Real-Time) users.
- **Cell Range**: B261:DD297
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 2 and 3
    - **Data Range**:
      - Annual data: D265:K297 (numeric values for annual periods)
      - Monthly data: M265:DD297 (numeric values for monthly periods)
- **Time Series Details**:
    - Annual: 2020 to 2027 (D3:K3).
    - Monthly: 2020-01-31 to 2027-12-31 (M3:DD3). Anchor points: M3=2020-01-31, Y3=2021-01-31, AK3=2022-01-31, AW3=2023-01-31, BI3=2024-01-31, BU3=2025-01-31, CG3=2026-01-31, CS3=2027-01-31
    - Frequency: Annual, Monthly
- **Key Components**: Users Added (Corporate, Financial, Total), Percent of New FDS RT Users Added (Corporate, Financial, Total), New FDS RT Users Added by Product (Corporate, Financial, Total), Enabled FDS RT Users (Corporate, Financial, Total Enabled RT Users), Active FDS RT Users (Corporate, Financial, Total Active RT Users), Percent of Active FDS RT Users (Corporate, Financial, Total Percent of Active RT Users).
- **Notes & Customizations**: User counts are scaled by 1000.


====================================================================================================
# SHEET 43: FDS RT Minimums
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: FDS RT Minimums
- **Key Sections Identified**:
    - User Tier Pricing Table

## 2. Detailed Section Analysis

### Section Name (User Tier Pricing Table)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the pricing structure for a product or service based on user tiers. It shows the incremental users, fee per user, total cost, maximum discount, and minimum/maximum total cost (annual and monthly) for each tier. This is used for sales and pricing calculations.
- **Cell Range**: B2:J26
- **Layout Structure**:
    - **Row Headers Location**: B2:B26
    - **Column Headers Location**: B2:J2
    - **Data Range**:
      - User Tiers: B3:B26
      - Incremental Users: C3:C26
      - Fee Per User: D3:D26
      - Total: E3:E26
      - Max Discount: G3:G26
      - Min Total (Annual): H3:H26
      - Max Total: I3:I26
      - Min Total (Monthly): J3:J26
- **Time Series Details**:
    - No time series data detected.
- **Key Components**: User Tiers, Incremental Users, Fee Per User, Total, Max Discount, Min Total (Annual), Max Total, Min Total (Monthly).
- **Notes & Customizations**: The pricing is structured in tiers, with the "Fee Per User" resetting at each tier. The values in ranges D3:E26 and G3:J26 are scaled by 1000.


====================================================================================================
# SHEET 44: Product User Splits
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Product User Splits
- **Key Sections Identified**:
    - Product User Data (Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR ($15k), AMR ($30k), AMR)
    - BRM Data (BRM - Global, BRM - Single)
    - FactSet RT Data
    - FactSet AMR Data
    - FactSet AMR / Active Data
    - FactSet AMR / Trailers Data
    - FactSet AMR / Internal Data
    - FactSet AMR Active Docs Purchased Data
    - FactSet AMR Trialer Docs Purchased Data
    - FactSet AMR Internal Docs Purchased Data

## 2. Detailed Section Analysis

### Product User Data (Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR ($15k), AMR ($30k), AMR)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the product user data split for various products like Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR ($15k), AMR ($30k), and AMR. It tracks the number of users for each product over time.
- **Cell Range**: B5:BP73
- **Layout Structure**:
    - **Row Headers Location**: Column B (B5, B6, B7, ..., B73)
    - **Column Headers Location**: Row 3 (D3:AT3, AV3:BP3)
    - **Data Range**:
      - Monthly data: D6:AT73
      - Monthly data: AV6:BP73
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017-01-31 to 2020-07-31 (D3:AT3). Anchor points: D3=2017-01-31, P3=2018-01-31, AB3=2019-01-31, AN3=2020-01-31
      - Monthly: 2017-01-31 to 2018-09-30 (AV3:BP3)
    - **Frequency**:
      - Monthly
      - Monthly
- **Key Components**: Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR ($15k), AMR ($30k), AMR, Financial, Corporate, Other, Total.
- **Notes & Customizations**: The data is scaled by 1000. There are two separate monthly time series.

### BRM Data (BRM - Global, BRM - Single)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the BRM (Business Relationship Management) data split for Global and Single products. It tracks the number of users for each product over time.
- **Cell Range**: B75:BP87
- **Layout Structure**:
    - **Row Headers Location**: Column B (B75, B76, B77, ..., B87)
    - **Column Headers Location**: Row 3 (D3:AT3, AV3:BP3)
    - **Data Range**:
      - Monthly data: D76:AT87
      - Monthly data: AV76:BP87
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017-01-31 to 2020-07-31 (D3:AT3). Anchor points: D3=2017-01-31, P3=2018-01-31, AB3=2019-01-31, AN3=2020-01-31
      - Monthly: 2017-01-31 to 2018-09-30 (AV3:BP3)
    - **Frequency**:
      - Monthly
      - Monthly
- **Key Components**: BRM - Global, BRM - Single, Total.
- **Notes & Customizations**: The data is scaled by 1000. There are two separate monthly time series.

### FactSet RT Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet RT (Real-Time) data. It tracks the number of users over time.
- **Cell Range**: B89:AT94
- **Layout Structure**:
    - **Row Headers Location**: Column B (B89, B90, B91, ..., B94)
    - **Column Headers Location**: Row 3 (D3:AT3)
    - **Data Range**:
      - Monthly data: AB90:AT94
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017-01-31 to 2020-07-31 (D3:AT3). Anchor points: D3=2017-01-31, P3=2018-01-31, AB3=2019-01-31, AN3=2020-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: FactSet RT, Total.
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR (After Market Research) data. It tracks the number of users over time.
- **Cell Range**: B96:AR101
- **Layout Structure**:
    - **Row Headers Location**: Column B (B96, B97, B98, ..., B101)
    - **Column Headers Location**: Row 3 (D3:AT3)
    - **Data Range**:
      - Monthly data: AK97:AR101
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017-01-31 to 2020-07-31 (D3:AT3). Anchor points: D3=2017-01-31, P3=2018-01-31, AB3=2019-01-31, AN3=2020-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: FactSet AMR, Total.
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR / Active Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR / Active data. It tracks the number of users over time.
- **Cell Range**: B103:AR104
- **Layout Structure**:
    - **Row Headers Location**: Column B (B103, B104)
    - **Column Headers Location**: Row 3 (D3:AT3)
    - **Data Range**:
      - Monthly data: AB104:AR104
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017-01-31 to 2020-07-31 (D3:AT3). Anchor points: D3=2017-01-31, P3=2018-01-31, AB3=2019-01-31, AN3=2020-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: FactSet AMR / Active, Total.
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR / Trailers Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR / Trailers data. It tracks the number of users over time.
- **Cell Range**: B106:AR107
- **Layout Structure**:
    - **Row Headers Location**: Column B (B106, B107)
    - **Column Headers Location**: Row 3 (D3:AT3)
    - **Data Range**:
      - Monthly data: AB107:AR107
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017-01-31 to 2020-07-31 (D3:AT3). Anchor points: D3=2017-01-31, P3=2018-01-31, AB3=2019-01-31, AN3=2020-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: FactSet AMR / Trailers, Total.
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR / Internal Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR / Internal data. It tracks the number of users over time.
- **Cell Range**: B109:AR110
- **Layout Structure**:
    - **Row Headers Location**: Column B (B109, B110)
    - **Column Headers Location**: Row 3 (D3:AT3)
    - **Data Range**:
      - Monthly data: AB110:AR110
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017-01-31 to 2020-07-31 (D3:AT3). Anchor points: D3=2017-01-31, P3=2018-01-31, AB3=2019-01-31, AN3=2020-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: FactSet AMR / Internal, Total.
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR Active Docs Purchased Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR Active Docs Purchased data. It tracks the number of documents purchased over time.
- **Cell Range**: B112:AR113
- **Layout Structure**:
    - **Row Headers Location**: Column B (B112, B113)
    - **Column Headers Location**: Row 3 (D3:AT3)
    - **Data Range**:
      - Monthly data: AB113:AR113
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017-01-31 to 2020-07-31 (D3:AT3). Anchor points: D3=2017-01-31, P3=2018-01-31, AB3=2019-01-31, AN3=2020-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: FactSet AMR Active Docs Purchased, Total.
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR Trialer Docs Purchased Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR Trialer Docs Purchased data. It tracks the number of documents purchased over time.
- **Cell Range**: B115:AR116
- **Layout Structure**:
    - **Row Headers Location**: Column B (B115, B116)
    - **Column Headers Location**: Row 3 (D3:AT3)
    - **Data Range**:
      - Monthly data: AB116:AR116
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017-01-31 to 2020-07-31 (D3:AT3). Anchor points: D3=2017-01-31, P3=2018-01-31, AB3=2019-01-31, AN3=2020-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: FactSet AMR Trialer Docs Purchased, Total.
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR Internal Docs Purchased Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR Internal Docs Purchased data. It tracks the number of documents purchased over time.
- **Cell Range**: B118:AR119
- **Layout Structure**:
    - **Row Headers Location**: Column B (B118, B119)
    - **Column Headers Location**: Row 3 (D3:AT3)
    - **Data Range**:
      - Monthly data: AB119:AR119
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017-01-31 to 2020-07-31 (D3:AT3). Anchor points: D3=2017-01-31, P3=2018-01-31, AB3=2019-01-31, AN3=2020-01-31
    - **Frequency**:
      - Monthly
- **Key Components**: FactSet AMR Internal Docs Purchased, Total.
- **Notes & Customizations**: The data is scaled by 1000.



====================================================================================================
# SHEET 45: TR BRM
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: TR BRM
- **Key Sections Identified**:
    - Tiered Pricing for Financials
    - Tiered Pricing for Corporate
    - Tiered Pricing for Other
    - User Count Summary

## 2. Detailed Section Analysis

### Section Name: Tiered Pricing for Financials
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the pricing and user mix for different tiers of Financial clients over a period of months. It allows for analysis of revenue based on client size and region.
- **Cell Range**: A3:W9
- **Layout Structure**:
    - **Row Headers Location**: A3:D9
    - **Column Headers Location**: E2:W2
    - **Data Range**:
      - Monthly data: F3:W9
- **Time Series Details**:
    - **Date Range**: Jan 17 to Jun 18
    - **Frequency**: Monthly
- **Key Components**: Global Users (1-10), Global Users (11-50), Global Users (51+), Single Region 1-10, Single Region 11-25, Single Region 26-50, Single Region 50+
- **Notes & Customizations**: Pricing is scaled by 1000.

### Section Name: Tiered Pricing for Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the pricing and user mix for different tiers of Corporate clients over a period of months. It allows for analysis of revenue based on client size and region.
- **Cell Range**: A10:W16
- **Layout Structure**:
    - **Row Headers Location**: A10:D16
    - **Column Headers Location**: E2:W2
    - **Data Range**:
      - Monthly data: F10:W16
- **Time Series Details**:
    - **Date Range**: Jan 17 to Jun 18
    - **Frequency**: Monthly
- **Key Components**: Global Users (1-10), Global Users (11-50), Global Users (51+), Single Region 1-10, Single Region 11-25, Single Region 26-50, Single Region 50+
- **Notes & Customizations**: Pricing is scaled by 1000.

### Section Name: Tiered Pricing for Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the pricing and user mix for different tiers of Other clients over a period of months. It allows for analysis of revenue based on client size and region.
- **Cell Range**: A17:W23
- **Layout Structure**:
    - **Row Headers Location**: A17:D23
    - **Column Headers Location**: E2:W2
    - **Data Range**:
      - Monthly data: F17:W23
- **Time Series Details**:
    - **Date Range**: Jan 17 to Jun 18
    - **Frequency**: Monthly
- **Key Components**: Global Users (1-10), Global Users (11-50), Global Users (51+), Single Region 1-10, Single Region 11-25, Single Region 26-50, Single Region 50+
- **Notes & Customizations**: Pricing is scaled by 1000.

### Section Name: User Count Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the user counts for Global research users, Single region users, Financial, Corporate, and Other users over a period of months.
- **Cell Range**: D36:W44
- **Layout Structure**:
    - **Row Headers Location**: D36:D44
    - **Column Headers Location**: F2:W2
    - **Data Range**:
      - Monthly data: F36:W44
- **Time Series Details**:
    - **Date Range**: Jan 17 to Jun 18
    - **Frequency**: Monthly
- **Key Components**: Global research users, Single region users, Financial, Corporate, Other
- **Notes & Customizations**: Pricing is scaled by 1000.



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
- **Description & Purpose**: This section contains monthly data for key metrics such as total firms, total users, and fees. It allows for tracking performance trends over time.
- **Cell Range**: A1:AA18
- **Layout Structure**:
    - **Row Headers Location**: A1:A18
    - **Column Headers Location**: B1:AA2
    - **Data Range**:
      - Monthly data: B3:AA18
- **Time Series Details**:
    - **Date Range**: Jan'17 to Jun'18
    - **Frequency**: Monthly
- **Key Components**: Month, Total Firms, Total users, Fees.
- **Notes & Customizations**: Fees are scaled by 1000.

### Cost Breakdown Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a breakdown of costs into different categories.
- **Cell Range**: G3:AA25
- **Layout Structure**:
    - **Row Headers Location**: G3:G23
    - **Column Headers Location**: J2:AA2
    - **Data Range**:
      - Monthly data: J3:AA23, J25:AA25
- **Time Series Details**:
    - **Date Range**: Jan'17 to Jun'18
    - **Frequency**: Monthly
- **Key Components**: Corporate, $15k, $30k, Financial, Other.
- **Notes & Customizations**: All values are scaled by 1000.


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
- **Description & Purpose**: Contains the monthly date headers for the financial data section.
- **Cell Range**: C1:T1
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: C1:T1
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 2017-02-01 to 2018-06-01 (approximated from the provided data, as the exact dates are not present in the JSON)
    - **Frequency**: Monthly
- **Key Components**: Month and Year labels (e.g., "2017-2 Feb", "2017-3 Mar")
- **Notes & Customizations**: The dates in row 1 are strings and not actual date values.

### Financial Data Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains financial data categorized by "Corporate" and "Other" over a monthly time series.
- **Cell Range**: B3:T9
- **Layout Structure**:
    - **Row Headers Location**: B3:B7, B9
    - **Column Headers Location**: C3:T3
    - **Data Range**:
      - Monthly data: C4:T7, C9:T9
- **Time Series Details**:
    - **Date Range**: 2017-01-31 to 2018-06-30 (C3:T3). Anchor points: C3=2017-01-31
    - **Frequency**: Monthly
- **Key Components**: Corporate, Other, Financial (B4, B5, B6, B7)
- **Notes & Customizations**: The section contains a monthly time series. Row 3 contains the actual date values, while row 1 contains string representations of the month and year.


====================================================================================================
# SHEET 48: DJ
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: DJ
- **Key Sections Identified**:
    - Revenue Breakdown

## 2. Detailed Section Analysis

### Section Name (Revenue Breakdown)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down revenue into different categories (Corporate and Other) over a monthly time series. It allows for analysis of revenue streams and their performance over time.
- **Cell Range**: B2:T7
- **Layout Structure**:
    - **Row Headers Location**: B4, B6
    - **Column Headers Location**: C2
    - **Data Range**:
      - Monthly data: C3:T3, C4:T4, C5:T5, C6:T7
- **Time Series Details**:
    - **Date Range**: 2017-01-01 to 2018-06-01
    - **Frequency**: Monthly
- **Key Components**: Corporate Revenue, Other Revenue, Financial (likely a category or label).
- **Notes & Customizations**: The data includes "Financial" as a string in cells B3 and B5, which might be a category label or a title. The revenue data is presented in a monthly time series format.


====================================================================================================
# SHEET 49: TR Transcripts
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: TR Transcripts
- **Key Sections Identified**:
    - Header
    - Corporate Financial Data
    - Corporate Financial Data (Monthly)

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains labels identifying the type of data presented in the subsequent sections.
- **Cell Range**: B3:B7
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Corporate, Financial, Other, Broker Partner
- **Notes & Customizations**: This section provides labels for the data presented in the annual section.

### Corporate Financial Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents quarterly financial data for Corporate, Financial, Other, and Broker Partner categories.
- **Cell Range**: B3:H8
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 2
    - **Data Range**: C3:H8
- **Time Series Details**:
    - **Date Range**: 2017-Q1 to 2018-Q2
    - **Frequency**: Quarterly
- **Key Components**: Corporate, Financial, Other, Broker Partner
- **Notes & Customizations**: Quarterly data is presented in columns C through H.

### Corporate Financial Data (Monthly)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents monthly financial data for Corporate, Financial, Other, and Broker Partner categories.
- **Cell Range**: B11:T17
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 11
    - **Data Range**: C12:T17
- **Time Series Details**:
    - **Date Range**: 2017-01-01 to 2018-06-01
    - **Frequency**: Monthly
- **Key Components**: Corporate, Financial, Other, Broker Partner
- **Notes & Customizations**: Monthly data is presented in columns C through T.



====================================================================================================
# SHEET 50: FS Transcripts
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: FS Transcripts
- **Key Sections Identified**:
    - Quarterly Data Section
    - Monthly Data Section

## 2. Detailed Section Analysis

### Quarterly Data Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents key financial metrics broken down by quarter. It allows for tracking performance trends on a quarterly basis.
- **Cell Range**: B4:H9
- **Layout Structure**:
    - **Row Headers Location**: B5:B9
    - **Column Headers Location**: C4:H4
    - **Data Range**: C5:H9
- **Time Series Details**:
    - **Date Range**: 2017-Q1 to 2018-Q2
    - **Frequency**: Quarterly
- **Key Components**: Financial, Corporate, Other, Broker Partner
- **Notes & Customizations**: The metrics are categorized into Financial, Corporate, Other, and Broker Partner.

### Monthly Data Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents key financial metrics broken down by month. It allows for tracking performance trends on a monthly basis.
- **Cell Range**: B12:T17
- **Layout Structure**:
    - **Row Headers Location**: B13:B17
    - **Column Headers Location**: C12:T12
    - **Data Range**: C13:T17
- **Time Series Details**:
    - **Date Range**: 2017-01-01 to 2018-06-01
    - **Frequency**: Monthly
- **Key Components**: Financial, Corporate, Other, Broker Partner
- **Notes & Customizations**: The metrics are categorized into Financial, Corporate, Other, and Broker Partner.


====================================================================================================
# SHEET 51: Filings
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Filings
- **Key Sections Identified**:
    - Header
    - Revenue by Segment

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the sheet title and potentially other high-level information.
- **Cell Range**: A1:B1
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: None
- **Notes & Customizations**: This is a simple header section.

### Revenue by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows revenue broken down by different segments (Other, Corporate, Broker Partner) over a period of time. It includes total revenue as well.
- **Cell Range**: B3:T8
- **Layout Structure**:
    - **Row Headers Location**: B3:B7
    - **Column Headers Location**: C2:T2
    - **Data Range**:
      - Annual data: C3:K7
      - Thousands data: L3:N7
      - Monthly data: O3:T7
    - **Total Revenue Range**: C8:T8
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2017-01-01 to 2017-09-01 (C2:K2)
      - Thousands: 2017-10-01 to 2017-12-01 (L2:N2)
      - Monthly: 2018-01-01 to 2018-06-01 (O2:T2)
    - **Frequency**:
      - Annual: Monthly
      - Thousands: Monthly
      - Monthly: Monthly
- **Key Components**: Financial, Other, Corporate, Broker Partner, Total Revenue.
- **Notes & Customizations**: There are three time series within this section: Annual, Thousands, and Monthly. The "Thousands" section appears to be a scaling factor applied to the data. The date series definition indicates a monthly series, but the column headers suggest it's being used to represent different periods within a year.



====================================================================================================
# SHEET 52: Detailed Income Statement
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Detailed Income Statement
- **Key Sections Identified**:
    - Header
    - Revenue Section
    - Cost of Service (COS) Section
    - Expenses Section
    - Other Income Section
    - Taxes Section
    - Interest Section
    - Other Section
    - Personnel Cost Breakdown

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and column headers.
- **Cell Range**: A1:BV3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: F3:BV3
    - **Data Range**: None
- **Time Series Details**:
    - Annual: Not applicable
    - Monthly: Not applicable
    - Frequency: None
- **Key Components**: "Income Statement", "Account Group", "Account Number", "Account Name", "Account Type"
- **Notes & Customizations**: None

### Revenue Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various revenue streams.
- **Cell Range**: A5:BV15
- **Layout Structure**:
    - **Row Headers Location**: A5:E14, A15
    - **Column Headers Location**: F3:BV3
    - **Data Range**:
      - Annual data: F6:G14 (values for 2024, 2025)
      - Monthly data: H6:BV14 (values for monthly periods)
- **Time Series Details**:
    - Annual: 2024 to 2025
    - Monthly: Dates in H3:BV3 (likely spanning several years, but no anchor points provided to determine the exact range).
    - Frequency: Annual, Monthly
- **Key Components**: Revenue, PRM Single Region, PRM Global, BRM Single Region, BRM Global, RMS, Dow Jones News, IDC, Service Revenue, License Revenue, Total Revenue
- **Notes & Customizations**: Revenue streams are broken down by region and product type.

### Cost of Service (COS) Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the costs associated with providing services.
- **Cell Range**: A17:BV27
- **Layout Structure**:
    - **Row Headers Location**: A17:E26, A27
    - **Column Headers Location**: F3:BV3
    - **Data Range**:
      - Annual data: F18:G26 (values for 2024, 2025)
      - Monthly data: H18:BV26 (values for monthly periods)
- **Time Series Details**:
    - Annual: 2024 to 2025
    - Monthly: Dates in H3:BV3 (likely spanning several years, but no anchor points provided to determine the exact range).
    - Frequency: Annual, Monthly
- **Key Components**: Cost of Service, Broker Research, After Market Research, Embargoed Research - FactSet, International Filings, Transcripts, News, News & Journals, IDC, COS, Web Service - Production, Total COS
- **Notes & Customizations**: COS is broken down by specific service offerings.

### Expenses Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various operating expenses.
- **Cell Range**: A33:BV123
- **Layout Structure**:
    - **Row Headers Location**: A33:E122, B53, B62, B74, B83, B95, B111, B115, B123
    - **Column Headers Location**: F3:BV3
    - **Data Range**:
      - Annual data: F35:G122 (values for 2024, 2025)
      - Monthly data: H35:BV122 (values for monthly periods)
- **Time Series Details**:
    - Annual: 2024 to 2025
    - Monthly: Dates in H3:BV3 (likely spanning several years, but no anchor points provided to determine the exact range).
    - Frequency: Annual, Monthly
- **Key Components**: Expenses, People, Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Commission, Bonus, Benefits, Recruiting Fees, Relocation, Contractors, Outsourced R&D, Total People Costs, Other Employee Costs, Cellular Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions, Total Other Employee Costs, Travel, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals, Daily Meal Allowance When Abroad, Business Meals, Internal Events, Total Travel Costs, Facilities Costs, Rent, CAM, Repairs & Maintenance, Utilities, Telephone, Computer & Internet, Total Facilities Costs, Marketing, Advertising & Promotion, Other Marketing, Marketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, SWAG, Total Marketing Costs, General and Administrative, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising fees, Miscellaneous, Total General & Administrative Costs, Legal, Legal Fees, Total Legal Costs, Other Costs, License Expense, DataFeeds, Web Service, Penalties & Settlements, Bad Debt, Total Other Costs
- **Notes & Customizations**: Expenses are categorized into People, Other Employee Costs, Travel, Facilities, Marketing, General & Administrative, Legal, and Other Costs.

### Depreciation & Amortization Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the depreciation and amortization expenses.
- **Cell Range**: B125:BV128
- **Layout Structure**:
    - **Row Headers Location**: B125:D127, B128
    - **Column Headers Location**: F3:BV3
    - **Data Range**:
      - Annual data: F126:G127 (values for 2024, 2025)
      - Monthly data: H126:BV127 (values for monthly periods)
- **Time Series Details**:
    - Annual: 2024 to 2025
    - Monthly: Dates in H3:BV3 (likely spanning several years, but no anchor points provided to determine the exact range).
    - Frequency: Annual, Monthly
- **Key Components**: Depreciation & Amortization, Depreciation Expense, Amortization of Capitalized R&D, Total Depreciation & Amortization
- **Notes & Customizations**: Includes depreciation and amortization of capitalized R&D.

### Other Income Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details any other income streams.
- **Cell Range**: B130:BV133
- **Layout Structure**:
    - **Row Headers Location**: B130:D132, B133
    - **Column Headers Location**: F3:BV3
    - **Data Range**:
      - Annual data: F131:G132 (values for 2024, 2025)
      - Monthly data: H131:BV132 (values for monthly periods)
- **Time Series Details**:
    - Annual: 2024 to 2025
    - Monthly: Dates in H3:BV3 (likely spanning several years, but no anchor points provided to determine the exact range).
    - Frequency: Annual, Monthly
- **Key Components**: Other Income, Subsidy Received, Revenue, Total Other Income
- **Notes & Customizations**: Includes subsidy received.

### Taxes Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various tax expenses.
- **Cell Range**: B135:BV139
- **Layout Structure**:
    - **Row Headers Location**: B135:D138, B139
    - **Column Headers Location**: F3:BV3
    - **Data Range**:
      - Annual data: F136:G138 (values for 2024, 2025)
      - Monthly data: H136:BV138 (values for monthly periods)
- **Time Series Details**:
    - Annual: 2024 to 2025
    - Monthly: Dates in H3:BV3 (likely spanning several years, but no anchor points provided to determine the exact range).
    - Frequency: Annual, Monthly
- **Key Components**: Taxes, Income Taxes, Other Taxes, Other Taxes - Non Deductible, Total Taxes
- **Notes & Customizations**: Includes breakdown of different tax types.

### Interest Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details interest income and expense.
- **Cell Range**: B141:BV144
- **Layout Structure**:
    - **Row Headers Location**: B141:D143, B144
    - **Column Headers Location**: F3:BV3
    - **Data Range**:
      - Annual data: F142:G143 (values for 2024, 2025)
      - Monthly data: H142:BV143 (values for monthly periods)
- **Time Series Details**:
    - Annual: 2024 to 2025
    - Monthly: Dates in H3:BV3 (likely spanning several years, but no anchor points provided to determine the exact range).
    - Frequency: Annual, Monthly
- **Key Components**: Interest, Interest Income, Interest Expense, Interest Net
- **Notes & Customizations**: Calculates net interest.

### Other Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other income and expenses not categorized elsewhere.
- **Cell Range**: B146:BV151
- **Layout Structure**:
    - **Row Headers Location**: B146:D149, A150, B151
    - **Column Headers Location**: F3:BV3
    - **Data Range**:
      - Annual data: F148:G149 (values for 2024, 2025)
      - Monthly data: H148:BV149 (values for monthly periods)
- **Time Series Details**:
    - Annual: 2024 to 2025
    - Monthly: Dates in H3:BV3 (likely spanning several years, but no anchor points provided to determine the exact range).
    - Frequency: Annual, Monthly
- **Key Components**: Other, Capitalized R&D Costs, Gain/Loss on FX, Gain/Loss on Consolidation, Intercompany Revenue / (Expense), FX Net
- **Notes & Customizations**: Includes FX gains/losses and intercompany transactions.

### Net Income Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Calculates the net income/(loss).
- **Cell Range**: A153:BV157
- **Layout Structure**:
    - **Row Headers Location**: A153, A155, A157
    - **Column Headers Location**: F3:BV3
    - **Data Range**: F155:BV155, G157:BV157
- **Time Series Details**:
    - Annual: 2024 to 2025
    - Monthly: Dates in H3:BV3 (likely spanning several years, but no anchor points provided to determine the exact range).
    - Frequency: Annual, Monthly
- **Key Components**: Total Expenses, Net Income/(loss)
- **Notes & Customizations**: Final calculation of net income.

### Personnel Cost Breakdown
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of personnel costs.
- **Cell Range**: D158:AM167
- **Layout Structure**:
    - **Row Headers Location**: D158:D167
    - **Column Headers Location**: F3:AM3
    - **Data Range**: F159:AM167
- **Time Series Details**:
    - Dates in F3:AM3 (likely spanning several years, but no anchor points provided to determine the exact range).
    - Frequency: Monthly
- **Key Components**: Salaries, Commission, Bonus, Benefits, Payroll Taxes, Worker Comp, Recruiting Fees, Relocation, Contractors, Outsourced R&D
- **Notes & Customizations**: Provides a detailed breakdown of personnel costs, likely monthly.


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
    - Liabilities & Equity Total & Check

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report.
- **Cell Range**: A1:A1
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: A1
- **Time Series Details**: None
- **Key Components**: Balance Sheet
- **Notes & Customizations**: None

### Section Name: Assets
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's assets, broken down into current, long-term, and fixed assets.
- **Cell Range**: A4:BV32
- **Layout Structure**:
    - **Row Headers Location**: A4:D30
    - **Column Headers Location**: E3:BV3
    - **Data Range**:
      - Monthly data: F7:BV30
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the JSON, but inferred from the data range F7:BV30. The "Actual" string is present in S2:BV2, suggesting a monthly time series. Assuming the data starts a reasonable period before the "detected_at" date (2025-10-15), a plausible range is 2023-01-31 to 2025-09-30.
    - **Frequency**: Monthly
- **Key Components**: Current Assets (Cash, Accounts Receivable, Prepaid Expenses), Long Term Assets (Other Long Term Assets), Fixed Assets (Capitalized R&D).
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Liabilities
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's liabilities, broken down into current and long-term liabilities.
- **Cell Range**: A34:BV83
- **Layout Structure**:
    - **Row Headers Location**: A34:D82
    - **Column Headers Location**: E3:BV3
    - **Data Range**:
      - Monthly data: F37:BV82
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the JSON, but inferred from the data range F37:BV82. The "Actual" string is present in S2:BV2, suggesting a monthly time series. Assuming the data starts a reasonable period before the "detected_at" date (2025-10-15), a plausible range is 2023-01-31 to 2025-09-30.
    - **Frequency**: Monthly
- **Key Components**: Current Liabilities (Accounts Payable, Accrued Expenses, Deferred Revenue), Long Term Liabilities (Long-term loan from credit institution, Convertible Notes).
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Equity
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's equity accounts.
- **Cell Range**: A87:BV98
- **Layout Structure**:
    - **Row Headers Location**: A87:D97
    - **Column Headers Location**: E3:BV3
    - **Data Range**:
      - Monthly data: F88:BV97
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the JSON, but inferred from the data range F88:BV97. The "Actual" string is present in S2:BV2, suggesting a monthly time series. Assuming the data starts a reasonable period before the "detected_at" date (2025-10-15), a plausible range is 2023-01-31 to 2025-09-30.
    - **Frequency**: Monthly
- **Key Components**: Common Stock, Preferred Series A, Net Income, Retained Earnings.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Liabilities & Equity Total & Check
- **Section Type**: Balance Sheet
- **Description & Purpose**: Calculates the total liabilities and equity and includes a check to ensure the balance sheet balances.
- **Cell Range**: A100:BV101
- **Layout Structure**:
    - **Row Headers Location**: A100:A101
    - **Column Headers Location**: E3:BV3
    - **Data Range**:
      - Monthly data: F100:BV101
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the JSON, but inferred from the data range F100:BV101. The "Actual" string is present in S2:BV2, suggesting a monthly time series. Assuming the data starts a reasonable period before the "detected_at" date (2025-10-15), a plausible range is 2023-01-31 to 2025-09-30.
    - **Frequency**: Monthly
- **Key Components**: Total Liabilities & Equity, Check.
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 54: Detailed Cash Flow Satement
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Detailed Cash Flow Satement
- **Key Sections Identified**:
    - Cash Flow Statement - Operating Activities
    - Cash Flow Statement - Investing Activities
    - Cash Flow Statement - Financing Activities
    - Cash Flow Statement - Reconciliation

## 2. Detailed Section Analysis

### Section Name (Cash Flow Statement - Operating Activities)
- **Section Type**: `Standard Cash Flow Statement`
- **Description & Purpose**: This section details the cash inflows and outflows resulting from the company's core business activities. It starts with Net Income and adjusts for non-cash items and changes in working capital accounts to arrive at Net Cash Flows from Operating Activities.
- **Cell Range**: `A4:BV42`
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 3
    - **Data Range**: `G6:BV40`, `G42:BV42`
- **Time Series Details**:
    - **Date Range**: 2015-01-01 to 2020-08-31 (G3:BV3). Anchor points: G3=2015-01-01, S3=2016-01-01, AE3=2017-01-01, AQ3=2018-01-01, BC3=2019-01-01, BO3=2020-01-01
    - **Frequency**: `Monthly`
- **Key Components**: Net Income, Changes in Operating Assets (Accounts Receivable, etc.), Changes in Operating Liabilities (Accounts Payable, etc.), Depreciation, Amortization, Net Cash Flows from Operating Activities.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name (Cash Flow Statement - Investing Activities)
- **Section Type**: `Standard Cash Flow Statement`
- **Description & Purpose**: This section outlines the cash flows related to the purchase and sale of long-term assets, such as property, plant, and equipment (PP&E) and capitalized research and development.
- **Cell Range**: `A44:BV49`
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 3
    - **Data Range**: `G46:BV47`, `G49:BV49`
- **Time Series Details**:
    - **Date Range**: 2015-01-01 to 2020-08-31 (G3:BV3). Anchor points: G3=2015-01-01, S3=2016-01-01, AE3=2017-01-01, AQ3=2018-01-01, BC3=2019-01-01, BO3=2020-01-01
    - **Frequency**: `Monthly`
- **Key Components**: Fixed Assets, Capitalized R&D, Net Cash Flows from Investing Activities.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name (Cash Flow Statement - Financing Activities)
- **Section Type**: `Standard Cash Flow Statement`
- **Description & Purpose**: This section details the cash flows related to how the company is financed, including debt, equity, and other forms of capital.
- **Cell Range**: `A51:BV77`
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 3
    - **Data Range**: `G53:BV74`, `G77:BV77`
- **Time Series Details**:
    - **Date Range**: 2015-01-01 to 2020-08-31 (G3:BV3). Anchor points: G3=2015-01-01, S3=2016-01-01, AE3=2017-01-01, AQ3=2018-01-01, BC3=2019-01-01, BO3=2020-01-01
    - **Frequency**: `Monthly`
- **Key Components**: Unrealized Subsidy, Short Term Loans, Capital Loans, Long-term loans, SVB Line of Credit, Common Stock, Preferred Series A, Convertible Notes, Retained Earnings, Net Cash Flows from Financing Activities.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name (Cash Flow Statement - Reconciliation)
- **Section Type**: `Standard Cash Flow Statement`
- **Description & Purpose**: This section reconciles the beginning and ending cash balances, showing the net change in cash during the period.
- **Cell Range**: `A80:BV85`
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 3
    - **Data Range**: `G80:BV85`
- **Time Series Details**:
    - **Date Range**: 2015-01-01 to 2020-08-31 (G3:BV3). Anchor points: G3=2015-01-01, S3=2016-01-01, AE3=2017-01-01, AQ3=2018-01-01, BC3=2019-01-01, BO3=2020-01-01
    - **Frequency**: `Monthly`
- **Key Components**: Cash, Beginning of Period, Net Change in Cash, Cash, End of Period.
- **Notes & Customizations**: The data is scaled by 1000. There's an additional "Check" row.



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
    - Cash & Debt
    - SaaS Metrics
    - Contract Duration
    - Deal Metrics
    - Client Counts
    - User Counts
    - Cancels
    - ARR New/Upsell/Increase $
    - Monthly Recurring Revenue

## 2. Detailed Section Analysis

### Section Name (Annual Subscription Value)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the annual subscription value over time, providing a high-level view of the company's recurring revenue.
- **Cell Range**: A4:CG16
- **Layout Structure**:
    - **Row Headers Location**: A4:A16
    - **Column Headers Location**: C4:CG4
    - **Data Range**:
      - Annual data: C6:N16
      - Monthly data: O6:BT16
      - Sales Plan data: BV6:CG16
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2016 (C1, O1)
      - Monthly: 2017 (AA1) to Unknown (BT1)
      - Sales Plan: Unknown (BV1) to Unknown (CG1)
    - **Frequency**:
      - Annual
      - Monthly
      - Sales Plan
- **Key Components**: ARR Added (Gross), New Sales, Upsells, Increases, Financial, Corporate, Other, Corporate as % of Total.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (ARR Added (Gross))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the ARR added (Gross) over time, providing a high-level view of the company's recurring revenue.
- **Cell Range**: A6:CG16
- **Layout Structure**:
    - **Row Headers Location**: A6:A16
    - **Column Headers Location**: C4:CG4
    - **Data Range**:
      - Annual data: C6:N16
      - Monthly data: O6:BT16
      - Sales Plan data: BV6:CG16
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2016 (C1, O1)
      - Monthly: 2017 (AA1) to Unknown (BT1)
      - Sales Plan: Unknown (BV1) to Unknown (CG1)
    - **Frequency**:
      - Annual
      - Monthly
      - Sales Plan
- **Key Components**: ARR Added (Gross), New Sales, Upsells, Increases, Financial, Corporate, Other, Corporate as % of Total.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (ARR Churn)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the ARR Churn over time, providing a high-level view of the company's recurring revenue.
- **Cell Range**: A17:CG21
- **Layout Structure**:
    - **Row Headers Location**: A17:A21
    - **Column Headers Location**: C4:CG4
    - **Data Range**:
      - Monthly data: C17:BT21
      - Sales Plan data: BV17:CG21
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (BT1)
      - Sales Plan: Unknown (BV1) to Unknown (CG1)
    - **Frequency**:
      - Monthly
      - Sales Plan
- **Key Components**: ARR Churn, Uncontrollable, Controllable, % Controllable, % YTD Controllable.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (ARR Churn Notifications)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the ARR Churn Notifications over time, providing a high-level view of the company's recurring revenue.
- **Cell Range**: A27:BT33
- **Layout Structure**:
    - **Row Headers Location**: A27:A33
    - **Column Headers Location**: C4:BT4
    - **Data Range**:
      - Monthly data: O27:BT33
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (BT1)
    - **Frequency**:
      - Monthly
- **Key Components**: ARR Churn Notifications, Budget/Firm Downsizing, Competitor, Insufficient value, Low use/engagement, User(s) left firm, Other.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (# of Client Firms)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of client firms over time.
- **Cell Range**: A35:BT37
- **Layout Structure**:
    - **Row Headers Location**: A35:A37
    - **Column Headers Location**: C4:BT4
    - **Data Range**:
      - Monthly data: C35:BT37
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (BT1)
    - **Frequency**:
      - Monthly
- **Key Components**: # of Client Firms, # of Client Firms Added, # of Client Firms Lost.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (# of Users)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of users over time.
- **Cell Range**: A39:BT41
- **Layout Structure**:
    - **Row Headers Location**: A39:A41
    - **Column Headers Location**: C4:BT4
    - **Data Range**:
      - Monthly data: C39:BT41
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (BT1)
    - **Frequency**:
      - Monthly
- **Key Components**: # of Users, # of Gross Users Added, # of Gross Users Lost.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Cash & Debt)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks cash and debt levels over time.
- **Cell Range**: A43:CG44
- **Layout Structure**:
    - **Row Headers Location**: A43:A44
    - **Column Headers Location**: I43:CG43
    - **Data Range**:
      - Annual data: I43:S43
      - Monthly data: T43:AR44
      - Sales Plan data: BV43:CG43
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to Unknown (S1)
      - Monthly: Unknown (T1) to Unknown (AR1)
      - Sales Plan: Unknown (BV1) to Unknown (CG1)
    - **Frequency**:
      - Annual
      - Monthly
      - Sales Plan
- **Key Components**: Cash, SVB Debt.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (SaaS Metrics)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks various SaaS metrics related to ARR and churn.
- **Cell Range**: A46:BT68
- **Layout Structure**:
    - **Row Headers Location**: A46:B68
    - **Column Headers Location**: C4:BT4
    - **Data Range**:
      - Monthly data: C47:BT68
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (BT1)
    - **Frequency**:
      - Monthly
- **Key Components**: ARR, Churn, Total Churn $, Total Churn %, Rolling 12 Month Churn %, Customer Churn %, Net Churn % (Rolling 12m), Net Retention % (Rolling 12m).
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Contract Duration)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks contract duration metrics.
- **Cell Range**: A70:BT94
- **Layout Structure**:
    - **Row Headers Location**: A70:B94
    - **Column Headers Location**: C4:BT4
    - **Data Range**:
      - Monthly data: O72:BT94
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (BT1)
    - **Frequency**:
      - Monthly
- **Key Components**: Contract Duration, New Contracts, Average contract Length, Weighted average contract Length, Existing Clients.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Deal Metrics)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks deal-related metrics such as average client size and ARPU.
- **Cell Range**: A96:BT119
- **Layout Structure**:
    - **Row Headers Location**: A96:B119
    - **Column Headers Location**: C4:BT4
    - **Data Range**:
      - Monthly data: C97:BT119
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (BT1)
    - **Frequency**:
      - Monthly
- **Key Components**: Total Average Client Size, New Client Average Size, New Sales ARPU, Total User Base ARPU.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Client Counts)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of client firms, both new and existing.
- **Cell Range**: A169:BT180
- **Layout Structure**:
    - **Row Headers Location**: A169:B180
    - **Column Headers Location**: C4:BT4
    - **Data Range**:
      - Monthly data: O170:BT180
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (BT1)
    - **Frequency**:
      - Monthly
- **Key Components**: New firms, Existing Firms, Total Firms.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (User Counts)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of users across different categories.
- **Cell Range**: A182:AU251
- **Layout Structure**:
    - **Row Headers Location**: A182:B251
    - **Column Headers Location**: T4:AU4
    - **Data Range**:
      - Monthly data: T183:AU251
- **Time Series Details**:
    - **Date Range**:
      - Monthly: Unknown (T1) to Unknown (AU1)
    - **Frequency**:
      - Monthly
- **Key Components**: Financial, Corporate, Other, BRM (PRM Global), BRM Global, BRM Global (PRM Single), BRM Single, PRM Global, PRM Single region, Empty Container, AMR $30K (PRM Single region), AMR $30K (PRM Global), Inactive, AMR $15K (PRM Global), AMR $15K (PRM Single), AMR $30K (BRM Single, PRM Global), AMR $15K (Empty Container), Check.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Cancels)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks cancels in terms of dollars, counts, and users.
- **Cell Range**: A256:BT274
- **Layout Structure**:
    - **Row Headers Location**: A256:B274
    - **Column Headers Location**: C4:BT4
    - **Data Range**:
      - Monthly data: C257:BT274
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (BT1)
    - **Frequency**:
      - Monthly
- **Key Components**: Cancels $, Cancels Count, Cancels Users, Financial, Corporate, Other.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (ARR New/Upsell/Increase $)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks ARR from new sales, upsells, and increases.
- **Cell Range**: A276:BT334
- **Layout Structure**:
    - **Row Headers Location**: A276:B334
    - **Column Headers Location**: C4:BT4
    - **Data Range**:
      - Monthly data: C276:BT334
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (BT1)
    - **Frequency**:
      - Monthly
- **Key Components**: ARR New/Upsell/Increase $, Deal Count, User Count, Financial, Corporate, Other.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Monthly Recurring Revenue)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks Monthly Recurring Revenue.
- **Cell Range**: A354:AU499
- **Layout Structure**:
    - **Row Headers Location**: A354
    - **Column Headers Location**: C4:AR4
    - **Data Range**:
      - Monthly data: C354:AR354
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2017 (AA1) to Unknown (AR1)
    - **Frequency**:
      - Monthly
- **Key Components**: Monthly Recurring Revenue.
- **Notes & Customizations**: Values are scaled by 1000.


====================================================================================================
# SHEET 56: Revenue by Client
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Revenue by Client
- **Key Sections Identified**:
    - Revenue by Client (Annual)
    - Revenue by Client (Monthly)
    - Income Statement (Annual)

## 2. Detailed Section Analysis

### Section Name (Revenue by Client (Annual))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the revenue generated by different client segments (Corporate, Other) over a series of years. It allows for tracking revenue trends and identifying key revenue drivers.
- **Cell Range**: A3:Z11
- **Layout Structure**:
    - **Row Headers Location**: A5:A11
    - **Column Headers Location**: C4:Z4
    - **Data Range**:
      - Annual data: C7:Z8, C9:Z9, C11:Z11
- **Time Series Details**:
    - **Date Range**: 2015 to 2016
    - **Frequency**: Annual
- **Key Components**: Row Labels, Corporate, Other, Financial, Grand Total, 2015, 2016, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
- **Notes & Customizations**: Revenue data is scaled by 1000.

### Section Name (Revenue by Client (Monthly))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the revenue generated by different client segments (Corporate, Other) over a series of months. It allows for tracking revenue trends and identifying key revenue drivers.
- **Cell Range**: AA3:BT11
- **Layout Structure**:
    - **Row Headers Location**: A5:A11
    - **Column Headers Location**: AA4:BT4, AA5:BT5
    - **Data Range**:
      - Monthly data: AA7:BT8, AA9:AR9, AA11:BD11, BE11:BI11, BK11:BU11
- **Time Series Details**:
    - **Date Range**: 2017
    - **Frequency**: Monthly
- **Key Components**: Row Labels, Corporate, Other, Financial, Grand Total, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
- **Notes & Customizations**: Revenue data is scaled by 1000.

### Section Name (Income Statement (Annual))
- **Section Type**: Standard P&L
- **Description & Purpose**: This section represents a simplified Income Statement, likely projecting or analyzing financial performance over a series of years.
- **Cell Range**: AM15:BJ22
- **Layout Structure**:
    - **Row Headers Location**: Not explicitly defined in the provided data, but assumed to be in column AM.
    - **Column Headers Location**: Not explicitly defined in the provided data, but assumed to be in row 15/16.
    - **Data Range**:
      - Annual data: AM15:BJ16, AM17:BJ17, AM19:AX19, AY19:BD19, BE19:BG19, BH19:BJ19, AM20:AX20, AY20:BD20, BE20:BG20, BH20:BJ20, AM21:AX21, AY21:BD21, BE21:BG21, BH21:BJ21, AM22:AR22
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the provided data, but assumed to be a series of years.
    - **Frequency**: Annual
- **Key Components**: Income Statement (Y17)
- **Notes & Customizations**: Some data is scaled by 1000. The specific line items are not provided in the JSON.



====================================================================================================
# SHEET 57: Client Support
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Client Support
- **Key Sections Identified**:
    - Client ARR Movement - Type 1
    - Client ARR Movement - Type 2
    - Client ARR Movement - Type 3
    - Churned CARR

## 2. Detailed Section Analysis

### Section Name: Client ARR Movement - Type 1
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the movement of Annual Recurring Revenue (ARR) for a specific client type, showing beginning ARR, additions, churn, and ending ARR.
- **Cell Range**: C4:DU8
- **Layout Structure**:
    - **Row Headers Location**: C5:C8
    - **Column Headers Location**: E2:DU2
    - **Data Range**:
      - Monthly data: F5:DU8
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-10-01 (E2:DU2). Anchor points: E2=2010-10-01, Q2=2011-10-01, AC2=2012-10-01, AO2=2013-10-01, BA2=2014-10-01, BM2=2015-10-01, BY2=2016-10-01, CK2=2017-10-01, CW2=2018-10-01, DI2=2019-10-01, DU2=2020-10-01
    - **Frequency**: Monthly
- **Key Components**: Financial, Beginning, Added, Churn, End
- **Notes & Customizations**: Data is scaled by 1000 in most columns.

### Section Name: Client ARR Movement - Type 2
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the movement of Annual Recurring Revenue (ARR) for a specific client type, showing beginning ARR, additions, churn, and ending ARR.
- **Cell Range**: C10:DU14
- **Layout Structure**:
    - **Row Headers Location**: C11:C14
    - **Column Headers Location**: E2:DU2
    - **Data Range**:
      - Monthly data: F11:DU14
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-10-01 (E2:DU2). Anchor points: E2=2010-10-01, Q2=2011-10-01, AC2=2012-10-01, AO2=2013-10-01, BA2=2014-10-01, BM2=2015-10-01, BY2=2016-10-01, CK2=2017-10-01, CW2=2018-10-01, DI2=2019-10-01, DU2=2020-10-01
    - **Frequency**: Monthly
- **Key Components**: Beginning, Added, Churn, End, Corp
- **Notes & Customizations**: Data is scaled by 1000 in most columns.

### Section Name: Client ARR Movement - Type 3
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the movement of Annual Recurring Revenue (ARR) for a specific client type, showing beginning ARR, additions, churn, and ending ARR.
- **Cell Range**: C16:DU20
- **Layout Structure**:
    - **Row Headers Location**: C17:C20
    - **Column Headers Location**: E2:DU2
    - **Data Range**:
      - Monthly data: F17:DU20
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-10-01 (E2:DU2). Anchor points: E2=2010-10-01, Q2=2011-10-01, AC2=2012-10-01, AO2=2013-10-01, BA2=2014-10-01, BM2=2015-10-01, BY2=2016-10-01, CK2=2017-10-01, CW2=2018-10-01, DI2=2019-10-01, DU2=2020-10-01
    - **Frequency**: Monthly
- **Key Components**: Other, Beginning, Added, Churn, End
- **Notes & Customizations**: Data is scaled by 1000 in most columns.

### Section Name: Churned CARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the churned CARR for Lost Clients and Corporate clients.
- **Cell Range**: C22:DF26
- **Layout Structure**:
    - **Row Headers Location**: C23:C26
    - **Column Headers Location**: E2:DU2
    - **Data Range**:
      - Monthly data: F23:DF26
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-10-01 (E2:DU2). Anchor points: E2=2010-10-01, Q2=2011-10-01, AC2=2012-10-01, AO2=2013-10-01, BA2=2014-10-01, BM2=2015-10-01, BY2=2016-10-01, CK2=2017-10-01, CW2=2018-10-01, DI2=2019-10-01, DU2=2020-10-01
    - **Frequency**: Monthly
- **Key Components**: Financial, Churned CARR - Lost Clients, Corporate, Other, Total
- **Notes & Customizations**: Data is scaled by 1000 in most columns.


====================================================================================================
# SHEET 58: Subscriber Support
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Subscriber Support
- **Key Sections Identified**:
    - Subscriber Counts by Type
    - Expense Allocation

## 2. Detailed Section Analysis

### Section Name: Subscriber Counts by Type
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the number of subscribers, broken down by different subscriber types (Financial, Corp, Other). It shows the beginning count, added subscribers, churned subscribers, and the ending subscriber count for each type. This allows for analysis of subscriber growth and churn rates.
- **Cell Range**: C4:DS20
- **Layout Structure**:
    - **Row Headers Location**: Column C (C5:C8, C11:C14, C17:C20)
    - **Column Headers Location**: Row 2 (E2:DS2) and Row 4 (C4)
    - **Data Range**:
      - Monthly data: F5:DS8, F11:DS14, F17:DS20
- **Time Series Details**:
    - **Date Range**: 2010-10-01 to 2020-08-31 (E2:DS2). Anchor points: E2=2010-10-01, Q2=2011-10-01, AC2=2012-10-01, AO2=2013-10-01, BA2=2014-10-01, BM2=2015-10-01, BY2=2016-10-01, CK2=2017-10-01, CW2=2018-10-01, DI2=2019-10-01
    - **Frequency**: Monthly
- **Key Components**: Financial, Corp, Other, Beginning, Added, Churn, End.
- **Notes & Customizations**: Subscriber counts are displayed in thousands (scale=1000), except for DA6:DS6, DA12:DS12, and DA18:DS18.

### Section Name: Expense Allocation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section allocates expenses to different categories. It shows the total expenses and then breaks them down by category (e.g., Admin). This helps understand the cost structure.
- **Cell Range**: CM25:CY26
- **Layout Structure**:
    - **Row Headers Location**: Column CM (CM25, CM26)
    - **Column Headers Location**: Row 25 (CM25)
    - **Data Range**: CN25:CY26
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the provided JSON. Assuming the same monthly series as Subscriber Counts, but only for a subset of time.
    - **Frequency**: Monthly (assumed)
- **Key Components**: Total, Admin, Soros / Cap Group - Internal Content
- **Notes & Customizations**: Expenses are displayed in thousands (scale=1000).



====================================================================================================
# SHEET 59: Headcount Support
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Headcount Support
- **Key Sections Identified**:
    - Department Headcount (Original)
    - Department Headcount (New)
    - Sales Team Headcount
    - Customer Success, Operations, Business Development Headcount

## 2. Detailed Section Analysis

### Section Name: Department Headcount (Original)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for various departments over time. It provides a view of how headcount changes month-to-month and includes a 2020 budget.
- **Cell Range**: A1:BW10
- **Layout Structure**:
    - **Row Headers Location**: A1:B10
    - **Column Headers Location**: D1:CI1, BW2
    - **Data Range**:
      - Monthly data: D4:AV9 (numeric values for monthly periods, scaled by 1000)
      - 2020 Budget: AW4:BK9 (numeric values for 2020 budget)
      - Monthly data: BL4:CI10 (numeric values for monthly periods, scaled by 1000)
- **Time Series Details**:
    - **Date Range**: 2015-01-01 to 2021-12-01 (D1:CI1). Anchor points: D1=2015-01-01, P1=2016-01-01, AB1=2017-01-01, AN1=2018-01-01, AZ1=2019-01-01, BL1=2020-01-01, BX1=2021-01-01
    - **Frequency**: Monthly
- **Key Components**: Department, Headcount, 2020 Budget
- **Notes & Customizations**: Headcount values are scaled by 1000 in some ranges.

### Section Name: Department Headcount (New)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for various departments over time. It provides a view of how headcount changes month-to-month and includes a 2020 budget.
- **Cell Range**: A13:BW30
- **Layout Structure**:
    - **Row Headers Location**: A13:B30
    - **Column Headers Location**: D1:CI1, BW2
    - **Data Range**:
      - Monthly data: D23:AV29 (numeric values for monthly periods, scaled by 1000)
      - 2020 Budget: AW23:BK28 (numeric values for 2020 budget)
      - Monthly data: BL24:BW30 (numeric values for monthly periods, scaled by 1000)
- **Time Series Details**:
    - **Date Range**: 2015-01-01 to 2021-12-01 (D1:CI1). Anchor points: D1=2015-01-01, P1=2016-01-01, AB1=2017-01-01, AN1=2018-01-01, AZ1=2019-01-01, BL1=2020-01-01, BX1=2021-01-01
    - **Frequency**: Monthly
- **Key Components**: Department, Headcount, 2020 Budget
- **Notes & Customizations**: Headcount values are scaled by 1000 in some ranges.

### Section Name: Sales Team Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for various roles within the Sales team.
- **Cell Range**: B34:BM61
- **Layout Structure**:
    - **Row Headers Location**: B34:B61
    - **Column Headers Location**: D1:BH1, BM34
    - **Data Range**:
      - Monthly data: D34:BH48 (numeric values for monthly periods, scaled by 1000)
      - Monthly data: BI51:BJ54 (numeric values)
      - Monthly data: BL51:BM54 (numeric values)
- **Time Series Details**:
    - **Date Range**: 2015-01-01 to 2020-06-01 (D1:BH1). Anchor points: D1=2015-01-01, P1=2016-01-01, AB1=2017-01-01, AN1=2018-01-01, AZ1=2019-01-01, BL1=2020-01-01
    - **Frequency**: Monthly
- **Key Components**: Sales Roles, Headcount
- **Notes & Customizations**: Headcount values are scaled by 1000.

### Section Name: Customer Success, Operations, Business Development Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for Customer Success, Operations, and Business Development teams.
- **Cell Range**: B63:BW77
- **Layout Structure**:
    - **Row Headers Location**: B63:B77
    - **Column Headers Location**: BI1:BW1
    - **Data Range**: BI64:BW77
- **Time Series Details**:
    - **Date Range**: 2020-07-01 to 2021-12-01 (BI1:BW1).
    - **Frequency**: Monthly
- **Key Components**: Customer Success Roles, Operations Roles, Business Development Roles, Headcount
- **Notes & Customizations**: This section appears to have a different date range than the previous Sales Team Headcount section.


====================================================================================================
# SHEET 60: Salary Support
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Salary Support
- **Key Sections Identified**:
    - Department Salary Breakdown (Departments)
    - Department Salary Breakdown (Job Titles)
    - FX Rate
    - Quota Based Sales Reps
    - Sales Team & Customer Success

## 2. Detailed Section Analysis

### Section Name: Department Salary Breakdown (Departments)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down salary expenses by department. It allows for tracking salary costs across different departments over time.
- **Cell Range**: A1:CV10
- **Layout Structure**:
    - **Row Headers Location**: B3:B10
    - **Column Headers Location**: D1:CI1, CK1
    - **Data Range**:
      - Monthly data (2015-01 to 2021-12): D3:CI10
      - Monthly data (2021-01 to 2027-12): CK3:CV10
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-01 to 2021-12-31 (D1:CI1). Anchor points: D1=2015-01-01, P1=2016-01-01, AB1=2017-01-01, AN1=2018-01-01, AZ1=2019-01-01, BL1=2020-01-01, BX1=2021-01-01
      - Monthly: 2021-01-31 to 2027-12-31 (CK1:CV1). Anchor points: CY1=2021-01-31, DK1=2022-01-31, DW1=2023-01-31, EI1=2024-01-31, EU1=2025-01-31, FG1=2026-01-31, FS1=2027-01-31
    - **Frequency**: Monthly
- **Key Components**: Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, VP Bus Dev, Engineering (India)
- **Notes & Customizations**: Values are in thousands.

### Section Name: Department Salary Breakdown (Job Titles)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down salary expenses by job title. It allows for tracking salary costs across different roles over time.
- **Cell Range**: A13:BW30
- **Layout Structure**:
    - **Row Headers Location**: B13:B30
    - **Column Headers Location**: D1:CI1, BL1
    - **Data Range**:
      - Monthly data (2015-01 to 2021-12): D23:CI30
      - Monthly data (2020-01 to 2021-12): BL13:BW30
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2015-01-01 to 2021-12-31 (D1:CI1). Anchor points: D1=2015-01-01, P1=2016-01-01, AB1=2017-01-01, AN1=2018-01-01, AZ1=2019-01-01, BL1=2020-01-01, BX1=2021-01-01
      - Monthly: 2020-01-01 to 2020-12-31 (BL1:BW1). No anchor points available.
    - **Frequency**: Monthly
- **Key Components**: Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, VP Bus Dev, Engineering (India)
- **Notes & Customizations**: Values are in thousands.

### Section Name: Department Salary Breakdown (Detailed Job Titles)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a more granular breakdown of salary expenses by specific job titles, primarily within the sales organization. It allows for detailed tracking of salary costs for various sales roles over time.
- **Cell Range**: A38:BH54
- **Layout Structure**:
    - **Row Headers Location**: B38:B54
    - **Column Headers Location**: D1:BH1
    - **Data Range**: D38:BH54
- **Time Series Details**:
    - **Date Range**: Monthly: 2015-01-01 to 2021-06-30 (D1:BH1). Anchor points: D1=2015-01-01, P1=2016-01-01, AB1=2017-01-01, AN1=2018-01-01, AZ1=2019-01-01, BL1=2020-01-01, BX1=2021-01-01
    - **Frequency**: Monthly
- **Key Components**: Account Manager, Account Manager - Corp, Account Executive - Financial, Account Executive - Corporate, Account Executive - Enterprise, CRO, Product Specialist, Sales Operations Manager, Sales Manager, Operations
- **Notes & Customizations**: Values are in thousands.

### Section Name: FX Rate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section stores the foreign exchange rates used for currency conversions.
- **Cell Range**: B57:BD57
- **Layout Structure**:
    - **Row Headers Location**: B57
    - **Column Headers Location**: AL1:BD1 (implicit, based on data ranges)
    - **Data Range**: AL57:AV57, AW57:BD57
- **Time Series Details**:
    - **Date Range**: Monthly: 2020-01-01 to 2021-12-31 (AL1:BD1). No anchor points available.
    - **Frequency**: Monthly
- **Key Components**: FX RATE
- **Notes & Customizations**: This section contains FX rates, likely used to convert salaries in different currencies.

### Section Name: Quota Based Sales Reps
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks salary expenses for quota-based sales representatives.
- **Cell Range**: B60:BM64
- **Layout Structure**:
    - **Row Headers Location**: B60:B64
    - **Column Headers Location**: BI1:BM1 (implicit, based on data ranges)
    - **Data Range**: BI61:BM64
- **Time Series Details**:
    - **Date Range**: Monthly: 2021-07-01 to 2021-11-30 (BI1:BM1). No anchor points available.
    - **Frequency**: Monthly
- **Key Components**: Quota Sales Reps, AE - Financial (Quota), AE - Corporate (Quota), AM - Financial (Quota), VP Partnerships (Quota)
- **Notes & Customizations**: Values are in thousands.

### Section Name: Sales Team & Customer Success
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks salary expenses for the sales team and customer success roles.
- **Cell Range**: B66:BM86
- **Layout Structure**:
    - **Row Headers Location**: B66:B86
    - **Column Headers Location**: BI1:BM1 (implicit, based on data ranges)
    - **Data Range**: BI67:BM83, BI86:BM86
- **Time Series Details**:
    - **Date Range**: Monthly: 2021-07-01 to 2021-11-30 (BI1:BM1). No anchor points available.
    - **Frequency**: Monthly
- **Key Components**: Sales Team, CRO, Sales Manager, SDR Manager, SDR, Customer Success, CS Manager, AM - Financial, AM - Corporate, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, Business Development, GTM Strategy
- **Notes & Customizations**: Values are in thousands.



====================================================================================================
# SHEET 61: Bonus Support
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Bonus Support
- **Key Sections Identified**:
    - Department Salary Budget (2019 & 2020)
    - Department Adjustment
    - Department Salary Budget (2019 & 2020) - Adjusted
    - Sales Bonus Summary
    - Sales Bonus Detail

## 2. Detailed Section Analysis

### Section Name: Department Salary Budget (2019 & 2020)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the salary budget for different departments for the years 2019 and 2020. It's used for financial planning and tracking departmental expenses.
- **Cell Range**: A1:R10
- **Layout Structure**:
    - **Row Headers Location**: A1:B10
    - **Column Headers Location**: D1:R2
    - **Data Range**:
      - 2019 Budget: D4:F9
      - 2020 Budget: G4:R9
- **Time Series Details**:
    - **Date Range**:
      - 2019 Budget: 2019 (D2)
      - 2020 Budget: 2020 (R2)
    - **Frequency**: Annual
- **Key Components**: Department (Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, Engineering (India), Sales), Salary, 2019 Budget, 2020 Budget.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: Department Adjustment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the adjustment amounts for different departments. It's used to account for changes in the budget.
- **Cell Range**: A12:R20
- **Layout Structure**:
    - **Row Headers Location**: A12:B20
    - **Column Headers Location**: G12:R12
    - **Data Range**: G13:R19
- **Time Series Details**:
    - **Date Range**: 2020 (G12:R12 - implied)
    - **Frequency**: Annual
- **Key Components**: Adjustment, Department (Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, Engineering (India), Sales).
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: Department Salary Budget (2019 & 2020) - Adjusted
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the adjusted salary budget for different departments for the years 2019 and 2020. It's used for financial planning and tracking departmental expenses after adjustments.
- **Cell Range**: A24:R31
- **Layout Structure**:
    - **Row Headers Location**: A24:B31
    - **Column Headers Location**: D2:R2
    - **Data Range**:
      - 2019 Budget: D25:F30
      - 2020 Budget: G25:R30
- **Time Series Details**:
    - **Date Range**:
      - 2019 Budget: 2019 (D2)
      - 2020 Budget: 2020 (R2)
    - **Frequency**: Annual
- **Key Components**: Department (Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, Engineering (India), Sales), Salary, 2019 Budget, 2020 Budget.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: Sales Bonus Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of the sales bonus, including the total bonus and average attainment. It's used to track sales performance and bonus payouts.
- **Cell Range**: B34:CX40
- **Layout Structure**:
    - **Row Headers Location**: B36:B38
    - **Column Headers Location**: D1:CX1
    - **Data Range**:
      - Total Sales Bonus: F36:CX36
      - AVERAGE BONUS ATTAINMENT: F38:CX38
- **Time Series Details**:
    - **Date Range**: 2019-10-01 to 2027-12-01 (D1:CX1). Anchor points: D1=2019-10-01, P1=2020-10-01, AB1=2021-10-01, AN1=2022-10-01, AZ1=2023-10-01, BL1=2024-10-01, BX1=2025-10-01, CJ1=2026-10-01, CV1=2027-10-01
    - **Frequency**: Monthly
- **Key Components**: Total Sales Bonus, AVERAGE BONUS ATTAINMENT.
- **Notes & Customizations**: The data in F36:CX36 is scaled by 1000.

### Section Name: Sales Bonus Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of the sales bonus by role. It's used to analyze bonus payouts and performance at a granular level.
- **Cell Range**: B41:CX75
- **Layout Structure**:
    - **Row Headers Location**: B42:B56, B61:B75
    - **Column Headers Location**: D1:CX1, F60:CX60
    - **Data Range**:
      - Count/Total/Avg: D42:CX56
      - TOTAL SALES BONUS: F61:CX75
- **Time Series Details**:
    - **Date Range**:
      - Monthly Series 1: 2019-10-01 to 2027-12-01 (D1:CX1). Anchor points: D1=2019-10-01, P1=2020-10-01, AB1=2021-10-01, AN1=2022-10-01, AZ1=2023-10-01, BL1=2024-10-01, BX1=2025-10-01, CJ1=2026-10-01, CV1=2027-10-01
      - Monthly Series 2: 2019-12-31 to 2027-12-31 (F60:CX60). Anchor points: F60=2019-12-31, R60=2020-12-31, AD60=2021-12-31, AP60=2022-12-31, BB60=2023-12-31, BN60=2024-12-31, BZ60=2025-12-31, CL60=2026-12-31, CX60=2027-12-31
    - **Frequency**: Monthly
- **Key Components**: Count, Total, Avg, CRO, VP of Sales, Sales Manager, SDR Manager, SDR, CS Manager, AM - Corporate, AM - Financial, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy.
- **Notes & Customizations**: The data in D42:CX56 is scaled by 1000. There are two distinct monthly time series in this section.


====================================================================================================
# SHEET 62: Bonus Support (Sales Ops Only)
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Bonus Support (Sales Ops Only)
- **Key Sections Identified**:
    - Department Salary and Adjustment Budget
    - Sales Bonus Calculation
    - Sales Bonus by Role

## 2. Detailed Section Analysis

### Section Name: Department Salary and Adjustment Budget
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the salary budget and adjustments for different departments within the organization. It provides a breakdown of budgeted amounts for each department across different time periods.
- **Cell Range**: A1:R31
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., Content, Engineering (ex India), Executive, etc.)
    - **Column Headers Location**: Row 1 (Department), Row 2 (Salary, 2019 Budget, 2020 Budget)
    - **Data Range**:
      - 2019 Budget: `D4:F10`, `D24:F30`
      - 2020 Budget: `G4:R10`, `G13:R19`, `G24:R31`
- **Time Series Details**:
    - **Date Range**:
      - 2019 Budget: Appears to represent a single period or a sum of periods within 2019.
      - 2020 Budget: Appears to represent a single period or a sum of periods within 2020.
    - **Frequency**: Annual (Implied)
- **Key Components**: Department names, Salary, 2019 Budget, 2020 Budget, Adjustment
- **Notes & Customizations**: The "Adjustment" section (B12:R19) seems to be an addition to the initial salary budget, potentially reflecting changes or corrections.

### Section Name: Sales Bonus Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates and summarizes sales bonus information, including total sales bonus, quarterly sales bonus, and average bonus attainment.
- **Cell Range**: B34:CX40
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., Total Sales Bonus, Quarterly Sales Bonus, AVERAGE BONUS ATTAINMENT)
    - **Column Headers Location**: Row 1 (Monthly dates from 2019-10 to 2027-12)
    - **Data Range**:
      - Monthly data: `D36:CX36`, `G37`, `J37`, `M37`, `P37`, `S37`, `V37`, `Y37`, `AB37`, `AE37`, `AH37`, `AK37`, `AN37`, `AQ37`, `AT37`, `AW37`, `AZ37`, `BC37`, `BF37`, `BI37`, `BL37`, `BO37`, `BR37`, `BU37`, `BX37`, `CA37`, `CD37`, `CG37`, `CJ37`, `CM37`, `CP37`, `CS37`, `CV37`, `F40:CX40`
- **Time Series Details**:
    - **Date Range**: 2019-10-01 to 2027-12-01 (D1:CX1). Anchor points: D1=2019-10-01, P1=2020-10-01, AB1=2021-10-01, AN1=2022-10-01, AZ1=2023-10-01, BL1=2024-10-01, BX1=2025-10-01, CJ1=2026-10-01, CV1=2027-10-01
    - **Frequency**: Monthly
- **Key Components**: Total Sales Bonus, Quarterly Sales Bonus, AVERAGE BONUS ATTAINMENT
- **Notes & Customizations**: The Quarterly Sales Bonus is sparsely populated, suggesting it might be a summary or target value for specific quarters.

### Section Name: Sales Bonus by Role
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of sales bonus data by specific roles within the sales organization. It shows the average bonus for each role across different time periods.
- **Cell Range**: B43:CX75
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., CRO, Sales Manager, SDR Manager, SDR, etc.)
    - **Column Headers Location**: Row 1 (Monthly dates from 2019-10 to 2027-12), Row 43 (Count, Total, Avg), Row 61 (Monthly dates from 2019-12 to 2027-12)
    - **Data Range**:
      - Monthly data: `F44:CX57`, `F62:CX75`
- **Time Series Details**:
    - **Date Range**:
      - 2019-10-01 to 2027-12-01 (D1:CX1). Anchor points: D1=2019-10-01, P1=2020-10-01, AB1=2021-10-01, AN1=2022-10-01, AZ1=2023-10-01, BL1=2024-10-01, BX1=2025-10-01, CJ1=2026-10-01, CV1=2027-10-01
      - 2019-12-31 to 2027-12-31 (F61:CX61). Anchor points: F61=2019-12-31, R61=2020-12-31, AD61=2021-12-31, AP61=2022-12-31, BB61=2023-12-31, BN61=2024-12-31, BZ61=2025-12-31, CL61=2026-12-31, CX61=2027-12-31
    - **Frequency**: Monthly
- **Key Components**: Role names, Count, Total, Avg Sales Bonus
- **Notes & Customizations**: There are two separate date series in this section, one starting in October 2019 and the other in December 2019. This might indicate different calculation methods or data sources for different roles or time periods.



====================================================================================================
# SHEET 63: OpEx - Content
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Content
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period label.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: C3:U3
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 03/31/2019 to Unknown (based on the last date in the data)
    - **Frequency**: Monthly
- **Key Components**: "Content", "Month Ending"
- **Notes & Customizations**: This section contains the report title and the label for the monthly time series.

### Section Name: Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, detailing revenue, cost of sales, expenses, and ultimately, profit or loss.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: A5:A138
    - **Column Headers Location**: C3:U3
    - **Data Range**:
      - Monthly data: B7:U15, B20:M30, B37:U54, B57:U62, B65:U73, B76:U82, B85:U93, B96:U108, B111:U111, B114:U116, B119:U120, B123:U124, B127:U129, B132:U133, B136:U136
- **Time Series Details**:
    - **Date Range**: 03/31/2019 to Unknown (based on the last date in the data)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses.
- **Notes & Customizations**: The report is presented in thousands (scale = 1000). There are several sub-categories within each major component (e.g., multiple line items under People Costs). The "Year To Date" column (B3) suggests that the monthly values are cumulative.


====================================================================================================
# SHEET 64: OpEx - Engineering
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Engineering
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period covered.
- **Cell Range**: A2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: C3:U3
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to N/A. The last date is not explicitly provided in the JSON, but the pattern suggests it's a monthly series ending sometime in 2020.
    - **Frequency**: Monthly
- **Key Components**: Engineering, Month Ending, Year To Date
- **Notes & Customizations**: The header indicates that this sheet is for Engineering Operational Expenses.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the financial performance of the Engineering department, including revenue, cost of sales, gross profit, expenses, and other income/expenses.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: A5:A138
    - **Column Headers Location**: B3:U4
    - **Data Range**: B7:U138
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to N/A. The last date is not explicitly provided in the JSON, but the pattern suggests it's a monthly series ending sometime in 2020.
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses
- **Notes & Customizations**: The data is presented in thousands (scale: 1000). The time series is monthly, starting from 02/28/2019.



====================================================================================================
# SHEET 65: OpEx - Executive
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Executive
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period covered.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: C3:U3
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on available data)
    - **Frequency**: Monthly
- **Key Components**: Executive, Month Ending
- **Notes & Customizations**: This section provides the context for the rest of the sheet.

### Section Name: Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, including revenue, cost of sales, expenses, and profit.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: B3:U3, B4:U4
    - **Data Range**: B7:U17, B20:U33, B37:U55, B57:U74, B76:U83, B85:U94, B96:U109, B111:U112, B114:U117, B119:U121, B123:U125, B127:U130, B132:U134, B136:U137, B138:U138
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on available data)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, People Costs, Expenses, Taxes, Interest Net, Total Expenses
- **Notes & Customizations**: The report is scaled by 1000.


====================================================================================================
# SHEET 66: OpEx - Finance & Admin
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Finance & Admin
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period covered.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B2, C3:U3
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: February 2019 to October 2019
    - **Frequency**: Monthly
- **Key Components**: "Finance & Admin", "Month Ending", "Year To Date"
- **Notes & Customizations**: This section contains the title of the report and the time period covered.

### Section Name: Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the financial performance of the "Finance & Admin" department over a period of time. It includes revenue, cost of sales, gross profit, expenses, and other income/expenses to arrive at a total expense figure.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: A5:A138
    - **Column Headers Location**: B3:U3, B4:U4
    - **Data Range**: B7:U17, B20:U30, B37:U54, B57:U62, B65:U73, B76:U82, B85:U93, B96:U108, B111:U111, B114:U116, B119:U120, B123:R123, B124:U124, B127:U129, B132:U133, B136:U136
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to N/A (column U)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses.
- **Notes & Customizations**: The report is scaled by 1000. The end date is not explicitly defined in the provided JSON, but the pattern suggests it continues monthly.


====================================================================================================
# SHEET 67: OpEx - Marketing
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Marketing
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period description.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B2:U3
- **Time Series Details**:
    - **Date Range**: February 2019 to October 2019 (based on C4:J4, assuming the pattern continues)
    - **Frequency**: Monthly
- **Key Components**: "Marketing", "Month Ending", "Year To Date"
- **Notes & Customizations**: The header spans two rows and provides context for the data below.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the financial performance of the Marketing department, including revenue, cost of sales, expenses, and other income/expenses.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 4 (C4:U4 contain dates)
    - **Data Range**: B7:U137
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to 10/31/2019 (based on C4:J4, assuming the pattern continues to U4)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses.
- **Notes & Customizations**: The report is scaled by 1000. The time series is monthly, starting from February 2019. The indentation in column A indicates the hierarchical structure of the income statement.


====================================================================================================
# SHEET 68: OpEx - Product
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Product
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the product name and the label for the time series data.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B2:U3
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Product, Month Ending
- **Notes & Customizations**: This section provides context for the data in the Income Statement.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: This section presents the Income Statement, detailing revenue, cost of sales, expenses, and other financial metrics over a period of months. It's used to track and analyze the financial performance of a product.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: A5:A138
    - **Column Headers Location**: C4:U4
    - **Data Range**: B7:U137
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (U4)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, People Costs, Marketing, General & Admin, Legal Costs, Depreciation & Amortization, Taxes, Interest Net, Total Expenses.
- **Notes & Customizations**: The data is scaled by 1000. The "Year To Date" label in B3 suggests that the monthly values represent year-to-date figures.


====================================================================================================
# SHEET 69: OpEx - Sales
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: OpEx - Sales
- **Key Sections Identified**:
    - Header
    - Income Statement

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time series label.
- **Cell Range**: B2:U3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: C3:U3
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on last date in the sheet)
    - **Frequency**: Monthly
- **Key Components**: Sales, Month Ending
- **Notes & Customizations**: "Year To Date" is in cell B3.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, detailing revenue, cost of sales, expenses, and ultimately, profitability.
- **Cell Range**: A5:U138
- **Layout Structure**:
    - **Row Headers Location**: A5:A138
    - **Column Headers Location**: B4:U4
    - **Data Range**: B7:U137
- **Time Series Details**:
    - **Date Range**: 02/28/2019 to Unknown (based on last date in the sheet)
    - **Frequency**: Monthly
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses.
- **Notes & Customizations**: All monetary values are scaled by 1000. The time series is monthly, starting from 02/28/2019.



====================================================================================================
# SHEET 70: Historical Quota& Productivity
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Historical Quota& Productivity
- **Key Sections Identified**:
    - Historical Quota
    - Historical Productivity

## 2. Detailed Section Analysis

### Section Name (Historical Quota)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the historical quota for different account manager roles. It allows for tracking quota performance over time.
- **Cell Range**: B6:H12
- **Layout Structure**:
    - **Row Headers Location**: B7:B12
    - **Column Headers Location**: E5:H5
    - **Data Range**:
      - Annual data: F7:H12
- **Time Series Details**:
    - **Date Range**: 2016 to 2018
    - **Frequency**: Annual
- **Key Components**: Account Manager, AE - Financial, AE - Corporate, AE - Enterprise, AE - Other, VP Bus Dev.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Historical Productivity)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the historical productivity for different account manager roles. It allows for tracking productivity performance over time.
- **Cell Range**: B15:BH23
- **Layout Structure**:
    - **Row Headers Location**: B16:B23
    - **Column Headers Location**: E5:H5, J5:BH5
    - **Data Range**:
      - Annual data: E16:G23
      - Monthly data: J16:BH23
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2016 to 2018
      - Monthly: 2015-01-31 to 2019-03-31 (J5:BH5). Anchor points: J5=2015-01-31, V5=2016-01-31, AH5=2017-01-31, AT5=2018-01-31, BF5=2019-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Account Manager, AE - Financial, AE - Corporate, AE - Enterprise, AE - Other, VP Bus Dev, Other, Total.
- **Notes & Customizations**: Values are scaled by 1000. There are two separate time series, annual and monthly, for productivity data.


====================================================================================================
# SHEET 71: Fixed Asset Depreciation
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Fixed Asset Depreciation
- **Key Sections Identified**:
    - Header
    - Fixed Asset Depreciation Schedule

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains labels for the data in the subsequent section.
- **Cell Range**: C3:F3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: C3:F3
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Account, Starting Balance, Conversion, Starting Balance (USD)
- **Notes & Customizations**: None

### Fixed Asset Depreciation Schedule
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the depreciation schedule for fixed assets, including starting balances, conversions, and monthly depreciation expenses.
- **Cell Range**: B5:DV18
- **Layout Structure**:
    - **Row Headers Location**: B5:B10, B13:B18
    - **Column Headers Location**: G3:DV3 (Implicit - not directly provided in JSON, but inferred from data ranges)
    - **Data Range**:
      - Initial Data: D5:F10
      - Monthly data: G6:DV10, G14:DV18
- **Time Series Details**:
    - **Date Range**: G3 to DV3 (Inferred monthly series). Specific dates are not provided in the JSON, but the data range suggests a monthly frequency.
    - **Frequency**: Monthly (Inferred)
- **Key Components**: LTD, Mgmt, Inc, Total, Oy, R&D
- **Notes & Customizations**: Values are scaled by 1000. The column headers for the monthly data are not explicitly defined in the JSON but are implied by the data ranges.


====================================================================================================
# SHEET 72: COGS vs. Marginal
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: COGS vs. Marginal
- **Key Sections Identified**:
    - Revenue and Seats Calculation
    - COGS Analysis
    - Marginal Cost Analysis

## 2. Detailed Section Analysis

### Section Name: Revenue and Seats Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates Revenue per Seat based on 2017 Revenue and 2017 Seats. It also shows the current and marginal Revenue/Seat values.
- **Cell Range**: B6:D10
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 4 (Current, Marginal)
    - **Data Range**:
      - C6:D10 (numeric values)
- **Time Series Details**:
    - **Date Range**: 2017
    - **Frequency**: Annual
- **Key Components**: 2017 Revenue, 2017 Seats, Revenue / Seat (Current), Revenue / Seat (Marginal)
- **Notes & Customizations**: Uses a scale of 1000 for some values.

### Section Name: COGS Analysis
- **Section Type**: Cost Analysis
- **Description & Purpose**: This section analyzes the Cost of Goods Sold (COGS) and related metrics like Gross Profit per Seat and % Margin. It includes per-seat costs for various services.
- **Cell Range**: B12:E35
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Implicit (no clear headers, but D and E seem to represent different scenarios)
    - **Data Range**:
      - C12 (COGS value)
      - D27:E33 (per-seat costs and profit metrics)
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but likely related to 2017 or a similar timeframe.
    - **Frequency**: Annual
- **Key Components**: COGS, Per-Seat costs (Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, IDC, Web Service - Production), Gross Profit per Seat, % Margin
- **Notes & Customizations**: Includes "Calculations" section.

### Section Name: Marginal Cost Analysis
- **Section Type**: Cost Analysis
- **Description & Purpose**: This section analyzes marginal costs associated with various services and user tiers. It calculates costs based on percentages of users and prices per user.
- **Cell Range**: B41:D105
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Implicit (no clear headers, but D seems to represent marginal costs)
    - **Data Range**:
      - D50:D52, D54, D56, D66, D100, D105 (marginal cost values)
- **Time Series Details**:
    - **Date Range**: Not explicitly defined, but likely related to 2017 or a similar timeframe.
    - **Frequency**: Annual
- **Key Components**: Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, IDC, Web Service - Production, Percent of Users AMR, AMR - $15k, AMR - $30k, Cost per User, Marginal Price, Percent of Users, Price per User - Tier 1
- **Notes & Customizations**: Includes calculations for "Total" costs. Contains text indicating flat fees for some services (e.g., "TR Transcripts - flat fee will be triggered so no marginal cost").


====================================================================================================
# SHEET 73: Accrued Wages
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Accrued Wages
- **Key Sections Identified**:
    - Accrued Wages Data

## 2. Detailed Section Analysis

### Section Name (e.g., "Accrued Wages Data")
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the accrual and pre-payment of various social costs and insurance fees related to wages. It provides a monthly breakdown of these expenses.
- **Cell Range**: A1:Z13
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 1
    - **Data Range**:
      - Monthly data: `C2:Z13`
- **Time Series Details**:
    - **Date Range**: 2020-01-31 to 2021-12-31 (C1:Z1)
    - **Frequency**: Monthly
- **Key Components**: Acc. of pension insurance fees(accruals), Accrual of employer's statutory ins. pmt, Pension pre-payments, Unemployment pre-payment, Accident insurance pre-payment, Life insurance pre-payment, Calculated social costs, Pension held from workers, Unemployment held from workers, Total 21225 Accured finish side costs, USD
- **Notes & Customizations**: The data is scaled by 1000.


====================================================================================================
# SHEET 74: Deposits
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Deposits
- **Key Sections Identified**:
    - Deposits Data

## 2. Detailed Section Analysis

### Section Name (Deposits Data)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains the deposit data, scaled by 1000, for each month from January 2020 to December 2021.
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

