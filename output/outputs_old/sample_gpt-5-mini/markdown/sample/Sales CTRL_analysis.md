## 1. Spreadsheet Overview
- **Sheet Name**: Sales CTRL
- **Key Sections Identified**:
  - Header & Time Axis (date series and titles)
  - Headcount — Additions / Removals by Role (detailed by AE / AM / VP / CRO / etc.)
  - Compensation — Salary & Sales Bonus (by role)
  - Operational Drivers & Ratios (Managers-per-Rep, PS-per-AE, SDR drivers, Reps-per-Manager, etc.)
  - Drivers & Assumptions (Historic 2018 drivers vs 2019-and-beyond annual drivers; "Old Assumptions" area)
  - Totals / Percent of Total Headcount and supporting metrics (embedded within headcount sections)

## 2. Detailed Section Analysis

### Header & Time Axis
- **Section Type**: Sheet header and date axis
- **Description & Purpose**: Contains the workbook title, sheet subtitle, model version marker and the primary date/period axis used by the whole sheet. This is the reference area that defines the annual and monthly time series that columns throughout the sheet align to.
- **Cell Range**: A1:FS8
- **Time Series Horizon**:
  - **Dates Location**:
    - Primary annual labels: E6:Q6 (date series id = ds_1)
    - Extended annual columns: T6:FS6 (date series id = ds_2)
    - Monthly series (where used): T8:FS8 (date series id = ds_3)
  - **Date Range**:
    - Annual series (ds_1 / ds_2): 2015 to 2027 (ds_1 defined as Annual series from 2015 to 2027; ds_2 is repeating annual)
    - Monthly series (ds_3): 2015-01 to 2027-12
  - **Frequency**:
    - ds_1 / ds_2: Annual
    - ds_3: Monthly
- **Key Components**:
  - Workbook and sheet title rows (e.g., "AlphaSense, Inc.", "Sales Representatives CTRL", model version label "1 - Base - $25mm")
  - Year and Month headings and the three date series placements (annual primary, extended annual, monthly)
- **Notes & Customizations**:
  - Two distinct annual ranges are present (E6:Q6 and T6:FS6) — the sheet uses both a primary annual block and an extended/repeating annual block for a longer horizon.
  - A monthly series (T8:FS8) is available for rows that require month-level granularity.

---

### Headcount — Additions & Removals by Role
- **Section Type**: Headcount driver tables (per-role Add / Remove flows)
- **Description & Purpose**: Detailed rows capturing headcount changes (added / removed / active / base / target / upside) for many sales roles (Quota Sales Reps, Account Manager, AE - Financial, AE - Corporate, AE - Enterprise, AE - Other, VP - Bus Dev, CRO, Product Specialist, Sales Admin, Sales Manager, Sales Operations Manager, SDR, etc.). This section is used to model headcount build-up and workforce changes over the time horizon.
- **Cell Range**: A11:FS154
- **Time Series Horizon**:
  - **Dates Location**:
    - Primary annual columns: E13:E/Q13… (aligned to E6:Q6) — general column axis E6:Q6 (ds_1)
    - Extended horizon columns where present: T#:FS# (aligned to T6:FS6, ds_2)
    - Where month granularity is used in specific rows, T8:FS8 (ds_3) applies
  - **Date Range**:
    - Annual: 2015 → 2027 (per ds_1/ds_2)
    - Monthly (if used for a row): 2015-01 → 2027-12 (ds_3)
  - **Frequency**: Primarily Annual; some rows reference Extended Annual columns and occasional monthly series for more granular inputs.
- **Key Components**:
  - Per-role "Headcount Added in Period" and "Headcount Removed in Period" rows (active/base/target/upside variants)
  - Per-role subtotals and "Total Headcount" indicators (Total Headcount entries appear throughout these blocks)
  - Row markers/section separators in column A (cells with "x") used to visually group blocks by role
- **Notes & Customizations**:
  - Numeric inputs in many rows are scaled (many ranges use a scale = 1000). Expect values in thousands for some columns.
  - Totals and percentage rows (e.g., "% of Total Headcount") are present in this area at specific rows; these are embedded rather than in a separate summary block.
  - The layout mixes short (E:Q) and extended (T:FS) column spans depending on the row — the full A11:FS154 range covers all variants.

---

### Compensation — Salary & Sales Bonus by Role
- **Section Type**: Compensation tables (Salary and Variable/Bonus)
- **Description & Purpose**: Salary and sales bonus (incentive) schedules for roles (Quota Sales Reps Salary, Account Manager Sales Bonus, AE - Financial Sales Bonus, AE - Corporate Sales Bonus, VP - Bus Dev Sales Bonus, AE - Enterprise Sales Bonus, Account Manager - Corporate/Financial, Enablement, CS Manager, etc.). Used to convert headcount to cost/compensation expense over time.
- **Cell Range**: A157:FS261
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual columns aligned to E6:Q6 (primary annual ds_1)
    - Extended horizon columns (T6:FS6, ds_2) used for later-year projections
    - Some salary/bonus rows include cell ranges that extend into BX/CB/… for longer-term arrays; these are within the A157:FS261 envelope
  - **Date Range**:
    - Annual: 2015 → 2027
    - Monthly (if used for particular bonus phasing): 2015-01 → 2027-12
  - **Frequency**: Primarily Annual with extended annual columns; select rows include monthly where specified
- **Key Components**:
  - Base salary schedules (per-role)
  - Sales bonus schedules (per-role) and roll-ups
  - Some rows include multi-column blocks for FY drivers vs longer horizons (note: e.g., some ranges span BX:FS indicating extended columns included)
- **Notes & Customizations**:
  - Many numeric ranges in this section use scale = 1000 (values stored in thousands).
  - Bonus rows sometimes use different column patterns than salary rows (mixed column spans).
  - "x" flags in column A continue to mark sub-block boundaries.

---

### Operational Drivers & Ratios (Managers / PS / SDR / Reps per Manager / ARR per Manager)
- **Section Type**: Driver & ratio tables (operational capacity planning)
- **Description & Purpose**: Contains the operational assumptions used to drive headcount demand and structure: managers-per-rep, SDRs-per-manager, AE-per-SDR, Product Specialist per AE, PS per Manager, Reps per Sales Manager, Account Manager ARR per Manager (Corp / Fin), and similar ratios that translate revenue/ARR or quotas into required headcount.
- **Cell Range**: A262:FS321
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual: E273:Q273 (example row for Sales Manager Reps per Manager) and similar rows align to E6:Q6 (ds_1)
    - Extended horizon T273:FS273 aligns to T6:FS6 (ds_2)
  - **Date Range**:
    - Annual: 2015 → 2027
    - Monthly: 2015-01 → 2027-12 (where specific rows use monthly series)
  - **Frequency**: Annual primary, with extended annual coverage across full horizon
- **Key Components**:
  - Manager-to-rep ratios (Sales Manager, SDR Manager, PS Manager)
  - Role-specific productivity assumptions (AE per Product Specialist, AE per SDR)
  - ARR-per-manager drivers (Account Manager - Corp / Fin)
- **Notes & Customizations**:
  - Several rows exist in both "2018 driver" (historical headcount-added in 2018 style) columns and "2019 and beyond annual driver" blocks — this dual structure is used across drivers to support legacy versus new annual-driver logic.
  - The driver rows are referenced by many downstream headcount and comp rows (these act as central drivers).

---

### Drivers & Assumptions — Old Assumptions & 2019+ Annual Drivers
- **Section Type**: Assumptions repository (historic drivers + long-run annual drivers)
- **Description & Purpose**: Houses an "Old Assumptions (To Be Deleted)" area and the large set of 2018-driver rows plus the 2019-and-beyond annual drivers used to calculate stable long-run ratios. This section includes numerous role-specific "added" drivers, per-role ratios for 2018 and for the annual repeating model, and other GTM/organizational assumptions.
- **Cell Range**: A334:FS574
- **Time Series Horizon**:
  - **Dates Location**:
    - Historic-driver blocks often use E338:H338 (short blocks) and T338:BW338 (multi-column historic ranges)
    - Annual driver columns align to E6:Q6 (ds_1) and extended to T6:FS6 (ds_2)
    - Where monthly drivers exist they align to T8:FS8 (ds_3)
  - **Date Range**:
    - Annual: 2015 → 2027
    - Historic driver mini-blocks include 2018-specific columns (explicit 2018-driver columns are present)
    - Monthly: 2015-01 → 2027-12 (ds_3) where used
  - **Frequency**: Mix of single-year historic columns (2018), annual repeating series (2019+), and occasional monthly series
- **Key Components**:
  - "Old Assumptions (To Be Deleted)" header and its specific 2018-driver rows
  - 2019+ annual driver rows for Manager, Product Specialist, Sales Admin, Sales Manager, SDR, Recruiter, Enablement, Sales Operations, GTM Strategy, etc.
  - Role-specific long-run per-manager and productivity drivers
- **Notes & Customizations**:
  - Some driver rows extend into non-standard columns (e.g., T:BW, CD:FS) to capture historical or extended projections — the full A334:FS574 range captures all of them.
  - The sheet keeps both legacy 2018-driver blocks and 2019+ annual drivers side-by-side to preserve backward calculations while enabling new annual-driver logic.
  - Many numeric driver rows also use scale = 1000.

---

### Totals, Percent Metrics & Summary Indicators (embedded)
- **Section Type**: Totals & KPI rows embedded inside headcount and driver blocks
- **Description & Purpose**: Throughout the headcount and drivers sections there are recurring "Total Headcount" rows and "% of Total Headcount" / "Annual Increase" metrics used to summarize and benchmark headcount allocations across functions. These are not isolated to a single contiguous location but are embedded at multiple role-block ends.
- **Cell Range**: Distributed; primary occurrences fall inside:
  - A11:FS154 (headcount totals embedded)
  - A334:FS574 (assumptions / some totals and % metrics)
  - Specific labeled cells noted in the inverted index (e.g., "Total Headcount" appears at B13, B28, B70, B112, B127, B142, B266, B297, B354, B371, B388, B405, B422, B439, B449)
- **Time Series Horizon**:
  - **Dates Location**: same column axes as the blocks they summarize (E6:Q6 primary; T6:FS6 extended; T8:FS8 monthly where used)
  - **Date Range**: Annual 2015→2027 and monthly 2015-01→2027-12 where applicable
  - **Frequency**: Matches source rows (primarily Annual)
- **Key Components**:
  - "Total Headcount" markers (per role and for aggregate)
  - "% of Total Headcount" rows (embedded at certain section ends)
  - "Annual Increase" entries used to grow certain drivers or headcount assumptions year over year
- **Notes & Customizations**:
  - Because totals and percent metrics are embedded, a consumer retrieving totals should query the specific rows identified above rather than expecting one contiguous summary area.
  - The inverted index lists multiple discrete cells where "Total Headcount" and "% of Total Headcount" labels appear — these are the exact row label positions to reference for locating that metric per role.

---

Notes / Implementation guidance for downstream retrieval:
- Primary annual column axis: E6:Q6 (ds_1) is the canonical date row for most annual figures. Use T6:FS6 when retrieving extended-year annual data (ds_2). For month-level series pick the monthly row T8:FS8 (ds_3).
- Many numerical ranges use a scale = 1000 — when extracting values check the cell metadata for scaling to restore true numeric amounts.
- Blocks are demarcated visually by column-A "x" markers and the B-column string labels (role names). To retrieve a specific role’s table, locate the row whose column B contains the role name (examples: B29 = "AE - Financial Headcount Added in Period", B157 = "Quota Sales Reps - Salary", B310 = "Product Specialist per Manager", etc.) and then extract the row’s numeric range across the same columns used for that block (typically E:Q and/or T:FS).
- If you need exact label-to-row mappings for a smaller set of roles, I can produce a compact lookup of role label → row number(s) (using the sheet’s label rows captured in the analysis).