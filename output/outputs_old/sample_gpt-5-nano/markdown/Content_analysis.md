## 1. Spreadsheet Overview
- **Sheet Name**: Content
- **Key Sections Identified**:
  - Content Operating Expenses (Overall) – the primary monthly expense schedule for Content including top-level totals and detailed categories.
  - Labor Costs Breakdown (Content) – the granular wage and headcount related lines nested under the broader operating expenses.
  - Content Facilities, Admin & IT Costs – the bucket covering facility costs, admin, and related IT/operational overhead.
  - Time Series Date Axis – the monthly date headers driving the time dimension for all numeric columns.

---

## 2. Detailed Section Analysis

### Content Operating Expenses (A5:Q398)
- **Section Type**: Custom P&L (Expense Schedule)
- **Description & Purpose**: Consolidates Content-related operating expenses in a monthly format. This section aggregates high-level expense totals and then flows into detailed cost breakdowns by category, enabling monitoring of Content spend, staffing-related costs, facilities, IT, marketing, and other operating items. It serves as the primary P&L-like view for Content within the reorganization structure.
- **Cell Range**: A5:Q398
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01-31 to 2027-12
  - **Frequency**: Monthly
- **Key Components**: 
  - Top-level totals such as “Total Content Expense,” “Total Content People Costs,” and “Total Engineering People Costs (excl Cap Wages).”
  - Broad expense categories followed by detailed Content-specific cost lines (e.g., wages, content-specific payroll components, travel, benefits, contractor costs, capitalized wages, and other operating line items).
  - Notable grouping markers include “Total Content Expense,” “Total Content People Costs,” “Total Engineering People Costs (excl Cap Wages),” and the extensive, labeled Content cost blocks that appear throughout the range (e.g., Content Wages, Content Salaries Working Abroad, Holiday Pay, Sick Leave, Commissions, Bonuses, Benefits, Payroll Taxes, Capitalized Wages, Capitalized Outsourced R&D, Capitalized R&D, etc.).
- **Notes & Customizations**:
  - The sheet uses thousands scaling on many numeric lines (scale: 1000) to reflect expense magnitudes.
  - There is extensive Content-specific granularity with many subcategories prefixed by “Content” to reflect department-level cost allocations.
  - This section reflects a restructured, content-centric operating expense model rather than a standard generic P&L.

---

### Labor Costs Breakdown (Content) (B12:Q398)
- **Section Type**: Custom Labor & Wages Schedule (Subset of Content Operating Expenses)
- **Description & Purpose**: Provides a granular view of labor and personnel costs within Content, including base wages, salaries (especially related to Content), working abroad, various paid time-off lines, commissions, bonuses, benefits, payroll taxes, and capitalization-related items. This subsection supports deeper analysis of headcount-driven costs and allocation between Content and Engineering, including capitalized components.
- **Cell Range**: B12:Q398
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01-31 to 2027-12
  - **Frequency**: Monthly
- **Key Components**:
  - Core wage lines: “Wages,” “Content Wages,” “Content Salaries Working Abroad,” “Holiday Pay,” “Content Holiday Pay,” “Sick Leave,” “Commission Expense,” “Bonus,” “Content Benefits,” “Payroll Taxes,” “Finnish Side Costs,” “Share Based Compensation,” “Recruiting Fees,” and related Content lines.
  - Capitalized items: “Capitalized Wages,” “Capitalized Outsourced R&D,” “Capitalized R&D,” and “Content Capitalized R&D.”
  - Supporting labor-related lines: “Total Content Other Employee Costs,” and related cost center breakdowns.
  - The subsections reflect detailed labor allocations across Content and connected cost centers (including engineering-related components excluded from cap wages).
- **Time Series Notes**:
  - The labor cost data align with the same monthly date axis used across the sheet (dates in T2:FS2).
  - Many lines use a scale factor (scale: 1000) to represent thousands of currency units.
- **Notes & Customizations**:
  - High granularity by cost type and department; emphasizes Content-specific labor categories.
  - Includes capitalized labor and R&D components, indicating capitalization treatment within the reporting.

---

### Content Facilities, Admin & IT Costs (B228:Q373)
- **Section Type**: Facilities & Admin Costs (Expense Category)
- **Description & Purpose**: Captures the non-labor operating costs tied to Content’s physical presence, administrative support, and IT/telecom infrastructure. This includes the Total Content Facility Costs and sub-items related to rent, CAM, utilities, admin services, data/telecom, and related overhead. It also aggregates adjacent admin and miscellaneous costs that support Content operations.
- **Cell Range**: B228:Q373
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01-31 to 2027-12
  - **Frequency**: Monthly
- **Key Components**:
  - Total Content Facility Costs, Rent, % of Headcount, Monthly Rent, Content Rent, CAM, Repairs & Maintenance, Amortization of Leasehold Improvements, Utilities, Telephone, Computer & Internet, Content Marketing-related lines, Insurance, Payroll & Benefit Admin, Postage & Delivery, Conferences & Meetings, Furniture, Hardware, Software, Office Supplies, Audit & Tax, Bank Fees, Professional Services, Fundraising, Miscellaneous, and other allied admin/overhead items.
  - The subsection also contains interleaved lines for general admin and content-specific facility costs, with several lines reflecting “Content” prefixes to emphasize department-specific allocations (e.g., Content Insurance, Content Payroll & Benefit Admin, Content Postage & Delivery, Content Office Supplies, Content DataFeeds, Content Web Service, etc.).
- **Time Series Notes**:
  - All facility/admin-related line items roll up to the same monthly date axis (T2:FS2).
  - There are many rows with a thousand-scale representation (scale: 1000) consistent with other cost blocks.
- **Notes & Customizations**:
  - The Facilities/Admin block overlaps with or touches multiple functional areas (IT, data services, insurance, professional services, marketing support, etc.), reflecting a broad admin and overhead footprint for Content.
  - The presence of both “Total Content Facility Costs” and a broad set of labeled sub-items indicates a detailed overhead allocation framework specific to Content operations rather than a generic corporate overhead.

---

### Time Series Date Axis (Date Series Definition)
- **Section Type**: Time Series Definition
- **Description & Purpose**: Defines the monthly date series used across the sheet to drive columnar time-based data. The date axis (ds_1) is leveraged by all numeric, time-series data ranges on the Content sheet.
- **Cell Range**: Dates are defined across the header row as a range (Dates Location) T2:FS2, with ds_1 as the associated date_series_id.
- **Time Series Horizon**:
  - **Dates Location**: T2:FS2
  - **Date Range**: 2015-01-31 to 2027-12
  - **Frequency**: Monthly
- **Key Components**: Monthly date headers (ds_1) spanning from January 2015 through December 2027.
- **Notes & Customizations**: The date series is explicitly labeled as monthly with a start date of 2015-01-31 and a continuation pattern described as "Monthly series from 2015-01 to 2027-12," enabling consistent slicing and retrieval of time-bound data across the sheet.