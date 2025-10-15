## 1. Spreadsheet Overview
- **Sheet Name**: ARR Looker
- **Key Sections Identified**:
    - Header
    - Quarterly ARR Data by Segment

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains labels for the data table, including segment names and date labels.
- **Cell Range**: A1:Q2
- **Layout Structure**:
    - **Row Headers Location**: A2, C2
    - **Column Headers Location**: C1, E1:I1, N1:Q1, D2:J2, O2:Q2
    - **Data Range**: None (Header only)
- **Time Series Details**:
    - **Date Range**: FY2017-Q4 to FY2022-Q3
    - **Frequency**: Quarterly
- **Key Components**: Segment, Date Fiscal Quarter, Total ARR, Churn, Downgrade, Expansion, Initial Sale, Partner, Corporate, Commercial, Strategic
- **Notes & Customizations**: The header defines the structure of the ARR data table below.

### Quarterly ARR Data by Segment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains the quarterly ARR data broken down by segment (Corporate, Commercial, Strategic) and by closed transaction type.
- **Cell Range**: A3:Q177
- **Layout Structure**:
    - **Row Headers Location**: A3:A177
    - **Column Headers Location**: B2:Q2, C1:I1
    - **Data Range**:
      - Quarterly data (Segment): E3:I10, E12:I19, D20:I28, D29:I37, D38:I46, D47:I55, D56:I64, D65:I73, D74:I82, D83:I91, D92:I100, D101:I109, D110:I118, D119:I127, D128:I136, D137:I145, D146:I154, D155:I163, D164:I172, D173:I177
      - Quarterly data (Corporate/Commercial/Strategic): O3:Q10, O3:Q10, O3:Q10, O3:Q10, O3:Q10, O3:Q10, O3:Q10, O3:Q10
- **Time Series Details**:
    - **Date Range**: FY2017-Q4 to FY2022-Q3
    - **Frequency**: Quarterly
- **Key Components**: FY2017-Q4, FY2018-Q1, FY2018-Q2, FY2018-Q3, FY2018-Q4, FY2019-Q1, FY2019-Q2, FY2019-Q3, FY2019-Q4, FY2020-Q1, FY2020-Q2, FY2020-Q3, FY2020-Q4, FY2021-Q1, FY2021-Q2, FY2021-Q3, FY2021-Q4, FY2022-Q1, FY2022-Q2, FY2022-Q3, Corporate, Commercial, Strategic, Churn, Downgrade, Expansion, Initial Sale, Partner
- **Notes & Customizations**: Data is scaled by 1000. There are two distinct sections of data: one for the combined segments (Corporate, Commercial, Strategic) and another for the individual segments.
