# Corporate Pension Fund Asset-Liability Matching (ALM) & Solvency Stress-Tester
**Lead Analyst:** Lenny Wanjiru | *Dedan Kimathi University of Technology (DeKUT)*  
**Core Stack:** Python, SQLite, NumPy, Pandas, Power BI (DAX)



##  Project Strategy & Value Proposition
Traditional corporate pension fund management frameworks frequently operate within isolated, legacy systems where liability forecasting is disconnected from capital market asset simulation. This structural separation introduces severe risk accumulation under volatile macroeconomic conditions, directly impacting an institution's ability to maintain statutory funding limits.

This repository implements a production-grade, end-to-end data analytics and quantitative risk pipeline in **Python** and **SQL**. By linking multi-decade demographic active cohort simulation with relational database analytical window functions and parallel geometric asset trajectories, the platform builds an institutional decision-making engine. It quantifies exact corporate funding thresholds and stress-tests fund resilience against dual solvency crises: unexpected mortality shifts (longevity risk) and extreme macroeconomic market drawdowns.



##  The Business Challenge & Core Risks
A defined-benefit pension fund holds a strict, long-term legal obligation to distribute guaranteed monthly lifetime annuities to thousands of workers over a multi-decade horizon. The system must remain resilient against two compounding structural crises:
1.  **Systemic Longevity Risk:** Medical advancements and dynamic mortality improvements push individual retiree lifespans past traditional actuarial table horizons, lengthening the liability timeline out much further than planned.
2.  **Market Co-Movement Risk:** If a severe macroeconomic downturn hits asset reserves precisely when a large demographic wave of employees reaches retirement age, the fund faces rapid, irreversible asset depletion.

The objective of this platform is to calculate the precise empirical probability of ruin, identifying optimal strategic asset allocations that isolate retirees from volatile market shocks.



##  Stakeholder Impact Summary
This analytical framework translates raw data parameters into actionable insights for corporate leadership:
*   **Chief Risk Officers (CROs):** Delivers a transparent, empirical probability distribution of ruin to actively guide regulatory risk capital reserve settings.
*   **Pension Board Trustees:** Provides a clean interface to verify if current fund assets can withstand projected multi-decade benefit check drains.
*   **Chief Investment Officers (CIOs):** pinpoints exact calendar years of peak portfolio liquidity strain, optimizing bond duration structures to avoid forced equity liquidation during market corrections.



## Technical Stack & Tooling
*   **Database Ingestion Layer (SQL):** Employs complex Common Table Expressions (CTEs) and high-performance analytical window functions (`SUM() OVER()`, `MAX() OVER()`) to map the continuous 40-year liability spine.
*   **Stochastic Simulation Engine (Python):** Utilizes `numpy` and `pandas` vectors to execute a highly parallelized 10,000-trial Monte Carlo simulation driven by Geometric Brownian Motion (GBM) market paths.
*   **Business Intelligence Cockpit (Power BI):** Deploys an interactive dashboard leveraging dynamic DAX parameters, alert triggers, and custom risk metrics to execute real-time fund stress tests.



##  Modular Implementation Methodology

### Phase 1: Liability Timeline Blueprinting (SQL Engineering)
*   **Execution:** Extracts raw synthetic demographic rosters from the staging file system and imports parameters into a relational SQLite database container.
*   **Actuarial Logic:** Automatically computes individual participant retirement years based on a statutory normal retirement age (N NRA = 65) and calculates individual projected benefit payouts using a 1.50% continuous service accrual modifier.

### Phase 2: Strategic Asset Allocation (Python Engine)
*   **Execution:** Structures a baseline institutional 60/40 asset allocation mix (60% Equities / 40% Fixed Income Corporate Bonds) initialized at a \$100,000,000.00 USD baseline funding profile.
*   **Market Simulation:** Runs the asset capital base forward across a 40-year horizon over 10,000 distinct market paths, factoring in annual funding premium inflows and subtracting matching SQL liability data cash extractions.

### Phase 3: Actuarial Longevity Shocks & Risk Tuning
*   **Execution:** Integrates an underwriting override module that applies variable Mortality Improvement Factors. 
*   **Stress Assessment:** Artificially shifts the post-retirement lifespan duration across cohort records (testing sudden +2, +5, and +8 year shifts) to measure the capital drain velocity on fund solvency.

### Phase 4: The Strategic Investment Hub (Power BI Visuals)
*   **Execution:** Maps the serialized database outputs into an interactive dashboard workspace.
*   **Dash Governance:** Implements dynamic DAX measures and sliders, allowing board trustees to instantly recalculate the empirical probability of ruin across custom investment allocations and live market drawdowns.



##  Repository Directory Structure
`text
pension-solvency_stress-tester/
├── data/
│   ├── employee_roster.csv             # Raw synthetic demographic & payroll data (1,000 records)
│   ├── fund_assets.csv                 # Initial corporate asset allocation registries
│   ├── liability_timeline_results.csv # Cached relational SQL analytical window function outputs
│   └── pension_alm.db                  # Local relational database container
├── documentation/
│   ├── sql_pipeline_docs.md            # Database schemas, CTE blueprints, and table inflections
│   └── project_methodology.md          # Advanced quantitative financial risk & DB equations
├── scripts/
│   ├── 01_generate_synthetic_data.py   # Data engineering pipeline script
│   ├── 02_run_sql_pipeline.py          # SQL database mapping and liability analytics execution
│   └── 03_stochastic_asset_modeling.py # Python Monte Carlo asset trajectory simulation engine
├── local_visualizations/
│   └── pension_solvency_dashboard.pbix # Interactive Power BI ESG Solvency Cockpit
└── README.md                           # Master repository presentation layout brief
`



##  Quick Start Execution Guide
Ensure you have your required Python dependencies active within your local terminal environment before running the operational modules in order:

`bash
# Install core quantitative dependencies
pip install pandas numpy

# Execute the pipeline components sequentially
python scripts/01_generate_synthetic_data.py
python scripts/02_run_sql_pipeline.py
python scripts/03_stochastic_asset_modeling.py
`
