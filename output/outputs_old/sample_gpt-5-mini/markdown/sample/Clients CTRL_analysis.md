## 1. Spreadsheet Overview
- **Sheet Name**: Clients CTRL
- **Key Sections Identified**:
  - Sheet Header & Time Axis (titles, scenario selector, Year/Month axes)
  - Clients Control - Financial (client ARR / churn metrics for Financial segment)
  - Clients Control - Corporate (client ARR / churn metrics for Corporate segment)
  - Clients Control - Other (client ARR / churn metrics for Other segment)

## 2. Detailed Section Analysis

### Sheet Header & Time Axis
- **Section Type**: Dashboard Header & Time Series Axis
- **Description & Purpose**: Contains the workbook title, sheet title, scenario selector, and the primary date/period axes used by the numeric tables on the sheet. This section establishes the time horizons (annual and monthly) and provides labels (Year / Month) that the client-control tables align to.
- **Cell Range**: A1:FS10
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual (primary year labels): E6:Q6 (date series ds_1)
    - Repeating-annual across monthly columns: T6:FS6 (date series ds_2)
    - Monthly labels (detailed monthly axis): T8:FS8 (date series ds_3)
    - Auxiliary numeric/label cells: E8:Q8 (numeric placeholders aligned to E6:Q6)
  - **Date Range**:
    - ds_1 (E6:Q6): Annual series from 2015 to 2027 (start 2015-01-01 to 2027 inclusive)
    - ds_2 (T6:FS6): Annual values repeating across monthly columns from 2015 to 2027 (pattern: annual values repeated 12 times per year)
    - ds_3 (T8:FS8): Monthly series from 2015-01 to 2027-12
  - **Frequency**:
    - E6:Q6 — Annual
    - T6:FS6 — Monthly columns holding repeating annual values (repeating_annual)
    - T8:FS8 — Monthly
- **Key Components**:
  - Workbook and sheet titles (B1, B2)
  - Scenario selector / scenario label (B3)
  - Primary Year header (B6) and Month header (B7)
  - Three date/period axes: annual (E6:Q6), repeating annual over monthly columns (T6:FS6), monthly (T8:FS8)
- **Notes & Customizations**:
  - The sheet uses two parallel time axes: a true annual axis (E6:Q6) and a set of monthly columns (T:FS) that either contain monthly data (ds_3) or repeat annual values (ds_2).
  - Downstream tables reference both axes; consumers must check whether a table reads E:Q (annual) or T:FS (monthly/repeated) for the intended granularity.

### Clients Control - Financial
- **Section Type**: Key Metrics Table (Client ARR & Churn by cohort)
- **Description & Purpose**: Presents ARR-related metrics and cohort breakouts for the "Financial" client segment. This block contains per-cohort measures (e.g., new booked ARR per new client), cohort size/value buckets (Base/Growth for $25mm and $50mm, R&D), and churn-related metrics. Intended for analyzing ARR generation and attrition for the Financial client cohort over time.
- **Cell Range**: A11:FS33
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual column labels: E6:Q6 (applies to the E:Q portion of this block; see header)
    - Monthly/repeating columns: T6:FS6 and T8:FS8 (applies to the T:FS portion of this block)
  - **Date Range**:
    - Annual: 2015 to 2027 (ds_1)
    - Monthly: 2015-01 to 2027-12 (ds_3)
    - Repeating annual across monthly columns: 2015 to 2027 (ds_2)
  - **Frequency**: Annual (E:Q) and Monthly (T:FS; some monthly columns hold repeating annual values)
- **Key Components**:
  - New Booked ARR per New Client (label present at B13)
  - Cohort/value buckets and scenarios (e.g., "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)" — located in column B within the block)
  - Churn metrics (e.g., "Churned ARR per Lost Client" at B20 and "% ARR Churn Attributable to Lost Clients" at B27)
  - Numeric time-series cells for the cohorts across E:Q (annual) and T:FS (monthly / repeated annual) with many numeric ranges scaled to thousands
- **Notes & Customizations**:
  - Numeric ranges within this block are scaled (many numeric cells are stored with a scale = 1000). Consumers should divide by 1,000 when interpreting raw cell values if needed.
  - The block is modular: it contains three internal subtables (new bookings, churn, % churn attributable) aligned vertically and repeated for each cohort/category.
  - Scenario label at B3 ("1 - Base - $25mm") likely indicates the active scenario for the displayed values.

### Clients Control - Corporate
- **Section Type**: Key Metrics Table (Client ARR & Churn by cohort)
- **Description & Purpose**: Same structural design as the Financial block but scoped to the "Corporate" client segment. Used to analyze ARR additions, cohort compositions (Base/Growth, $25mm/$50mm tiers), and churn behavior for Corporate clients across the same time horizons.
- **Cell Range**: A34:FS56
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual: E6:Q6 (sheet header)
    - Monthly/repeating: T6:FS6 and T8:FS8
  - **Date Range**:
    - Annual: 2015 to 2027 (ds_1)
    - Monthly: 2015-01 to 2027-12 (ds_3)
    - Repeating annual across monthly columns: 2015 to 2027 (ds_2)
  - **Frequency**: Annual (E:Q) and Monthly (T:FS; includes repeating-annual usage)
- **Key Components**:
  - New Booked ARR per New Client (label present at B36)
  - The same cohort/value bucket labels repeated (Base/Growth for $25mm and $50mm, plus R&D where applicable)
  - Churn metrics mirrored for Corporate (e.g., Churned ARR per Lost Client at B43 and % ARR Churn Attributable to Lost Clients at B50)
  - Time-series numeric values aligned to the header axes; many internal numeric ranges are scaled to thousands
- **Notes & Customizations**:
  - Structure mirrors the Financial block so extraction logic can be reused; only row offsets differ.
  - The same scaling (x1,000) is used in many numeric ranges within this block.

### Clients Control - Other
- **Section Type**: Key Metrics Table (Client ARR & Churn by cohort)
- **Description & Purpose**: Same structure again for the "Other" client segment. Captures ARR per new client, cohort breakouts (Base/Growth, tiers), and churn metrics for smaller / miscellaneous client types.
- **Cell Range**: A57:FS77
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual: E6:Q6
    - Monthly/repeating: T6:FS6 and T8:FS8
  - **Date Range**:
    - Annual: 2015 to 2027 (ds_1)
    - Monthly: 2015-01 to 2027-12 (ds_3)
    - Repeating annual across monthly columns: 2015 to 2027 (ds_2)
  - **Frequency**: Annual (E:Q) and Monthly (T:FS)
- **Key Components**:
  - New Booked ARR per New Client (label present at B59)
  - Cohort/value buckets (Base/Growth $25mm, $50mm, Base - $50mm (R&D) etc.)
  - Churn metrics (Churned ARR per Lost Client at B66; % ARR Churn Attributable to Lost Clients at B73)
  - Time-series numeric arrays (E:Q annual and T:FS monthly) with many numeric ranges scaled to thousands
- **Notes & Customizations**:
  - Final block in the sheet; numeric ranges end at row 77.
  - Same scaling and layout conventions as the other two client-control blocks; extraction code should reuse the same column logic and only vary the row offsets.

General extraction notes for an automated retriever
- Primary temporal axes live in the Sheet Header & Time Axis region: E6:Q6 (annual), T6:FS6 (repeating annual), T8:FS8 (monthly). Use these ranges to resolve column dates for the rest of the sheet.
- The three client-control logical blocks are vertically contiguous and uniform in layout:
  - Financial: A11:FS33
  - Corporate: A34:FS56
  - Other: A57:FS77
- Many numeric cells are reported with a scale = 1000 in the source; treat those values as thousands unless the cell's metadata indicates otherwise.
- Labels of interest (resolved from the sheet): "Clients Control - Financial" (B11), "Clients Control - Corporate" (B34), "Clients Control - Other" (B57), "New Booked ARR per New Client" (B13, B36, B59), "Churned ARR per Lost Client" (B20, B43, B66), "% ARR Churn Attributable to Lost Clients" (B27, B50, B73), and cohort buckets such as "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)" (appear in column B across the blocks).
- The sheet contains both annual and monthly detail; confirm which axis (E:Q vs T:FS) a given formula or cell block expects before pulling time series.