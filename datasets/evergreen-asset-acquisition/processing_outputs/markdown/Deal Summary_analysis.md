## 1. **Sheet Name**: (Sheet name is not provided in the JSON, assuming it's "Sheet1")

### Fleet Summary and Investment Overview
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides a summary of the current fleet, usage and fleet sizing, and an investment overview for Evergreen Nationwide. It includes key assumptions, financial returns, and sensitivity analysis.
- **Cell Range**: C5:Q32
- **Layout Structure**:
    - **Row Headers Location**: Column C and N
    - **Column Headers Location**: Row 6
    - **Data Range**:
      - Numeric values and formulas are scattered throughout the range, including D7:D11, G7:G12, P7:P16, etc.
- **Time Series Details**:
    - **Date Range**: Year 1 (P19)
    - **Frequency**: Annual
- **Key Components**: Current EVG Fleet (Owned, Leased, Scrapped), Fleet Required, Cost per Usage Day, Investment Overview (Assets, Repositioning, Working Capital, Reconditioning), Financial Returns (CH Revenue, MH Revenue, Total Revenue, Adj. EBITDA, NPV).
- **Notes & Customizations**: Includes commentary/assumptions for various investment components.

### Sensitivity Analysis
- **Section Type**: Sensitivity Analysis Table
- **Description & Purpose**: This section presents a sensitivity analysis of the model, showing how different input parameters affect key output metrics.
- **Cell Range**: C34:R42
- **Layout Structure**:
    - **Row Headers Location**: Column C
    - **Column Headers Location**: Row 36
    - **Data Range**: D38:R41
- **Time Series Details**:
    - None explicitly defined, but the analysis is based on a single point in time or an average across the investment horizon.
- **Key Components**: Scenario, Lease Cost per Day to EVG, Average Prem/(Disc) per Chassis, Terminal Rate, MH Conversion, Total Investment, Investment Multiple, Purchase Price per Chassis, Average EBITDA, Average EBITDA Margin %, 10 year depreciated value IRR %, 5x EBITDA exit multiple IRR %, NPV.
- **Notes & Customizations**: Includes notes on the model inputs and outputs.

### Rate Sensitivity
- **Section Type**: Sensitivity Analysis Table
- **Description & Purpose**: This section presents a sensitivity analysis of the CH and Terminal rates.
- **Cell Range**: C46:H59
- **Layout Structure**:
    - **Row Headers Location**: Column E
    - **Column Headers Location**: Row 46, 55
    - **Data Range**: D47:E54, F56:H59
- **Time Series Details**:
    - None explicitly defined, but the analysis is based on a single point in time or an average across the investment horizon.
- **Key Components**: % MH, CH Rate, Change in Rate, Purchase Price Per Chassis, CH Rate per day, Terminal Rate per day.
- **Notes & Customizations**: Includes different options for the rates.
