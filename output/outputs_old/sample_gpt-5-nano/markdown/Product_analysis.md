## 1. Spreadsheet Overview
- **Sheet Name**: Product
- **Key Sections Identified**:
  - Product Operating Expenses Summary (product-level operating expense P&L)
  - Date Series Definition & Metadata (monthly time axis used by the sheet)

## 2. Detailed Section Analysis

### Product Operating Expenses Summary
- **Section Type**: Custom P&L
- **Description & Purpose**: A product-level operating expenses summary used to analyze cost drivers and profitability for each product line. This section aggregates and presents the major cost categories under operating expenses, enabling tracking of total product costs, people costs, and category-level drivers across a monthly time axis.
- **Cell Range**: B5:Q397
- **Time Series Horizon**:
  - **Dates Location**: Dates are defined in the header row range T2:FS2.
  - **Date Range**: Monthly series from 2015-01 to 2027-12.
  - **Frequency**: Monthly
- **Key Components**: Major cost clusters and sub-clusters that structure the section (high-level only):
  - Total Product Expense (summary aggregate)
  - Product People Costs (including wages, salaries, and related costs)
  - Wages and Product Wages
  - Product Salaries Working Abroad
  - Holiday Pay, Sick Leave, and other holiday-related costs
  - Bonuses, Benefits, Payroll Taxes
  - Capitalized wages and related R&D expenditures (Capitalized Wages, Capitalized Outsourced R&D, Capitalized R&D)
  - General & Admin and Product General & Admin (Total Product General & Admin)
  - Travel, Entertainment, Meals, and related travel costs
  - Marketing, Advertising, and other product-specific costs
  - Utilities, Rent, CAM, IT/Data costs, Telecommunications
  - Outsourced R&D, DataFeeds, Software, Professional Services, and other overheads
  - Other Costs (Miscellaneous, Legal Fees, Bank Fees, Penalties, Bad Debt, etc.)
- **Notes & Customizations**:
  - The section is presented with many product-specific line items (prefixed by “Product” in labels) and includes several lines where values are scaled (e.g., scale: 1000) to reflect thousands.
  - It is a bespoke, product-focused P&L rather than a standard GAAP-style financial statement.
  - The data layout uses a single time axis across columns I–Q (and related date headers in T2:FS2) to display monthly values for each line item.
- **Dictionary-Resolved Metrics (from the inverted_index in the data)**:
  - % of Wages — Ranges: B17, B22, B26, B32, B38, B46, B50
  - Cost Per Head — Ranges: B42, B55, B60, B79, B84, B96, B104, B109, B116, B121, B126, B131, B152, B161, B170, B179, B188, B197, B206, B215, B237, B242, B247, B252, B257, B262, B269, B274, B279, B284, B289, B294, B299, B304, B309, B319, B324, B332, B337, B346, B354, B359, B364, B369, B376, B381, B386, B391, B396
  - Product Worker Compensation — Ranges: B47, B51, B56, B61
  - Headcount — Ranges: B54, B59, B78, B83, B95, B103, B108, B115, B120, B125, B130, B151, B160, B169, B178, B187, B196, B205, B214, B220, B236, B241, B246, B251, B256, B261, B268, B273, B278, B283, B288, B293, B298, B303, B308, B318, B323, B331, B336, B345, B353, B358, B363, B368, B375, B380, B385, B390, B395

-