# Asset-Liability Matching (ALM) & Solvency Stress-Testing Methodology
**Project:** Corporate Pension Fund ALM & Solvency Stress-Tester  
**Lead Analyst:** Lenny Wanjiru | *Dedan Kimathi University of Technology (DeKUT)*  
**Infrastructure Specifications:** Python, SQLite, NumPy, Pandas, Power BI



## 1. The Defined Benefit Liability System

### Benefit Accrual Rule
The underlying corporate retirement system models an un-indexed, continuous lifetime Defined Benefit (DB) structure. For each individual participant ($i$), the projected annual lifetime benefit entitlement ($B_i$) is mathematically defined by the following accrual expression:

$$B_i = a \times S_i \times (Y_i + \Delta t_i)$$

*   **$a$ (Benefit Replacement Accrual Rate):** Fixed at 0.015 (1.50% accrual loading factor per annum).
*   **$S_i$:** The individual participant's final baseline salary recorded at the valuation date.
*   **$Y_i$:** Accumulated historical years of pensionable active corporate service.
*   **$\Delta t_i$:** Remaining continuous service years accruing until reaching the Normal Retirement Age (NRA = 65). Calculated directly as: $\Delta t_i = 65 - \text{Age}_i$.

### Collective Cash Outflow Mapping
The gross portfolio liability cash drain ($L_t$) for any evaluated calendar year ($t$) represents the aggregate sum of all active benefit payouts triggered per path. The system assumes a static post-retirement lifespan duration of exactly 20 years, meaning benefits are paid continuously from Age 65 through Age 84:

$$L_t = \sum_{i \in R_t} B_i$$

*   Where $R_t$ represents the dynamic active subset of living retirees drawing pensions during calendar year $t$, satisfying the strict constraint: $\text{Age}_i \in [65, 84]$.



## 2. Capital Market Simulation Engine

### Stochastic Asset Trajectories (Geometric Brownian Motion)
Market returns for the collective asset reserves are driven by continuous Stochastic Differential Equations (SDEs) tracking a multi-asset Geometric Brownian Motion (GBM) framework:

$$A_t = \left[ A_{t-1} \times \exp\left(\left(\mu_p - \frac{1}{2}\sigma_p^2\right)\Delta t + \sigma_p\sqrt{\Delta t} \cdot Z_t\right) \right] + P - L_t$$

*   **$A_t$:** Net asset wealth reserves logged at the conclusion of calendar step $t$.
*   **$\mu_p$ & $\sigma_p$:** The expected composite portfolio long-term investment return and total aggregated portfolio annual volatility.
*   **$Z_t$:** A generated independent random vector of standard normal distributions: $Z_t \sim N(0, 1)$.
*   **$P$ (Annual Strategic Inflow):** Fixed institutional funding injection set at \$1,200,000 USD per annum.
*   **$L_t$:** Mandatory cash outflows extracted at the step boundary to pay active pension checks.

### Portfolio Parameter Aggregation
Given an initial asset mix allocation of 60% Equities ($w_e$) and 40% Fixed-Income Corporate Bonds ($w_b$), the tracking benchmarks are aggregated as follows:

$$\mu_p = (w_e \cdot \mu_e) + (w_b \cdot \mu_b) = (0.60 \cdot 0.08) + (0.40 \cdot 0.04) = 6.40\%$$

$$\sigma_p = \sqrt{(w_e^2 \cdot \sigma_e^2) + (w_b^2 \cdot \sigma_b^2)} = \sqrt{(0.60^2 \cdot 0.16^2) + (0.40^2 \cdot 0.05^2)} = 9.81\%$$

### Insolvency Floor Constraint
If net capital assets drop to or below zero in any simulation trail due to market drops intersecting with high cash outflows, the fund is locked into default:

$$A_t = \max(0, A_t)$$



## 3. Empirical Risk Metrics Definitions

### Probability of Ruin (Fund Insolvency Risk)
The core objective indicator tracking systemic fund vulnerability is defined as the empirical probability of insolvency across all generated paths ($N = 10,000$):

$$\psi = \frac{1}{N}\sum_{j=1}^{N} I\left( \min_{0 \le t \le T} A_{t,j} = 0 \right) \times 100$$

*   Where $I(\cdot)$ represents an indicator function returning 1 if the individual simulation trajectory breaches asset reserves ($A_t = 0$) at any point across the 40-year horizon, and 0 otherwise. Prioritizing this empirical tracking metric ensures that multi-decade liabilities remain backed by asset allocation limits, protecting long-term fund sustainability.
*
