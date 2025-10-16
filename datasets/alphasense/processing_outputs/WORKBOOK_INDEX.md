# Workbook Index

This is a compact index of all sheets in the workbook for quick reference.
Use this to identify relevant sheets before querying the full MASTER_WORKBOOK_ANALYSIS.md

**Total Sheets**: 74

---

## Summary

### Changes Log
- **Section Type**: Documentation/Notes
- **Description & Purpose**: Documents changes made to the underlying model or data. Useful for understanding the evolution of the forecast.
- **Key Components**: Change descriptions.
- **Notes & Customizations**: Free-form text.

### Key Metrics - Monthly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents key performance indicators (KPIs) and financial metrics on a monthly basis. Allows for tracking trends and performance over time.
- **Key Components**: Cash, Debt, ARR, Bookings, ARR TTM Growth, Margin, EBITDA, FCF, Reps, Eff Reps.
- **Notes & Customizations**: Values are scaled by 1000 in some rows.

### Key Metrics - Annual
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents key performance indicators (KPIs) and financial metrics on an annual basis. Provides a summary view of the company's performance over the years.
- **Key Components**: ARR, FCF, Avg FCF, Cash, Debt, Growth Rate, Avg Eff Reps, Bookings, Avg Bkgs.
- **Notes & Customizations**: Values are scaled by 1000 in some rows.

---

## Master Ctrl

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and the name of the spreadsheet.
- **Key Components**: AlphaSense, Inc., Master CTRL
- **Notes & Customizations**: Standard header information.

### Control Panel
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains key input assumptions and control variables for the model.
- **Key Components**: Master Case, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**: Contains different scenarios for the model.

### Global Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains global assumptions for the model, such as the latest actual month and months left in the year.
- **Key Components**: Latest Actual Month, Months Left in Year
- **Notes & Customizations**: Contains global assumptions for the model.

### Productivity Case
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains productivity case assumptions for the model.
- **Key Components**: Base, Target
- **Notes & Customizations**: Contains different scenarios for the model.

---

## Dash Control

### Dashboard Title/Scenario Selection
- **Section Type**: `Dashboard Configuration`
- **Description & Purpose**: This section contains the title of the dashboard and allows the user to select different scenarios. It's used to configure the dashboard's display.
- **Key Components**: "AlphaSense, Inc.", "Dashboard CTRL", "1 - Base - $25mm"
- **Notes & Customizations**: This section is used to set the context for the rest of the dashboard.

### Time Series Headers
- **Section Type**: `Time Series Header`
- **Description & Purpose**: This section defines the time periods for the data displayed in the dashboard. It includes both annual and monthly time series.
- **Key Components**: "Year", "Month", Years (2015-2027), Months (Jan-Dec)
- **Notes & Customizations**: Contains both annual and monthly time series data. The annual data in T7:FS7 is repeating.

### Key Metrics Table
- **Section Type**: `Key Metrics Table`
- **Description & Purpose**: This section displays key performance indicators (KPIs) and financial metrics for different scenarios. It includes metrics like "Support Fees - % of CAC", "ARR Multipler", and "Perpetuity Factor", across various base scenarios.
- **Key Components**: "Support Fees - % of CAC", "ARR Multipler ", "Perpetuity Factor", "ARR Multipler  - Financial", "Perpetuity Factor - Financial", "ARR Multipler - Corporate", "Perpetuity Factor - Corporate", "% Travel Costs", "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: The data is scaled by 1000. The table contains multiple scenarios (Base, Growth) and different calculation methods (Financial, Corporate).

---

## Dash

### Income Statement Metrics
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's Income Statement, including Revenue, Cost of Sales, Gross Profit, Operating Expenses, and EBITDA. Used to assess profitability.
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Operating Expenses, EBITDA, Free Cashflow (FCF)
- **Time Range**: Annual: 2011-2023, Monthly: 2015-2027
- **Notes & Customizations**: Includes a "Memo" line for Free Cashflow. Values are scaled by 1000.

### ARR Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the company's Annual Recurring Revenue (ARR) at the beginning and end of the period.
- **Key Components**: Beginning ARR, Ending ARR
- **Time Range**: Annual: 2011-2023, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the company's Bookings, broken down by Financial, Corporate, and Other categories.
- **Key Components**: Financial Bookings, Corporate Bookings, Other Bookings, Total Bookings, New Bookings, Total New Bookings, Upsell, Total Upsell
- **Time Range**: Annual: 2011-2023, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Segment Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes ARR by Segment.
- **Key Components**: Beginning ARR, Ending ARR
- **Time Range**: Annual: 2011-2023, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Headcount Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the company's Headcount by department.
- **Key Components**: Executive, Engineering, Product, Sales, Marketing, Content, Finance, HR, and Operations, Total Headcount, Avg Effective Quota Carrying Sales Reps, New ARR per Sales Rep, New Clients per Sales Rep.
- **Time Range**: Annual: 2011-2023, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000. Includes a "Memo" line for India Employees.

### Client & Subscriber Counts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the company's Client and Subscriber counts.
- **Key Components**: Clients (End of Period), Users (End of Period), Clients, Beginning of Period, Added, Churned, Clients, End of Period, ARR Per Client
- **Time Range**: Annual: 2011-2023, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Retention Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the company's Retention Metrics.
- **Key Components**: Upsells, Up for Renewal, Renewed, Churn, Ann. Net Dollar Retention, Ann. Gross Dollar Retention, Ann. Cohort Retention, Ann. Net Dollar Retention - TTM, Ann. Gross Dollar Retention - TTM, Ann. Cohort Retention - TTM
- **Time Range**: Annual: 2011-2023, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000 for some metrics.

### Key Performance Indicators Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes Key Performance Indicators.
- **Key Components**: LTV / CAC
- **Time Range**: Annual: 2011-2023, Monthly: 2017-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Key Performance Indicators Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details Key Performance Indicators.
- **Key Components**: Margin (end of Period), Avg Quota Carrying Salee Reps, Bookings per Sales Rep, ARR per Sales Rep, Avg. Users per Client, Annual Rev/Client (ARPC), Annual COS/Client, Annual Rev/Subscriber (ARPU), Annual COS/Subscriber, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback Period (Months)
- **Time Range**: Annual: 2011-2023, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Key Performance Indicators by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details Key Performance Indicators by Segment.
- **Key Components**: Avg. Users per Client, Annual Rev/Client (ARPC), Annual COS/Client, Annual Rev/Subscriber (ARPU), Annual COS/Subscriber, Churn, Annual Gross Dollar Retention, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, LTV / CAC
- **Time Range**: Annual: 2011-2023, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Debt Availability Build
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Calculates Debt Availability based on MRR and other factors.
- **Key Components**: Multiplier of MRR, T3M MRR, T3M Revenue Lost, T3M Churn, Annualized Retention Rate, Current MRR, Availability Amount
- **Notes & Customizations**: Values are scaled by 1000.

---

## CAC by Segment

### Title/Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and other descriptive information.
- **Key Components**: "AlphaSense, Inc.", "CAC by Segment", "1 - Base - $25mm"
- **Notes & Customizations**: None

### CAC Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of Upsell Cost, CAC, and Support Cost for Total Company, Financial, and Corporate segments.
- **Key Components**: Upsell Cost, CAC, Support Cost, Total Company, Financial, Corporate
- **Time Range**: Annual: 2013-2021, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### CAC Detail by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of CAC by segment, including Account Manager - Corp, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, and AE - Enterprise. Also includes Wages and Support Costs.
- **Key Components**: Account Manager - Corp, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise, Total, % Financial, % Corporate, Wages
- **Time Range**: Annual: 2015-2021, Quarterly: 2018-2020
- **Notes & Customizations**: Values are scaled by 1000.

### Adjusted Sales and Marketing Cost Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes Adjusted Sales and Marketing Costs, including People Costs and All-In Support Costs.
- **Key Components**: Total Company, Adjusted Sales and Marketing Cost, % to CAC, % to Upsell, $ to CAC, $ to Upsell, People Costs, Adjusted People Costs, All-In Support Costs, Total Users (excl. Other), % Financial, % Corporate
- **Time Range**: Annual: 2013-2021, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

---

## Payback Period

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Key Components**: AlphaSense, Inc., Payback Period, 1 - Base - $25mm
- **Notes & Customizations**: Contains the company name, report title, and scenario description.

### Payback Period - Total Company
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summary of key metrics used to calculate the payback period for the total company.
- **Key Components**: LTV / CAC, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback
- **Notes & Customizations**: Values are scaled by 1000.

### Cash Payback - Monthly Detail
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Monthly detail of cash payback, likely used to create a waterfall chart.
- **Key Components**: Month, Multiplier, Increase
- **Notes & Customizations**: Values are scaled by 1000.

### Payback Period - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summary of key metrics used to calculate the payback period for the Financial division.
- **Key Components**: LTV / CAC, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback
- **Notes & Customizations**: Values are scaled by 1000.

### Payback Period - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summary of key metrics used to calculate the payback period for the Corporate division.
- **Key Components**: LTV / CAC, Initial Period ARR, New Clients Added, Initial Period ARR per New Client, ARR Multiplier, Fully Ramped ARR, Gross Margin, Contribution ARR, Support Cost, Average Clients in Period, Support Cost per Client, Upsell Cost, Upsell Cost per Client, Perpetuity Factor, LTV, Total CAC, CAC per Client, Payback
- **Notes & Customizations**: Values are scaled by 1000.

### Cash Payback - Monthly Detail (Financial)
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Monthly detail of cash payback for the Financial division, likely used to create a waterfall chart.
- **Key Components**: Month, Multiplier, Increase
- **Notes & Customizations**: Values are scaled by 1000.

### Cash Payback - Monthly Detail (Corporate)
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Monthly detail of cash payback for the Corporate division, likely used to create a waterfall chart.
- **Key Components**: Month, Multiplier, Increase
- **Notes & Customizations**: Values are scaled by 1000.

---

## Fin CTRL

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description. Provides context for the financial data.
- **Key Components**: AlphaSense, Inc., Financial Statements CTRL, 1 - Base - $25mm
- **Notes & Customizations**: None

### Balance Sheet Support
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides key metrics and assumptions used to support the balance sheet projections. Includes calculations and percentages related to various balance sheet accounts.
- **Key Components**: Days Sales Outstanding, Prepaid Expenses (Monthly % of Operating Expenses), Capital Expenditures - % of Revenue, Accounts Payable Days Payable Outstanding, Commissions Payable - % of ARR, Accrued Expenses Days Payable Outstanding, Accrued Commissions - % of ARR, Accrued Wages - % Growth, Accrued Holiday Pay - % of Wages, Accrued Interest - % Growth, Payroll Taxes Payable - % Growth, Sales Taxes Payable - % of Revenue, Deferred Commissions Growth, Tekes - 14887, Tekes - 15118, Tekes - 14560, Tekes - 14223, Tekes - 15543, Interest Rate, Interest Rate - Admin Fee, Interest Rate on Cash Account, Percent of Cash in Account, Effective Commission Rate, Day Sales Outstanding, Credit Card Payable - % of OpEx, Target Hit Rate - Accrued Commission, LIBOR
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series data. Some rows have "na" values for certain periods. The "x" in column A likely indicates a row that is used in calculations or is otherwise important.

---

## Fin

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and scenario description.
- **Key Components**: AlphaSense, Inc., Financial Statements, 1 - Base - $25mm
- **Notes & Customizations**: None

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time.
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Operating Expenses, EBITDA, Net Income
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes intercompany revenue/expenses.

### Balance Sheet
- **Section Type**: Balance Sheet
- **Description & Purpose**: Presents a snapshot of the company's assets, liabilities, and equity at a specific point in time.
- **Key Components**: Current Assets, Fixed Assets, Accounts Payable, Accrued Expenses, Deferred Revenue, Convertible Notes, Total Liabilities & Equity
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes a note about budgeted values.

### Cash Flow Statement
- **Section Type**: Standard Cash Flow Statement
- **Description & Purpose**: Tracks the movement of cash both into and out of the company during a period of time.
- **Key Components**: Net Income, Depreciation, Accounts Receivable, Accounts Payable, Net Cash Flows from Operating Activities, Net Cash Flows from Investing Activities, Net Cash Flows from Financing Activities, Cash, End of Period
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Balance Sheet Support
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides supporting calculations and metrics for the balance sheet.
- **Key Components**: Days in Period, Total Billings, Total Bookings, Days Sales Outstanding, Allowance for Doubtful Accounts, Fixed Assets, Total
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes calculations related to prepaid expenses, depreciation, and accounts receivable.

### Long Term Liabilities
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the calculations and projections for long-term liabilities.
- **Key Components**: Tekes - 14887, Tekes - 15118, Tekes - 14560, Tekes - 14223, Tekes - 15543, Starting Balance, Ending Balance, Interest Rate, Total Interest / Admin Expense, Total Payback
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Focuses on specific long-term loan details.

### Equity Investment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the calculations and projections for equity investment.
- **Key Components**: Net Investment Amount, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Focuses on specific Equity Investment details.

### SVB Debt
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the calculations and projections for SVB Debt.
- **Key Components**: MRR, Multiplier, Retention, Total Availability, Debt, Leverage, Minimum Cash Balance, Cash from Operations, Cash from Investing Activities, Revolver, Cash from Financing Activities, Change in Cash, Cash, BoP, Change, Cash, EoP, Cash (Excluding Revolver), Revolver Drawn (Y/N), Cash Needed, Beginning, Add, Paid Down, End, Debt Issuance Amortization, Interest, LIBOR, Interest Rate
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Focuses on specific SVB Debt details.

### Income Statement Support - Income Taxes
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides supporting calculations for income taxes in the income statement.
- **Key Components**: Pre Tax Income, Starting NOL, NOL (Use) Add, Ending NOL, Taxable Income, Tax Rate, Taxes Paid, FCF, CFO, EBITDA
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes NOL calculations and adjustments to EBITDA.

---

## Debt Compliance

### Revenue Growth Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes revenue growth and compares it against a growth covenant to ensure compliance.
- **Key Components**: Revenue, T3M, Growth Rate, Growth Covenant, Compliance Check
- **Time Range**: Annual: 2018-2027, Monthly: 2018-2027
- **Notes & Customizations**: Revenue is scaled by 1000. Compliance check shows "OK" if the covenant is met.

### Liquidity Compliance Check
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks various liquidity metrics, including EBITDA, cash, borrowings, and availability, to assess compliance with liquidity covenants.
- **Key Components**: Remaining Months Liquidity (RML), Total Borrowings, Total Availability, Cash, Net Availability + Unrestricted Cash, EBITDA, Capitalized R&D, Capitalized Expenditures, Change in Deferred Revenue, Adjusted EBITDA, Liquidity Threshold, Restricted Cash, Net Availability, Liquidity, Thershold, Compliance Check
- **Time Range**: Annual: 2018-2027, Monthly: 2018-2027
- **Notes & Customizations**: Values are scaled by 1000. "N/A" and "Breaks" are present in some cells. Compliance check shows "OK" if the covenant is met.

### Liquidity Buffer Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates different liquidity buffers to assess the company's financial cushion.
- **Key Components**: $5m Liquidity Buffer, RML Liquidity Buffer, Overall Liqudity Buffer
- **Time Range**: Monthly: 2018-2027
- **Notes & Customizations**: Values are scaled by 1000.

---

## ARR and Rev CTRL

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and report title.
- **Key Components**: Company Name, Report Title
- **Notes & Customizations**: None

### Revenue & Quota Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines revenue assumptions and quota targets for different sales roles and scenarios (Base, Growth, Upside). It includes revenue percentages of MRR for various customer segments and quota attainment levels.
- **Key Components**: Rev % of MRR (Financial, Corporate, Other), Quota (Account Manager, AE - Financial, AE - Corporate, VP Bus Dev, AE - Enterprise)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Scenarios include "Base", "Growth", and "Base (R&D)". Quotas are split into "Active", "Base", and "Upside".

### Productivity - % of Quota
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates productivity as a percentage of quota, incorporating seasonality and adjustments.
- **Key Components**: Productivity - % of Quota, Seasonality, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes adjustments and seasonality factors.

### Total ARR - % New Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the percentage of total ARR attributable to new bookings.
- **Key Components**: Total ARR - % New Bookings, Account Manager, AE - Financial, AE - Corporate, VP Bus Dev, AE - Enterprise
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Total ARR - % Upsell
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the percentage of total ARR attributable to upsells.
- **Key Components**: Total ARR - % Upsell, Account Manager, AE - Financial, AE - Corporate, VP Bus Dev, AE - Enterprise
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Productivity - Allocation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section focuses on the allocation of productivity across different segments.
- **Key Components**: VP - Bus Dev - % to Financial, VP - Bus Dev - % to Corporate, AE - Enterprise - % to Financial, AE - Enterprise - % to Corporate
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### ARR Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents key ARR metrics, including year-over-year growth and ARR per user.
- **Key Components**: % YoY Growth, ARR / User - Active, ARR / User - Base, ARR / User - Target
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Metrics are categorized by Financial, Corporate, and Other segments.

---

## Sales Prod Input

### Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the quota per person and seasonality assumptions used in the sales productivity calculations.
- **Key Components**: Quota per Person, Seasonality, All Roles
- **Notes & Customizations**: Quota is scaled by 1000.

### Productivity by Role
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the productivity of different roles within the sales organization.
- **Key Components**: Productivity, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise
- **Notes & Customizations**: None.

### Productivity (Adjusted for Seasonality)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the productivity of different roles adjusted for seasonality.
- **Key Components**: Productivity (Adjusted for Seasonality), Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise
- **Notes & Customizations**: None.

---

## ARR and Revenue

### ARR and Revenue Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a high-level overview of ARR, Revenue, and related metrics. It tracks the company's overall performance.
- **Key Components**: ARR - Start, New Business, Upsell, Churn, ARR - End, % Churn Rate, Up for Renewal, Retention Rate, ARR, Revenue, % Growth
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: The "% YoY Growth" in cell E13 is marked as "na" for the first year.

### ARR by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down ARR by different segments (Financial, Corporate, Other) to analyze performance across customer groups.
- **Key Components**: Financial, Corporate, Other, Total ARR
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Revenue by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down Revenue by different segments (Financial, Corporate, Other) to analyze performance across customer groups.
- **Key Components**: Financial, Corporate, Other, Total Revenue
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Revenue as % of MRR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the percentage of revenue relative to monthly recurring revenue (MRR) by segment.
- **Key Components**: Financial, Corporate, Other, Total Revenue as % of MRR
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Sales Productivity
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks sales headcount and productivity metrics.
- **Key Components**: Sales Headcount, Account Manager, AE - Financial, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other, Total Sales Headcount, Effective Sales Headcount, Total Effective Sales Reps, Quota per Person
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: The "Quota per Person" has a different column structure (F66:H66, I66:Q66, BD66:CI66, CJ66:FS66).

### Total Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks total bookings.
- **Key Components**: Total Quota, Productivity - % of Quota (Adjusted for Seasonality), Total Bookings, Account Manager, Other, New Bookings
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: The "Productivity - % of Quota (Adjusted for Seasonality)" has a different column structure (F83:Q83, CB83:CI83, CJ83:FS83).

### New Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks new bookings.
- **Key Components**: New Bookings, Account Manager, Total New Bookings
- **Time Range**: Annual: 2017-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Upsell
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks upsell bookings.
- **Key Components**: Upsell, Account Manager, Total Upsell
- **Time Range**: Annual: 2017-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### New Bookings - % of Total Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks new bookings as a percentage of total bookings.
- **Key Components**: New Bookings - % of Total Bookings, Account Manager, Total New Bookings
- **Time Range**: Annual: 2017-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Upsell - % of Total Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks upsell bookings as a percentage of total bookings.
- **Key Components**: Upsell - % of Total Bookings, Account Manager, Total Upsell
- **Time Range**: Annual: 2017-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Total Bookings by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks total bookings by segment.
- **Key Components**: VP - Bus Dev, % Financial, Amount to Financial, % Corporate, Amount to Corporate, AE - Enterprise, Financial, Corporate, Other, Total Bookings
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: The "% YoY Growth" in cell E158 is marked as "na" for the first year.

### New Bookings by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks new bookings by segment.
- **Key Components**: New Bookings by Segment, Financial, Corporate, Other, Total New Bookings
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: The "% YoY Growth" in cell E165 is marked as "na" for the first year.

### Upsell by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks upsell bookings by segment.
- **Key Components**: Upsell by Segment, Financial, Corporate, Other, Total Upsell
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: The "% YoY Growth" in cell E172 is marked as "na" for the first year.

### Financial ARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks financial ARR.
- **Key Components**: Financial ARR, Beginning ARR, New Business, Upsell, Churn, Ending ARR, % YoY Growth, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Corporate ARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks corporate ARR.
- **Key Components**: Corporate ARR, Beginning ARR, New Business, Upsell, Churn, Ending ARR, % YoY Growth, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Other ARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks other ARR.
- **Key Components**: Other ARR, Beginning ARR, New Business, Upsell, Churn, Ending ARR, % YoY Growth, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

### Combined
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks combined metrics.
- **Key Components**: Combined, Clients, Net, ARR / Client, Users, Net, ARR / Subscriber, Users / Client
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: None

---

## Sales CTRL

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the spreadsheet's purpose.
- **Key Components**: AlphaSense, Inc., Sales Representatives CTRL, 1 - Base - $25mm
- **Notes & Customizations**: Standard header information.

### Quota Sales Reps Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of quota-carrying sales representatives and related metrics.
- **Key Components**: Total Headcount, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes headcount added and removed in the period.

### Account Manager Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Account Managers and related metrics.
- **Key Components**: Account Manager, Annual Increase, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes salary and sales bonus information.

### AE - Financial Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Financial and related metrics.
- **Key Components**: AE - Financial, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D), % of Total Headcount
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes headcount added and removed in the period, broken down by base, target, and upside.

### AE - Corporate Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Corporate and related metrics.
- **Key Components**: AE - Corporate, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D), % of Total Headcount
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes headcount added and removed in the period, broken down by base, target, and upside.

### VP - Bus Dev Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of VP - Bus Dev and related metrics.
- **Key Components**: VP - Bus Dev, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D), % of Total Headcount
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes headcount added and removed in the period.

### AE - Enterprise Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Enterprise and related metrics.
- **Key Components**: AE - Enterprise, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D), % of Total Headcount
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes headcount added and removed in the period.

### AE - Other Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of AE - Other and related metrics.
- **Key Components**: AE Other - Headcount Added in Period, AE Other - Headcount Removed in Period, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes headcount added and removed in the period.

### Other Sales - Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of CRO and related metrics.
- **Key Components**: CRO, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes headcount added in the period.

### Other Sales - Salary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the salary of CRO and related metrics.
- **Key Components**: CRO, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes annual increase.

### Old Assumptions (To Be Deleted)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the assumptions for Manager - Corporate and related metrics.
- **Key Components**: Manager - Corporate, Manager - Corporate - Added in Period (2018 Driver), Manager - Corporate - AE Corp per Manager Corporate (2019 and Beyond Annual Driver)
- **Time Range**: Annual: 2015-2018, Monthly: 2015-2019
- **Notes & Customizations**: Includes assumptions for 2018 and beyond.

### Product Specialist Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Product Specialist and related metrics.
- **Key Components**: Product Specialist, AE per Product Specialist (2019 and Beyond Annual Driver)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes Product Specialist Added (2018 Driver).

### Product Specialist Manager Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Product Specialist Manager and related metrics.
- **Key Components**: Product Specialist - Mgr, Product Specialist per Product Specialist Manager (2019 and Beyond Annual Driver)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes Product Specialist Manager Added (2018 Driver).

### Sales - Admin Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Sales - Admin and related metrics.
- **Key Components**: Sales - Admin, AE per Sales Admin (2019 and Beyond Annual Driver)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes Sales Admin Added (2018 Driver).

### Sales Manager Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Sales Manager and related metrics.
- **Key Components**: Sales Manager, Quota'd Rep per Sales Manager (2019 and Beyond Annual Driver)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes Sales Manager Added (2018 Driver).

### Sales Operations Manager Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Sales Operations Manager and related metrics.
- **Key Components**: Sales Operations Manager, AE per Sales Operations Manager (2019 and Beyond Annual Driver)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes Sales Operations Manager Added (2018 Driver).

### Sales Recruiter Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of Sales Recruiter and related metrics.
- **Key Components**: Sales Recruiter, Sales Recruiter Added
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes headcount added in the period.

### SDR Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the headcount of SDR and related metrics.
- **Key Components**: SDR, AE per SDR (2019 and Beyond Annual Driver) - Active, Base, Upside
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes SDR Added (2018 Driver).

---

## Sales Role Input

### Section Name (Sales Role Headcount Input - Quota Roles)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the headcount requirements for quota-carrying sales roles. It allows users to input the number of sales roles required, and the system calculates the associated costs.
- **Key Components**: AE - Corporate, AE - Financial, Account Manager, VP Bus Dev, Beginning, Added, Lost, Ending.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name (Sales Role Headcount Input - Non-Quota Roles)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the headcount requirements for non-quota-carrying sales roles. It allows users to input the number of sales roles required, and the system calculates the associated costs. There are two sub-sections, one for roles where the headcount is directly input, and another where the headcount is derived from a formula.
- **Key Components**: CRO, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy, AM - Financial (Quota) moved to (Non-Quota), VP of Sales (Reports per VP), VP of Sales (Total AE Reports), Sales Manager (AEs per Manager), SDR Manager (SDRs per Manager), SDR (AEs per SDR), VP Customer Success (AMs + PS Managers per VP), Corporate AM (ARR per AM), Financial AM (ARR per AM), Product Specialist Manager (PS per Manager), Product Specialist (ARR per PS).
- **Notes & Customizations**: The data is scaled by 1000. The VP of Sales (Total AE Reports) section spans a larger range (AM51:DD51) than the other non-quota roles.

---

## Sales Reps

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and report title.
- **Key Components**: AlphaSense, Inc., Sales Reps Detail, 1 - Base - $25mm
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains the company name, report title, and a scenario description.

### Quota Sales Rep Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the quota'd sales rep headcount.
- **Key Components**: Quota Sales Rep Headcount, Total Quota Sales Rep Headcount, Average Effective Quota Headcount, AM - Financial, AE - Corporate, VP - Partnerships, AE - Enterprise, AE - Other, Total Average Effective Quota Headcount
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Non Quota'd Sales Team Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the non-quota'd sales team headcount.
- **Key Components**: CRO, VP of Sales, Sales Manager, SDR Manager, SDR, CS Manager, AM - Corporate, AM - Financial, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy, Total Non Quota'd Sales Team
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Quota Sales Rep Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed information on quota'd sales reps, including ramp, efficiency, and attrition.
- **Key Components**: Beginning of Period, Added, Removed, End of Period, Ramp, Efficiency, Month 1, Month 2, Month 3, Month 4, Month 5, Month 6, Month 7, Month 8, Month 9, Month 10, Attrition, Effective Start, Add, Effective End, VP - Bus Dev
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes both annual and monthly time series data. Contains ramp-up and attrition metrics.

### Other Sales Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed information on other sales roles, including sales team size and required managers.
- **Key Components**: Sales Team, CRO, VP of Sales, Reports per VP of Sales, AEs, Sales Managers, Reports, Min. Required Sales Managers, SDRs per SDR Manager, SDRs, Min. Required SDR Managers, AE per SDR, AE, Min. Required SDRs, Customer Success, Customer Success Manager, AM + PS Manager per CS Manager, Ams + PS Manager, Min. Required AMs, Account Manager - Corporate, Corporate ARR - End of Period, Corporate ARR per Account Manager - Corp, Min. Required Account Manager - Corp, Account Manager - Financial, Financial ARR - End of Period, Financial ARR per Account Manager - FS, Min Required Account Manager - FS, Quota Carrying AMs, Quota Carrying AMs Moved, Product Specialist per Product Specialist Manager, Product Specialist, Min. Required PS - Mgrs, Operations, Enablement Manager, Sales - Admin, Sales Operations Manager, Sales Operations, Business Development
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes both annual and monthly time series data. Contains ratios and minimum required headcount calculations.

### Total Sales Heads
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides total sales headcount information.
- **Key Components**: Total Sales Heads
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Quota Rep - Salary Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the salaries for quota'd sales reps.
- **Key Components**: Quota Rep - Salary Summary, Account Manager, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other, Total
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Quota Rep - Bonus Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the bonus amounts for quota'd sales reps.
- **Key Components**: Quota Rep - Bonus Summary, Account Manager, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other, Total
- **Time Range**: Annual: 2019-2027, Monthly: 2020-2027
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Quota Rep - Salary Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed salary information for quota'd sales reps.
- **Key Components**: Employees, Average Salary, Total Wages, Sales Bonus per Head, Total Sales Bonus, Account Manager, AE - Corporate, VP - Bus Dev, AE - Enterprise, AE - Other
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Other Sales - Salary Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed salary information for other sales roles.
- **Key Components**: Sales Team, CRO, VP of Sales, Sales Manager, SDR Manager, SDR, Customer Success, Customer Success Manager, Account Manager - Corporate, Account Manager - Financial, Product Specialist - Mgr, Product Specialist, Enablement Manager, Sales - Admin, Sales Operations Manager, Sales Operations, GTM Strategy, Total Sales Salary, Average Employees
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Includes both annual and monthly time series data.

### Total Sales Salary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides total sales salary information.
- **Key Components**: Total Sales Salary, Average Employees, Average Salary, Total Wages
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Includes both annual and monthly time series data.

---

## Clients CTRL

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and sheet title.
- **Key Components**: Company Name, Sheet Name, Scenario Description
- **Notes & Customizations**: Simple header information.

### Clients Control - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays financial metrics related to client acquisition and churn, broken down by different client size segments.
- **Key Components**: New Booked ARR per New Client, Churned ARR per Lost Client, % ARR Churn Attributable to Lost Clients, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000. The "x" in column A seems to be a placeholder or indicator.

### Clients Control - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays financial metrics related to client acquisition and churn, broken down by different client size segments.
- **Key Components**: New Booked ARR per New Client, Churned ARR per Lost Client, % ARR Churn Attributable to Lost Clients, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000. The "x" in column A seems to be a placeholder or indicator.

### Clients Control - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays financial metrics related to client acquisition and churn, broken down by different client size segments.
- **Key Components**: New Booked ARR per New Client, Churned ARR per Lost Client, % ARR Churn Attributable to Lost Clients, Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000. The "x" in column A seems to be a placeholder or indicator.

---

## Clients

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario.
- **Key Components**: Company Name, Report Title, Scenario
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series.

### Clients Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes key client metrics like beginning clients, new clients, churned clients, and ending clients.
- **Key Components**: Beginning Clients, New Added, Churned, Ending Clients
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series.

### Clients Detail - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of client metrics related to financial performance, such as new booked ARR and churned ARR.
- **Key Components**: New Booked ARR - New Clients, Clients Added, New Booked ARR per New Client, Churned ARR - Lost Clients, Clients Lost, Churned ARR per Lost Client, Total Churned ARR, Churned ARR Attributable to Lost Clients, % of Churned ARR Attributable to Lost Clients
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series.

### Client Detail - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of client metrics related to corporate clients.
- **Key Components**: Beginning Clients, New Added, Churned, Ending Clients, New Booked ARR - New Clients, Clients Added, New Booked ARR per New Client, Churned ARR - Lost Clients, Clients Lost, Churned ARR per Lost Client, Total Churned ARR, Churned ARR Attributable to Lost Clients, % of Churned ARR Attributable to Lost Clients
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series.

### Client Detail - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of client metrics related to other client types.
- **Key Components**: Beginning Clients, New Added, Churned, Ending Clients, New Booked ARR - New Clients, Clients Added, New Booked ARR per New Client, Churned ARR - Lost Clients, Clients Lost, Churned ARR per Lost Client, Total Churned ARR, Churned ARR Attributable to Lost Clients, % of Churned ARR Attributable to Lost Clients
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series. The range `T64:CI64` and `CJ64:FS64` are separate monthly data ranges for "Churned ARR per Lost Client".

---

## Retention CTRL

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains company name, report name, and scenario description.
- **Key Components**: Company Name, Report Name, Scenario Description
- **Notes & Customizations**: Contains the scenario name, such as "1 - Base - $25mm".

### Annual Retention - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention percentages for different revenue scenarios.
- **Key Components**: Revenue, Annual Retention % - Financial, "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Evergreen Retention - Financial (Annual Equivalent)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays evergreen retention percentages (annual equivalent) for different revenue scenarios.
- **Key Components**: Evergreen Retention % - Financial (Annual Equivalent), "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Annual Retention - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention percentages for different revenue scenarios.
- **Key Components**: Annual Retention % - Corporate, "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Annual Retention - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention percentages for different revenue scenarios.
- **Key Components**: Annual Retention % - Other, "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Evergreen Retention - Other (Annual Equivalent)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays evergreen retention percentages (annual equivalent) for different revenue scenarios.
- **Key Components**: Evergreen Retention % - Other (Annual Equivalent), "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Retention percentages are scaled by 1000.

---

## Retention

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the data.
- **Key Components**: Company Name, Data Description, Time Series Headers.
- **Time Range**: Annual: 2010-2014
- **Notes & Customizations**: Contains both annual and monthly time series data.

### Financial Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Financial segment, including churn and retention percentages.
- **Key Components**: Churn, Total Churn, Financial, Blended Retention %.
- **Time Range**: Annual: 2010-2021
- **Notes & Customizations**: Data is scaled by 1000.

### Corporate Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Corporate segment.
- **Key Components**: Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal.
- **Time Range**: Annual: 2010-2021
- **Notes & Customizations**: Data is scaled by 1000. Contains "Annual Financial Up for Renewal" section with data in J33:Q33 and CI33:FS33.

### Corporate Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Corporate segment.
- **Key Components**: Total Corporate Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal.
- **Time Range**: Annual: 2010-2021
- **Notes & Customizations**: Data is scaled by 1000. Contains "Annual Up for Renewal" section with data in J52:Q52 and CI52:FS52.

### Other Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the retention details for the Other segment.
- **Key Components**: Total Other Up for Renewal, Retention %, Renewed, Churned, New Bookings, Previous Renewal.
- **Time Range**: Annual: 2010-2021
- **Notes & Customizations**: Data is scaled by 1000. Contains "Annual Other Up for Renewal" section with data in J71:Q71 and CI71:FS71.

### Summary Retention Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of retention metrics.
- **Key Components**: Up for Renewal, Retention %, Renewed, Churned.
- **Time Range**: Annual: 2010-2021
- **Notes & Customizations**: Data is scaled by 1000.

---

## Renewed

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains header information like account type, ASV, effective date, close date, segment, and notes.
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage, Segement Key, Hedge Fund, Financial, Renewal, Renewal - Won, Independent Research Firm, Other, Corporate, Research & Advisory, Broker Partner, Renewal - Lost, Investment Manager (long only), Private Equity, Law Firm, Family Office, Corporate - Agency, Financial (Research/IB), Bank, Regulator, Private Wealth, Endowment, Sell Side (Research/IB), Renewal (contract/email required), Evergreen, Renewal (full term), Renewal (default), Pending Cancel (notice given), Pending Partial Cancel, Renewal (low probability)
- **Notes & Customizations**: Contains a note to update the information by taking the ASV tab on the Sales Worksheet.

### Renewal Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains the actual renewal data, including account type, ASV, effective date, close date, segment, and other related information.
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage
- **Notes & Customizations**: The data is related to the renewal process and includes information about the stage of the renewal.

---

## Renewal Base

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the column headers for the renewal data.
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage
- **Notes & Customizations**: None

### Renewal Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains the renewal data for each account, including ASV, effective dates, close dates, and other relevant information.
- **Key Components**: Account Type, ASV, Effective Date, Close Date, Segment, EOM Effective Date, EOM Close Date, AlphaSense Opp #, Renewal Type, Stage
- **Notes & Customizations**: Effective Date, Close Date, EOM Effective Date, and EOM Close Date are unordered date series.

---

## Deferred Build

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and report title.
- **Key Components**: Company Name, Report Title, Dates
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series.

### Deferred Revenue Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes the deferred revenue balance and its components.
- **Key Components**: ARR, Deferred Beginning Balance, Add (Projected), Recognized as Revenue (Projected), Deferred Ending Balance, % of ARR
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series. Values are scaled by 1000.

### Deferred Revenue Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of the additions to the deferred revenue balance.
- **Key Components**: ARR Added (Bookings, Renewals), Total ARR Added Previous Month, Added to Deferred Revenue Balance (Bookings, Renewals), Total Added to Deferred Revenue Balance
- **Time Range**: Monthly: 2019-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Revenue Recognition
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the revenue recognized from various sources.
- **Key Components**: Revenue, Bookings Revenue Recognized, Renewal Revenue Recognized, Revenue from Deferred Revenue Balance
- **Time Range**: Monthly: 2019-2027
- **Notes & Customizations**: Values are scaled by 1000.

---

## Headcount and Salaries CTRL

### Headcount and Salaries Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the headcount and ARR assumptions for various departments within AlphaSense, Inc. It provides a breakdown of headcount added in each period and ARR generated per head, serving as a basis for financial projections.
- **Key Components**: Total Headcount, Executive, Engineering, Product, Marketing, Content, Finance, HR, and Operations, Engineering/Ops - India, ARR per head.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: ARR per head is calculated for different departments. Some calculations are based on 2018 or 2019 drivers, indicating a change in methodology over time.

### Salary Calculations
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the salary calculations for various departments within AlphaSense, Inc. It includes average salaries and annual increases, providing a basis for expense projections.
- **Key Components**: Average Salaries, Annual Increase, Executive Salary, Engineering Salary, Product Salary, Marketing Salary, Content Salary, Finance, HR, Operations Salary, Engineering/Ops - India Salary.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Salary calculations are provided for different departments, with annual increases factored in.

---

## Headcount and Salaries

### Section Name: Headcount and Salaries Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of headcount across different departments. It's used to track the overall size and composition of the workforce.
- **Key Components**: Headcount for Executive, Engineering, Product, Sales, Marketing, Content, Finance & Admin, Engineering/Ops - India, Total Headcount.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Memo: Average Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides average headcount across different departments.
- **Key Components**: Average Headcount for Executive, Engineering, Product, Sales, Marketing, Content, Finance, HR, and Operations, Engineering/Ops - India, Total Headcount.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Salary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides salary information for different departments.
- **Key Components**: Salary for Executive, Engineering, Product, Sales, Marketing, Content, Finance & Admin, Engineering/Ops - India, Total Salary, Total Salary (excl. India).
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Salary per Head
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides salary per head information for different departments.
- **Key Components**: Salary per Head for Executive, Engineering, Product, Sales, Marketing, Content, Finance & Admin, Engineering/Ops - India, Total Salary per Head.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Headcount Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed headcount information, including beginning of period, added, and end of period counts.
- **Key Components**: Beginning of Period, Added, End of Period, ARR per Head, ARR, Net Added.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Salaries Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides detailed salary information, including average employees, average salary, and total wages.
- **Key Components**: Average Employees, Average Salary, Total Wages.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Values are scaled by 1000.

---

## Opex CTRL

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Key Components**: AlphaSense, Inc., Operating Expenses CTRL, 1 - Base - $25mm
- **Notes & Customizations**: None

### Operating Expenses Inputs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains the operating expense inputs, including various cost categories and their corresponding values over time. It allows for scenario planning and expense forecasting.
- **Key Components**: Other Employee Costs - % of Wages, Travel - % of Wages, Other Costs (Airplane) - % of Wages, Other Facilities Cost - % of Rent, Marketing Cost - Spend per Booked Dollar, Non-Salary G&A Costs per Head, Legal Fees - Yearly $ Amount, Engineering Headcount Growth - 2018B, Other Costs - % YoY Growth, Salaries Working Abroad - % of Wages, Holiday Pay - % of Wages, Additional Holiday Pay - % of Wages, Sick Leave - % of Wages, President's Club - Annual Fee, Other Incentives, Commissions %, Bonus per Head, Benefits - % of Wages, Payroll Taxes - % of Wages, Relocation Fee - Buffer, Contractors, Capitalized Wages - % of Engineering Salaries, Workers Compensation per Employee, Recruiter Fees  - $ per Added Head, Stock Based Compensaiton, Rent Expense per Employee, Professional Services Growth Rate, Web Service Expense per Engineering Employee per Month, Bad Debt Expense % of Revenue, Company Wide Opex Inputs, Rent - Buffer, Rent - Park 215, Rent - NYC - 5th Floor, Rent - NYC - 6th Floor, Rent - Helsinki, Rent - Pune, Rent - Mumbai, Rent - Stamford, Rent - SF, Rent - Boston WeWork, Rent - Chicago WeWork, Rent - London WeWork, Rent - Charleston WeWork, Rent - North Carolina WeWork, CAM, Repairs & Maintenance, Amoritzation of Leasehold Improvements, Utilities, Telephone, Computer & Internet, Insurance, Payroll & Benefit Admin, Postage & Delivery, Furniture, Hardware, Office Supplies, Bank Fees, Fundraising, Miscellaneous, DataFeeds, Penalties, Bad Debt, Depreciation Expense, Amortization of Capitalized R&D, Subsidy Received, Other Income, Income Taxes, Other Taxes, Other Taxes - Non Deductible, Interest Income, Interest Expense, Gain / (Loss) on FX, Sales Opex Monthly Inputs, Product Opex Monthly Inputs, Marketing Opex Monthly Inputs, Finance & People Opex Monthly Inputs, Executive Opex Monthly Inputs, Engineering Opex Monthly Inputs
- **Notes & Customizations**: The section contains both annual and monthly time series data, with many rows representing percentages or cost per employee metrics. Several rows also have "Buffer" in their name, indicating they are used for scenario planning.

---

## Operating Expenses

### Section Name (Operating Expenses Summary)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of operating expenses, including key categories like People Costs, Travel, Facilities Costs, Marketing, and General & Administrative. It allows for quick overview and comparison of expense trends over time.
- **Key Components**: Operating Expenses, People Costs, Other Employee Costs, Travel, Facilities Costs, Rental Income, Marketing, General and Administrative, Legal, Other Costs, Total Operating Expenses, % YoY Growth.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Expenses are presented in thousands. The "% YoY Growth" calculation starts from column F (2016) for annual data and AF (2016-01-31) for monthly data.

### Section Name (Operating Expenses Detail)
- **Section Type**: Custom P&L
- **Description & Purpose**: Provides a detailed breakdown of operating expenses, drilling down into sub-categories within each major expense area (e.g., People Costs broken down into Salaries, Benefits, Payroll Taxes, etc.). This section allows for granular analysis of cost drivers.
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Commission, Stock Based Compensation, Bonus, Benefits, Payroll Taxes, Recruiting Fees, Contractors, Capitalized Wages, Cellular Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals, Daily Meal Allowance When Abroad, Business Meals, Internal Events, Rent, CAM, Repairs & Maintenance, Utilities, Telephone, Computer & Internet, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising Fees, Miscellaneous, DataFeeds, Web Service, Penalties, Bad Debt, Headcount.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Expenses are presented in thousands. Some rows have additional calculations or percentages (e.g., "% of Wages", "Marketing Cost per Booking"). There are some rows with split monthly data (e.g. E27:Q27, T27:CI27, CJ27:FS27).

---

## Content

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Key Components**: AlphaSense, Inc., Operating Expenses Reorganization, 1 - Base - $25mm
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series data.

### Content Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of total content expenses.
- **Key Components**: Total Content Expense
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content People Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes total people costs associated with content creation.
- **Key Components**: Total Content People Costs, Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finnish Side Costs, Share Based Compensation
- **Notes & Customizations**: Values are scaled by 1000. Includes various sub-categories of people costs.

### Total Content Other Employee Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes other employee costs associated with content creation.
- **Key Components**: Total Content Other Employee Costs, Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content Travel Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes travel costs associated with content creation.
- **Key Components**: Total Content Travel Costs, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content Facility Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes facility costs associated with content creation.
- **Key Components**: Total Content Facility Costs, Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content Marketing
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes marketing costs associated with content creation.
- **Key Components**: Total Content Marketing, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content General & Admin
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes general and administrative costs associated with content creation.
- **Key Components**: Total Content General & Admin, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising, Miscellaneous
- **Notes & Customizations**: Values are scaled by 1000.

### Total Content Other Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes other costs associated with content creation.
- **Key Components**: Total Content Other Costs, Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt
- **Notes & Customizations**: Values are scaled by 1000.

---

## Engineering

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario information.
- **Key Components**: Company Name, Report Title, Scenario.
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series.

### Engineering Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of total engineering expenses.
- **Key Components**: Total Engineering Expense, Total Engineering People Costs, Total Engineering People Costs (excl Cap Wages).
- **Time Range**: Annual: 2019-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering People Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering people costs.
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finnish Side Costs, Share Based Compensation.
- **Time Range**: Annual: 2019-2027
- **Notes & Customizations**: Values are scaled by 1000, except for I56:K56.

### Engineering Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of other engineering employee costs.
- **Key Components**: Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions.
- **Time Range**: Annual: 2019-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Travel Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering travel costs.
- **Key Components**: Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Business Meals / Entertainment.
- **Time Range**: Annual: 2019-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Facility Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering facility costs.
- **Key Components**: Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet.
- **Time Range**: Annual: 2019-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Marketing
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering marketing expenses.
- **Key Components**: Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG.
- **Time Range**: Annual: 2019-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering General & Admin
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of engineering general and administrative expenses.
- **Key Components**: Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees.
- **Time Range**: Annual: 2019-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Engineering Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various components of other engineering expenses.
- **Key Components**: Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt.
- **Time Range**: Annual: 2019-2027
- **Notes & Customizations**: Values are scaled by 1000.

---

## Executive

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description. Provides context for the entire spreadsheet.
- **Key Components**: AlphaSense, Inc., Operating Expenses Reorganization, 1 - Base - $25mm
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains the title of the report and a scenario description.

### Section Name: Executive Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of total executive expenses.
- **Key Components**: Executive Operating Expenses Summary, Total Executive Expense
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive People Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of executive people costs, including wages, benefits, and other related expenses.
- **Key Components**: Total Executive People Costs, Wages, Executive Wages, Salaries Working Abroad, Executive Salaries Working Abroad, Holiday Pay, Executive Holiday Pay, Additional Holiday Pay, Executive Additional Holiday Pay, Sick Leave, Executive Sick Leave, Commission Expense, Bonus, Executive Bonus, Benefits, Executive Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation, Headcount, Cost Per Head.
- **Notes & Customizations**: Values are scaled by 1000. Includes calculations for % of Wages.

### Section Name: Executive Other Employee Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of other employee costs, including cell phone service, internet, and home office expenses.
- **Key Components**: Total Executive Other Employee Costs, Celluar Phone Service, Executive Celluar Phone Service, Home Internet Service, Executive Home Internet Service, Home Office Phone, Executive Home Office Phone, Home Office, Executive Home Office, Membership Dues, Executive Membership Dues, Subscriptions, Executive Subscriptions.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive Travel Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of executive travel costs, including airfare, auto/cab, lodging, and meals.
- **Key Components**: Total Executive Travel Costs, Airfare/Train, Executive Airfare/Train, Auto/Cab, Executive Auto/Cab, Mileage, Executive Mileage, Lodging, Executive Lodging, Travel Internet, Executive Travel Internet, Employee Meals / Entertainment, Executive Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Content Daily Mail Allowance When Abroad, Business Meals / Entertainment, Executive Business Meals / Entertainment.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive Facility Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of executive facility costs, including rent, CAM, and utilities.
- **Key Components**: Total Executive Facility Costs, Rent, Executive Rent, CAM, Executive CAM, Repairs & Maintenance, Executive Repairs & Maintenance, Amortization of Leasehold Improvements, Executive Amortization of Leasehold Improvements, Utilities, Executive Utilities, Telephone, Executive Telephone, Computer & Internet, Executive Computer & Internet.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive Marketing
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of executive marketing expenses, including advertising, research, and events.
- **Key Components**: Total Executive Marketing, Advertising & Promotion, Executive Advertising & Promotion, Other Marketing, Executive Other Marketing, Omarketing Research, Executive Omarketing Research, Marketing Events, Executive Marketing Events, Public Relations, Executive Public Relations, Paid Search, Executive Paid Search, Paid Social, Executive Paid Social, Paid Display, Executive Paid Display, Paid SWAG, Executive SWAG.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive General & Admin
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of executive general and administrative expenses, including insurance, payroll admin, and office supplies.
- **Key Components**: Total Executive General & Admin, Payroll & Benefit Admin, Executive Payroll & Benefit Admin, Postage & Delivery, Executive Postage & Delivery, Conference & Meetings, Executive Conference & Meetings, Furniture, Executive Furniture, Hardware, Executive Hardware, Software, Executive Software, Office Supplies, Executive Office Supplies.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Executive Other Costs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the components of other executive costs, including legal fees, data feeds, and web services.
- **Key Components**: Total Executive Other Costs, DataFeeds, Executive DataFeeds, Web Service, Executive Web Service, Penalties, Executive Penalties, Bad Debt, Executive Bad Debt.
- **Notes & Customizations**: Values are scaled by 1000.

---

## Finance & Admin

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and a brief description of the report.
- **Key Components**: Company Name, Report Title, Scenario Description.
- **Notes & Customizations**: None

### Finance & Admin Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of the total Finance & Admin expenses.
- **Key Components**: Total Finance & Admin Expense, Total Finance & Admin Expense (excl Cap Wages), Total Finance & Admin Admin Costs, Total Engineering Admin Costs (excl Cap Wages)
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various employee-related costs for the Finance & Admin department.
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Recruiting Fees
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various recruiting fees for the Finance & Admin department.
- **Key Components**: Recruiting Fees, Finance & Admin Recruiting Fees
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Relocation
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the relocation costs for the Finance & Admin department.
- **Key Components**: Relocation, Finance & Admin Relocation
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Contractors
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the contractor costs for the Finance & Admin department.
- **Key Components**: Contractors, Finance & Admin Contractors
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Outsourced R&D
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the outsourced R&D costs for the Finance & Admin department.
- **Key Components**: Outsourced R&D, Finance & Admin Outsourced R&D
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Capitalized R&D
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the capitalized R&D costs for the Finance & Admin department.
- **Key Components**: Capitalized Wages, Capitalized Outsourced R&D, Capitalized R&D
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the other employee costs for the Finance & Admin department.
- **Key Components**: Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Travel Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the travel costs for the Finance & Admin department.
- **Key Components**: Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Facility Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the facility costs for the Finance & Admin department.
- **Key Components**: Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Rental Income
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the rental income for the Finance & Admin department.
- **Key Components**: Rental Income, Finance & Admin Rental Income
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Marketing
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the marketing expenses for the Finance & Admin department.
- **Key Components**: Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin General & Admin
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the general and administrative expenses for the Finance & Admin department.
- **Key Components**: Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies
- **Notes & Customizations**: Values are scaled by 1000.

### Finance & Admin Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the other costs for the Finance & Admin department.
- **Key Components**: Audit & Tax, Bank Fees, Professional Services, Fundraising, Miscellaneous, Legal Fees, DataFeeds, Web Service, Penalties
- **Notes & Customizations**: Values are scaled by 1000.

### Bad Debt
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the bad debt expenses for the Finance & Admin department.
- **Key Components**: Bad Debt, Finance & Admin Bad Debt
- **Notes & Customizations**: Values are scaled by 1000.

---

## Marketing

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and budget information.
- **Key Components**: Company Name, Report Title, Budget Amount
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series.

### Marketing Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of total marketing expenses.
- **Key Components**: Total Marketing Expense, Total Marketing People Costs
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing People Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of marketing people costs, including wages, benefits, and related expenses.
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation
- **Notes & Customizations**: Uses a scale of 1000 for the values. Includes "% of Wages" calculations.

### Marketing Other Employee Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of other employee costs, such as phone service, internet, and home office expenses.
- **Key Components**: Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Travel Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of travel costs, including airfare, auto, lodging, and meals.
- **Key Components**: Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Business Meals / Entertainment
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Facility Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of facility costs, including rent, CAM, and utilities.
- **Key Components**: Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Expenses Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of marketing expenses, including advertising, research, and events.
- **Key Components**: Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing General & Admin Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of general and administrative expenses.
- **Key Components**: Insurance, Payroll & Benefit Admin, Postage & Delivery, Furniture, Hardware, Software
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Other Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of other costs, including legal fees, data feeds, and web services.
- **Key Components**: Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt
- **Notes & Customizations**: Uses a scale of 1000 for the values.

---

## Product

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and scenario description.
- **Key Components**: Company Name, Report Title, Scenario Description.
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Includes a scenario description "1 - Base - $25mm".

### Product Operating Expenses Summary
- **Section Type**: Custom P&L
- **Description & Purpose**: Detailed breakdown of Product Operating Expenses, including people costs, facility costs, marketing expenses, and other costs.
- **Key Components**: Total Product Expense, Total Product People Costs, Wages, Salaries Working Abroad, Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finnish Side Costs, Share Based Compensation, Recruiting Fees, Relocation, Contractors, Outsourced R&D, Capitalized Wages, Capitalized Outsourced R&D, Capitalized R&D, Total Product Other Employee Costs, Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office, Total Product Travel Costs, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Business Meals / Entertainment, Internal Events, Total Product Facility Costs, Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet, Total Product Marketing, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG, Total Product General & Admin, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising, Miscellaneous, Total Product Other Costs, Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt.
- **Time Range**: Annual: 2019-2027
- **Notes & Customizations**: Expenses are broken down by category (People Costs, Facility Costs, Marketing, etc.) and then further broken down into specific line items. Many line items have a "Product" prefix, indicating the allocation of costs to the Product department. Values are scaled by 1000.

---

## Sales

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and date information. Provides context for the entire spreadsheet.
- **Key Components**: AlphaSense, Inc., Operating Expenses Reorganization, 1 - Base - $25mm
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Contains both annual and monthly time series data.

### Sales Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of total sales expenses.
- **Key Components**: Sales Operating Expenses Summary, Total Sales Expense
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales People Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the costs associated with sales personnel, including wages, benefits, and payroll taxes.
- **Key Components**: Total Sales People Costs, Wages, Sales Wages, Salaries Working Abroad, Sales Salaries Working Abroad, Holiday Pay, Sales Holiday Pay, Additional Holiday Pay, Sales Additional Holiday Pay, Sick Leave, Sales Sick Leave, Commission Expense, Bonus, Sales Bonus, Benefits, Sales Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation, Cost Per Head, Sales Worker Compensation
- **Notes & Customizations**: Totals are scaled by 1000. Includes calculations based on "% of Wages".

### Sales Other Employee Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other employee costs such as cell phone service, home internet, home office expenses, and subscriptions.
- **Key Components**: Total Sales Other Employee Costs, Celluar Phone Service, Sales Celluar Phone Service, Home Internet Service, Sales Home Internet Service, Home Office Phone, Sales Home Office Phone, Home Office, Sales Home Office, Membership Dues, Sales Membership Dues, Subscriptions, Sales Subscriptions
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales Travel Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details travel-related costs for the sales team.
- **Key Components**: Total Sales Travel Costs, Airfare/Train, Sales Airfare/Train, Auto/Cab, Sales Auto/Cab, Mileage, Sales Mileage, Lodging, Sales Lodging, Travel Internet, Sales Travel Internet, Employee Meals / Entertainment, Sales Employee Meals / Entertainment, Daily Meal Allowance When Abroad, Content Daily Mail Allowance When Abroad, Business Meals / Entertainment, Sales Business Meals / Entertainment
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales Facility Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details facility-related costs allocated to the sales team.
- **Key Components**: Total Sales Facility Costs, Rent, Sales Rent, CAM, Sales CAM, Repairs & Maintenance, Sales Repairs & Maintenance, Amortization of Leasehold Improvements, Sales Amortization of Leasehold Improvements, Utilities, Sales Utilities, Telephone, Sales Telephone, Computer & Internet, Sales Computer & Internet
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales Marketing
- **Section Type**: Standard P&L
- **Description & Purpose**: Details marketing expenses for the sales team.
- **Key Components**: Total Sales Marketing, Advertising & Promotion, Sales Advertising & Promotion, Other Marketing, Sales Other Marketing, Omarketing Research, Sales Omarketing Research, Marketing Events, Sales Marketing Events, Public Relations, Sales Public Relations, Paid Search, Sales Paid Search, Paid Social, Sales Paid Social, Paid Display, Sales Paid Display, Paid SWAG, Sales SWAG
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales General & Admin
- **Section Type**: Standard P&L
- **Description & Purpose**: Details general and administrative expenses allocated to the sales team.
- **Key Components**: Total Sales General & Admin, Insurance, Sales Insurance, Payroll & Benefit Admin, Sales Payroll & Benefit Admin, Postage & Delivery, Sales Postage & Delivery, Conferences & Meetings, Sales Conference & Meetings, Furniture, Sales Furniture, Hardware, Sales Hardware, Software, Sales Software
- **Notes & Customizations**: Totals are scaled by 1000.

### Sales Other Costs
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other costs allocated to the sales team.
- **Key Components**: Total Sales Other Costs, Legal Fees, Sales Legal Fees, DataFeeds, Sales DataFeeds, Web Service, Sales Web Service, Penalties, Sales Penalties, Bad Debt, Sales Bad Debt
- **Notes & Customizations**: Totals are scaled by 1000.

---

## Commission Waterfall

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and report title.
- **Key Components**: Company Name, Report Title, Scenario Description
- **Notes & Customizations**: None

### Commissions Expense Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of commissions expense, including bonus expense and total commission expense. It also includes bookings data and commission percentages.
- **Key Components**: Commissions Expense, Bonus Expense, Total Commission Expense, Financial Bookings, Corporate Bookings, Other Bookings, Commission Percentages, Financial Commission, Corporate Commission, Other Commission, Sales Manager Commission.
- **Time Range**: Annual: 2015-2021, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### Financial Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of financial commissions over time.
- **Key Components**: Months, Commission values
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### Corporate Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of corporate commissions over time.
- **Key Components**: Months, Commission values
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### Other Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of other commissions over time.
- **Key Components**: Months, Commission values
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### AE Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: Details the waterfall of AE commissions over time.
- **Key Components**: Months, Commission values
- **Time Range**: Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### Commissions Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of commissions expense, including bonus expense and total commission expense.
- **Key Components**: Commissions Expense, Bonus Expense, Total Commission Expense
- **Time Range**: Annual: 2015-2021, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

---

## Bad Debt

### Section Name (Reconciliation Header)
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the reconciliation.
- **Key Components**: Title: "ADFDA Reconciliation 2020"
- **Notes & Customizations**: None

### Section Name (AFDA Reconciliation)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section reconciles the Allowance for Doubtful Accounts (AFDA) balance between two sources (WP and Intacct) over a monthly time series.
- **Key Components**: ADFA beg balance per WP, ADFA beg balance per Intacct, Invoices written-off/collected, AFDA balance before adj, A/R ending balance per Intacct, AFDA as % of A/R to be maintained, Amount to be added to AFDA, AFDA end balance per WP, ADFA end balance per Intacct, Difference.
- **Notes & Customizations**: Values are scaled by 1000. Includes a calculation for "AFDA as % of A/R to be maintained" and an adjustment to the AFDA balance.

---

## COGS CTRL

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name and the title of the spreadsheet.
- **Key Components**: AlphaSense, Inc., Cost of Goods Sold CTRL, 1 - Base - $25mm
- **Notes & Customizations**: None

### User Percentage Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the percentage of users for various categories (Financial, Corporate, Other) across different products and user segments.
- **Key Components**: Trend of Net Add Users, Financial BRM Users - % of Total Financial Users, Corporate BRM Users - % of Total Corporate Users, Other BRM Users - % of Total Other Users, Financial TR Transcripts Users - % of Total Financial Users, Corporate TR Transcripts Users - % of Total Corporate Users, Other TR Transcripts Users - % of Total Other Users, Financial FactSet Transcripts Users - % of Total Financial Users, Corporate FactSet Transcripts Users - % of Total Corporate Users, Other FactSet Transcripts Users - % of Total Other Users, Financial DJ Users - % of Total Financial, Corporate DJ Users - % of Total Corporate, Other DJ Users - % of Total Other, Financial AMR ($15k Users) - % of Total Financial, Corporate AMR ($15k Users) - % of Total Corporate, Other AMR ($15k Users) - % of Total Other, Financial AMR ($30k Users) - % of Total Financial, Corporate AMR ($30k Users) - % of Total Corporate, Other AMR ($30k Users) - % of Total Other, Financial Lexis Nexis Users - % of Total Financial, Corporate Lexis Nexis Users - % of Total Corporate, Other Lexis Nexis Users - % of Total Other, Financial International Filings Users - % of Total Financial, Corporate International Filings Users - % of Total Corporate, Other International Filings Users - % of Total Other, FactSet RT Users - % of Total Financial, FactSet RT Users - % of Total Corporate, FactSet RT Users - % of Total Other, FactSet AMR Users - % of Total Financial, FactSet AMR Users - % of Total Corporate, FactSet AMR Users - % of Total Other, Broker Partners - % Growth
- **Notes & Customizations**: Data is scaled by 1000.

### Product Cost Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the assumptions used for product costs, including ramp assumptions for global and single-region users, and cost per user for global and single research.
- **Key Components**: Broker Research Module, Ramp Assumption - Global Users, Ramp Assumption - Global Users Base, Ramp Assumption - Global Users Upside, Ramp Assumption - Single Region Users, Ramp Assumption - Single Region Users Base, Ramp Assumption - Single Region Users Upside, Global Research (1-10) Cost Per User, Global Research (11-50) Cost Per User, Global Research (50+) Cost Per User, Global Research (1-10) % Cost Per User, Global Research (11-50) % Cost Per User, Global Research (50+) % Cost Per User, Single Research (1-10) Cost Per User, Single Research (11-25) Cost Per User, Single Research (26-50) Cost Per User, Single Research (51+) Cost Per User, Single Research (1-10) % Cost Per User, Single Research (11-25) % Cost Per User, Single Research (26-50) % Cost Per User, Single Research (51+) % Cost Per User, TR Minimum, TR New Contract - Minimum Payment, TR New Contract - Minimum Payment Base, TR New Contract - Minimum Payment Upside, TR New Contract - Minimum Users, TR New Contract - Price per Additional User, FactSet Minimum, After Market Research, AMR $15k Cost per User, AMR $30k Cost per User, AMR - % on TR, AMR - % on TR Base, AMR - % on TR Upside, TR AMR Minimum Fee, AMR TR Alternative Cost per User, AMR TR Alternative Cost - Minimum, TR to FactSet AMR Conversion
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### International Filings Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with international filings, including percentages, user limits, and prices for different tiers.
- **Key Components**: International Filing Expense - % of Non Paying Brokers, International Filing Expense - Tier 1 User Limit, International Filing Expense - Tier 1 Price, International Filing Expense - Tier 2 User Limit, International Filing Expense - Tier 2 Price, International Filing Expense - Tier 3 User Limit, International Filing Expense - Tier 3 Price, International Filing Expense - Tier 4 User Limit, International Filing Expense - Tier 4 Price, International Filing Expense - Tier 5 User Limit, International Filing Expense - Tier 5 Price, International Filing Expense - Price Per User in Excess
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### Transcripts Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with transcripts, including percentages, user limits, and prices for different tiers.
- **Key Components**: TR Transcript Expense - % of Non Paying Brokers, TR Transcript Expense - Tier 1 User Limit, TR Transcript Expense - Tier 1 Price, TR Transcript Expense - Tier 2 User Limit, TR Transcript Expense - Tier 2 Price, TR Transcript Expense - Tier 3 User Limit, TR Transcript Expense - Tier 3 Price, TR Transcript Expense - Tier 4 User Limit, TR Transcript Expense - Tier 4 Price, TR Transcript Expense - Tier 5 User Limit, TR Transcript Expense - Tier 5 Price, TR Transcript Expense - Tier 6 User Limit, TR Transcript Expense - Tier 6 Price, TR Transcript Expense - Tier 7 User Limit, TR Transcript Expense - Tier 7 Price, TR Transcript Expense - Tier 8 User Limit, TR Transcript Expense - Tier 8 Price, TR Transcript Expense - Excess Price, FactSet Transcript Expense - % of Non Paying Brokers, FactSet Transcript Expense - User Limit, FactSet Transcript Expense - Fee Minimum, FactSet Transcript Expense - Global % of Excess Users, FactSet Transcript Expense - Fee per Excess Global User, FactSet Transcript Expense - Regional % of Excess Users, FactSet Transcript Expense - Fee per Excess Regional User
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### Dow Jones Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with Dow Jones, including user limits, prices for different tiers, and admin fees.
- **Key Components**: Dow Jones - Base, Dow Jones Expense - Fee Minimum, Dow Jones Expense - Tier 1 User Limit, Dow Jones Expense - Tier 1 Price, Dow Jones Expense - Tier 2 User Limit, Dow Jones Expense - Tier 2 Price, Dow Jones Expense - Tier 3 User Limit, Dow Jones Expense - Tier 3 Price, Dow Jones Expense - Admin Fee, Dow Jones Expense - Tier 1 Monthly Fee, Dow Jones Expense - Tier 2 Monthly Fee, Dow Jones Expense - Tier 3 Monthly Fee, Dow Jones Expense - Tier 4 User Limit, Dow Jones Expense - Tier 4 Monthly Fee, Dow Jones Expense - Tier 5 User Limit, Dow Jones Expense - Tier 5 Monthly Fee, Dow Jones Expense - Tier 6 User Limit, Dow Jones Expense - Tier 6 Monthly Fee, Dow Jones Expense - Tier 7 User Limit, Dow Jones Expense - Tier 7 Monthly Fee, Dow Jones Expense - Tier 8 User Limit, Dow Jones Expense - Tier 8 Monthly Fee, Dow Jones Expense - Tier 9 User Limit, Dow Jones Expense - Tier 9 Monthly Fee, Dow Jones Expense - Tier 10 User Limit, Dow Jones Expense - Tier 10 Monthly Fee, Dow Jones Expense - Tier 11 User Limit, Dow Jones Expense - Tier 11 Monthly Fee, Dow Jones Expense - Tier 12 User Limit, Dow Jones Expense - Tier 12 Monthly Fee, Dow Jones Expense - Tier 13 User Limit, Dow Jones Expense - Tier 13 Monthly Fee, Dow Jones Expense - Tier 14 User Limit, Dow Jones Expense - Tier 14 Monthly Fee
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### News & Journals Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with News & Journals, including Lexis Nexis fees and user tiers, and Acquire 2 News expenses.
- **Key Components**: Lexis Nexis - Base Fee, Lexis Nexis - Base Users, Lexis Nexis - Tier 1 Users, Lexis Nexis - Tier 1 Price per User, Lexis Nexis - Tier 2 Users, Lexis Nexis - Tier 2 Price per User, Lexis Nexis - Tier 3 Price per User, Acquire 2 News Expense
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### IDC Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with IDC.
- **Key Components**: IDC Expense
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### Web Service Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with Web Service per user.
- **Key Components**: Web Service per User
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### Other Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with Other Additional Data Sources, including cost per year.
- **Key Components**: Other Additional Data Sources - Cost per Year, Other Additional Data Sources - Cost per Year Base, Other Additional Data Sources - Cost per Year Upside
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### ASR Expenses
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses associated with ASR, including pool contribution per user and direct consumption cost.
- **Key Components**: Pool Contribution per User, Direct Consumption Cost
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### Bernstein, Deutsche Bank, Barclays, HSBC, BOA, UBS, Morgan Stanley, Cowen, Autonomous, Evercore, Citi, Credit Suisse, JP Morgan, Raymond James, RBC Revenue Share and Minimums
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the usage, revenue share, and minimums for various brokers.
- **Key Components**: Bernstein Usage, Deutsche Bank Usage, Barclays Usage, HSBC Usage, BOA Usage, UBS Usage, Morgan Stanley Usage, Cowen Usage, Autonomous Usage, Evercore Usage, Citi Usage, Credit Suisse Usage, JP Morgan Usage, Raymond James Usage, RBC Usage, FactSet AMR Usage, FactSet RT Usage, Bernstein Revenue Share, Deutsche Bank Revenue Share, Barclays Revenue Share, HSBC Revenue Share, BOA Revenue Share, UBS Revenue Share, Morgan Stanley Revenue Share, Cowen Revenue Share, Autonomous Revenue Share, Evercore Revenue Share, Citi Revenue Share, Credit Suisse Revenue Share, JP Morgan Revenue Share, Raymond James Revenue Share, RBC Revenue Share, Bernstein Minimum, Deutsche Bank Minimum, Barclays Minimum, HSBC Minimum, BOA Minimum, UBS Minimum, Morgan Stanley Minimum, Cowen Minimum, Autonomous Minimum, Evercore Minimum, Citi Minimum, Credit Suisse Minimum, JP Morgan Minimum, Raymond James Minimum, RBC Minimum
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

### WSI FactSet Controls
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the WSI FactSet controls, including new user additions, active users, bookings per user, docs per user, and document costs.
- **Key Components**: WSI New User Additions - Corporate, WSI New User Additions - Financial, % of WSI New User Additions - Corporate (Professional Services), % of WSI New User Additions - Corporate (Pharma & Life Sciences), % of WSI New User Additions - Corporate (Tech, Media & Telecom), % of WSI New User Additions - Corporate (Energy & Utilities), % of WSI New User Additions - Corporate (Retail & Consumer Products), % of WSI New User Additions - Financial (Financial), % of Non-WSI Corporate Users Converted, % of WSI Users Active - Corporate (Professional Services), % of WSI Users Active - Corporate (Pharma & Life Sciences), % of WSI Users Active - Corporate (Tech, Media & Telecom), % of WSI Users Active - Corporate (Energy & Utilities), % of WSI Users Active - Corporate (Retail & Consumer Products), % of WSI Users Active - Financial (Financial), Docs per Active User per Month - (Professional Services), Docs per Active User per Month - (Pharma & Life Sciences), Docs per Active User per Month - (Tech, Media & Telecom), Docs per Active User per Month - (Energy & Utilities), Docs per Active User per Month - (Retail & Consumer Products), Docs per Active User per Month - (Financial), Consumption Reduction, Users Active, Bookings per Active Trialer, Bookings per Internal User, Docs per Active User, Docs per Trail User, Docs per Internal User, Internal Docs Minimum, Reduction, Total Document Minimum, Document Cost - Minimum, Document Cost - Excess, FactSet AMR Minimum, Total FactSet Minimum
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is scaled by 1000.

---

## Cost of Goods Sold

### Cost of Goods Sold Summary
- **Section Type**: Standard P&L
- **Description & Purpose**: Summarizes the various components contributing to the Cost of Goods Sold. It provides a high-level overview of expenses related to delivering the company's products and services.
- **Key Components**: Cost of Goods Sold, Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, IDC, Web Service - Production, Other Data, Total Cost of Goods Sold.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Product Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a summary of various product-related metrics. This section likely breaks down COGS by product category.
- **Key Components**: Broker Research, After Market Research, International Filings, Transcripts, News, News and Journals, Other Data, Total.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Product Summary - % of Revenue
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows product-related metrics as a percentage of revenue. This helps in understanding the relative contribution of each product to the overall cost structure.
- **Key Components**: Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, Other Data, Total COGS.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Total User Count
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the total number of users, broken down by category (Financial, Corporate, Other).
- **Key Components**: Users, Corporate , Other, Total Users.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Total User Net Adds
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the net additions of users, broken down by category (Financial, Corporate, Other).
- **Key Components**: Financial, Corporate, Other, Total Users.
- **Time Range**: Annual: 2017-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Product Detail Net Adds - Live Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of net user additions for live users, categorized by product.
- **Key Components**: TR Broker Research, Financial , % of  Financial Net Adds, % of  Corporate Net Adds, % of  Other Net Adds, TR Transcripts, Factset Transcripts, Dow Jones, AMR ($15k), AMR ($30k), Lexis Nexis, FactSet RT, FactSet AMR.
- **Time Range**: Annual: 2017-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series. Monthly data is split across multiple ranges in some rows.

### Product Detail - Live Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of live users, categorized by product.
- **Key Components**: TR Broker Research, Financial , % of Total Financial , % of Total Corporate, % of Total Other, TR Transcripts, Factset Transcripts, Dow Jones, AMR ($15k), AMR ($30k), Lexis Nexis, FactSet RT, FactSet AMR.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### TR Research - New Contract
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the terms and user counts associated with a new contract for TR Research.
- **Key Components**: Minimum Payment, Minimum Users, Minimum Price per User, Excess Over Minimum, Converted to FactSet, Additional TR Users, Price per Additional User, Additional TR Cost, Total TR Research, Total FS RT Users, % of Total Users.
- **Time Range**: Annual: 2019-2027, Monthly: 2019-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Factset Research
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a breakdown of Factset Research costs and user counts across different user tiers.
- **Key Components**: User Tiers, Cost, <500 Users, 500-750 Users, 750-1,000 Users, 1,000-1,500 Users, 1,500-2,500 Users, 2,500-3,500 Users, 3500-4500, 4500-7500, 7500-10000, 10000-12500, 12500-15000, 15000-20000, 20000-25000, 25000-35000, 35000-50000, 50000-75000, >75,000 Users, Converted from TR, FS RT users, FactSet Users (Average), FS BRM Expense, FactSet Minimum, Total FactSet Expense, Total Broker Research Expense, After Market Research Expense, User count - $15k package, User count - $30k package, TR AMR, TR - User count - $15k package, $15k - % TR, TR - User count - $30k package, $30k - % TR, TR - Co-Sell, Conversion %, AMR - $15k, Cost per User, AMR - $30k, Total TR Expense, FactSet, FS Minimum, FS - User Count, Check, TR Alt - Expense.
- **Time Range**: Annual: 2019-2027, Monthly: 2019-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Dow Jones News Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the expenses related to Dow Jones News.
- **Key Components**: Base Case, Minimum Fee, User count, Tier 1, Price per User, Tier 2, Tier 3, Tier 4, Tier 5, Admin Fee, Base Case Total.
- **Time Range**: Annual: 2019-2027, Monthly: 2019-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### COGS by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Breaks down the Cost of Goods Sold by different segments.
- **Key Components**: Cost of Goods Sold, Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, IDC, Web Service - Production, Other Data, Total Cost of Goods Sold.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### COGS Allocation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Allocates COGS across different categories or segments.
- **Key Components**: COGS Allocation, AMR Users, % of AMR Users, International Filings Users, % of Filings Users, Transcripts Users, % of Transcripts Users, DJ Users, % of Dow Jones Users, News and Journals Users, % of News and Journals Users, Other COGS, User Allocation, Total COGS.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### P&L
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents a simplified Profit & Loss statement.
- **Key Components**: P&L, Check.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### BRM
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to Broker Research Module (BRM).
- **Key Components**: BRM Users, Corporate, Other, Total, % of BRM Users.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### AMR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to After Market Research (AMR).
- **Key Components**: AMR Users, Corporate, Other, Total, % of AMR Users.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### International Filings Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to International Filings.
- **Key Components**: International Filings Users, Corporate, Other, Total, % of Filings Users.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Transcripts Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to Transcripts.
- **Key Components**: Transcripts Users, Corporate, Other, Total, % of Transcripts Users.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### News & Journals Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to News & Journals.
- **Key Components**: News and Journals Users, Corporate, Other, Total, % of News and Journals Users.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Dow Jones News Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to Dow Jones News.
- **Key Components**: DJ Users, Corporate, Other, Total, % of Dow Jones Users.
- **Time Range**: Annual: 2017-2027, Monthly: 2017-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### IDC Expense
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to IDC.
- **Key Components**: Total IDC.
- **Time Range**: Annual: 2019-2027, Monthly: 2019-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Web Service
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to Web Service.
- **Key Components**: Web Service.
- **Time Range**: Annual: 2019-2027, Monthly: 2019-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Other Additional Data Sources
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides metrics related to Other Additional Data Sources.
- **Key Components**: Other Additional Data Sources.
- **Time Range**: Annual: 2019-2027, Monthly: 2019-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Factset Research (Upside Case)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a breakdown of Factset Research costs and user counts across different user tiers under an Upside Case scenario.
- **Key Components**: Upside Case, Tier 1, Price, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6, Tier 7, Tier 8, Tier 9, Tier 10, Tier 11, Tier 12, Tier 13, Tier 14, Total Upside Case.
- **Time Range**: Annual: 2019-2027, Monthly: 2019-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### Lexis Nexis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a breakdown of Lexis Nexis costs and user counts across different user tiers.
- **Key Components**: News & Journals Expense, User count, Base Fees, Base Users, Tier 1, Price per User, Tier 2, Tier 3, Total Lexis Nexis.
- **Time Range**: Annual: 2019-2027, Monthly: 2019-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

### S&P Transcripts
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a breakdown of S&P Transcripts costs and user counts across different user tiers.
- **Key Components**: S&P Transcripts, Up to 4999, 5000 to 5999, 6000 to 6999, 7000 to 7999, 8000 to 8999, 9000 to 9999, >25000, Total Users, User Limit, Minimum, Total S&P Expense, Total Transcript Expense.
- **Time Range**: Annual: 2019-2027, Monthly: 2021-2027
- **Notes & Customizations**: Data is presented in thousands. There are both annual and monthly time series.

---

## Total FDS Cost

### Section Name (Summary FDS COGS Expense (FDS Content))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the FDS Content expenses, broken down by category. It provides a summary of the costs associated with FDS content creation and management.
- **Key Components**: Pool Floor, BRM, AMR, Transcripts, M&A, Total
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (FDS Excess Expense)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the FDS Excess expenses, broken down by category. It provides a summary of the costs associated with FDS excess expense.
- **Key Components**: Pool Floor, BRM, AMR, Transcripts, M&A, Total Excess
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Total FDS Spend & Minimum)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the Total FDS Spend and Minimum.
- **Key Components**: Total FDS Spend, Total FDS Minimum
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Pool Contribution & Carryover Balance)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the Pool Contribution and Carryover Balance, including Paid, Carryover, and Excess amounts.
- **Key Components**: Paid, Carryover, Excess, Carryover Balance, Change in Carryover
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Adjusted FDS COGS Expense)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the Adjusted FDS COGS Expense and related components like AMR Expense.
- **Key Components**: AMR Expense, Change in Carryover, Adjusted AMR Expense, BRM, AMR, Transcripts, M&A, Total
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Values are scaled by 1000.

---

## FDS AMR

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report.
- **Key Components**: "FDS AMR"
- **Notes & Customizations**: Scale is in thousands.

### User Statistics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays key user statistics, including total bookings, active users, and active trialer users.
- **Key Components**: "% Active", "Total Bookings", "Active Users", "Active Trialer Users", "FDS Entitled AMR Users"
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Some values are scaled in thousands.

### Documents Purchased Statistics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents data related to documents purchased by different user types.
- **Key Components**: "Active Users", "Active - Documents Purchased", "Trialers - Documents Purchased", "Internal - Documents Purchased", "Total Docs Purchased"
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Some values are scaled in thousands.

### Cost Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Analyzes document costs, including costs per tier and total costs.
- **Key Components**: "Annual Documents Read", "Document Cost - Tier 1", "Total Document Cost", "FactSet AMR Minimum", "Total FactSet AMR Cost", "Rollover Balance", "Excess Over Minimum", "Adjusted Excess", "Total Adjusted FactSet AMR Cost"
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Some values are scaled in thousands.

---

## Direct Broker

### Section Name: Overview Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a high-level overview of key metrics related to AlphaSense's cost of goods sold, including expenses, user activity, and consumption data. It helps track overall performance and efficiency.
- **Notes & Customizations**: Expenses are scaled by 1000. Cost per user is calculated from column J onwards.

### Section Name: Reads Consumption by Broker
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the reads consumption and percentage of reads consumption by broker. This helps understand which brokers are driving the most usage.
- **Notes & Customizations**: Reads Consumption is displayed in absolute numbers and as a percentage.

### Section Name: WSI Broker Expense Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of expenses associated with each broker, including strategic investment, usage, consumption, revenue share, expense, minimum, and adjusted expense. It helps in understanding the cost structure for each broker.
- **Time Range**: Annual: 2015-2027, Monthly: 2015-2027
- **Notes & Customizations**: Expenses are scaled by 1000. There are two time series: annual data in columns E:Q and monthly data in columns T:FS.

---

## Additional FDS Content

### FDS RT Expense - User Tier Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total FDS RT (Real-Time) users, their associated costs, and percentage of total users, broken down by user tiers. It provides a snapshot of user distribution and cost allocation across different user segments.
- **Key Components**: Total FDS RT Users, User Tiers, Users, Cost, % of Total Users.
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Costs are scaled by 1000.

### FDS RT Excess Expense Calculation
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section calculates the Total FDS RT Excess Expense, adjusting for discounts and pool floors. It aims to determine the minimum excess spend based on user buckets.
- **Key Components**: Total FDS RT Excess Expense, Pool Floor, Discount (%), Discount Adjusted FDS RT Excess Expense, Minimum Excess Spend.
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Expenses are scaled by 1000.

### FDS Transcripts - User Tier Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total FDS Transcript users, broken down by user tiers. It provides a snapshot of user distribution across different user segments.
- **Key Components**: Total FDS Transcript Users, User Tiers, Users, Cost, % of Total Users, Total FDS Transcripts Excess Expense.
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Users are scaled by 1000.

### FDS M&A - User Tier Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section analyzes the total FDS M&A users, broken down by user tiers. It provides a snapshot of user distribution across different user segments.
- **Key Components**: Total FDS M&A Users, User Tiers, Users, Cost, % of Total Users, Total FDS M&A Excess Expense.
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: Values are scaled by 1000.

---

## FDS User Growth

### User Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level overview of user growth and ARR for Corporate and Financial user segments. This section is used to track overall business performance.
- **Key Components**: Corporate ARR, Financial ARR, Total ARR, Average Corporate Users, Average Financial Users, Total Average Users, Corporate Users at Year End, Financial Users at Year End, Total Users at Year End, Corporate Users (Added), Financial Users (Added), Total Users (Added), Corporate Enabled WSI Users, Financial Enabled WSI Users, Total Enabled WSI Users, % of Corporate Users, % of Financial Users, % of Total Users.
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: ARR values are scaled by 1000.

### New WSI Users Additions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Breaks down new WSI user additions by product and sector. This section helps understand the drivers of WSI user growth.
- **Key Components**: Percent of New Users Added by Product (WSI, Non-WSI, Total Corporate, Financial, Total Financial), New Users Added by Product (WSI, Non-WSI, Total Corporate, Financial, Total Financial), Percent of New Users Added (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total), New WSI Users Added by Sector (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Financial - Other, Total), Financial - Other, Total Financial.
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: User counts are scaled by 1000.

### Non-WSI Corporate Users Converted
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the conversion of Non-WSI Corporate users, providing insights into user migration.
- **Key Components**: Percent Converted by Sector (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: None.

### Non-WSI Users Converted
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the conversion of Non-WSI users, providing insights into user migration.
- **Key Components**: Non-WSI Users Converted (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: User counts are scaled by 1000.

### Percent of New Non-WSI Users Added by Sector
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the percentage of new Non-WSI users added by sector.
- **Key Components**: Percent of New Non-WSI Users Added by Sector (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: None.

### Non-WSI Users Added
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of Non-WSI users added by sector.
- **Key Components**: Non-WSI Users Added (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: User counts are scaled by 1000.

### Non-WSI Net User Change
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the net change in Non-WSI users by sector.
- **Key Components**: Non-WSI Net User Change (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: User counts are scaled by 1000.

### Non-WSI Users by Sector
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the total number of Non-WSI users by sector.
- **Key Components**: Non-WSI Users by Sector (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total).
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: User counts are scaled by 1000.

### WSI User Additions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of WSI user additions by sector.
- **Key Components**: Total Users Added by Sector (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Total), Total Users.
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: User counts are scaled by 1000.

### Total Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the total number of users by product.
- **Key Components**: Users by Product (Average WSI Enabled Users, Average Non-WSI Users, Total Average Corporate Users, Total Average Financial Users, WSI Enabled Users at Year End, Non-WSI Users at Year End, Total Corporate Users at Year End, Total Financial Users at Year End).
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: User counts are scaled by 1000.

### Total Enabled Users
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the total number of enabled users by sector.
- **Key Components**: Total Enabled Users (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial, Total), Percent of Active Users (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial, Total), Total Active Users (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial, Total).
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: User counts are scaled by 1000.

### Document Consumption
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks document consumption metrics.
- **Key Components**: Docs Per Active User per Month (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Financial), Consumpstion Reduction, Docs Per Active User per Month - Reduction (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Financial - Other, Total Docs - Reduction (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial - Other, Total), Total Docs - Unadjusted (Professional Services, Pharma & Life Sciences, Tech, Media & Telecom, Energy & Utilities, Retail & Consumer Products, Finacial - Other, Total).
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: User counts are scaled by 1000.

### FDS RT Users Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks details about FDS RT (Real-Time) users.
- **Key Components**: Users Added (Corporate, Financial, Total), Percent of New FDS RT Users Added (Corporate, Financial, Total), New FDS RT Users Added by Product (Corporate, Financial, Total), Enabled FDS RT Users (Corporate, Financial, Total Enabled RT Users), Active FDS RT Users (Corporate, Financial, Total Active RT Users), Percent of Active FDS RT Users (Corporate, Financial, Total Percent of Active RT Users).
- **Time Range**: Annual: 2020-2027, Monthly: 2020-2027
- **Notes & Customizations**: User counts are scaled by 1000.

---

## FDS RT Minimums

### Section Name (User Tier Pricing Table)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the pricing structure for a product or service based on user tiers. It shows the incremental users, fee per user, total cost, maximum discount, and minimum/maximum total cost (annual and monthly) for each tier. This is used for sales and pricing calculations.
- **Key Components**: User Tiers, Incremental Users, Fee Per User, Total, Max Discount, Min Total (Annual), Max Total, Min Total (Monthly).
- **Notes & Customizations**: The pricing is structured in tiers, with the "Fee Per User" resetting at each tier. The values in ranges D3:E26 and G3:J26 are scaled by 1000.

---

## Product User Splits

### Product User Data (Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR ($15k), AMR ($30k), AMR)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the product user data split for various products like Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR ($15k), AMR ($30k), and AMR. It tracks the number of users for each product over time.
- **Key Components**: Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR ($15k), AMR ($30k), AMR, Financial, Corporate, Other, Total.
- **Time Range**: Monthly: 2017-2018
- **Notes & Customizations**: The data is scaled by 1000. There are two separate monthly time series.

### BRM Data (BRM - Global, BRM - Single)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the BRM (Business Relationship Management) data split for Global and Single products. It tracks the number of users for each product over time.
- **Key Components**: BRM - Global, BRM - Single, Total.
- **Time Range**: Monthly: 2017-2018
- **Notes & Customizations**: The data is scaled by 1000. There are two separate monthly time series.

### FactSet RT Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet RT (Real-Time) data. It tracks the number of users over time.
- **Key Components**: FactSet RT, Total.
- **Time Range**: Monthly: 2017-2020
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR (After Market Research) data. It tracks the number of users over time.
- **Key Components**: FactSet AMR, Total.
- **Time Range**: Monthly: 2017-2020
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR / Active Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR / Active data. It tracks the number of users over time.
- **Key Components**: FactSet AMR / Active, Total.
- **Time Range**: Monthly: 2017-2020
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR / Trailers Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR / Trailers data. It tracks the number of users over time.
- **Key Components**: FactSet AMR / Trailers, Total.
- **Time Range**: Monthly: 2017-2020
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR / Internal Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR / Internal data. It tracks the number of users over time.
- **Key Components**: FactSet AMR / Internal, Total.
- **Time Range**: Monthly: 2017-2020
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR Active Docs Purchased Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR Active Docs Purchased data. It tracks the number of documents purchased over time.
- **Key Components**: FactSet AMR Active Docs Purchased, Total.
- **Time Range**: Monthly: 2017-2020
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR Trialer Docs Purchased Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR Trialer Docs Purchased data. It tracks the number of documents purchased over time.
- **Key Components**: FactSet AMR Trialer Docs Purchased, Total.
- **Time Range**: Monthly: 2017-2020
- **Notes & Customizations**: The data is scaled by 1000.

### FactSet AMR Internal Docs Purchased Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the FactSet AMR Internal Docs Purchased data. It tracks the number of documents purchased over time.
- **Key Components**: FactSet AMR Internal Docs Purchased, Total.
- **Time Range**: Monthly: 2017-2020
- **Notes & Customizations**: The data is scaled by 1000.

---

## TR BRM

### Section Name: Tiered Pricing for Financials
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the pricing and user mix for different tiers of Financial clients over a period of months. It allows for analysis of revenue based on client size and region.
- **Key Components**: Global Users (1-10), Global Users (11-50), Global Users (51+), Single Region 1-10, Single Region 11-25, Single Region 26-50, Single Region 50+
- **Notes & Customizations**: Pricing is scaled by 1000.

### Section Name: Tiered Pricing for Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the pricing and user mix for different tiers of Corporate clients over a period of months. It allows for analysis of revenue based on client size and region.
- **Key Components**: Global Users (1-10), Global Users (11-50), Global Users (51+), Single Region 1-10, Single Region 11-25, Single Region 26-50, Single Region 50+
- **Notes & Customizations**: Pricing is scaled by 1000.

### Section Name: Tiered Pricing for Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the pricing and user mix for different tiers of Other clients over a period of months. It allows for analysis of revenue based on client size and region.
- **Key Components**: Global Users (1-10), Global Users (11-50), Global Users (51+), Single Region 1-10, Single Region 11-25, Single Region 26-50, Single Region 50+
- **Notes & Customizations**: Pricing is scaled by 1000.

### Section Name: User Count Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the user counts for Global research users, Single region users, Financial, Corporate, and Other users over a period of months.
- **Key Components**: Global research users, Single region users, Financial, Corporate, Other
- **Notes & Customizations**: Pricing is scaled by 1000.

---

## AMR

### Monthly Data Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains monthly data for key metrics such as total firms, total users, and fees. It allows for tracking performance trends over time.
- **Key Components**: Month, Total Firms, Total users, Fees.
- **Notes & Customizations**: Fees are scaled by 1000.

### Cost Breakdown Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a breakdown of costs into different categories.
- **Key Components**: Corporate, $15k, $30k, Financial, Other.
- **Notes & Customizations**: All values are scaled by 1000.

---

## LN

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the monthly date headers for the financial data section.
- **Key Components**: Month and Year labels (e.g., "2017-2 Feb", "2017-3 Mar")
- **Notes & Customizations**: The dates in row 1 are strings and not actual date values.

### Financial Data Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains financial data categorized by "Corporate" and "Other" over a monthly time series.
- **Key Components**: Corporate, Other, Financial (B4, B5, B6, B7)
- **Notes & Customizations**: The section contains a monthly time series. Row 3 contains the actual date values, while row 1 contains string representations of the month and year.

---

## DJ

### Section Name (Revenue Breakdown)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down revenue into different categories (Corporate and Other) over a monthly time series. It allows for analysis of revenue streams and their performance over time.
- **Key Components**: Corporate Revenue, Other Revenue, Financial (likely a category or label).
- **Notes & Customizations**: The data includes "Financial" as a string in cells B3 and B5, which might be a category label or a title. The revenue data is presented in a monthly time series format.

---

## TR Transcripts

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains labels identifying the type of data presented in the subsequent sections.
- **Key Components**: Corporate, Financial, Other, Broker Partner
- **Notes & Customizations**: This section provides labels for the data presented in the annual section.

### Corporate Financial Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents quarterly financial data for Corporate, Financial, Other, and Broker Partner categories.
- **Key Components**: Corporate, Financial, Other, Broker Partner
- **Notes & Customizations**: Quarterly data is presented in columns C through H.

### Corporate Financial Data (Monthly)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Presents monthly financial data for Corporate, Financial, Other, and Broker Partner categories.
- **Key Components**: Corporate, Financial, Other, Broker Partner
- **Notes & Customizations**: Monthly data is presented in columns C through T.

---

## FS Transcripts

### Quarterly Data Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents key financial metrics broken down by quarter. It allows for tracking performance trends on a quarterly basis.
- **Key Components**: Financial, Corporate, Other, Broker Partner
- **Notes & Customizations**: The metrics are categorized into Financial, Corporate, Other, and Broker Partner.

### Monthly Data Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents key financial metrics broken down by month. It allows for tracking performance trends on a monthly basis.
- **Key Components**: Financial, Corporate, Other, Broker Partner
- **Notes & Customizations**: The metrics are categorized into Financial, Corporate, Other, and Broker Partner.

---

## Filings

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the sheet title and potentially other high-level information.
- **Key Components**: None
- **Notes & Customizations**: This is a simple header section.

### Revenue by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows revenue broken down by different segments (Other, Corporate, Broker Partner) over a period of time. It includes total revenue as well.
- **Key Components**: Financial, Other, Corporate, Broker Partner, Total Revenue.
- **Time Range**: Annual: 2017-2017, Monthly: 2018-2018
- **Notes & Customizations**: There are three time series within this section: Annual, Thousands, and Monthly. The "Thousands" section appears to be a scaling factor applied to the data. The date series definition indicates a monthly series, but the column headers suggest it's being used to represent different periods within a year.

---

## Detailed Income Statement

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and column headers.
- **Key Components**: "Income Statement", "Account Group", "Account Number", "Account Name", "Account Type"
- **Notes & Customizations**: None

### Revenue Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various revenue streams.
- **Key Components**: Revenue, PRM Single Region, PRM Global, BRM Single Region, BRM Global, RMS, Dow Jones News, IDC, Service Revenue, License Revenue, Total Revenue
- **Time Range**: Annual: 2024-2025
- **Notes & Customizations**: Revenue streams are broken down by region and product type.

### Cost of Service (COS) Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the costs associated with providing services.
- **Key Components**: Cost of Service, Broker Research, After Market Research, Embargoed Research - FactSet, International Filings, Transcripts, News, News & Journals, IDC, COS, Web Service - Production, Total COS
- **Time Range**: Annual: 2024-2025
- **Notes & Customizations**: COS is broken down by specific service offerings.

### Expenses Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various operating expenses.
- **Key Components**: Expenses, People, Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Commission, Bonus, Benefits, Recruiting Fees, Relocation, Contractors, Outsourced R&D, Total People Costs, Other Employee Costs, Cellular Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions, Total Other Employee Costs, Travel, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals, Daily Meal Allowance When Abroad, Business Meals, Internal Events, Total Travel Costs, Facilities Costs, Rent, CAM, Repairs & Maintenance, Utilities, Telephone, Computer & Internet, Total Facilities Costs, Marketing, Advertising & Promotion, Other Marketing, Marketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, SWAG, Total Marketing Costs, General and Administrative, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising fees, Miscellaneous, Total General & Administrative Costs, Legal, Legal Fees, Total Legal Costs, Other Costs, License Expense, DataFeeds, Web Service, Penalties & Settlements, Bad Debt, Total Other Costs
- **Time Range**: Annual: 2024-2025
- **Notes & Customizations**: Expenses are categorized into People, Other Employee Costs, Travel, Facilities, Marketing, General & Administrative, Legal, and Other Costs.

### Depreciation & Amortization Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the depreciation and amortization expenses.
- **Key Components**: Depreciation & Amortization, Depreciation Expense, Amortization of Capitalized R&D, Total Depreciation & Amortization
- **Time Range**: Annual: 2024-2025
- **Notes & Customizations**: Includes depreciation and amortization of capitalized R&D.

### Other Income Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details any other income streams.
- **Key Components**: Other Income, Subsidy Received, Revenue, Total Other Income
- **Time Range**: Annual: 2024-2025
- **Notes & Customizations**: Includes subsidy received.

### Taxes Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details the various tax expenses.
- **Key Components**: Taxes, Income Taxes, Other Taxes, Other Taxes - Non Deductible, Total Taxes
- **Time Range**: Annual: 2024-2025
- **Notes & Customizations**: Includes breakdown of different tax types.

### Interest Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details interest income and expense.
- **Key Components**: Interest, Interest Income, Interest Expense, Interest Net
- **Time Range**: Annual: 2024-2025
- **Notes & Customizations**: Calculates net interest.

### Other Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Details other income and expenses not categorized elsewhere.
- **Key Components**: Other, Capitalized R&D Costs, Gain/Loss on FX, Gain/Loss on Consolidation, Intercompany Revenue / (Expense), FX Net
- **Time Range**: Annual: 2024-2025
- **Notes & Customizations**: Includes FX gains/losses and intercompany transactions.

### Net Income Section
- **Section Type**: Standard P&L
- **Description & Purpose**: Calculates the net income/(loss).
- **Key Components**: Total Expenses, Net Income/(loss)
- **Time Range**: Annual: 2024-2025
- **Notes & Customizations**: Final calculation of net income.

### Personnel Cost Breakdown
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of personnel costs.
- **Key Components**: Salaries, Commission, Bonus, Benefits, Payroll Taxes, Worker Comp, Recruiting Fees, Relocation, Contractors, Outsourced R&D
- **Notes & Customizations**: Provides a detailed breakdown of personnel costs, likely monthly.

---

## Detailed Balance Sheet

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report.
- **Key Components**: Balance Sheet
- **Notes & Customizations**: None

### Section Name: Assets
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's assets, broken down into current, long-term, and fixed assets.
- **Key Components**: Current Assets (Cash, Accounts Receivable, Prepaid Expenses), Long Term Assets (Other Long Term Assets), Fixed Assets (Capitalized R&D).
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Liabilities
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's liabilities, broken down into current and long-term liabilities.
- **Key Components**: Current Liabilities (Accounts Payable, Accrued Expenses, Deferred Revenue), Long Term Liabilities (Long-term loan from credit institution, Convertible Notes).
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Equity
- **Section Type**: Balance Sheet
- **Description & Purpose**: Details the company's equity accounts.
- **Key Components**: Common Stock, Preferred Series A, Net Income, Retained Earnings.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Liabilities & Equity Total & Check
- **Section Type**: Balance Sheet
- **Description & Purpose**: Calculates the total liabilities and equity and includes a check to ensure the balance sheet balances.
- **Key Components**: Total Liabilities & Equity, Check.
- **Notes & Customizations**: Values are scaled by 1000.

---

## Detailed Cash Flow Satement

### Section Name (Cash Flow Statement - Operating Activities)
- **Section Type**: `Standard Cash Flow Statement`
- **Description & Purpose**: This section details the cash inflows and outflows resulting from the company's core business activities. It starts with Net Income and adjusts for non-cash items and changes in working capital accounts to arrive at Net Cash Flows from Operating Activities.
- **Key Components**: Net Income, Changes in Operating Assets (Accounts Receivable, etc.), Changes in Operating Liabilities (Accounts Payable, etc.), Depreciation, Amortization, Net Cash Flows from Operating Activities.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name (Cash Flow Statement - Investing Activities)
- **Section Type**: `Standard Cash Flow Statement`
- **Description & Purpose**: This section outlines the cash flows related to the purchase and sale of long-term assets, such as property, plant, and equipment (PP&E) and capitalized research and development.
- **Key Components**: Fixed Assets, Capitalized R&D, Net Cash Flows from Investing Activities.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name (Cash Flow Statement - Financing Activities)
- **Section Type**: `Standard Cash Flow Statement`
- **Description & Purpose**: This section details the cash flows related to how the company is financed, including debt, equity, and other forms of capital.
- **Key Components**: Unrealized Subsidy, Short Term Loans, Capital Loans, Long-term loans, SVB Line of Credit, Common Stock, Preferred Series A, Convertible Notes, Retained Earnings, Net Cash Flows from Financing Activities.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name (Cash Flow Statement - Reconciliation)
- **Section Type**: `Standard Cash Flow Statement`
- **Description & Purpose**: This section reconciles the beginning and ending cash balances, showing the net change in cash during the period.
- **Key Components**: Cash, Beginning of Period, Net Change in Cash, Cash, End of Period.
- **Notes & Customizations**: The data is scaled by 1000. There's an additional "Check" row.

---

## Key Metrics

### Section Name (Annual Subscription Value)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the annual subscription value over time, providing a high-level view of the company's recurring revenue.
- **Key Components**: ARR Added (Gross), New Sales, Upsells, Increases, Financial, Corporate, Other, Corporate as % of Total.
- **Time Range**: Annual: 2015-2016
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (ARR Added (Gross))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the ARR added (Gross) over time, providing a high-level view of the company's recurring revenue.
- **Key Components**: ARR Added (Gross), New Sales, Upsells, Increases, Financial, Corporate, Other, Corporate as % of Total.
- **Time Range**: Annual: 2015-2016
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (ARR Churn)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the ARR Churn over time, providing a high-level view of the company's recurring revenue.
- **Key Components**: ARR Churn, Uncontrollable, Controllable, % Controllable, % YTD Controllable.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (ARR Churn Notifications)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the ARR Churn Notifications over time, providing a high-level view of the company's recurring revenue.
- **Key Components**: ARR Churn Notifications, Budget/Firm Downsizing, Competitor, Insufficient value, Low use/engagement, User(s) left firm, Other.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (# of Client Firms)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of client firms over time.
- **Key Components**: # of Client Firms, # of Client Firms Added, # of Client Firms Lost.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (# of Users)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of users over time.
- **Key Components**: # of Users, # of Gross Users Added, # of Gross Users Lost.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Cash & Debt)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks cash and debt levels over time.
- **Key Components**: Cash, SVB Debt.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (SaaS Metrics)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks various SaaS metrics related to ARR and churn.
- **Key Components**: ARR, Churn, Total Churn $, Total Churn %, Rolling 12 Month Churn %, Customer Churn %, Net Churn % (Rolling 12m), Net Retention % (Rolling 12m).
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Contract Duration)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks contract duration metrics.
- **Key Components**: Contract Duration, New Contracts, Average contract Length, Weighted average contract Length, Existing Clients.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Deal Metrics)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks deal-related metrics such as average client size and ARPU.
- **Key Components**: Total Average Client Size, New Client Average Size, New Sales ARPU, Total User Base ARPU.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Client Counts)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of client firms, both new and existing.
- **Key Components**: New firms, Existing Firms, Total Firms.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (User Counts)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the number of users across different categories.
- **Key Components**: Financial, Corporate, Other, BRM (PRM Global), BRM Global, BRM Global (PRM Single), BRM Single, PRM Global, PRM Single region, Empty Container, AMR $30K (PRM Single region), AMR $30K (PRM Global), Inactive, AMR $15K (PRM Global), AMR $15K (PRM Single), AMR $30K (BRM Single, PRM Global), AMR $15K (Empty Container), Check.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Cancels)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks cancels in terms of dollars, counts, and users.
- **Key Components**: Cancels $, Cancels Count, Cancels Users, Financial, Corporate, Other.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (ARR New/Upsell/Increase $)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks ARR from new sales, upsells, and increases.
- **Key Components**: ARR New/Upsell/Increase $, Deal Count, User Count, Financial, Corporate, Other.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Monthly Recurring Revenue)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks Monthly Recurring Revenue.
- **Key Components**: Monthly Recurring Revenue.
- **Notes & Customizations**: Values are scaled by 1000.

---

## Revenue by Client

### Section Name (Revenue by Client (Annual))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the revenue generated by different client segments (Corporate, Other) over a series of years. It allows for tracking revenue trends and identifying key revenue drivers.
- **Key Components**: Row Labels, Corporate, Other, Financial, Grand Total, 2015, 2016, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
- **Notes & Customizations**: Revenue data is scaled by 1000.

### Section Name (Revenue by Client (Monthly))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the revenue generated by different client segments (Corporate, Other) over a series of months. It allows for tracking revenue trends and identifying key revenue drivers.
- **Key Components**: Row Labels, Corporate, Other, Financial, Grand Total, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
- **Notes & Customizations**: Revenue data is scaled by 1000.

### Section Name (Income Statement (Annual))
- **Section Type**: Standard P&L
- **Description & Purpose**: This section represents a simplified Income Statement, likely projecting or analyzing financial performance over a series of years.
- **Key Components**: Income Statement (Y17)
- **Notes & Customizations**: Some data is scaled by 1000. The specific line items are not provided in the JSON.

---

## Client Support

### Section Name: Client ARR Movement - Type 1
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the movement of Annual Recurring Revenue (ARR) for a specific client type, showing beginning ARR, additions, churn, and ending ARR.
- **Key Components**: Financial, Beginning, Added, Churn, End
- **Notes & Customizations**: Data is scaled by 1000 in most columns.

### Section Name: Client ARR Movement - Type 2
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the movement of Annual Recurring Revenue (ARR) for a specific client type, showing beginning ARR, additions, churn, and ending ARR.
- **Key Components**: Beginning, Added, Churn, End, Corp
- **Notes & Customizations**: Data is scaled by 1000 in most columns.

### Section Name: Client ARR Movement - Type 3
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Tracks the movement of Annual Recurring Revenue (ARR) for a specific client type, showing beginning ARR, additions, churn, and ending ARR.
- **Key Components**: Other, Beginning, Added, Churn, End
- **Notes & Customizations**: Data is scaled by 1000 in most columns.

### Section Name: Churned CARR
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the churned CARR for Lost Clients and Corporate clients.
- **Key Components**: Financial, Churned CARR - Lost Clients, Corporate, Other, Total
- **Notes & Customizations**: Data is scaled by 1000 in most columns.

---

## Subscriber Support

### Section Name: Subscriber Counts by Type
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the number of subscribers, broken down by different subscriber types (Financial, Corp, Other). It shows the beginning count, added subscribers, churned subscribers, and the ending subscriber count for each type. This allows for analysis of subscriber growth and churn rates.
- **Key Components**: Financial, Corp, Other, Beginning, Added, Churn, End.
- **Notes & Customizations**: Subscriber counts are displayed in thousands (scale=1000), except for DA6:DS6, DA12:DS12, and DA18:DS18.

### Section Name: Expense Allocation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section allocates expenses to different categories. It shows the total expenses and then breaks them down by category (e.g., Admin). This helps understand the cost structure.
- **Key Components**: Total, Admin, Soros / Cap Group - Internal Content
- **Notes & Customizations**: Expenses are displayed in thousands (scale=1000).

---

## Headcount Support

### Section Name: Department Headcount (Original)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for various departments over time. It provides a view of how headcount changes month-to-month and includes a 2020 budget.
- **Key Components**: Department, Headcount, 2020 Budget
- **Notes & Customizations**: Headcount values are scaled by 1000 in some ranges.

### Section Name: Department Headcount (New)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for various departments over time. It provides a view of how headcount changes month-to-month and includes a 2020 budget.
- **Key Components**: Department, Headcount, 2020 Budget
- **Notes & Customizations**: Headcount values are scaled by 1000 in some ranges.

### Section Name: Sales Team Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for various roles within the Sales team.
- **Key Components**: Sales Roles, Headcount
- **Notes & Customizations**: Headcount values are scaled by 1000.

### Section Name: Customer Success, Operations, Business Development Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount for Customer Success, Operations, and Business Development teams.
- **Key Components**: Customer Success Roles, Operations Roles, Business Development Roles, Headcount
- **Notes & Customizations**: This section appears to have a different date range than the previous Sales Team Headcount section.

---

## Salary Support

### Section Name: Department Salary Breakdown (Departments)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down salary expenses by department. It allows for tracking salary costs across different departments over time.
- **Key Components**: Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, VP Bus Dev, Engineering (India)
- **Time Range**: Monthly: 2021-2027
- **Notes & Customizations**: Values are in thousands.

### Section Name: Department Salary Breakdown (Job Titles)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down salary expenses by job title. It allows for tracking salary costs across different roles over time.
- **Key Components**: Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, VP Bus Dev, Engineering (India)
- **Time Range**: Monthly: 2020-2020
- **Notes & Customizations**: Values are in thousands.

### Section Name: Department Salary Breakdown (Detailed Job Titles)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a more granular breakdown of salary expenses by specific job titles, primarily within the sales organization. It allows for detailed tracking of salary costs for various sales roles over time.
- **Key Components**: Account Manager, Account Manager - Corp, Account Executive - Financial, Account Executive - Corporate, Account Executive - Enterprise, CRO, Product Specialist, Sales Operations Manager, Sales Manager, Operations
- **Notes & Customizations**: Values are in thousands.

### Section Name: FX Rate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section stores the foreign exchange rates used for currency conversions.
- **Key Components**: FX RATE
- **Notes & Customizations**: This section contains FX rates, likely used to convert salaries in different currencies.

### Section Name: Quota Based Sales Reps
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks salary expenses for quota-based sales representatives.
- **Key Components**: Quota Sales Reps, AE - Financial (Quota), AE - Corporate (Quota), AM - Financial (Quota), VP Partnerships (Quota)
- **Notes & Customizations**: Values are in thousands.

### Section Name: Sales Team & Customer Success
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks salary expenses for the sales team and customer success roles.
- **Key Components**: Sales Team, CRO, Sales Manager, SDR Manager, SDR, Customer Success, CS Manager, AM - Financial, AM - Corporate, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, Business Development, GTM Strategy
- **Notes & Customizations**: Values are in thousands.

---

## Bonus Support

### Section Name: Department Salary Budget (2019 & 2020)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the salary budget for different departments for the years 2019 and 2020. It's used for financial planning and tracking departmental expenses.
- **Key Components**: Department (Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, Engineering (India), Sales), Salary, 2019 Budget, 2020 Budget.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: Department Adjustment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the adjustment amounts for different departments. It's used to account for changes in the budget.
- **Key Components**: Adjustment, Department (Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, Engineering (India), Sales).
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: Department Salary Budget (2019 & 2020) - Adjusted
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the adjusted salary budget for different departments for the years 2019 and 2020. It's used for financial planning and tracking departmental expenses after adjustments.
- **Key Components**: Department (Content, Engineering (ex India), Executive, Finance & Admin, Marketing, Product, Engineering (India), Sales), Salary, 2019 Budget, 2020 Budget.
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: Sales Bonus Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of the sales bonus, including the total bonus and average attainment. It's used to track sales performance and bonus payouts.
- **Key Components**: Total Sales Bonus, AVERAGE BONUS ATTAINMENT.
- **Notes & Customizations**: The data in F36:CX36 is scaled by 1000.

### Section Name: Sales Bonus Detail
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of the sales bonus by role. It's used to analyze bonus payouts and performance at a granular level.
- **Key Components**: Count, Total, Avg, CRO, VP of Sales, Sales Manager, SDR Manager, SDR, CS Manager, AM - Corporate, AM - Financial, PS Manager, Product Specialist, Enablement Manager, Sales Admin, Sales Operations Manager, Sales Operations, GTM Strategy.
- **Notes & Customizations**: The data in D42:CX56 is scaled by 1000. There are two distinct monthly time series in this section.

---

## Bonus Support (Sales Ops Only)

### Section Name: Department Salary and Adjustment Budget
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the salary budget and adjustments for different departments within the organization. It provides a breakdown of budgeted amounts for each department across different time periods.
- **Key Components**: Department names, Salary, 2019 Budget, 2020 Budget, Adjustment
- **Notes & Customizations**: The "Adjustment" section (B12:R19) seems to be an addition to the initial salary budget, potentially reflecting changes or corrections.

### Section Name: Sales Bonus Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates and summarizes sales bonus information, including total sales bonus, quarterly sales bonus, and average bonus attainment.
- **Key Components**: Total Sales Bonus, Quarterly Sales Bonus, AVERAGE BONUS ATTAINMENT
- **Notes & Customizations**: The Quarterly Sales Bonus is sparsely populated, suggesting it might be a summary or target value for specific quarters.

### Section Name: Sales Bonus by Role
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of sales bonus data by specific roles within the sales organization. It shows the average bonus for each role across different time periods.
- **Key Components**: Role names, Count, Total, Avg Sales Bonus
- **Notes & Customizations**: There are two separate date series in this section, one starting in October 2019 and the other in December 2019. This might indicate different calculation methods or data sources for different roles or time periods.

---

## OpEx - Content

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period label.
- **Key Components**: "Content", "Month Ending"
- **Notes & Customizations**: This section contains the report title and the label for the monthly time series.

### Section Name: Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, detailing revenue, cost of sales, expenses, and ultimately, profit or loss.
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses.
- **Notes & Customizations**: The report is presented in thousands (scale = 1000). There are several sub-categories within each major component (e.g., multiple line items under People Costs). The "Year To Date" column (B3) suggests that the monthly values are cumulative.

---

## OpEx - Engineering

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period covered.
- **Key Components**: Engineering, Month Ending, Year To Date
- **Notes & Customizations**: The header indicates that this sheet is for Engineering Operational Expenses.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the financial performance of the Engineering department, including revenue, cost of sales, gross profit, expenses, and other income/expenses.
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses
- **Notes & Customizations**: The data is presented in thousands (scale: 1000). The time series is monthly, starting from 02/28/2019.

---

## OpEx - Executive

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period covered.
- **Key Components**: Executive, Month Ending
- **Notes & Customizations**: This section provides the context for the rest of the sheet.

### Section Name: Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, including revenue, cost of sales, expenses, and profit.
- **Key Components**: Revenue, Cost of Sales, Gross Profit, People Costs, Expenses, Taxes, Interest Net, Total Expenses
- **Notes & Customizations**: The report is scaled by 1000.

---

## OpEx - Finance & Admin

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period covered.
- **Key Components**: "Finance & Admin", "Month Ending", "Year To Date"
- **Notes & Customizations**: This section contains the title of the report and the time period covered.

### Section Name: Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the financial performance of the "Finance & Admin" department over a period of time. It includes revenue, cost of sales, gross profit, expenses, and other income/expenses to arrive at a total expense figure.
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses.
- **Notes & Customizations**: The report is scaled by 1000. The end date is not explicitly defined in the provided JSON, but the pattern suggests it continues monthly.

---

## OpEx - Marketing

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period description.
- **Key Components**: "Marketing", "Month Ending", "Year To Date"
- **Notes & Customizations**: The header spans two rows and provides context for the data below.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the financial performance of the Marketing department, including revenue, cost of sales, expenses, and other income/expenses.
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses.
- **Notes & Customizations**: The report is scaled by 1000. The time series is monthly, starting from February 2019. The indentation in column A indicates the hierarchical structure of the income statement.

---

## OpEx - Product

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the product name and the label for the time series data.
- **Key Components**: Product, Month Ending
- **Notes & Customizations**: This section provides context for the data in the Income Statement.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: This section presents the Income Statement, detailing revenue, cost of sales, expenses, and other financial metrics over a period of months. It's used to track and analyze the financial performance of a product.
- **Key Components**: Revenue, Cost of Sales, Gross Profit, People Costs, Marketing, General & Admin, Legal Costs, Depreciation & Amortization, Taxes, Interest Net, Total Expenses.
- **Notes & Customizations**: The data is scaled by 1000. The "Year To Date" label in B3 suggests that the monthly values represent year-to-date figures.

---

## OpEx - Sales

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time series label.
- **Key Components**: Sales, Month Ending
- **Notes & Customizations**: "Year To Date" is in cell B3.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, detailing revenue, cost of sales, expenses, and ultimately, profitability.
- **Key Components**: Revenue, Cost of Sales, Gross Profit, Expenses (People Costs, Travel Costs, Facility Costs, Marketing, General & Admin, Legal Costs, Other Costs, Depreciation & Amortization), Other Income, Taxes, Interest Net, Other, Total Expenses.
- **Notes & Customizations**: All monetary values are scaled by 1000. The time series is monthly, starting from 02/28/2019.

---

## Historical Quota& Productivity

### Section Name (Historical Quota)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the historical quota for different account manager roles. It allows for tracking quota performance over time.
- **Key Components**: Account Manager, AE - Financial, AE - Corporate, AE - Enterprise, AE - Other, VP Bus Dev.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Historical Productivity)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the historical productivity for different account manager roles. It allows for tracking productivity performance over time.
- **Key Components**: Account Manager, AE - Financial, AE - Corporate, AE - Enterprise, AE - Other, VP Bus Dev, Other, Total.
- **Time Range**: Annual: 2016-2018, Monthly: 2015-2019
- **Notes & Customizations**: Values are scaled by 1000. There are two separate time series, annual and monthly, for productivity data.

---

## Fixed Asset Depreciation

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains labels for the data in the subsequent section.
- **Key Components**: Account, Starting Balance, Conversion, Starting Balance (USD)
- **Notes & Customizations**: None

### Fixed Asset Depreciation Schedule
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the depreciation schedule for fixed assets, including starting balances, conversions, and monthly depreciation expenses.
- **Key Components**: LTD, Mgmt, Inc, Total, Oy, R&D
- **Notes & Customizations**: Values are scaled by 1000. The column headers for the monthly data are not explicitly defined in the JSON but are implied by the data ranges.

---

## COGS vs. Marginal

### Section Name: Revenue and Seats Calculation
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates Revenue per Seat based on 2017 Revenue and 2017 Seats. It also shows the current and marginal Revenue/Seat values.
- **Key Components**: 2017 Revenue, 2017 Seats, Revenue / Seat (Current), Revenue / Seat (Marginal)
- **Notes & Customizations**: Uses a scale of 1000 for some values.

### Section Name: COGS Analysis
- **Section Type**: Cost Analysis
- **Description & Purpose**: This section analyzes the Cost of Goods Sold (COGS) and related metrics like Gross Profit per Seat and % Margin. It includes per-seat costs for various services.
- **Key Components**: COGS, Per-Seat costs (Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, IDC, Web Service - Production), Gross Profit per Seat, % Margin
- **Notes & Customizations**: Includes "Calculations" section.

### Section Name: Marginal Cost Analysis
- **Section Type**: Cost Analysis
- **Description & Purpose**: This section analyzes marginal costs associated with various services and user tiers. It calculates costs based on percentages of users and prices per user.
- **Key Components**: Broker Research, After Market Research, International Filings, Transcripts, News, News & Journals, IDC, Web Service - Production, Percent of Users AMR, AMR - $15k, AMR - $30k, Cost per User, Marginal Price, Percent of Users, Price per User - Tier 1
- **Notes & Customizations**: Includes calculations for "Total" costs. Contains text indicating flat fees for some services (e.g., "TR Transcripts - flat fee will be triggered so no marginal cost").

---

## Accrued Wages

### Section Name (e.g., "Accrued Wages Data")
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the accrual and pre-payment of various social costs and insurance fees related to wages. It provides a monthly breakdown of these expenses.
- **Key Components**: Acc. of pension insurance fees(accruals), Accrual of employer's statutory ins. pmt, Pension pre-payments, Unemployment pre-payment, Accident insurance pre-payment, Life insurance pre-payment, Calculated social costs, Pension held from workers, Unemployment held from workers, Total 21225 Accured finish side costs, USD
- **Notes & Customizations**: The data is scaled by 1000.

---

## Deposits

### Section Name (Deposits Data)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains the deposit data, scaled by 1000, for each month from January 2020 to December 2021.
- **Key Components**: Deposits
- **Notes & Customizations**: The deposit values are scaled by 1000.

---

