```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Model
- **Key Sections Identified**:
    - ARR Build - Harpoon
    - Revenue & Contribution
    - New Bookings Assumptions
    - Customer Size & Count
    - ARR Build - LT Model

## 2. Detailed Section Analysis

### ARR Build - Harpoon
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section forecasts the ARR (Annual Recurring Revenue) build for the "Harpoon" product, broken down by customer segment (Corporate, Commercial, Enterprise) and tracks key metrics like Initial Sale, Expansion, Churn, and Gross Revenue Retention (GRR).
- **Cell Range**: C7:FB35
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data: `D10:L14`, `D17:L21`, `D24:L28`, `D31:L35`
      - Quarterly data: `N10:AW14`, `N17:AW21`, `N24:AW28`, `N31:AW35`
      - Monthly data: `AY10:FB14`, `AY17:FB21`, `AY24:FB28`, `AY31:FB35`
- **Time Series Details**:
    - Annual: 2019 to 2027
        - **Frequency**: Annual
    - Quarterly: Q1 2019 to Q4 2027
        - **Frequency**: Quarterly
    - Monthly: 2018-02 to 2027-01
        - **Frequency**: Monthly
- **Key Components**: Corporate BOP ARR, Initial Sale, Expansion, Churn, EOP ARR, GRR %, Total BOP ARR.
- **Notes & Customizations**: ARR is broken down by Corporate, Commercial, and Enterprise segments. Values are scaled by 1000.

### Revenue & Contribution
- **Section Type**: Custom P&L
- **Description & Purpose**: This section projects revenue, cost of goods sold (COGS), commission, and calculates the net harpoon contribution and cash contribution. It also includes calculations for subscription revenue percentage of ARR, gross margin, and commission rate.
- **Cell Range**: C37:FB47
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data: `D37:L40`, `D42:L43`, `H45:L47`
      - Quarterly data: `N37:AW40`, `N42:AW43`
      - Monthly data: `AY37:FB39`, `DG42:FB42`, `CI45:FB47`
- **Time Series Details**:
    - Annual: 2019 to 2027
        - **Frequency**: Annual
    - Quarterly: Q1 2019 to Q4 2027
        - **Frequency**: Quarterly
    - Monthly: 2018-02 to 2027-01
        - **Frequency**: Monthly
- **Key Components**: Revenue, COGS, Commission, Net Harpoon Contribution, NWC Impact - Deferred Revenue, Net Harpoon Cash Contribution, Subscription Revenue % of ARR (per Mo.), Gross Margin %, Commission Rate (% Bookings).
- **Notes & Customizations**: Values are scaled by 1000, except for percentages.

### New Bookings Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the assumptions used to forecast new bookings, including harpoon selling months, attach rate, ASP increase, and bookings by customer segment (Corporate, Commercial, Enterprise).
- **Cell Range**: C49:FB70
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data: `D51:L51`, `D55:L55`, `D58:L58`, `D60:L60`, `D63:L63`, `D65:L65`, `G70:L70`
      - Quarterly data: `N51:AW51`, `N55:AW55`, `N58:AW58`, `N60:AW60`, `N63:AW63`, `N65:AW65`, `N70:AW70`
      - Monthly data: `AY51:FB51`, `AY55:FB55`, `AY58:FB58`, `AY60:FB60`, `AY63:FB63`, `AY65:FB65`, `AY70:FB70`
- **Time Series Details**:
    - Annual: 2019 to 2027
        - **Frequency**: Annual
    - Quarterly: Q1 2019 to Q4 2027
        - **Frequency**: Quarterly
    - Monthly: 2018-02 to 2027-01
        - **Frequency**: Monthly
- **Key Components**: Harpoon Selling Months, New Bookings, Corporate Bookings, Attach Rate, ASP Increase (%), Corporate Harpoon Bookings, Commercial, Commercial Harpoon Bookings, Enterprise, Enterprise Harpoon Bookings, Total New Bookings.
- **Notes & Customizations**: Values are scaled by 1000, except for percentages.

### Customer Size & Count
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the customer size and count assumptions for each customer segment (Corporate, Commercial, Enterprise), along with price point and penetration of existing customers.
- **Cell Range**: C133:L170
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 2
    - **Data Range**:
      - Annual data: `G134:L136`, `G139:L142`, `H144:L146`, `H149:L151`, `G154:L157`, `G160:L163`, `I164:L165`, `G167:L167`, `G170:L170`
- **Time Series Details**:
    - Annual: 2019 to 2027
        - **Frequency**: Annual
- **Key Components**: Customer Size Avg, Customer Count, Price Point, Penetration of Existing, Base, Harpoon, LogRocket, Total Bookings, Worst Case, Best Case.
- **Notes & Customizations**: Values are scaled by 1000.

### ARR Build - LT Model
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section projects the ARR build using a long-term model, broken down by customer segment (Corporate, Commercial, Enterprise) and tracks key metrics like Initial Sale, Expansion, Churn, and Gross Revenue Retention (GRR).
- **Cell Range**: C90:FB118
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Rows 2 and 5
    - **Data Range**:
      - Annual data: `D91:L96`, `D101:L106`, `D111:L116`
      - Quarterly data: `N91:AW96`, `N101:AW106`, `N111:AW116`
      - Monthly data: `AY91:FB96`, `AY101:FB106`, `AY111:FB116`
- **Time Series Details**:
    - Annual: 2019 to 2027
        - **Frequency**: Annual
    - Quarterly: Q1 2019 to Q4 2027
        - **Frequency**: Quarterly
    - Monthly: 2018-02 to 2027-01
        - **Frequency**: Monthly
- **Key Components**: Corporate BOP ARR, Initial Sale, Expansion, Churn, EOP ARR, GRR - Corp, Commercial BOP ARR, GRR - Comm, Enterprise BOP ARR, GRR - Ent.
- **Notes & Customizations**: ARR is broken down by Corporate, Commercial, and Enterprise segments. Values are scaled by 1000.
```