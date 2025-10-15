## 1. Spreadsheet Overview
- **Sheet Name**: ARR and Revenue
- **Key Sections Identified**:
  - ARR Summary (ARR rollforward / summary)
  - ARR & Revenue by Segment (segment-level ARR and revenue tables)
  - Total Revenue / Revenue as % of MRR
  - Sales Productivity (headcount, quotas, productivity KPIs)
  - Bookings Overview (New Bookings, Upsell, % mix)
  - Bookings by Segment (Total / New / Upsell by segment)
  - Segment ARR Breakdowns (Financial ARR, Corporate ARR, Other ARR)
  - Combined (aggregate / combined metrics across segments)

---

## 2. Detailed Section Analysis

### ARR Summary
- **Section Type**: Key Metrics Table / ARR rollforward
- **Description & Purpose**: Top-level ARR summary showing beginning ARR, movements (new business, upsell, churn), ending ARR, churn/retention rates, ARR → Revenue conversions and simple ARR-derived KPIs (clients, users, ARR per client/subscriber). Designed to provide a consolidated rollforward and headline metrics for ARR and revenue.
- **Cell Range**: B5:FS22
- **Time Series Horizon**:
  - **Dates Location**:
    - Primary (monthly timeline used across most columns): T2:FS2 (date series ds_2: monthly 2015-01 → 2027-12)
    - Secondary (quarterly header present for AF–CM columns): AF1:CM1 (date series ds_1: quarterly 2016-Q1 → 2020-Q4)
    - Note: The block includes left-side compact columns E:Q used for snapshot/historical values (these columns do not map to the ds_2 row header).
  - **Date Range**: Jan 2015 to Dec 2027 (primary monthly), with an additional quarterly band from Q1 2016 to Q4 2020 where AF1:CM1 is used.
  - **Frequency**: Monthly (primary); Quarterly (secondary / legacy band)
- **Key Components**:
  - ARR start/end rollforward (Beginning ARR, New Business, Upsell, Churn, Ending ARR)
  - Churn / Retention metrics (% Churn Rate, Retention Rate, Renewed)
  - Revenue derived from ARR and % growth metrics
  - High-level client/user KPIs (Clients Net, Users Net, ARR / Client, ARR / Subscriber)
- **Notes & Customizations**:
  - Numeric values are presented with mixed scaling; many cells are scaled (thousands).
  - Two date header conventions coexist (monthly and a quarterly snapshot band).
  - The E:Q columns act as compact historical snapshots separate from the main timeline.

---

### ARR by Segment (includes Revenue by Segment / Total ARR / Total Revenue)
- **Section Type**: Segment-level ARR and Revenue tables
- **Description & Purpose**: Breaks ARR and revenue into primary business segments (Financial, Corporate, Other) and shows totals. Useful for analyzing segment contribution to ARR and revenue over time.
- **Cell Range**: B26:FS36
- **Time Series Horizon**:
  - **Dates Location**:
    - Primary: T2:FS2 (monthly series, ds_2)
    - Secondary: AF1:CM1 (quarterly series, ds_1) — used where AF–CM columns appear
    - Historical snapshot columns: E:Q (compact columns)
  - **Date Range**: Jan 2015 → Dec 2027 (monthly); Q1 2016 → Q4 2020 (quarterly band)
  - **Frequency**: Monthly (primary) and Quarterly (secondary)
- **Key Components**:
  - Segment ARR rows and segment revenue rows (per-segment time series)
  - Total ARR and Total Revenue rows aggregating segment results
  - Revenue as % of MRR line for high-level conversion insight
- **Notes & Customizations**:
  - Revenue rows often stored in thousands (scale present).
  - Segment detail is repeated in later dedicated segment blocks (see segment ARR breakdowns).

---

### Total Revenue as % of MRR (Summary KPI)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows a KPI row that expresses total revenue as a percentage of MRR (Monthly Recurring Revenue) across the timeline — a quick health/monetization metric.
- **Cell Range**: B42:FS42
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly); AF1:CM1 for quarterly columns if present
  - **Date Range**: Jan 2015 → Dec 2027 (monthly)
  - **Frequency**: Monthly (primary)
- **Key Components**:
  - Single KPI row across time (Revenue as % of MRR)
- **Notes & Customizations**:
  - Values scaled (thousands) in many columns.

---

### Sales Productivity (headcount, quotas, productivity KPIs)
- **Section Type**: Key Metrics Table / Sales Productivity Dashboard
- **Description & Purpose**: Tracks sales organization capacity and productivity: headcount by role, effective sales headcount, quota per rep, quota attainment (productivity %), and seasonality-adjusted productivity metrics. Supports quota planning and productivity analysis.
- **Cell Range**: B44:FS88
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (monthly series, ds_2); AF1:CM1 available for quarterly columns
  - **Date Range**: Jan 2015 → Dec 2027 (monthly)
  - **Frequency**: Monthly (primary)
- **Key Components**:
  - Sales headcount by role and totals (Total Sales Headcount, Effective Sales Headcount)
  - Quota per person, Total Quota, and Total Bookings comparisons
  - Productivity metrics: Productivity % of Quota and Seasonality-adjusted productivity
- **Notes & Customizations**:
  - Multiple rows use thousand-scaling; some columns contain compact snapshots (E:Q).
  - Productivity is shown both raw and seasonality-adjusted.

---

### Bookings Overview (New Bookings, Upsell, Mix)
- **Section Type**: Bookings Table / Mix Analysis
- **Description & Purpose**: Overview of bookings activity including New Business bookings, Upsell, Churn contributions to bookings, plus mix metrics (% of total bookings). Enables analysis of new logos vs. expansion.
- **Cell Range**: B100:FS150
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (monthly series, ds_2); quarterly band AF1:CM1 where applicable; E:Q snapshot columns also present.
  - **Date Range**: Jan 2015 → Dec 2027 (monthly)
  - **Frequency**: Monthly (primary)
- **Key Components**:
  - New Bookings time series and related subtotals
  - Upsell time series and contribution to total bookings
  - % of Total Bookings breakdowns (New vs Upsell)
- **Notes & Customizations**:
  - Mixed scaling (many values in thousands).
  - The section contains multiple rows for per-role and aggregate bookings (not all labels shown here).

---

### Bookings by Segment (Total / New / Upsell by segment)
- **Section Type**: Key Metrics Table / Segment bookings
- **Description & Purpose**: Shows bookings (total, new, upsell) broken down by Business segments (Financial, Corporate, Other). Useful for segment-level pipeline and booking composition analysis.
- **Cell Range**: B152:FS171
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (monthly series, ds_2); AF1:CM1 for quarterly band when used
  - **Date Range**: Jan 2015 → Dec 2027 (monthly)
  - **Frequency**: Monthly (primary)
- **Key Components**:
  - Total Bookings by Segment, New Bookings by Segment, Upsell by Segment
  - Segment subtotals and 'na' placeholders for some rows where relevant
- **Notes & Customizations**:
  - Some rows include 'na' text markers for non-applicable periods.
  - Numeric columns frequently scaled (thousands).

---

### Financial ARR (segment rollforward)
- **Section Type**: Standard ARR (segment rollforward)
- **Description & Purpose**: Detailed ARR rollforward and KPIs specific to the Financial segment (Beginning ARR, New, Upsell, Churn, Ending ARR, clients/users KPIs). Mirrors the top-level rollforward but scoped to the Financial segment.
- **Cell Range**: B173:FS188
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (monthly series, ds_2); AF1:CM1 for quarterly band if present
  - **Date Range**: Jan 2015 → Dec 2027 (monthly)
  - **Frequency**: Monthly (primary)
- **Key Components**:
  - Per-period Financial segment ARR start/end and flows
  - Clients/Users KPIs (Clients Net, ARR / Client, Users Net, ARR / Subscriber)
- **Notes & Customizations**:
  - Uses the same layout / scaling conventions as the aggregated ARR Summary (many values in thousands).

---

### Corporate ARR (segment rollforward)
- **Section Type**: Standard ARR (segment rollforward)
- **Description & Purpose**: ARR rollforward and KPIs for the Corporate segment — same structure as Financial ARR but scoped to Corporate customers.
- **Cell Range**: B190:FS205
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (monthly series, ds_2); AF1:CM1 quarterly band if present
  - **Date Range**: Jan 2015 → Dec 2027 (monthly)
  - **Frequency**: Monthly (primary)
- **Key Components**:
  - Corporate segment beginning/ending ARR, flows (new, upsell, churn)
  - Clients/users level KPIs and per-client metrics
- **Notes & Customizations**:
  - Numeric scaling in thousands for many rows.

---

### Other ARR (segment rollforward)
- **Section Type**: Standard ARR (segment rollforward)
- **Description & Purpose**: ARR rollforward and KPIs for the Other segment (all non-Financial/Corporate), including flows and client/user level metrics.
- **Cell Range**: B207:FS216
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (monthly series, ds_2); AF1:CM1 quarterly band if present
  - **Date Range**: Jan 2015 → Dec 2027 (monthly)
  - **Frequency**: Monthly (primary)
- **Key Components**:
  - Segment ARR start/end and constituent flows
  - Client and user KPIs
- **Notes & Customizations**:
  - A number of per-period slices use thousand scaling; some later columns include large-column banding (CJ..FS).

---

### Combined (aggregate summary across segments)
- **Section Type**: Aggregated Key Metrics Table
- **Description & Purpose**: Consolidated combined metrics (aggregate ARR / users / clients) across all segments. Serves as the reconciled/global view for the model.
- **Cell Range**: B224:FS232
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (monthly series, ds_2); AF1:CM1 for quarterly columns if present
  - **Date Range**: Jan 2015 → Dec 2027 (monthly)
  - **Frequency**: Monthly (primary)
- **Key Components**:
  - Aggregated ARR, client/user metrics, ARR per client/subscriber
- **Notes & Customizations**:
  - Final consolidated section; follows the same mixed-scaling conventions.

---

Notes on date headers and scaling (global)
- Primary timeline for the sheet is the monthly date series located at T2:FS2 (date series id ds_2 — monthly from 2015-01 to 2027-12). Many time series rows reference columns T:FS and should be retrieved using T2:FS2 as the column-period header.
- A secondary quarterly date header exists at AF1:CM1 (date series id ds_1 — quarterly from 2016-Q1 to 2020-Q4). AF–CM columns in multiple rows align to that quarterly band.
- Several left-side compact columns E:Q appear throughout the sheet as historical snapshots or aggregated pre-period columns; they do not have an explicit ds_2 header row and should be treated as snapshot columns when extracting time series.
- Many numeric cells are presented with a scale of 1,000 (thousands). When extracting raw numeric values, consult cell-level formatting (the sheet includes scale metadata on many ranges).