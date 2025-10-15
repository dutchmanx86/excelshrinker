## 1. Spreadsheet Overview
- **Sheet Name**: Renewal Base
- **Key Sections Identified**:
  - Renewal Base Data Table
  - Date Series Definitions

## 2. Detailed Section Analysis

### Renewal Base Data Table
- **Section Type**: Data Table
- **Description & Purpose**: Primary dataset housing renewal opportunities. Captures key attributes such as account type, contract value (ASV), renewal timing, segment, renewal type, and current stage. This table serves as the core source for renewal forecasting, pipeline reporting, and segmentation analysis within the Renewal Base sheet.
- **Cell Range**: A1:M1858
- **Time Series Horizon**:
  - **Dates Location**: 
    - Effective Date: C2:C1858
    - Close Date: D2:D1858
    - EOM Effective Date: F2:F1858
    - EOM Close Date: G2:G1858
  - **Date Range**:
    - ds_1 (Effective Dates): 2019-02-01 to 2023-07-01
    - ds_2 (Close Dates): 2019-02-01 to 2023-07-01
    - ds_3 (EOM Dates): 2019-02-28 to 2023-07-31
  - **Frequency**: Irregular / Unordered
- **Key Components**: 
  - Account Type (A1 header)
  - ASV (B1)
  - Dates columns: Effective Date (C1), Close Date (D1), EOM Effective Date (F1), EOM Close Date (G1)
  - Segment (E1)
  - AlphaSense Opp # (H1)
  - Renewal Type (I1)
  - Stage (J1)
  - Note (M1)
- **Notes & Customizations**:
  - This is a specialized Renewal pipeline data table rather than a traditional financial statement (e.g., P&L or Balance Sheet).
  - There is a note suggesting “Note: Update by taking the ASV tab on the Sales Worksheet,” indicating cross-sheet data coordination and a non-standard data refresh process.
  - The header set omits some typical financial dimensions and focuses on renewal-specific attributes (e.g., Segment, Renewal Type, Stage).

### Date Series Definitions
- **Section Type**: Time Series Registry (Date Series Definitions)
- **Description & Purpose**: Configuration registry for the time series used by the Renewal Base dataset. Defines the date series identifiers (ds_1, ds_2, ds_3) and their respective temporal boundaries and counts. Enables time-based analyses on the renewal data, including horizon-based filtering and trend assessment.
- **Cell Range**: C2:C1858; D2:D1858; F2:F1858; G2:G1858 (dates that underpin the date series) 
- **Time Series Horizon**:
  - **Dates Location**:
    - ds_1: C2:C1858
    - ds_2: D2:D1858
    - ds_3: F2:F1858 and G2:G1858 (EOM dates reference ds_3)
  - **Date Range**:
    - ds_1: 2019-02-01 to 2023-07-01
    - ds_2: 2019-02-01 to 2023-07-01
    - ds_3: 2019-02-28 to 2023-07-31
  - **Frequency**: Irregular / Unordered (the series are defined as unordered_column, not a uniform cadence)
- **Key Components**:
  - ds_1 (start_date: 2019-02-01, end_date: 2023-07-01, count: 393)
  - ds_2 (start_date: 2019-02-01, end_date: 2023-07-01, count: 395)
  - ds_3 (start_date: 2019-02-28, end_date: 2023-07-31, count: 39)
- **Notes & Customizations**:
  - The date series are defined as unordered columns rather than fixed-frequency time series.
  - The ds_3 series has a distinctly different start/end window and a smaller count, reflecting a separate horizon (likely end-of-month or specific cadence) used for EOM dates.

Notes on dictionary/lookup mapping (context):
- The spreadsheet includes an internal dictionary-like index (inverted_index) that maps various account-type groupings (e.g., Hedge Fund, Financial, Corporate, etc.) to extensive, non-contiguous cell ranges. This dictionary is used to locate sections of the workbook by account-type category and is referenced to support data retrieval and scoping for sections of the Renewal Base ecosystem. For retrieval, use the high-level section names (e.g., “Hedge Fund,” “Corporate,” “Private Equity,” etc.) and follow the associated ranges when drilling into the corresponding slices of the workbook. The actual ranges are dispersed across multiple non-contiguous blocks (e.g., A2, M3, A4:A5, …), rather than a single rectangular region. If you need a concrete mapping, consult the inverted_index in the data payload which lists every range per category.