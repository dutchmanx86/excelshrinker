## 1. Spreadsheet Overview
- **Sheet Name**: Headcount and Salaries CTRL
- **Key Sections Identified**:
  - Title / Control Header
  - Time Axis / Date Labels
  - Headcount (by function, drivers, added heads; includes India sub-section)
  - Salary (by function; includes Average India salary and detailed salary rows)

## 2. Detailed Section Analysis

### Title / Control Header
- **Section Type**: Sheet Header / Metadata
- **Description & Purpose**: Top-left labels that identify the company and the sheet, plus an initial scenario indicator. Used for human context and light control/documentation.
- **Cell Range**: B1:B3
- **Time Series Horizon**:
  - **Dates Location**: none (this is a static header)
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**: Company name ("AlphaSense, Inc."), sheet title ("Headcount and Salaries CTRL"), scenario label ("1 - Base - $25mm").
- **Notes & Customizations**: Static; no numeric series. Useful anchor when locating the sheet programmatically.

---

### Time Axis / Date Labels
- **Section Type**: Date / Time axis (column headers)
- **Description & Purpose**: Column-level period labels that drive all time series data in the sheet. This area contains the annual and monthly date series used by both the Headcount and Salary sections.
- **Cell Range**: B6:FS8
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual (primary): E6:Q6
    - Repeating annual / extended annual: T6:FS6
    - Monthly series (detailed): T8:FS8
  - **Date Range**:
    - Annual series (E6:Q6): 2015 to 2027 (annual)
    - Repeating annual (T6:FS6): repeats annual values from 2015 to 2027 (patterned/repeating)
    - Monthly series (T8:FS8): 2015-01 to 2027-12 (monthly)
  - **Frequency**: Annual (E6:Q6 and T6:FS6), Monthly (T8:FS8)
- **Key Components**: Year and Month header cells (B6 = "Year", B7 = "Month"), two annual date bands and one monthly date band for extended projections.
- **Notes & Customizations**: Two distinct annual bands are present (one core, one repeating/extended) plus a full monthly band. Consumers should check whether a given data row aligns to the annual band (E6:Q6) or the extended/repeating band (T6:FS6 / T8:FS8).

---

### Headcount
- **Section Type**: Key Metrics Table (Headcount by function and drivers)
- **Description & Purpose**: Functional headcount planning and driver metrics. Contains sections for Executive, Engineering, Product, Marketing, Content, Finance/HR/Operations and an India-specific Engineering/Ops section. Includes rows for "added heads in period", ARR-per-head drivers, and aggregated headcount metrics used to drive Revenue/ARR models.
- **Cell Range**: A11:FS93
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual columns: E6:Q6 (primary) and T6:FS6 (extended)
    - Monthly detail (where applicable): T8:FS8
  - **Date Range**:
    - Annual: 2015 → 2027 (annual series)
    - Monthly: 2015-01 → 2027-12 (monthly series for detailed rows)
  - **Frequency**: Primarily Annual; some sub-rows use Monthly or extended annual columns
- **Key Components** (major sub-components, not exhaustive):
  - Function headings and driver rows: Executive; Engineering; Product; Marketing; Content; Finance, HR, and Operations
  - Driver metrics: "ARR per [Function] - 2019+ Driver", "ARR per [Function] - 2018 Driver" (used to convert headcount to ARR)
  - Additions / hires: "[Function] Headcount Added in Period" rows (periodic hires)
  - India sub-section: "Engineering/Ops - India" with "Added Heads" and separate arrays (notably extends across the extended column band)
  - Totals / aggregate headcount rows (implicit in the block)
- **Notes & Customizations**:
  - Many numeric cells in this block use a scale of 1,000 (thousands); consumers must respect scale metadata.
  - The India added-heads row shows data extending into far-right columns (BX:FS) indicating a longer/expanded horizon for that sub-component.
  - Column alignment is mixed: some driver values align to the core annual band (E:Q) while others use the extended annual/monthly bands (T:FS). Check row metadata to determine which date axis to use for each sub-row.

---

### Salary
- **Section Type**: Key Metrics Table (Salary by function; compensation schedules)
- **Description & Purpose**: Detailed salary and compensation schedules by function. This section includes Executive Salary, Engineering Salary, Product Salary, Marketing Salary, Content Salary, Finance/HR/Operations Salary, Engineering/Ops - India Salary and supporting rows (average salary, component breakdowns). Used to convert headcount into total salary expense.
- **Cell Range**: A95:FS151
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual columns: E6:Q6 (primary) and T6:FS6 (extended)
    - Monthly detail (where applicable): T8:FS8
  - **Date Range**:
    - Annual: 2015 → 2027 (annual series)
    - Monthly: 2015-01 → 2027-12 (monthly series for detailed rows)
  - **Frequency**: Primarily Annual, with extended columns supporting longer projections and some monthly detail
- **Key Components**:
  - Function salary blocks: Executive Salary; Engineering Salary; Product Salary; Marketing Salary; Content Salary; Finance/HR/Operations Salary; Engineering/Ops - India Salary
  - Average salary metrics (e.g., "Average Engineering/Ops - India Salary") used as inputs to calculate salary cost per added head or ongoing headcount
  - Sub-rows include detailed salary components and lines that are scaled (many cells have a 1,000 scale)
- **Notes & Customizations**:
  - Consistent use of a 1,000 scale on many numeric cells — apply this scale when aggregating or exporting.
  - Salary blocks mirror the function groups in the Headcount section to allow direct multiplication of headcount x salary.
  - Extended horizon columns (T:FS) are populated in many salary rows — salary projections extend to the same horizon as the extended annual/monthly axis.

---

General Notes & Retrieval Guidance
- The sheet uses three date series defined as:
  - Annual (E6:Q6): 2015 → 2027 (1-year increment)
  - Repeating annual / extended (T6:FS6): 2015 → 2027 repeated across the extended band
  - Monthly (T8:FS8): 2015-01 → 2027-12 (1-month increment)
- Many numeric ranges are stored at a thousands scale (cells marked with scale=1000 in the metadata). When extracting values programmatically, apply the scale where indicated.
- For broad retrieval, use:
  - Headcount block: A11:FS93
  - Salary block: A95:FS151
  - Date headers: B6:FS8
  - Title / sheet header: B1:B3

If you want, I can (a) produce a compact mapping of the principal function row start rows (e.g., exact row numbers for Executive, Engineering, Product, etc.) or (b) produce code-ready ranges (JSON) for automated extraction. Which would you prefer?