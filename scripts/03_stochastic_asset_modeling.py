import pandas as pd
import numpy as np
import os

# Set random seed for statistical reproducibility
np.random.seed(42)

# Define pipeline execution data targets
liability_results_path = 'data/liability_timeline_results.csv'
sim_output_path = 'data/monte_carlo_solvency_results.csv'

print("📥 Loading Phase 1 baseline SQL liability timeline...")
if not os.path.exists(liability_results_path):
    raise FileNotFoundError(f"Missing base timeline data at {liability_results_path}. Run script 02 first!")

df_liabilities = pd.read_csv(liability_results_path)
years = df_liabilities['calendar_year'].values
liabilities = df_liabilities['total_annual_liability_outflow'].values
n_years = len(years)

# ==============================================================================
# 📐 QUANTITATIVE SIMULATION CONFIGURATION PARAMETERS
# ==============================================================================
n_trials = 10000              # Total parallel economic realities simulated
initial_assets = 100000000.0  # Fund Assets Single Source Baseline ($100 Million USD)

# Asset Allocation Weights (60% Equities / 40% Fixed Income Mix)
w_equity = 0.60
w_bonds = 0.40

# Historical Volatility & Expected Return Parameters (Stochastic Benchmarks)
mu_equity, sigma_equity = 0.08, 0.16  # Equities: 8% expected annual return, 16% volatility
mu_bonds, sigma_bonds = 0.04, 0.05    # Bonds: 4% expected annual yield, 5% volatility

# Portfolio Aggregation (Expected continuous return and standard deviation parameters)
portfolio_mu = (w_equity * mu_equity) + (w_bonds * mu_bonds)
portfolio_sigma = np.sqrt((w_equity**2 * sigma_equity**2) + (w_bonds**2 * sigma_bonds**2))

print(f"⚙️ Portfolio Profile: Expected Portfolio Return = {portfolio_mu*100:.2f}%, Volatility = {portfolio_sigma*100:.2f}%")
print(f"⚡ Launching {n_trials:,} parallel stochastic Monte Carlo trajectories over {n_years} years...")

# Initialize matrix arrays to log fund asset evolution paths
# Row index = years, Column index = individual trials
asset_matrix = np.zeros((n_years, n_trials))
asset_matrix[0, :] = initial_assets

bankruptcy_flags = np.zeros(n_trials)

# ==============================================================================
# 🎲 THE STOCHASTIC SIMULATION CORE ENGINE (GEOMETRIC BROWNIAN MOTION LOOP)
# ==============================================================================
for t in range(1, n_years):
    # Generate vector of random standard normal distributions for continuous Brownian Motion
    Z = np.random.normal(0, 1, n_trials)
    
    # Compute continuous asset geometric returns for the step interval delta t
    dt = 1.0
    market_returns = np.exp((portfolio_mu - 0.5 * portfolio_sigma**2) * dt + portfolio_sigma * np.sqrt(dt) * Z)
    
    # Evolve fund capital asset values forward from prior step, adjusting for market returns
    previous_assets = asset_matrix[t-1, :]
    simulated_growth = previous_assets * market_returns
    
    # Deduct mandatory structural pension cash obligations computed by the database
    net_assets = simulated_growth - liabilities[t]
    
    # Enforce asset floor constraint at $0 (A bankrupt fund remains bankrupt)
    net_assets = np.clip(net_assets, 0, None)
    
    # Log state updates back into our simulation array matrix
    asset_matrix[t, :] = net_assets
    
    # Track any structural default events across our timelines
    bankruptcy_flags[net_assets == 0] = 1

# ==============================================================================
# 🧠 ACTUARIAL METRICS HARVESTING & REPORTING
# ==============================================================================
final_ruin_probability = (np.sum(bankruptcy_flags) / n_trials) * 100
mean_ending_assets = np.mean(asset_matrix[-1, :])
median_ending_assets = np.median(asset_matrix[-1, :])

print("\n📊 --- QUANTITATIVE ACTUARIAL RISK METRICS REPORT ---")
print(f"🛑 Empirical Probability of Ruin (Fund Insolvency Risk): {final_ruin_probability:.2f}%")
print(f"💰 Mean Estimated Capital Assets at Horizon Year 2066: ${mean_ending_assets:,.2f}")
print(f"📈 Median Estimated Capital Assets at Horizon Year 2066: ${median_ending_assets:,.2f}")

# Export data matrix summaries to feed downstream Power BI dashboards
df_export = pd.DataFrame(asset_matrix, index=years).T
df_export.index.name = 'trial_id'
df_export.to_csv(sim_output_path)
print(f"\n✅ Simulation data pipeline successfully exported to: '{sim_output_path}'")