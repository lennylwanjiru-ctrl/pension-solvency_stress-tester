#  Corporate Pension Fund Asset-Liability Matching (ALM) & Solvency Stress Tester

---

##  1. Why  This Project (The Purpose)
As a fourth-year actuarial science student, I built this project to demonstrate how modern data analysis tools bridge the gap between traditional risk mathematics and enterprise-level execution. Actuarial models often live in siloed, legacy systems. 

This project proves how an entry-level professional can build a transparent, scalable quantitative risk pipeline using **SQL relational engineering**, **Python stochastic simulation**, and **Power BI corporate business intelligence** to tackle a massive macroeconomic problem.

---

##  2. The Business Challenge
A defined-benefit pension fund holds a strict, long-term legal obligation to pay monthly benefits to thousands of aging workers over a 30-to-40-year horizon. The fund must remain solvent, but faces two compounding structural crises:
1. **Longevity Risk:** Medical advancements and lifestyle improvements mean retirees are living years longer than historical mortality tables predict, stretching the liability timeline out much further than planned.
2. **Market Co-Movement Risk:** If a severe macroeconomic downturn (like a 2008-style market crash) hits asset reserves right when a large demographic wave of employees reaches retirement age, the fund risks catastrophic bankruptcy.

The business problem is determining the exact probability that the fund will drop below statutory solvency limits under highly volatile capital markets, and finding an investment mix that insulates retirees.

---

##  3. Who This Project Benefits
This analytical framework acts as an institutional decision-making engine built directly for corporate leadership:
* **Chief Risk Officers (CROs):** Gives them a clear, mathematical probability distribution of ruin so they can actively adjust regulatory capital reserve constraints.
* **Pension Board Trustees:** Provides a transparent, non-technical interface to verify if current fund assets can comfortably back promised retirement checks.
* **Investment Managers / Chief Investment Officers (CIOs):** Identifies exact calendar years of high liquidity strain, helping them match corporate bond durations and avoid forced equity selloffs during market crashes.

---

##  4. Technical Stack & Tooling
* **Database Layer (SQL):** Complex Common Table Expressions (CTEs), Window Functions (`SUM() OVER()`, `MAX() OVER()`), and a continuous Calendar Spine to map the 40-year liability timeline.
* **Simulation Engine (Python):** `NumPy` and `Pandas` running a highly parallelized 10,000-trial Stochastic Monte Carlo Simulation.
* **Stochastic Modeling Frameworks:** **Geometric Brownian Motion (GBM)** to model volatile equity returns and mean-reverting interest rate models for fixed income.
* **Visualization Layer (Power BI):** Interactive Executive Dashboard leveraging dynamic **DAX Parameters** and custom measures to execute live portfolio rebalancing stress tests.

---

##  5. How I Solved The Problem (The Methodology)
The solution is built through a robust, four-phase data and analytics engineering pipeline:

### Phase 1: Liability Timeline Blueprinting (SQL Engineering)
The analyst engineered a database query that processes raw synthetic demographic data. Applying actuarial pension accrual formulas (`1.5% * Service Years * Final Salary`), the query projects annual benefit outflows over a 40-year window, utilizing window metrics to flag the fund's absolute **Peak Cash Demand Year**.

### Phase 2: Stochastic Asset Modeling (Python Engine)
I built a simulation loop that models capital growth over time. Using Geometric Brownian Motion, the engine generates 10,000 distinct financial realities, evaluating a baseline portfolio mix across multi-decade horizons while factoring in unpredictable market drops.

### Phase 3: Actuarial Longevity Shocks & Risk Tuning (Python)
I built an actuarial tuning module that applies "Mortality Improvement Factors." This artificially shifts the life expectancy of the synthetic retiree pool outward by +2, +5, and +8 years. The asset returns are offset against the SQL liability curves daily to export a distribution of final **Funding Ratios**.

### Phase 4: The Strategic Investment Hub (Power BI Visuals)
I fed the simulated distributions into an interactive dashboard. Using DAX parameters, I constructed live sliders that allow board members to adjust asset allocations in real-time, watching an interactive gauge instantly calculate the mathematical probability of bankruptcy based on their strategy.

---

##  Repository Architecture
```text
├──  data/
│   ├── employee_roster.csv          # Raw synthetic demographic & payroll data
│   ├── fund_assets.csv              # Initial corporate asset allocations
│   └── pension_alm.db               # Local database container for analytics
│
├──  documentation/
│   ├── sql_pipeline_docs.md         # Detailed database schemas & metadata
│   └── project_methodology.md       # Actuarial frameworks & model formulas
│
├──  scripts/
│   ├── 01_generate_synthetic_data.py # Data engineering pipeline script
│   ├── 02_liability_projection.sql   # SQL database liability analytics
│   └── 03_stochastic_asset_modeling.py # Python Monte Carlo simulation engine
│
└──  README.md                     # Main portfolio presentation page
```

---
📄 *This project serves as a comprehensive portfolio piece showcasing end-to-end data analytics and quantitative risk strategy capabilities within the financial services sector.*