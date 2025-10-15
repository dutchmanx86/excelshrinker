## 1. Spreadsheet Overview
- **Sheet Name**: Product User Splits
- **Key Sections Identified**:
  - Product User Splits Data Matrix (Source-by-Source Monthly Values)
  - Time Series Date Headers and Axis Definition
  - Source Header Labels (Lexis Nexis, DJ, FactSet Transcripts, Transcripts, BRM, AMR, and FactSet AMR subcategories)

## 2. Detailed Section Analysis

### Lexis Nexis Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: The Lexis Nexis portion represents one primary data source's monthly values (by month) within the overall Product User Splits matrix. It forms the headered data region used to compute source-level contributions over time.
- **Section Range**: C4:AS117; AU4:BO117
  - Note: The Lexis Nexis data for each row is stored in two column blocks (C4:ASn and AU4:BO n) across most rows, creating a composite range. The combined ranges above cover the full Lexis Nexis data region across rows 4 through the final data row.
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Lexis Nexis label (A3), the paired date headers (C1:AS1 and AU1:BO1), and the monthly numeric blocks aligned under those headers.
- **Notes & Customizations**: This section uses multiple numeric blocks per row (e.g., C4:AS4 and AU4:BO4; later rows follow the same pattern). Many numeric cells include thousand-scale adjustments (scale: 1000) in related blocks. The data is a time-series matrix segmented by source, with a two-block per-row layout.

### DJ Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: The DJ block represents another data source within the same Product User Splits matrix, contributing its own monthly values to the overall totals.
- **Section Range**: C4:AS117; AU4:BO117
  - Note: Similar two-block per row structure as Lexis Nexis (for most rows), enabling consistent monthly series capture.
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: DJ header context appears in the section, aligned with the same date axes as Lexis Nexis.
- **Notes & Customizations**: Follows the same structural design as Lexis Nexis, including potential thousand-multipliers for numeric values.

### FactSet Transcripts Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: Captures monthly values for the FactSet Transcripts source within the dataset.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: FactSet Transcripts header, date axes, and the recurring two-block-per-row numeric layout.
- **Notes & Customizations**: Consistent with other source blocks; numeric cells may include scale factors (1000) in several rows.

### TR Transcripts Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: Represents the Transcripts-related data from the TR domain, integrated into the Product User Splits matrix.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: TR Transcripts label, time-series axis, two-block data layout.
- **Notes & Customizations**: Aligned with other source blocks in structure and scaling.

### Transcripts Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: Another source-specific block within the dataset, representing general transcripts data across months.
- **Section Range**: C4:BO117 (composite across the row blocks used in this section; includes two primary numeric blocks per row)
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Transcripts header, monthly axes, and per-row numeric blocks (two blocks in many rows).
- **Notes & Customizations**: Part of a larger grid that uses a consistent monthly cadence with standard thousand-scaling in many cells.

### TR Filings Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: Captures TR Filings related values within the data matrix.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: TR Filings label and date axes; standard two-block per-row data layout.
- **Notes & Customizations**: Part of the shared data-grid design; may include 1000-scale multipliers.

### TR BRM Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: TR BRM section aggregates BRM-related metrics under the TR domain.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: TR BRM label, time-series headers, multi-block per-row data layout.
- **Notes & Customizations**: Consistent with the method used for other source blocks; some values are scaled (1000).

### AMR ($15k) Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: AMR category with a nominal $15k marker, part of the AMR family in the dataset.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: AMR label (AMR ($15k)), standard date axes, two-block per-row data structure.
- **Notes & Customizations**: Part of a repeated grid pattern across sections; appears with occasional thousand-scaling in numeric cells.

### AMR ($30k) Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: AMR category with a nominal $30k marker, another tier within the AMR family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: AMR ($30k) header, standard date axis.
- **Notes & Customizations**: Similar structure and scaling as other AMR blocks.

### AMR Data Block (General AMR)
- **Section Type**: Source Data Table
- **Description & Purpose**: Core AMR data region without a specific dollar-marker annotation, within the AMR family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: AMR label, time-axis, multi-block per-row data.
- **Notes & Customizations**: Uniform across AMR variants; many cells carry scale 1000.

### BRM - Global Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: BRM Global data slice under the broader BRM family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: BRM Global header, time series axis, standard two-block layout (and occasional additional blocks).
- **Notes & Customizations**: Part of the BRM family with typical thousand-scaling in numeric cells.

### BRM - Single Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: BRM Single data slice, another BRM subtype represented in the same matrix.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: BRM Single header and time-axis; two-block per-row data flow.
- **Notes & Customizations**: Mirrors the BRM Global structure with same scaling conventions.

### FactSet RT Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: FactSet RT portion, a distinct data source within the broader Product User Splits grid.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: FactSet RT label, date axis alignment, multi-block per-row data.
- **Notes & Customizations**: Consistent with the two-block per-row design and scaling patterns.

### FactSet AMR Data Block (Active)
- **Section Type**: Source Data Table
- **Description & Purpose**: Active AMR data branch within FactSet AMR family (AMR Active domain).
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: AMR Active labeling, time-axis, standard two-block per-row data.
- **Notes & Customizations**: Part of the broader AMR family with typical scaling.

### FactSet AMR Data Block (Trailers)
- **Section Type**: Source Data Table
- **Description & Purpose**: AMR Trailers within the FactSet AMR family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Trailers labeling, date series, two-block per-row grid.
- **Notes & Customizations**: Standard AMR sub-block pattern with scaling.

### FactSet AMR Data Block (Internal)
- **Section Type**: Source Data Table
- **Description & Purpose**: AMR Internal section within the FactSet AMR family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Internal label, date axis, two-block per-row layout.
- **Notes & Customizations**: Aligned with other AMR blocks; scaling patterns apply.

### FactSet AMR Active Docs Purchased Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: AMR Active Docs Purchased, a specific metric within the AMR family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Active Docs Purchased label, time axis, two-block per-row data.
- **Notes & Customizations**: Consistent with FactSet AMR sub-blocks; scaling may apply.

### FactSet AMR Trialer Docs Purchased Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: AMR Trialer Docs Purchased data within the AMR family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Trialer Docs Purchased label, axis, and two-block grid.
- **Notes & Customizations**: Part of the AMR family; standard scaling rules apply.

### FactSet AMR Internal Docs Purchased Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: AMR Internal Docs Purchased (internal custody) block within FactSet AMR.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Internal Docs Purchased label, date axis, two-block per-row grid.
- **Notes & Customizations**: Consistent with other AMR blocks; thousand-scaling applies.

### FactSet AMR Summary / Active
- **Section Type**: Source Data Table
- **Description & Purpose**: High-level AMR metrics aggregating active items across the AMR family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: AMR aggregate header, time axis, two-block per-row data.
- **Notes & Customizations**: Central AMR aggregation; standard scaling.

### FactSet AMR Summary / Trailers
- **Section Type**: Source Data Table
- **Description & Purpose**: Aggregate metrics for AMR Trailers subset within the AMR family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Trailers summary, date axis, two-block per-row data.
- **Notes & Customizations**: Part of the AMR family mode; scaling rules apply.

### FactSet AMR Summary / Internal
- **Section Type**: Source Data Table
- **Description & Purpose**: Aggregate metrics for AMR Internal subset within the AMR family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Internal metrics summary, time axis, two-block per-row data.
- **Notes & Customizations**: Alignment with other AMR blocks; scaling patterns apply.

### FactSet AMR Active Docs Purchased Data Block (All AMR Active Docs Purchased)
- **Section Type**: Source Data Table
- **Description & Purpose**: Active Docs Purchased indicator within AMR, consolidated under IFAMR.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Active Docs Purchased label, time axis, two-block grid.
- **Notes & Customizations**: Part of AMR data family; scaling applies.

### FactSet AMR Trialer Docs Purchased Data Block
- **Section Type**: Source Data Table
- **Description & Purpose**: AMR Trialer Docs Purchased data within the AMR family.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Trialer Docs Purchased labeling, date axis, two-block per-row grid.
- **Notes & Customizations**: AMR-related block with standard scaling.

### FactSet AMR Internal Docs Purchased Data Block (Internal)
- **Section Type**: Source Data Table
- **Description & Purpose**: AMR Internal Docs Purchased sub-block within FactSet AMR.
- **Section Range**: C4:AS117; AU4:BO117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: Internal Docs Purchased label, time axis, two-block per-row layout.
- **Notes & Customizations**: Part of the AMR data family; scaling rules apply.

### Derived Totals / Totals Row Block
- **Section Type**: Totals Table (Summary Row Group)
- **Description & Purpose**: Aggregated totals row blocks aligned to Section Totals (e.g., “Total” in the inverted_index mapping). These rows summarize the combined effect of all sources for each period.
- **Section Range**: A8; A15; A22; A29; A36; A43; A50; A57; A64; A71; A78; A85; A92; A99; A102; A105; A108; A111; A114; A117
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1; AU1:BO1 (same date headers as the main matrix)
  - **Date Range**:
    - ds_1: Monthly series from 2017-01 to 2020-07
    - ds_2: Monthly series from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Key Components**: “Total” row anchors that sum across sources, used for quick KPI-style retrieval.
- **Notes & Customizations**: This section aggregates across the full set of source blocks; flag values are in the A-column totals lines.

### Time Series Headers (Dates Axis)
- **Section Type**: Header / Axis Definition
- **Description & Purpose**: Defines the monthly date axes used by all data blocks in the matrix. There are two date series (ds_1 and ds_2) enabling parallel views or historical comparison.
- **Section Range**: C1:AS1 (ds_1 header row); AU1:BO1 (ds_2 header row)
- **Time Series Horizon**:
  - **Dates Location**: C1:AS1 and AU1:BO1 (date labels across columns)
  - **Date Range**:
    - ds_1: Monthly labels from 2017-01 to 2020-07
    - ds_2: Monthly labels from 2017-01 to 2018-09
  - **Frequency**: Monthly
- **Notes & Customizations**: The JSON date_series_definitions confirms ds_1 as “Monthly series from 2017-01 to 2020-07” and ds_2 as “Monthly series from 2017-01 to 2018-09.” The two series enable broader vs. shorter horizon analysis within the same sheet.

Guidance notes for future data retrieval
- The primary data matrix is organized as a consolidated, multi-source time-series grid. The two date axes (C1:AS1 and AU1:BO1) embody the time dimension, with monthly cadence (ds_1 and ds_2).
- Source blocks are mapped in column A with headers such as Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, BRM Global, BRM Single, and various FactSet AMR sub-blocks (Active, Trailers, Internal, Active Docs Purchased, Trialer Docs Purchased, Internal Docs Purchased, etc.).
- Numeric cells are often scaled by 1000 (scale: 1000) to reflect thousands; be mindful of unit interpretation when aggregating or presenting results.
- Totals lines (A8, A15, A22, etc.) summarize across the source blocks for each period; these can be used to quickly verify cross-source aggregates.

If you want, I can convert this into a machine-readable schema with exact per-section ranges for every block, or extract a compact index mapping that links each source header to its corresponding two-block per-row data ranges.