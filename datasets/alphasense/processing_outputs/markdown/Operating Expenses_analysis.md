```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Operating Expenses
- **Key Sections Identified**:
    - Operating Expenses Summary
    - Operating Expenses Detail

## 2. Detailed Section Analysis

### Section Name (Operating Expenses Summary)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of operating expenses, including key categories like People Costs, Travel, Facilities Costs, Marketing, and General & Administrative. It allows for quick overview and comparison of expense trends over time.
- **Cell Range**: B6:FS21
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E11:Q21` (numeric values for annual periods)
      - Monthly data: `T11:FS21` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Operating Expenses, People Costs, Other Employee Costs, Travel, Facilities Costs, Rental Income, Marketing, General and Administrative, Legal, Other Costs, Total Operating Expenses, % YoY Growth.
- **Notes & Customizations**: Expenses are presented in thousands. The "% YoY Growth" calculation starts from column F (2016) for annual data and AF (2016-01-31) for monthly data.

### Section Name (Operating Expenses Detail)
- **Section Type**: Custom P&L
- **Description & Purpose**: Provides a detailed breakdown of operating expenses, drilling down into sub-categories within each major expense area (e.g., People Costs broken down into Salaries, Benefits, Payroll Taxes, etc.). This section allows for granular analysis of cost drivers.
- **Cell Range**: B23:FS231
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Annual data: `E26:Q231` (numeric values for annual periods)
      - Monthly data: `T26:FS231` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Annual: 2015 to 2027
      - Monthly: 2015-01-31 to 2027-12-31 (T3:FS3). Anchor points: T3=2015-01-31, AF3=2016-01-31, AR3=2017-01-31, BD3=2018-01-31, BP3=2019-01-31, CB3=2020-01-31, CN3=2021-01-31, CZ3=2022-01-31, DL3=2023-01-31, DX3=2024-01-31, EJ3=2025-01-31, EV3=2026-01-31, FH3=2027-01-31
    - **Frequency**:
      - Annual
      - Monthly
- **Key Components**: Wages, Salaries Working Abroad, Holiday Pay, Additional Holiday Pay, Sick Leave, Commission, Stock Based Compensation, Bonus, Benefits, Payroll Taxes, Recruiting Fees, Contractors, Capitalized Wages, Cellular Phone Service, Home Internet Service, Home Office Phone, Home Office, Membership Dues, Subscriptions, Airfare/Train, Auto/Cab, Mileage, Lodging, Travel Internet, Employee Meals, Daily Meal Allowance When Abroad, Business Meals, Internal Events, Rent, CAM, Repairs & Maintenance, Utilities, Telephone, Computer & Internet, Advertising & Promotion, Other Marketing, Omarketing Research, Marketing Events, Public Relations, Paid Search, Paid Social, Paid Display, Paid SWAG, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising Fees, Miscellaneous, DataFeeds, Web Service, Penalties, Bad Debt, Headcount.
- **Notes & Customizations**: Expenses are presented in thousands. Some rows have additional calculations or percentages (e.g., "% of Wages", "Marketing Cost per Booking"). There are some rows with split monthly data (e.g. E27:Q27, T27:CI27, CJ27:FS27).
```