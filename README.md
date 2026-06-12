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


### B1 – Automated ETL Scheduling

#### Objective

Automate the NAV data collection and ETL pipeline execution without manual intervention.

#### Implementation

A scheduling mechanism was configured to execute the NAV fetching script automatically every weekday at 8:00 PM.

The automation workflow performs the following tasks:

1. Fetches the latest mutual fund NAV data from MFAPI.
2. Validates and cleans the downloaded data.
3. Updates processed CSV files.
4. Refreshes the SQLite database.
5. Generates execution logs for monitoring.

#### Script Used

```text
scripts/live_nav_fetch.py
```

#### Scheduling Configuration

Linux Cron Example:

```bash
0 20 * * 1-5 python3 scripts/live_nav_fetch.py
```

Windows Task Scheduler:

* Trigger: Daily at 8:00 PM
* Days: Monday to Friday
* Action: Run Python executable
* Argument: scripts/live_nav_fetch.py

#### Expected Output

```text
data/processed/
    latest_nav_data.csv

data/db/
    bluestock_mf.db

logs/
    nav_update_YYYY-MM-DD.log
```

#### Benefits

* Eliminates manual data refresh.
* Ensures consistent NAV updates.
* Keeps analytics and dashboard data current.
* Demonstrates production-style ETL automation.

#### Sample Log Output

```text
2026-06-12 20:00:01 - ETL Started
2026-06-12 20:00:15 - NAV Data Downloaded
2026-06-12 20:00:24 - Database Updated
2026-06-12 20:00:25 - ETL Completed Successfully
```



### B3 – Monte Carlo Simulation for Future NAV Projection

#### Objective

Estimate potential future NAV growth over a 5-year investment horizon using Monte Carlo simulation and historical return distributions.

#### Methodology

The simulation uses historical daily returns of mutual funds to generate thousands of possible future price paths.

Steps:

1. Calculate daily percentage returns.
2. Estimate historical mean return and volatility.
3. Generate random returns using a normal distribution.
4. Simulate future NAV paths over 5 years.
5. Calculate confidence intervals and expected NAV values.

#### Assumptions

* Historical returns are representative of future behavior.
* Daily returns follow a normal distribution.
* Trading year consists of 252 trading days.
* Projection period = 5 years.

#### Parameters

```text
Simulation Runs : 1000
Projection Period : 5 Years
Trading Days/Year : 252
Total Days Simulated : 1260
```

#### Output Files

```text
data/processed/
    monte_carlo_projection.csv
```

#### Visualisations

The notebook generates:

* Simulated NAV trajectories
* Median forecast path
* 5th percentile confidence band
* 95th percentile confidence band

#### Sample Output

| Metric          | Value    |
| --------------- | -------- |
| Current NAV     | ₹78.00  |
| Median NAV (5Y) | ₹121.50 |
| 5th Percentile  | ₹94.20  |
| 95th Percentile | ₹158.80 |

#### Business Insights

* Provides a probabilistic view of future performance.
* Helps investors understand downside and upside scenarios.
* Quantifies uncertainty rather than relying on a single forecast.
* Useful for long-term investment planning and risk assessment.

#### Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Plotly

#### Deliverables

```text
notebooks/
    06_monte_carlo_simulation.ipynb

data/processed/
    monte_carlo_projection.csv

```


## Bonus Challenge B5 – Automated Weekly Email Report

Implemented an automated HTML report generator.

Script:
scripts/email_report.py

Output:
reports/weekly_report.html

Features:

- Top performing fund identification
- Lowest performing fund identification
- CAGR summary table
- Auto-generated HTML format
- Ready for SMTP email integration

## Author

Sri Gouri Sundara

Bluestock Mutual Fund Analytics Capstone Project
