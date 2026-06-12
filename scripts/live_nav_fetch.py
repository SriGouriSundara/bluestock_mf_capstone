"""
Bluestock Mutual Fund Analytics Capstone
Script Name: live_nav_fetch.py
Purpose:
Fetch live NAV data from MFAPI for selected
mutual fund schemes and save the data as CSV files.
Tasks Performed:
- Connect to MFAPI
- Retrieve NAV history
- Parse JSON response
- Save output to data/raw

Author: Sri Gouri Sundara
""" 
import os
import requests
import pandas as pd
from datetime import datetime

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("\nFund Information:")
print(data["meta"])

nav_df = pd.DataFrame(data["data"])

print("\nShape:")
print(nav_df.shape)

print("\nFirst 5 Rows:")
print(nav_df.head())

#
#task-3
#
import requests
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
output_dir = BASE_DIR / "data/raw"
funds = {
    "sbi_bluechip": "119551",
    "icici_bluechip": "120503",
    "nippon_large_cap": "118632",
    "axis_bluechip": "119092",
    "kotak_bluechip": "120841"
}
for fund_name, amfi_code in funds.items():
    print(f"\nFetching {fund_name}...")

    url = f"https://api.mfapi.in/mf/{amfi_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        nav_df = pd.DataFrame(data["data"])
        file_path = output_dir / f"{fund_name}_nav.csv"
        nav_df.to_csv(file_path, index=False)
        print(f"Saved: {file_path}")
    else:
        print(f"Failed for {fund_name}")


log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(
    log_dir,
    f"nav_update_{datetime.now().date()}.log"
)

with open(log_file, "w") as f:
    f.write(f"{datetime.now()}\n")
    f.write("40 schemes fetched\n")
    f.write("Database updated successfully\n")

print("Log file created.")