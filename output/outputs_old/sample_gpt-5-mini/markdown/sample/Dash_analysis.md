## 1. Spreadsheet Overview
- **Sheet Name**: Dash
- **Key Sections Identified**:
  - Income Statement Metrics
  - ARR Summary (Bookings / New Bookings / Upsell)
  - Segment Summary (ARR / Revenue / COS / GP / GM by segment)
  - Headcount Summary
  - Client & Subscriber Counts
  - Retention Metrics
  - Key Performance Indicators (Summary & Detail)
  - Key Performance Indicators by Segment
  - Debt Availability Build

## 2. Detailed Section Analysis

### Income Statement Metrics
- **Section Type**: Standard P&L / Income Statement metrics (includes memo FCF)
- **Description & Purpose**: Consolidated income statement line items used for top‑line and margin analysis: Revenue, Cost of Sales, Gross Profit, Operating Expenses and EBITDA, plus a memo row for Free Cash Flow. Designed to support profit & loss review and trend analysis across the sheet's time series.
- **Cell Range**: A5:FS24
- **Time Series Horizon**:
  - **Dates Location**: Primary date series at T2:FS2 (monthly series). Note: the section also contains summary/historical columns in E:Q (non‑monthly aggregate columns).
  - **Date Range**: Monthly series from 2015-01-31 through 2027-12 (date series "ds_1": start_date = 2015-01-31; pattern = "Monthly series from 2015-01 to 2027-12").
  - **Frequency**: Monthly (primary). Summary columns in E:Q are aggregated/legacy columns (not part of ds_1).
- **Key Components**:
  - Revenue (top-line)
  - Cost of Sales and resulting Gross Profit
  - Operating Expenses
  - EBITDA
  - Memo: Free Cash Flow (FCF)
- **Notes & Customizations**:
  - Several columns/blocks use a scale of 1,000 (thousands). Some leading cells contain "na" placeholders.
  - Dates are split between short/historical columns (E:Q) and the main monthly series (T:FS).

---

### ARR Summary (Bookings / New Bookings / Upsell)
- **Section Type**: ARR / Bookings Summary
- **Description & Purpose**: Annual Recurring Revenue (ARR) rollforward and bookings detail: Bookings, New Bookings, Upsell and totals. Used to reconcile ARR movement and booking composition over time.
- **Cell Range**: A26:FS51
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series). Aggregated/historical columns located in E:Q for summary snapshots.
  - **Date Range**: Monthly series 2015-01 to 2027-12 (ds_1).
  - **Frequency**: Monthly (primary), with historical/summary columns in E:Q.
- **Key Components**:
  - Beginning / Ending ARR (rollforward)
  - Bookings (breakdown rows)
  - New Bookings, Upsell, Total Bookings
- **Notes & Customizations**:
  - Numeric values frequently scaled to thousands. Some sub-rows include "na" markers in the short/historical columns.

---

### Segment Summary (ARR / Revenue / COS / GP / GM by segment)
- **Section Type**: Segment Analysis / Memo tables
- **Description & Purpose**: Multi-part segment reporting for ARR and Revenue by segment and accompanying memos: ARR by segment, Revenue by segment, COS (Cost of Sales) by segment, GP and Gross Margin by segment. Supports segment-level profitability and ARR composition analysis.
- **Cell Range**: A53:FS107
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series). Historical/summary columns also present in E:Q and specific columns across the sheet for legacy quarterly/annual snapshots.
  - **Date Range**: Monthly series 2015-01 to 2027-12 (ds_1).
  - **Frequency**: Monthly (primary). Some memo tables include aggregated columns (E:Q and scattered intermediate columns).
- **Key Components**:
  - Memo: ARR by Segment
  - Memo: Revenue by Segment
  - Memo: COS by Segment
  - Memo: GP / GM by Segment
- **Notes & Customizations**:
  - Multiple memo tables are collocated in this block (ARR, revenue, COS, GP). Mixed scaling (thousands) across many rows and columns.
  - Some columns are split into different block groupings (e.g., AR/quarter snapshot columns) — take care when extracting time series.

---

### Headcount Summary
- **Section Type**: Headcount Table / Operational Metrics
- **Description & Purpose**: Headcount by functional area (Executive, Engineering, Product, Sales, Marketing, Content, Finance/HR/Operations) plus totals and related sales rep metrics. Used for operating cost analysis and sales productivity metrics.
- **Cell Range**: A110:FS126
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series). Some headcount columns also appear in E:Q summary columns.
  - **Date Range**: Monthly series 2015-01 to 2027-12 (ds_1).
  - **Frequency**: Monthly (primary), with summary snapshots in E:Q.
- **Key Components**:
  - Headcount by function and Total Headcount
  - Avg effective quota‑carrying sales reps
  - New ARR per Sales Rep / New Clients per Sales Rep
  - Memo: India Employees
- **Notes & Customizations**:
  - Several headcount numbers are scaled (thousands) in some columns.
  - Sales productivity metrics are integrated in same block (not a separate sheet).

---

### Client & Subscriber Counts
- **Section Type**: Customer / Subscriber Count Tables
- **Description & Purpose**: Counts and flow metrics for clients and subscribers: Clients (beginning, added, churned, end of period), ARR per client, users per client and total users. Designed to support cohort and ARPC/ARPU calculations.
- **Cell Range**: A128:FS189
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series). Snapshot/summary columns in E:Q are used for earlier/higher‑level periods.
  - **Date Range**: Monthly series 2015-01 to 2027-12 (ds_1).
  - **Frequency**: Monthly (primary). Some client flows may be presented as period aggregates in E:Q.
- **Key Components**:
  - Clients flow (Beginning, Added, Churned, End)
  - ARR per Client, Avg Users per Client
  - Total Users (End of Period)
- **Notes & Customizations**:
  - Multiple instances of the same label appear in different sub-rows (e.g., Clients Beginning/End by cohort). Numeric scaling used for many columns.

---

### Retention Metrics
- **Section Type**: Retention / Cohort Metrics
- **Description & Purpose**: Retention KPIs including Upsells, Up for Renewal, Renewed amounts, Annual Net/Gross/Cohort retention and TTM variants. Used to track revenue retention performance and cohort behavior over time.
- **Cell Range**: A191:FS205
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series). Some retention TTM calculations extend across AE..FS blocks as TTM rollups.
  - **Date Range**: Monthly series 2015-01 to 2027-12 (ds_1).
  - **Frequency**: Monthly (primary); Annual retention measures reported as derived annual metrics.
- **Key Components**:
  - Upsells, Up for Renewal, Renewed
  - Annual Net Dollar Retention, Annual Gross Dollar Retention, Annual Cohort Retention
  - TTM versions of the annual retention metrics
- **Notes & Customizations**:
  - TTM blocks use AE:FS for extended rolling calculations; some columns scaled to thousands.

---

### Key Performance Indicators (Summary & Detail)
- **Section Type**: KPI Dashboard (Summary + Detail)
- **Description & Purpose**: Consolidated KPIs for executive review: top KPI summary (totals and high level ratios) and detailed KPI rows (margins, bookings/ARR per rep, ARPU/ARPC, LTV/CAC, payback period, etc.). Supports holistic performance monitoring and investor metrics.
- **Cell Range**: A207:FS262
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series). Summary snapshots also present in E210:L210 and other E:Q columns.
  - **Date Range**: Monthly series 2015-01 to 2027-12 (ds_1).
  - **Frequency**: Monthly (primary). Many KPIs are expressed on an annualized or per‑period basis (ARPC, ARPU, LTV/CAC).
- **Key Components**:
  - KPI Summary (total ARR/Bookings aggregates)
  - KPI Detail rows: Margin, Avg quota carrying reps, Bookings per rep, ARR per rep, ARPC, ARPU, COS per client/subscriber, LTV / CAC, Payback Period, Annual retention metrics
- **Notes & Customizations**:
  - The KPI block mixes absolute financials (many scaled to thousands) and ratios/percentages.
  - Some KPI values are split into separate column groups (e.g., T:AJ then AK:FS) — pay attention to column splits when extracting ranges.

---

### Key Performance Indicators by Segment
- **Section Type**: KPI by Segment / Segment KPIs
- **Description & Purpose**: Segment‑level KPIs mirroring the main KPI set but broken down by business segments. Includes ARPC/ARPU, support/upsell cost per client, CAC, LTV, payback and other segment metrics to evaluate unit economics by segment.
- **Cell Range**: A265:FS355
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary monthly series). Many segment KPIs also appear in G:Q and AR:FS grouped columns (segment-specific placements).
  - **Date Range**: Monthly series 2015-01 to 2027-12 (ds_1).
  - **Frequency**: Monthly (primary). KPI metrics often presented on annualized or per-period bases.
- **Key Components**:
  - ARR / Revenue per client/subscriber metrics by segment
  - CAC, LTV, LTV/CAC, Support and Upsell cost per client
  - Payback Period (months) and Annual Gross Dollar Retention by segment
- **Notes & Customizations**:
  - Complex layout: many segment KPI rows use different column groupings (G:Q and AR:FS for mirrored segment columns) and heavy use of thousands scaling.
  - Section contains many repeated metric rows for multiple segments — treat extraction as repeated blocks.

---

### Debt Availability Build
- **Section Type**: Debt Availability / Financing Build
- **Description & Purpose**: Model for debt availability based on MRR multiplier, trailing 3‑month MRR metrics, churn, and retention to compute available debt capacity. Intended for lender/financing analysis and availability schedules.
- **Cell Range**: A359:DW372
- **Time Series Horizon**:
  - **Dates Location**: Primary time series for the sheet at T2:FS2 remains the header for this area when applicable; however this block places computed elements in BW362:DW372 (rightward columns outside the main T:FS block) and also references trailing windows (BW:DW).
  - **Date Range**: The sheet's primary monthly series is 2015-01 to 2027-12 (ds_1); the Debt build uses the later-width BW:DW column group for the availability calculation.
  - **Frequency**: Monthly (primary), with trailing 3‑month aggregation elements (T3M).
- **Key Components**:
  - Multiplier of MRR
  - T3M MRR, T3M Revenue Lost, T3M Churn
  - Annualized Retention Rate and Current MRR
  - Final Availability amounts (rows A369:A372 paired with BW369:DW372)
- **Notes & Customizations**:
  - This block stores outputs in a separate right-side column group (BW:DW) rather than the main T:FS series — extract using the explicit BW:DW ranges provided.
  - Several rows within the block use thousand scaling.

---

Notes on Dates / Extraction:
- Primary date labels for the sheet are defined in T2:FS2 and reference date series "ds_1" (monthly series from 2015-01-31 to 2027-12). When extracting time series for any section prefer T2:FS2 as the canonical date header.
- Many sections also include left-side summary or historical columns (E:Q) and some right-side specialized columns (e.g., BW:DW, AR:FS, BP:FS) — those are intentionally used for aggregated snapshots or segment mirroring. When retrieving a section, use the section cell range listed above (includes both summary and main monthly blocks) to ensure complete capture.