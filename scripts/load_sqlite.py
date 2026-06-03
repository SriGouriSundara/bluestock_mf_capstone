import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW = BASE_DIR / "data" / "raw"
PROCESSED = BASE_DIR / "data" / "processed"
DB = BASE_DIR / "data" / "db"

DB.mkdir(exist_ok=True)

db_file = DB / "bluestock_mf.db"

conn = sqlite3.connect(db_file)

print("Connected to SQLite")

# ------------------
# DIM FUND
# ------------------

fund = pd.read_csv(
    RAW / "01_fund_master.csv"
)

fund.to_sql(
    "dim_fund",
    conn,
    if_exists="replace",
    index=False
)

print("dim_fund loaded")

# ------------------
# FACT NAV
# ------------------

nav = pd.read_csv(
    PROCESSED /
    "nav_history_clean.csv"
)

nav.rename(
    columns={
        "date":"nav_date"
    },
    inplace=True
)

nav.to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

print("fact_nav loaded")

# ------------------
# FACT TRANSACTIONS
# ------------------

txn = pd.read_csv(
    PROCESSED /
    "investor_transactions_clean.csv"
)

txn.to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded")

# ------------------
# FACT PERFORMANCE
# ------------------

perf = pd.read_csv(
    PROCESSED /
    "scheme_performance_clean.csv"
)

perf.to_sql(
    "fact_performance",
    conn,
    if_exists="replace",
    index=False
)

print("fact_performance loaded")

# ------------------
# FACT AUM
# ------------------

aum = pd.read_csv(
    RAW /
    "03_aum_by_fund_house.csv"
)

aum.rename(
    columns={
        "date":"report_date"
    },
    inplace=True
)

aum.to_sql(
    "fact_aum",
    conn,
    if_exists="replace",
    index=False
)

print("fact_aum loaded")

conn.close()

print("\nDatabase Loading Complete")