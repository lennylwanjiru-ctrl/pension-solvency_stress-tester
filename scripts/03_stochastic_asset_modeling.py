
Project: Corporate Pension Fund Asset-Liability Matching (ALM) & Solvency Stress-Tester
Module: Strategic Portfolio Return Modeling & Stochastic Monte Carlo Asset-Liability Tracking
Analyst: Lenny Wanjiru (DeKUT Actuarial Science)


import os
import logging
import numpy as np
import pandas as pd

# Configure enterprise logger interface for execution tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define absolute file system paths
liability_results_path = os.path.join('data', 'liability_timeline_results.csv')
sim_output_path = os.path.join('data', 'monte_carlo_solvency_results.csv')

# 1. Environment Workspace Safeguard Check
if not os.path.exists(liability_results_path):
    logging.error(f"Execution Aborted: Required configuration file missing at: {liability_results_path}")
    raise FileNotFoundError("Please execute the primary relational database aggregation script first.")

logging.info("Loading baseline liability projections for stochastic path execution...")
df_liabilities = pd.read_csv(liability_results_path)

# Extract temporal dimensions and structured liability cash outflow vectors
years = df_liabilities['calendar_year'].values
liabilities = df_liabilities['total_annual_liability_outflow'].values


# QUANTITATIVE SIMULATION PARAMETERS (GBM STRUCTURAL BASELINES)

logging.info("Configuring multi-asset strategic allocation return matrices...")

np.random.seed(42)
n_trials = 10000
n_years = len(years)
initial_assets = 100000000.00 

# Asset Allocation Weights (60% Equities / 40% Fixed Income Mix)
w_equity = 0.60
w_bonds = 0.40

# Historical Asset Parameter Volatilities & Expected Continuous Returns
mu_equity, sigma_equity = 0.08, 0.16
mu_bonds, sigma_bonds = 0.04, 0.05

# Portfolio Aggregation via Weighted Drift and Variance Scaling
portfolio_mu = (w_equity * mu_equity) + (w_bonds * mu_bonds)
portfolio_sigma = np.sqrt((w_equity**2 * sigma_equity**2) + (w_bonds**2 * sigma_bonds**2))

logging.info(f"Aggregated Portfolio Base: Expected Return = {portfolio_mu:.2%} | Portfolio Volatility = {portfolio_sigma:.2%}")

# Initialize multidimensional projection arrays to track capital paths
asset_matrix = np.zeros((n_years, n_trials))
asset_matrix[0, :] = initial_assets
bankruptcy_flags = np.zeros(n_trials)


# STOCHASTIC ENGINING: THE MULTI-PATH SIMULATION LOOP

logging.info("Launching parallel stochastic Monte Carlo trajectories over active horizons...")

dt = 1.0
annual_premium_inflow = 1200000.0  # Normalized structural funding injections

for t in range(1, n_years):
    # Draw independent standard normal shock arrays representing market volatility
    Z = np.random.normal(0, 1, n_trials)
    
    # Compute continuous asset geometric returns via stochastic path transformations
    market_returns = np.exp((portfolio_mu - 0.5 * (portfolio_sigma**2)) * dt + portfolio_sigma * np.sqrt(dt) * Z)
    
    # Evolve fund asset trajectories forward, adjusting for incoming premiums and outgoing benefit claims
    previous_assets = asset_matrix[t - 1, :]
    simulated_growth = previous_assets * market_returns
    
    # Deduct structural pension liability obligations computed by the database layer
    net_assets = simulated_growth + annual_premium_inflow - liabilities[t]
    
    # Enforce a strict asset floor constraint at 0.0 to track permanent default thresholds
    asset_matrix[t, :] = np.clip(net_assets, 0, None)

# Track structural bankruptcy occurrences across individual path timelines
bankruptcy_flags[asset_matrix[-1, :] == 0] = 1
final_ruin_probability = (np.sum(bankruptcy_flags) / n_trials) * 100

mean_ending_assets = np.mean(asset_matrix[-1, :])
median_ending_assets = np.median(asset_matrix[-1, :])


# DATA LAYER SERIALIZATION & TELEMETRY REPORTING

logging.info("Serializing stochastic path coordinates back to flat storage...")

df_export = pd.DataFrame(asset_matrix, index=years)
df_export.index.name = 'trial_id'
df_export.to_csv(sim_output_path)

logging.info(f"Simulation matrix records successfully written to: {sim_output_path}")

# Executive Audit Reporting Layout
print("\n" + "="*80)
print("ACTUARIAL SOLVENCY AUDIT BRIEF: STOCHASTIC PENSION PLAN RESILIENCE")
print("="*80)
print(f"Stochastic Evaluation Matrix Scope:  {n_trials:,} Parallel Economic Paths")
print(f"Plan Asset Allocation Strategy:      60/40 Institutional Strategic Mix")
print(f"Liability Horizon Range Boundary:    {min(years)} to {max(years)} ({n_years} Years)")
print("-"*80)
print("Aggregated Portfolio Solvency Performance Diagnostics:")
print(f" -> Empirical Probability of Ruin (Fund Default Risk): {final_ruin_probability:.2f}%")
print(f" -> Mean Predicted Capital Assets at Year {max(years)}:       ${mean_ending_assets:,.2f}")
print(f" -> Median Predicted Capital Assets at Year {max(years)}:     ${median_ending_assets:,.2f}")
print("="*80 + "\n")
