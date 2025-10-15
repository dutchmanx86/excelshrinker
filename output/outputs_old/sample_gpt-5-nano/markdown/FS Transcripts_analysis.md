## 1. Spreadsheet Overview
- **Sheet Name**: FS Transcripts
- **Key Sections Identified**:
  - Financial
  - Corporate
  - Other
  - Broker Partner

## 2. Detailed Section Analysis

### Financial
- **Section Type**: Custom Data Table
- **Description & Purpose**: Represents a segment-specific data block used for analyzing financial metrics by category across two time-series horizons. This section aggregates value data for the Financial category in both a quarterly (ds_1) and a monthly (ds_2) context, enabling cross-temporal comparison and aggregation.
- **Cell Range**: A2:G6; A9:S14
- **Time Series Horizon**:
  - **Dates Location**: ds_1: B1:G1; ds_2: B9:S9
  - **Date Range**: ds_1: 2017-Q1 to 2018-Q2; ds_2: 2017-01 to 2018-06
  - **Frequency**: Quarterly (ds_1); Monthly (ds_2)
- **Key Components**:
  - Dual time-series blocks: a quarterly block (ds_1) and a monthly block (ds_2)
  - Row-level category grouping for the Financial data (across two blocks)
  - Data value ranges aligned to each horizon (B2:G6 for quarterly values; B10:S14 for monthly values)
  - Left-hand labels (A2:A6 in the first block and A9:A14 in the second block) that define the structure
- **Notes & Customizations**:
  - The sheet uses a two-horizon structure with different column spans (G columns for quarterly; S columns for monthly)
  - Category labels are repeated across blocks (Financial appears in multiple rows per ds_1 and ds_2)
  - This is a customized, multi-horizon data table rather than a standard single-statement report

---

### Corporate
- **Section Type**: Custom Data Table
- **Description & Purpose**: Represents the Corporate data segment within the same two-horizon framework, enabling segment-level analysis across quarterly and monthly views. It provides a focused view of corporate-related metrics alongside other segments.
- **Cell Range**: A2:G6; A9:S14
- **Time Series Horizon**:
  - **Dates Location**: ds_1: B1:G1; ds_2: B9:S9
  - **Date Range**: ds_1: 2017-Q1 to 2018-Q2; ds_2: 2017-01 to 2018-06
  - **Frequency**: Quarterly (ds_1); Monthly (ds_2)
- **Key Components**:
  - Dual horizon data blocks (ds_1 and ds_2)
  - Corporate category rows distributed across both blocks
  - Numeric data ranges corresponding to each horizon (B2:G6 and B10:S14)
  - Left-column labels (A2:A6 and A9:A14) mapping to the Corporate subset
- **Notes & Customizations**:
  - Part of the same two-horizon design as Financial, with identical structural layout but focused on Corporate data

---

### Other
- **Section Type**: Custom Data Table
- **Description & Purpose**: Encapsulates the “Other” data segment within the two-horizon structure, allowing cross-period comparison for miscellaneous metrics outside the primary Corporate/Financial categories.
- **Cell Range**: A2:G6; A9:S14
- **Time Series Horizon**:
  - **Dates Location**: ds_1: B1:G1; ds_2: B9:S9
  - **Date Range**: ds_1: 2017-Q1 to 2018-Q2; ds_2: 2017-01 to 2018-06
  - **Frequency**: Quarterly (ds_1); Monthly (ds_2)
- **Key Components**:
  - Two-horizon blocks with dedicated data ranges
  - “Other” category rows in both blocks
  - Data values aligned to each horizon (quarterly: B2:G6; monthly: B10:S14)
- **Notes & Customizations**:
  - Maintains consistency with the overall two-horizon layout; used for non-core categories

---

### Broker Partner
- **Section Type**: Custom Data Table
- **Description & Purpose**: Contains data related to Broker Partner interactions or metrics, organized across quarterly and monthly contexts to support partner-facing analysis and reconciliation.
- **Cell Range**: A2:G6; A9:S14
- **Time Series Horizon**:
  - **Dates Location**: ds_1: B1:G1; ds_2: B9:S9
  - **Date Range**: ds_1: 2017-Q1 to 2018-Q2; ds_2: 2017-01 to 2018-06
  - **Frequency**: Quarterly (ds_1); Monthly (ds_2)
- **Key Components**:
  - Two-horizon blocks for the Broker Partner data
  - Identifying rows for the Broker Partner subset in both blocks
  - Numeric data spans: quarterly (B2:G6) and monthly (B10:S14)
- **Notes & Customizations**:
  - Aligned with the same structural design as the other sections; dedicated to Broker Partner metrics

---

Notes:
- The sheet uses two parallel time-series blocks:
  - ds_1 (quarterly): B1:G1 for dates; B2:G6 and related ranges for values
  - ds_2 (monthly): B9:S9 for dates; B10:S14 for values
- Left-column labels that define section context appear in A2:A6 and A9:A14, mapped via the inverted_index keys: Financial, Corporate, Other, and Broker Partner.