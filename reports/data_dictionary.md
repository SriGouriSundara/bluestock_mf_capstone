BlueStock Mutual Fund Capstone Project 
---------------------------------------=

Data Dictionary:

Project Name: BlueStock Mutual Fund Analytics Capstone
Prepared By: Sri Gouri Sundara
Date: 03 June 2026
---

1. Purpose of this Document:

This Data Dictionary provides a detailed description of all datasets used in the BlueStock Mutual Fund Analytics Project. It serves as a reference guide for understanding data fields, business definitions, data types, and source files used throughout the ETL, database, analytics, and dashboard development phases.

---

2. Dataset Overview:

Dataset ID| Dataset Name| Source File| Purpose
D1| Fund Master| 01_fund_master.csv| Master reference for all mutual fund schemes
D2| NAV History| 02_nav_history.csv| Historical Net Asset Value tracking
D3| AUM by Fund House| 03_aum_by_fund_house.csv| Assets Under Management analysis
D4| Monthly SIP Inflows| 04_monthly_sip_inflows.csv| SIP investment trend analysis
D5| Category Inflows| 05_category_inflows.csv| Fund category investment flows
D6| Industry Folio Count| 06_industry_folio_count.csv| Investor participation analysis
D7| Scheme Performance| 07_scheme_performance.csv| Fund performance evaluation
D8| Investor Transactions| 08_investor_transactions.csv| Investor transaction analysis
D9| Portfolio Holdings| 09_portfolio_holdings.csv| Portfolio composition analysis
D10| Benchmark Indices| 10_benchmark_indices.csv| Market benchmark comparison

---

3. Dataset Details

D1 – Fund Master:

* Business Purpose:
Acts as the master reference table containing scheme-level information for all mutual funds included in the project.

* Source File:
"01_fund_master.csv":
Column Name| Data Type| Business Definition
amfi_code| Integer| Unique AMFI scheme identifier
fund_house| Text| Asset Management Company (AMC) name
scheme_name| Text| Official mutual fund scheme name
category| Text| Broad fund category
sub_category| Text| Detailed scheme classification
plan| Text| Direct or Regular investment plan
launch_date| Date| Date the scheme was launched
benchmark| Text| Benchmark index used for performance comparison
expense_ratio_pct| Decimal| Annual management expense ratio (%)
exit_load_pct| Decimal| Fee charged for early redemption (%)
min_sip_amount| Decimal| Minimum SIP investment amount
min_lumpsum_amount| Decimal| Minimum one-time investment amount
fund_manager| Text| Name of scheme fund manager
risk_category| Text| Scheme risk classification
sebi_category_code| Text| SEBI category identifier

---

D2 – NAV History

* Business Purpose:
Stores daily Net Asset Value (NAV) information used for performance analysis, return calculations, volatility measurement, and dashboard reporting.

* Source File:
"02_nav_history.csv":
Column Name| Data Type| Business Definition
amfi_code| Integer| Mutual fund scheme identifier
date| Date| NAV reporting date
nav| Decimal| Net Asset Value per unit

---

D7 – Scheme Performance:

* Business Purpose:
Provides historical return and risk statistics used to evaluate scheme performance.

* Source File:
"07_scheme_performance.csv":

Column Name| Data Type| Business Definition
amfi_code| Integer| Scheme identifier
scheme_name| Text| Mutual fund scheme name
fund_house| Text| AMC managing the scheme
category| Text| Fund category
plan| Text| Direct or Regular plan
return_1yr_pct| Decimal| One-year return (%)
return_3yr_pct| Decimal| Three-year return (%)
return_5yr_pct| Decimal| Five-year return (%)
benchmark_3yr_pct| Decimal| Benchmark return over 3 years (%)
alpha| Decimal| Excess return generated over benchmark
beta| Decimal| Sensitivity to market movements
sharpe_ratio| Decimal| Risk-adjusted performance measure
sortino_ratio| Decimal| Downside risk-adjusted return measure
std_dev_ann_pct| Decimal| Annualized volatility (%)
max_drawdown_pct| Decimal| Maximum observed decline (%)
aum_crore| Decimal| Assets Under Management (₹ Crore)
expense_ratio_pct| Decimal| Annual expense ratio (%)
morningstar_rating| Integer| Morningstar fund rating
risk_grade| Text| Risk classification level

---

D8 – Investor Transactions

* Business Purpose:
Captures investor activity and transaction behavior across mutual fund schemes.

* Source File:
"08_investor_transactions.csv" :

Column Name| Data Type| Business Definition
investor_id| Text| Unique investor identifier
transaction_date| Date| Date of transaction
amfi_code| Integer| Mutual fund scheme identifier
transaction_type| Text| SIP, Lumpsum, or Redemption
amount_inr| Decimal| Transaction value in Indian Rupees
state| Text| Investor state
city| Text| Investor city
city_tier| Text| Tier classification of city
age_group| Text| Investor age segment
gender| Text| Investor gender
annual_income_lakh| Decimal| Annual income in lakhs
payment_mode| Text| Payment method used
kyc_status| Text| KYC verification status

---

4. Data Quality Rules Applied:

Validation Rule| Description
Duplicate Removal| Duplicate records removed from NAV data
Date Validation| All date fields converted to valid datetime format
Missing NAV Handling| Missing NAV values forward-filled for non-trading days
Positive NAV Validation| NAV values validated to be greater than zero
Positive Transaction Amount Validation| Transactions with invalid amounts removed
Transaction Standardization| SIP, Lumpsum and Redemption values standardized
Expense Ratio Validation| Expense ratios validated within acceptable range

---

5. Data Storage Architecture:

Raw Layer:
Stores original source files without modification.
data/raw/

Processed Layer:
Stores cleaned datasets ready for analytics.
data/processed/

Database Layer:
Stores structured SQLite database tables.
data/db/bluestock_mf.db

---

6. Business Usage:

The datasets documented in this Data Dictionary support:

* Mutual Fund Performance Analysis
* Risk Assessment
* Investor Behaviour Analysis
* SIP Growth Analysis
* AUM Trend Monitoring
* Benchmark Comparison
* Advanced Analytics and Performance Metrics

//  End of Document //
