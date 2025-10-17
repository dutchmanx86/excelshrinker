## 1. **Sheet Name**: (Sheet name is not provided in the JSON. Assuming "Assumptions")

### Utilization & Purchase Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the key assumptions used in the financial model, including utilization rates, purchase/lease costs, and operating expenses. It allows users to adjust these assumptions to see the impact on the overall financial results.
- **Cell Range**: B5:F14
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C6:C14, E6:E14
- **Time Series Details**: None. This section contains static assumptions.
- **Key Components**: Total EVG Chassis Purchased, Total EVG Chassis Leased, Total EVG Chassis for Scrap, Total EVG Leases, Total Excess Chassis Leased, Total DCLI Backfill, EVG Average Daily Usage, EVG Utilization Rate, Total Chassis Required for EVG Use.
- **Notes & Customizations**: Includes assumptions for different leasing scenarios (DCLI leases vs. purchases).

### Purchase/Lease Cost Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the cost assumptions related to purchasing and leasing chassis, including book value, premiums/discounts, and lease costs.
- **Cell Range**: B16:C24
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C17:C24
- **Time Series Details**: None. This section contains static assumptions.
- **Key Components**: Average Book Value per Chassis, Premium / (Discount) to Book (Upfront), Premium / (Discount) to Book (PO), Purchase Price, Lease Cost per Day for EVG Chassis, Lease Cost per Day for EVG Leases, Lease Cost per Day for Add. Capacity.
- **Notes & Customizations**: Includes assumptions for both upfront and purchase order (PO) premiums/discounts.

### Upfront Investment Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the upfront investment costs associated with the chassis, including repositioning, decoupling, reconditioning, retitling, stenciling, and offhire costs.
- **Cell Range**: B26:C43, E34:F34
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: None
    - **Data Range**: C27:C43, E34:E34
- **Time Series Details**: None. This section contains static assumptions.
- **Key Components**: Repositioning, # of Chassis w/ Repositioning, Decouping Costs, Chassis to be Decouped, Reconditioning Costs, # of Chassis Requiring Reconditioning, Retitling Costs, Chassis to be Retitled, Stenciling Costs, Chassis to be Stenciled, Offhire Costs, Chassis to be Offhired.
- **Notes & Customizations**: Includes a toggle for reconditioning costs (on/off).

### Operating Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the operating assumptions used in the model, including terminal percentages, billing thresholds, and cost assumptions for M&R, Admin, Repo, and Other expenses.
- **Cell Range**: B45:I51, B53:C60
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: E50:H50
    - **Data Range**: C45:C49, F51, C53:C60, G51:H51
- **Time Series Details**: None. This section contains static assumptions.
- **Key Components**: Sales Tax, Terminal % Assumption Placeholder, Terminal Billing Threshold, Cost Assumptions (M&R, Admin, Repo, Other), PSW MH Rate, EVG CH Rate, Terminal Rate, MH Annual Conversion %, Gain Sharing % on Conversion, Bad Debt (as % of Revenue).
- **Notes & Customizations**: Cost assumptions are referenced as being provided by operations.
