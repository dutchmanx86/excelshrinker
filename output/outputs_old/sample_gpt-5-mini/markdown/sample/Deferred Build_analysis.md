## 1. Spreadsheet Overview
- **Sheet Name**: Deferred Build
- **Key Sections Identified**:
  - Deferred Summary
  - Deferred Detail
  - Workbook/Header metadata (company & scenario header rows)

## 2. Detailed Section Analysis

### Deferred Summary
- **Section Type**: Key Metrics Table / Deferred Revenue Summary
- **Description & Purpose**: High-level summary of deferred revenue and ARR dynamics used to track beginning deferred balance, projected additions, projected revenue recognition, ending deferred balance and the deferred balance as a percent of ARR. This section is the summary roll‑up used for executive reporting and as the top‑level input to P&L/cash timing analyses.
- **Cell Range**: A5:DV13
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary date/period labels for the monthly time series)
  - **Date Range**: Jan 2015 to Nov 2023 (columns populated in this summary use the monthly series beginning at T -> 2015-01-31 and extend through DV -> 2023-11)
  - **Frequency**: Monthly
- **Key Components**:
  - ARR (annual recurring revenue) row
  - Deferred Beginning Balance
  - Additions (Projected)
  - Recognized as Revenue (Projected)
  - Deferred Ending Balance
  - % of ARR
  - Top header/context cells (company name and sheet title near B1:B3)
- **Notes & Customizations**:
  - Dates are driven by a monthly date series (date series id ds_1 with start_date 2015-01-31).
  - The summary contains two numeric blocks: an earlier numeric block in E:Q (historical or aggregated columns) and the monthly series block starting at T and continuing through DV; both are used in the same summary rows.
  - Several numeric rows/columns are stored with a scale of 1,000 (values in some ranges are scaled by 1000). Expect to apply the scale factor when retrieving raw numbers.

---

### Deferred Detail
- **Section Type**: Transaction / Activity Detail (Deferred Revenue Detail)
- **Description & Purpose**: Row-level detail of deferred revenue movements and the drivers behind the summary (ARR additions by source, amounts added to deferred balance, monthly recognition split by bookings vs renewals, and totals). This is the operational ledger feeding the Deferred Summary.
- **Cell Range**: A18:DV33
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2 (primary date/period labels for mapping columns to calendar months)
  - **Date Range**: Jan 2019 to Nov 2023 (the detailed numeric columns populated for this section start in BP and run through DV; BP corresponds to 2019-01 within the sheet’s monthly series and DV corresponds to 2023-11)
  - **Frequency**: Monthly
- **Key Components**:
  - ARR Added (by source)
  - Bookings / Renewals (labels present in the sheet; e.g., "Bookings" appears at B21 and B26, "Renewals" at B22 and B27)
  - Total ARR Added Previous Month
  - Added to Deferred Revenue Balance / Total Added to Deferred Revenue Balance
  - Revenue recognition rows (Bookings Revenue Recognized, Renewal Revenue Recognized, Revenue from Deferred Revenue Balance)
- **Notes & Customizations**:
  - Detailed activity columns are located in a later block of the sheet (BP:DV); these columns map to the master monthly date series starting at T.
  - Multiple ranges in this section use a 1,000x scale (apply when retrieving values).
  - The inverted index in the JSON indicates repeated string labels (e.g., "Bookings" and "Renewals") appear in multiple rows — useful for locating row positions programmatically.
  - The detail section is structured as an operational ledger intended to reconcile into the summary rows above.

---

Notes on global date mapping and scaling:
- The workbook’s primary monthly date series is defined at ds_1 with start_date = 2015-01-31 and pattern "Monthly series from 2015-01 to 2027-12". Column T maps to 2015-01 in that series; use T2:FS2 as the canonical date header range. When extracting numbers from columns that start later (e.g., BP), map the column index offset from T to compute the actual month (BP = T + 48 months → 2019-01; DV = 2023-11).
- Several numeric ranges are flagged with "scale": 1000 in the source metadata — apply this scale consistently when converting stored values to actual amounts.