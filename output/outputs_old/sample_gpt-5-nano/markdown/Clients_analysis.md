## 1. Spreadsheet Overview
- **Sheet Name**: Clients
- **Key Sections Identified**:
  - Clients Summary
  - Client Detail - Financial
  - Client Detail - Corporate
  - Client Detail - Other

## 2. Detailed Section Analysis

### Clients Summary
- **Section Type**: `Key Metrics Table`
- **Description & Purpose**: Provides the high-level view of the client base and churn-related ARR metrics over time. Serves as the top-level snapshot of how many clients are present, how many are gained or lost, and the associated ARR impact due to churn and new bookings. This section anchors the monthly time series for the overall client business activity.
- **Cell Range**: A5:FR29
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2
  - **Date Range**: January 2015 through December 2027
  - **Frequency**: Monthly
- **Key Components**: Beginning/Added/Ending/Lost clients; churn split metrics; new booked ARR (by new clients); churned ARR (by lost clients); ARR attributable to churn; percentage of churn attributable to lost clients.
- **Notes & Customizations**:
  - Many numeric fields are presented in thousands (scale 1000) across selected ranges.
  - The date axis is shared with other sections via the header row (S2:FR2) and follows a monthly cadence defined by the included date series.

### Client Detail - Financial
- **Section Type**: `Custom Time Series Data Table` (monthly detail)
- **Description & Purpose**: Delivers financial detail by the “Financial” subcategory for each month, providing granular monthly metrics that feed into the broader client performance view. This section complements the high-level summary with deeper financial rows for analysis or drill-downs.
- **Cell Range**: A12:FR29
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2
  - **Date Range**: January 2015 through December 2027
  - **Frequency**: Monthly
- **Key Components**: The “Client Detail - Financial” block contains month-by-month financial metrics that align with the overall time series axis; laid out under the Financial subsection.
- **Notes & Customizations**:
  - Values are predominantly scaled by 1000 (thousands) in many fields.
  - This section sits between the Summary header (A5) and the Corporate section header (A31), representing a dedicated financial drill-down.

### Client Detail - Corporate
- **Section Type**: `Custom Time Series Data Table` (monthly detail)
- **Description & Purpose**: Captures corporate-level client metrics and associated monthly figures for the corporate segment. This subsection provides a segment-focused view that supports comparison against the broader client metrics in the summary.
- **Cell Range**: A31:FR48
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2
  - **Date Range**: January 2015 through December 2027
  - **Frequency**: Monthly
- **Key Components**: Corporate client metrics and monthly financials; sub-blocks under the Corporate header present consistent time-series data aligned to the same date axis.
- **Notes & Customizations**:
  - Many values are scaled to thousands (scale 1000) for readability and comparability with the summary block.
  - The Corporate block ends where the next section (Other) begins, enabling a clean separation for retrieval.

### Client Detail - Other
- **Section Type**: `Custom Time Series Data Table` (monthly detail)
- **Description & Purpose**: Contains the remaining client detail data for categories other than Financial and Corporate. This section completes the full detail view of monthly client metrics across the non-core segments.
- **Cell Range**: A50:FR67
- **Time Series Horizon**:
  - **Dates Location**: S2:FR2
  - **Date Range**: January 2015 through December 2027
  - **Frequency**: Monthly
- **Key Components**: Other client detail metrics layered over the same monthly date axis; supports broader segmentation analysis beyond Financial and Corporate.
- **Notes & Customizations**:
  - Scale 1000 is used widely across numeric fields.
  - This section sits after the Corporate block, completing the primary data sections of the sheet.