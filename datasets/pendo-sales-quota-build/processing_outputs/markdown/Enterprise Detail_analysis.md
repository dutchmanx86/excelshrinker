## 1. Spreadsheet Overview
- **Sheet Name**: Enterprise Detail
- **Key Sections Identified**:
    - Header
    - Bookings Targets by Manager
    - QoS (Net) by Manager
    - Attainment by Manager
    - Attainment (% Manager QoS)

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and column headers for the subsequent data sections.
- **Cell Range**: B2:Z4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B4:Z4
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Enterprise, Bookings Targets, QoS (Net), Attainment, Attainment (% Manager QoS)
- **Notes & Customizations**: None

### Section Name: Bookings Targets by Manager
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the bookings targets for each manager across different quarters.
- **Cell Range**: B6:F26
- **Layout Structure**:
    - **Row Headers Location**: B7:B26
    - **Column Headers Location**: C6:E6
    - **Data Range**:
      - Quarterly data: `C7:F10`, `C12:F13`, `C15:F16`, `C20:F26`
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Coverage, Managers, Sabikihi, Harsh, NYC ENT RVP, Miller, BJ, Tuttle, Patrick, Yatsko, Natalie, Wilson, Matt, Total Manager Target
- **Notes & Customizations**: Values are in thousands.

### Section Name: QoS (Net) by Manager
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the QoS (Net) for each manager across different quarters.
- **Cell Range**: H6:L26
- **Layout Structure**:
    - **Row Headers Location**: H7:H26
    - **Column Headers Location**: I6:K6
    - **Data Range**:
      - Quarterly data: `I7:L10`, `I12:L13`, `I15:L16`, `I20:L26`
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Coverage, Managers, Sabikihi, Harsh, NYC ENT RVP, Miller, BJ, Tuttle, Patrick, Yatsko, Natalie, Wilson, Matt, Total Manager Target, Managers - Gross (No Attrition)
- **Notes & Customizations**: Values are in thousands.

### Section Name: Attainment by Manager
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the attainment for each manager across different quarters.
- **Cell Range**: N6:R26
- **Layout Structure**:
    - **Row Headers Location**: N7:N26
    - **Column Headers Location**: O6:Q6
    - **Data Range**:
      - Quarterly data: `O7:R10`, `O20:R26`
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Managers, Sabikihi, Harsh, NYC ENT RVP, Miller, BJ, Tuttle, Patrick, Yatsko, Natalie, Wilson, Matt, Total Manager Target, Managers - Gross (No Attrition)
- **Notes & Customizations**: None

### Section Name: Attainment (% Manager QoS)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the attainment percentage based on Manager QoS for Company and VP across different quarters.
- **Cell Range**: T4:X12
- **Layout Structure**:
    - **Row Headers Location**: T7:T12
    - **Column Headers Location**: U6:W6
    - **Data Range**:
      - Quarterly data: `U7:X12`
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Manager QoS, CRO, Company, VP
- **Notes & Customizations**: None
