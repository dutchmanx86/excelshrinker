## 1. Spreadsheet Overview
- **Sheet Name**: FDS AMR
- **Key Sections Identified**:
  - KPI Dashboard & Summary Metrics
  - Users & Engagement Metrics
  - Document Usage & Purchase Metrics
  - Document Cost & AMR Metrics
  - Time Series Data & Definitions

## 2. Detailed Section Analysis

### KPI Dashboard & Summary Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level snapshot of activity, user distribution, and core engagement metrics used for quick health checks and executive review. It captures overall counts, user mix, and initial performance indicators that feed into deeper analyses.
- **Cell Range**: A4:DC9
- **Time Series Horizon**:
  - **Dates Location**: C1:J1 (ds_1 dates), L1:DC1 (ds_2 dates), C2:J2 (ds_1 dates), L2:DC2 (ds_3 dates)
  - **Date Range**:
    - ds_1: 2020-01-01 to 2027-01-01 (Annual)
    - ds_2: 2020-01-01 to 2027-01-01 (Annual)
    - ds_3: 2020-01-31 to 2027-12-31 (Monthly)
  - **Frequency**:
    - ds_1: Annual
    - ds_2: Annual
    - ds_3: Monthly
- **Key Components**: High-level aggregates, time-series anchors, and quick-distribution metrics (e.g., percentage mix and per-period totals) that serve as a top-level summary.
- **Notes & Customizations**: This is a custom KPI/dashboard block with multiple date axes and scaled sub-blocks (e.g., certain metrics scaled by 1000). It consolidates multiple time-axes into a single overview region.

### Users & Engagement Metrics
- **Section Type**: Custom Metrics Table (Users & Engagement)
- **Description & Purpose**: Tracks the core user-related metrics that drive engagement and adoption: total users, entitlement status, trial activity, and active internal users. Serves as the inputs to behavior and adoption analyses.
- **Cell Range**: A11:DC23
- **Time Series Horizon**:
  - **Dates Location**: Integrated with the top-date headers (ds_1, ds_2, ds_3) used across the sheet; time labels anchor the user metrics across periods.
  - **Date Range**:
    - ds_1: 2020-01-01 to 2027-01-01 (Annual)
    - ds_2: 2020-01-01 to 2027-01-01 (Annual)
    - ds_3: 2020-01-31 to 2027-12-31 (Monthly)
  - **Frequency**:
    - ds_1: Annual
    - ds_2: Annual
    - ds_3: Monthly
- **Key Components**: Major user-related blocks include:
  - “Users”
  - “FDS Entitled AMR Users”
  - “Bookings per Active Trialer”
  - “Bookings per Internal User”
  - “Active Internal Users”
- **Notes & Customizations**: The section reflects tailored user-metrics alongside derived ratios and per-capita-style figures. Some blocks apply scaling (e.g., 1000x) to illustrate large values consistently.

### Document Usage & Purchase Metrics
- **Section Type**: Usage & Documents Metrics Table
- **Description & Purpose**: Analyzes document-related activity and usage by user type, including documents purchased, pages consumed, and efficiency measures (e.g., pages per document). This section aggregates volume and per-user-type metrics to assess content consumption patterns.
- **Cell Range**: A25:DC67
- **Time Series Horizon**:
  - **Dates Location**: Leveraged from the same top-date headers (ds_1, ds_2, ds_3) that anchor the broader sheet; date axes support per-period interpretation of usage metrics.
  - **Date Range**:
    - ds_1: 2020-01-01 to 2027-01-01 (Annual)
    - ds_2: 2020-01-01 to 2027-01-01 (Annual)
    - ds_3: 2020-01-31 to 2027-12-31 (Monthly)
  - **Frequency**:
    - ds_1: Annual
    - ds_2: Annual
    - ds_3: Monthly
- **Key Components**: Major sub-blocks include:
  - “Docs Purchased per User Type”
  - “Active - Unadjusted Pages Purchased”
  - “FDS AMR Consumption”
  - “FDS AMR Unadjusted Pages Purchased”
  - “Pages per Document”
  - “Docs per Trialer User”
  - “Internal Users”
  - “Docs per Internal User”
  - “Docs Read” and related minimums/limits
- **Notes & Customizations**: The section appears to be a bespoke compilation of usage and efficiency metrics, with several lines scaled (e.g., 1000x) for readability and cross-metric comparability. It also includes a hierarchy of user-type and tier-level breakdowns.

### Document Cost & AMR Metrics
- **Section Type**: Cost Analysis Table
- **Description & Purpose**: Provides the cost structure and financial metrics related to AMR and document services, including tiered costs, total costs, rollover balances, excess over minimum, adjustments, and the total adjusted AMR cost. This section represents the financial impact and reserve/adjustment logic behind AMR costs.
- **Cell Range**: A69:DC88
- **Time Series Horizon**:
  - **Dates Location**: The sheet’s global date headers anchor these metrics (ds_1, ds_2, ds_3) wherever period-based interpretation applies.
  - **Date Range**:
    - ds_1: 2020-01-01 to 2027-01-01 (Annual)
    - ds_2: 2020-01-01 to 2027-01-01 (Annual)
    - ds_3: 2020-01-31 to 2027-12-31 (Monthly)
  - **Frequency**:
    - ds_1: Annual
    - ds_2: Annual
    - ds_3: Monthly
- **Key Components**: Major cost and AMR-related blocks include:
  - “Document Cost - Tier 1/2/3/Excess”
  - “Total Document Cost”
  - “FactSet AMR Minimum”
  - “Total FactSet AMR Cost”
  - “Rollover Balance”
  - “Excess Over Minimum”
  - “Adjusted Excess”
  - “Total Adjusted FactSet AMR Cost”
- **Notes & Customizations**: This section reflects a bespoke cost model with tiered costs, rollover logic, and adjustment steps. It uses scaling on several rows to maintain readability of large figures.

### Time Series Data & Definitions
- **Section Type**: Time Series Definitions
- **Description & Purpose**: Documents the time-series definitions used across the sheet (ds_1, ds_2, ds_3), including the series type, frequency, start dates, and patterns. This provides the provenance for all period-based calculations in the workbook.
- **Cell Range**: C1:DC2 (date headers and definitions appear here; the time-series definitions are declared separately in the data structure)
- **Time Series Horizon**:
  - **Dates Location**:
    - ds_1: C1:J1 and C2:J2
    - ds_2: L1:DC1
    - ds_3: L2:DC2
  - **Date Range**:
    - ds_1: 2020-01-01 to 2027-01-01 (Annual)
    - ds_2: 2020-01-01 to 2027-01-01 (Annual)
    - ds_3: 2020-01-31 to 2027-12-31 (Monthly)
  - **Frequency**:
    - ds_1: Annual
    - ds_2: Annual
    - ds_3: Monthly
- **Key Components**: ds_1 (annual series from 2020 to 2027), ds_2 (repeating annual values from 2020 to 2027), ds_3 (monthly series from 2020-01 to 2027-12)
- **Notes & Customizations**: The definitions are explicitly provided in the data (start dates, frequency, and pattern). They drive the interpretation of all per-period metrics across the workbook.

