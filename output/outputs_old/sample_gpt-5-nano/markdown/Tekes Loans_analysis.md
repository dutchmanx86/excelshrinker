## 1. Spreadsheet Overview
- **Sheet Name**: Tekes Loans
- **Key Sections Identified**:
  - Opening Principal Balance
  - Principal Payment
  - Accrued Interest
  - Interest Payment
  - Principal Payment FX Rate

## 2. Detailed Section Analysis

### Opening Principal Balance
- **Section Type**: Debt Schedule (Amortization) Balance Series
- **Description & Purpose**: Represents the opening loan principal balance values aligned to the defined monthly time periods, serving as the seed for the amortization/cash-flow tracking across the loan life.
- **Cell Range**: B2, B12, B23, B36, B47
- **Time Series Horizon**:
  - **Dates Location**: C1:AY1
  - **Date Range**: 2019-12 to 2023-12
  - **Frequency**: Monthly
- **Key Components**: Opening balance values by period (start-of-period principal)
- **Notes & Customizations**: Data points are represented at discrete rows in column B rather than a continuous row sequence; part of a broader debt schedule with other lines feeding the cash-flow structure.

### Principal Payment
- **Section Type**: Debt Schedule (Amortization) Principal Payments
- **Description & Purpose**: Captures the principal portion of debt serviced in each monthly period, driving loan payoff and balance reduction.
- **Cell Range**: B3, B13, B24, B37, B48
- **Time Series Horizon**:
  - **Dates Location**: C1:AY1
  - **Date Range**: 2019-12 to 2023-12
  - **Frequency**: Monthly
- **Key Components**: Principal repayment per period; interacts with opening balance and interest to determine balance progression
- **Notes & Customizations**: Presented as discrete period points within the same debt-amortization structure; linked to the FX-rate component for any currency adjustments.

### Accrued Interest
- **Section Type**: Debt Schedule (Interest Accrual)
- **Description & Purpose**: Tracks interest that accrues on outstanding principal between payment dates, providing a basis for later cash interest calculations.
- **Cell Range**: B4, B14, B25, B38, B49
- **Time Series Horizon**:
  - **Dates Location**: C1:AY1
  - **Date Range**: 2019-12 to 2023-12
  - **Frequency**: Monthly
- **Key Components**: Interest accrual amounts per period
- **Notes & Customizations**: Works in concert with the cash-interest line; separate from actual cash payments.

### Interest Payment
- **Section Type**: Debt Schedule (Interest Cash Outflows)
- **Description & Purpose**: Records the cash interest payments due in each monthly period, representing the actual outflow for interest.
- **Cell Range**: B5, B15, B26, B39, B50
- **Time Series Horizon**:
  - **Dates Location**: C1:AY1
  - **Date Range**: 2019-12 to 2023-12
  - **Frequency**: Monthly
- **Key Components**: Interest cash payments per period
- **Notes & Customizations**: Distinct from accrual line; reflects actual cash movement.

### Principal Payment FX Rate
- **Section Type**: FX Adjustment for Principal Payments
- **Description & Purpose**: Applies currency conversion/fx-rate adjustments to principal payments, capturing translation effects in multi-currency loan scenarios.
- **Cell Range**: B7, B17, B28, B41, B52
- **Time Series Horizon**:
  - **Dates Location**: C1:AY1
  - **Date Range**: 2019-12 to 2023-12
  - **Frequency**: Monthly
- **Key Components**: FX rate per period affecting principal payment values
- **Notes & Customizations**: Represents currency translation impact on principal; separate from nominal principal values, indicating a non-standard adjustment layer within the debt schedule.