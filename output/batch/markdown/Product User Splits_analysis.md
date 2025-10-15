```markdown
## 1. Spreadsheet Overview
- **Sheet Name**: Product User Splits
- **Key Sections Identified**:
    - Product User Data (Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR)
    - BRM Data (BRM - Global, BRM - Single)
    - FactSet RT Data
    - FactSet AMR Data
    - FactSet AMR Breakdown Data (FactSet AMR / Active, FactSet AMR / Trailers, FactSet AMR / Internal)
    - FactSet AMR Docs Purchased Data (FactSet AMR Active Docs Purchased, FactSet AMR Trialer Docs Purchased, FactSet AMR Internal Docs Purchased)

## 2. Detailed Section Analysis

### Section Name: Product User Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the user counts for various products (Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR). It provides a breakdown of user data for each product across different time periods.
- **Cell Range**: B5:BP73
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data (First Series): `D7:AT73`
      - Monthly data (Second Series): `AV7:BP73`
- **Time Series Details**:
    - **Date Range**:
      - Monthly (First Series): 2017-01-31 to 2020-07-31
      - Monthly (Second Series): 2017-01-31 to 2018-09-30
    - **Frequency**: Monthly
- **Key Components**: Lexis Nexis, DJ, FactSet Transcripts, TR Transcripts, Transcripts, TR Filings, TR BRM, AMR ($15k), AMR ($30k), AMR.
- **Notes & Customizations**: The data is scaled by 1000. There are two distinct monthly time series. Column AK contains an "x" for each product.

### Section Name: BRM Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the user counts for BRM products, broken down into Global and Single versions.
- **Cell Range**: B75:BP87
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data (First Series): `D76:AT87`
      - Monthly data (Second Series): `AV76:BP87`
- **Time Series Details**:
    - **Date Range**:
      - Monthly (First Series): 2017-01-31 to 2020-07-31
      - Monthly (Second Series): 2017-01-31 to 2018-09-30
    - **Frequency**: Monthly
- **Key Components**: BRM - Global, BRM - Single.
- **Notes & Customizations**: The data is scaled by 1000. There are two distinct monthly time series.

### Section Name: FactSet RT Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the user counts for FactSet RT.
- **Cell Range**: B89:AT94
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data: `AB90:AT94`
- **Time Series Details**:
    - **Date Range**: 2017-02-28 to 2020-07-31
    - **Frequency**: Monthly
- **Key Components**: FactSet RT
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: FactSet AMR Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the user counts for FactSet AMR.
- **Cell Range**: B96:AR101
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data: `AK97:AR101`
- **Time Series Details**:
    - **Date Range**: 2017-09-30 to 2018-04-30
    - **Frequency**: Monthly
- **Key Components**: FactSet AMR
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: FactSet AMR Breakdown Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the user counts for FactSet AMR, broken down by Active, Trailers, and Internal.
- **Cell Range**: B103:AR110
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data: `AB104:AR110`
- **Time Series Details**:
    - **Date Range**: 2017-02-28 to 2018-04-30
    - **Frequency**: Monthly
- **Key Components**: FactSet AMR / Active, FactSet AMR / Trailers, FactSet AMR / Internal
- **Notes & Customizations**: The data is scaled by 1000.

### Section Name: FactSet AMR Docs Purchased Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section shows the number of documents purchased for FactSet AMR, broken down by Active, Trailers, and Internal.
- **Cell Range**: B112:AR119
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Row 3
    - **Data Range**:
      - Monthly data: `AB113:AR119`
- **Time Series Details**:
    - **Date Range**: 2017-02-28 to 2018-04-30
    - **Frequency**: Monthly
- **Key Components**: FactSet AMR Active Docs Purchased, FactSet AMR Trialer Docs Purchased, FactSet AMR Internal Docs Purchased
- **Notes & Customizations**: The data is scaled by 1000.
```