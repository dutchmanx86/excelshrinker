## 1. Spreadsheet Overview
- **Sheet Name**: Marketing
- **Key Sections Identified**:
    - Header
    - Marketing Operating Expenses Summary
    - Marketing People Costs Breakdown
    - Marketing Other Employee Costs Breakdown
    - Marketing Travel Costs Breakdown
    - Marketing Facility Costs Breakdown
    - Marketing Expenses Breakdown
    - Marketing General & Admin Breakdown
    - Marketing Other Costs Breakdown

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the company name, report title, and budget information.
- **Cell Range**: B2:FS4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E3:FS3 (Years and Months)
    - **Data Range**: E3:H3, I3:Q3, T3:FS3
- **Time Series Details**:
    - Annual: E3 to Q3 (Years not specified in JSON, but present)
    - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**: Annual, Monthly
- **Key Components**: Company Name, Report Title, Budget Amount
- **Notes & Customizations**: Contains both annual and monthly time series.

### Marketing Operating Expenses Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of total marketing expenses.
- **Cell Range**: A6:Q10
- **Layout Structure**:
    - **Row Headers Location**: A6, B6, A10, B10
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I8:Q8, I10:Q10
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Total Marketing Expense, Total Marketing People Costs
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing People Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of marketing people costs, including wages, benefits, and related expenses.
- **Cell Range**: A10:Q62
- **Layout Structure**:
    - **Row Headers Location**: B13:B62
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I14:Q14, I15:Q15, I19:Q19, I24:Q24, I28:Q28, I34:Q34, I36:Q36, I40:Q40, I44:Q44, I48:Q48, I52:Q52, I57:Q57, I62:Q62
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Sick Leave, Bonus, Benefits, Work Compensation, Payroll Taxes, Finish Side Costs, Share Based Compensation
- **Notes & Customizations**: Uses a scale of 1000 for the values. Includes "% of Wages" calculations.

### Marketing Other Employee Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of other employee costs, such as phone service, internet, and home office expenses.
- **Cell Range**: A113:Q133
- **Layout Structure**:
    - **Row Headers Location**: B115:B133
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I118:Q118, I123:Q123, I128:Q128, I133:Q133
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Celluar Phone Service, Home Internet Service, Home Office Phone, Home Office
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Travel Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of travel costs, including airfare, auto, lodging, and meals.
- **Cell Range**: A145:Q217
- **Layout Structure**:
    - **Row Headers Location**: B151:B217
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I154:Q154, I163:Q163, I172:Q172, I181:Q181, I190:Q190, I199:Q199, I217:Q217
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals / Entertainment, Business Meals / Entertainment
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Facility Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of facility costs, including rent, CAM, and utilities.
- **Cell Range**: A229:Q264
- **Layout Structure**:
    - **Row Headers Location**: B231:B264
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I234:Q234, I239:Q239, I244:Q244, I249:Q249, I254:Q254, I259:Q259, I264:Q264
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Expenses Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of marketing expenses, including advertising, research, and events.
- **Cell Range**: A266:Q299
- **Layout Structure**:
    - **Row Headers Location**: B268:B299
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I271:Q271, I274:Q274, I277:Q277, I280:Q280, I283:Q283, I288:Q288, I291:Q291, I294:Q294, I299:Q299
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing General & Admin Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of general and administrative expenses.
- **Cell Range**: A301:Q330
- **Layout Structure**:
    - **Row Headers Location**: B303:B330
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I304:Q304, I309:Q309, I314:Q314, I322:Q322, I327:Q327, I330:Q330
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Insurance, Payroll & Benefit Admin, Postage & Delivery, Furniture, Hardware, Software
- **Notes & Customizations**: Uses a scale of 1000 for the values.

### Marketing Other Costs Breakdown
- **Section Type**: Custom P&L
- **Description & Purpose**: Details the breakdown of other costs, including legal fees, data feeds, and web services.
- **Cell Range**: A360:Q385
- **Layout Structure**:
    - **Row Headers Location**: B362:B385
    - **Column Headers Location**: I3:Q3 (Years)
    - **Data Range**: I365:Q365, I370:Q370, I375:Q375, I380:Q380, I385:Q385
- **Time Series Details**:
    - Annual: Years not specified, but present in columns I to Q.
    - **Frequency**: Annual
- **Key Components**: Legal Fees, DataFeeds, Web Service, Penalties, Bad Debt
- **Notes & Customizations**: Uses a scale of 1000 for the values.
