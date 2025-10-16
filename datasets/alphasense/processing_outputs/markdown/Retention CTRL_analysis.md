```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Retention CTRL
- **Key Sections Identified**:
    - Header
    - Annual Retention - Financial
    - Evergreen Retention - Financial (Annual Equivalent)
    - Annual Retention - Corporate
    - Annual Retention - Other
    - Evergreen Retention - Other (Annual Equivalent)

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains company name, report name, and scenario description.
- **Cell Range**: B2:B4
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: B2:B4
- **Time Series Details**: None
- **Key Components**: Company Name, Report Name, Scenario Description
- **Notes & Customizations**: Contains the scenario name, such as "1 - Base - $25mm".

### Annual Retention - Financial
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention percentages for different revenue scenarios.
- **Cell Range**: A12:Q18
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E7:Q7
    - **Data Range**:
      - Annual data: I15:Q18
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Revenue, Annual Retention % - Financial, "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Evergreen Retention - Financial (Annual Equivalent)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays evergreen retention percentages (annual equivalent) for different revenue scenarios.
- **Cell Range**: A21:Q25
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E7:Q7
    - **Data Range**:
      - Annual data: I22:Q25
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Evergreen Retention % - Financial (Annual Equivalent), "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Annual Retention - Corporate
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention percentages for different revenue scenarios.
- **Cell Range**: A28:DV32
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E7:Q7, T7:FS7
    - **Data Range**:
      - Annual data: I29:Q32
      - Monthly data: BX28:DV28
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-01 to 2027-12-01 (T7:FS7). Anchor points: T7=2015-01-01, AF7=2016-01-01, AR7=2017-01-01, BD7=2018-01-01, BP7=2019-01-01, CB7=2020-01-01, CN7=2021-01-01, CZ7=2022-01-01, DL7=2023-01-01, DX7=2024-01-01, EJ7=2025-01-01, EV7=2026-01-01, FH7=2027-01-01
    - **Frequency**:
      - Annual
      - Repeating Annual (12 times)
- **Key Components**: Annual Retention % - Corporate, "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Annual Retention - Other
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays annual retention percentages for different revenue scenarios.
- **Cell Range**: A35:DV39
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E7:Q7, T7:FS7
    - **Data Range**:
      - Annual data: I36:Q39
      - Monthly data: BX35:DV35
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-01 to 2027-12-01 (T7:FS7). Anchor points: T7=2015-01-01, AF7=2016-01-01, AR7=2017-01-01, BD7=2018-01-01, BP7=2019-01-01, CB7=2020-01-01, CN7=2021-01-01, CZ7=2022-01-01, DL7=2023-01-01, DX7=2024-01-01, EJ7=2025-01-01, EV7=2026-01-01, FH7=2027-01-01
    - **Frequency**:
      - Annual
      - Repeating Annual (12 times)
- **Key Components**: Annual Retention % - Other, "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.

### Evergreen Retention - Other (Annual Equivalent)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays evergreen retention percentages (annual equivalent) for different revenue scenarios.
- **Cell Range**: A42:DV46
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E7:Q7, T7:FS7
    - **Data Range**:
      - Annual data: I43:Q46
      - Monthly data: BX42:DV42
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-01 to 2027-12-01 (T7:FS7). Anchor points: T7=2015-01-01, AF7=2016-01-01, AR7=2017-01-01, BD7=2018-01-01, BP7=2019-01-01, CB7=2020-01-01, CN7=2021-01-01, CZ7=2022-01-01, DL7=2023-01-01, DX7=2024-01-01, EJ7=2025-01-01, EV7=2026-01-01, FH7=2027-01-01
    - **Frequency**:
      - Annual
      - Repeating Annual (12 times)
- **Key Components**: Evergreen Retention % - Other (Annual Equivalent), "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"
- **Notes & Customizations**: Retention percentages are scaled by 1000.
```