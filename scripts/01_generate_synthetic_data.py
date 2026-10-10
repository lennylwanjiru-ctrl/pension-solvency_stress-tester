
Project: Corporate Pension Fund Asset-Liability Matching (ALM) & Solvency Stress-Tester
Module: Demographic Simulation & Strategic Asset Allocation Engineering
Analyst: Lenny Wanjiru (DeKUT Actuarial Science)


import os
import logging
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Configure enterprise logger interface for execution tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize target relative directories
output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)

# Set global reproducibility seeds for demographic sampling consistency
np.random.seed(42)
n_employees = 1000


# PHASE 1: DEMOGRAPHIC SIMULATION & COHORT ROSTER GENERATION

logging.info("Initializing synthetic employee active cohort simulation...")

employee_ids = [f"EMP_{str(i).zfill(4)}" for i in range(1, n_employees + 1)]

# Model localized corporate age distributions (Bounded normal structure between 22 and 64)
ages = np.clip(np.random.normal(loc=47, scale=10, size=n_employees).astype(int), 22, 64)
birth_years = 2026 - ages
birth_dates = [datetime(year, 1, 1) + timedelta(days=int(np.random.randint(0, 365))) for year in birth_years]

# Map right-skewed salary levels using a log-normal distribution matrix
salaries = np.clip(np.random.lognormal(mean=11.15, sigma=0.35, size=n_employees).astype(int), 35000, 220000)

# Model correlated years of service mapping (Constrained by operational age floors)
years_of_service = []
for age in ages:
    max_possible_service = age - 22
    service = 0 if max_possible_service <= 0 else np.random.randint(0, max_possible_service + 1)
    years_of_service.append(service)

# Construct primary operational roster dataframe
roster_df = pd.DataFrame({
    'employee_id': employee_ids,
    'birth_date': [dt.strftime('%Y-%m-%d') for dt in birth_dates],
    'current_age': ages,
    'salary': salaries,
    'years_of_service': years_of_service,
    'gender': np.random.choice(['M', 'F'], size=n_employees, p=[0.51, 0.49])
})


# PHASE 2: STRATEGIC ASSET ALLOCATION ENGINEERING (60/40 INSTITUTIONAL MIX)

logging.info("Materializing baseline institutional 60/40 asset allocation structure...")

assets_data = {
    'asset_class': [
        'Domestic Equities',
        'International Equities',
        'Corporate Bonds',
        'Government Bonds',
        'Cash Equivalents'
    ],
    'ticker': ['SPY', 'VXUS', 'LQD', 'BND', 'BIL'],
    'allocation_pct': [0.40, 0.20, 0.25, 0.10, 0.05],
    'current_value_usd': [40000000.00, 20000000.00, 25000000.00, 10000000.00, 5000000.00]
}

assets_df = pd.DataFrame(assets_data)


# PHASE 3: DATA LAYOUT SERIALIZATION

logging.info("Serializing analytical portfolios directly to database flat files...")

roster_df.to_csv(os.path.join(output_dir, 'employee_roster.csv'), index=False)
assets_df.to_csv(os.path.join(output_dir, 'fund_assets.csv'), index=False)

logging.info("Data engineering pipeline execution finalized successfully.")

# Terminal Telemetry Output Layout
print("\n" + "="*80)
print("PENSION DATA ENGINEERING LEDGER: DATA SET LIFECYCLE SUMMARY")
print("="*80)
print(f" -> Active Cohort Records Cached: {len(roster_df):,} Profiles (data/employee_roster.csv)")
print(f" -> Portfolio Strategic Allocation: 60/40 Institutional Baseline (data/fund_assets.csv)")
print("="*80 + "\n")
