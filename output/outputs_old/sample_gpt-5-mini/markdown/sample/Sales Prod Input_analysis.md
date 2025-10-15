## 1. Spreadsheet Overview
- **Sheet Name**: Sales Prod Input
- **Key Sections Identified**:
  - Time Series Header (monthly periods)
  - Quota per Person (role-level quotas)
  - Seasonality (all-roles monthly factors)
  - Productivity (role-level productivity inputs)
  - Productivity (Adjusted for Seasonality) (calculated/adjusted role productivity)

## 2. Detailed Section Analysis

### Time Series Header
- **Section Type**: Date Header / Time Series Row
- **Description & Purpose**: Contains the primary period labels used across the sheet (the monthly columns). All monthly data columns in the tables reference these period labels for alignment and retrieval.
- **Cell Range**: E1:P1
- **Time Series Horizon**:
  - **Dates Location**: E1:P1
  - **Date Range**: Jan 2021 to Dec 2021 (defined by date series ds_1; start_date = 2021-01-31; pattern: "Monthly series from 2021-01 to 2021-12")
  - **Frequency**: Monthly
- **Key Components**:
  - 12 monthly period cells aligned left-to-right across E1:P1
- **Notes & Customizations**:
  - Date series is defined in the sheet metadata as ds_1 (monthly, increment 1 month, start_date 2021-01-31).

---

### Quota per Person
- **Section Type**: Key Metrics Table (custom role quota table)
- **Description & Purpose**: Role-level quota settings and monthly quota values for each sales role. Used to define baseline quotas and monthly quota distribution by role.
- **Cell Range**: A3:P9
- **Time Series Horizon**:
  - **Dates Location**: E1:P1 (this section's monthly values align under the global date header)
  - **Date Range**: Jan 2021 to Dec 2021
  - **Frequency**: Monthly
- **Key Components**:
  - Section heading at A3 ("Quota per Person")
  - Role labels in column A for this block (A5:A9)
  - Baseline / summary numeric columns (single-value columns in C5:C9)
  - Monthly quota values in columns E5:P9 (per-role monthly series)
- **Notes & Customizations**:
  - Roles used here (and repeated elsewhere) are:
    - "Account Manager" at A5
    - "AE - Financial" at A6
    - "AE - Corporate" at A7
    - "VP - Bus Dev" at A8
    - "AE - Enterprise" at A9
  - Some monthly cells in this block use an internal scale factor (F7:P7, F8:P8, F9:P9 are flagged with scale = 1000); treat those rows as thousands when retrieving raw values.
  - Baseline numbers for each role appear in column C (C5:C9).

---

### Seasonality
- **Section Type**: Key Metrics Table (seasonality factors)
- **Description & Purpose**: Single-row seasonality factors applied across all roles to model intra-year variation (used to adjust productivity/quotas).
- **Cell Range**: A11:P13
- **Time Series Horizon**:
  - **Dates Location**: E1:P1
  - **Date Range**: Jan 2021 to Dec 2021
  - **Frequency**: Monthly
- **Key Components**:
  - Section heading at A11 ("Seasonality")
  - "All Roles" label at A13 indicating a single set of monthly seasonality factors that apply to all roles
  - Monthly seasonality factor values in E13:P13
- **Notes & Customizations**:
  - Seasonality is provided as one row of monthly multipliers/factors that upstream calculations (e.g., adjusted productivity) use.

---

### Productivity
- **Section Type**: Key Metrics Table (role-level productivity inputs)
- **Description & Purpose**: Input table of productivity assumptions by role. These are likely conversion or productivity rates that feed into production or quota attainment calculations.
- **Cell Range**: A15:P21
- **Time Series Horizon**:
  - **Dates Location**: E1:P1
  - **Date Range**: Jan 2021 to Dec 2021
  - **Frequency**: Monthly
- **Key Components**:
  - Section heading at A15 ("Productivity")
  - Role labels in A17:A21 matching the same role order as the quota block
  - Baseline / scalar productivity inputs in column C (C17:C21)
  - Monthly productivity values in E17:P21
- **Notes & Customizations**:
  - The same five roles are present here and mapped to exact cells:
    - "Account Manager" at A17
    - "AE - Financial" at A18
    - "AE - Corporate" at A19
    - "VP - Bus Dev" at A20
    - "AE - Enterprise" at A21
  - A few monthly cells may be single-value entries (e.g., E19 and F19:P19 have explicit numbers), ensure retrieval handles both single-cell and range formats.

---

### Productivity (Adjusted for Seasonality)
- **Section Type**: Calculated Metrics Table (adjusted productivity)
- **Description & Purpose**: Role-level productivity after application of the seasonality factors. Intended to be the effective monthly productivity used in downstream modeling (combines raw productivity and seasonality).
- **Cell Range**: A23:P29
- **Time Series Horizon**:
  - **Dates Location**: E1:P1
  - **Date Range**: Jan 2021 to Dec 2021
  - **Frequency**: Monthly
- **Key Components**:
  - Section heading at A23 ("Productivity (Adjusted for Seasonality)")
  - Role labels in A25:A29 (same five roles)
  - Monthly adjusted productivity values in E25:P29
  - Possibly baseline adjusted values in column C (if present; C25:C29 are available/expected)
- **Notes & Customizations**:
  - Roles map to these cells:
    - "Account Manager" at A25
    - "AE - Financial" at A26
    - "AE - Corporate" at A27
    - "VP - Bus Dev" at A28
    - "AE - Enterprise" at A29
  - Monthly values for adjusted productivity exist across E25:P29; some rows include single-cell numbers in E/F before the full E:P range (e.g., E27 and F27:P27 noted as numeric). Verify retrieval logic to capture both the initial cell and the extended F:Px ranges.
  - This section is clearly derived from the Productivity and Seasonality sections (custom calculated table rather than raw inputs).

---

Notes on repeated role mapping and value types
- The five role labels repeat in identical order across the three role blocks. Exact cell positions (resolved from the sheet dictionary):
  - Account Manager: A5, A17, A25
  - AE - Financial: A6, A18, A26
  - AE - Corporate: A7, A19, A27
  - VP - Bus Dev: A8, A20, A28
  - AE - Enterprise: A9, A21, A29
- Primary monthly columns for time series are E:P and are defined by date series ds_1 (Monthly, Jan–Dec 2021).
- Several numeric ranges include a scale metadata (scale = 1000) for specific rows (notably F7:P7, F8:P8, F9:P9). When extracting values, apply that scale to convert to base units.
- Baseline single-cell numeric entries exist in column C for many rows (C5, C6, C7, C8, C9, C17–C21, etc.) — these appear to be role-level baselines or summary inputs and should be captured alongside the monthly series.