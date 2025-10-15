## 1. Spreadsheet Overview
- **Sheet Name**: FDS RT Minimums
- **Key Sections Identified**:
  - Pricing Tier Minimums (Tiered Minimums Data)

## 2. Detailed Section Analysis

### Pricing Tier Minimums
- **Section Type**: Custom Data Table
- **Description & Purpose**: A tier-based pricing/minimums dataset that defines user-count ranges, the associated per-user fee (reset at each tier), and the corresponding total metrics (annual and monthly minima/maxima) along with a discount cap. This section serves as input data for pricing logic tied to tier thresholds.
- **Cell Range**: A1:I25
- **Time Series Horizon**:
  - **Dates Location**: Not applicable
  - **Date Range**: Not applicable
  - **Frequency**: Not applicable
- **Key Components**: High-level sub-structure includes:
  - Tier header row (columns define the fields): User Tiers, Incremental Users, Fee Per User (Reset at Each Tier), Total, Max Discount, Min Total (Annual), Max Total, Min Total (Monthly).
  - Tier rows (A2:A25 define tier labels, B2:B25 define tier ranges like "0-1500", "1501-2000", etc.; C, D, F, G-I hold the numeric values for each tier).
- **Notes & Customizations**:
  - The table uses unusual formatting for alignment (non-breaking spaces) in header and tier label cells.
  - Numeric fields include scale modifiers (e.g., D3:D25 and G3:I25 have a scale of 1000) indicating values are presented in thousands.
  - This appears to be a custom pricing/minimums table rather than a standard financial statement, intended to drive tier-based calculations rather than reflect a single period financial statement.