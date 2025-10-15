# Master Workbook Analysis

This document provides a comprehensive analysis of all sheets in the Excel workbook.

---

## Table of Contents

1. [Overview](#overview)
   - [Summary Metrics](#overview-summary-metrics)
   - [Segments Breakdown](#overview-segments-breakdown)
   - [Emerging Segments Breakdown](#overview-emerging-segments-breakdown)
2. [QoS Summ](#qos-summ)
   - [Section Name: Forecast Total QoS](#qos-summ-section-name-forecast-total-qos)
   - [Section Name: Budget Total QoS](#qos-summ-section-name-budget-total-qos)
   - [Section Name: Forecast to Budget Variance](#qos-summ-section-name-forecast-to-budget-variance)
   - [Section Name: EMEA Adjustments](#qos-summ-section-name-emea-adjustments)
3. [Corp Detail](#corp-detail)
   - [Bookings Targets - Quarterly](#corp-detail-bookings-targets---quarterly)
   - [QoS (Net) - Quarterly](#corp-detail-qos-net---quarterly)
   - [Attainment - Quarterly](#corp-detail-attainment---quarterly)
   - [Attainment (% Manager QoS) - Quarterly](#corp-detail-attainment-%-manager-qos---quarterly)
   - [Managers - Gross (No Attrition) - Quarterly](#corp-detail-managers---gross-no-attrition---quarterly)
4. [Comm Detail](#comm-detail)
   - [Section Name: Commercial Bookings Targets](#comm-detail-section-name-commercial-bookings-targets)
   - [Section Name: Managers - Gross (No Attrition)](#comm-detail-section-name-managers---gross-no-attrition)
   - [Section Name: Booking Assumptions](#comm-detail-section-name-booking-assumptions)
5. [Enterprise Detail](#enterprise-detail)
   - [Section Name: Header](#enterprise-detail-section-name-header)
   - [Section Name: Bookings Targets by Manager](#enterprise-detail-section-name-bookings-targets-by-manager)
   - [Section Name: QoS (Net) by Manager](#enterprise-detail-section-name-qos-net-by-manager)
   - [Section Name: Attainment by Manager](#enterprise-detail-section-name-attainment-by-manager)
   - [Section Name: Attainment (% Manager QoS)](#enterprise-detail-section-name-attainment-%-manager-qos)
6. [SS Detail](#ss-detail)
   - [Section Name: Bookings Targets - Company Budget](#ss-detail-section-name-bookings-targets---company-budget)
   - [Section Name: QoS (Net) - Managers - Gross (No Attrition)](#ss-detail-section-name-qos-net---managers---gross-no-attrition)
   - [Section Name: Attainment - Total Manager Target](#ss-detail-section-name-attainment---total-manager-target)
   - [Section Name: Attainment (% Manager QoS) - Notes](#ss-detail-section-name-attainment-%-manager-qos---notes)
7. [EMEA Detail](#emea-detail)
   - [Section Name: Bookings Targets](#emea-detail-section-name-bookings-targets)
   - [Section Name: QoS (Net)](#emea-detail-section-name-qos-net)
   - [Section Name: Attainment](#emea-detail-section-name-attainment)
   - [Section Name: Attainment (% Manager QoS)](#emea-detail-section-name-attainment-%-manager-qos)
8. [Corp Quotas](#corp-quotas)
   - [Section Name: Corporate Manager Quotas](#corp-quotas-section-name-corporate-manager-quotas)
   - [Section Name: Inputs](#corp-quotas-section-name-inputs)
9. [Comm Quotas](#comm-quotas)
   - [Section Name (Commercial Manager Quotas Table)](#comm-quotas-section-name-commercial-manager-quotas-table)
   - [Section Name (Inputs Section)](#comm-quotas-section-name-inputs-section)
10. [Ent Quotas](#ent-quotas)
   - [Title/Header](#ent-quotas-titleheader)
   - [Quota Data by Enterprise Manager](#ent-quotas-quota-data-by-enterprise-manager)
   - [Total Enterprise Quota Summary](#ent-quotas-total-enterprise-quota-summary)
   - [Input Assumptions](#ent-quotas-input-assumptions)
11. [SS Quotas](#ss-quotas)
   - [Section Name: Sub Success Manager Quotas Table](#ss-quotas-section-name-sub-success-manager-quotas-table)
   - [Section Name: Input Assumptions Table](#ss-quotas-section-name-input-assumptions-table)
   - [Section Name: Output Table](#ss-quotas-section-name-output-table)
12. [EMEA Quotas](#emea-quotas)
   - [Title](#emea-quotas-title)
   - [SMB Quota Table](#emea-quotas-smb-quota-table)
   - [Foundation Quota Table](#emea-quotas-foundation-quota-table)
   - [Growth Quota Table](#emea-quotas-growth-quota-table)
   - [SubServ Quota Table](#emea-quotas-subserv-quota-table)
   - [Total EMEA Quota Table](#emea-quotas-total-emea-quota-table)
   - [Input Assumptions Table](#emea-quotas-input-assumptions-table)
13. [Corp Team](#corp-team)
   - [Section Name: Corporate Team Member Data (Batt, Kate)](#corp-team-section-name-corporate-team-member-data-batt-kate)
   - [Section Name: Corporate Team Member Data (Hoy, Michael)](#corp-team-section-name-corporate-team-member-data-hoy-michael)
   - [Section Name: Corporate Team Member Data (Klemm, Brian)](#corp-team-section-name-corporate-team-member-data-klemm-brian)
   - [Section Name: Corporate Team Member Data (TBD Corp Dir #1)](#corp-team-section-name-corporate-team-member-data-tbd-corp-dir-#1)
   - [Section Name: Corporate Team Member Data (TBD Corp Dir #2)](#corp-team-section-name-corporate-team-member-data-tbd-corp-dir-#2)
14. [Comm Team](#comm-team)
   - [Header](#comm-team-header)
   - [Commercial Team Data - Ferguson, Brook](#comm-team-commercial-team-data---ferguson-brook)
   - [Commercial Team Data - Braithwaite-Stanford, Andre](#comm-team-commercial-team-data---braithwaite-stanford-andre)
   - [Commercial Team Data - Ionescu, Sarah](#comm-team-commercial-team-data---ionescu-sarah)
   - [Commercial Team Data - Wilson, Cari](#comm-team-commercial-team-data---wilson-cari)
   - [Commercial Team Data - Commercial Select RVP](#comm-team-commercial-team-data---commercial-select-rvp)
   - [Commercial Team Data - TBD RVP #5](#comm-team-commercial-team-data---tbd-rvp-#5)
15. [Ent Team](#ent-team)
   - [Header](#ent-team-header)
   - [ISV RVP - Gary Revenue Data](#ent-team-isv-rvp---gary-revenue-data)
   - [Putlock, Gary Revenue Data](#ent-team-putlock-gary-revenue-data)
   - [Sabikihi, Harsh Revenue Data](#ent-team-sabikihi-harsh-revenue-data)
   - [Sabikihi/NYC ENT RVP Revenue Data](#ent-team-sabikihinyc-ent-rvp-revenue-data)
   - [Miller, BJ Revenue Data](#ent-team-miller-bj-revenue-data)
   - [Tuttle, Patrick Revenue Data](#ent-team-tuttle-patrick-revenue-data)
   - [Yatsko, Natalie Revenue Data](#ent-team-yatsko-natalie-revenue-data)
   - [Wilson, Matt Revenue Data](#ent-team-wilson-matt-revenue-data)
16. [SS Team](#ss-team)
   - [Section Name: SS Corp Dir Headcount and Quota](#ss-team-section-name-ss-corp-dir-headcount-and-quota)
   - [Section Name: SS Comm Dir Headcount and Quota](#ss-team-section-name-ss-comm-dir-headcount-and-quota)
17. [EMEA Team](#emea-team)
   - [Header](#emea-team-header)
   - [SMB Team Data](#emea-team-smb-team-data)
   - [Foundation Team Data](#emea-team-foundation-team-data)
   - [Growth Team Data](#emea-team-growth-team-data)
   - [Enterprise Team Data](#emea-team-enterprise-team-data)
   - [SubServ Team Data](#emea-team-subserv-team-data)
18. [Targets](#targets)
   - [Section Name: Budget Total QoS](#targets-section-name-budget-total-qos)
   - [Section Name: Budget Total Bookings](#targets-section-name-budget-total-bookings)
   - [Section Name: CRO Target](#targets-section-name-cro-target)
   - [Section Name: VP Target](#targets-section-name-vp-target)
   - [Section Name: Manager Target (Budget-based)](#targets-section-name-manager-target-budget-based)
   - [Section Name: Starting Point for Attainment Targets](#targets-section-name-starting-point-for-attainment-targets)
   - [Section Name: Manager Attainment](#targets-section-name-manager-attainment)
19. [FY22 QoS](#fy22-qos)
   - [Plan Name and Quota Table](#fy22-qos-plan-name-and-quota-table)
   - [Employee Headcount and Quota Details](#fy22-qos-employee-headcount-and-quota-details)
   - [Summary Metrics](#fy22-qos-summary-metrics)
20. [FY22 Overlay](#fy22-overlay)
   - [Header](#fy22-overlay-header)
   - [Sales Rep Data](#fy22-overlay-sales-rep-data)
   - [Quarterly Quota Attainment](#fy22-overlay-quarterly-quota-attainment)
21. [Comm Model](#comm-model)
   - [Section Name (Corporate Forecast Details (Headcount))](#comm-model-section-name-corporate-forecast-details-headcount)
   - [Section Name (Ramp Build - Corporate (Headcount Changes))](#comm-model-section-name-ramp-build---corporate-headcount-changes)
   - [Section Name (Ramp)](#comm-model-section-name-ramp)
   - [Section Name (Ramped Team Adjustment)](#comm-model-section-name-ramped-team-adjustment)
   - [Section Name (Inputs (Plan Data))](#comm-model-section-name-inputs-plan-data)
22. [Corp Model](#corp-model)
   - [Header](#corp-model-header)
   - [Corporate Forecast Details](#corp-model-corporate-forecast-details)
   - [Corporate: Full Team Headcount](#corp-model-corporate-full-team-headcount)
   - [Corporate: Ramped Team - Value Team](#corp-model-corporate-ramped-team---value-team)
   - [Inputs](#corp-model-inputs)
23. [Clean](#clean)
   - [Roster Header](#clean-roster-header)
   - [Employee Roster Data](#clean-employee-roster-data)
   - [Ramped Headcount Data](#clean-ramped-headcount-data)
24. [Sheet4](#sheet4)
   - [Employee List](#sheet4-employee-list)

---


====================================================================================================
# SHEET 1: Overview
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Overview
- **Key Sections Identified**:
    - Summary Metrics
    - Segments Breakdown
    - Emerging Segments Breakdown

## 2. Detailed Section Analysis

### Summary Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a high-level summary of key performance indicators (KPIs) related to headcount, quota, attainment, and budget performance across different business segments. The purpose is to give a quick overview of overall performance.
- **Cell Range**: B2:AW24
- **Layout Structure**:
    - **Row Headers Location**: B4:C24
    - **Column Headers Location**: D4:AW5
    - **Data Range**:
      - Quarterly data: D9:F22, H9:J22, L9:N22, Q9:S22, V9:X22, AA9:AC22, AE9:AG22, AI9:AK22, AM9:AO22, AQ9:AS22, AU9:AW22
- **Time Series Details**:
    - **Date Range**: Q2, Q3, Q4
    - **Frequency**: Quarterly
- **Key Components**: Total Headcount (Gross), Average Ramped Headcount (Gross), Total Quota on Street (Gross), Forecast Quota on Street (Net), Manager Bookings Target, % Attainment (Gross), % Attainment (Net), Budget QoS Target, Manager % Budget QoS, Budget Bookings Target, Manager % Target, Corporate, Commercial, Enterprise, Sub Success, Adopt, VoC, DAP, ANZ, BD, EMEA, JPN, Total, Adopt (Mgr), Forecast QoS.
- **Notes & Customizations**: The data is presented in thousands (scale = 1000) for some metrics. There are also percentage attainment metrics.

### Segments Breakdown
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a detailed breakdown of KPIs by individual managers within each segment (Corporate, Commercial, Enterprise, Sub Success). This allows for granular performance tracking and identification of top/bottom performers.
- **Cell Range**: B26:AG57
- **Layout Structure**:
    - **Row Headers Location**: B28:C57
    - **Column Headers Location**: D4:AG5
    - **Data Range**:
      - Quarterly data: D29:F57, H29:J57, L29:N57, Q29:S57, V29:X57, AA29:AC57, AE29:AG57
- **Time Series Details**:
    - **Date Range**: Q2, Q3, Q4
    - **Frequency**: Quarterly
- **Key Components**: Manager names (e.g., Batt, Kate; Hoy, Michael), Total Headcount (Gross), Average Ramped Headcount (Gross), Total Quota on Street (Gross), Forecast Quota on Street (Net), Manager Bookings Target, % Attainment (Gross), % Attainment (Net).
- **Notes & Customizations**: Data is presented in thousands (scale = 1000) for some metrics. Totals for each segment are included.

### Emerging Segments Breakdown
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Provides a breakdown of KPIs for emerging segments (Adopt, VoC, DAP, BD, JPN) and their respective managers. This section focuses on tracking performance in newer or strategically important areas.
- **Cell Range**: B59:AJ85
- **Layout Structure**:
    - **Row Headers Location**: B60:C85
    - **Column Headers Location**: Q4:AJ5
    - **Data Range**:
      - Quarterly data: Q61:S85, V61:X85, AE61:AG85
- **Time Series Details**:
    - **Date Range**: Q2, Q3, Q4
    - **Frequency**: Quarterly
- **Key Components**: Manager names (e.g., Sandman, Josh; VOC RVP TBH 1), Forecast Quota on Street (Net), Manager Bookings Target, % Attainment (Net), VP/Manager Target buffer.
- **Notes & Customizations**: Data is presented in thousands (scale = 1000) for some metrics.


====================================================================================================
# SHEET 2: QoS Summ
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: QoS Summ
- **Key Sections Identified**:
    - Forecast Total QoS
    - Budget Total QoS
    - Forecast to Budget Variance
    - EMEA Adjustments

## 2. Detailed Section Analysis

### Section Name: Forecast Total QoS
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the forecast for Total QoS (Quality of Service) across different business units and regions. It allows for tracking projected performance.
- **Cell Range**: B3:T21
- **Layout Structure**:
    - **Row Headers Location**: B5:B21
    - **Column Headers Location**: C4:G4, I4:T4
    - **Data Range**:
      - Quarterly/FY data: `C6:G21`
      - Monthly data: `I6:T21`
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: Q1 to FY (Implied Fiscal Year)
      - Monthly: 2021-02-01 to 2022-01-01
    - **Frequency**:
      - Quarterly
      - Monthly
- **Key Components**: Core, Commercial, Corporate, Enterprise, SubSuccess, Emerging, Adopt, VoC, DAP, ANZ, BD, EMEA, JPN, Total
- **Notes & Customizations**: Values are scaled by 1000. "BD" appears to be a placeholder or abbreviation.

### Section Name: Budget Total QoS
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the budget for Total QoS across different business units and regions. It serves as a benchmark for performance.
- **Cell Range**: V3:AA21
- **Layout Structure**:
    - **Row Headers Location**: V5:V21
    - **Column Headers Location**: W4:AA4, I4:T4
    - **Data Range**:
      - Quarterly/FY data: `W6:AA21`
      - Monthly data: `I6:T21`
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: Q1 to FY (Implied Fiscal Year)
      - Monthly: 2021-02-01 to 2022-01-01
    - **Frequency**:
      - Quarterly
      - Monthly
- **Key Components**: Core, Commercial, Corporate, Enterprise, SubSuccess, Emerging, Adopt, VoC, DAP, ANZ, BD, EMEA, JPN, Total
- **Notes & Customizations**: Values are scaled by 1000. "BD" appears to be a placeholder or abbreviation.

### Section Name: Forecast to Budget Variance
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section presents the variance between the forecast and budget for Total QoS across different business units and regions. It highlights areas of over or under performance. Also includes headcount data.
- **Cell Range**: AC3:AH67
- **Layout Structure**:
    - **Row Headers Location**: AC5:AC67
    - **Column Headers Location**: AD4:AH4, I4:T4
    - **Data Range**:
      - Quarterly/FY data: `AD6:AH67`
      - Monthly data: `I6:T67`
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: Q1 to FY (Implied Fiscal Year)
      - Monthly: 2021-02-01 to 2022-01-01
    - **Frequency**:
      - Quarterly
      - Monthly
- **Key Components**: Core, Commercial, Corporate, Enterprise, SubSuccess, Emerging, Adopt, VoC, DAP, ANZ, BD, EMEA, JPN, Total, Average Ramped Heads - Forecast, Average Ramped Heads - Budget, Total Headcount - Forecast (EOP), Total Headcount - Budget
- **Notes & Customizations**: "BD" appears to be a placeholder or abbreviation.

### Section Name: EMEA Adjustments
- **Section Type**: Custom P&L
- **Description & Purpose**: This section details adjustments related to EMEA (Europe, Middle East, and Africa) operations.
- **Cell Range**: W71:Z87
- **Layout Structure**:
    - **Row Headers Location**: W71, W73, W81
    - **Column Headers Location**: None explicitly defined, but X, Y, Z likely represent periods.
    - **Data Range**: `X73:Z74`, `X75:Z75`, `X77:Z78`, `X79:Z79`, `X81:Z82`, `X83:Z83`, `X85:Z86`, `X87:Z87`
- **Time Series Details**:
    - **Date Range**: Implied Quarterly (based on column headers in other sections)
    - **Frequency**: Quarterly
- **Key Components**: EMEA Adjustments, VoC Adj, DAP, SS
- **Notes & Customizations**: Values are scaled by 1000. This section appears to be highly customized and lacks clear column headers.


====================================================================================================
# SHEET 3: Corp Detail
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Corp Detail
- **Key Sections Identified**:
    - Bookings Targets - Quarterly
    - QoS (Net) - Quarterly
    - Attainment - Quarterly
    - Attainment (% Manager QoS) - Quarterly
    - Managers - Gross (No Attrition) - Quarterly

## 2. Detailed Section Analysis

### Bookings Targets - Quarterly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the bookings targets for different entities (Company, CRO, VP) across multiple quarters. It is used for setting and tracking sales goals.
- **Cell Range**: B4:F24
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Company Budget", "CRO", "Coverage", "Managers", "Batt, Kate", "Hoy, Michael", "Klemm, Brian", "PFSU Other", "Total Manager Target")
    - **Column Headers Location**: Row 6 (C6: "Q2", D6: "Q3", E6: "Q4") and Row 19 (C19: "Q2", D19: "Q3", E19: "Q4")
    - **Data Range**:
      - Quarterly data: C7:F10, C12:F13, C15:F16, C20:F24
- **Time Series Details**:
    - **Date Range**: Q2 to Q4 (unspecified year)
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Coverage, Managers, Individual Manager Targets (Batt, Kate, Hoy, Michael, Klemm, Brian, PFSU Other), Total Manager Target.
- **Notes & Customizations**: Bookings Targets are scaled by 1000.

### QoS (Net) - Quarterly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the QoS (Quality of Service - Net) targets for different entities (Company, CRO, VP) across multiple quarters. It is used for setting and tracking service quality goals.
- **Cell Range**: H4:L24
- **Layout Structure**:
    - **Row Headers Location**: Column H (e.g., "Company Budget", "CRO", "Coverage", "Managers", "Batt, Kate", "Hoy, Michael", "Klemm, Brian", "PFSU Other", "Total Manager Target", "Managers - Gross (No Attrition)")
    - **Column Headers Location**: Row 6 (I6: "Q2", J6: "Q3", K6: "Q4") and Row 19 (I19: "Q2", J19: "Q3", K19: "Q4") and Row 27 (I27: "Q2", J27: "Q3", K27: "Q4")
    - **Data Range**:
      - Quarterly data: I7:L10, I12:L13, I15:L16, I20:L24, I28:L32
- **Time Series Details**:
    - **Date Range**: Q2 to Q4 (unspecified year)
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Coverage, Managers, Individual Manager Targets (Batt, Kate, Hoy, Michael, Klemm, Brian, PFSU Other), Total Manager Target, Managers - Gross (No Attrition).
- **Notes & Customizations**: QoS (Net) Targets are scaled by 1000.

### Attainment - Quarterly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the attainment metrics for different entities (Company, CRO, VP) across multiple quarters. It is used for tracking performance against targets.
- **Cell Range**: N4:R24
- **Layout Structure**:
    - **Row Headers Location**: Column N (e.g., "CRO", "Managers", "Batt, Kate", "Hoy, Michael", "Klemm, Brian", "PFSU Other", "Total Manager Target", "Managers - Gross (No Attrition)")
    - **Column Headers Location**: Row 6 (O6: "Q2", P6: "Q3", Q6: "Q4") and Row 19 (O19: "Q2", P19: "Q3", Q19: "Q4") and Row 27 (O27: "Q2", P27: "Q3", Q27: "Q4")
    - **Data Range**:
      - Quarterly data: O7:R10, O20:R24, O28:R32
- **Time Series Details**:
    - **Date Range**: Q2 to Q4 (unspecified year)
    - **Frequency**: Quarterly
- **Key Components**: CRO, Managers, Individual Manager Targets (Batt, Kate, Hoy, Michael, Klemm, Brian, PFSU Other), Total Manager Target, Managers - Gross (No Attrition).
- **Notes & Customizations**: Attainment is not scaled.

### Attainment (% Manager QoS) - Quarterly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the attainment percentage based on Manager QoS for different entities (Company, CRO, VP) across multiple quarters. It is used for tracking performance against targets.
- **Cell Range**: T4:X12
- **Layout Structure**:
    - **Row Headers Location**: Column T (e.g., "Manager QoS", "Company", "VP")
    - **Column Headers Location**: Row 6 (U6: "Q2", V6: "Q3", W6: "Q4")
    - **Data Range**:
      - Quarterly data: U7:X12
- **Time Series Details**:
    - **Date Range**: Q2 to Q4 (unspecified year)
    - **Frequency**: Quarterly
- **Key Components**: Manager QoS, Company, VP.
- **Notes & Customizations**: Attainment (% Manager QoS) is scaled by 1000.

### Managers - Gross (No Attrition) - Quarterly
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the Managers - Gross (No Attrition) metrics for different entities across multiple quarters.
- **Cell Range**: H26:R32
- **Layout Structure**:
    - **Row Headers Location**: Column H (e.g., "Managers - Gross (No Attrition)", "Batt, Kate", "Hoy, Michael", "Klemm, Brian", "PFSU Other", "Total Manager Target")
    - **Column Headers Location**: Row 27 (I27: "Q2", J27: "Q3", K27: "Q4", O27: "Q2", P27: "Q3", Q27: "Q4")
    - **Data Range**:
      - Quarterly data: I28:L32, O28:R32
- **Time Series Details**:
    - **Date Range**: Q2 to Q4 (unspecified year)
    - **Frequency**: Quarterly
- **Key Components**: Managers - Gross (No Attrition), Individual Manager Targets (Batt, Kate, Hoy, Michael, Klemm, Brian, PFSU Other), Total Manager Target.
- **Notes & Customizations**: Managers - Gross (No Attrition) is scaled by 1000.



====================================================================================================
# SHEET 4: Comm Detail
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Comm Detail
- **Key Sections Identified**:
    - Commercial Bookings Targets
    - Managers - Gross (No Attrition)
    - Booking Assumptions

## 2. Detailed Section Analysis

### Section Name: Commercial Bookings Targets
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the commercial bookings targets, QoS (Net), and attainment metrics for various managers and VPs. It provides a quarterly breakdown of targets and performance.
- **Cell Range**: B2:Z26
- **Layout Structure**:
    - **Row Headers Location**: B7:B26 (Manager Names, VP, Total Manager Target)
    - **Column Headers Location**: C6:F6, I6:L6, O6:R6, U6:X6 (Q2, Q3, Q4)
    - **Data Range**:
      - Quarterly data: C7:F26, I7:L26, O7:R26, U7:X26
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Coverage, Managers, Total Manager Target, Manager QoS, Attainment.
- **Notes & Customizations**: Targets are scaled by 1000 in some sections. Includes notes on quota adjustments and manager attainment.

### Section Name: Managers - Gross (No Attrition)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the manager's gross targets without attrition. It provides a quarterly breakdown of targets and performance.
- **Cell Range**: B28:R36
- **Layout Structure**:
    - **Row Headers Location**: B28:B36 (Manager Names, Total Manager Target)
    - **Column Headers Location**: I29:L29, O29:R29 (Q2, Q3, Q4)
    - **Data Range**:
      - Quarterly data: I30:L36, O30:R36
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Managers - Gross (No Attrition), Total Manager Target.
- **Notes & Customizations**: Targets are scaled by 1000 in some sections.

### Section Name: Booking Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the assumptions used for bookings.
- **Cell Range**: H45:I48
- **Layout Structure**:
    - **Row Headers Location**: H45:H47 (Terms, Promos, Hiring/Transfers)
    - **Column Headers Location**: None
    - **Data Range**: I45:I48
- **Time Series Details**:
    - **Date Range**: Not Applicable
    - **Frequency**: Not Applicable
- **Key Components**: Terms, Promos, Hiring/Transfers
- **Notes & Customizations**: Targets are scaled by 1000.


====================================================================================================
# SHEET 5: Enterprise Detail
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Enterprise Detail
- **Key Sections Identified**:
    - Header
    - Bookings Targets by Manager
    - QoS (Net) by Manager
    - Attainment by Manager
    - Attainment (% Manager QoS)

## 2. Detailed Section Analysis

### Section Name: Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and column headers for the subsequent data sections.
- **Cell Range**: B2:Z4
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B4:Z4
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Enterprise, Bookings Targets, QoS (Net), Attainment, Attainment (% Manager QoS)
- **Notes & Customizations**: None

### Section Name: Bookings Targets by Manager
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the bookings targets for each manager across different quarters.
- **Cell Range**: B6:F26
- **Layout Structure**:
    - **Row Headers Location**: B7:B26
    - **Column Headers Location**: C6:E6
    - **Data Range**:
      - Quarterly data: `C7:F10`, `C12:F13`, `C15:F16`, `C20:F26`
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Coverage, Managers, Sabikihi, Harsh, NYC ENT RVP, Miller, BJ, Tuttle, Patrick, Yatsko, Natalie, Wilson, Matt, Total Manager Target
- **Notes & Customizations**: Values are in thousands.

### Section Name: QoS (Net) by Manager
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the QoS (Net) for each manager across different quarters.
- **Cell Range**: H6:L26
- **Layout Structure**:
    - **Row Headers Location**: H7:H26
    - **Column Headers Location**: I6:K6
    - **Data Range**:
      - Quarterly data: `I7:L10`, `I12:L13`, `I15:L16`, `I20:L26`
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Coverage, Managers, Sabikihi, Harsh, NYC ENT RVP, Miller, BJ, Tuttle, Patrick, Yatsko, Natalie, Wilson, Matt, Total Manager Target, Managers - Gross (No Attrition)
- **Notes & Customizations**: Values are in thousands.

### Section Name: Attainment by Manager
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the attainment for each manager across different quarters.
- **Cell Range**: N6:R26
- **Layout Structure**:
    - **Row Headers Location**: N7:N26
    - **Column Headers Location**: O6:Q6
    - **Data Range**:
      - Quarterly data: `O7:R10`, `O20:R26`
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Managers, Sabikihi, Harsh, NYC ENT RVP, Miller, BJ, Tuttle, Patrick, Yatsko, Natalie, Wilson, Matt, Total Manager Target, Managers - Gross (No Attrition)
- **Notes & Customizations**: None

### Section Name: Attainment (% Manager QoS)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Displays the attainment percentage based on Manager QoS for Company and VP across different quarters.
- **Cell Range**: T4:X12
- **Layout Structure**:
    - **Row Headers Location**: T7:T12
    - **Column Headers Location**: U6:W6
    - **Data Range**:
      - Quarterly data: `U7:X12`
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Manager QoS, CRO, Company, VP
- **Notes & Customizations**: None



====================================================================================================
# SHEET 6: SS Detail
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: SS Detail
- **Key Sections Identified**:
    - Bookings Targets - Company Budget
    - QoS (Net) - Managers - Gross (No Attrition)
    - Attainment - Total Manager Target
    - Attainment (% Manager QoS) - Notes

## 2. Detailed Section Analysis

### Section Name: Bookings Targets - Company Budget
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the bookings targets for the company, broken down by quarter.
- **Cell Range**: B4:F7
- **Layout Structure**:
    - **Row Headers Location**: B4, B7
    - **Column Headers Location**: C6:E6
    - **Data Range**: C7:F7
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Bookings Targets, Company Budget
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: QoS (Net) - Managers - Gross (No Attrition)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the QoS (Net) metrics, broken down by quarter.
- **Cell Range**: H4:L25
- **Layout Structure**:
    - **Row Headers Location**: H4, H7, H9, H10, H12, H13, H15, H16, H18, H20, H21, H22, H23, H25
    - **Column Headers Location**: I6:K6, I19:K19, I26:K26
    - **Data Range**: I7:L7, I9:L9, I10:L10, I12:L12, I13:L13, I15:L15, I16:L16, I20:L20, I21:L21, I22:L22, I23:L23, I27:L27, I28:L28, I29:L29, I30:L30
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: QoS (Net), Company Budget, CRO, Coverage, VP, Managers, Bumgardner, Josh, TBD SS Corp Dir, TBD SS Comm Dir, Total Manager Target, Managers - Gross (No Attrition)
- **Notes & Customizations**: Values are scaled by 1000 in some rows.

### Section Name: Attainment - Total Manager Target
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the attainment metrics, broken down by quarter.
- **Cell Range**: N4:R30
- **Layout Structure**:
    - **Row Headers Location**: N4, N7, N8, N9, N10, N18, N20, N21, N22, N23, N25, N27, N28, N29, N30
    - **Column Headers Location**: O6:Q6, O19:Q19, O26:Q26
    - **Data Range**: O7:R7, O8:R8, O9:R9, O10:R10, O20:R20, O21:R21, O22:R22, O23:R23, O27:R27, O28:R28, O29:R29, O30:R30
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Attainment, Manager QoS, VP, Company, CRO, Managers, Bumgardner, Josh, TBD SS Corp Dir, TBD SS Comm Dir, Total Manager Target, Managers - Gross (No Attrition), Wise, Matt, Chowdhury, Nadil, VOC/DAP
- **Notes & Customizations**: None.

### Section Name: Attainment (% Manager QoS) - Notes
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the attainment (% Manager QoS) metrics, broken down by quarter, along with notes.
- **Cell Range**: T4:Z7
- **Layout Structure**:
    - **Row Headers Location**: T4, T7, T9, T10, T11, T12
    - **Column Headers Location**: U6:W6, Z6
    - **Data Range**: U7:X7, U9:X9, U10:X10, U11:X11, U12:X12, Z7
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Attainment (% Manager QoS), Manager QoS, Company, VP, CRO, Managers, Notes
- **Notes & Customizations**: Values are scaled by 1000 in some rows. The last column contains text notes.


====================================================================================================
# SHEET 7: EMEA Detail
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: EMEA Detail
- **Key Sections Identified**:
    - Bookings Targets
    - QoS (Net)
    - Attainment
    - Attainment (% Manager QoS)

## 2. Detailed Section Analysis

### Section Name: Bookings Targets
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the bookings targets for different categories (e.g., Company Budget, CRO, Coverage, Managers, SMB, Foundation, Growth, Enterprise, SubServ, Total Manager Target) across different quarters. It helps in tracking and managing sales performance.
- **Cell Range**: B4:F25
- **Layout Structure**:
    - **Row Headers Location**: Column B (B7, B9, B10, B12, B13, B15, B16, B18, B20, B21, B22, B23, B24, B25)
    - **Column Headers Location**: C6:F6 (Q2, Q3, Q4)
    - **Data Range**:
      - Quarterly data: C7:F7, C9:F10, C12:F13, C15:F16, C20:F25
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Coverage, Managers, SMB, Foundation, Growth, Enterprise, SubServ, Total Manager Target
- **Notes & Customizations**: Bookings Targets are scaled by 1000 in some rows.

### Section Name: QoS (Net)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the QoS (Net) metrics for different categories (e.g., Company Budget, CRO, Coverage, Managers, SMB, Foundation, Growth, Enterprise, SubServ, Total Manager Target) across different quarters. It helps in tracking and managing the quality of sales.
- **Cell Range**: H4:L34
- **Layout Structure**:
    - **Row Headers Location**: Column H (H7, H9, H10, H12, H13, H15, H16, H18, H20, H21, H22, H23, H24, H25, H27, H29, H30, H31, H32, H33, H34)
    - **Column Headers Location**: I6:K6 (Q2, Q3, Q4)
    - **Data Range**:
      - Quarterly data: I7:L7, I9:L10, I12:L13, I15:L16, I20:L25, I29:L34
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Coverage, Managers, SMB, Foundation, Growth, Enterprise, SubServ, Total Manager Target, Managers - Gross (No Attrition)
- **Notes & Customizations**: QoS (Net) metrics are scaled by 1000 in some rows.

### Section Name: Attainment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the attainment metrics for different categories (e.g., Company Budget, CRO, Coverage, Managers, SMB, Foundation, Growth, Enterprise, SubServ, Total Manager Target) across different quarters. It helps in tracking and managing sales performance against targets.
- **Cell Range**: N4:R34
- **Layout Structure**:
    - **Row Headers Location**: Column N (N7, N8, N9, N10, N18, N20, N21, N22, N23, N24, N25, N27, N29, N30, N31, N32, N33, N34)
    - **Column Headers Location**: O6:Q6 (Q2, Q3, Q4)
    - **Data Range**:
      - Quarterly data: O7:R10, O20:R25, O29:R34
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Company Budget, CRO, Coverage, Managers, SMB, Foundation, Growth, Enterprise, SubServ, Total Manager Target, Managers - Gross (No Attrition)
- **Notes & Customizations**: None

### Section Name: Attainment (% Manager QoS)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the attainment as a percentage of Manager QoS for different categories (e.g., Manager QoS, Company, VP) across different quarters. It helps in understanding the relationship between attainment and the quality of sales management.
- **Cell Range**: T4:X12
- **Layout Structure**:
    - **Row Headers Location**: Column T (T4, T7, T9, T10, T11, T12)
    - **Column Headers Location**: U6:W6 (Q2, Q3, Q4)
    - **Data Range**:
      - Quarterly data: U7:X7, U9:X12
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Manager QoS, Company, VP
- **Notes & Customizations**: Attainment (% Manager QoS) metrics are scaled by 1000 in some rows.


====================================================================================================
# SHEET 8: Corp Quotas
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Corp Quotas
- **Key Sections Identified**:
    - Corporate Manager Quotas
    - Inputs

## 2. Detailed Section Analysis

### Section Name: Corporate Manager Quotas
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the quotas and related metrics for corporate managers. It allows for tracking performance against targets.
- **Cell Range**: A6:Q51
- **Layout Structure**:
    - **Row Headers Location**: Column B (e.g., "Batt, Kate", "Hoy, Michael", "Klemm, Brian", "PFSU Other", "Total Corporate")
    - **Column Headers Location**: Row 5 (Q2, Q3, Q4) and Row 6 (PFSU)
    - **Data Range**:
      - Quarterly data: `E7:G51` (numeric values for Q2, Q3, Q4)
      - Monthly data: `I7:Q51` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: Q2 2021 to Q4 2021
      - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Quarterly
      - Monthly
- **Key Components**: Total HC (Gross), Ramped HC (Gross), QoS, Attrition Factor, QoS (Adj), Attainment (%), Bookings Target
- **Notes & Customizations**: Data is presented in thousands (scale = 1000). There are multiple time series with quarterly and monthly data.

### Section Name: Inputs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains input parameters and plan data used for calculations or analysis in other parts of the spreadsheet.
- **Cell Range**: B56:Q70
- **Layout Structure**:
    - **Row Headers Location**: Column B and Column I (e.g., "Plan:", "Q1 Attnmt", "Q2 Attnmt", "Q3 Attnmt", "Q4 Attnmt")
    - **Column Headers Location**: Row 64 (Monthly dates)
    - **Data Range**:
      - Monthly data: `I65:Q70` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**: 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Active, Commercial, Corporate, Enterprise, SS Corp, SS Comm, Q1 Attnmt, Q2 Attnmt, Q3 Attnmt, Q4 Attnmt
- **Notes & Customizations**: This section contains plan data and attainment metrics.


====================================================================================================
# SHEET 9: Comm Quotas
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Comm Quotas
- **Key Sections Identified**:
    - Commercial Manager Quotas Table
    - Inputs Section

## 2. Detailed Section Analysis

### Section Name (Commercial Manager Quotas Table)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the commercial manager quotas and related metrics such as Total HC, Ramped HC, QoS, Attrition Factor, QoS (Adj), Attainment (%), and Bookings Target. It allows for tracking and analysis of performance against targets.
- **Cell Range**: B2:Q69
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 4 and 5
    - **Data Range**:
      - Current: `C7:C69` (current values)
      - Quarterly data: `E7:G69` (numeric values for Q2, Q3, Q4 of 2022)
      - Monthly data: `I7:Q69` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: Q2 2022 to Q4 2022
      - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Quarterly
      - Monthly
- **Key Components**: Total HC, Ramped HC, QoS, Attrition Factor, QoS (Adj), Attainment (%), Bookings Target, individual manager names.
- **Notes & Customizations**: Data is presented for individual commercial managers and aggregated for "Total Commercial". Values are scaled by 1000 in some rows.

### Section Name (Inputs Section)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains input values used in calculations within the spreadsheet. It includes plan values and attainment percentages for different categories.
- **Cell Range**: B74:Q88
- **Layout Structure**:
    - **Row Headers Location**: Column G
    - **Column Headers Location**: Row 82
    - **Data Range**:
      - `J76:O79`
      - `I83:Q88`
- **Time Series Details**:
    - **Date Range**: 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Plan values (Q1 Attnmt, Q2 Attnmt, Q3 Attnmt, Q4 Attnmt), Active, Commercial, Corporate, Enterprise, SS Corp, SS Comm.
- **Notes & Customizations**: This section appears to feed into calculations in the main Commercial Manager Quotas Table.


====================================================================================================
# SHEET 10: Ent Quotas
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Ent Quotas
- **Key Sections Identified**:
    - Title/Header
    - Quota Data by Enterprise Manager
    - Total Enterprise Quota Summary
    - Input Assumptions

## 2. Detailed Section Analysis

### Title/Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report and the time period covered.
- **Cell Range**: B2:Q5
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E5:G5 (Q2, Q3, Q4), I4:Q4 (22Q2, 22Q3, 22Q4), I5:Q5 (Date Series)
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: "Enterprise Manager Quotas", "22Q2", "22Q3", "22Q4", "Q2", "Q3", "Q4"
- **Notes & Customizations**: The header spans multiple rows and columns to define the report context. There is a monthly time series in the header.

### Quota Data by Enterprise Manager
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays quota-related metrics for each Enterprise Manager.
- **Cell Range**: B6:Q58
- **Layout Structure**:
    - **Row Headers Location**: B6:B58 (Enterprise Manager Names and related descriptions)
    - **Column Headers Location**: C5, E5:G5, I4:Q4, I5:Q5
    - **Data Range**:
      - Quarterly data: C7:C58, E7:G58
      - Monthly data: I7:Q58
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: Q2, Q3, Q4 (Implied, but not explicitly dates)
      - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Quarterly
      - Monthly
- **Key Components**: Total HC, Ramped HC, QoS, Attrition Factor, QoS (Adj), Attainment (%), Bookings Target
- **Notes & Customizations**: Data is presented for each Enterprise Manager, with metrics scaled by 1000 in some cases. There are two time series: Quarterly (Q2, Q3, Q4) and Monthly (2021-05-01 to 2022-01-01).

### Total Enterprise Quota Summary
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section summarizes the quota-related metrics for the entire Enterprise.
- **Cell Range**: B62:Q69
- **Layout Structure**:
    - **Row Headers Location**: B62:B69 (Total Enterprise and related descriptions)
    - **Column Headers Location**: C5, E5:G5, I4:Q4, I5:Q5
    - **Data Range**:
      - Quarterly data: C63:C69, E63:G69
      - Monthly data: I63:Q69
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: Q2, Q3, Q4 (Implied, but not explicitly dates)
      - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Quarterly
      - Monthly
- **Key Components**: Total HC, Ramped HC, QoS, Attrition Factor, QoS (adj), Attainment (%), Bookings Target
- **Notes & Customizations**: Data is presented for the entire Enterprise, with metrics scaled by 1000 in some cases. There are two time series: Quarterly (Q2, Q3, Q4) and Monthly (2021-05-01 to 2022-01-01).

### Input Assumptions
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains input assumptions used in the quota calculations.
- **Cell Range**: B74:Q88
- **Layout Structure**:
    - **Row Headers Location**: B74, B76, I76:I79, G83:G88
    - **Column Headers Location**: I82:Q82
    - **Data Range**: J76:O79, I83:Q88
- **Time Series Details**:
    - **Date Range**: 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Plan, Q1 Attnmt, Q2 Attnmt, Q3 Attnmt, Q4 Attnmt, Active, Commercial, Corporate, Enterprise, SS Corp, SS Comm
- **Notes & Customizations**: This section contains both plan inputs and attainment data by segment. There is a monthly time series from 2021-05-01 to 2022-01-01.


====================================================================================================
# SHEET 11: SS Quotas
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: SS Quotas
- **Key Sections Identified**:
    - Sub Success Manager Quotas Table
    - Input Assumptions Table
    - Output Table

## 2. Detailed Section Analysis

### Section Name: Sub Success Manager Quotas Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the quotas and attainment metrics for individual Sub Success Managers. It allows for tracking performance against targets.
- **Cell Range**: B2:Q51
- **Layout Structure**:
    - **Row Headers Location**: Column B
    - **Column Headers Location**: Rows 4-5
    - **Data Range**:
      - Q2-Q4 2022: `E7:G51`
      - Monthly: `I7:Q51`
- **Time Series Details**:
    - **Date Range**:
      - Quarterly: Q2 2022 to Q4 2022
      - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Quarterly
      - Monthly
- **Key Components**: Total HC, Ramped HC, QoS, Attrition Factor, QoS (Adj), Attainment (%), Bookings Target
- **Notes & Customizations**: Values are scaled by 1000 in many cells. There are multiple time series, one quarterly (Q2-Q4 2022) and one monthly (May 2021 - Jan 2022).

### Section Name: Input Assumptions Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains input assumptions used for calculations.
- **Cell Range**: B56:O61
- **Layout Structure**:
    - **Row Headers Location**: Column I
    - **Column Headers Location**: Row 58
    - **Data Range**: `J58:O61`
- **Time Series Details**:
    - **Date Range**: Q1 Attnmt to Q4 Attnmt
    - **Frequency**: Quarterly
- **Key Components**: Q1 Attnmt, Q2 Attnmt, Q3 Attnmt, Q4 Attnmt
- **Notes & Customizations**: This section appears to be for inputting attainment percentages for each quarter.

### Section Name: Output Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the output of calculations based on the input assumptions.
- **Cell Range**: G64:Q70
- **Layout Structure**:
    - **Row Headers Location**: Column G
    - **Column Headers Location**: Row 64
    - **Data Range**: `I65:Q70`
- **Time Series Details**:
    - **Date Range**: 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Active, Commercial, Corporate, Enterprise, SS Corp, SS Comm
- **Notes & Customizations**: This section shows the distribution of some metric (unclear from the provided data) across different categories (Active, Commercial, etc.) over a monthly time series.


====================================================================================================
# SHEET 12: EMEA Quotas
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: EMEA Quotas
- **Key Sections Identified**:
    - Title
    - SMB Quota Table
    - Foundation Quota Table
    - Growth Quota Table
    - SubServ Quota Table
    - Total EMEA Quota Table
    - Input Assumptions Table

## 2. Detailed Section Analysis

### Title
- **Section Type**: Title
- **Description & Purpose**: The title of the spreadsheet, indicating its purpose.
- **Cell Range**: B2:B2
- **Layout Structure**:
    - **Row Headers Location**: N/A
    - **Column Headers Location**: N/A
    - **Data Range**: B2:B2
- **Time Series Details**: N/A
- **Key Components**: EMEA Manager Quotas
- **Notes & Customizations**: N/A

### SMB Quota Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays key performance indicators (KPIs) and targets for the SMB segment.
- **Cell Range**: B6:Q13
- **Layout Structure**:
    - **Row Headers Location**: B6:B13
    - **Column Headers Location**: C5:G5, I4:Q4
    - **Data Range**:
      - Q2-Q4: C7:G13
      - 22Q2-22Q4: I7:Q13
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
      - 22Q2 to 22Q4
    - **Frequency**: Quarterly
- **Key Components**: Total HC, Ramped HC, QoS, Attrition Factor, QoS (Adj), Attainment (%), Bookings Target
- **Notes & Customizations**: Values are scaled by 1000.

### Foundation Quota Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays key performance indicators (KPIs) and targets for the Foundation segment.
- **Cell Range**: B15:Q22
- **Layout Structure**:
    - **Row Headers Location**: B15:B22
    - **Column Headers Location**: C5:G5, I4:Q4
    - **Data Range**:
      - Q2-Q4: C16:G22
      - 22Q2-22Q4: I16:Q22
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
      - 22Q2 to 22Q4
    - **Frequency**: Quarterly
- **Key Components**: Total HC, Ramped HC, QoS, Attrition Factor, QoS (Adj), Attainment (%), Bookings Target
- **Notes & Customizations**: Values are scaled by 1000.

### Growth Quota Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays key performance indicators (KPIs) and targets for the Growth segment.
- **Cell Range**: B24:Q31
- **Layout Structure**:
    - **Row Headers Location**: B24:B31
    - **Column Headers Location**: C5:G5, I4:Q4
    - **Data Range**:
      - Q2-Q4: C25:G31
      - 22Q2-22Q4: I25:Q31
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
      - 22Q2 to 22Q4
    - **Frequency**: Quarterly
- **Key Components**: Total HC, Ramped HC, QoS, Attrition Factor, QoS (Adj), Attainment (%), Bookings Target
- **Notes & Customizations**: Values are scaled by 1000.

### SubServ Quota Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays key performance indicators (KPIs) and targets for the SubServ segment.
- **Cell Range**: B42:Q49
- **Layout Structure**:
    - **Row Headers Location**: B42:B49
    - **Column Headers Location**: C5:G5, I4:Q4
    - **Data Range**:
      - Q2-Q4: C43:G49
      - 22Q2-22Q4: I43:Q49
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
      - 22Q2 to 22Q4
    - **Frequency**: Quarterly
- **Key Components**: Total HC, Ramped HC, QoS, Attrition Factor, QoS (Adj), Attainment (%), Bookings Target
- **Notes & Customizations**: Values are scaled by 1000.

### Total EMEA Quota Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays key performance indicators (KPIs) and targets for the Total EMEA.
- **Cell Range**: B53:Q60
- **Layout Structure**:
    - **Row Headers Location**: B53:B60
    - **Column Headers Location**: C5:G5, I4:Q4
    - **Data Range**:
      - Q2-Q4: C54:G60
      - 22Q2-22Q4: I54:Q60
- **Time Series Details**:
    - **Date Range**: Q2 to Q4
      - 22Q2 to 22Q4
    - **Frequency**: Quarterly
- **Key Components**: Total HC, Ramped HC, QoS, Attrition Factor, QoS (Adj), Attainment (%), Bookings Target
- **Notes & Customizations**: Values are scaled by 1000.

### Input Assumptions Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays input assumptions used for calculations.
- **Cell Range**: B65:Q80
- **Layout Structure**:
    - **Row Headers Location**: B67:B80, G74:G80
    - **Column Headers Location**: I67:Q67, I73:Q73
    - **Data Range**:
      - J67:P70
      - I74:Q80
- **Time Series Details**:
    - **Date Range**: 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Plan, Q1 Attnmt, Q2 Attnmt, Q3 Attnmt, Q4 Attnmt, Active, Commercial, Corporate, Enterprise, SS Corp, SS Comm, EMEA
- **Notes & Customizations**: N/A


====================================================================================================
# SHEET 13: Corp Team
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Corp Team
- **Key Sections Identified**:
    - Corporate Team Member Data (Batt, Kate)
    - Corporate Team Member Data (Hoy, Michael)
    - Corporate Team Member Data (Klemm, Brian)
    - Corporate Team Member Data (TBD Corp Dir #1)
    - Corporate Team Member Data (TBD Corp Dir #2)

## 2. Detailed Section Analysis

### Section Name: Corporate Team Member Data (Batt, Kate)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains headcount, ramped headcount, and quota data for the "Corporate" team members under "Batt, Kate". The purpose is to track and manage team performance metrics.
- **Cell Range**: B7:BG20
- **Layout Structure**:
    - **Row Headers Location**: B7:B20, D7:D20, AX7:AX20
    - **Column Headers Location**: E5:P5, R3, R5:Z5, AB3, AB5:AJ5, AL3, AL5:AT5, AY5:BG5
    - **Data Range**:
      - Monthly data (E5:P5): E7:P20
      - Monthly data (R5:Z5): R7:Z20
      - Monthly data (AB5:AJ5): AB7:AJ20
      - Monthly data (AL5:AT5): AL7:AT20
      - Monthly data (AY5:BG5): AY7:BG20
- **Time Series Details**:
    - **Date Range**:
      - Monthly (E5:P5): 2021-02-01 to 2022-01-01
      - Monthly (R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5): 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Monthly
      - Monthly
- **Key Components**: Allie Winstead, Mackenzie Smith--Old Mgr, Ash Cochran, Cassie Davis, Future Hire, Steph Hastings--PFSU
- **Notes & Customizations**: Data is scaled by 1000 in columns R:Z, AB:AJ, AL:AT, and AY:BG.

### Section Name: Corporate Team Member Data (Hoy, Michael)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains headcount, ramped headcount, and quota data for the "Corporate" team members under "Hoy, Michael". The purpose is to track and manage team performance metrics.
- **Cell Range**: B22:BG35
- **Layout Structure**:
    - **Row Headers Location**: B22:B35, D22:D35, AX22:AX27
    - **Column Headers Location**: E5:P5, R3, R5:Z5, AB3, AB5:AJ5, AL3, AL5:AT5, AY5:BG5
    - **Data Range**:
      - Monthly data (E5:P5): E22:P27
      - Monthly data (R5:Z5): R22:Z27
      - Monthly data (AB5:AJ5): AB22:AJ27
      - Monthly data (AL5:AT5): AL22:AT27
      - Monthly data (AY5:BG5): AY22:BG27
- **Time Series Details**:
    - **Date Range**:
      - Monthly (E5:P5): 2021-02-01 to 2022-01-01
      - Monthly (R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5): 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Monthly
      - Monthly
- **Key Components**: Taylor Tharrington, Mackenzie Smith, Sam Turner, Laura Vancosky, Melissa Moriarty, Abbey Freeman
- **Notes & Customizations**: Data is scaled by 1000 in columns R:Z, AB:AJ, AL:AT, and AY:BG.

### Section Name: Corporate Team Member Data (Klemm, Brian)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains headcount, ramped headcount, and quota data for the "Corporate" team members under "Klemm, Brian". The purpose is to track and manage team performance metrics.
- **Cell Range**: B37:AT50
- **Layout Structure**:
    - **Row Headers Location**: B37:B50, D37:D50
    - **Column Headers Location**: E5:P5, R3, R5:Z5, AB3, AB5:AJ5, AL3, AL5:AT5
    - **Data Range**:
      - Monthly data (E5:P5): E37:P42
      - Monthly data (R5:Z5): R37:Z42
      - Monthly data (AB5:AJ5): AB37:AJ42
      - Monthly data (AL5:AT5): AL37:AT42
- **Time Series Details**:
    - **Date Range**:
      - Monthly (E5:P5): 2021-02-01 to 2022-01-01
      - Monthly (R5:Z5, AB5:AJ5, AL5:AT5): 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Monthly
      - Monthly
- **Key Components**: Jack Miller, Lara George, Emily Cutts, Will Jones, Steph Hastings--East
- **Notes & Customizations**: Data is scaled by 1000 in columns R:Z, AB:AJ, AL:AT.

### Section Name: Corporate Team Member Data (TBD Corp Dir #1)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains headcount, ramped headcount, and quota data for the "Corporate" team members under "TBD Corp Dir #1". The purpose is to track and manage team performance metrics.
- **Cell Range**: B52:AT65
- **Layout Structure**:
    - **Row Headers Location**: B52:B65, D52:D65
    - **Column Headers Location**: E5:P5, R3, R5:Z5, AB3, AB5:AJ5, AL3, AL5:AT5
    - **Data Range**:
      - Monthly data (E5:P5): I52:P57
      - Monthly data (R5:Z5): S52:Z62
      - Monthly data (AB5:AJ5): AC52:AJ62
      - Monthly data (AL5:AT5): AM52:AT62
- **Time Series Details**:
    - **Date Range**:
      - Monthly (E5:P5): 2021-02-01 to 2022-01-01
      - Monthly (R5:Z5, AB5:AJ5, AL5:AT5): 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Monthly
      - Monthly
- **Key Components**: Future Hire
- **Notes & Customizations**: Data is scaled by 1000 in columns S:Z, AC:AJ, and AM:AT.

### Section Name: Corporate Team Member Data (TBD Corp Dir #2)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains headcount, ramped headcount, and quota data for the "Corporate" team members under "TBD Corp Dir #2". The purpose is to track and manage team performance metrics.
- **Cell Range**: B67:AT80
- **Layout Structure**:
    - **Row Headers Location**: B67:B80, D67:D80
    - **Column Headers Location**: E5:P5, R3, R5:Z5, AB3, AB5:AJ5, AL3, AL5:AT5
    - **Data Range**:
      - Monthly data (E5:P5): I67:P72
      - Monthly data (R5:Z5): R67:Z72
      - Monthly data (AB5:AJ5): AB67:AJ72
      - Monthly data (AL5:AT5): AL67:AT72
- **Time Series Details**:
    - **Date Range**:
      - Monthly (E5:P5): 2021-02-01 to 2022-01-01
      - Monthly (R5:Z5, AB5:AJ5, AL5:AT5): 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Monthly
      - Monthly
- **Key Components**: James Ferraro, Briauna Smith, Douglas Godette
- **Notes & Customizations**: Data is scaled by 1000 in columns R:Z, AB:AJ, and AL:AT.


====================================================================================================
# SHEET 14: Comm Team
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Comm Team
- **Key Sections Identified**:
    - Header
    - Commercial Team Data - Ferguson, Brook
    - Commercial Team Data - Braithwaite-Stanford, Andre
    - Commercial Team Data - Ionescu, Sarah
    - Commercial Team Data - Wilson, Cari
    - Commercial Team Data - Commercial Select RVP
    - Commercial Team Data - TBD RVP #5

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains labels for the data and time series.
- **Cell Range**: A1:BG5
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**:
        - Monthly: 2021-02-01 to 2022-01-01
        - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
        - Monthly
        - Monthly
- **Key Components**: Headcount, Ramped Headcount, Quota, Date headers
- **Notes & Customizations**: Contains multiple monthly time series starting at different months.

### Commercial Team Data - Ferguson, Brook
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the "Commercial" team member "Ferguson, Brook".
- **Cell Range**: B7:BG20
- **Layout Structure**:
    - **Row Headers Location**: B7:B20
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5
    - **Data Range**:
        - E7:P20 (numeric values for monthly periods)
        - R7:Z20 (numeric values for monthly periods)
        - AB7:AJ20 (numeric values for monthly periods)
        - AL7:AT20 (numeric values for monthly periods)
        - AY7:BG20 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
        - Monthly: 2021-02-01 to 2022-01-01
        - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
        - Monthly
        - Monthly
- **Key Components**: Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000. Contains multiple monthly time series starting at different months.

### Commercial Team Data - Braithwaite-Stanford, Andre
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the "Commercial" team member "Braithwaite-Stanford, Andre".
- **Cell Range**: B22:BG35
- **Layout Structure**:
    - **Row Headers Location**: B22:B35
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5
    - **Data Range**:
        - E22:P35 (numeric values for monthly periods)
        - R22:Z35 (numeric values for monthly periods)
        - AB22:AJ35 (numeric values for monthly periods)
        - AL22:AT35 (numeric values for monthly periods)
        - AY22:BG35 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
        - Monthly: 2021-02-01 to 2022-01-01
        - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
        - Monthly
        - Monthly
- **Key Components**: Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000. Contains multiple monthly time series starting at different months.

### Commercial Team Data - Ionescu, Sarah
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the "Commercial" team member "Ionescu, Sarah".
- **Cell Range**: B37:AT50
- **Layout Structure**:
    - **Row Headers Location**: B37:B50
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
        - E37:P50 (numeric values for monthly periods)
        - R37:Z50 (numeric values for monthly periods)
        - AB37:AJ50 (numeric values for monthly periods)
        - AL37:AT50 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
        - Monthly: 2021-02-01 to 2022-01-01
        - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
        - Monthly
        - Monthly
- **Key Components**: Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000. Contains multiple monthly time series starting at different months.

### Commercial Team Data - Wilson, Cari
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the "Commercial" team member "Wilson, Cari".
- **Cell Range**: B52:AT65
- **Layout Structure**:
    - **Row Headers Location**: B52:B65
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
        - E52:P65 (numeric values for monthly periods)
        - R52:Z65 (numeric values for monthly periods)
        - AB52:AJ65 (numeric values for monthly periods)
        - AL52:AT65 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
        - Monthly: 2021-02-01 to 2022-01-01
        - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
        - Monthly
        - Monthly
- **Key Components**: Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000. Contains multiple monthly time series starting at different months.

### Commercial Team Data - Commercial Select RVP
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the "Commercial Select RVP" team.
- **Cell Range**: B67:BG80
- **Layout Structure**:
    - **Row Headers Location**: B67:B80
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5
    - **Data Range**:
        - E67:P80 (numeric values for monthly periods)
        - R67:Z80 (numeric values for monthly periods)
        - AB67:AJ80 (numeric values for monthly periods)
        - AL67:AT80 (numeric values for monthly periods)
        - AY67:BG80 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
        - Monthly: 2021-02-01 to 2022-01-01
        - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
        - Monthly
        - Monthly
- **Key Components**: Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000. Contains multiple monthly time series starting at different months.

### Commercial Team Data - TBD RVP #5
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the "TBD RVP #5" team.
- **Cell Range**: B82:AT95
- **Layout Structure**:
    - **Row Headers Location**: B82:B95
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
        - E82:P95 (numeric values for monthly periods)
        - R82:Z95 (numeric values for monthly periods)
        - AB82:AJ95 (numeric values for monthly periods)
        - AL82:AT95 (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**:
        - Monthly: 2021-02-01 to 2022-01-01
        - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
        - Monthly
        - Monthly
- **Key Components**: Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000. Contains multiple monthly time series starting at different months.



====================================================================================================
# SHEET 15: Ent Team
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Ent Team
- **Key Sections Identified**:
    - Header
    - ISV RVP - Gary Revenue Data
    - Putlock, Gary Revenue Data
    - Sabikihi, Harsh Revenue Data
    - Sabikihi/NYC ENT RVP Revenue Data
    - Miller, BJ Revenue Data
    - Tuttle, Patrick Revenue Data
    - Yatsko, Natalie Revenue Data
    - Wilson, Matt Revenue Data

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains labels for the data sections below, including headcount, ramped headcount, and quota.
- **Cell Range**: R3:AT3
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: R3:AT3
    - **Data Range**: None
- **Time Series Details**: None
- **Key Components**: Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: This section provides context for the data presented in the subsequent sections.

### ISV RVP - Gary Revenue Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains revenue data for ISV RVP - Gary team members.
- **Cell Range**: B7:CA20
- **Layout Structure**:
    - **Row Headers Location**: B7:B20, D7:D20
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5, BI5:BQ5, BS5:CA5
    - **Data Range**:
      - Monthly data (E5:P5): E7:P20
      - Monthly data (R5:Z5): AY7:BG20, BI7:BQ20, BS7:CA20
- **Time Series Details**:
    - Monthly: 2021-02-01 to 2022-01-01 (E5:P5)
        - Frequency: Monthly
    - Monthly: 2021-05-01 to 2022-01-01 (R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5, BI5:BQ5, BS5:CA5)
        - Frequency: Monthly
- **Key Components**: Team member names (e.g., Trevor Usken, Charlie Holliday), Revenue metrics.
- **Notes & Customizations**: Revenue data is scaled by 1000. There are multiple monthly time series.

### Putlock, Gary Revenue Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains revenue data for Putlock, Gary team members.
- **Cell Range**: B22:CA35
- **Layout Structure**:
    - **Row Headers Location**: B22:B35, D22:D35
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5, BI5:BQ5, BS5:CA5
    - **Data Range**:
      - Monthly data (E5:P5): E22:P35
      - Monthly data (R5:Z5): AY22:BG35, BI22:BQ35, BS22:CA35
- **Time Series Details**:
    - Monthly: 2021-02-01 to 2022-01-01 (E5:P5)
        - Frequency: Monthly
    - Monthly: 2021-05-01 to 2022-01-01 (R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5, BI5:BQ5, BS5:CA5)
        - Frequency: Monthly
- **Key Components**: Team member names (e.g., Bob Ternes, Nick Valldeperas), Revenue metrics.
- **Notes & Customizations**: Revenue data is scaled by 1000. There are multiple monthly time series.

### Sabikihi, Harsh Revenue Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains revenue data for Sabikihi, Harsh team members.
- **Cell Range**: B37:AT50
- **Layout Structure**:
    - **Row Headers Location**: B37:B50, D37:D50
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
      - Monthly data (E5:P5): E37:P50
      - Monthly data (R5:Z5): R37:Z50, AB37:AJ50, AL37:AT50
- **Time Series Details**:
    - Monthly: 2021-02-01 to 2022-01-01 (E5:P5)
        - Frequency: Monthly
    - Monthly: 2021-05-01 to 2022-01-01 (R5:Z5, AB5:AJ5, AL5:AT5)
        - Frequency: Monthly
- **Key Components**: Team member names (e.g., Dave Grinnell), Revenue metrics.
- **Notes & Customizations**: Revenue data is scaled by 1000. There are multiple monthly time series.

### Sabikihi/NYC ENT RVP Revenue Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains revenue data for Sabikihi/NYC ENT RVP team members.
- **Cell Range**: B52:AT65
- **Layout Structure**:
    - **Row Headers Location**: B52:B65, D52:D65
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
      - Monthly data (E5:P5): E52:P65
      - Monthly data (R5:Z5): R52:Z65, AB52:AJ65, AL52:AT65
- **Time Series Details**:
    - Monthly: 2021-02-01 to 2022-01-01 (E5:P5)
        - Frequency: Monthly
    - Monthly: 2021-05-01 to 2022-01-01 (R5:Z5, AB5:AJ5, AL5:AT5)
        - Frequency: Monthly
- **Key Components**: Team member names (e.g., Kathleen Evans, Leah Koren), Revenue metrics.
- **Notes & Customizations**: Revenue data is scaled by 1000. There are multiple monthly time series.

### Miller, BJ Revenue Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains revenue data for Miller, BJ team members.
- **Cell Range**: B67:AT80
- **Layout Structure**:
    - **Row Headers Location**: B67:B80, D67:D80
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
      - Monthly data (E5:P5): E67:P80
      - Monthly data (R5:Z5): R67:Z80, AB67:AJ80, AL67:AT80
- **Time Series Details**:
    - Monthly: 2021-02-01 to 2022-01-01 (E5:P5)
        - Frequency: Monthly
    - Monthly: 2021-05-01 to 2022-01-01 (R5:Z5, AB5:AJ5, AL5:AT5)
        - Frequency: Monthly
- **Key Components**: Team member names (e.g., David Curtis, Shioban Lawler), Revenue metrics.
- **Notes & Customizations**: Revenue data is scaled by 1000. There are multiple monthly time series.

### Tuttle, Patrick Revenue Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains revenue data for Tuttle, Patrick team members.
- **Cell Range**: B82:AT95
- **Layout Structure**:
    - **Row Headers Location**: B82:B95, D82:D95
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
      - Monthly data (E5:P5): E82:P95
      - Monthly data (R5:Z5): R82:Z95, AB82:AJ95, AL82:AT95
- **Time Series Details**:
    - Monthly: 2021-02-01 to 2022-01-01 (E5:P5)
        - Frequency: Monthly
    - Monthly: 2021-05-01 to 2022-01-01 (R5:Z5, AB5:AJ5, AL5:AT5)
        - Frequency: Monthly
- **Key Components**: Team member names (e.g., Joe Zusin, Chris Freeman), Revenue metrics.
- **Notes & Customizations**: Revenue data is scaled by 1000. There are multiple monthly time series.

### Yatsko, Natalie Revenue Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains revenue data for Yatsko, Natalie team members.
- **Cell Range**: B97:AT110
- **Layout Structure**:
    - **Row Headers Location**: B97:B110, D97:D110
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
      - Monthly data (E5:P5): E97:P110
      - Monthly data (R5:Z5): R97:Z110, AB97:AJ110, AL97:AT110
- **Time Series Details**:
    - Monthly: 2021-02-01 to 2022-01-01 (E5:P5)
        - Frequency: Monthly
    - Monthly: 2021-05-01 to 2022-01-01 (R5:Z5, AB5:AJ5, AL5:AT5)
        - Frequency: Monthly
- **Key Components**: Team member names (e.g., Bob Ternes, Fay Hernandez), Revenue metrics.
- **Notes & Customizations**: Revenue data is scaled by 1000. There are multiple monthly time series.

### Wilson, Matt Revenue Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains revenue data for Wilson, Matt team members.
- **Cell Range**: B112:AT125
- **Layout Structure**:
    - **Row Headers Location**: B112:B125, D112:D125
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
      - Monthly data (E5:P5): E112:P125
      - Monthly data (R5:Z5): R112:Z125, AB112:AJ125, AL112:AT125
- **Time Series Details**:
    - Monthly: 2021-02-01 to 2022-01-01 (E5:P5)
        - Frequency: Monthly
    - Monthly: 2021-05-01 to 2022-01-01 (R5:Z5, AB5:AJ5, AL5:AT5)
        - Frequency: Monthly
- **Key Components**: Team member names (e.g., Trevor Usken, Charlie Holliday), Revenue metrics.
- **Notes & Customizations**: Revenue data is scaled by 1000. There are multiple monthly time series.



====================================================================================================
# SHEET 16: SS Team
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: SS Team
- **Key Sections Identified**:
    - SS Corp Dir Headcount and Quota
    - SS Comm Dir Headcount and Quota

## 2. Detailed Section Analysis

### Section Name: SS Corp Dir Headcount and Quota
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount and quota information for the SS Corp Dir team, including individual team members and future hires. It allows for monitoring team size, ramp-up, and performance targets.
- **Cell Range**: B7:BG20
- **Layout Structure**:
    - **Row Headers Location**: B7:B20 (Names of team members: Bumgardner, Josh)
    - **Column Headers Location**: E5:P5 (Monthly dates), R3 (Headcount), AB3 (Ramped Headcount), AL3 (Quota), AY5:BG5 (Monthly dates)
    - **Data Range**:
      - Monthly data (Headcount): E7:P20
      - Monthly data (Quota): AY7:BG20
      - Headcount data: R7:Z20
      - Ramped Headcount data: AB7:AJ20
      - Quota data: AL7:AT20
- **Time Series Details**:
    - **Date Range**:
      - Monthly (Headcount): 2021-02-01 to 2022-01-01
      - Monthly (Quota): 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Monthly
      - Monthly
- **Key Components**: Team member names, Headcount, Ramped Headcount, Quota.
- **Notes & Customizations**: Headcount and Quota are tracked on a monthly basis. Headcount, Ramped Headcount, and Quota are scaled by 1000.

### Section Name: SS Comm Dir Headcount and Quota
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section tracks the headcount and quota information for the SS Comm Dir team, including individual team members and future hires. It allows for monitoring team size, ramp-up, and performance targets.
- **Cell Range**: B37:AT50
- **Layout Structure**:
    - **Row Headers Location**: B37:B50 (Names of team members: TBD SS Comm Dir)
    - **Column Headers Location**: E5:P5 (Monthly dates), R3 (Headcount), AB3 (Ramped Headcount), AL3 (Quota)
    - **Data Range**:
      - Monthly data: E37:P50
      - Headcount data: R37:Z50
      - Ramped Headcount data: AB37:AJ50
      - Quota data: AL37:AT50
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2021-02-01 to 2022-01-01
      - Monthly: 2021-05-01 to 2022-01-01
    - **Frequency**:
      - Monthly
      - Monthly
- **Key Components**: Team member names, Headcount, Ramped Headcount, Quota.
- **Notes & Customizations**: Headcount and Quota are tracked on a monthly basis. Headcount, Ramped Headcount, and Quota are scaled by 1000.


====================================================================================================
# SHEET 17: EMEA Team
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: EMEA Team
- **Key Sections Identified**:
    - Header
    - SMB Team Data
    - Foundation Team Data
    - Growth Team Data
    - Enterprise Team Data
    - SubServ Team Data

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains titles and labels for the entire sheet, including "Headcount", "Ramped Headcount", and "Quota".
- **Cell Range**: A1:BG5
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5
    - **Data Range**: None
- **Time Series Details**:
    - Monthly (E5:P5): 2021-02-01 to 2022-01-01
    - Monthly (R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5): 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Headcount, Ramped Headcount, Quota, Date Headers
- **Notes & Customizations**: Contains two distinct monthly time series.

### SMB Team Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the SMB team members.
- **Cell Range**: B7:BG20
- **Layout Structure**:
    - **Row Headers Location**: B7:B20
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5
    - **Data Range**:
      - Monthly data: E7:P7, R7:Z7, AB7:AJ7, AL7:AT7, AY7:BG7, T8:Z8, AD8:AJ8, AN8:AT8, AY8:BG8, U9:Z9, AE9:AJ9, AO9:AT9, AY9:BG9, Z10, AJ10, AT10, AY10:BG10, AY11:BG11, AY12:BG12, AY13:BG13, AY14:BG14, AY15:BG15, AY16:BG16, AY17:BG17
- **Time Series Details**:
    - Monthly (E5:P5): 2021-02-01 to 2022-01-01
    - Monthly (R5:Z5, AB5:AJ5, AL5:AT5, AY5:BG5): 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Team Member Names, Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000.

### Foundation Team Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the Foundation team members.
- **Cell Range**: B22:AT35
- **Layout Structure**:
    - **Row Headers Location**: B22:B35
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
      - Monthly data: E22:P22, R22:Z22, AB22:AJ22, AL22:AT22, E23:J23, R23:Z23, AB23:AJ23, AL23:AT23, E24:J24, R24:Z24, AB24:AJ24, AL24:AT24, H25:J25, R25:Z25, AB25:AJ25, AL25:AT25, U26:Z26, AE26:AJ26, AO26:AT26, U27:Z27, AE27:AJ27, AO27:AT27
- **Time Series Details**:
    - Monthly (E5:P5): 2021-02-01 to 2022-01-01
    - Monthly (R5:Z5, AB5:AJ5, AL5:AT5): 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Team Member Names, Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000.

### Growth Team Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the Growth team members.
- **Cell Range**: B37:AT50
- **Layout Structure**:
    - **Row Headers Location**: B37:B50
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
      - Monthly data: E37:P37, R37:Z37, AB37:AJ37, AL37:AT37, E38:P38, R38:Z38, AB38:AJ38, AL38:AT38, K39:M39, N40:O40, R39:Z39, AB39:AJ39, AL39:AT39, X40:Z40, AH40:AJ40, AR40:AT40, Z41, AJ41, AT41
- **Time Series Details**:
    - Monthly (E5:P5): 2021-02-01 to 2022-01-01
    - Monthly (R5:Z5, AB5:AJ5, AL5:AT5): 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Team Member Names, Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000.

### Enterprise Team Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the Enterprise team members.
- **Cell Range**: B52:AT65
- **Layout Structure**:
    - **Row Headers Location**: B52:B65
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
      - Monthly data: E52:P52, R52:Z52, AB52:AJ52, AL52:AT52, E53:P53, R53:Z53, AB53:AJ53, AL53:AT53, K54:P54, U54:Z54, AE54:AJ54, AO54:AT54, K55:P55, U55:Z55, AE55:AJ55, AO55:AT55, K56:P56, U56:Z56, AE56:AJ56, AO56:AT56
- **Time Series Details**:
    - Monthly (E5:P5): 2021-02-01 to 2022-01-01
    - Monthly (R5:Z5, AB5:AJ5, AL5:AT5): 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Team Member Names, Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000.

### SubServ Team Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains headcount, ramped headcount and quota data for the SubServ team members.
- **Cell Range**: B67:AT80
- **Layout Structure**:
    - **Row Headers Location**: B67:B80
    - **Column Headers Location**: E5:P5, R5:Z5, AB5:AJ5, AL5:AT5
    - **Data Range**:
      - Monthly data: E67:P67, R67:Z67, AB67:AJ67, AL67:AT67, U68:Z68, AE68:AJ68, AO68:AT68
- **Time Series Details**:
    - Monthly (E5:P5): 2021-02-01 to 2022-01-01
    - Monthly (R5:Z5, AB5:AJ5, AL5:AT5): 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Team Member Names, Headcount, Ramped Headcount, Quota
- **Notes & Customizations**: Data is scaled by 1000.



====================================================================================================
# SHEET 18: Targets
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Targets
- **Key Sections Identified**:
    - Budget Total QoS
    - Budget Total Bookings
    - CRO Target
    - VP Target
    - Manager Target (Budget-based)
    - Starting Point for Attainment Targets
    - Manager Attainment

## 2. Detailed Section Analysis

### Section Name: Budget Total QoS
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the budget targets for Total QoS, broken down by quarter and fiscal year, for different customer segments. It is used for setting and tracking performance goals.
- **Cell Range**: B2:G20
- **Layout Structure**:
    - **Row Headers Location**: B4:B20
    - **Column Headers Location**: C3:G3
    - **Data Range**: C5:G20
- **Time Series Details**:
    - **Date Range**: Q1 to FY
    - **Frequency**: Quarterly
- **Key Components**: Core, Commercial, Corporate, Enterprise, SubSuccess, Emerging, Adopt1, VoC, DAP, ANZ, EMEA, JPN, Total
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Budget Total Bookings
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the budget targets for Total Bookings, broken down by quarter and fiscal year, for different customer segments. It is used for setting and tracking performance goals.
- **Cell Range**: I2:M20
- **Layout Structure**:
    - **Row Headers Location**: B4:B20
    - **Column Headers Location**: I3:M3
    - **Data Range**: I5:M20
- **Time Series Details**:
    - **Date Range**: Q1 to FY
    - **Frequency**: Quarterly
- **Key Components**: Core, Commercial, Corporate, Enterprise, SubSuccess, Emerging, Adopt1, VoC, DAP, ANZ, EMEA, JPN, Total
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: CRO Target
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the CRO targets, broken down by quarter and fiscal year, for different customer segments. It is used for setting and tracking performance goals.
- **Cell Range**: O2:S20
- **Layout Structure**:
    - **Row Headers Location**: B4:B20
    - **Column Headers Location**: O3:S3
    - **Data Range**: O5:S20
- **Time Series Details**:
    - **Date Range**: Q1 to FY
    - **Frequency**: Quarterly
- **Key Components**: Core, Commercial, Corporate, Enterprise, SubSuccess, Emerging, Adopt1, VoC, DAP, ANZ, EMEA, JPN, Total
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: VP Target
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the VP targets, broken down by quarter and fiscal year, for different customer segments. It is used for setting and tracking performance goals.
- **Cell Range**: V2:Y20
- **Layout Structure**:
    - **Row Headers Location**: B4:B20
    - **Column Headers Location**: U3:Y3
    - **Data Range**: U5:Y20
- **Time Series Details**:
    - **Date Range**: Q1 to FY
    - **Frequency**: Quarterly
- **Key Components**: Core, Commercial, Corporate, Enterprise, SubSuccess, Emerging, Adopt1, VoC, DAP, ANZ, EMEA, JPN, Total
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Manager Target (Budget-based)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the Manager targets, broken down by quarter and fiscal year, for different customer segments. It is used for setting and tracking performance goals.
- **Cell Range**: AB2:AE20
- **Layout Structure**:
    - **Row Headers Location**: B4:B20
    - **Column Headers Location**: AA3:AE3
    - **Data Range**: AA5:AE20
- **Time Series Details**:
    - **Date Range**: Q1 to FY
    - **Frequency**: Quarterly
- **Key Components**: Core, Commercial, Corporate, Enterprise, SubSuccess, Emerging, Adopt1, VoC, DAP, ANZ, EMEA, JPN, Total
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name: Starting Point for Attainment Targets
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the starting point for attainment targets, broken down by quarter, for different customer segments and roles (Co., CRO, Manager, VP). It is used as a baseline for calculating attainment.
- **Cell Range**: B24:V44
- **Layout Structure**:
    - **Row Headers Location**: B28:B44
    - **Column Headers Location**: D26:V27
    - **Data Range**: D29:V44
- **Time Series Details**:
    - **Date Range**: Q1 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Core, Commercial, Corporate, Enterprise, SubSuccess, Emerging, Adopt1, VoC, DAP, ANZ, EMEA, JPN, Total, Co., CRO, Manager, VP
- **Notes & Customizations**: The column headers are split across rows 26 and 27.

### Section Name: Manager Attainment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section displays the Manager attainment, broken down by quarter, for different customer segments. It is used for tracking performance against targets.
- **Cell Range**: B48:G66
- **Layout Structure**:
    - **Row Headers Location**: B50:B66
    - **Column Headers Location**: D49:G49
    - **Data Range**: D51:G66
- **Time Series Details**:
    - **Date Range**: Q1 to Q4
    - **Frequency**: Quarterly
- **Key Components**: Core, Commercial, Corporate, Enterprise, SubSuccess, Emerging, Adopt1, VoC, DAP, ANZ, EMEA, JPN, Total
- **Notes & Customizations**: The row labels include "BD" in B61.


====================================================================================================
# SHEET 19: FY22 QoS
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: FY22 QoS
- **Key Sections Identified**:
    - Plan Name and Quota Table
    - Employee Headcount and Quota Details
    - Summary Metrics

## 2. Detailed Section Analysis

### Plan Name and Quota Table
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section defines the planned quotas for different roles and segments within the organization. It's used for setting targets and tracking performance.
- **Cell Range**: A1:K52
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 1
    - **Data Range**: B2:J52 (numeric values)
- **Time Series Details**:
    - **Date Range**: Not a time series.
    - **Frequency**: N/A
- **Key Components**: Plan Name, Fully Ramped Quota, Adopt, Sr Adopt, Corporate, Commercial, Sr Commercial, Commercial Select, Enterprise, SubSuccess - Corporate, SubSuccess - Commercial, EMEA, BizDev, DAP - Corporate, DAP- Commercial, VoC - Corporate, VoC- Commercial.
- **Notes & Customizations**: The "Fully Ramped Quota" is scaled by 1000.

### Employee Headcount and Quota Details
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section lists individual employees, their roles, managers, regions, and quota information. It's used for detailed headcount planning and performance tracking.
- **Cell Range**: A55:CC293
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: Row 55
    - **Data Range**:
      - Headcount data: K56:V293
      - Quota data: W56:AY293
      - Monthly data: BE56:BP293
      - Quarterly data: BR56:CC293
- **Time Series Details**:
    - **Date Range**:
      - Monthly: 2021-02-28 to 2022-01-31 (BE55:BP55 and BR55:CC55)
    - **Frequency**:
      - Monthly
- **Key Components**: Name, Term Date, Plan, Manager, Region, Position Status, FY22 Quota, Ramp Start Month, Q1FY22, Q2FY22, Q3FY22, Q4FY22, FY22 Ramped Quota, Manager (Clean), Headcount (Clean).
- **Notes & Customizations**: FY22 Quota is scaled by 1000. There are multiple date columns present: Term Date (column C), Ramp Start Month (column J), and monthly columns (BE:BP and BR:CC).

### Summary Metrics
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section provides summary metrics related to QoS and headcount, both including and excluding terminated employees.
- **Cell Range**: J294:AT319
- **Layout Structure**:
    - **Row Headers Location**: Column AI
    - **Column Headers Location**: Row K
    - **Data Range**:
      - Ramped Headcount: K297:V301
      - QoS: AI297:AT301
      - Ramped Headcount (incl term): K304:AH308
      - QoS (incl term): AI304:AT308
      - Attrition Factor: AI311:AT315
- **Time Series Details**:
    - **Date Range**: Not a time series.
    - **Frequency**: N/A
- **Key Components**: QoS (excl term), Ramped Headcount (incl term), QoS (incl term), Attrition Factor.
- **Notes & Customizations**: Ramped Headcount and QoS are scaled by 1000.


====================================================================================================
# SHEET 20: FY22 Overlay
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: FY22 Overlay
- **Key Sections Identified**:
    - Header
    - Sales Rep Data
    - Quarterly Quota Attainment

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains column labels defining the data in subsequent rows. Provides context for understanding the data.
- **Cell Range**: A1:AM1
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: A1:AM1
    - **Data Range**: None
- **Time Series Details**:
    - **Date Range**: Q1FY22 to Q4FY22
    - **Frequency**: Quarterly
- **Key Components**: Name, Term Date, Plan, Segment, Manager, Region, Position Status, FY22 Quota, Ramp Start Month, Q1FY22, Q2FY22, Q3FY22, Q4FY22, FY22 Ramped Quota
- **Notes & Customizations**: "FY22" likely refers to Fiscal Year 2022.

### Sales Rep Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains information about individual sales representatives, including their plan, segment, manager, region, quota, and ramp-up details.
- **Cell Range**: A2:J6
- **Layout Structure**:
    - **Row Headers Location**: A2:A6 (Name), D2:D6 (Plan), E2:E6 (Segment), F2:F6 (Manager), G2:G6 (Region), H2:H6 (Position Status)
    - **Column Headers Location**: A1:J1
    - **Data Range**: B2:B6, C2:C6, D2:D6, E2:E6, F2:F6, G2:G6, H2:H6, I2:I6, J2:J6
- **Time Series Details**: None
- **Key Components**: Name, Term Date, Plan, Segment, Manager, Region, Position Status, FY22 Quota, Ramp Start Month
- **Notes & Customizations**: "Future Hire" is a possible value for "Position Status." Quota is scaled by 1000.

### Quarterly Quota Attainment
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains quarterly quota attainment data for each sales representative.
- **Cell Range**: AI1:AM6
- **Layout Structure**:
    - **Row Headers Location**: A2:A6 (Implied Sales Rep Names)
    - **Column Headers Location**: AI1:AM1
    - **Data Range**: AI2:AM6
- **Time Series Details**:
    - **Date Range**: Q1FY22 to Q4FY22
    - **Frequency**: Quarterly
- **Key Components**: Q1FY22, Q2FY22, Q3FY22, Q4FY22, FY22 Ramped Quota
- **Notes & Customizations**: Values are scaled by 1000.



====================================================================================================
# SHEET 21: Comm Model
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Comm Model
- **Key Sections Identified**:
    - Corporate Forecast Details (Headcount)
    - Ramp Build - Corporate (Headcount Changes)
    - Ramped Team Adjustment
    - Inputs (Plan Data)

## 2. Detailed Section Analysis

### Section Name (Corporate Forecast Details (Headcount))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section outlines the forecast for gross and net headcount, both overall and ramped, for the Corporate team. It provides a high-level overview of headcount planning.
- **Cell Range**: C4:AE14
- **Layout Structure**:
    - **Row Headers Location**: Column C (e.g., "Total QoS", "Average Quota", "Gross Headcount", "Net Headcount")
    - **Column Headers Location**: Row 5 (implicitly defined by the date series in row 19)
    - **Data Range**:
      - Monthly data: `W5:AE14`
- **Time Series Details**:
    - **Date Range**: 2020-02-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Total QoS, Average Quota, Gross Headcount, Attrition, Net Headcount, Gross Ramped Headcount, Net Ramped Headcount.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Ramp Build - Corporate (Headcount Changes))
- **Section Type**: Waterfall Chart Data
- **Description & Purpose**: This section details the ramp-up of the Corporate team, showing the beginning headcount, additions, removals, and ending headcount for each month.
- **Cell Range**: C19:AE24
- **Layout Structure**:
    - **Row Headers Location**: Column C (e.g., "Ramp Build - Corporate", "Beginning of Period", "Added", "Removed", "End of Period")
    - **Column Headers Location**: Row 19 (monthly dates)
    - **Data Range**:
      - Monthly data: `H21:AE24`
- **Time Series Details**:
    - **Date Range**: 2020-02-01 to 2022-01-01 (based on date series in row 19)
    - **Frequency**: Monthly
- **Key Components**: Beginning of Period Headcount, Added Headcount, Removed Headcount, End of Period Headcount.
- **Notes & Customizations**: "Assume 1 headcount attrition spread over year for promos out (offset by ramped heads coming in)" in cell AG22. Values in F21, F22, F23, F24 are also part of the section.

### Section Name (Ramp)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details the ramp and efficiency metrics for the Corporate team, showing the monthly ramp and efficiency values.
- **Cell Range**: C26:AE36
- **Layout Structure**:
    - **Row Headers Location**: Columns C and D (e.g., "Ramp", "Efficiency", "Attrition")
    - **Column Headers Location**: Row 26 (monthly dates)
    - **Data Range**:
      - Monthly data: `I27:AE36`
- **Time Series Details**:
    - **Date Range**: 2020-02-01 to 2022-01-01 (based on date series in row 26)
    - **Frequency**: Monthly
- **Key Components**: Month 1, Month 2, Month 3, Month 4, Month 5, Month 6, Month 7, Month 8, Month 9, Attrition.
- **Notes & Customizations**: Values are scaled by 1000.

### Section Name (Ramped Team Adjustment)
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section details adjustments to the ramped team, including effective start, add, and effective end values.
- **Cell Range**: C38:AE41
- **Layout Structure**:
    - **Row Headers Location**: Column C (e.g., "Effective Start", "Add", "Effective End")
    - **Column Headers Location**: Row 38 (monthly dates)
    - **Data Range**:
      - Monthly data: `H39:AE41`
- **Time Series Details**:
    - **Date Range**: 2020-02-01 to 2022-01-01 (based on date series in row 38)
    - **Frequency**: Monthly
- **Key Components**: Effective Start, Add, Effective End.
- **Notes & Customizations**: Includes adjustment factors in columns AG and AH. Values are scaled by 1000.

### Section Name (Inputs (Plan Data))
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section contains plan data inputs, including headcount and attainment metrics for different categories.
- **Cell Range**: M43:S65
- **Layout Structure**:
    - **Row Headers Location**: Column M (e.g., "Attrition", "Quota", "Ramped", "Q1 Attnmt", "Q2 Attnmt", "Q3 Attnmt", "Q4 Attnmt")
    - **Column Headers Location**: Row 44 (e.g., "Active", "Commercial", "Corporate", "Enterprise", "SS Corp", "SS Comm")
    - **Data Range**: `N45:S65`
- **Time Series Details**: No time series detected in this section.
- **Frequency**: N/A
- **Key Components**: Attrition, Quota, Ramped, Q1 Attnmt, Q2 Attnmt, Q3 Attnmt, Q4 Attnmt.
- **Notes & Customizations**: Values are scaled by 1000 where applicable.



====================================================================================================
# SHEET 22: Corp Model
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Corp Model
- **Key Sections Identified**:
    - Header
    - Corporate Forecast Details
    - Corporate: Full Team Headcount
    - Corporate: Ramped Team - Value Team
    - Ramp Build - Corporate
    - Inputs

## 2. Detailed Section Analysis

### Header
- **Section Type**: Header
- **Description & Purpose**: Contains the title of the report.
- **Cell Range**: B2:B2
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: None
    - **Data Range**: B2:B2
- **Time Series Details**: None
- **Key Components**: Corporate: Forecast Details
- **Notes & Customizations**: None

### Corporate Forecast Details
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Summarizes key headcount metrics derived from the QoS model.
- **Cell Range**: C4:AE14
- **Layout Structure**:
    - **Row Headers Location**: C4:C14
    - **Column Headers Location**: W5:AE5 (Implicit monthly dates)
    - **Data Range**:
      - Monthly data: W8:AE14
- **Time Series Details**:
    - **Date Range**: 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Total QoS, Average Quota, Gross Headcount, Attrition, Net Headcount, Gross Ramped Headcount, Attrition, Net Ramped Headcount
- **Notes & Customizations**: Values are scaled by 1000.

### Corporate: Full Team Headcount
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the headcount for the full corporate team, broken down by individuals and teams.
- **Cell Range**: B17:AH49
- **Layout Structure**:
    - **Row Headers Location**: C19:C41, AH20:AH23, AH30:AH31, AH44:AH46
    - **Column Headers Location**: W19:AE19 (Monthly dates)
    - **Data Range**:
      - Monthly data: W20:AE25, W28:AE31, W38:AE41, W45:AE46, W49:AE49, AC44:AE44, AG30:AG31, AG44:AG46
- **Time Series Details**:
    - **Date Range**: 2021-05-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Total Headcount (Net), Batt, Kate, Hoy, Michael, Klemm, Brian, TBD Corp Dir #2, John Gresham, Value Team, Full Team, Value, PFSU, Total Corporate (from QoS), Ramped Headcount - Adjusted (Attrition), Attrition Adjustment - Value
- **Notes & Customizations**: Values are scaled by 1000. PFSU Transition only has data from Z40:AE40.

### Corporate: Ramped Team - Value Team
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Details the ramp build for the corporate value team.
- **Cell Range**: B52:AE76
- **Layout Structure**:
    - **Row Headers Location**: C54:C59, C61:C71, C74:C76
    - **Column Headers Location**: H54:AE54, H61:AE61, H73:AE73 (Monthly dates)
    - **Data Range**:
      - Monthly data: H56:AE59, I62:AE71, H74:AE76, D57:E70, F56:F59, F74:F76, AG74:AG75
- **Time Series Details**:
    - **Date Range**: 2020-02-01 to 2022-01-01
    - **Frequency**: Monthly
- **Key Components**: Ramp Build - Corporate, Beginning of Period, Added, Removed, End of Period, Ramp, Attrition, Effective Start, Add, Effective End
- **Notes & Customizations**: Values are scaled by 1000.

### Inputs
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Input assumptions for the model.
- **Cell Range**: B78:S100
- **Layout Structure**:
    - **Row Headers Location**: C80, M93:M100
    - **Column Headers Location**: N79:S79, N92:S92 (Categories)
    - **Data Range**: N80:S88, N93:S100
- **Time Series Details**: None
- **Key Components**: Plan, Active, Commercial, Corporate, Enterprise, SS Corp, SS Comm, Quota, Attrition, Ramped, Q1 Attnmt, Q2 Attnmt, Q3 Attnmt, Q4 Attnmt
- **Notes & Customizations**: None



====================================================================================================
# SHEET 23: Clean
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Clean
- **Key Sections Identified**:
    - Roster Header
    - Employee Roster Data
    - Ramped Headcount Data

## 2. Detailed Section Analysis

### Roster Header
- **Section Type**: Header
- **Description & Purpose**: Contains the column headers for the employee roster data. Defines the structure and meaning of the columns.
- **Cell Range**: B5:BI7
- **Layout Structure**:
    - **Row Headers Location**: None
    - **Column Headers Location**: B5:BI7
    - **Data Range**: None
- **Time Series Details**:
    - Monthly: 2021-02-01 to 2022-01-01
        - **Frequency**: Monthly
- **Key Components**: Roster, Ramped HC, Manager, Employee, Hire Date, Term Date, Role, Quota, Updated Name, Updated Manager, Monthly dates
- **Notes & Customizations**: Contains both static column headers (e.g., "Manager", "Employee") and a series of monthly date headers.

### Employee Roster Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains the employee roster data, including manager, employee name, hire date, term date, role, and quota. Used for tracking employee information and headcount.
- **Cell Range**: B8:G65
- **Layout Structure**:
    - **Row Headers Location**: B8:C65 (Manager, Employee)
    - **Column Headers Location**: B7:G7 (Manager, Employee, Hire Date, Term Date, Role, Quota)
    - **Data Range**:
      - Static Data: D8:G65
- **Time Series Details**:
    - Hire Date: 2018-04-16 to 2021-12-01
        - **Frequency**: Unordered
    - Term Date: 2021-02-28 to 2021-07-30
        - **Frequency**: Unordered
- **Key Components**: Manager, Employee, Hire Date, Term Date, Role, Quota
- **Notes & Customizations**: Includes employee transfers and future hires.

### Ramped Headcount Data
- **Section Type**: Key Metrics Table
- **Description & Purpose**: Contains the ramped headcount data, showing headcount and quota information over a monthly time series.
- **Cell Range**: K5:BI65
- **Layout Structure**:
    - **Row Headers Location**: K5, AX5 (Headcount)
    - **Column Headers Location**: K7:BI7 (Monthly Dates)
    - **Data Range**:
      - Monthly Data: K8:BI65
- **Time Series Details**:
    - Monthly: 2021-02-01 to 2022-01-01
        - **Frequency**: Monthly
- **Key Components**: Headcount, Quota, Monthly Headcount/Quota values
- **Notes & Customizations**: Data is scaled by 1000.


====================================================================================================
# SHEET 24: Sheet4
====================================================================================================

## 1. Spreadsheet Overview
- **Sheet Name**: Sheet4
- **Key Sections Identified**:
    - Employee List

## 2. Detailed Section Analysis

### Employee List
- **Section Type**: Key Metrics Table
- **Description & Purpose**: This section lists employee names. It is likely used as a reference table for other calculations or reports within the workbook.
- **Cell Range**: A2:A12
- **Layout Structure**:
    - **Row Headers Location**: Column A
    - **Column Headers Location**: None
    - **Data Range**: A2:A12
- **Time Series Details**:
    - **Date Range**: N/A
    - **Frequency**: N/A
- **Key Components**: Employee Names
- **Notes & Customizations**: This is a simple list with no apparent calculations or time series data.
