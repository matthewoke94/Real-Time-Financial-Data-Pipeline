-- Total Transaction Volume

SELECT SUM(amount)
FROM financial_transactions;

-- Transactions by Country

SELECT country, COUNT(*)
FROM financial_transactions
GROUP BY country;

-- Successful Transactions

SELECT *
FROM financial_transactions
WHERE status='SUCCESS';

-- Failed Transactions

SELECT *
FROM financial_transactions
WHERE status='FAILED';

-- Top 10 Largest Transactions

SELECT *
FROM financial_transactions
ORDER BY amount DESC
LIMIT 10;