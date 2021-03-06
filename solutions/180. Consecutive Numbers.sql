/* Write your PL/SQL query statement below */
SELECT DISTINCT CONSECUTIVENUMS FROM(
SELECT
CASE
WHEN (NUM=LEAD(NUM) OVER(ORDER BY ID) AND NUM=LEAD(NUM,2) OVER(ORDER BY ID)) THEN NUM
END AS CONSECUTIVENUMS
FROM LOGS)
WHERE CONSECUTIVENUMS IS NOT NULL
