## 1. Spreadsheet Overview
- **Sheet Name**: FDS User Growth
- **Key Sections Identified**:
  - User Growth Overview & ARR Metrics
  - Sector & Segment Totals (WSI vs Non-WSI)
  - New Users Additions & Product Mix
  - Document Consumption & Docs Per Active User
  - FDS RT Users Metrics

## 2. Detailed Section Analysis

### User Growth Overview & ARR Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Top-level summary of customer ARR and user averages, providing a concise view of overall growth and ARR composition (Corporate, Financial, and Total) used for strategic monitoring and planning.
- **Cell Range**: A5:DC11
- **Time Series Horizon**:
  - **Dates Location**: L1:DC1
  - **Date Range**: 2020-01-01 to 2027-12-31
  - **Frequency**: Annual
- **Key Components**: Corporate ARR, Financial ARR, Total ARR; Average Corporate Users; Average Financial Users; Total Users (and related ARR blocks)
- **Notes & Customizations**: This section combines ARR-based metrics with high-level user averages (a non-standard mix for a pure P&L view). The data appears to be aligned with the sheet’s date axis defined in the date-series definitions (ds_1, ds_2, ds_3).

### Sector & Segment Totals (WSI vs Non-WSI)
- **Section Name**: WSI vs Non-WSI & Sector Totals
- **Section Type**: Sector Breakdown Data
- **Description & Purpose**: Provides segmentation of users and totals by WSI vs Non-WSI, including corporate vs financial totals and sector-level groupings. This supports understanding share and composition across organizational types and industries.
- **Cell Range**: A36:DC80
- **Time Series Horizon**:
  - **Dates Location**: C37:J37
  - **Date Range**: 2020-01-01 to 2027-12-31
  - **Frequency**: Annual
- **Key Components**: WSI; Non-WSI; Total Corporate; Total Financial; Sector categories (Professional Services, Pharma & Life Sciences, Tech, Energy & Utilities, Retail & Consumer Products, Financial - Other, and Total)
- **Notes & Customizations**: The dictionary reflects multiple sector groupings and aggregations. There are occasional misspellings in dictionary keys (e.g., “Finacial”) that may require harmonization in downstream processes.

### New Users Additions & Product Mix
- **Section Name**: New WSI Users Additions & Product Mix
- **Section Type**: KPI/Product Mix Table
- **Description & Purpose**: Tracks onboarding momentum by product for new WSI users and the distribution of new users by product category, including percentage shares. This supports product-level onboarding insights and growth attribution.
- **Cell Range**: A32:DC75
- **Time Series Horizon**:
  - **Dates Location**: C75:J75
  - **Date Range**: 2020-01-01 to 2027-12-31
  - **Frequency**: Annual
- **Key Components**: New WSI Users Additions; Percent of New Users Added by Product; New Users Added by Product; Sector-level/new-product distributions
- **Notes & Customizations**: Combines absolute additions with percentage shares. Some header labels show typographical inconsistencies in the sheet (e.g., “Consumpstion” later in the document), which may affect readability.

### Document Consumption & Docs Per Active User
- **Section Name**: Document Consumption & Docs Per Active User
- **Section Type**: Usage Metrics Table
- **Description & Purpose**: Measures document consumption and the rate of docs per active user, providing a lens on usage intensity and engagement per user.
- **Cell Range**: A216:DC221
- **Time Series Horizon**:
  - **Dates Location**: L1:DC1
  - **Date Range**: 2020-01-01 to 2027-12-31
  - **Frequency**: Monthly
- **Key Components**: Document Consumption; Docs Per Active User per Month
- **Notes & Customizations**: Monthly usage metrics are included (Docs per Active User per Month). Some header labels may include typographical issues; ensure downstream parsing accounts for any idiosyncrasies in naming.

### FDS RT Users Metrics
- **Section Name**: FDS Real-Time (RT) Users Metrics
- **Section Type**: Usage Metrics Table
- **Description & Purpose**: Details RT user metrics, including additions, totals, and active counts, as well as the share of active RT users. This supports monitoring RT adoption and utilization patterns.
- **Cell Range**: A260:DC296
- **Time Series Horizon**:
  - **Dates Location**: L1:DC1
  - **Date Range**: 2020-01-01 to 2027-12-31
  - **Frequency**: Monthly
- **Key Components**: Users Added; Total Active RT Users; Active RT Users; Percent of Active RT Users
- **Notes & Customizations**: Product-specific RT metrics are included with both granular and aggregated views. The dictionary includes a misspelling variant ("Finacial") that may need normalization in downstream references.

Additional context on the data structure and references:
- The analyzed sheet is named FDS User Growth and relies on a defined date axis (ds_1, ds_2, ds_3) to orient time-series data across several sections. The date definitions include:
  - ds_1: repeating_annual, start 2020-01-01, pattern suggests annual values through 2027
  - ds_2: annual, start 2020-01-01, through 2027
  - ds_3: monthly, start 2020-01-31, through 2027-12
- The document uses a mix of top-level ARR metrics, sector/WSI breakdowns, product mix distributions, document usage, and RT user metrics to provide a comprehensive view of user growth and usage dynamics.
- Several dictionary keys in the inverted index reflect domain labels such as "WSI," "Non-WSI," sector names (e.g., "Professional Services," "Pharma & Life Sciences," "Tech, Media & Telecom"), and usage-oriented headings (e.g., "Document Consumption," "Total Active RT Users"). Some keys contain misspellings (e.g., "Finacial"), which may warrant cleanup for consistent downstream processing.

If you want adjustments to section boundaries, alternative section names, or different cell-range consolidations (e.g., grouping non-contiguous ranges under a single section header), I can refine the mappings accordingly.