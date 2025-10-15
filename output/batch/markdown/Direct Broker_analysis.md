```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Direct Broker
- **Key Sections Identified**:
    - Overview Section
    - Reads Consumption Section
    - WSI Broker Expense Section
    - Direct Broker Expense Section

## 2. Detailed Section Analysis

### Overview Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides an overview of key metrics related to AlphaSense's cost of goods sold, including expenses, user activity, and page consumption. It allows for tracking performance and identifying trends over time.
- **Cell Range**: B6:Q47
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**:
      - Annual data: `E8:Q23`, `E25:Q27`, `E29:Q29`, `J31:Q31`, `E33:Q33`, `J34:Q34`, `E38:Q40`, `E42:Q43`, `E45:Q47`
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Bernstein Expense, Deutsche Bank Expense, Barclays Expense, HSBC Expense, BOA Expense, UBS Expense, Morgan Stanley Expense, Cowen Expense, Autonomous Expense, Evercore Expense, Citi Expense, Credit Suisse Expense, JP Morgan Expense, Raymond James Expense, RBC Expense, Direct Consumption Expense, FS AMR Expense, Total WSI, Total Active Users, Cost per User, FS BRM Expense, Total Users, Active Users, Active (%), Total Page Reads, Page Reads per Active User, Contribution per User, Total Pool Contribution ($)
- **Notes & Customizations**: The data is scaled by 1000.

### Reads Consumption Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section breaks down the reads consumption by different brokers and direct sources, showing both the absolute consumption and the percentage contribution.
- **Cell Range**: B49:Q95
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**:
      - Annual data: `E51:Q71`, `E75:Q95`
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Bernstein, Deutsche Bank, Barclays, HSBC, BOA, UBS, Morgan Stanley, Cowen, Autonomous, Evercore, Citi , Credit Suisse , JP Morgan , Raymond James, RBC, Direct Broker, FactSet AMR, FactSet RT, Total, Reads Consumption (%), FactSet AMR, FactSet RT, Total
- **Notes & Customizations**: The data is scaled by 1000 for reads consumption and is a percentage for reads consumption (%).

### WSI Broker Expense Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the total pool contribution and the direct broker expense.
- **Cell Range**: B97:Q105
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**:
      - Annual data: `E101:Q105`
- **Time Series Details**:
    - **Date Range**: 2015 to 2027
    - **Frequency**: Annual
- **Key Components**: Total Pool Contribution, Direct Broker Expense, Adjusted Direct Broker Expense
- **Notes & Customizations**: The data is scaled by 1000.

### Direct Broker Expense Section
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a detailed breakdown of the direct broker expense, including strategic investment, usage, consumption, revenue share, expense, minimum, and adjusted expense for each broker.
- **Cell Range**: B103:Q255
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Columns E to Q
    - **Data Range**:
      - Annual data: `E104:Q104`, `E105:Q105`, `E110:Q115`, `E120:Q125`, `E130:Q135`, `E140:Q145`, `E150:Q155`, `E160:Q165`, `E170:Q175`, `E180:Q185`, `E190:Q195`, `E200:Q205`, `E210:Q215`, `E220:Q225`, `E230:Q235`, `E240:Q245`, `E250:Q255`
    - **Data Range**:
      - Monthly data: `J109:Q109`, `J119:Q119`, `J129:Q129`, `J139:Q139`, `J149:Q149`, `J159:Q159`, `J169:Q169`, `J179:Q179`, `J189:Q189`, `J199:Q199`, `J209:Q209`, `J219:Q219`, `J229:Q229`, `J239:Q239`, `J249:Q249`
- **Time Series Details**:
    - **Date Range**: 2015 to 2027 (Annual)
    - **Frequency**: Annual
    - **Date Range**: 2015-01-31 to 2027-12-31 (Monthly)
    - **Frequency**: Monthly
- **Key Components**: Strategic Investment, Usage, Consumption, Revenue Share, Expense, Minimum, Adjusted Expense (repeated for each broker: Bernstein, Deutsche Bank, Barclays, HSBC, BOA, UBS, Morgan Stanley, Cowen, Autonomous, Evercore, Citi, Credit Suisse, JP Morgan, Raymond James, RBC)
- **Notes & Customizations**: The data is scaled by 1000. Some rows have monthly data from column J onwards.
```