## 1. Spreadsheet Overview
- **Sheet Name**: Retention CTRL
- **Key Sections Identified**:
  - Header / Title Block
  - Time Axis / Date Headers
  - Revenue header & summary
  - Annual Retention % - Financial (with scenario-level amounts)
  - Evergreen Retention % - Financial (Annual Equivalent)
  - Annual Retention % - Corporate (with scenario-level amounts)
  - Annual Retention % - Other (with scenario-level amounts)
  - Evergreen Retention % - Other (Annual Equivalent)
  - Scenario labels (repeated across retention blocks; e.g., "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)")

## 2. Detailed Section Analysis

### Header / Title Block
- **Section Type**: Metadata / Worksheet Title
- **Description & Purpose**: Contains company name and the sheet title and the selected model/scenario name. Used to identify the workbook context and active scenario.
- **Cell Range**: B1:B3
- **Time Series Horizon**:
  - **Dates Location**: (none — this is a header block)
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**:
  - Company name ("AlphaSense, Inc.")
  - Sheet title ("Retention CTRL")
  - Scenario title / selector ("1 - Base - $25mm")
- **Notes & Customizations**: Simple header; no numeric time series here.

### Time Axis / Date Headers
- **Section Type**: Date / Period Axis
- **Description & Purpose**: Primary horizontal time axis(s) used by the retention and revenue tables. The sheet contains multiple date series layouts: an annual series, a repeating-annual series (aligned to a wider column range), and a monthly series.
- **Cell Range**: E6:FS8
- **Time Series Horizon**:
  - **Dates Location**:
    - E6:Q6 — annual date series (date_series_id = ds_1)
    - T6:DV6 — repeating annual date series (date_series_id = ds_2)
    - T8:FS8 — monthly date series (date_series_id = ds_3)
  - **Date Range**:
    - ds_1 (E6:Q6): Annual series from 2015 to 2027 (start_date = 2015-01-01)
    - ds_2 (T6:DV6): Annual values repeating across columns from 2015 to 2027 (start_date = 2015-01-01)
    - ds_3 (T8:FS8): Monthly series from 2015-01 to 2027-12 (start_date = 2015-01-31)
  - **Frequency**:
    - E6:Q6 — Annual
    - T6:DV6 — Annual (repeating across a wider column set)
    - T8:FS8 — Monthly
- **Key Components**:
  - Row of Year labels (E6:Q6 and T6:DV6)
  - Row(s) for Month / monthly labels (B7 and T7:DV7 and the monthly series row T8:FS8)
- **Notes & Customizations**: Multiple parallel date series are present (annual and monthly) — callers must choose the appropriate date row depending on which column block (E:Q vs T:DV vs T:FS) a data section uses.

### Revenue header & summary
- **Section Type**: Header / Summary row for Revenue
- **Description & Purpose**: Top-level revenue label and nearby summary cells. Serves as the anchor label for the revenue area above/beside retention tables.
- **Cell Range**: A10:N11
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 and T6:DV6 (time series used by adjacent numeric cells)
  - **Date Range**: Annual 2015 → 2027 (ds_1 / ds_2); monthly axis available (ds_3) if needed
  - **Frequency**: Annual (primary)
- **Key Components**:
  - "Revenue" label (B11)
  - Nearby numeric summary row (J10:N10) that appears to provide a compact revenue summary or header totals
- **Notes & Customizations**: This is not the full revenue time series table; it is the label and a small summary band. Full scenario-level amounts are present in the retention blocks below.

### Annual Retention % - Financial
- **Section Type**: Key Metrics Table (Retention rates + scenario-level amounts)
- **Description & Purpose**: Captures the "Annual Retention % - Financial" headline and the scenario-level numeric rows beneath it (scenario labels and monetary amounts). Used to drive financial retention modeling for the "Financial" customer category across scenarios.
- **Cell Range**: B13:DV17
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual columns: E6:Q6 (ds_1)
    - Repeating / extended annual columns: T6:DV6 (ds_2)
  - **Date Range**: 2015 → 2027 (annual coverage from ds_1 and ds_2)
  - **Frequency**: Annual
- **Key Components**:
  - Headline retention row (label at B13)
  - Scenario label rows (column B rows 14–17 contain scenario names such as "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)")
  - Scenario numeric rows (amount rows scaled by 1,000 in I14:Q14 through I17:Q17 and extended columns in BX13:DV13 where present)
- **Notes & Customizations**:
  - Several numeric cells for the headline row appear both in the near-term block (I13:Q13) and in a far-right block (BX13:DV13) — the retention headline and scenario amounts are split across the sheet's column blocks.
  - Numeric scenario rows are stored in thousands (scale = 1000) for rows 14–17.

### Evergreen Retention % - Financial (Annual Equivalent)
- **Section Type**: Key Metrics Table (Evergreen retention converted to annual equivalents)
- **Description & Purpose**: Stores evergreen retention expressed as annual-equivalent retention rates and the associated scenario monetary values. This supports modeling of ongoing subscription renewals for the Financial segment.
- **Cell Range**: B20:DV24
- **Time Series Horizon**:
  - **Dates Location**:
    - Annual columns: E6:Q6 (ds_1)
    - Extended columns: T6:DV6 (ds_2)
  - **Date Range**: 2015 → 2027
  - **Frequency**: Annual (annual-equivalent values)
- **Key Components**:
  - Headline evergreen retention row (B20)
  - Scenario label rows (B21:B24 with matching scenario names)
  - Numeric anniversary / amount rows (I21:Q21 through I24:Q24; extended blocks BX20:DV20 for headline and BX??:DV?? for other values where present)
- **Notes & Customizations**:
  - Headline values appear in both near and far column blocks (I20:Q20 and BX20:DV20).
  - Scenario numeric rows use a 1,000 scale.

### Annual Retention % - Corporate
- **Section Type**: Key Metrics Table (Retention rates + scenario-level amounts for Corporate segment)
- **Description & Purpose**: Annual retention rates and scenario monetary figures for the Corporate customer segment; used to model retention impacts on corporate ARR.
- **Cell Range**: B27:DV31
- **Time Series Horizon**:
  - **Dates Location**:
    - Near-term annual axis: E6:Q6 (ds_1)
    - Extended annual axis (aligns to these rows' right-side values): T6:DV6 (ds_2)
  - **Date Range**: 2015 → 2027
  - **Frequency**: Annual
- **Key Components**:
  - Headline annual retention row (B27)
  - Scenario labels (B28:B31)
  - Scenario numeric rows (I28:Q28 through I31:Q31 scaled by 1,000; additional values appear across T27:DV27 for extended columns)
- **Notes & Customizations**:
  - This block uses both the I:Q column block and the T:DV extended block for time series values (T27:DV27 contains extended annual values).

### Annual Retention % - Other
- **Section Type**: Key Metrics Table (Retention rates + amounts for Other segment)
- **Description & Purpose**: Annual retention rates and scenario monetary figures for the "Other" customer segment.
- **Cell Range**: B34:DV38
- **Time Series Horizon**:
  - **Dates Location**:
    - E6:Q6 (ds_1) for near columns
    - T6:DV6 (ds_2) for extended columns (T34:DV34 specifically referenced)
  - **Date Range**: 2015 → 2027
  - **Frequency**: Annual
- **Key Components**:
  - Headline row (B34)
  - Scenario label rows (B35:B38)
  - Numeric scenario rows (I35:Q35 through I38:Q38 scaled by 1,000; extended values across T34:DV34)
- **Notes & Customizations**:
  - Like other blocks, the "Other" section spans both near and extended column blocks to cover the full modeled horizon.

### Evergreen Retention % - Other (Annual Equivalent)
- **Section Type**: Key Metrics Table (Evergreen retention Annual Equivalent for Other segment)
- **Description & Purpose**: Evergreen retention for the "Other" segment expressed on an annual equivalent basis, with scenario-level monetary values.
- **Cell Range**: B41:DV45
- **Time Series Horizon**:
  - **Dates Location**:
    - Near annual axis: E6:Q6 (ds_1)
    - Extended axis: T6:DV6 (ds_2)
  - **Date Range**: 2015 → 2027
  - **Frequency**: Annual (annual-equivalent)
- **Key Components**:
  - Headline evergreen retention row (B41)
  - Scenario label rows (B42:B45)
  - Numeric scenario rows (I42:Q42 through I45:Q45 scaled by 1,000; BX41:DV41 includes headline/extended values)
- **Notes & Customizations**:
  - Headline and some values are duplicated across the near and far-right column blocks (I41:Q41 and BX41:DV41).
  - Scenario numeric rows use the 1,000 scaling convention.

Notes on Scenario Labels (resolved)
- Scenario labels appear repeatedly in column B across the scenario rows for each retention block. The dataset explicitly contains the strings:
  - "Base - $25mm"
  - "Growth - $25mm"
  - "Base - $50mm"
  - "Base - $50mm (R&D)"
  These appear in cells B14,B15,B16,B17 and repeated in analogous rows within each retention block.

General Notes & Customizations
- Several numeric rows are stored with a scale factor of 1,000 (indicated in the format metadata). Callers should divide by 1,000 when extracting full-dollar values for those rows.
- The sheet uses multiple parallel date axes. Match extraction columns to the appropriate date header row:
  - Use E6:Q6 for the compact near-term annual block (ds_1).
  - Use T6:DV6 for the extended annual block (ds_2).
  - Use T8:FS8 for monthly granularity (ds_3) where present.
- Many headline rows have two numeric blocks (near-term I:Q and far-right BX:DV). Retrieve both blocks to assemble the full horizon.