## 1. Spreadsheet Overview
- **Sheet Name**: Fleet Sizing
- **Key Sections Identified**:
    - Fleet Sizing Calculation Table
    - Data Source & Assumptions

## 2. Detailed Section Analysis

### Section Name: Fleet Sizing Calculation Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates the required chassis for Evergreen PSW LSA/LGB operations based on gate-outs, dwell times, and stress levels. It aims to determine the optimal fleet size under different utilization scenarios (85% and 95%).
- **Cell Range**: A1:D12
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 1 (Evergreen PSW LSA/LGB), Row 2 (at 85%, at 95%)
    - **Data Range**:
      - B3:C12 (data for 85% and 95% utilization)
      - D7:D12 (additional data, possibly a different calculation or scenario)
- **Time Series Details**:
    - **Date Range**: Not explicitly time-series data, but rather scenario-based calculations.
    - **Frequency**: N/A
- **Key Components**: gate-outs in period, dwell, chassis on the street in period, days in period, chassis on street, stress, chassis required for street, percentage of terminal chassis, chassis required for terminal, chassis required for Evergreen.
- **Notes & Customizations**: The calculations are performed for two different utilization rates (85% and 95%). The scale of some values is in thousands.

### Section Name: Data Source & Assumptions
- **Section Type**: Notes
- **Description & Purpose**: This section provides information about the data sources used for the calculations and the assumptions made in the analysis.
- **Cell Range**: A15:A17
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: None
    - **Data Range**: A15:A17
- **Time Series Details**:
    - **Date Range**: Refers to data from April, May, June 2015 for dwell time analysis.
    - **Frequency**: N/A
- **Key Components**: Data source (CMS-PC and Evergreen statement), OOS (out-of-service) consideration, Dwell analysis period.
- **Notes & Customizations**: This section contains textual descriptions of the data sources and assumptions.
