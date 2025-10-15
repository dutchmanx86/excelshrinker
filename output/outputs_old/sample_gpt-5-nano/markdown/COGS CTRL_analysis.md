## 1. Spreadsheet Overview
- **Sheet Name**: COGS CTRL
- **Key Sections Identified**:
  - Base - $25mm
  - Growth - $25mm
  - Base - $50mm
  - Base - $50mm (R&D)
  - International Filing Expense - % of Non Paying Brokers
  - Dow Jones - Base
  - Dow Jones Expense - Tier 1 User Limit
  - Dow Jones Expense - Tier 2 User Limit
  - Dow Jones Expense - Tier 3 User Limit

## 2. Detailed Section Analysis

### Base - $25mm
- **Section Type**: Custom P&L
- **Description & Purpose**: Scenario-based cost-of-goods-sold (COGS) data block representing a baseline cost profile at a $25 million level; used to project and compare cost drivers across time.
- **Cell Range**: B14:B1586
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (Year labels linked to ds_1)
  - **Date Range**: 2015 through 2027 (Annual)
  - **Frequency**: Annual
  - Secondary/Complementary Dates: T6:CJ6 (ds_2) for an additional annual/date-row structure; T8:FS8 (ds_3) provides monthly date labels if referenced
- **Key Components**: Major cost drivers and categories arranged in rows within the section; high-level categories guide the P&L-like structure (without listing every label).
- **Notes & Customizations**: This is a tailored base scenario, not a standard off-the-shelf P&L; multiple date axes and an extended category layout indicate a customized planning model.

### Growth - $25mm
- **Section Type**: Custom P&L
- **Description & Purpose**: Growth-oriented variant of the base model at the same dollar scale (growth scenario for the $25mm baseline), enabling comparison of incremental costs under growth conditions.
- **Cell Range**: B15:B1587
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (Year labels linked to ds_1)
  - **Date Range**: 2015 through 2027 (Annual)
  - **Frequency**: Annual
  - Complementary Dates: T6:CJ6 (ds_2) and T8:FS8 (ds_3) may also be involved for aligned axes
- **Key Components**: High-level cost-driver groups and growth-related adjustments; similar structural layout to the Base - $25mm section.
- **Notes & Customizations**: Custom scenario mirroring the base with growth adjustments; designed for scenario analysis.

### Base - $50mm
- **Section Type**: Custom P&L
- **Description & Purpose**: Baseline COGS projection at a higher scale ($50mm), to compare with the $25mm baselines and assess scale effects.
- **Cell Range**: B16:B1588
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (Year labels linked to ds_1)
  - **Date Range**: 2015 through 2027 (Annual)
  - **Frequency**: Annual
  - Complementary Dates: T6:CJ6 (ds_2) and T8:FS8 (ds_3)
- **Key Components**: Broad cost-category structure consistent with other base scenarios; supports scale-based comparison.
- **Notes & Customizations**: Higher scale is reflected in the same structural layout to facilitate direct comparison with the $25mm scenarios.

### Base - $50mm (R&D)
- **Section Type**: Custom P&L
- **Description & Purpose**: $50mm base with an explicit R&D allocation or focus, allowing an R&D-adjusted COGS view within the same framework.
- **Cell Range**: B17:B1589
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (Year labels linked to ds_1)
  - **Date Range**: 2015 through 2027 (Annual)
  - **Frequency**: Annual
  - Complementary Dates: T6:CJ6 (ds_2) and T8:FS8 (ds_3)
- **Key Components**: Base structure plus R&D-specific adjustments or lines; maintains a common scaffolding with other base scenarios.
- **Notes & Customizations**: Customization to isolate R&D-related costs within the broader COGS framework.

### International Filing Expense - % of Non Paying Brokers
- **Section Type**: Cost Allocation Table
- **Description & Purpose**: Allocation/expense line items for international filing costs tied to non-paying brokers; a targeted cost category rather than a full P&L view.
- **Cell Range**: B468:B475
- **Time Series Horizon**:
  - **Dates Location**: Not explicitly shown in this small block; typically linked to the overall ds structure if used in a larger row/column grid
  - **Date Range**: N/A for this compact slice; would align with the sheet’s date axes if extended
  - **Frequency**: N/A (static allocation block)
- **Key Components**: High-level expense category; focuses on international filing costs as a percentage-driven line item.
- **Notes & Customizations**: Specific to international filing costs; not a full P&L but a dedicated cost category.

### Dow Jones - Base
- **Section Type**: Expense Schedule
- **Description & Purpose**: Baseline Dow Jones-related costs and fees; serves as a reference point for Dow Jones-specific expenses within the broader COGS CTRL model.
- **Cell Range**: B731:B788
- **Time Series Horizon**:
  - **Dates Location**: I1001:Q1001 (ds_4) and BP1001:FS1001 (ds_5) provide date-backed series for Dow Jones items
  - **Date Range**:
    - ds_4: Annual series from 2000 for 9 periods (start 2000-01-01)
    - ds_5: Annual series from 2000 for 108 periods (start 2000-01-01)
  - **Frequency**:
    - ds_4: Annual
    - ds_5: Annual
- **Key Components**: Core Dow Jones cost items (base line) with associated monthly/annual date axes; captures a broad set of Dow Jones-related expenses.
- **Notes & Customizations**: Includes both base data and multi-period date-backed series to support long-horizon analysis.

### Dow Jones Expense - Tier 1 User Limit
- **Section Type**: Tiered Expense Schedule
- **Description & Purpose**: Tier 1 user-limit based Dow Jones expense line items; part of a multi-tier cost structure for Dow Jones costs.
- **Cell Range**: B740:B790
- **Time Series Horizon**:
  - **Dates Location**: I1001:Q1001 (ds_4) and BP1001:FS1001 (ds_5) provide date-backed series
  - **Date Range**: 
    - ds_4: Annual periods starting 2000 (9 periods)
    - ds_5: Annual periods starting 2000 (108 periods)
  - **Frequency**:
    - ds_4: Annual
    - ds_5: Annual
- **Key Components**: Tiered price/expense lines corresponding to a 1st-tier user limit; aligns with other Dow Jones tier sections.
- **Notes & Customizations**: Includes both yearly and extended-year date references to support tier-based financial modelling.

### Dow Jones Expense - Tier 2 User Limit
- **Section Type**: Tiered Expense Schedule
- **Description & Purpose**: Dow Jones costs aligned to Tier 2 user limit; complements Tier 1 data for a complete tiered cost view.
- **Cell Range**: B754:B804
- **Time Series Horizon**:
  - **Dates Location**: I1001:Q1001 (ds_4) and BP1001:FS1001 (ds_5)
  - **Date Range**: 
    - ds_4: Annual, starting 2000 for 9 periods
    - ds_5: Annual, starting 2000 for 108 periods
  - **Frequency**: Annual
- **Key Components**: Tier 2 cost items; structured similarly to Tier 1 for comparability.
- **Notes & Customizations**: Standardized tier approach across Dow Jones expenses.

### Dow Jones Expense - Tier 3 User Limit
- **Section Type**: Tiered Expense Schedule
- **Description & Purpose**: Dow Jones costs tied to Tier 3 user limit; final tier in the Dow Jones expense family for modelling purposes.
- **Cell Range**: B768:B818
- **Time Series Horizon**:
  - **Dates Location**: I1001:Q1001 (ds_4) and BP1001:FS1001 (ds_5)
  - **Date Range**: 
    - ds_4: Annual, 9 periods starting 2000
    - ds_5: Annual, 108 periods starting 2000
  - **Frequency**: Annual
- **Key Components**: Tier 3 cost items; designed to mirror the Tier 1 and Tier 2 structures.
- **Notes & Customizations**: Part of an overarching Dow Jones expense framework with multi-tier data.

Notes on the dictionary-derived structure:
- The analysis focuses on the major logical sections inferred from the inverted_index mappings, which map to blocks of cells in column B that contain section labels and their associated data. Each section’s time-series context uses the ds_1 through ds_5 date-series definitions provided in the data, with explicit date-locations and ranges where applicable.
- The sheet’s date-series definitions (ds_1 through ds_5) indicate a mix of annual and monthly horizons, applied across different sections for time-aligned analysis.
- The sections are arranged to support scenario analysis (Base, Growth, and higher scale) and a tiered Dow Jones cost structure, consistent with a cost-control and planning framework.

If you’d like, I can add a compact retrieval map that translates each section into a single lookup object with its exact cell-range and date-series references for quick programmatic access.