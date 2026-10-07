# Quantitative Project Methodology & Actuarial Frameworks

This document details the underlying mathematical formulas, distribution mechanics, and statistical parameters utilized to power the ALM Solvency Simulator.

---

## 🧮 1. The Defined Benefit Liability System
The corporate scheme models a classical Defined Benefit (DB) structure. Benefits are treated as an un-indexed continuous life annuity starting precisely at the Normal Retirement Age (NRA).

### Benefit Accrual Rule
For each individual participant ($i$), the projected annual lifetime benefit entitlement ($B_i$) is defined by:
$$B_i = \alpha \times S_i \times (Y_i + \Delta t_i)$$

Where:
* $\alpha$: The benefit replacement accrual rate (fixed at $1.5\% = 0.015$).
* $S_i$: The final baseline annual salary recorded at the valuation date.
* $Y_i$: Accumulated historic years of pensionable corporate service.
* $\Delta t_i$: Remaining continuous service years accruing until retirement ($65 - \text{Age}_i$).

### Collective Cash Outflow Mapping
The gross liability drain ($L_t$) for any evaluated calendar year ($t$) represents the aggregate sum of all active benefit payments:
$$L_t = \sum_{i \in R_t} B_i$$

Where $R_t$ represents the dynamic subset of living retirees in year $t$, assuming a static global post-retirement lifespan duration of exactly 20 years ($\text{Age} \in [65, 85)$).

---

## 🎲 2. Capital Market Simulation Engine
To evolve portfolio values against annual liability cash drains, assets are projected under a parallel stochastic framework over a multi-decade horizon.

### Stochastic Asset Trajectories (Geometric Brownian Motion)
Market returns for the collective asset reserves are driven by continuous Stochastic Differential Equations (SDEs) tracking Geometric Brownian Motion (GBM):
$$A_t = \left[ A_{t-1} \times \exp\left( \left(\mu_p - \frac{1}{2}\sigma_p^2\right)\Delta t + \sigma_p \sqrt{\Delta t} Z_t \right) \right] - L_t$$

Where:
* $A_t$: Net asset wealth reserves logged at the conclusion of calendar step $t$.
* $\mu_p$: Expected composite portfolio long-term investment return.
* $\sigma_p$: Total aggregated portfolio annual volatility.
* $Z_t$: A generated independent random vector of standard normal distributions ($Z_t \sim \mathcal{N}(0, 1)$).
* $L_t$: Mandatory cash outflows extracted at the step boundary to pay active pension checks.

### Portfolio Parameter Aggregation
Given an initial asset mix allocation of $60\%$ Equities ($w_e$) and $40\%$ Fixed-Income Corporate Bonds ($w_b$), the tracking benchmarks are aggregated as follows:
$$\mu_p = (w_e \cdot \mu_e) + (w_b \cdot \mu_b) = (0.60 \cdot 0.08) + (0.40 \cdot 0.04) = 6.40\%$$

$$\sigma_p = \sqrt{(w_e^2 \cdot \sigma_e^2) + (w_b^2 \cdot \sigma_b^2)} = \sqrt{(0.60^2 \cdot 0.16^2) + (0.40^2 \cdot 0.05^2)} = 9.81\%$$

### Insolvency Floor Constraint
If net capital assets drop to or below zero in any simulation trail due to market drops intersecting with high cash outflows, the fund is locked into default:
$$A_t = \max(0, A_t)$$

---

## 🛑 3. Empirical Risk Metrics Definitions

### Probability of Ruin
The core objective indicator tracking systemic fund vulnerability is defined as the empirical probability of insolvency across all generated paths ($N = 10,000$):
$$\psi = \frac{1}{N}\sum_{j=1}^{N} \mathbb{I}\left( \min_{0 \le t \le T} A_{t,j} = 0 \right) \times 100\%$$

Where $\mathbb{I}(\cdot)$ represents an indicator function returning $1$ if the individual simulation trajectory $j$ breaches asset reserves ($A = 0$) at any point across the 40-year horizon, and $0$ otherwise.