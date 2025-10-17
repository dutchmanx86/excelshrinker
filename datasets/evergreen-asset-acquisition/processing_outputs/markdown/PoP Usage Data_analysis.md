## 1. **Sheet Name**: (Assumed to be Sheet1 based on common convention, since the JSON doesn't explicitly name the sheet)

### Chassis On-Street Analysis
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the number of chassis on the street (i.e., in use) by various steamship lines and aggregates them to calculate total chassis on the street and utilization rates. It provides insights into chassis usage and fleet management.
- **Cell Range**: C2:F57
- **Layout Structure**:
    - **Row Headers Location**: Column C (C4:C54)
    - **Column Headers Location**: Row 3 (E3:F3)
    - **Data Range**: E4:F54
- **Time Series Details**:
    - **Date Range**: 2015-03-07 to 2015-03-14
    - **Frequency**: Weekly
- **Key Components**:
    - Chassis counts for various steamship lines (Horizon Lines, Hamburg Sud, Maersk, MSC, etc.)
    - Total Chassis on the Street
    - Pool of Pools Fleet
    - Total Street Utilization
    - DCLP/GACP Fleet and Utilization
- **Notes & Customizations**:
    - The data reflects chassis with a gated-out status by steamship line.
    - DCSZ is used as the steamship SCAC when the chassis gates out bare with no container.
    - There are some italicized values in the data range.
