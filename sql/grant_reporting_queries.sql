-- Nonprofit Grant Reporting Data System
-- SQL Portfolio Queries
-- Author: David Niyigena

-- 1. View all grant reporting records
SELECT *
FROM grant_reporting_data;

-- 2. Total grant budget by donor
SELECT
    donor,
    SUM(grant_amount) AS total_grant_amount
FROM grant_reporting_data
GROUP BY donor
ORDER BY total_grant_amount DESC;

-- 3. Total amount spent by program area
SELECT
    program_area,
    SUM(amount_spent) AS total_amount_spent
FROM grant_reporting_data
GROUP BY program_area
ORDER BY total_amount_spent DESC;

-- 4. Calculate spending rate for each grant
SELECT
    grant_id,
    grant_name,
    donor,
    program_area,
    grant_amount,
    amount_spent,
    ROUND((amount_spent * 100.0 / grant_amount), 2) AS spending_rate
FROM grant_reporting_data
ORDER BY spending_rate DESC;

-- 5. Identify grants with low spending rates
SELECT
    grant_id,
    grant_name,
    donor,
    program_area,
    grant_amount,
    amount_spent,
    ROUND((amount_spent * 100.0 / grant_amount), 2) AS spending_rate
FROM grant_reporting_data
WHERE (amount_spent * 100.0 / grant_amount) < 70
ORDER BY spending_rate ASC;

-- 6. Identify grants with high spending rates
SELECT
    grant_id,
    grant_name,
    donor,
    program_area,
    grant_amount,
    amount_spent,
    ROUND((amount_spent * 100.0 / grant_amount), 2) AS spending_rate
FROM grant_reporting_data
WHERE (amount_spent * 100.0 / grant_amount) >= 90
ORDER BY spending_rate DESC;

-- 7. Summarize grants by reporting status
SELECT
    reporting_status,
    COUNT(*) AS number_of_grants,
    SUM(grant_amount) AS total_grant_amount,
    SUM(amount_spent) AS total_amount_spent
FROM grant_reporting_data
GROUP BY reporting_status
ORDER BY number_of_grants DESC;

-- 8. Count grants with compliance issues
SELECT
    compliance_issue,
    COUNT(*) AS number_of_records
FROM grant_reporting_data
GROUP BY compliance_issue
ORDER BY number_of_records DESC;

-- 9. Identify grants with compliance issues
SELECT
    grant_id,
    grant_name,
    donor,
    program_area,
    compliance_issue,
    reporting_status
FROM grant_reporting_data
WHERE compliance_issue = 'Yes';

-- 10. Total beneficiaries reached by program area
SELECT
    program_area,
    SUM(beneficiaries_reached) AS total_beneficiaries_reached
FROM grant_reporting_data
GROUP BY program_area
ORDER BY total_beneficiaries_reached DESC;

-- 11. Average spending rate by donor
SELECT
    donor,
    ROUND(AVG(amount_spent * 100.0 / grant_amount), 2) AS average_spending_rate
FROM grant_reporting_data
GROUP BY donor
ORDER BY average_spending_rate DESC;

-- 12. Grant performance by quarter
SELECT
    reporting_period,
    SUM(grant_amount) AS total_grant_amount,
    SUM(amount_spent) AS total_amount_spent,
    ROUND((SUM(amount_spent) * 100.0 / SUM(grant_amount)), 2) AS overall_spending_rate
FROM grant_reporting_data
GROUP BY reporting_period
ORDER BY reporting_period;

-- 13. Identify grants that need follow-up
SELECT
    grant_id,
    grant_name,
    donor,
    program_area,
    reporting_status,
    compliance_issue,
    ROUND((amount_spent * 100.0 / grant_amount), 2) AS spending_rate
FROM grant_reporting_data
WHERE reporting_status IN ('Delayed', 'Incomplete')
   OR compliance_issue = 'Yes'
   OR (amount_spent * 100.0 / grant_amount) < 70
ORDER BY spending_rate ASC;

-- 14. Regional grant summary
SELECT
    region,
    COUNT(*) AS number_of_grants,
    SUM(grant_amount) AS total_grant_amount,
    SUM(amount_spent) AS total_amount_spent,
    SUM(beneficiaries_reached) AS total_beneficiaries_reached
FROM grant_reporting_data
GROUP BY region
ORDER BY total_grant_amount DESC;

-- 15. Program area summary for reporting dashboard
SELECT
    program_area,
    COUNT(*) AS number_of_grants,
    SUM(grant_amount) AS total_grant_amount,
    SUM(amount_spent) AS total_amount_spent,
    ROUND((SUM(amount_spent) * 100.0 / SUM(grant_amount)), 2) AS spending_rate,
    SUM(beneficiaries_reached) AS total_beneficiaries_reached
FROM grant_reporting_data
GROUP BY program_area
ORDER BY total_beneficiaries_reached DESC;
