## 1. Spreadsheet Overview
- **Sheet Name**: Clients CTRL
- **Key Sections Identified**:
  - Clients Control - Financial
  - Clients Control - Corporate
  - Clients Control - Other

## 2. Detailed Section Analysis

### Clients Control - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Consolidates ARR-related projections and performance metrics for the financial planning view. Captures scenario-based ARR levels (base and growth) and churn dynamics to support planning of new bookings, retention, and churn impacts.
- **Cell Range**: A11:Q31
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 and T6:FS6 (header date rows for respective series); additional monthly axis appears in T8:FS8
  - **Date Range**:
    - ds_1 (annual): 2015-01-01 through 2027-01-01
    - ds_2 (annual repeating): 2015-01-01 through 2027-01-01
    - ds_3 (monthly): 2015-01-31 through 2027-12
  - **Frequency**: Annual (ds_1, ds_2); Monthly (ds_3)
- **Key Components**:
  - New Booked ARR per New Client
  - Base - $25mm
  - Growth - $25mm
  - Base - $50mm
  - Base - $50mm (R&D)
  - Churned ARR per Lost Client
  - % ARR Churn Attributable to Lost Clients
- **Notes & Customizations**:
  - The section spans multiple scenario blocks with several “x” anchors and thousands-scale formatting (scale 1000 in many blocks).
  - Uses multiple date-series headers to support both annual and monthly views.
  - This is a multi-scenario ARR planning surface rather than a traditional income statement format.

### Clients Control - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Corporate-level ARR contributions and related metrics, aggregating performance across corporate-focused segments and sub-categories to inform the corporate-strategy view of ARR impact.
- **Cell Range**: A34:Q47
- **Time Series Horizon**:
  - **Dates Location**: E36:Q36 and T36:FS36 (primary headers for the corporate portion); additional headers appear in E43:Q43, T43:FS43; and later blocks (E50:Q50, E59:Q59, E66:Q66, E73:Q73) indicating continued date-series usage across the section
  - **Date Range**:
    - ds_1 (annual): 2015-01-01 through 2027-01-01
    - ds_2 (annual repeating): 2015-01-01 through 2027-01-01
    - ds_3 (monthly): 2015-01-31 through 2027-12
  - **Frequency**: Annual (ds_1, ds_2); Monthly (ds_3)
- **Key Components**:
  - Corporate sub-blocks and metrics (standalone corporate performance lines within the section)
  - Consolidated corporate ARR contributions by sub-category
- **Notes & Customizations**:
  - The corporate subsection shares the same three time-series structure as the Financial section but focuses on corporate-oriented lines.
  - Uses scale adjustments (e.g., scale: 1000) in several ranges to represent thousands.
  - Anchors and headers (e.g., rows with "x") delineate sub-blocks within Corporate.

### Clients Control - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Captures additional ARR-related metrics outside the Financial and Corporate areas, representing the residual or miscellaneous ARR contributions and related figures.
- **Cell Range**: A57:Q77
- **Time Series Horizon**:
  - **Dates Location**: E59:Q59; E66:Q66; E73:Q73 (primary headers within this section); monthly headers exist in I60:Q60, I61:Q61, I62:Q62, I63:Q63, I74:Q74, I75:Q75, I76:Q76, I77:Q77
  - **Date Range**:
    - ds_1 (annual): 2015-01-01 through 2027-01-01
    - ds_2 (annual repeating): 2015-01-01 through 2027-01-01
    - ds_3 (monthly): 2015-01-31 through 2027-12
  - **Frequency**: Annual (ds_1, ds_2); Monthly (ds_3)
- **Key Components**:
  - Other (miscellaneous) ARR lines and metrics that supplement the main Financial and Corporate sections
- **Notes & Customizations**:
  - Contains additional blocks and anchors (e.g., rows around A59, A66, A73) to delineate the “Other” portion.
  - Scaled data (scale: 1000) appears in several ranges to present thousands.
  - The section relies on the same global date-series definitions as the other sections, enabling consistent cross-section comparison.

Notes on date-time and structure used across all sections:
- The workbook defines three date-series definitions:
  - ds_1: annual, start 2015-01-01, pattern “Annual series from 2015 to 2027”
  - ds_2: repeating annual, start 2015-01-01, pattern “Annual values repeating 12 times from 2015 to 2027”
  - ds_3: monthly, start 2015-01-31, pattern “Monthly series from 2015-01 to 2027-12”
- Primary date headers appear in E6:Q6 (ds_1) and T6:FS6 (ds_2); monthly headers appear in T8:FS8 (ds_3). This structure is used across the Financial, Corporate, and Other sections to enable multi-granularity time-series analysis.
- The sheet uses several anchor rows (e.g., A11, A34, A57) to denote section boundaries and to organize the data into three major blocks corresponding to Financial, Corporate, and Other, each containing multiple scenario-based sub-blocks (e.g., Base, Growth, New Booked ARR, Churn metrics).

If you’d like, I can provide a compact retrieval map that lists exact section KPIs and their corresponding sub-ranges within each cell range, or generate a quick lookup dictionary linking section names to their precise cell bounds.