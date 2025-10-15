## 1. Spreadsheet Overview
- **Sheet Name**: Additional FDS Content
- **Key Sections Identified**:
  - FDS RT Metrics & Bucketed Spend
  - Transcript Usage & Related Costs
  - M&A Usage & Related Costs

## 2. Detailed Section Analysis

### FDS RT Metrics & Bucketed Spend
- **Section Type**: Custom Metrics Table
- **Description & Purpose**: Consolidates RT (Real-Time or “RT” qualifier in this context) expense data and user counts, organized by bucketed spend ranges and related adjustments. This section serves as a high-level view of cost per user across predefined buckets, including totals, discounts, and minimum spend constructs that feed into performance and spend optimization analyses.
- **Cell Range**: A4:DE48
- **Time Series Horizon**:
  - **Dates Location**:
    - ds_1 (annual header): N1:DE1
    - ds_2 (annual header): E2:L2
    - ds_3 (monthly header): N2:DE2
  - **Date Range**:
    - ds_1: 2020-01-01 to 2027-01-01 (annual)
    - ds_2: 2020-01-01 to 2027-01-01 (annual)
    - ds_3: 2020-01-31 to 2027-12-31 (monthly)
  - **Frequency**:
    - ds_1: Annual
    - ds_2: Annual
    - ds_3: Monthly
- **Key Components**: 
  - FDS RT Expense (label and numeric values)
  - Total FDS RT Users
  - Bucketing structure (e.g., Up to 6000; 2000–425000; several multi-thousand bands)
  - Discount and adjustment-related metrics (Discount (%), Discount Adjusted FDS RT Excess Expense, Total Discount Adjusted FDS RT Excess Expense)
  - Minimum Excess Spend concepts and buckets
- **Notes & Customizations**: This section adopts a non-standard bucketed framework with multiple overlapping metrics (excess expense, adjustments, bucket-based spend ranges). It is customized beyond a traditional P&L and appears to be a dedicated analytic module for FDS RT spend optimization and user-level cost attribution.

### Transcript Usage & Related Costs
- **Section Type**: Custom Metrics Table
- **Description & Purpose**: Encapsulates the usage and cost dynamics for transcript-related data (Factset Transcripts). Includes a header indicator for transcripts, a total transcripts user count, and subsequent bucketed cost/data lines that likely feed into usage-based cost analyses for transcripts.
- **Cell Range**: A50:DE84 (covering the initial transcripts header and the early, bucketed transcript data up to the 84th row)
- **Time Series Horizon**:
  - **Dates Location**:
    - ds_1 (annual header): N1:DE1
    - ds_2 (annual header): E2:L2
    - ds_3 (monthly header): N2:DE2
  - **Date Range**:
    - ds_1: 2020-01-01 to 2027-01-01 (annual)
    - ds_2: 2020-01-01 to 2027-01-01 (annual)
    - ds_3: 2020-01-31 to 2027-12-31 (monthly)
  - **Frequency**:
    - ds_1: Annual
    - ds_2: Annual
    - ds_3: Monthly
- **Key Components**:
  - “Factset Transcripts” labeling
  - Total FDS Transcript Users
  - Transcript expenditure/cost buckets
- **Notes & Customizations**: This block is tailored to transcript-related analytics and costs, distinguished from standard product spend by its focus on transcript usage and related expenses.

### FDS M&A Usage & Related Costs
- **Section Type**: Custom Metrics Table
- **Description & Purpose**: Aggregates M&A-related user activity and costs within the FDS suite. Includes a dedicated label for Factset M&A, a total FDS M&A Users metric, and an associated expense/excess-cost section that informs M&A-related spend optimization and attribution.
- **Cell Range**: A82:DE111
- **Time Series Horizon**:
  - **Dates Location**:
    - ds_1 (annual header): N1:DE1
    - ds_2 (annual header): E2:L2
    - ds_3 (monthly header): N2:DE2
  - **Date Range**:
    - ds_1: 2020-01-01 to 2027-01-01 (annual)
    - ds_2: 2020-01-01 to 2027-01-01 (annual)
    - ds_3: 2020-01-31 to 2027-12-31 (monthly)
  - **Frequency**:
    - ds_1: Annual
    - ds_2: Annual
    - ds_3: Monthly
- **Key Components**:
  - “Factset M&A” label
  - Total FDS M&A Users
  - Total FDS M&A Excess Expense (and related buckets)
- **Notes & Customizations**: This section specifically supports M&A-related analytics and expense attribution, distinct from the RT and Transcript modules. It consolidates M&A user counts with their corresponding excess expense figures.