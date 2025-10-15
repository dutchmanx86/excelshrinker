## 1. Spreadsheet Overview
- **Sheet Name**: AMR
- **Key Sections Identified**:
  - Summary KPI Header and shared time-series header (A1:D2 and J2:AA2 areas)
  - Monthly Metrics Data Table (central time-series matrix spanning B2:AA25)
  - KPI Segments / Threshold Groups defined in the inverted_index: Corporate, $15k, $30k, Financial, Other

## 2. Detailed Section Analysis

### Corporate
- **Section Type**: Custom KPI Group
- **Description & Purpose**: A corporate-level KPI cluster comprising a small set of top-line indicators used for executive or consolidated reporting. The section aggregates critical corporate indicators from a few non-contiguous cells to provide a high-level view of corporate performance.
- **Cell Range**: G3:G4; H16; H21
- **Time Series Horizon**:
  - **Dates Location**: J2:AA2
  - **Date Range**: Jan'17 to Jun'18
  - **Frequency**: Monthly
- **Key Components**: Major KPI anchors and supplementaries that form the corporate view (e.g., top-line points in G3:G4 and select indicators in H16 and H21).
- **Notes & Customizations**: The data is distributed across non-contiguous cells rather than a single block, indicating a custom, composite KPI layout tailored for executive-level visibility.

### $15k
- **Section Type**: Custom KPI Group
- **Description & Purpose**: A threshold-triggered KPI subset labeled “$15k,” likely used to segment or flag performance metrics around a 15k level for closer monitoring or scenario analysis.
- **Cell Range**: H3; H5; H7; H9; G15
- **Time Series Horizon**:
  - **Dates Location**: J2:AA2
  - **Date Range**: Jan'17 to Jun'18
  - **Frequency**: Monthly
- **Key Components**: Specific KPI cells that collectively define the $15k threshold segment (e.g., H3, H5, H7, H9, and G15).
- **Notes & Customizations**: This is a non-contiguous, threshold-based KPI grouping, indicating a custom slice rather than a standard row-block metric.

### $30k
- **Section Type**: Custom KPI Group
- **Description & Purpose**: A threshold-triggered KPI subset labeled “$30k,” used to flag or compare performance around the 30k level for analytic or reporting purposes.
- **Cell Range**: H4; H6; H8; H10; G20
- **Time Series Horizon**:
  - **Dates Location**: J2:AA2
  - **Date Range**: Jan'17 to Jun'18
  - **Frequency**: Monthly
- **Key Components**: Targeted KPI cells within the $30k segment (e.g., H4, H6, H8, H10, G20).
- **Notes & Customizations**: Non-contiguous configuration; designed to support scenario/threshold comparisons rather than a single contiguous block.

### Financial
- **Section Type**: Custom KPI Group
- **Description & Purpose**: A financial KPI block capturing core financial metrics positioned to support consolidated financial analysis. This collection of cells forms the core financial view within the KPI framework.
- **Cell Range**: G5:G8; H15; H17; H20; H22
- **Time Series Horizon**:
  - **Dates Location**: J2:AA2
  - **Date Range**: Jan'17 to Jun'18
  - **Frequency**: Monthly
- **Key Components**: Central financial indicators distributed across multiple cells (e.g., G5:G8 and select cells in H15, H17, H20, H22).
- **Notes & Customizations**: Arranged as a non-contiguous KPI block, reflecting a tailored financial reporting layout rather than a simple, single-table structure.

### Other
- **Section Type**: Custom KPI Group
- **Description & Purpose**: A miscellaneous KPI cluster for supplementary metrics that do not fit into the main Corporate or Financial groups. This section aggregates auxiliary indicators used for secondary analyses.
- **Cell Range**: G9:G10; H18; H23
- **Time Series Horizon**:
  - **Dates Location**: J2:AA2
  - **Date Range**: Jan'17 to Jun'18
  - **Frequency**: Monthly
- **Key Components**: Auxiliary KPI anchors in G9:G10 and supporting indicators in H18 and H23.
- **Notes & Customizations**: Non-contiguous and supplementary by design, providing additional context without cluttering the core KPI blocks.