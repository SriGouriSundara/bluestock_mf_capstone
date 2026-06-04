-- (1)
SELECT fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- (2)
SELECT strftime('%Y-%m',nav_date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

-- (3)
SELECT transaction_type,
COUNT(*) total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- (4)
SELECT state,
SUM(amount_inr)
FROM fact_transactions
GROUP BY state
ORDER BY 2 DESC;

-- (5)
SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- (6)
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- (7)
SELECT risk_category,
COUNT(*)
FROM dim_fund
GROUP BY risk_category;

-- (8)
SELECT fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- (9)
SELECT category,
AVG(return_3yr_pct)
FROM fact_performance
GROUP BY category;

 --(10)

SELECT kyc_status,
COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;