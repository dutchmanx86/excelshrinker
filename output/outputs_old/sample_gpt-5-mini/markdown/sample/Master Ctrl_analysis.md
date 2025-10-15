## 1. Spreadsheet Overview
- **Sheet Name**: Master Ctrl
- **Key Sections Identified**:
  - Header / Title block
  - Period Inputs (Year / Month)
  - Control Toggles
  - Master Case / Scenario Selector
  - Global Assumptions
  - Productivity Case (assumption inputs)
  - Margin Case (assumption inputs)

## 2. Detailed Section Analysis

### Header / Title block
- **Section Type**: Metadata / Title
- **Description & Purpose**: Top-of-sheet identification showing company name and sheet purpose. Used for human orientation and possibly for automated sheet selection.
- **Cell Range**: B1:B2
- **Time Series Horizon**:
  - **Dates Location**: N/A (no time series in this section)
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**: Company name ("AlphaSense, Inc.") and sheet title ("Master CTRL").
- **Notes & Customizations**: Simple static header. No calculated fields.

### Period Inputs (Year / Month)
- **Section Type**: Input Controls
- **Description & Purpose**: Where the model's active period is selected — primary year and month selectors that drive other calculations across the model.
- **Cell Range**: B6:B7
- **Time Series Horizon**:
  - **Dates Location**: B6 (Year), B7 (Month)
  - **Date Range**: Single-value selectors (not a multi-period series)
  - **Frequency**: N/A (controls choose period-level context)
- **Key Components**: Year selector, Month selector.
- **Notes & Customizations**: These are single-cell inputs expected to be referenced by other sheets; no visible multi-column date series here.

### Control Toggles
- **Section Type**: Input Controls / Flags
- **Description & Purpose**: Binary or toggle controls to enable/disable features or logical branches in the model (e.g., generic "Control" flag).
- **Cell Range**: A11:B11
- **Time Series Horizon**:
  - **Dates Location**: N/A
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**: Toggle marker (column A) and label ("Control").
- **Notes & Customizations**: Single-row control area intended to be read by model logic. May be used to show/hide sections elsewhere.

### Master Case / Scenario Selector
- **Section Type**: Scenario Selector / Master Case Table
- **Description & Purpose**: Lists the available master cases / scenarios (e.g., various revenue / plan cases) and the selected case values. Serves as the central scenario control for model runs.
- **Cell Range**: A13:C17
- **Time Series Horizon**:
  - **Dates Location**: N/A (scenario list, not a time series)
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**: Section title ("Master Case"), scenario names (e.g., "Base - $25mm", "Growth - $25mm", "Base - $50mm", "Base - $50mm (R&D)"), and adjacent selection/value cells for each scenario.
- **Notes & Customizations**: 
  - Some scenario labels appear elsewhere on the sheet per the inverted index (e.g., the string "1 - Base - $25mm" is present at other locations). These are resolved here as literal scenario names.
  - Expect these rows to feed downstream scenario logic; cells in column C are numeric inputs/flags for each scenario.

### Global Assumptions
- **Section Type**: Assumptions Table / Global Parameters
- **Description & Purpose**: Centralized global assumptions used across the model (e.g., latest actual month, months left in year). Designed to provide single-source-of-truth assumption values.
- **Cell Range**: A19:E24
- **Time Series Horizon**:
  - **Dates Location**: B21 contains "Latest Actual Month"; B24 contains "Months Left in Year" with the numeric in E24
  - **Date Range**: Single-point references (e.g., latest actual month) — not a multi-period series
  - **Frequency**: N/A (global parameters)
- **Key Components**: Section heading ("Global Assumptions"), parameter entries such as Latest Actual Month and Months Left in Year, numeric parameter cells (e.g., E24).
- **Notes & Customizations**: This block centralizes parameters that drive forecasting logic; values are single-cell inputs rather than series.

### Productivity Case (assumption inputs)
- **Section Type**: Key Metrics Table / Case Parameters
- **Description & Purpose**: Numeric inputs defining the productivity case assumptions (likely baseline and target values used to compute productivity-driven changes).
- **Cell Range**: B26:C28
- **Time Series Horizon**:
  - **Dates Location**: N/A (parameter inputs, not time series)
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**: Section header ("Productivity Case") and related numeric input rows (commonly a Base and Target pair plus a calculated or additional parameter).
- **Notes & Customizations**:
  - The model contains repeated short labels such as "Base" and "Target" which appear in proximity to these inputs (inverted-index shows "Base" and "Target" strings appear at related cells). These are resolved as the standard Base/Target pair for the case.
  - Cells in column C (C26–C28) are numeric inputs.

### Margin Case (assumption inputs)
- **Section Type**: Key Metrics Table / Case Parameters
- **Description & Purpose**: Numeric inputs defining margin-case assumptions (base/target or similar margin levers used by the model).
- **Cell Range**: B30:C32
- **Time Series Horizon**:
  - **Dates Location**: N/A (parameter inputs)
  - **Date Range**: N/A
  - **Frequency**: N/A
- **Key Components**: Section header ("Margin Case") and associated numeric parameter rows, typically including Base and Target margin inputs.
- **Notes & Customizations**:
  - As with Productivity Case, label duplication exists: "Base" and "Target" appear adjacent to these rows (resolved from the sheet's string index).
  - Numeric inputs occupy C30:C32.

General Notes
- The sheet is a control/assumptions page rather than a multi-period financial statement. Most blocks are single-value inputs or small parameter tables, not columnar time series.
- Several strings appear multiple times on the sheet (as indicated by the inverted index). Those strings have been resolved to their literal values (for example: "1 - Base - $25mm", "1 - Base", "Base", "Target") and are used as scenario/label identifiers across the ranges noted above.
- If a future AI needs to retrieve multi-period time series, this sheet provides period selectors (Year/Month and Latest Actual Month) and scenario flags but not the actual multi-period financial series — those are expected to live on other sheets referenced by these controls.