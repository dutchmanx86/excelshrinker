## 1. Spreadsheet Overview
- **Sheet Name**: Accrued Wages
- **Key Sections Identified**:
  - Accrued Wages Components Schedule (monthly accruals ledger for wage-related costs)

## 2. Detailed Section Analysis

### Accrued Wages Components Schedule
- **Section Type**: Custom Accruals Schedule
- **Description & Purpose**: A monthly ledger of wage-related accruals and social-cost components. It aggregates various pre-payments and holdbacks (e.g., pension, unemployment, insurance) and combines them to reflect total accrued costs over a defined monthly horizon. The section appears geared toward tracking accruals across multiple months and presenting a USD-equivalent line as a currency reference.
- **Cell Range**: A2:AA14
- **Time Series Horizon**:
  - **Dates Location**: C1:Z1
  - **Date Range**: 2020-01 to 2021-12
  - **Frequency**: Monthly
- **Key Components**:
  - Pension and social insurance accruals (and related pre-payments)
  - Unemployment, accident, and life insurance pre-payments
  - Calculated social costs
  - Pension/Unemployment held from workers
  - Total accruals line (including a labeled total row)
  - USD currency line (currency context foraggregated values)
- **Notes & Customizations**:
  - Numeric data in C2:Z2 and similar ranges are scaled by 1000, implying values are in thousands of the base currency.
  - The section includes a dedicated USD line (USD) and an additional AA12 numeric cell, suggesting a supplementary or currency-specific note outside the main monthly axis.
  - The date axis is defined across C1:Z1, providing the monthly periods for the 2020-01 through 2021-12 window; some cells outside the primary date-aligned grid (e.g., AA column) appear to serve auxiliary context or totals.