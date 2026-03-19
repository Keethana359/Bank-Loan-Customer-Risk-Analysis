-- Total customers by job
SELECT job, COUNT(*) 
FROM customers
GROUP BY job;

-- Loan approval rate
SELECT y AS loan_status, COUNT(*) 
FROM customers
GROUP BY y;

-- Average age by loan status
SELECT y, AVG(age)
FROM customers
GROUP BY y;