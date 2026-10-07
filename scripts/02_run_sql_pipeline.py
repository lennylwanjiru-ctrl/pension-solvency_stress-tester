import pandas as pd
import sqlite3
import os

# Define file paths
db_path = 'data/pension_alm.db'
roster_csv = 'data/employee_roster.csv'
assets_csv = 'data/fund_assets.csv'
output_csv = 'data/liability_timeline_results.csv'

print("🔄 Initializing SQLite database container...")
conn = sqlite3.connect(db_path)

print("📥 Ingesting synthetic data tables...")
roster_df = pd.read_csv(roster_csv)
assets_df = pd.read_csv(assets_csv)

# 1. Calculate base individual retirement parameters via Pandas first
print("📐 Computing retirement individual horizons...")
roster_df['years_to_retirement'] = 65 - roster_df['current_age']
roster_df['retirement_year'] = 2026 + roster_df['years_to_retirement']
roster_df['annual_pension_payout'] = round(0.015 * (roster_df['years_of_service'] + roster_df['years_to_retirement']) * roster_df['salary'], 2)

# Write baseline datasets directly into the database engine
roster_df.to_sql('employee_roster', conn, if_exists='replace', index=False)
assets_df.to_sql('fund_assets', conn, if_exists='replace', index=False)

# 2. Build our 40-year temporal calendar spine directly using Python
print("📅 Creating calendar temporal timeline skeleton...")
years = list(range(2026, 2067))
calendar_df = pd.DataFrame({'calendar_year': years})
calendar_df.to_sql('calendar_spine', conn, if_exists='replace', index=False)

# 3. Execute pure, standard relational joins and analytical window functions
print("⚡ Executing relational SQL processing analytics...")
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
        WHEN total_annual_liability_outflow = MAX(total_annual_liability_outflow) OVER() THEN '⚠️ PEAK CASH DEMAND YEAR'
        WHEN total_annual_liability_outflow > 0 THEN 'Active Payout Phase'
        ELSE 'Accumulation Phase (No Active Retirees)'
    END AS fund_risk_status
FROM LiabilityCurve
ORDER BY calendar_year;
"""

try:
    results_df = pd.read_sql_query(sql_query, conn)
    results_df.to_csv(output_csv, index=False)
    print(f"✅ Pipeline complete! Results exported to: '{output_csv}'\n")
    
    print("📋 --- PENSION FUND METRICS TIMELINE PREVIEW ---")
    print(results_df.to_string(index=False))
    
except Exception as e:
    print(f"❌ Error executing analytical framework: {e}")

finally:
    conn.close()
    print("\n🔒 Database connection isolated and closed safely.")