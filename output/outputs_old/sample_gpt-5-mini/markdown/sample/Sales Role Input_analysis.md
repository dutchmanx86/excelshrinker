## 1. Spreadsheet Overview
- **Sheet Name**: Sales Role Input
- **Key Sections Identified**:
  - Worksheet Header & Time Series (date row + budget labels)
  - AE Corporate
  - AE Financial
  - Account Manager
  - VP / Bus Dev (mid-block sales role group)
  - Non-Quota Sales Roles (Non Formula)
  - Non-Quota Sales Roles (Formula / Staffing Ratios & Aggregates)

## 2. Detailed Section Analysis

### Worksheet Header & Time Series
- **Section Type**: Worksheet Header / Date Series
- **Description & Purpose**: Contains the worksheet-level metadata and the primary date row used by all time-series numeric blocks. Also holds budget labels (e.g., "2019 Budget", "2020 Budget", "Budget") and an “UPDATED” note. This row is the canonical monthly timeline (ds_1) that other sections reference for monthly columns.
- **Cell Range**: C1:DU6
- **Time Series Horizon**:
  - **Dates Location**: F6:DU6 (master date series row)
  - **Date Range**: Jan 2018 to Dec 2027 (ds_1)
  - **Frequency**: Monthly
- **Key Components**:
  - Master monthly dates (F6:DU6)
  - Budget labels in the header (AB5 = "2019 Budget", AD5 = "2020 Budget", AL5 = "Budget")
  - Worksheet note/last updated (C1 = "UPDATED - JG - 11.18.19")
- **Notes & Customizations**:
  - The master date row extends to DU (end of ds_1). Individual sections use contiguous subsets of this row (see each section's Dates Location).

---

### AE Corporate
- **Section Type**: Custom P&L / Headcount / ARR by AE segment
- **Description & Purpose**: Monthly time-series for the "AE Corporate" sales segment. Includes the common movement rows (Beginning, Added, Lost, Ending) and multiple numeric rows (sales / ARR / headcount metrics). Used to track corporate AEs over time.
- **Cell Range**: C8:BA13
- **Time Series Horizon**:
  - **Dates Location**: F6:BA6
  - **Date Range**: Jan 2018 to Dec 2021
  - **Frequency**: Monthly
- **Key Components**:
  - Segment label (C8 = "AE Corporate")
  - Movement rows (Beginning, Added, Lost, Ending at C10:C13)
  - Monthly numeric series across F:BA for several detail rows (rows 10–13)
- **Notes & Customizations**:
  - Numeric values are supplied across two contiguous numeric range blocks (F10:AO10 and AP10:BA10 for some rows) — representing a continuous monthly series split in the sheet.
  - Several AE rows in this block are presented in thousands (scale = 1,000) for specific rows (see format map entries around rows 12–13).

---

### AE Financial
- **Section Type**: Custom P&L / Headcount (financial AE segment)
- **Description & Purpose**: Monthly time-series for the "AE Financial" segment. Tracks the same movement and monthly metrics as AE Corporate but for financial account executives.
- **Cell Range**: C15:BA20
- **Time Series Horizon**:
  - **Dates Location**: F6:BA6
  - **Date Range**: Jan 2018 to Dec 2021
  - **Frequency**: Monthly
- **Key Components**:
  - Segment label (C15 = "AE Financial")
  - Movement/value rows (rows 17–20) including monthly numeric series
- **Notes & Customizations**:
  - Some rows in this block are scaled (scale = 1,000) for reporting convenience (notably totals / ARR-style rows such as those in row 19–20).

---

### Account Manager
- **Section Type**: Role Headcount / Quota P&L
- **Description & Purpose**: Tracks the "Acct Manager" population and related monthly metrics (begin/add/lost/end and associated numeric values) for Account Managers.
- **Cell Range**: C22:BA27
- **Time Series Horizon**:
  - **Dates Location**: F6:BA6
  - **Date Range**: Jan 2018 to Dec 2021
  - **Frequency**: Monthly
- **Key Components**:
  - Section title (C22 = "Acct Manager")
  - Time-series numeric rows (F24:AO24, AP24:BA24 and other rows 25–27)
  - Movement rows (Beginning/Added/Lost/Ending present in the column C block for these rows)
- **Notes & Customizations**:
  - Certain rows in this block are scaled to thousands (scale = 1,000) — e.g., total/ARR style rows (rows 26–27).

---

### VP / Bus Dev block (mid-block sales roles)
- **Section Type**: Role Headcount / Management-level aggregates
- **Description & Purpose**: Contains VP-level or business-development related role rows (including a "VP Bus Dev" label) and associated monthly metrics (headcount, aggregates). Functions as an intermediate block between AE/AM groups and non-quota sections.
- **Cell Range**: C29:BA34
- **Time Series Horizon**:
  - **Dates Location**: F6:BA6
  - **Date Range**: Jan 2018 to Dec 2021
  - **Frequency**: Monthly
- **Key Components**:
  - VP label(s) (C29 and A32:A33 contain VP-related labels)
  - Monthly numeric rows across F:BA for rows 31–34
  - Movement rows (Beginning/Added/Lost/Ending present at C31:C34)
- **Notes & Customizations**:
  - Some managerial rows are scaled (scale = 1,000), e.g., lower-detail totals in rows 33–34.

---

### Non-Quota Sales Roles (Non Formula)
- **Section Type**: Non-Quota Role Time Series (explicit numeric inputs)
- **Description & Purpose**: Non-quota support or GTM roles listed as "Non-Quota Sales Roles (Non Formula)". These are explicit monthly numeric inputs for roles like CRO, Enablement Manager, Sales Admin, Sales Ops, GTM Strategy, and reclassified AM rows.
- **Cell Range**: C36:CK44
- **Time Series Horizon**:
  - **Dates Location**: AM6:CK6 (this block begins later in the master date series)
  - **Date Range**: Oct 2020 to Dec 2024
  - **Frequency**: Monthly
- **Key Components**:
  - Section label (C36 = "Non-Quota Sales Roles (Non Formula)")
  - Individual role rows (C38-C44 contain role names such as "CRO", "Enablement Manager", "Sales Admin", "Sales Operations Manager", "Sales Operations", "GTM Strategy", and a note row at C44)
  - Monthly numeric series for each role across AM:CK (some rows split AM:BA and BB:CK)
- **Notes & Customizations**:
  - This block starts later in the global timeline (AM column) indicating a later start of recording for these roles.
  - Many of these numeric rows are in thousands (scale = 1,000) — e.g., Sales Admin, Sales Ops and related role rows.

---

### Non-Quota Sales Roles (Formula)
- **Section Type**: Staffing Ratios / Aggregates / Formula-driven non-quota metrics
- **Description & Purpose**: Formula-driven section providing calculated aggregates and staffing ratios for non-quota groups and managers (e.g., VP of Sales reports per VP, VP of Sales totals, Sales Manager AEs per Manager, SDR ratios, PS ratios, ARR-per-AM, etc.). These rows are used for modeled headcount and capacity planning.
- **Cell Range**: C46:DD57
- **Time Series Horizon**:
  - **Dates Location**: AM6:DD6
  - **Date Range**: Oct 2020 to Jul 2026
  - **Frequency**: Monthly
- **Key Components**:
  - Section title (C46 = "Non-Quota Sales Roles (Formula)")
  - Formulas and ratio rows (C48–C57 contain labels such as "VP of Sales (Reports per VP)", "VP of Sales (Total AE Reports)", "Sales Manager (AEs per Manager)", "SDR Manager", "SDR", "VP Customer Success", "Corporate AM (ARR per AM)", "Financial AM (ARR per AM)", "Product Specialist Manager", "Product Specialist")
  - Monthly calculated outputs across AM:DD (multiple contiguous ranges) — includes a longer horizon for some aggregates (note: BB49:DD49 extends further to DD for the VP total)
- **Notes & Customizations**:
  - This area mixes AM:CK columns with some rows extending to DD (BB49:DD49) — indicating that certain aggregated projections continue beyond the AM–CK window through DD.
  - Many formula-driven rows are scaled (scale = 1,000) for readability; these typically represent ARR or headcount-derived ARR measures.
  - The split ranges (AM:BA and BB:CK and BB:DD) indicate the sheet splits series across contiguous blocks; treat AM:DD as the union for retrieval.

---

Notes about scales and retrieval:
- The sheet uses a global monthly series (F6:DU6). Individual sections use contiguous subranges of that master row; use each section's Dates Location to align months to numeric columns for retrieval.
- Several numeric rows are stored at a scale of 1,000 (format_ranges include "scale": 1000). Notable scaled groups include some AE totals, AE Financial totals, Account Manager totals, certain VP/manager totals, and many non-quota role rows. When extracting numeric values, check the cell's format metadata (scale) to convert to base units if needed.
- Text labels used in headers and section titles resolved from the sheet: "AE Corporate" (C8), "AE Financial" (C15), "Acct Manager" (C22), "Non-Quota Sales Roles (Non Formula)" (C36), "Non-Quota Sales Roles (Formula)" (C46), and individual role labels (e.g., "CRO", "Enablement Manager", etc.) are present at the positions noted above.

If you want, I can produce a compact retrieval map (start cell → end cell → date-column offsets) for programmatic extraction of each monthly series.