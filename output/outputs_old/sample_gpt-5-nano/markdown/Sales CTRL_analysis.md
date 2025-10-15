## 1. Spreadsheet Overview
- **Sheet Name**: Sales CTRL
- **Key Sections Identified**:
  - Headcount Baselines & Scenarios (multi-scenario staffing plan)
  - Role-based Headcount Allocation (by role, with additions/removals)
  - Percent of Total Headcount (composition metric)

Notes:
- The file appears to be a workforce model with multiple staffing scenarios and a detailed, role-specific headcount/deduction view. Time series are defined using three embedded date series in the workbook:
  - ds_1: Annual series (2015 through 2027)
  - ds_2: Repeating annual monthly view (monthly across years)
  - ds_3: Monthly series (2015-01 to 2027-12)
- The three date-series definitions are explicitly provided in the JSON and are resolved to actual values below.

Date-series definitions resolved from the JSON:
- ds_1 (Annual): series_type = annual; start_date = 2015-01-01; pattern = "Annual series from 2015 to 2027".
- ds_2 (Monthly, repeating annual): series_type = repeating_annual; start_date = 2015-01-01; pattern = "Annual values repeating 12 times from 2015 to 2027".
- ds_3 (Monthly): series_type = monthly; start_date = 2015-01-31; pattern = "Monthly series from 2015-01 to 2027-12".

Cited data source references (for retrieval context):
- Primary time-series headers are located in E6:Q6 (annual ds_1) and T6:FS6 (monthly ds_2). Monthly numeric periods/data align with ds_3 through E8:Q8 and related ranges.

## 2. Detailed Section Analysis

### Headcount Baselines & Scenarios
- **Section Type**: Custom Headcount Table
- **Description & Purpose**: Consolidates the baseline headcount, plus planned growth and base scenarios. This section provides the foundational staffing levels and the delta between scenarios (Base - $25mm, Growth - $25mm, Base - $50mm, Base - $50mm (R&D)), along with a percentage of total headcount. It is intended to support scenario planning and headcount budgeting across annual and monthly horizons.
- **Cell Range**: B13:B571
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (annual ds_1) and T6:FS6 (monthly ds_2)
  - **Date Range**: 
    - ds_1 (Annual): 2015-01-01 to 2027-01-01
    - ds_2 (Monthly): 2015-01-01 to 2027-12-31
  - **Frequency**:
    - Annual (ds_1)
    - Monthly (ds_2)
- **Key Components**: 
  - Total Headcount
  - Base - $25mm
  - Growth - $25mm
  - Base - $50mm
  - Base - $50mm (R&D)
  - % of Total Headcount
- **Notes & Customizations**: This is a multi-scenario staffing plan with several distinct baselines. It includes baseline, growth, and split baselines, plus a percentage composition metric. The structure appears tailored for scenario comparison rather than a single standard P&L/Balance Sheet format.

### Role-based Headcount Allocations (Additions)
- **Section Type**: Headcount Table by Role
- **Description & Purpose**: Captures headcount changes by specific roles, showing additions/removals across periods. This section drives staffing allocations and headcount movement analysis by function and title, supporting workforce planning and cost/supply planning across time.
- **Cell Range (example subset)**: 
  - Account Manager: B160:B163
  - AE - Financial: (example range) B177:B180
  - AE - Corporate: B194:B197
  - VP - Bus Dev: B211:B214
  - AE - Enterprise: B228:B231
  - AE - Other: B245:B248
  - CRO: B264:B479
  - Product Specialist: B352:B535
  - Product Specialist - Mgr: B369:B528
  - Sales - Admin: B386:B549
  - Sales Manager: B403:B486
  - Sales Operations Manager: B420:B556
  - SDR: B447:B500
- **Time Series Horizon**:
  - **Dates Location**: T6:FS6 (monthly ds_2 as the primary date axis for time-series columns) and related month-columns
  - **Date Range**: 2015-01-01 to 2027-12-31
  - **Frequency**: Monthly
- **Key Components**: 
  - Role title (e.g., Account Manager, AE/Corp/Enterprise, CRO, SDR, Sales Ops, etc.)
  - Additions in period (and in some rows, removals or adjusted baselines)
  - Role-specific compensation/headcount-related metrics often scaled (note: many numeric cells are scaled by 1000)
- **Notes & Customizations**: The ranges imply a large, role-by-role, period-by-period dataset. Data appear to be built to support scenario planning and headcount budgeting at the granularity of individual roles, including additions/removals and multi-year horizons. The presence of 1000x scaling and multiple monthly columns indicates a blend of headcount counts and related financial metrics.

### Percent of Total Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Shows the composition of headcount as a percentage of total headcount, enabling quick assessment of share by role or category within the overall workforce.
- **Cell Range**: B48:B134
- **Time Series Horizon**:
  - **Dates Location**: E6:Q6 (annual ds_1) and T6:FS6 (monthly ds_2) (where applicable for the percent-of-total data)
  - **Date Range**:
    - ds_1 (Annual): 2015-01-01 to 2027-01-01
    - ds_2 (Monthly): 2015-01-01 to 2027-12-31
  - **Frequency**:
    - Annual (ds_1)
    - Monthly (ds_2)
- **Key Components**: The section captures the share of headcount by category/role, enabling quick visibility into workforce mix.
- **Notes & Customizations**: This is a derived metric that complements the base headcount narrative, providing mix insights rather than a standalone headcount count.

### CRO (Chief Revenue Officer) - Role Headcount
- **Section Type**: Headcount Table by Role
- **Description & Purpose**: Represents the CRO-related headcount data and its evolution across periods. It sits within the broader role-based headcount analysis and likely aggregates multiple sub-rows of data pertaining to revenue leadership.
- **Cell Range**: B264:B479
- **Time Series Horizon**:
  - **Dates Location**: T6:FS6 (monthly ds_2)
  - **Date Range**: 2015-01-01 to 2027-12-31
  - **Frequency**: Monthly
- **Key Components**: CRO headcount path, additions/removals across periods; broader leadership/headcount metrics in the CRO domain.
- **Notes & Customizations**: The CRO section spans a substantial vertical range, indicating a cluster of related rows (likely multiple sub-entries such as additions, removals, and targets). It’s a bespoke data block rather than a single standard template line.

### Product Specialist (and Manager) Headcount
- **Section Type**: Headcount Table by Role
- **Description & Purpose**: Contains data for Product Specialist roles, including the base, added, removed, and potentially upside/downside scenarios, across periods. Useful for product-focused headcount planning.
- **Cell Range**: 
  - Product Specialist: B352:B535
  - Product Specialist - Mgr: B369:B528
- **Time Series Horizon**:
  - **Dates Location**: T6:FS6
  - **Date Range**: 2015-01-01 to 2027-12-31
  - **Frequency**: Monthly
- **Key Components**: Product Specialist headcount by role with manager-level overlay; period-by-period movement and associated metrics.
- **Notes & Customizations**: Large, role-specific blocks indicating nuanced product-organization staffing planning.

### Sales - Admin, Sales Manager, Sales Operations Manager, SDR (Sales & Enablement Proper)
- **Section Type**: Headcount Table by Role
- **Description & Purpose**: Role-specific blocks for Sales Operations, Sales Management, SDRs, and related administrative roles. These sections support granular sales force planning, leadership alignment, and enablement staffing considerations.
- **Cell Ranges**:
  - Sales - Admin: B386:B549
  - Sales Manager: B403:B486
  - Sales Operations Manager: B420:B556
  - SDR: B447:B500
- **Time Series Horizon**:
  - **Dates Location**: T6:FS6
  - **Date Range**: 2015-01-01 to 2027-12-31
  - **Frequency**: Monthly
- **Key Components**: Role-specific headcount and implied compensation/staffing metrics across the sales enablement and management layers.
- **Notes & Customizations**: Indicates a sizable, role-based budgeting footprint across multiple time periods, with 1000x scaling used in many numeric blocks to reflect large-scale financial figures.

### Additional Role-Driven Sections (if applicable)
- The inverted index contains several other role-specific blocks (e.g., AE - Financial, AE - Corporate, AE - Enterprise, AE - Other, VP - Bus Dev, etc.). Each would similarly be defined as a separate "Headcount Table by Role" subsection with:
  - Cell Range: corresponding B-column blocks (e.g., B177:B180 for AE - Financial; B194:B197 for AE - Corporate; B211:B214 for VP - Bus Dev; B228:B231 for AE - Enterprise; … up to B500-range for SDR-related lines)
  - Time Series Horizon: Dates Location - T6:FS6 (monthly ds_2); Date Range 2015-01-01 to 2027-12-31; Frequency Monthly
  - Description: Role-specific headcount movements (additions/removals), aligned to the overall staffing model
  - Notes: Role-specific structure may include multi-row groupings to capture sub-activities; scaling (1000x) is common in numeric blocks

End notes:
- The structure is clearly designed for a multi-year headcount planning model with several scenario baselines and a detailed role-by-role view. The time series framework relies on three resolved date-series definitions (annual, monthly repeating-annual, and monthly). For retrieval, use the sheet name Sales CTRL as the anchor, and then target the appropriate section ranges as listed above (e.g., Headcount Baselines & Scenarios at B13:B571, or Role-based Headcount at B160:B163 for Account Manager, etc.).