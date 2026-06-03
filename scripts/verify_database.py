import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

db_path = BASE_DIR / "data" / "db" / "bluestock_mf.db"

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count} rows")

conn.close()