## 1. Spreadsheet Overview
- **Sheet Name**: Headcount and Salaries
- **Key Sections Identified**:
  - Headcount and Salaries Summary
  - Headcount Detail
  - Salaries Detail
  - Wages (Income Statement)
  - Wages (Income Statement) - PLUG

## 2. Detailed Section Analysis

### Headcount and Salaries Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: A top-level dashboard of workforce and compensation metrics, providing a concise view of headcount, salary totals, and related averages to support planning and cost visibility.
- **Cell Range**: A5:FS51
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01 to 2027-12
  - **Frequency**: Monthly
- **Key Components**: Core summary metrics such as Headcount, Average Employees, Average Salary, Total Wages, Total Salary, and Total Salary per Head (plus related rate/ratio elements like Salary per Head).
- **Notes & Customizations**: This is a custom HR/finance-focused summary rather than a standard financial P&L; includes notes like “Memo: Average Headcount” and specialized HR cost constructs (e.g., “Total Salary (excl. India)” in related sections).

### Headcount Detail
- **Section Type**: Key Metrics Table (HR Detail)
- **Description & Purpose**: Detailed monthly breakdown of headcount, including period beginnings/ends and additions, enabling granular workforce tracking and trend analysis beyond the high-level summary.
- **Cell Range**: A53:FS119
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01 to 2027-12
  - **Frequency**: Monthly
- **Key Components**: Beginning of Period, Added, End of Period, Headcount counts, Memo: Average Headcount, and related monthly detail blocks.
- **Notes & Customizations**: Contains explicit Headcount Detail blocks interspersed with headers (e.g., “Headcount”) and period-level calculations; includes annotations and monthly spread across multiple ranges.

### Salaries Detail
- **Section Type**: Custom Data Table (Salaries Detail)
- **Description & Purpose**: Comprehensive, monthly breakdown of salaries by category/region/department, designed for cost accounting and deeper salary analysis beyond the summary and basic headcount figures.
- **Cell Range**: A120:FS183
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01 to 2027-12
  - **Frequency**: Monthly
- **Key Components**: Salary line items, totals, per-head aggregates, and multi-block salary data (including category-specific and regional splits; broad range of monthly figures).
- **Notes & Customizations**: Large, multi-block dataset; includes explicit headers like “Salaries Detail,” “Total Salary,” “Total Salary per Head,” and supports India vs. non-India splits in various subsections.

### Wages (Income Statement)
- **Section Type**: Standard P&L
- **Description & Purpose**: Wages as a primary labor-cost line item used in the income statement; provides monthly wage expense figures for financial reporting and variance analysis.
- **Cell Range**: B191:FS191
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01 to 2027-12
  - **Frequency**: Monthly
- **Key Components**: Wages (Income Statement) line values across months; core wage expense figure for the period.
- **Notes & Customizations**: Represents a standard P&L line item, with monthly granularity and typical formatting (scaling and date alignment). No unusual constructs beyond the monthly display.

### Wages (Income Statement) - PLUG
- **Section Type**: Custom Data Table (PLUG)
- **Description & Purpose**: Adjusted/PLUG version of the wages data used to reconcile or align wages with underlying data sources; serves as a correction/adjustment line for the wage expense.
- **Cell Range**: T193:CI193
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01 to 2027-12
  - **Frequency**: Monthly
- **Key Components**: PLUG adjustment values displayed across the monthly range.
- **Notes & Customizations**: Not part of the standard P&L; included specifically for reconciliation/adjustment purposes.