## 1. Spreadsheet Overview
- **Sheet Name**: Detailed Income Statement
- **Key Sections Identified**:
    - Header
    - Income Statement
    - Personnel Cost Breakdown

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and column headers.
- **Cell Range**: A1:E3
- **Layout Structure**:
    - **Row Headers Location**: A1:D3
    - **Column Headers Location**: E3
    - **Data Range**: N/A
- **Time Series Details**: None
- **Key Components**: "Income Statement", "Account Group", "Account Number", "Account Name", "Account Type"
- **Notes & Customizations**: Standard header information.

### Income Statement
- **Section Type**: Standard P&L
- **Description & Purpose**: Presents the company's financial performance over a period of time, detailing revenue, cost of service, expenses, and ultimately, net income.
- **Cell Range**: A5:BV157
- **Layout Structure**:
    - **Row Headers Location**: Column A and D
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `F6:R157`
      - Monthly data: `S6:BV157`
- **Time Series Details**:
    - **Date Range**:
      - Annual: Assuming F3:R3 represents a range of years, e.g., 2015 to 2027. The exact years are not specified in the provided data.
      - Monthly: Assuming S3:BV3 represents a range of months. The exact months are not specified in the provided data, but based on the "Actual" label in S2:BV2, it's likely a series of monthly "Actual" values.
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Revenue, Total Revenue, Cost of Service, Total COS, Gross Profit, Expenses, Total Expenses, Other Income, Total Other Income, Taxes, Total Taxes, Interest, Interest Net, Net Income/(loss)
- **Notes & Customizations**: The data is presented in thousands (scale = 1000). There are sections for "People Costs", "Travel Costs", "Facilities Costs", "Marketing Costs", "General and Administrative Costs", "Legal Costs", "Other Costs", and "Depreciation & Amortization" within the Expenses section.

### Personnel Cost Breakdown
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of personnel costs, including salaries, commission, bonus, benefits, recruiting fees, relocation, contractors, and outsourced R&D.
- **Cell Range**: D158:AM167
- **Layout Structure**:
    - **Row Headers Location**: Column D
    - **Column Headers Location**: Row 158
    - **Data Range**: `F159:AM167`
- **Time Series Details**:
    - **Date Range**: Assuming F158:AM158 represents a range of months. The exact months are not specified in the provided data.
    - **Frequency**: Monthly
- **Key Components**: Salaries, Commission, Bonus, Benefits, Recruiting Fees, Relocation, Contractors, Outsourced R&D, Payroll Taxes, Worker Comp
- **Notes & Customizations**: The data is presented in thousands (scale = 1000).
