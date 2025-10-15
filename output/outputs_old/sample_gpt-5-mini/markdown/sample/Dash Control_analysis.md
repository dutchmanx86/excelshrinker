## 1. Spreadsheet Overview
- **Sheet Name**: Dash Control
- **Key Sections Identified**:
  - Sheet header & period labels (Year / Month series)
  - Dashboard control title / sheet-level toggle
  - Support Fees - % of CAC (assumption block)
  - ARR Multiplier (assumption block)
  - Perpetuity Factor (assumption block)
  - ARR Multiplier - Financial (assumption block)
  - Perpetuity Factor - Financial (assumption block)
  - ARR Multiplier - Corporate (assumption block)
  - Perpetuity Factor - Corporate (assumption block)
  - % Travel Costs (assumption block)
  - Scenario presets (repeating scenario labels used across blocks: "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)")

---

## 2. Detailed Section Analysis

### Sheet header & period labels
- **Section Type**: Date / Period Axis / Sheet Title block
- **Description & Purpose**: Top-level sheet title and the primary period headers used to index the time series present throughout the sheet. Contains annual and monthly date series that are used as column headers for the assumption blocks below.
- **Cell Range**: A1:FS8
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual header (primary): E6:Q6 (date series id: ds_1)
    - Annual header (extended/repeating): T6:FS6 (date series id: ds_2)
    - Monthly header (primary): E8:Q8 (numeric/month indicator)
    - Monthly header (extended): T8:FS8 (date series id: ds_3)
  - **Date Range**:
    - ds_1 (E6:Q6) — Annual from 2015 to 2027 (start: 2015-01-01 → years 2015..2027)
    - ds_2 (T6:FS6) — Annual repeating values covering 2015 to 2027 (start: 2015-01-01 → pattern 2015..2027)
    - ds_3 (T8:FS8 / E8:Q8 context) — Monthly series from Jan 2015 to Dec 2027 (start: 2015-01-31 → monthly to 2027-12)
  - **Frequency**: Annual (E6:Q6, T6:FS6) and Monthly (E8:Q8, T8:FS8) are both present and used as column axes.
- **Key Components**:
  - Sheet name / title cells (B1:B3)
  - Year and Month header rows (E6:Q6, T6:FS6, E8:Q8, T8:FS8)
  - Provides the column-alignment for all time-series assumption cells in the sheet.
- **Notes & Customizations**:
  - Two distinct annual header bands exist (E6:Q6 and T6:FS6) — blocks use either the E–Q band or the T–FS band depending on column placement.
  - Monthly series is defined and available; some areas may use monthly columns though most assumption rows use annual columns.

---

### Dashboard Control (sheet control/title row)
- **Section Type**: Control Title / Metadata
- **Description & Purpose**: Single-row label indicating this sheet is the dashboard control center (high-level descriptor).
- **Cell Range**: A11:B11
- **Time Series Horizon**:
  - **Dates Location**: none (this is a label row)
  - **Date Range**: n/a
  - **Frequency**: n/a
- **Key Components**:
  - Label "Dashboard Control" (B11) and an indicator flag in A11.
- **Notes & Customizations**:
  - Acts as a visual/semantic separator between header and the assumptions blocks below.

---

### Support Fees - % of CAC
- **Section Type**: Key Metrics Table / Assumption block
- **Description & Purpose**: Input block for support-fee assumptions expressed as percentage of CAC and associated numeric scenarios. Likely contains scenario-level lines and multi-year values.
- **Cell Range**: A13:FS17
- **Time Series Horizon**:
  - **Dates Location**:
    - Primary (annual) columns for the left band: E6:Q6 (applies to cells in columns J:Q)
    - Primary (annual/extended) columns for the right band: T6:FS6 (applies to cells in AR:FS)
  - **Date Range**:
    - Annual headers (E6:Q6 / T6:FS6) → 2015 to 2027
  - **Frequency**: Annual (section values align to the annual header bands)
- **Key Components**:
  - Section label: "Support Fees - % of CAC" (B13)
  - Top row of numeric values: J13:Q13 (left band) and AR13:FS13 (right band)
  - Scenario value rows (scaled) below: J14:Q14 → J17:Q17 (these rows map to scenario labels in B14:B17)
- **Notes & Customizations**:
  - Several numeric rows in this block are stored with scale = 1,000 (rows J14:Q14 through J17:Q17 flagged as scale 1000).
  - Scenario labels referenced for these rows appear in the common scenario locations (see Scenario presets section).

---

### ARR Multiplier
- **Section Type**: Key Metrics Table / Assumption block
- **Description & Purpose**: Stores ARR multiplier assumptions used for valuation or KPI scaling across forecast periods; includes multiple column bands for different output ranges (left and extended right).
- **Cell Range**: A19:FS23
- **Time Series Horizon**:
  - **Dates Location**:
    - Left-band annual header: E6:Q6 (applies to E19:I19 and J19:Q19)
    - Right-band annual header: T6:FS6 (applies to T19:BA19 and BQ19:FS19 etc.)
  - **Date Range**: 2015 to 2027 (annual)
  - **Frequency**: Annual
- **Key Components**:
  - Section label: "ARR Multipler" (B19)
  - Row of short-run numeric inputs: E19:I19
  - Multi-year numeric bands: J19:Q19 (scaled 1000), T19:BA19, BB19:BO19 (scaled 1000), BP19 (scaled 1000), BQ19:FS19
  - Additional scenario rows under the block: J20:Q20, J21:Q21, J22:Q22, J23:Q23 (all scale 1000)
- **Notes & Customizations**:
  - Mixed column bands indicate values are split between a left forecast window (E–Q) and an extended forecast/window on the right (T–FS). Several blocks use mixed scaling (some bands flagged as thousands).
  - Many values in this block are in thousands (scale = 1000).

---

### Perpetuity Factor
- **Section Type**: Key Metrics Table / Assumption block
- **Description & Purpose**: Inputs for the terminal/perpetuity factor used in valuations (likely used to compute terminal value or long‑run multipliers).
- **Cell Range**: A26:FS30
- **Time Series Horizon**:
  - **Dates Location**:
    - Left-band annual header: E6:Q6 (applies to E26:Q26)
    - Right-band annual header: T6:FS6 (applies to T26:FS26)
  - **Date Range**: 2015 to 2027 (annual)
  - **Frequency**: Annual
- **Key Components**:
  - Section label: "Perpetuity Factor" (B26)
  - One-line numeric series in header bands: E26:Q26 and T26:FS26
  - Scenario numeric rows beneath (J27:Q27, J28:Q28, J29:Q29, J30:Q30 — scale 1000)
- **Notes & Customizations**:
  - Clear separation of a headline perpetual factor (single-line) and scenario-scaled rows below.
  - Scenario rows use thousand-scale notation.

---

### ARR Multiplier - Financial
- **Section Type**: Key Metrics Table / Assumption block (financial-specific)
- **Description & Purpose**: ARR multiplier inputs specifically for financial-line valuation or reporting (distinct from corporate / general ARR multipliers).
- **Cell Range**: A33:FS37
- **Time Series Horizon**:
  - **Dates Location**:
    - Left-band annual header: E6:Q6 (applies to E33:Q33 and J34:Q34..J37:Q37)
    - Right-band annual header: T6:FS6 (applies to T33:FS33)
  - **Date Range**: 2015 to 2027 (annual)
  - **Frequency**: Annual
- **Key Components**:
  - Section label: "ARR Multipler  - Financial" (B33)
  - Headline series: E33:Q33 and T33:FS33
  - Scenario numeric rows: J34:Q34, J35:Q35, J36:Q36, J37:Q37 (scale 1000)
- **Notes & Customizations**:
  - Separate banding for financial multipliers; scenario rows are in thousands.

---

### Perpetuity Factor - Financial
- **Section Type**: Key Metrics Table / Assumption block (financial terminal assumption)
- **Description & Purpose**: Terminal/perpetuity rate inputs specific to the financial view (used in financial-line terminal value calculations).
- **Cell Range**: A40:FS44
- **Time Series Horizon**:
  - **Dates Location**:
    - Left-band annual header: E6:Q6 (applies to E40:Q40)
    - Right-band annual header: T6:FS6 (applies to T40:FS40)
  - **Date Range**: 2015 to 2027 (annual)
  - **Frequency**: Annual
- **Key Components**:
  - Section label: "Perpetuity Factor - Financial" (B40)
  - Headline numeric line(s): E40:Q40 and T40:FS40
  - Scenario rows (scaled): J41:Q41, J42:Q42, J43:Q43, J44:Q44 (scale 1000)
- **Notes & Customizations**:
  - Follows same structure as the general perpetuity factor block but scoped to financial calculations.

---

### ARR Multiplier - Corporate
- **Section Type**: Key Metrics Table / Assumption block (corporate-specific)
- **Description & Purpose**: ARR multiplier inputs used for corporate-level valuation or reporting (distinct group from financial multipliers).
- **Cell Range**: A47:FS51
- **Time Series Horizon**:
  - **Dates Location**:
    - Left-band annual header: E6:Q6 (applies to E47:Q47)
    - Right-band annual header: T6:FS6 (applies to T47:FS47)
  - **Date Range**: 2015 to 2027 (annual)
  - **Frequency**: Annual
- **Key Components**:
  - Section label: "ARR Multipler - Corporate" (B47)
  - Headline series in E47:Q47 and T47:FS47
  - Scenario rows (scaled): J48:Q48, J49:Q49, J50:Q50, J51:Q51 (scale 1000)
- **Notes & Customizations**:
  - Corporate-specific multipliers separated from financial multipliers; same layout conventions.

---

### Perpetuity Factor - Corporate
- **Section Type**: Key Metrics Table / Assumption block (corporate terminal)
- **Description & Purpose**: Terminal/perpetuity factor inputs for corporate-level valuation.
- **Cell Range**: A54:FS58
- **Time Series Horizon**:
  - **Dates Location**:
    - Left-band annual header: E6:Q6 (applies to E54:Q54)
    - Right-band annual header: T6:FS6 (applies to T54:FS54)
  - **Date Range**: 2015 to 2027 (annual)
  - **Frequency**: Annual
- **Key Components**:
  - Section label: "Perpetuity Factor - Corporate" (B54)
  - Headline numeric lines: E54:Q54 and T54:FS54
  - Scenario rows (scaled): J55:Q55, J56:Q56, J57:Q57, J58:Q58 (scale 1000)
- **Notes & Customizations**:
  - Matches the pattern used for financial and general perpetuity factor blocks.

---

### % Travel Costs
- **Section Type**: Key Metrics Table / Assumption block
- **Description & Purpose**: Travel cost assumptions expressed as percentages and their mapped numeric impacts across scenarios and forecast periods.
- **Cell Range**: A61:FS65
- **Time Series Horizon**:
  - **Dates Location**:
    - Left-band annual header: E6:Q6 (applies to J61:Q61 and J62:Q62 .. J65:Q65)
    - Right-band annual header: T6:FS6 (applies to T61:FS61 and T62:BW62, T63:BW63, T64:BW64, T65:BW65)
  - **Date Range**: 2015 to 2027 (annual); some right-band columns stop at BW for mid‑block extensions but the header band extends to FS.
  - **Frequency**: Annual
- **Key Components**:
  - Section label: "% Travel Costs" (B61)
  - Headline percentage row(s): J61:Q61 (left) and T61:FS61 (right)
  - Scenario rows (scaled): J62:Q62, J63:Q63, J64:Q64, J65:Q65 (scale 1000) with corresponding right-side bands in T62:BW62, T63:BW63, T64:BW64, T65:BW65
- **Notes & Customizations**:
  - Combination of left and right bands again used; note that the right-side scenario bands are narrower (T:BW) in places while header band (T:FS) extends further.

---

### Scenario presets (repeating scenario labels mapped across blocks)
- **Section Type**: Reference / Label mapping
- **Description & Purpose**: The sheet uses a repeating set of scenario labels that are placed adjacent to each assumption block; these labels identify the row-level scenarios used across multiple blocks (e.g., Base, Growth, etc.). They are key to aligning scenario rows with numeric bands.
- **Cell Range**: B14, B15, B16, B17, B20, B21, B22, B23, B27, B28, B29, B30, B34, B35, B36, B37, B41, B42, B43, B44, B48, B49, B50, B51, B55, B56, B57, B58, B62, B63, B64, B65
  - (These are the explicit cell addresses where the preset scenario labels appear adjacent to the numeric rows in each block.)
- **Time Series Horizon**:
  - **Dates Location**: Labels are row labels (column B) and do not contain date series.
  - **Date Range**: n/a
  - **Frequency**: n/a
- **Key Components**:
  - Resolved preset strings found in the sheet (from the inverted index):
    - "Base - $25mm" (occurs at B14, B20, B27, B34, B41, B48, B55, B62)
    - "Growth - $25mm" (occurs at B15, B21, B28, B35, B42, B49, B56, B63)
    - "Base - $50mm" (occurs at B16, B22, B29, B36, B43, B50, B57, B64)
    - "Base - $50mm (R&D)" (occurs at B17, B23, B30, B37, B44, B51, B58, B65)
- **Notes & Customizations**:
  - These four scenario labels repeat directly beneath each section header row such that each block's scenario rows align to the same label set (consistent cross-block scenario mapping).
  - When extracting a scenario row for a given block, match the row (e.g., row corresponding to "Growth - $25mm" in column B) to the numeric bands in that block (J:Q left band and right-band columns).

---

Notes on numeric scaling and retrieval:
- Many numeric rows are stored with a "scale: 1000" flag in the source format. Rows in the blocks described above explicitly flagged with scale 1000 (e.g., J14:Q14..J17:Q17, J19:Q19, J20..J23 etc.). When retrieving raw values, multiply by the scale if you need absolute units.
- The sheet uses two primary column windows for time-series values:
  - Left forecast window: columns roughly E through Q (most compact annual window). Numeric bands typically appear in columns J:Q within this window.
  - Extended forecast/window: columns T through FS (extended annual or repeated bands). Numeric bands appear in several band widths here (T:BA, BB:BO, BQ:FS, AR:FS, etc.). Use the corresponding header rows (T6:FS6 or T8:FS8) to interpret these columns.
- The monthly date series (ds_3) exists (2015-01 → 2027-12) in the sheet and can be used where monthly columns are present; however most assumption values here are aligned to the annual windows.

If you want, I can produce a compact mapping table that links each block's scenario row labels (exact row numbers) to the exact numeric cell bands for that scenario (e.g., for "Growth - $25mm" show J15:Q15 and AR15:FS15), to make automated retrieval straightforward.