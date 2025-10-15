## 1. Spreadsheet Overview
- **Sheet Name**: Sales Reps
- **Key Sections Identified**:
  - Sales Rep Summary (headcount & quota summaries)
  - Non Quota'd Sales Team Summary
  - Quota Sales Rep Detail (detailed per-role/month ramp & attrition)
  - Other Sales Detail (reports, ratios, SDR/AM/CS capacity rules)
  - Total Sales Heads (aggregate headcount totals)
  - Quota Rep - Salary Summary
  - Quota Rep - Bonus Summary
  - Quota Rep - Salary Detail (per-role salary lines)
  - Other Salary & Role Details (other teams / managers / product specialists salary blocks)
  - Total Sales Salary (aggregate salaries for Sales organization)

## 2. Detailed Section Analysis

### Sales Rep Summary
- **Section Type**: Key Metrics Table / Headcount Summary
- **Description & Purpose**: Provides the high-level quota-carrying headcount metrics (quota headcount, totals, average effective quota headcount) and short summary measures used to roll up into downstream capacity and cost calculations. This is the top-level summary for quota-bearing reps.
- **Cell Range**: B5:FS23
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series). Note: columns E:Q contain additional numeric snapshot/aggregate columns (non-date numeric cells).
  - **Date Range**: January 2015 to December 2027 (date series definition ds_1).
  - **Frequency**: Monthly
- **Key Components**:
  - Quota Sales Rep Headcount / Total Quota Sales Rep Headcount
  - Average Effective Quota Headcount and Total Average Effective Quota Headcount
  - Summary aggregates across multiple period columns (E:Q snapshot + T:FS monthly series)
- **Notes & Customizations**:
  - Many numeric cells in this block use a thousand-scale (values presented / computed in thousands).
  - This section is designed as a compact summary feeding detailed sections below.

### Non Quota'd Sales Team Summary
- **Section Type**: Key Metrics Table / Non-Quota Headcount Summary
- **Description & Purpose**: Summarizes non-quota sales organization headcount (CS Managers, AMs, PS Managers, Sales Admin, etc.) and produces totals used for headcount and cost calculations outside of quota-carrying reps.
- **Cell Range**: B25:FS41
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series); E:Q are summary/aggregate columns.
  - **Date Range**: January 2015 to December 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Individual lines for CS Manager, AM - Corporate, PS Manager, Sales Admin
  - Total Non Quota'd Sales Team (rollup)
- **Notes & Customizations**:
  - Section mixes compact snapshot columns (E:Q) with the full monthly series (T:FS).
  - Values in many columns are scaled by 1,000 (see format metadata).

### Quota Sales Rep Detail
- **Section Type**: Custom P&L-style / Headcount Ramp & Attrition Detail (per-role)
- **Description & Purpose**: Detailed, role-level view of quota-carrying reps that includes ramp profile (Month 1..Month 10), efficiency measures, beginning/added/removed/end of period counts, and effective start/end indicators. This section underpins the summary headcount metrics and is repeated per-role (AEs, SDRs, Sales Managers, etc.).
- **Cell Range**: B43:FS189
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series). The block also contains summary columns E:Q for discrete aggregates.
  - **Date Range**: January 2015 to December 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Ramp / Efficiency rows (Month 1..Month 10)
  - Beginning of Period, Added, Removed, End of Period, Attrition
  - Effective Start/End and Add rows to capture staged hires and attrition timing
  - Repeated role blocks (e.g., AE roles, SDR roles, Sales Manager roles)
- **Notes & Customizations**:
  - The layout is a custom headcount ramp model (not a standard P&L). Ramp months and many operational metrics are embedded in each role block.
  - Many rows/columns use 1,000-scale formatting.

### Other Sales Detail
- **Section Type**: Key Metrics Table / Operational Ratios & Capacity Rules
- **Description & Purpose**: Contains "Other Sales" operational metrics such as reports per VP of Sales, quota’d reps per manager, SDR to AE ratios, AE per SDR, ARR per AM (corporate/financial segments), minimum required managers, and other capacity/coverage rules used to derive required headcount.
- **Cell Range**: B191:FS326
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series); E:Q used for aggregated snapshots.
  - **Date Range**: January 2015 to December 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Capacity rules (Reports per VP, Quota'd Reps per Sales Manager, SDRs per SDR Manager)
  - Role-specific efficiency ratios (AE per SDR, AM per CS Manager, Product Specialist ratios)
  - ARR / ARR per manager lines (Corporate ARR, Financial ARR, ARR per Product Specialist)
- **Notes & Customizations**:
  - Section includes many segmented blocks for different go-to-market roles (corporate vs financial, product specialist, etc.).
  - Values often presented in the monthly series with some columns using thousand-scale.

### Total Sales Heads
- **Section Type**: Key Metrics Table / Aggregate Headcount Rollup
- **Description & Purpose**: Aggregated totals for all sales heads across quota and non-quota teams; a rollup used for executive summary and payroll calculations.
- **Cell Range**: B327:FS333
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series); E:Q snapshot columns also present.
  - **Date Range**: January 2015 to December 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Total headcount lines across multiple team groupings
  - Short-term snapshot columns alongside the full monthly series
- **Notes & Customizations**:
  - Part of the workbook’s headcount consolidation and used as input to salary/bonus sections below.

### Quota Rep - Salary Summary
- **Section Type**: Key Metrics Table / Compensation Summary
- **Description & Purpose**: High-level salary summary for quota-carrying reps (average salary, total wages lines) that feed into overall compensation expense.
- **Cell Range**: B334:FS342
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (monthly series); E:Q snapshots included.
  - **Date Range**: January 2015 to December 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Average salary per role group, total wages for quota reps
  - Aggregated compensation totals (used in combining with bonus)
- **Notes & Customizations**:
  - Numeric values frequently use 1,000-scale.

### Quota Rep - Bonus Summary
- **Section Type**: Key Metrics Table / Incentive Summary
- **Description & Purpose**: Aggregated quota rep bonus calculations (bonus per head, total sales bonus, and totals) — used to compute total incentive expense for quota-bearing reps.
- **Cell Range**: B344:FS352
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series); some columns (I:Q, CB:FS) are used for segmented bonus columns.
  - **Date Range**: January 2015 to December 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Sales bonus per head and total sales bonus rollups
  - Totals for quota-carrying incentive expense
- **Notes & Customizations**:
  - Bonus detail spans both compact (I:Q) and extended (CB:FS) column areas; multiple column blocks are used for different payout timing or categories.
  - 1,000-scale formatting applied in many cells.

### Quota Rep - Salary Detail
- **Section Type**: Detailed Key Metrics Table / Per-role Compensation Detail
- **Description & Purpose**: Row-level compensation detail for quota reps (per-role average salary, total wages, month-by-month compensation build for hires), that supports the salary summary and expense timing.
- **Cell Range**: B354:FS376
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (monthly series). Detailed monthly compensation timing is captured across T:FS.
  - **Date Range**: January 2015 to December 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Per-role salary components (average salary, wages by role)
  - Adjustment rows and per-role monthly salary distributions
- **Notes & Customizations**:
  - This detail ties headcount ramp to cost recognition; multiple columns use different sub-blocks (e.g., I:J, CB:FS) for split reporting.
  - Adjustment rows exist (e.g., a labeled "Adjustment") used to reconcile or normalize totals.

### Other Salary & Role Details
- **Section Type**: Detailed Key Metrics Table / Non-quota Compensation & Role Details
- **Description & Purpose**: Detailed salary and compensation sections for other sales functions and managers (Product Specialists, Enablement, Sales Ops, Customer Success, Account Managers, etc.). These blocks mirror the quota salary detail structure but are for non-quota roles and managers.
- **Cell Range**: B377:FS518
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (monthly series); many role-specific detail blocks contain both snapshot columns and the T:FS monthly range.
  - **Date Range**: January 2015 to December 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Per-role salary lines (Product Specialist, Enablement Manager, Sales Operations Manager, Customer Success Manager, etc.)
  - Average Employees / Average Salary / Total Wages and per-role bonus mappings
  - Role-specific cell blocks contain per-role monthly distributions and some role-specific capacity metrics
- **Notes & Customizations**:
  - Blocks repeat for many role types (see inverted index labels such as "Product Specialist", "Enablement Manager", "Sales Operations Manager", "Customer Success Manager", "Account Manager - Corporate", "Account Manager - Financial", etc.).
  - Several ranges for role blocks use different column offsets (some use CJ:FS or CB:FS areas) — keep the full horizontal span (to FS) when extracting.

### Total Sales Salary
- **Section Type**: Aggregate Key Metrics Table / Compensation Rollup
- **Description & Purpose**: Final rollup of all salary and compensation (salaries + bonuses + adjustments) for the entire sales organization. This section is the output used in expense forecasting and P&L integration.
- **Cell Range**: B519:FS523
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series). Snapshot/aggregate columns present in E:Q as well.
  - **Date Range**: January 2015 to December 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Final aggregated salary and bonus totals per period
  - Lines labeled "Total Sales Salary" and supporting totals in adjacent rows (monthly and snapshot columns)
- **Notes & Customizations**:
  - The final totals pull from multiple previous sections and are scaled (many fields use 1,000-scale).
  - Use this block as canonical source for exporting the Sales payroll time series.

---

General Notes & Conventions across the sheet
- Primary column-based date series is located at T2:FS2 and uses the date series ds_1 (monthly from 2015-01 to 2027-12). Many data rows populate across T:FS for time-series values.
- Many sections also include E:Q columns (non-date numeric snapshots or aggregated historic/quarterly columns). When extracting time series data, prioritize the T:FS monthly columns.
- Numeric scaling: a substantial number of numeric ranges are marked with a scale of 1000 in the formatting metadata — values in those ranges should be multiplied by 1,000 to get raw amounts.
- Repeating role blocks: the sheet uses repeated structural blocks for different roles (e.g., AE - Financial, AE - Corporate, VP - Partnerships, Product Specialist, Sales Operations Manager, etc.). These labels appear in column B throughout the sheet and can be used as anchor rows to locate role-specific blocks within the ranges above.
- Standard operational rows repeated across role blocks include: Beginning of Period, Added, Removed, End of Period, Ramp (Month 1..Month 10), Attrition, Effective Start/End, Efficiency. Expect those row labels inside the Quota Sales Rep Detail and replicated role salary/detail blocks.

If you want, I can:
- produce a CSV-style map of anchor label row numbers (e.g., where "Quota Sales Rep Detail" starts at row 43, "Total Sales Salary" at row 519) for programmatic retrieval, or
- extract a single section (by the exact cell range above) into JSON-ready arrays.