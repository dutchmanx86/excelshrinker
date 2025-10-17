## 1. **Sheet Name**: (Assumed to be "Sheet1" as the JSON doesn't explicitly name it)

### Chassis Requirement Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section calculates and displays the chassis requirements for Evergreen PSW LSA/LGB operations under different stress levels (85% and 95%). It uses gate-out data, dwell times, and days in the period to determine the number of chassis needed on the street and in the terminal.
- **Cell Range**: A1:D13
- **Layout Structure**:
    - **Row Headers Location**: Column A (A3:A12)
    - **Column Headers Location**: Row 2 (B2:C2)
    - **Data Range**:
      - B3:C10 (numeric values related to chassis requirements at 85% and 95% stress)
      - D11 (chassis required for terminal)
      - B12:D12 (chassis required for Evergreen)
- **Time Series Details**:
    - **Date Range**: Not explicitly defined in the provided data, but the notes mention "April, May, June 2015" for dwell analysis. This suggests a potential, but limited, time series context.
    - **Frequency**: Not applicable, as the primary focus is on a static calculation based on period data, not a time series.
- **Key Components**: gate-outs in period, dwell, chassis on the street in period, days in period, chassis on street, chassis required for street, percentage of terminal chassis, chassis required for terminal, chassis required for Evergreen.
- **Notes & Customizations**: The analysis considers out-of-service (OOS) chassis and uses a data source of CMS-PC and Evergreen statement of 36k gate moves at Seaside per month. Dwell times are based on analysis of April, May, and June 2015 data.
