## 1. Spreadsheet Overview
- **Sheet Name**: ARR and Rev CTRL
- **Key Sections Identified**:
  - Sheet Header & Date Rows
  - Revenue (Rev % of MRR by segment)
  - Quota & Sales Role Targets
  - Productivity, Seasonality & Allocation
  - ARR Composition (New Bookings & Upsell by role)
  - Segment ARR and ARR / User metrics (Financial, Corporate, Other)

## 2. Detailed Section Analysis

### Sheet Header & Date Rows
- **Section Type**: Metadata / Time-series header
- **Description & Purpose**: Contains the workbook and sheet title, scenario selector text, and the primary date row(s) used across the sheet. This is the authoritative location for the time-axis (annual and monthly series) that other sections reference.
- **Cell Range**: A1:FS8
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual (primary): E6:Q6 (date series id ds_1)
    - Repeating/extended annual: T6:FS6 (date series id ds_2)
    - Monthly series: T8:FS8 (date series id ds_3)
  - **Date Range**:
    - ds_1 / ds_2 (annual): 2015-01-01 through 2027 (pattern: Annual series from 2015 to 2027)
    - ds_3 (monthly): 2015-01-31 through 2027-12 (pattern: Monthly series from 2015-01 to 2027-12)
  - **Frequency**: Annual (primary), with a secondary repeating-annual horizon and a monthly horizon available
- **Key Components**:
  - Workbook / sheet titles (B1, B2)
  - Scenario / label line (B3)
  - Year and Month label rows (B6, B7)
  - Primary date rows (E6:Q6, T6:FS6, T8:FS8)
- **Notes & Customizations**:
  - Two different annual date ranges are present (E6:Q6 and T6:FS6) — one is the primary annual series and one is an extended/repeating annual series for longer horizon reporting. Monthly series (ds_3) exists for detailed monthly reporting.

---

### Revenue (Rev % of MRR by segment)
- **Section Type**: Key Metrics Table (Revenue / Rev % of MRR)
- **Description & Purpose**: Presents revenue-related metrics expressed as percentages of MRR and numeric revenue figures (scaled in thousands in the numeric columns). It is split by revenue buckets (Financial, Corporate, Other) and provides the revenue % of MRR rows and the numeric underlying amounts.
- **Cell Range**: A11:FS31
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (primary annual labels covering the numeric columns I:Q) and T6:FS6 for extended years; monthly detail if present aligns to T8:FS8.
  - **Date Range**: Annual 2015 → 2027 (ds_1 / ds_2); monthly 2015-01 → 2027-12 for any monthly sub-series (ds_3)
  - **Frequency**: Annual (primary); monthly available for extended detail
- **Key Components**:
  - Rev % of MRR - Financial / Corporate / Other (label rows)
  - Corresponding numeric rows for revenue (annual columns I:Q and extended columns T:FS)
  - Percentage rows (H13:Q13, H20:Q20, H27:Q27) and underlying numeric amounts (I14:Q31)
- **Notes & Customizations**:
  - Numeric data in this block is stored at two scales: percentage rows and revenue amounts (revenue amounts often scaled by 1,000).
  - The block spans both the primary annual horizon and the extended repeating-annual / monthly horizons.

---

### Quota & Sales Role Targets
- **Section Type**: Key Metrics Table (Quota by role / Sales targets)
- **Description & Purpose**: Contains quotas and target lines for sales roles (Account Manager, AE - Financial, AE - Corporate, AE - Enterprise, VP Bus Dev) and their Active/Base/Upside splits. Used for headcount/coverage planning and revenue target allocation across roles and scenarios.
- **Cell Range**: A34:FS116
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (primary annual labels for I:Q columns) and T6:FS6 for extended years
  - **Date Range**: Annual 2015 → 2027 (ds_1 / ds_2)
  - **Frequency**: Annual (primary)
- **Key Components**:
  - Master "Quota" label and per-role quota rows (Account Manager - Active / Base / Upside; Quota - AE - Financial / Corporate / Enterprise and their Base/Upside / VP Bus Dev)
  - Numeric quota values (I:Q for the core horizon with extended values in T:FS)
  - Columns include both immediate horizon (I:Q) and extended/forecast horizon (BX:FS as used)
- **Notes & Customizations**:
  - Many quota lines have both "level" labels (Active/Base/Upside) and separate numeric rows; numbers are sometimes stored in thousands.
  - The block is broader than a simple table — it includes both short-term and long-term (extended) quota fields (hence the use of FS columns).

---

### Productivity, Seasonality & Allocation
- **Section Type**: Key Metrics Table (Productivity & Allocation)
- **Description & Purpose**: Captures productivity metrics (productivity as % of quota), seasonality adjustments, and allocation of sales effort between segments (e.g., VP - Bus Dev % to Financial/Corporate, AE allocations). This section converts quotas and coverage into effective productivity by period and segment.
- **Cell Range**: A119:FS241
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (primary annual), with extended annual T6:FS6 and monthly series where applied (T8:FS8)
  - **Date Range**: Annual 2015 → 2027 (ds_1 / ds_2); monthly 2015-01 → 2027-12 when monthly seasonality is present
  - **Frequency**: Annual (primary), with seasonality often applied on a monthly/quarterly pattern
- **Key Components**:
  - Productivity - % of Quota, Adjustment, Seasonality (seasonality input rows and seasonality-applied numeric rows)
  - Productivity - Allocation and % splits (VP / AE allocation rows)
  - Role-level allocation percentages to Financial / Corporate segments
- **Notes & Customizations**:
  - Seasonality rows are present and used to modify annual quotas into periodized outputs; some seasonality and adjustment cells exist in extended columns (CB..FS).
  - Allocation rows are expressed as percentages; underlying numeric application is in adjacent numeric rows (scaled where noted).

---

### ARR Composition (New Bookings & Upsell by role)
- **Section Type**: Key Metrics Table (ARR composition / New vs Upsell)
- **Description & Purpose**: Summarizes how Total ARR is built from New Bookings and Upsell components, broken down by sales roles and segments. Used to track contribution to ARR from each role and to reconcile quotas/production to ARR outcomes.
- **Cell Range**: A157:FS219
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (primary annual span for I:Q numeric columns) and T6:FS6 for extended horizon
  - **Date Range**: Annual 2015 → 2027 (ds_1 / ds_2)
  - **Frequency**: Annual (primary)
- **Key Components**:
  - "Total ARR - % New Bookings" and related role-level breakdown rows
  - "Total ARR - % Upsell" with corresponding role-level upsell rows
  - Role-specific numeric contribution rows (I159:Q219 and extended BX:FS columns)
- **Notes & Customizations**:
  - This block ties quotas/productivity to ARR outcomes and includes multiple role-level series for both New Bookings and Upsell.
  - Numeric rows are often scaled (1,000) and repeated across extended horizon columns.

---

### Segment ARR and ARR / User metrics (Financial, Corporate, Other)
- **Section Type**: Key Metrics Table (Segment ARR rolls + Unit metrics)
- **Description & Purpose**: Segment-level ARR roll-ups for Financial, Corporate and Other segments and unit metrics such as ARR / User for Upside / Base / Target. This is the bottom-line segment reporting area used for product/business-level performance and unit economics analysis.
- **Cell Range**: A248:FS317
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual labels: E6:Q6 (primary) and extended annual in T6:FS6
    - Monthly detail if present aligns with T8:FS8
  - **Date Range**:
    - Annual 2015 → 2027 (ds_1 / ds_2)
    - Monthly 2015-01 → 2027-12 (ds_3) for any monthly series
  - **Frequency**: Annual (primary); several unit metrics include rolling/extended annual and monthly capacity for detail
- **Key Components**:
  - Segment headings: Financial (B248 and rows 251–255), Corporate (B272 and rows 275–279), Other (B296 and rows 298–303)
  - Segment-level ARR numeric rows (F250:Q250, F274:Q274, F298:Q298 and their expanded F..Q and T..FS ranges)
  - ARR / User metrics: ARR / User - Upside, Base, Target (rows around B265, B282, B289, B299, B306, B313)
  - Supporting numeric detail rows for users and ARR per user (I:Q and extended columns)
- **Notes & Customizations**:
  - ARR amounts are stored at different scales (many core values scaled in thousands).
  - ARR / User metrics are recorded separately per segment and scenario (Upside / Base / Target) and repeated across the long forecast horizon (T:FS).
  - This block is the primary output area for segment P&L-like ARR summaries and unit-economics.

---

If you want, I can:
- produce a CSV-style list of the exact row labels detected per section for quick indexing, or
- return these section ranges as a JSON object for programmatic retrieval.