# Bluestock Mutual Fund Analytics Capstone

## Project Overview:

This project analyzes Indian mutual fund industry data using Python, SQLite, and Power BI.
The objective is to perform end-to-end data analytics, including:
- ETL Processing
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Performance Analytics
- Advanced Risk Analytics
- Interactive Dashboard Development
This project covers mutual fund performance,investor behaviour,SIP trends,AUM growth,portfolio concentration and risk-adjusted returns.
---

## Objective:

- Build an ETL pipeline for mutual fund datasets.
- Design and implement a SQLite database.
- Perform data cleaning and validation.
- Conduct exploratory data analysis (EDA).
- Calculate performance metrics such as CAGR, Sharpe Ratio, Sortino - Ratio, Alpha, Beta, and Maximum Drawdown.
- Perform advanced risk analytics including VaR and CVaR.
- Build a Power BI dashboard for interactive analysis.
- Generate insights and recommendations for investors.
---

## Project Architecture:

```text
Raw Data
   ↓
ETL
   ↓
Data Cleaning
   ↓
SQLite Database
   ↓
EDA
   ↓
Performance Analytics
   ↓
Advanced Analytics
   ↓
Power BI Dashboard
```

---

## Project Structure:

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── load_sqlite.py
│   ├── verify_database.py
│   ├── recommender.py
│   └── run_pipeline.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   └── dashboard.pdf
│
├── reports/
│   ├── charts/
│   └── data_dictionary.md
│
├── README.md
└── requirements.txt
```

---

## Datasets Used:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Technologies Used:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SQLite
- SQLAlchemy
- Jupyter Notebook
- Power BI

---

## Setup Instructions

### Clone Repository:

```bash
git clone <repository_url>
cd bluestock_mf_capstone
```

### Install Dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## Running the ETL Pipeline:

```bash
python scripts/run_pipeline.py
```

This executes:

- ETL Processing
- NAV Data Ingestion
- Database Loading
- Database Verification

---

## Opening the Dashboard:

Open the following file in Power BI Desktop:

```text
dashboard/bluestock_mf_dashboard.pbix
```

Dashboard Pages:

1. Industry Overview
2. Fund Performance
3. Investor Analytics
4. SIP & Market Trends

---

## Key Outputs:

### Performance Analytics:

- fund_scorecard.csv
- alpha_beta.csv
- sharpe_ratios.csv
- sortino_ratios.csv
- max_drawdown.csv

### Advanced Analytics:

- var_cvar_report.csv
- rolling_sharpe_chart.png

### Dashboard Outputs:

- dashboard.pdf
- page1_industry_overview.png
- page2_fund_performance.png
- page3_investor_analytics.png
- page4_sip_market_trends.png

---

## Key Findings:

- Mutual fund AUM showed strong growth during 2022–2025.
- SIP inflows reached record highs in 2025.
- Several funds demonstrated superior risk-adjusted returns.
- Investor participation increased significantly across states.
- Advanced risk metrics helped identify high-risk schemes.

---

## Author
Sri Gouri Sundara

Bluestock Mutual Fund Analytics Capstone Project