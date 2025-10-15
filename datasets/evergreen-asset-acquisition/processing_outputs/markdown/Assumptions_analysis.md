## 1. Spreadsheet Overview
- **Sheet Name**: Assumptions
- **Key Sections Identified**:
    - Utilization Assumptions
    - Purchase/Lease Assumptions
    - Upfront Investment
    - Operating Assumptions

## 2. Detailed Section Analysis

### Section Name: Utilization Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines the assumptions related to the utilization of EVG chassis, including purchase, lease, and scrap quantities, as well as utilization rates. This section is used to calculate the total chassis required for EVG use.
- **Cell Range**: B5:F14
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**:
      - C6:C14 (numeric values)
      - E6:E14 (numeric values)
- **Time Series Details**:
    - No time series data detected.
- **Key Components**: Total EVG Chassis Purchased, Total EVG Chassis Leased, Total EVG Chassis for Scrap, Total EVG Leases, Total Excess Chassis Leased, Total DCLI Backfill, EVG Average Daily Usage, EVG Utilization Rate, Total Chassis Required for EVG Use.
- **Notes & Customizations**: Includes assumptions for different leasing scenarios (DCLI leases all excess vs. backfilling some excess).

### Section Name: Purchase/Lease Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines the assumptions related to the purchase and lease costs of chassis, including book value, premiums/discounts, and lease rates.
- **Cell Range**: B16:C24
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C17:C24 (numeric values)
- **Time Series Details**:
    - No time series data detected.
- **Key Components**: Average Book Value per Chassis, Premium / (Discount) to Book (Upfront), Premium / (Discount) to Book (PO), Purchase Price, Lease Cost per Day for EVG Chassis, Lease Cost per Day for EVG Leases, Lease Cost per Day for Add. Capacity.
- **Notes & Customizations**: None.

### Section Name: Upfront Investment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines the assumptions related to upfront investment costs, including repositioning, decoupling, reconditioning, retitling, stenciling, and offhire costs.
- **Cell Range**: B26:C43
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C27:C43 (numeric values)
- **Time Series Details**:
    - No time series data detected.
- **Key Components**: Repositioning, # of Chassis w/ Repositioning, Decouping Costs, Chassis to be Decouped, Reconditioning Costs, # of Chassis Requiring Reconditioning, Retitling Costs, Chassis to be Retitled, Stenciling Costs, Chassis to be Stenciled, Offhire Costs, Chassis to be Offhired.
- **Notes & Customizations**: Includes an "on/off" switch (E34) related to reconditioning costs.

### Section Name: Operating Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Defines the assumptions related to operating costs and revenue, including terminal percentages, billing thresholds, cost assumptions for M&R, Admin, Repo, and Other. Also includes PSW MH Rate, EVG CH Rate, Terminal Rate, MH Annual Conversion %, Gain Sharing % on Conversion, and Bad Debt.
- **Cell Range**: B47:I60
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E50:H50
    - **Data Range**:
      - C48:C60 (numeric values)
      - E51:H51 (numeric values)
- **Time Series Details**:
    - No time series data detected.
- **Key Components**: Terminal % Assumption Placeholder, Terminal Billing Threshold, M&R, Admin, Repo, Other, PSW MH Rate, EVG CH Rate, Terminal Rate, MH Annual Conversion %, Gain Sharing % on Conversion, Bad Debt (as % of Revenue).
- **Notes & Customizations**: Cost assumptions are provided by operations (I51).
