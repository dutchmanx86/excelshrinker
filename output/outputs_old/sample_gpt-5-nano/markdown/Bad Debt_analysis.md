## 1. Spreadsheet Overview
- **Sheet Name**: Bad Debt
- **Key Sections Identified**:
  - AFDA Reconciliation (Bad Debt)

## 2. Detailed Section Analysis

### AFDA Reconciliation (Bad Debt)
- **Section Type**: Balance Sheet
- **Description & Purpose**: A monthly reconciliation of the Allowance for Doubtful Accounts (AFDA) and related AR balances, spanning beginning balances, write-offs, adjustments, and end-of-period AFDA levels. The section supports tracking and minting the AFDA target against AR activity to determine required reserves.
- **Cell Range**: A5:CS23
- **Time Series Horizon**:
  - **Dates Location**: B4:CS4
  - **Date Range**: January 2020 to December 2027
  - **Frequency**: Monthly
- **Key Components**: 
  - Beginning AFDA balances (WP vs. Intacct)
  - Invoices written-off/collected
  - AFDA balance before adjustment
  - A/R ending balance per Intacct
  - AFDA as a percentage of A/R to be maintained
  - 3.18% of current A/R (threshold)
  - Less: AFDA balance before adjustment
  - Amount to be added to AFDA
  - AFDA end balance per WP
  - ADFA end balance per Intacct
  - Higher of specific allowance or 3.18% of AR (calculation rule)
- **Notes & Customizations**:
  - This is a custom reconciliation structure that cross-referencesWorkday (WP) vs. Intacct balances and applies a threshold of 3.18% of AR, using the higher of the calculated specific allowance or the threshold.
  - Many numeric cells are stored with a scale of 1000 (i.e., values represent thousands), so retrieval should account for thousands scaling. 
  - The date series is defined as a monthly series from 2020-01 to 2027-12 (ds_1), which drives the column headers in B4:CS4. 
  - Additional reference cells include A7 and A20 (Difference) used for calculating or validating differences, though they are not part of the primary A5:CS23 block.