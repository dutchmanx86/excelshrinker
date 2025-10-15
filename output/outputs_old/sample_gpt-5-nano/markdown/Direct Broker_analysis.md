## 1. Spreadsheet Overview
- **Sheet Name**: Direct Broker
- **Key Sections Identified**:
  - Overview & Time-Series Grid
  - Broker Expense Detail
  - WSI Metrics & Page Usage
  - Strategic Investments & Consolidated Financials

## 2. Detailed Section Analysis

### Overview & Time-Series Grid
- **Section Type**: Time-Series Data Grid
- **Description & Purpose**: This top section anchors the sheet with a concise overview and the global time-series axis used by the rest of the workbook. It provides the high-level context, navigation anchors, and initial metric scaffolding that align to the monthly date axis defined elsewhere in the sheet.
- **Cell Range**: A5:P70
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2
  - **Date Range**: 2015-01-31 to 2027-12 (Monthly series)
  - **Frequency**: Monthly
- **Key Components**: Overview label, high-level metrics, foundational headings that precede detailed sections (e.g., “Overview,” and initial metric rows such as Total/Active metrics and related summaries).
- **Notes & Customizations**: The section serves as a general header and context zone rather than a full P&L; it establishes the monthly axis and anchors subsequent detailed sections. Some labels may appear with trailing spaces or minor naming inconsistencies that are resolved in downstream mappings.

### Broker Expense Detail
- **Section Type**: Expense Data Table
- **Description & Purpose**: A detailed tabulation of broker-related costs and related expense components, including direct broker costs, per-broker totals, and associated sub-allocations. This section acts as the primary ledger for broker-related spend and its breakdowns across multiple brokers and expense lines.
- **Cell Range**: A24:P104
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2
  - **Date Range**: 2015-01 to 2027-12 (Monthly)
  - **Frequency**: Monthly
- **Key Components**: 
  - Direct Broker Expense
  - Individual broker expense lines (e.g., Bernstein Expense, Deutsche Bank Expense, Barclays Expense, HSBC Expense, etc.)
  - Peripheral expense lines (e.g., FS AMR Expense, FS BRM Expense, WSI-related expense lines, Direct Consumption Expense, Strategic Investment-related entries, and miscellaneous aggregates such as Total WSI, Total Active Users, Cost per User)
  - Breakouts such as Direct Broker Expense, Adjusted Direct Broker Expense, and various aggregated and per-broker labels
- **Notes & Customizations**: This section aggregates a large set of broker-related metrics and includes several multi-row blocks (e.g., “Strategic Investment” spans multiple separate ranges in the sheet). Some broker labels include minor formatting irregularities (e.g., trailing spaces in keys like "Citi " and "Credit Suisse "), which are harmonized for retrieval. The data is aligned to the monthly time axis defined in the overview.

### WSI Metrics & Page Usage
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Focused on usage and engagement metrics for the WSI (Reads/Usage) domain, including total users, active users, page reads, reads per active user, and engagement-related contributions. This section complements the expense data by illustrating how usage correlates with cost components.
- **Cell Range**: A105:P164
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2
  - **Date Range**: 2015-01 to 2027-12 (Monthly)
  - **Frequency**: Monthly
- **Key Components**:
  - WSI Page Consumption
  - Total Users
  - Active Users
  - Active (%)
  - Total Page Reads
  - Page Reads per Active User
  - Contribution per User
  - Total Pool Contribution ($)
  - Reads Consumption
  - Reads Consumption (%)
- **Notes & Customizations**: The block includes measures scaled in thousands for many columns and contains several derived engagement metrics (e.g., reads per user, consumption percentages). The structure emphasizes the relationship between user activity and the associated cost/expense lines in the broker expense context.

### Strategic Investments & Consolidated Financials
- **Section Type**: Consolidated Metrics Table
- **Description & Purpose**: This final section aggregates strategic investment activity and related KPI-style metrics. It collects multi-row blocks of the “Strategic Investment” component along with related usage, consumption, revenue share, expense, minimums, and adjusted expense figures. The aim is to present a consolidated view of investments and the corresponding financial impacts across time.
- **Cell Range**: A165:P254
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2
  - **Date Range**: 2015-01 to 2027-12 (Monthly)
  - **Frequency**: Monthly
- **Key Components**:
  - Strategic Investment (multi-block across several rows)
  - Usage, Consumption, Revenue Share, Expense, Minimum, Adjusted Expense
  - Other related totals and aggregates that feed into the overall forecast or KPI dashboard
- **Notes & Customizations**: The section is inherently multi-block and multi-metric, reflecting a customized consolidation of investments and associated metrics rather than a standard one-column-per-period style. The organization supports trend analysis and scenario planning across the defined monthly horizon.