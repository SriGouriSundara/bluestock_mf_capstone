"""
Bluestock Mutual Fund Analytics Capstone
Script Name: recommender.py
Purpose:
Recommend mutual funds based on
investor risk appetite.
Risk Categories:
- Low Risk
- Moderate Risk
- High Risk
Tasks Performed:
- Read performance metrics
- Filter by risk profile
- Rank funds using Sharpe Ratio
- Display top recommendations

Author: Sri Gouri Sundara
"""
import pandas as pd

scorecard = pd.read_csv(
    "../data/processed/fund_scorecard.csv"
)

fund_master = pd.read_csv(
    "../data/raw/01_fund_master.csv"
)

df = scorecard.merge(
    fund_master,
    on="amfi_code",
    how="left"
)

print(df["risk_category"].dropna().unique())

risk = input(
    "Enter Risk Level (Low/Moderate/High): "
)

result = (
    df[
        df["risk_category"]
        .str.lower()
        .str.contains(risk.lower(), na=False)
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(
    result[
        [
            "amfi_code",
            "scheme_name",
            "risk_category",
            "sharpe_ratio"
        ]
    ]
)