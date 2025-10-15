## 1. Spreadsheet Overview
- **Sheet Name**: Corp Model
- **Key Sections Identified**:
    - Header
    - Corporate Forecast Details
    - Corporate: Full Team Headcount
    - Corporate: Ramped Team - Value Team
    - Ramp Build - Corporate
    - Inputs

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report.
- **Cell Range**: B2:B2
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: B2:B2
- **Time Series Details**: None
- **Key Components**: Corporate: Forecast Details
- **Notes & Customizations**: None

### Corporate Forecast Details
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes key headcount metrics derived from the QoS model.
- **Cell Range**: C4:AE14
- **Layout Structure**:
    - **Row Headers Location**: C4:C14
    - **Column Headers Location**: W5:AE5 (Implicit monthly dates)
    - **Data Range**:
      - Monthly data: W8:AE14
- **Time Series Details**:
    - **Date Range**: 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Total QoS, Average Quota, Gross Headcount, Attrition, Net Headcount, Gross Ramped Headcount, Attrition, Net Ramped Headcount
- **Notes & Customizations**: Values are scaled by 1000.

### Corporate: Full Team Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the headcount for the full corporate team, broken down by individuals and teams.
- **Cell Range**: B17:AH49
- **Layout Structure**:
    - **Row Headers Location**: C19:C41, AH20:AH23, AH30:AH31, AH44:AH46
    - **Column Headers Location**: W19:AE19 (Monthly dates)
    - **Data Range**:
      - Monthly data: W20:AE25, W28:AE31, W38:AE41, W45:AE46, W49:AE49, AC44:AE44, AG30:AG31, AG44:AG46
- **Time Series Details**:
    - **Date Range**: 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Total Headcount (Net), Batt, Kate, Hoy, Michael, Klemm, Brian, TBD Corp Dir #2, John Gresham, Value Team, Full Team, Value, PFSU, Total Corporate (from QoS), Ramped Headcount - Adjusted (Attrition), Attrition Adjustment - Value
- **Notes & Customizations**: Values are scaled by 1000. PFSU Transition only has data from Z40:AE40.

### Corporate: Ramped Team - Value Team
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the ramp build for the corporate value team.
- **Cell Range**: B52:AE76
- **Layout Structure**:
    - **Row Headers Location**: C54:C59, C61:C71, C74:C76
    - **Column Headers Location**: H54:AE54, H61:AE61, H73:AE73 (Monthly dates)
    - **Data Range**:
      - Monthly data: H56:AE59, I62:AE71, H74:AE76, D57:E70, F56:F59, F74:F76, AG74:AG75
- **Time Series Details**:
    - **Date Range**: 2020-02-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Ramp Build - Corporate, Beginning of Period, Added, Removed, End of Period, Ramp, Attrition, Effective Start, Add, Effective End
- **Notes & Customizations**: Values are scaled by 1000.

### Inputs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Input assumptions for the model.
- **Cell Range**: B78:S100
- **Layout Structure**:
    - **Row Headers Location**: C80, M93:M100
    - **Column Headers Location**: N79:S79, N92:S92 (Categories)
    - **Data Range**: N80:S88, N93:S100
- **Time Series Details**: None
- **Key Components**: Plan, Active, Commercial, Corporate, Enterprise, SS Corp, SS Comm, Quota, Attrition, Ramped, Q1 Attnmt, Q2 Attnmt, Q3 Attnmt, Q4 Attnmt
- **Notes & Customizations**: None
