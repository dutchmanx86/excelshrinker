## 1. Spreadsheet Overview
- **Sheet Name**: FY22 Overlay
- **Key Sections Identified**:
    - Header
    - Sales Rep Data
    - Quarterly Quota Attainment

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains column labels defining the data in subsequent rows. Provides context for understanding the data.
- **Cell Range**: A1:AM1
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: A1:AM1
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: Q1FY22 to Q4FY22
    - **Frequency**: Quarterly
- **Key Components**: Name, Term Date, Plan, Segment, Manager, Region, Position Status, FY22 Quota, Ramp Start Month, Q1FY22, Q2FY22, Q3FY22, Q4FY22, FY22 Ramped Quota
- **Notes & Customizations**: "FY22" likely refers to Fiscal Year 2022.

### Sales Rep Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains information about individual sales representatives, including their plan, segment, manager, region, quota, and ramp-up details.
- **Cell Range**: A2:J6
- **Layout Structure**:
    - **Row Headers Location**: A2:A6 (Name), D2:D6 (Plan), E2:E6 (Segment), F2:F6 (Manager), G2:G6 (Region), H2:H6 (Position Status)
    - **Column Headers Location**: A1:J1
    - **Data Range**: B2:B6, C2:C6, D2:D6, E2:E6, F2:F6, G2:G6, H2:H6, I2:I6, J2:J6
- **Time Series Details**: None
- **Key Components**: Name, Term Date, Plan, Segment, Manager, Region, Position Status, FY22 Quota, Ramp Start Month
- **Notes & Customizations**: "Future Hire" is a possible value for "Position Status." Quota is scaled by 1000.

### Quarterly Quota Attainment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains quarterly quota attainment data for each sales representative.
- **Cell Range**: AI1:AM6
- **Layout Structure**:
    - **Row Headers Location**: A2:A6 (Implied Sales Rep Names)
    - **Column Headers Location**: AI1:AM1
    - **Data Range**: AI2:AM6
- **Time Series Details**:
    - **Date Range**: Q1FY22 to Q4FY22
    - **Frequency**: Quarterly
- **Key Components**: Q1FY22, Q2FY22, Q3FY22, Q4FY22, FY22 Ramped Quota
- **Notes & Customizations**: Values are scaled by 1000.
