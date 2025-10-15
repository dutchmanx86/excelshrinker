## 1. Spreadsheet Overview
- **Sheet Name**: Retention CTRL
- **Key Sections Identified**:
  - Retention KPI Dashboard (left matrix of annual and evergreen retention metrics)
  - Retention KPI Dashboard (right matrix of additional evergreen/annual metrics)
  - Time Series Framework & Metadata (date axes, headers, and start dates used to drive the metrics)

---

## 2. Detailed Section Analysis

### Retention KPI Dashboard (Left Matrix)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Centralized matrix of retention metrics organized by annual financial retention and evergreen retention (annual equivalent). This block supports evaluating the core retention assumptions under primary base scenarios and feeding the revenue-related metrics across the period.
- **Cell Range**: I13:Q45
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6
  - **Date Range**: Annual series from 2015 to 2027
  - **Frequency**: Annual
- **Key Components**:
  - Annual Retention % - Financial
  - Evergreen Retention % - Financial (Annual Equivalent)
  - Revenue line items and associated retention metrics
  - Scaling note: several rows use a scale of 1000
  - Scenario anchors (actual dictionary values): Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)
- **Notes & Customizations**:
  - The left matrix captures the core retention signals in a contiguous left-hand block, but is tied to multiple date axes via the header row (E6:Q6) and includes several scaled numeric blocks. This reflects a custom retention dashboard rather than a standard off-the-shelf P&L.

---

### Retention KPI Dashboard (Right Matrix)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Complementary right-hand block containing evergreen/annual-equivalent retention data and additional retention segments. Provides a broader view of retention across supplementary dimensions and scenarios.
- **Cell Range**: BX13:DV45
- **Time Series Horizon**:
  - **Dates Location**:
    - ds_2 axis: T6:FS6 (annual repeating values)
    - ds_3 axis: T8:FS8 (monthly)
  - **Date Range**:
    - ds_2: Annual values repeating 12 times from 2015 to 2027
    - ds_3: Monthly series from 2015-01 to 2027-12
  - **Frequency**:
    - ds_2: Monthly (with an annual repeating pattern)
    - ds_3: Monthly
- **Key Components**:
  - Evergreen Retention % - Financial (Annual Equivalent)
  - Annual Retention % - Corporate
  - Annual Retention % - Other
  - Evergreen/Annual Equivalent blocks corresponding to the right-hand data
- **Notes & Customizations**:
  - Contains parallel retention lines aligned to the same time frame as the left matrix but organized in a separate right-hand block. Some blocks are scaled (scale: 1000) consistent with the left side, and the right block uses its own date axis to support the additional series.

---

### Time Series Definitions & Headers
- **Section Type**: Custom Data Table
- **Description & Purpose**: Defines the time-series axes that underpin the entire sheet’s metrics. Includes the primary year axis, month axis, and annual/montly patterns with start dates and descriptive patterns to aid automated retrieval and interpretation.
- **Cell Range**: E6:Q6; T6:FS6; T8:FS8
- **Time Series Horizon**:
  - **Dates Location**:
    - ds_1: E6:Q6
    - ds_2: T6:FS6
    - ds_3: T8:FS8
  - **Date Range**:
    - ds_1: Annual series from 2015 to 2027
    - ds_2: Annual values repeating 12 times from 2015 to 2027
    - ds_3: Monthly series from 2015-01-31 to 2027-12
  - **Frequency**:
    - ds_1: Annual
    - ds_2: Monthly (with annual repetition)
    - ds_3: Monthly
- **Key Components**:
  - ds_1: Annual series
  - ds_2: Repeating annual series (12 months per year)
  - ds_3: Monthly series
- **Notes & Customizations**:
  - Time-series axes are defined across three distinct header ranges, each tied to a specific date_series_id. Pattern strings describe the intended periodicity and start dates (annual 2015–2027, 12-month repeating, and monthly 2015–2027).

---

Notes for future retrieval and interpretation:
- The sheet uses a small set of time-series definitions (ds_1, ds_2, ds_3) with explicit date header ranges. These headers map to the numeric blocks in the left and right retention matrices (I13:Q45 for the left block and BX13:DV45 for the right block).
- The top of the sheet includes identifying metadata (company name, project title) and dimension labels (Year, Month) that anchor the analysis. These are part of the overall layout but are not included in a single rectangular data table; instead, they appear as header/matrix anchors around the main KPI blocks.