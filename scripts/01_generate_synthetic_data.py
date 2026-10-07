import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Create data directory if it doesn't exist yet
os.makedirs('data', exist_ok=True)

# Set random seed for consistent results
np.random.seed(42)
n_employees = 1000

# ==============================================================================
# 1. GENERATE SYNTHETIC EMPLOYEE ROSTER
# ==============================================================================
employee_ids = [f"EMP_{str(i).zfill(4)}" for i in range(1, n_employees + 1)]

# Age distribution: Skewed toward an older corporate profile (Ages 22 to 64)
ages = np.clip(np.random.normal(loc=47, scale=10, size=n_employees).astype(int), 22, 64)
birth_years = 2026 - ages
birth_dates = [datetime(year, 1, 1) + timedelta(days=int(np.random.randint(0, 365))) for year in birth_years]

# Salary distribution: Right-skewed using lognormal distribution
salaries = np.random.lognormal(mean=11.15, sigma=0.35, size=n_employees).astype(int)
salaries = np.clip(salaries, 35000, 220000)

# Years of Service: Correlated with age (cannot start working before age 22)
years_of_service = []
for age in ages:
    max_possible_service = age - 22
    service = 0 if max_possible_service <= 0 else np.random.randint(0, max_possible_service + 1)
    years_of_service.append(service)

roster_df = pd.DataFrame({
    'employee_id': employee_ids,
    'birth_date': [dt.strftime('%Y-%m-%d') for dt in birth_dates],
    'current_age': ages,
    'salary': salaries,
    'years_of_service': years_of_service,
    'gender': np.random.choice(['M', 'F'], size=n_employees, p=[0.51, 0.49])
})

# ==============================================================================
# 2. GENERATE INITIAL FUND ASSETS (Total Fund Value: $100,000,000 Baseline)
# ==============================================================================
# Modeling an institutional 60/40 Asset Mix (60% Equities / 40% Fixed Income)
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

# ==============================================================================
# 3. EXPORT DATASETS TO THE DATA FOLDER
# ==============================================================================
roster_df.to_csv('data/employee_roster.csv', index=False)
assets_df.to_csv('data/fund_assets.csv', index=False)

print(" Data Engineering Pipeline Complete!")
print(" -> Saved: 'data/employee_roster.csv' (1,000 records)")
print(" -> Saved: 'data/fund_assets.csv' (60/40 Baseline Strategic Mix)")