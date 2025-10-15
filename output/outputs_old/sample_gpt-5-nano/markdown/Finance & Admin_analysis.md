## 1. Spreadsheet Overview
- **Sheet Name**: Finance & Admin
- **Key Sections Identified**:
  - Finance & Admin Operating Expenses Summary
  - Time Series Definition

## 2. Detailed Section Analysis

### Finance & Admin Operating Expenses Summary
- **Section Type**: Custom P&L
- **Description & Purpose**: This section provides a consolidated view of Finance & Admin operating costs for the period, aggregating wage-related expenses, non-wage admin costs, capitalized items, and a broad set of cost categories. It serves as the primary operating expenses outline used to monitor total spend and the composition of Finance & Admin costs over time.
- **Cell Range**: A5:Q404
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01 to 2027-12
  - **Frequency**: Monthly
- **Key Components**: Major sub-sections that define the structure (high-level view, not every item)
  - Total Finance & Admin Expense (overall)
  - Wages and Finance & Admin wage-related line items
  - Administration & General Costs (non-wage admin costs)
  - Capitalized Wages and Capitalized Outsourced R&D
  - Travel, Recruiting, Relocation, IT/Software, Facilities costs
  - Insurance, Professional Services, Fundraising, Miscellaneous, and other notable cost categories
  - Interactions between headcount metrics (e.g., % of headcount) and cost-per-head metrics
- **Notes & Customizations**:
  - The section is designed as a bespoke, multi-category operating expense view rather than a strict standard P&L; it includes numerous granular line items and cross-references (e.g., “Finance & Admin X” vs. “Total X” lines).
  - Values are typically presented in thousands (scale applied in many numeric ranges), and there are grouping markers (e.g., marker entries in column A) to delineate sections.
  - It integrates headcount and cost-per-head considerations within the broader expenses view, rather than exposing every line item as independent totals.

### Time Series Definition
- **Section Type**: Time Series Definition
- **Description & Purpose**: Documents the time-series configuration used across the sheet, ensuring consistent alignment of data by date. This defines the monthly series that underpins all date-bound financial data, enabling retrieval by period.
- **Cell Range**: T2:FS2
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01 to 2027-12
  - **Frequency**: Monthly
- **Key Components**:
  - ds_1: Monthly series
  - Start date: 2015-01-31
  - Increment: 1 month
  - Pattern: Monthly series from 2015-01 to 2027-12
- **Notes & Customizations**:
  - The defined monthly series begins at 2015-01-31 and continues in one-month increments through 2027-12, as captured in the “Monthly series from 2015-01 to 2027-12” pattern.
  - This section directly references the date range used for the numeric data in the Operating Expenses Summary and related components (dates located in T2:FS2).