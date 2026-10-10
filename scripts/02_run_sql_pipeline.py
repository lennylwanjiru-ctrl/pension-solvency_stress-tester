
Project: Corporate Pension Fund Asset-Liability Matching (ALM) & Solvency Stress-Tester
Module: Relational Database Compiling, Window Functions & Liability-Curve Ingestion
Analyst: Lenny Wanjiru (DeKUT Actuarial Science)


import os
import sqlite3
import logging
import pandas as pd

# Configure enterprise logger interface for execution tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define absolute file system paths
db_path = os.path.join('data', 'pension_alm.db')
roster_csv = os.path.join('data', 'employee_roster.csv')
assets_csv = os.path.join('data', 'fund_assets.csv')
output_csv = os.path.join('data', 'liability_timeline_results.csv')

# 1. Environment Workspace Safeguard Check
if not os.path.exists(roster_csv) or not os.path.exists(assets_csv):
    logging.error("Execution Aborted: Required configuration flat files missing inside data/ directory.")
    raise FileNotFoundError("Please execute the primary synthetic cohort generation script first.")

logging.info("Initializing relational SQLite database compilation pipeline...")
roster_df = pd.read_csv(roster_csv)
assets_df = pd.read_csv(assets_csv)


# PHASE 1: ACTUARIAL RETIREMENT HORIZON DATA TRANSFORMATIONS

logging.info("Computing active participant retirement horizons and benefit projections...")

# Enforce explicit baseline definitions for individual employee paths
roster_df['years_to_retirement'] = 65 - roster_df['current_age']
roster_df['retirement_year'] = 2026 + roster_df['years_to_retirement']

# Calculate projected annual pension benefit based on accrual rate and lifespan expectations
roster_df['annual_pension_payout'] = round(
    0.015 * (roster_df['years_of_service'] + roster_df['years_to_retirement']) * roster_df['salary'], 2
)

# Connect to relational database and write baseline registries
conn = sqlite3.connect(db_path)
roster_df.to_sql('employee_roster', conn, if_exists='replace', index=False)
assets_df.to_sql('fund_assets', conn, if_exists='replace', index=False)


# PHASE 2: SPATIAL-TEMPORAL CALENDAR SPINE GENERATION

logging.info("Materializing 40-year temporal calendar spine container table...")

# Generate structural sequence covering continuous liability projection horizon
years = list(range(2026, 2067))
calendar_df = pd.DataFrame({'calendar_year': years})
calendar_df.to_sql('calendar_spine', conn, if_exists='replace', index=False)

# PHASE 3: ADVANCED WINDOW FUNCTION ANALYSIS (LIABILITY PROJECTION LOGIC)

logging.info("Executing analytical relational query blocks over relational memory schemas...")

sql_query = """
WITH ActivePayouts AS (
    SELECT 
        c.calendar_year,
        r.employee_id,
        r.annual_pension_payout
    FROM calendar_spine c
    CROSS JOIN employee_roster r
    WHERE c.calendar_year >= r.retirement_year
      AND c.calendar_year < (r.retirement_year + 20)
),
LiabilityCurve AS (
    SELECT 
        calendar_year,
        COUNT(DISTINCT employee_id) AS active_retirees_drawing_pension,
        SUM(annual_pension_payout) AS total_annual_liability_outflow
    FROM ActivePayouts
    GROUP BY calendar_year
)
SELECT 
    calendar_year,
    active_retirees_drawing_pension,
    ROUND(total_annual_liability_outflow, 2) AS total_annual_liability_outflow,
    ROUND(SUM(total_annual_liability_outflow) OVER (ORDER BY calendar_year), 2) AS cumulative_liability_drain,
    CASE 
        WHEN total_annual_liability_outflow = MAX(total_annual_liability_outflow) OVER () 
        THEN ' PEAK CASH DEMAND YEAR'
        WHEN total_annual_liability_outflow > 0 
        THEN 'Active Payout Phase'
        ELSE 'Accumulation Phase (No Active Retirees)'
    END AS fund_risk_status
FROM LiabilityCurve
ORDER BY calendar_year;
"""

try:
    results_df = pd.read_sql_query(sql_query, conn)
    results_df.to_csv(output_csv, index=False)
    logging.info(f"Analytical outcomes successfully written to: {output_csv}")
    
    # Structural visual dashboard summary reporting
    print("\n" + "="*80)
    print("PORTFOLIO INSIGHTS MATRIX: PROJECTED 40-YEAR BENE-CASH OUTFLOW SUMMARY")
    print("="*80)
    print(results_df.head(15).to_string(index=False))
    print("-"*80)
    print(results_df.tail(10).to_string(index=False))
    print("="*80 + "\n")

except Exception as e:
    logging.error(f"Execution Failed: Structural relational processing error - {str(e)}")

finally:
    conn.close()
    logging.info("Database instance connection safely isolated and terminated.")
    
