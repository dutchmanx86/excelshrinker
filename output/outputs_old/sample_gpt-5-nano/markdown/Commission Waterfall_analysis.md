## 1. Spreadsheet Overview
- **Sheet Name**: Commission Waterfall
- **Key Sections Identified**:
  - Commissions Expense Detail
  - Commissions Expense Summary
  - Financial Commission Waterfall
  - Corporate Commission Waterfall
  - Other Commission Waterfall
  - AE Commission Waterfall

Notes on structure:
- The sheet centers on a detailed breakdown of commissions and a set of monthly waterfall analyses broken out by Financial, Corporate, Other, and AE (Agent/Account Executive) components.
- Time series data are defined in two ways:
  - A monthly date series (ds_1) anchored to the header row T2:FS2, spanning 2015-01-31 through 2027-12-31.
  - A long, row-based date series (ds_2) across B29:B577, spanning 2017-01-31 through 2027-12-31, used by the waterfall sections.
- Month label anchors are defined in the dictionary as cells C26, C165, C304, and C443, providing discrete month label positions used for alignment across sections.

## 2. Detailed Section Analysis

### Commissions Expense Detail
- **Section Type**: Custom P&L
- **Description & Purpose**: Provides the granular structure and labels for commissions-related costs (e.g., Commissions Expense, Bonus Expense, Total Commission Expense) and the supporting monthly context that feeds the summary and waterfall analyses.
- **Cell Range**: B2:FS24
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01-31 to 2027-12-31
  - **Frequency**: Monthly
- **Key Components**: Core commission line items (Commissions Expense, Bonus Expense, Total Commission Expense) and the Months context used for the monthly view.
- **Notes & Customizations**: This section establishes the foundational numeric context and the monthly cadence used by downstream sections. It leverages the workbook’s standard 1000-scale presentation in the waterfall blocks, and it aligns with the “Commissions Expense Detail” header found at B2.

### Commissions Expense Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: A consolidated, KPI-style view that summarises the distribution of commissions by category (e.g., Financial, Corporate, Other bookings) and the related commission percentages and totals. It serves as the bridge between the granular detail and the waterfall analyses.
- **Cell Range**: B5:FS23
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01-31 to 2027-12-31
  - **Frequency**: Monthly
- **Key Components**: 
  - Booking categories: Financial Bookings, Corporate Bookings, Other Bookings
  - Commission percentage lines: Financial Commission %, Corporate Commission %, Other Commission %
  - Specific monthly totals: Financial Commission, Corporate Commission, Other Commission
  - Subtotals for Sales Manager Commission and related totals
- **Notes & Customizations**: This section consolidates multiple sub-categories into a single monthly view. It uses a broad range across columns (G7:Q7, AR7:FS7, etc.) to accommodate the month-by-month layout. It references the same monthly cadence defined by the ds_1 series (monthly from 2015 onward).

### Financial Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: The primary waterfall view for the Financial Commission, decomposing monthly flows into the net contributions that compose the financial commission line items. It covers a long horizon and uses a date column ds_2 for row-wise dates.
- **Cell Range**: B25:FS577
- **Time Series Horizon**:
  - **Dates Location**: B29:B577
  - **Date Range**: 2017-01-31 to 2027-12-31
  - **Frequency**: Monthly (132 periods) via an unordered date series
- **Key Components**: 
  - Financial, Corporate, and Other booking flows contributing to the Financial Commission line
  - Monthly values spread across a wide matrix (C30:FS30 through subsequent rows)
- **Notes & Customizations**: The section relies on the 132-date row set and includes many columns with scale factors (notably scale: 1000 in many ranges). It’s a dense, wide waterfall dataset designed for month-by-month visualization.

### Corporate Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: The corporate portion of the commissions waterfall, representing the same time horizon as the Financial commission waterfall but segmented to reflect corporate-specific flows and totals.
- **Cell Range**: B164:FS577
- **Time Series Horizon**:
  - **Dates Location**: B29:B577
  - **Date Range**: 2017-01-31 to 2027-12-31
  - **Frequency**: Monthly (132 periods) via ds_2
- **Key Components**: 
  - Corporate Booking lines and Corporate Commission portions
  - Monthly corporate contribution to the overall commission waterfall
- **Notes & Customizations**: Uses the same long ds_2-based date spine as the Financial Commission waterfall. Includes extensive 1000-scale normalization on values to support large financial figures.

### Other Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: The “Other” category waterfall, capturing non-core or miscellaneous commission flows over the same multi-year monthly horizon.
- **Cell Range**: B303:FS582
- **Time Series Horizon**:
  - **Dates Location**: B29:B577
  - **Date Range**: 2017-01-31 to 2027-12-31
  - **Frequency**: Monthly (132 periods) via ds_2
- **Key Components**: 
  - Other Bookings and Other Commission components
  - Monthly contributions to the overall commission structure
- **Notes & Customizations**: Aligns with the ds_2 date spine and uses 1000-scale formatting on numeric fields. Extends through row 582 to accommodate the extended dataset for this category.

### AE Commission Waterfall
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: The AE (Account Executive) commission waterfall, representing the remaining or residual commission flows attributable to AE-related activities.
- **Cell Range**: B442:FS582
- **Time Series Horizon**:
  - **Dates Location**: B29:B577
  - **Date Range**: 2017-01-31 to 2027-12-31
  - **Frequency**: Monthly (132 periods) via ds_2
- **Key Components**: 
  - AE Commission contributions and related waterfall entries
  - Sub-components aligned with monthly AE activity
- **Notes & Customizations**: Like other waterfall sections, values are scaled and presented across a wide column footprint. It uses the same monthly backbone (ds_2) and shares the same date spine.

Additional context resolved from the dataset:
- Months anchors used for alignment of the cadence are located in cells C26, C165, C304, and C443.
- The primary monthly cadence is defined as a monthly series from 2015-01-31 to 2027-12-31 (ds_1) with header dates at T2:FS2.
- The long, row-based date spine used by the waterfall sections is a 132-entry series from 2017-01-31 to 2027-12-31 (ds_2), located in B29:B577 for the date column across waterfall sections.

If you’d like, I can adapt this into a compact lookup table mapping each section to a single, precise contiguous cell range that you can use directly in an AI retrieval step, or adjust the ranges to a stricter interpretation of contiguous blocks per section.