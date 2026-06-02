import pandas as pd 
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent  # root

#csv files

files = {
    "fund_master": BASE_DIR / "data/raw/01_fund_master.csv",
    "nav_history": BASE_DIR / "data/raw/02_nav_history.csv",
    "aum_by_fund_house": BASE_DIR / "data/raw/03_aum_by_fund_house.csv",
    "monthly_sip_inflows": BASE_DIR / "data/raw/04_monthly_sip_inflows.csv",
    "category_inflows": BASE_DIR / "data/raw/05_category_inflows.csv",
    "industry_folio_count": BASE_DIR / "data/raw/06_industry_folio_count.csv",
    "scheme_performance": BASE_DIR / "data/raw/07_scheme_performance.csv",
    "investor_transactions": BASE_DIR / "data/raw/08_investor_transactions.csv",
    "portfolio_holdings": BASE_DIR / "data/raw/09_portfolio_holdings.csv",
    "benchmark_indices": BASE_DIR / "data/raw/10_benchmark_indices.csv"
}
#load datasets

datasets = {}

for dataset_name, file_path in files.items():

    df = pd.read_csv(file_path)

    datasets[dataset_name] = df

    print("\n")
    print("=" * 60)
    print(dataset_name.upper())
    print("=" * 60)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

#
# fund matser analysis
#
print("\n" + "="*60)
print("FUND MASTER ANALYSIS")
print("="*60)
fund_master = datasets["fund_master"]
print("\nFund Houses")
print(fund_master["fund_house"].unique())
print("\nCategories")
print(fund_master["category"].unique())
print("\nSub Categories")
print(fund_master["sub_category"].unique())
print("\nRisk Grades")
print(fund_master["risk_category"].unique())

#
# amfi code validation
#
print("\n" + "="*60)
print("AMFI CODE VALIDATION")
print("="*60)

fund_master = datasets["fund_master"]
nav_history = datasets["nav_history"]

missing_codes = (
    set(fund_master["amfi_code"])
    - set(nav_history["amfi_code"])
)

if len(missing_codes) == 0:
    print("✅ Data Quality Passed")
else:
    print(" Missing Codes Found")
    print(missing_codes)