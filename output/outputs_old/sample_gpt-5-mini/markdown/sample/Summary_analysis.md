## 1. Spreadsheet Overview
- **Sheet Name**: Summary
- **Key Sections Identified**:
  - Change Log / Notes
  - Monthly KPIs & Time Series (primary monthly series covering 2018-01 to 2023-12)
  - Supplementary Monthly Series (subset monthly series ending 2022-12 used by some rows)
  - Annual Summary / Averages (2018–2022)

---

## 2. Detailed Section Analysis

### Change Log / Notes
- **Section Type**: Notes / Change Log
- **Description & Purpose**: Free-text change log detailing recent adjustments to drivers, allocations, and data-cleaning steps. Intended to document model edits and assumptions for reviewers.
- **Cell Range**: A1:A5
- **Time Series Horizon**:
  - **Dates Location**: N/A (text notes)
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**: Short bullet/text lines describing changes (e.g., "CHANGES", adjustments to Web Service COGS, allocation corrections).
- **Notes & Customizations**: Purely textual; no time-series data or numeric scaling.

---

### Monthly KPIs & Time Series (Primary monthly series: 2018-01 to 2023-12)
- **Section Type**: Key Metrics Table / Monthly Time Series
- **Description & Purpose**: Main wide monthly table of core financial and operational metrics across a multi-year horizon. Used for trend analysis, KPI tracking and feeding downstream summaries or visualizations.
- **Cell Range**: B39:BV52
  - This block includes the primary date header row and the associated metric rows that span to BV.
- **Time Series Horizon**:
  - **Dates Location**: C39:BV39 (primary monthly date row; uses ds_1)
  - **Date Range**: January 2018 to December 2023
  - **Frequency**: Monthly
- **Key Components**:
  - High-level financial series and metrics such as Cash, Debt, ARR, Bookings, FCF (these label positions appear in column B within this block).
  - KPI ratios and rolling metrics such as ARR TTM Growth, Margin, EBITDA.
  - Operational metrics such as Reps and Eff Reps.
  - Each metric typically has a single current or summary value in column C with the full monthly series in columns D onward.
- **Notes & Customizations**:
  - Several rows in this area are scaled in the source (numbers stored at a 1,000 scale) for presentation/storage — e.g., rows with ranges like D41:BV41 are scaled by 1,000.
  - The block contains a mixture of rows that follow the full ds_1 horizon (to BV / Dec‑2023) and rows that instead use a shorter monthly series (ds_2) that ends Dec‑2022 (see the next subsection). See "Supplementary Monthly Series" note below for which rows use the shorter series.

---

### Supplementary Monthly Series (subset monthly series: 2018-01 to 2022-12)
- **Section Type**: Supplementary Monthly Series / Alternate Monthly Date Window
- **Description & Purpose**: A subset of monthly date rows and metric series that stop at Dec‑2022. These coexist inside the same visual area as the primary monthly table but use a separate date series and column boundary (up to BJ). Useful for metrics that only have data through 2022 or for historical comparisons limited to that window.
- **Cell Range**: B42:B52 plus C42:BJ42 and D43:BJ52 (logical span: B42:B52 and C42:BJ52)
  - The date header(s) and metric cells using the shorter monthly series occupy columns through BJ.
- **Time Series Horizon**:
  - **Dates Location**: C42:BJ42 (ds_2); additional date header rows appear at C46:BJ46 and C48:BJ48 for grouped subsections that also use ds_2.
  - **Date Range**: January 2018 to December 2022
  - **Frequency**: Monthly
- **Key Components**:
  - A mirror set of monthly values for a subset of metrics (examples include rows where D...:BJ... holds the monthly values instead of extending to BV).
  - Rows that use ds_2 include numeric series for ARR-related rows and several KPI rows (these rows present historical monthly detail to Dec‑2022).
- **Notes & Customizations**:
  - Several of these ds_2-backed ranges are stored with a 1,000x scale (e.g., D44:BJ44, D45:BJ45, D49:BJ49, D50:BJ50, D51:BJ51, D52:BJ52).
  - ds_2 is an explicit shorter monthly date series (start 2018-01-31; pattern indicates through 2022-12). Use the C42:BJ42 header to align columns for retrieval.

---

### Annual Summary / Averages (2018–2022)
- **Section Type**: Key Metrics Table / Annual Summary
- **Description & Purpose**: Compact annual table that captures multi-year aggregates and averages used for high-level benchmarking and multi-year trend metrics (e.g., Avg FCF, Avg Eff Reps, Avg Bookings, Growth Rate).
- **Cell Range**: B56:G65
  - This block contains the annual date header and the per-metric annual values or averages.
- **Time Series Horizon**:
  - **Dates Location**: C56:G56 (ds_3)
  - **Date Range**: 2018 to 2022
  - **Frequency**: Annual
- **Key Components**:
  - Multi-year annual values and computed averages: Avg FCF, Avg Eff Reps, Avg Bookings, Growth Rate and related aggregate metrics.
  - Typical structure: label in column B, single-value column C (often the latest/summary), and the annual series across D:G.
- **Notes & Customizations**:
  - ds_3 is an annual series (start 2018-01-01; pattern 2018–2022).
  - Some annual number ranges have scale adjustments (for example, D58:G58 and similar rows are scaled by 1,000 in the source ranges).
  - This block is designed for multi-year summary analysis rather than detailed monthly trend work.

---

If you want, I can produce a compact mapping table that lists the specific rows (by label text in column B) mapped to their exact cell ranges inside each section (e.g., "Cash — B40, series at C40:BV40"), to accelerate programmatic retrieval.