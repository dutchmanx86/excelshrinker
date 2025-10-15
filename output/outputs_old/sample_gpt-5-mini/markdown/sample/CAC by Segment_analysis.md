## 1. Spreadsheet Overview
- **Sheet Name**: CAC by Segment
- **Key Sections Identified**:
  - Worksheet Header & Time Axis
  - Summary (Top-level CAC / Upsell / Support summary)
  - Detail (Detailed segment / role-level breakout)
  - People Costs & Wages (Wages, capitalized wages, related people cost detail)
  - Segment Allocations & KPIs (Adjusted sales & marketing cost, Financial / Corporate user counts and support costs)

## 2. Detailed Section Analysis

### Worksheet Header & Time Axis
- **Section Type**: Worksheet Header & Time Axis
- **Description & Purpose**: Contains the company name and sheet title, plus the primary period headers used across the sheet. This is the authoritative location for the time axis used by downstream tables (the sheet exposes two column time bands: a historical/aggregated block and a detailed monthly forecast block).
- **Cell Range**: A1:FS3
- **Time Series Horizon**:
  - **Dates Location**:
    - Primary monthly series: T2:FS2 (date-typed cells; mapped to date_series id ds_1)
    - Secondary/aggregated periods (historical buckets): E2:Q2 (numeric / aggregated headers — not linked to ds_1 in metadata)
  - **Date Range**:
    - T2:FS2: Monthly series from 2015-01 to 2027-12 (ds_1; start_date 2015-01-31)
    - E2:Q2: Historical / aggregated periods (no explicit date mapping in metadata)
  - **Frequency**:
    - T2:FS2: Monthly
    - E2:Q2: Aggregated/historical (frequency unspecified in metadata)
- **Key Components**:
  - Company title (B1 = "AlphaSense, Inc.")
  - Sheet title (B2 = "CAC by Segment")
  - Primary monthly date row (T2:FS2)
  - Secondary / historical header block (E2:Q2)
- **Notes & Customizations**:
  - The sheet uses a split time-axis: E:Q for historical/aggregated columns and T:FS for the detailed monthly series. The monthly series is explicitly defined as ds_1 in the file metadata.

---

### Summary (Top-level CAC / Upsell / Support summary)
- **Section Type**: Key Metrics Table (Top-level summary)
- **Description & Purpose**: High-level summary of CAC, Upsell Cost and Support Cost metrics (top-of-sheet KPIs). Intended to give a quick, consolidated view of the main CAC-related metrics before the full-detail breakout.
- **Cell Range**: A5:FS20
- **Time Series Horizon**:
  - **Dates Location**:
    - Primary monthly forecast columns: T2:FS2 (applies to the summary numeric ranges in T8:FS8, T13:FS13, T18:FS18, etc.)
    - Historical / aggregated columns: E2:Q2 (applies to the summary numeric ranges in E8:Q8, E13:Q13, E18:F18, etc.)
  - **Date Range**:
    - Monthly forecast: January 2015 → December 2027 (T2:FS2)
    - Historical: aggregated buckets in E2:Q2 (no explicit date mapping)
  - **Frequency**:
    - Forecast: Monthly
    - Historical: Aggregated / unspecified
- **Key Components**:
  - Top-level labels and groupings (B5 = "Summary")
  - Upsell Cost block (B7 and associated numeric rows, e.g., row 8)
  - CAC block (B12 and associated numeric rows, e.g., row 13)
  - Support Cost top-line (B17 and associated numeric rows, e.g., row 18)
  - Totals for these metrics across historical and forecast columns
- **Notes & Customizations**:
  - Many summary numeric ranges appear in two bands (E:Q and T:FS) — ensure callers retrieve both bands if full time coverage is needed.
  - Numerical formatting sometimes uses a scale of 1,000 for display; check cell metadata before numeric aggregation.

---

### Detail (Detailed segment / role-level breakout)
- **Section Type**: Detailed Segment Breakdown / Role-Level Table
- **Description & Purpose**: Full breakdown by segment and internal role buckets (e.g., Total Company, Financial, Corporate, Account Manager, AE roles, VP — Bus Dev, etc.). This is the area that shows per-role/per-segment cost and user metrics across the same two time bands (historical & monthly forecast).
- **Cell Range**: A22:FS67
- **Time Series Horizon**:
  - **Dates Location**:
    - Primary monthly forecast: T2:FS2 (applies to detailed rows with T*:FS* ranges, e.g., T25:FS25, T26:FS26, ...)
    - Historical / aggregated: E2:Q2 (applies to G25:Q25 and E/Q blocks)
  - **Date Range**:
    - Monthly forecast: January 2015 → December 2027 (T2:FS2)
    - Historical: aggregated buckets (E2:Q2; not explicitly date-mapped)
  - **Frequency**:
    - Forecast: Monthly
    - Historical: Aggregated / unspecified
- **Key Components**:
  - Segment / role labels (e.g., "Total Company", "Financial", "Corporate", "Account Manager - Corp", "Account Manager", "AE - Financial", "AE - Corporate", "VP - Bus Dev", "AE - Enterprise")
  - Role-level numeric lines for costs, users, or allocations (multiple numeric rows with both historical and monthly columns)
  - Subtotals and "Total" lines (e.g., B56/B65 style "Total")
- **Notes & Customizations**:
  - Several numeric ranges in this block use a 1,000-scale display (scale=1000). Be careful when extracting raw values vs. displayed values.
  - The section is organized vertically by role/segment; lookups should reference the label column (column B) and fetch the horizontal numeric blocks in E:Q and T:FS.

---

### People Costs & Wages
- **Section Type**: Cost Detail Table (People & Wages)
- **Description & Purpose**: Detailed wages and people-cost related items: total wages, product specialist salary splits, % of wages, capitalized wages, and other support-related people costs. This section supports CAC allocation and adjusted people-cost calculations used in higher-level metrics.
- **Cell Range**: A71:FS94
- **Time Series Horizon**:
  - **Dates Location**:
    - Primary monthly forecast: T2:FS2 (applies to rows in this block that have T*:FS* numeric ranges such as T81:FS81, T82:FS82, T86:FS86, T92:FS92, etc.)
    - Historical / aggregated: E2:Q2 (applies to E81:Q81, E82:Q82, E86:G86, etc.)
  - **Date Range**:
    - Monthly forecast: January 2015 → December 2027 (T2:FS2)
    - Historical: aggregated buckets (E2:Q2)
  - **Frequency**:
    - Forecast: Monthly
    - Historical: Aggregated / unspecified
- **Key Components**:
  - "Total Wages" and product specialist salary lines (B81, B82)
  - "% of Total Wages" and related ratios (B83)
  - Capitalized wages (B86 with multi-column numeric blocks)
  - "Other Support Related People Costs" (B92 and its numeric blocks)
- **Notes & Customizations**:
  - Several multi-column ranges are split between E..Q and T..FS and include scale=1000 in cell metadata for many rows. When exporting or summing, apply scale conversion where required.
  - Rows A71 and A97 (marked "x") are used as visual separators; they can be used by parsing logic to delimit blocks.

---

### Segment Allocations & KPIs (Adjusted sales & marketing cost, user counts, support costs)
- **Section Type**: Segment-level KPI & Support Allocations / Summary of Allocations
- **Description & Purpose**: Consolidated allocation results and KPIs segmented by user type (Financial Users, Corporate Users), adjusted S&M costs, "% to CAC", "% to Upsell", $-to-CAC / $-to-Upsell, and segmented support costs. This is the block where allocations are converted to per-user or per-segment KPIs and where totals and support cost allocations appear.
- **Cell Range**: A97:FS140
- **Time Series Horizon**:
  - **Dates Location**:
    - Primary monthly forecast: T2:FS2 (applies to rows in this block with T*:FS* ranges, e.g., T99:FS99, T115:FS115, T117:FS117, T121:FS121, T138:FS138, T140:FS140)
    - Historical / aggregated: E2:Q2 (applies to E99:Q99, E115:Q115, E121:Q121, etc.)
  - **Date Range**:
    - Monthly forecast: January 2015 → December 2027 (T2:FS2)
    - Historical: aggregated buckets (E2:Q2)
  - **Frequency**:
    - Forecast: Monthly
    - Historical: Aggregated / unspecified
- **Key Components**:
  - Adjusted Sales and Marketing Cost lines and related "% to CAC", "% to Upsell", "$ to CAC", "$ to Upsell"
  - Financial Users and Financial Support Costs (B115, B117)
  - Corporate Users and Corporate Support Costs (B138, B140)
  - Aggregate and per-user KPIs that convert cost pools into per-user or percentage metrics
- **Notes & Customizations**:
  - The inverted index shows repeated label placements for certain KPIs (e.g., "Adjusted Sales and Marketing Cost" appears in multiple B-row locations). The concrete numeric blocks for these labels live inside this A97:FS140 range (and earlier summary range for top-level aggregates).
  - Numeric ranges in this block often use scale=1000 formatting; verify before arithmetic operations.
  - The sheet uses multiple "x" markers (A97, A119) to logically separate sub-blocks; these are reliable delimitation cues.

---

Notes for data retrieval and automation:
- Primary machine-readable timeline: T2:FS2 — this is the defined monthly series (ds_1). Always use T2:FS2 to map columns to actual calendar months (2015-01 → 2027-12).
- Many numeric ranges are present twice (E:Q and T:FS). E:Q appears to be a historical / aggregated band and is not explicitly mapped to ds_1; when extracting a full time series, combine E:Q (historical buckets) with T:FS (monthly forecast) based on how the consumer intends to treat aggregated vs. monthly data.
- Watch for 1,000-scale metadata on many numeric ranges — cell metadata indicates scale in those ranges; adjust values if you need raw units.