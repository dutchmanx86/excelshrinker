## 1. Spreadsheet Overview
- **Sheet Name**: Sales Role Input
- **Key Sections Identified**:
  - Time Series Budget Grid
  - Role Headcount & Allocation by Category
  - Staffing Hierarchy, Ratios & Revenue Metrics

## 2. Detailed Section Analysis

### Time Series Budget Grid
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides the global time-series framework and budget anchors for planning. It combines a monthly time-series horizon with annual/budget labels to drive month-by-month headcount and cost projections across the sheet.
- **Cell Range**: AB5:CK57
- **Time Series Horizon**:
  - **Dates Location**: F6:DU6
  - **Date Range**: 2018-01 to 2027-12 (monthly sequence)
  - **Frequency**: Monthly
- **Key Components**: 
  - Budget anchors (2019 Budget in AB5, 2020 Budget in AD5, Budget in AL5)
  - Comprehensive monthly header row (F6:DU6) feeding the data blocks
  - Monthly numeric data cells across rows 6–57 and columns F–CK
- **Notes & Customizations**: A dynamic monthly series is defined (ds_1) with start at 2018-01-31 and a pattern described as “Monthly series from 2018-01 to 2027-12.” This section centralizes budgeting and month-by-month planning aligned to the monthly headers.

### Role Headcount & Allocation by Category
- **Section Type**: Custom P&L (Headcount Allocation Table)
- **Description & Purpose**: Captures core staffing lines and headcount allocations for key sales and corporate roles. This section aligns left-side role labels with their corresponding monthly figures and budget anchors, enabling a consolidated view of headcount-driven costs by category.
- **Cell Range**: A11:CK33
- **Time Series Horizon**:
  - **Dates Location**: F6:DU6
  - **Date Range**: 2018-01 to 2027-12 (monthly sequence)
  - **Frequency**: Monthly
- **Key Components**: 
  - Role blocks including AE Corporate, AE Financial, Account Manager, and VP Bus Dev
  - Cross-column placement indicating how headcount/expenses map across the same monthly grid used by the Time Series Grid
- **Notes & Customizations**: The section includes multiple, non-contiguous role lines (e.g., AE Corporate in A11:A12, AE Financial in A18:A19, Account Manager in A25:A26, and VP Bus Dev entries around C29 and A32:A33), consolidated here as a broad contiguous range for the section (A11:CK33). This reflects a grouped view of key staffing categories and their monthly allocations.

### Staffing Hierarchy, Ratios & Revenue Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Houses the more granular, ratio-based and ARR-oriented metrics per role. This section aggregates leadership and operational metrics (e.g., Non-Quota vs. Quota roles, Reports per VP, ARR per AM, and related manager/role ratios) to support revenue attribution and staffing productivity analysis.
- **Cell Range**: C36:CK57
- **Time Series Horizon**:
  - **Dates Location**: F6:DU6
  - **Date Range**: 2018-01 to 2027-12 (monthly sequence)
  - **Frequency**: Monthly
- **Key Components**: 
  - Non-Quota Sales Roles (Non Formula) and Non-Quota Sales Roles (Formula)
  - VP of Sales (Reports per VP) and VP of Sales (Total AE Reports)
  - Managerial ratio lines (Sales Manager, SDR Manager; SDRs per SDR)
  - ARR-focused metrics per AMs (Corporate AM, Financial AM)
  - Roles like Product Specialist Manager and Product Specialist (ARR per PS)
- **Notes & Customizations**: This section intentionally consolidates a wide set of role-level metrics and revenue-related calculations, spread across wide column ranges (e.g., AM38:CK38, BB38:CK38, AM46:CK46, etc.). It includes scale adjustments (noted as scale 1000 in several ranges) to reflect unit sizing for monthly numbers.

Date-series reference (from dictionary-like metadata):
- Date series definition (ds_1) is monthly, starting 2018-01-31, continuing to 2027-12. The primary dates for the sections above are carried in F6:DU6, representing the monthly horizon used across all sections.