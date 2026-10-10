# Script Technical Documentation & Relational Pipeline Brief
**Project:** Corporate Pension Fund ALM & Solvency Stress-Tester  
**Pipeline Module Name:** Corporate Pension Liability Spine Engine  
**Lead Analyst:** Lenny Wanjiru | *Dedan Kimathi University of Technology (DeKUT)*  
**Core Infrastructure:** Python SQL Pipeline Interface (`02_run_sql_pipeline.py`)



## 1. Structural Assumptions & Core Math
To extract a deterministic multi-decade cash outflow profile and isolate precise portfolio liquidity risks, the pipeline maps individual participant attributes using clear actuarial boundaries:

1.  **Retirement Horizon Threshold:** All active cohort participants are modeled to transition seamlessly from active to retired status exactly on their 65th birthday.
2.  **Actuarial Benefit Formula (Defined Benefit Structure):** Annual lifetime retirement benefit allocations are determined using an un-indexed linear accumulation rule:
    \[\text{Annual Pension Payout} = 0.015 \times (\text{Years of Service} + \text{Years to Retirement}) \times \text{Salary}\]
3.  **Service Accrual Dynamics:** Active records add exactly 1.0 year of pensionable service credit for every continuous calendar year they remain active prior to hitting Age 65.
4.  **Baseline Longevity Horizon:** Post-retirement lifespan is fixed at exactly 20 years across all cohorts. Single-person annuity payouts are distributed continuously from Age 65 through Age 84.
5.  **Temporal Timeline Anchor:** The baseline valuation timeline initialization clock begins in the current year, 2026.



## 2. Baseline Model Execution Results
The table below maps the structural macro inflection milestones calculated dynamically by the relational database query window functions from the 1,000 synthetic employee cohort profiles:

| Calendar Year | Active Retirees Drawing Pension | Total Annual Liability Outflow (\$) | Cumulative Liability Drain (\$) | Fund Risk Status |
| :--- | :---: | :---: | :---: | :--- |
| **2027** | 48 | 1,342,358.28 | 1,342,358.28 | Active Payout Phase |
| **2035** | 174 | 5,030,389.15 | 26,945,632.81 | Active Payout Phase |
| **2045** | 555 | 17,303,597.68 | 137,255,673.41 | Active Payout Phase |
| **2050** | 645 | 21,171,545.27 | 233,214,272.94 | Active Payout Phase |
| **2055** | 701 | 24,286,918.05 | 350,421,763.56 |  PEAK CASH DEMAND YEAR |
| **2060** | 619 | 22,814,936.97 | 467,721,366.57 | Active Payout Phase |
| **2066** | 411 | 16,167,353.40 | 580,559,727.68 | Terminal Wind-down Phase |



## 3. Actuarial Interpretation & Strategic Insights

### Demographic Concentration Risk
The relational model isolates an aggressive, exponential slope in annual benefit liabilities beginning in the late 2030s and climbing to its maximum intensity in the year 2055. This acceleration is driven entirely by a massive structural demographic cluster of middle-aged active personnel (currently aged 35–45) who move into retirement within the same compact 10-year window. This concentration creates an acute systemic liquidity challenge that the fund's asset base must be engineered to survive.

### Asset-Liability Matching (ALM) Matrix
1.  **Immunization Mandate:** Because our primary corporate pension liability out-flows are heavily back-loaded—climbing from \$1.3M in 2027 to over \$24M by 2055—the investment framework must avoid locking core capital into short-term, low-yield vehicles during the early years. The portfolio requires an aggressive equity compounding phase over the next 15 years to outpace the mounting liability curve.
2.  **The Liquidity Pivot Point:** As the calendar timeline passes the **Year 2045 threshold**, the asset allocation strategy must execute a systematic de-risking roadmap. Portfolio managers must step out of highly volatile equities and build a protective cash and short-duration bond ladder to fully match the massive \$24M annual obligations, guaranteeing payment liquidity without running the risk of a forced asset sale during an unexpected market correction.
