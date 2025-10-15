## 1. Spreadsheet Overview
- **Sheet Name**: Fin CTRL
- **Key Sections Identified**:
    - Title/Scenario Description
    - Time Series Headers
    - Balance Sheet Support Assumptions
    - Interest Rate Assumptions

## 2. Detailed Section Analysis

### Title/Scenario Description
- **Section Type**: Title/Scenario Description
- **Description & Purpose**: Describes the spreadsheet and the scenario being modeled.
- **Cell Range**: B1:B3
- **Layout Structure**:
    - **Row Headers Location**: Column B, Rows 1-3
    - **Column Headers Location**: N/A
    - **Data Range**: B1:B3
- **Time Series Details**: N/A
- **Key Components**: AlphaSense, Inc., Financial Statements CTRL, 1 - Base - $25mm
- **Notes & Customizations**: This section provides context for the entire spreadsheet.

### Time Series Headers
- **Section Type**: Time Series Headers
- **Description & Purpose**: Defines the time periods for the financial data. Contains both annual and monthly time series.
- **Cell Range**: B6:FS8
- **Layout Structure**:
    - **Row Headers Location**: B6, B7
    - **Column Headers Location**: E6:Q6 (Years), T6:FS6 (Months), T8:FS8 (Months)
    - **Data Range**:
      - Annual data: E6:Q6
      - Monthly data: T6:FS6, T8:FS8
- **Time Series Details**:
    - Annual: 2015 to 2027
        - Frequency: Annual
    - Monthly: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Year, Month
- **Notes & Customizations**: Contains both annual and monthly time series data.

### Balance Sheet Support Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains key assumptions used to support the balance sheet projections, such as Days Sales Outstanding, Capital Expenditures, Accounts Payable Days, etc.
- **Cell Range**: A11:FS136
- **Layout Structure**:
    - **Row Headers Location**: Column B, Rows 13, 20, 27, 34, 41, 48, 55, 62, 69, 76, 83, 90, 97, 104, 111, 118, 125, 132
    - **Column Headers Location**: E6:Q6 (Years), T6:FS6 (Months)
    - **Data Range**:
      - Annual data: E13:Q13, I20:Q20, I21:Q24, I27:Q31, E34:Q34, I35:Q38, BX41:FS41, BX42:FS45, E48:Q48, I49:Q52, I55:Q55, I56:Q59, F62:Q62, I63:Q66, H69:Q69, I70:Q73, I76:Q76, F83:Q83, I84:Q87, E90:Q90, I91:Q94, I97:Q97, E104:Q104, BX105:FS105, BX106:FS108, E111:Q111, BX112:FS112, BX113:FS115, E118:Q118, BX119:FS119, BX120:FS122, E125:Q125, BX126:FS126, BX127:FS129, E132:Q132, BX133:FS133, BX134:FS136
      - Monthly data: T13:FS13, T20:FS20, T27:FS27, T34:FS34, T48:FS48, BX55:FS55, U62:BW62, CB62, CN62, CZ62, DL62, DX62, EJ62, EV62, FH62, T69:FS69, CB76, CN76, CZ76, DL76, DX76, EJ76, EV76, FH76, T83:FS83, U83:BW83, CB83, CN83, CZ83, DL83, DX83, EJ83, EV83, FH83, T90:FS90, BX97:FS97, T104:FS104, T111:FS111, T118:FS118, T125:FS125, T132:FS132
- **Time Series Details**:
    - Annual: 2015 to 2027
        - Frequency: Annual
    - Monthly: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Days Sales Outstanding, Prepaid Expenses, Capital Expenditures, Accounts Payable Days Payable Outstanding, Commissions Payable, Accrued Expenses, Accrued Commissions, Accrued Wages, Accrued Holiday Pay, Accrued Interest, Payroll Taxes Payable, Sales Taxes Payable, Deferred Commissions Growth, Tekes - 14887, Tekes - 15118, Tekes - 14560, Tekes - 14223, Tekes - 15543
- **Notes & Customizations**: This section contains a mix of percentages, days outstanding, and other metrics used to drive the balance sheet. Many rows have both annual and monthly data.

### Interest Rate Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains assumptions related to interest rates.
- **Cell Range**: A139:FS188
- **Layout Structure**:
    - **Row Headers Location**: Column B, Rows 139, 146, 152, 158, 160, 166, 172, 178, 184
    - **Column Headers Location**: E6:Q6 (Years), T6:FS6 (Months)
    - **Data Range**:
      - Annual data: I139:Q139, I140:Q143, I146:Q146, I147:Q150, E160:Q160, E161:Q164, I166:Q166, I167:Q170, E172:Q172, I173:Q176, E178:Q178, I179:Q182, E184:Q184, J185:Q188
      - Monthly data: T139:FS139, T146:FS146, T152:FS152, T158:FS158, T160:FS160, T166:FS166, T172:FS172, T178:FS178, T184:FS184
- **Time Series Details**:
    - Annual: 2015 to 2027
        - Frequency: Annual
    - Monthly: 2015-01-31 to 2027-12-31
        - Frequency: Monthly
- **Key Components**: Interest Rate, Interest Rate - Admin Fee, Interest Rate on Cash Account, Percent of Cash in Account, Effective Commission Rate, Day Sales Outstanding, Credit Card Payable, Target Hit Rate, LIBOR
- **Notes & Customizations**: This section defines the interest rate assumptions used in the model.
