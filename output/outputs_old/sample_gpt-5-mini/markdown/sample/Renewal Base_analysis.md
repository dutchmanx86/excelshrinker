## 1. Spreadsheet Overview
- **Sheet Name**: Renewal Base
- **Key Sections Identified**:
  - Header Row / Column Definitions
  - Master Data Table (Renewal records)
  - Date Fields (Effective / Close / EOM dates) — time-series context
  - Segment Key & Notes (side lookup / instructions)

---

## 2. Detailed Section Analysis

### Header Row / Column Definitions
- **Section Type**: Schema / Column Header block
- **Description & Purpose**: The top row provides the canonical column labels used by the entire sheet (field names and a short instruction). Use this row to map columns to business attributes when extracting or transforming records.
- **Cell Range**: A1:N1
- **Time Series Horizon**:
  - **Dates Location**: N/A (this is header/meta row)
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components** (high level):
  - Explicit column labels including:
    - A1 = "Account Type"
    - B1 = "ASV"
    - C1 = "Effective Date"
    - D1 = "Close Date"
    - E1 = "Segment"
    - F1 = "EOM Effective Date"
    - G1 = "EOM Close Date"
    - H1 = "AlphaSense Opp #"
    - I1 = "Renewal Type"
    - J1 = "Stage"
    - M1 = "Note: Update by taking the ASV tab on the Sales Worksheet"
  - Auxiliary columns (K,L) are present in the sheet region but not used for primary fields in the header row; N1 included for side lookup labels.
- **Notes & Customizations**:
  - The sheet includes a free-text note in M1 (instruction referencing another worksheet).
  - The header row uses the exact text shown above (e.g., "ASV", "AlphaSense Opp #") — use these labels to reliably access columns in code.

---

### Master Data Table (Renewal records)
- **Section Type**: Flat transactional dataset (per-record renewal table)
- **Description & Purpose**: The primary dataset: one record per row describing renewal-related attributes for accounts (account type, ASV numeric metric, effective/close dates, segment classification, identifiers, renewal type, stage). This is the core table for analytics and modeling (renewal forecasting, cohorting by segment, time-to-close, etc.).
- **Cell Range**: A2:N1858
  - (Includes all data rows; header row is A1:N1 and defined separately)
- **Time Series Horizon**:
  - **Dates Location**:
    - Effective Date column: C2:C1858 (date series id: ds_1)
    - Close Date column: D2:D1858 (date series id: ds_2)
    - EOM Effective Date column: F2:F1858 (date series id: ds_3)
    - EOM Close Date column: G2:G1858 (date series id: ds_3)
  - **Date Range**:
    - Effective Date (C2:C1858, ds_1): start = 2019-02-01, end = 2023-07-01
    - Close Date (D2:D1858, ds_2): start = 2019-02-01, end = 2023-07-01
    - EOM Effective / Close (F2:F1858 & G2:G1858, ds_3): start = 2019-02-28, end = 2023-07-31
    - (These are the earliest and latest dates detected in each date series definition.)
  - **Frequency**: Per-record / irregular (each row is an event/record date; the date-series definitions are unordered columns of record dates; ds_3 represents a limited set of end-of-month dates)
- **Key Components**:
  - Primary identifiers and numeric measures:
    - Account identifier fields: A ("Account Type") and H ("AlphaSense Opp #")
    - Numeric metric: B ("ASV") — stored as numeric per row
  - Categorical attributes:
    - E ("Segment") and related side-key columns (M/N) for mapping/lookup
    - I ("Renewal Type"), J ("Stage")
  - Dates for lifecycle analyses:
    - Effective and Close (both raw and EOM normalized)
- **Notes & Customizations**:
  - Dates are stored at the record level and are not aligned to a fixed reporting frequency — treat them as event timestamps (use EOM columns F/G if you require month-aligned aggregation).
  - The sheet contains 1,857 data rows (rows 2..1858) with the main numerical/ID columns concentrated in B and H respectively; many categorical labels appear in columns A, E and occasional auxiliary labels in column N.
  - The header indicates an external dependency / instruction (M1): "Note: Update by taking the ASV tab on the Sales Worksheet" — the ASV column values may come from another worksheet and could be refreshed externally.

---

### Date Fields (explicit time-series focus)
- **Section Type**: Date field group (time-stamps for each record)
- **Description & Purpose**: Consolidated description of all date columns used for time-based analyses and cohorting. These are the primary fields to drive time-windowed queries (e.g., renewals by month, time to close).
- **Cell Range**: C2:D1858, F2:G1858 (these are the exact ranges containing the dated values)
- **Time Series Horizon**:
  - **Dates Location** (repeat for clarity):
    - Effective Date: C2:C1858 (ds_1) — 2019-02-01 → 2023-07-01
    - Close Date: D2:D1858 (ds_2) — 2019-02-01 → 2023-07-01
    - EOM Effective Date: F2:F1858 (ds_3) — 2019-02-28 → 2023-07-31
    - EOM Close Date: G2:G1858 (ds_3) — 2019-02-28 → 2023-07-31
  - **Frequency**:
    - ds_1 and ds_2: record-level (unordered column of event dates)
    - ds_3: EOM-aligned series (39 unique EOM dates detected) — use for monthly aggregation aligned to month-ends
- **Key Components**:
  - Two parallel representations of event timing:
    - Raw event dates (Effective/Close)
    - Month-aligned event dates (EOM Effective / EOM Close)
  - Use EOM columns when performing time-bucketed metrics (monthly cohorts), and raw dates for precise latency calculations.
- **Notes & Customizations**:
  - The date-series definitions are labeled ds_1, ds_2, ds_3 in the extracted metadata; their resolved start/end dates are provided above — use those resolved values for any time-bound filtering.
  - ds_1 and ds_2 have similar start/end bounds; ds_3 is explicitly end-of-month aligned and has fewer unique values (suitable for monthly reporting).

---

### Segment Key & Notes (side lookup)
- **Section Type**: Lookup / instruction block (Segment Key)
- **Description & Purpose**: Side area that lists segment definitions / keys and a brief instruction. This block provides human-readable mapping and/or segment-key legend used by the main "Segment" column (E). Use this for mapping segments into groups for reporting.
- **Cell Range**: M1:N19
  - (M1 contains the ASV instruction note; M2 contains "Segement Key" label; M3..M19 and N3..N19 include segment labels and mapping entries referenced across the sheet)
- **Time Series Horizon**:
  - **Dates Location**: N/A (lookup / categorical)
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**:
  - M1 = "Note: Update by taking the ASV tab on the Sales Worksheet" (instruction)
  - M2 = "Segement Key" (label; note the sheet spelling "Segement")
  - M3..M19 and N3..N19 contain categorical/segment labels used across the main table (these are the canonical lookup entries for Segment / Account Type groupings)
- **Notes & Customizations**:
  - There is a misspelling in the label (M2 = "Segement Key"). When automating extraction, match the exact text or prefer column coordinates rather than string equality.
  - Some segment/categorical values also appear in column N in data rows (e.g., N257 = "Consulting Firm") — treat M/N together as the side lookup area and the main table might contain either the short code (E) or the expanded label (N) in different rows.
  - The inverted index in the metadata indicates many categorical values repeated across column A and other columns; the lookup block is the authoritative place for segment-key instructions.

---

Notes on navigation and data retrieval:
- Primary table to query for row-level analytics: A2:N1858. Use header labels from A1:N1 to map columns programmatically.
- For date-based aggregations use EOM columns (F2:F1858 and G2:G1858) for month-aligned buckets; use raw dates (C2:C1858 and D2:D1858) for latency/interval calculations.
- The sheet-level instruction in M1 indicates ASV values (B column) may be externally controlled — validate ASV against the Sales Worksheet if you need authoritative ASV figures.