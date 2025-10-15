```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Detailed Cap Table 11.12.21 (wi
- **Key Sections Identified**:
    - Header
    - Capitalization Table
    - Summary Statistics

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the "As of" date. Provides context for the entire sheet.
- **Cell Range**: A1:A2
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: A1:A2
- **Time Series Details**: None
- **Key Components**: Report Title, "As of" Date
- **Notes & Customizations**: None

### Capitalization Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Detailed breakdown of ownership by individual and investor, showing shares held across different classes of stock, outstanding shares, fully diluted shares, and ownership percentages.
- **Cell Range**: A4:M126
- **Layout Structure**:
    - **Row Headers Location**: Column A (A4:A126) - "Anonymized Employee ID / Investor"
    - **Column Headers Location**: Row 4 (B4:M4) - Share classes (Common, Series A Preferred, Series B Preferred, Series Seed Preferred, Options), Outstanding Shares, Fully Diluted Shares, Outstanding Ownership
    - **Data Range**: B5:K126 (share counts), L5:L126 (Outstanding Ownership), M5:M126 (Fully Diluted Ownership)
- **Time Series Details**: None
- **Key Components**: Investor/Employee Names, Common Shares, Preferred Shares (Series A, B, Seed), Options, Outstanding Shares, Fully Diluted Shares, Outstanding Ownership, Fully Diluted Ownership.
- **Notes & Customizations**: Share counts are scaled by 1000.

### Summary Statistics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides summary statistics on shares outstanding, percentage outstanding, and price per share.
- **Cell Range**: A127:M133
- **Layout Structure**:
    - **Row Headers Location**: Column A (A127:A133) - Descriptions of share statistics
    - **Column Headers Location**: Row 4 (B4:M4) - Share classes (Common, Series A Preferred, Series B Preferred, Series Seed Preferred, Options), Outstanding Shares, Fully Diluted Shares, Outstanding Ownership
    - **Data Range**: B129:K133, L131, M128:M129 (various share statistics and prices)
- **Time Series Details**: None
- **Key Components**: Options and RSU's issued and outstanding, Shares available for issuance under the plan, Fully diluted shares, Total Shares Outstanding, Percentage Outstanding, Price per share
- **Notes & Customizations**: Share counts are scaled by 1000.
```