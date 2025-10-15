## 1. Spreadsheet Overview
- **Sheet Name**: PoP Usage Data
- **Key Sections Identified**:
    - Title/Header
    - Chassis Usage Data by Company
    - Totals & Utilization Metrics
    - Footnotes

## 2. Detailed Section Analysis

### Title/Header
- **Section Type**: Title/Header
- **Description & Purpose**: Contains the title of the report and a brief description.
- **Cell Range**: C2:F3
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: E3:F3
    - **Data Range**: N/A
- **Time Series Details**:
    - **Date Range**: W.E. 3/7/2015 to W.E. 3/14/2015
    - **Frequency**: Weekly
- **Key Components**: Pool of Pools Chassis on the Street* - WEEKLY AVERAGE, W.E. 3/7/2015, W.E. 3/14/2015
- **Notes & Customizations**: The title indicates that the data represents a weekly average of chassis on the street.

### Chassis Usage Data by Company
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the chassis usage data for various companies.
- **Cell Range**: C4:F33
- **Layout Structure**:
    - **Row Headers Location**: C4:C33
    - **Column Headers Location**: E3:F3
    - **Data Range**: E4:F33
- **Time Series Details**:
    - **Date Range**: W.E. 3/7/2015 to W.E. 3/14/2015
    - **Frequency**: Weekly
- **Key Components**: Horizon Lines, Hamburg Sud - SSA Piers A and J, Maersk, MSC, DCLP, APL, Evergreen - YTI, Hanjin - YTI, Hapag-Lloyd, Hyundai, MOL, NYK, OOCL, GACP, China Shipping, CMA-CGM, COSCO, Evergreen - All Other, Hamburg Sud - All Other, Hanjin - All Other, K Line, Pacific International, Polynesia Line, United Arab Shipping, Wan Hai Lines, Yang Ming Line, Zim Israel Navigation Co., LABP
- **Notes & Customizations**: The data is scaled by 1000.

### DCSZ and Unassigned Chassis Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the chassis usage data for DCSZ and Unassigned chassis.
- **Cell Range**: C35:F37
- **Layout Structure**:
    - **Row Headers Location**: C35:C37
    - **Column Headers Location**: E3:F3
    - **Data Range**: E35:F37
- **Time Series Details**:
    - **Date Range**: W.E. 3/7/2015 to W.E. 3/14/2015
    - **Frequency**: Weekly
- **Key Components**: DCSZ (bare outs, no SS SCAC)**, Unassigned (no SS SCAC or unauthorized)
- **Notes & Customizations**: The data is scaled by 1000.

### Totals & Utilization Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates totals and utilization metrics based on the chassis usage data.
- **Cell Range**: C39:F54
- **Layout Structure**:
    - **Row Headers Location**: C39:C54
    - **Column Headers Location**: E3:F3
    - **Data Range**: E39:F54
- **Time Series Details**:
    - **Date Range**: W.E. 3/7/2015 to W.E. 3/14/2015
    - **Frequency**: Weekly
- **Key Components**: Total Chassis on the Street, Pool of Pools Fleet, Total Street Utilization (incl. DCSZ and unassigned), DCLP Fleet, GACP Fleet, DCLI-GACP Fleet, TRAC-GACP Fleet, LABP Fleet, DCLP Street Utilization, GACP Street Utilization, DCLI-GACP Street Utilization, TRAC-GACP Street Utilization, LABP Street Utilization
- **Notes & Customizations**: Some data is scaled by 1000, while utilization is a percentage.

### Footnotes
- **Section Type**: Notes
- **Description & Purpose**: Provides additional context and explanations for the data.
- **Cell Range**: C56:C57
- **Layout Structure**:
    - **Row Headers Location**: C56:C57
    - **Column Headers Location**: N/A
    - **Data Range**: N/A
- **Time Series Details**: N/A
- **Key Components**: * Reflects chassis with gated-out status by day by steamship line scac, ** Generally, DCSZ is used as the steamship scac when the chassis gates out bare with no container
- **Notes & Customizations**: These footnotes clarify the meaning of certain data points and abbreviations used in the spreadsheet.
