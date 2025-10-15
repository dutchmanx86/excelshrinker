## 1. Spreadsheet Overview
- **Sheet Name**: Clients
- **Key Sections Identified**:
  - Header / Metadata (company name, view selection, master date row)
  - Clients Summary
  - Clients Detail - Financial
  - Client Detail - Corporate
  - Client Detail - Other

## 2. Detailed Section Analysis

### Header / Metadata
- **Section Type**: Document Header / Metadata (includes master date row)
- **Description & Purpose**: Contains the workbook title, sheet title and scenario/view descriptor plus the primary date row used by all time-series tables on the sheet. Serves as the sheet-level metadata and the canonical monthly date series for downstream retrieval and alignment.
- **Cell Range**: A1:FR3
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2 (master monthly date row)
  - **Date Range**: 2015-01-31 (Jan 2015) through 2027-12-31 (Dec 2027) — monthly series
  - **Frequency**: Monthly
- **Key Components**:
  - Company name / sheet title (A1:A3)
  - Scenario / view label (A3)
  - Master monthly date series (S2:FR2)
- **Notes & Customizations**:
  - Date series is defined as ds_1: monthly increments starting 2015-01-31 (pattern covers Jan 2015 → Dec 2027).
  - Numeric summary columns exist to the left of the monthly series (D:P) — see other sections for usage.

---

### Clients Summary
- **Section Type**: Key Metrics Table (Client counts & aggregate ARR summary)
- **Description & Purpose**: High-level summary of client population and churn/bookings aggregates. Intended to give a snapshot of counts (beginning, added, ending), churn totals and higher-level ARR metrics across summary columns and the monthly time series.
- **Cell Range**: A5:FR10
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2 (primary monthly labels) — numeric monthly values populate S7:FR9 within this block
  - **Date Range**: Jan 2015 to Dec 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Client counts (Beginning Clients, New Added, Ending Clients)
  - Churn indicator row(s) (Churned)
  - Aggregated numeric columns to the left (D7:P7 etc.) used for non-monthly summary buckets
  - Monthly series values in S7:FR9 for time-series tracking
- **Notes & Customizations**:
  - The section mixes summary buckets (columns D:P) with a long monthly series (S:FR).
  - Monetary-like columns in the block often use a 1,000 scale in the mid/right columns (see Notes section per sheet).

---

### Clients Detail - Financial
- **Section Type**: Time Series Financial Detail (Client-level ARR & bookings)
- **Description & Purpose**: Detailed financial-oriented client metrics for the "Financial" segment. Tracks new bookings, ARR by new/lost clients, per-client averages, and churn attribution — available both in summary buckets and across the monthly date series for trend analysis.
- **Cell Range**: A12:FR29
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2 (primary monthly labels). Numeric time-series cells for this section occupy S14:FR29.
  - **Date Range**: Jan 2015 to Dec 2027
  - **Frequency**: Monthly
- **Key Components**:
  - New bookings metrics (e.g., New Booked ARR - New Clients, New Booked ARR per New Client)
  - Churned ARR metrics (Churned ARR - Lost Clients, Total Churned ARR, Churned ARR Attributable to Lost Clients, % of Churned ARR Attributable to Lost Clients)
  - Count rows (Clients Added, Clients Lost)
  - Left-side summary columns (D14:P19 etc.) and monthly series (S14:FR29)
- **Notes & Customizations**:
  - Numeric layout pattern: the first numeric column in many rows (column D) is an unscaled count/metric; subsequent arrays (E:P and T:FR) frequently use a scale factor of 1,000 for monetary values. Treat D and S columns as raw counts/values while E:P and T:FR are typically scaled thousands.
  - This is a custom client-focused financial detail table (not a standard P&L or balance sheet).

---

### Client Detail - Corporate
- **Section Type**: Time Series Financial Detail (Corporate segment)
- **Description & Purpose**: Segment-level detail for the Corporate client group mirroring the Financial detail layout. Tracks client counts, new bookings and churn metrics for the Corporate segment across summary buckets and monthly series.
- **Cell Range**: A31:FR48
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2 (primary monthly labels). Numeric time-series cells for this section occupy S33:FR48.
  - **Date Range**: Jan 2015 to Dec 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Same major metric families as Financial section: client counts, new bookings/ARR per client, churned ARR and per-client churn metrics
  - Summary columns to the left (D33:P39 etc.) and detailed monthly columns (S33:FR48)
- **Notes & Customizations**:
  - Follows the same scaling convention (D and S often raw; E:P and T:FR typically scaled by 1,000 for monetary fields).
  - Structured to allow per-segment roll-ups into the overall Clients Summary.

---

### Client Detail - Other
- **Section Type**: Time Series Financial Detail (Other segment)
- **Description & Purpose**: Segment-level detail for "Other" clients. Same purpose and structure as the Corporate and Financial sections, supporting granular tracking of bookings and churn for non-core segments.
- **Cell Range**: A50:FR67
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2 (primary monthly labels). Numeric time-series cells for this section occupy S52:FR67.
  - **Date Range**: Jan 2015 to Dec 2027
  - **Frequency**: Monthly
- **Key Components**:
  - Client counts, new booked ARR, churned ARR, per-client averages, totals and attribution percentages
  - Left-side summary buckets (D52:P58 etc.) and monthly detail (S52:FR67)
- **Notes & Customizations**:
  - Same scaling/format pattern as other detail sections (monetary columns frequently scaled by 1,000).
  - Designed to be consistent with the Financial and Corporate blocks to enable combined aggregation.

General Notes (sheet-wide)
- Primary monthly date headers: S2:FR2 (ds_1) — monthly from Jan 2015 to Dec 2027.
- Numeric layout pattern: two numeric block types per section:
  - Left summary block: columns D:P (summary buckets / snapshot metrics).
  - Long monthly block: columns S:FR (monthly time series).
- Monetary amounts commonly use a scale of 1,000 in mid and right arrays (E:P and T:FR); first numeric columns in each row (D and S) are often raw counts or unscaled values — account for these when extracting monetary vs. count metrics.
- Repeating label families across sections include: client counts (beginning/added/ending), churn metrics, new booked ARR (total and per-client), and churn attribution percentages. These are the key primitives for retrieval and aggregation.