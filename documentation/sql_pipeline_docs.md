# Phase 1: Liability Timeline Generation & Cash Demand Engine

## 📋 1. Script Technical Documentation
* **Pipeline Name:** Corporate Pension Liability Spine
* **Engine Type:** Relational Database Workflow (SQL Core embedded via Python)
* **Execution Script:** `scripts/02_run_sql_pipeline.py` / `scripts/02_liability_projection.sql`
* **Primary Target:** Map the exact 40-year cash outflow profile of the pension fund to pinpoint liquidity risk concentrations.

### 📐 Structural Assumptions & Core Math
1. **Normal Retirement Horizon:** Employees retire exactly on their **65th birthday**.
2. **Benefit Formula (Defined Benefit):** 
   \[\text{Annual Benefit Payout} = 1.5\% \times \text{Final Estimated Service Years} \times \text{Salary}\]
3. **Service Accrual Dynamics:** Active workers add exactly **1 year of service** for every year they remain active until age 65.
4. **Baseline Longevity Horizon:** Post-retirement lifespan is fixed at **20 years** (payouts run continuously from age 65 to age 85).
5. **Base Timeline Anchor:** The baseline valuation clock begins in **2026**.

---

## 📊 2. Baseline Model Execution Results
The table below represents the key structural inflection points calculated dynamically from the 1,000 synthetic employee records:

| Calendar Year | Active Retirees Drawing Pension | Total Annual Liability Outflow (\$) | Cumulative Liability Drain (\$) | Fund Risk Status |
| :---: | :---: | :---: | :---: | :--- |
| **2027** | 48 | \$1,342,358.28 | \$1,342,358.28 | Active Payout Phase |
| **2035** | 174 | \$5,030,389.15 | \$26,945,632.81 | Active Payout Phase |
| **2045** | 555 | \$17,303,597.68 | \$137,255,673.41 | Active Payout Phase |
| **2050** | 645 | \$21,171,545.27 | \$233,214,272.94 | Active Payout Phase |
| **2055** | **701** | **\$24,286,918.05** | **\$350,421,763.56** | ⚠️ **PEAK CASH DEMAND YEAR** |
| **2060** | 619 | \$22,814,936.97 | \$467,721,366.57 | Active Payout Phase |
| **2066** | 411 | \$16,167,353.40 | \$580,559,727.68 | Terminal Wind-down Phase |

---

## 🧠 3. Actuarial Interpretation & Strategic Insights

### 📉 The Demographic Concentration Risk
The data highlights an aggressive exponential curve in benefit outlays starting in the late 2030s and peaking in **2055**. This indicates that our synthetic corporate profile contains a massive cluster of middle-aged personnel (currently aged 35–45) who will transition into retirement within the same compact 10-year window. This concentration creates a severe systemic liquidity crunch.

### ⏳ Asset-Liability Matching (ALM) Matrix
* **Immunization Strategy:** Because our primary liability payments are highly back-loaded (climbing from \$1.3M in 2027 to over \$24M by 2055), the investment team must avoid locking capital into short-term low-yield vehicles during the early years. The fund needs an aggressive equity compounding phase over the next 15 years to outpace the mounting liability curve.
* **The Liquidity Pivot Point:** As the calendar clicks past 2045, the asset allocation strategy must execute a systematic de-risking roadmap. Portfolio managers must step out of volatile equities and build a protective "cash/short-duration bond ladder" to fully match the massive \$24M annual obligations without risking a forced asset fire-sale during a sudden market crash.
*