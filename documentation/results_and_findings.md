# Actuarial Risk Analysis: Solvency Stress Testing & Findings Report
**Project:** Corporate Pension Fund ALM & Solvency Stress-Tester  
**Lead Analyst:** Lenny Wanjiru | *Dedan Kimathi University of Technology (DeKUT)*  




## 1. Core Simulation Metadata & Output Metrics
To evaluate long-term fund sustainability, the simulation engine executed a parallel multi-path asset-liability projection mapping across a continuous 40-year multi-decade investment horizon.

### Model Execution Baseline:
*   **Stochastic Trials:** 10,000 Independent Capital Market Paths (Monte Carlo Simulation)
*   **Outlook Horizon:** 40 Years (Continuous annual timeline increments from 2027 to 2066)
*   **Asset Initializer:** \$100,000,000.00 USD Starting Reserves
*   **Strategic Allocation Mix:** 60% Equities ($w_e$) / 40% Fixed Income Corporate Bonds ($w_b$)
*   **Portfolio Liability Commitment:** \$580,559,727.68 USD Aggregate Continuous Outflow Obligation

### Primary Solvency Indicators Summary:
*   **Empirical Probability of Ruin (Fund Default Risk):** 87.99%
*   **Mean Estimated Capital Assets at Horizon Year (2066):** \$54,876,970.35 USD
*   **Median Estimated Capital Assets at Horizon Year (2066):** \$0.00 USD



## 2. Deep Dive Interpretation & Actuarial Diagnosis

### The Median Collapse vs. Right-Skew Paradox
The structural divergence between the Mean Ending Assets (\$54.8M) and the Median Ending Assets (\$0.00) exposes a critical tail-risk anomaly. In **87.99% of simulated market paths**, the pension fund suffers absolute asset depletion, causing complete fund ruin before the Year 2066 horizon. 

The positive mean value is driven entirely by a small cluster of exceptional, high-performing trials where equity portfolios grew exponentially. This extreme statistical right-skew demonstrates why managing an institutional pension plan based on "mean baselines" or "average returns" is inherently dangerous; a Chief Risk Officer cannot fund guaranteed retirement checks using a lottery-style tail distribution. The baseline 60/40 investment mix is structurally flawed under this liability profile.

### The Peak Cash Strain Correlation (Year 2055)
The database logging layer successfully isolated **Year 2055 as the Peak Cash Demand Year**, tracking a single-year liability drain of **\$24.28M**. 

The asset portfolio collapses at this intersection because the intense cash drain hits precisely after three decades of compounding benefit outflows have already eroded the base capital reserve. When equity market corrections hit during this high-outflow phase, the fund is forced to liquidate volatile equities at depressed market prices to fulfill monthly pension obligations. This lock-in permanently damages the fund's capital foundation, destroying its ability to capture compounding growth when the market eventually recovers.



## 3. Strategic Recommendations for the Board
To mitigate the 87.99% Probability of Ruin and bring the fund within safe regulatory solvency parameters (typically a default risk threshold $< 5\%$), the following asset-liability management overhauls are recommended:

1.  **Implement Dynamic Liability Glidepaths:** Maintain the initial 60/40 growth allocation for the first 15 years while active employee cash outflows remain low (\$1.3M – \$5.0M). Beginning in Year 16 (2041), automatically execute an accumulation shift—reallocating 5% of equity exposures annually into a structured bond ladder to secure liquid cash matching the upcoming retirement wave.
2.  **Execute Liabilities Duration Immunization:** Lock the 40% fixed-income allocation exclusively into ultra-long-duration corporate and government bonds during the accumulation phase. This immunizes the portfolio against sudden interest rate declines and matches the exact cash flow demands of the 2055 liability tail.
3.  **Deploy Contingent Funding Injections:** Establish a legally binding trigger rule with the corporate sponsor. If the dynamic funding ratio drops below 80% during a severe market correction, the sponsor must execute immediate emergency cash injections to prevent equity liquidation at market troughs.
