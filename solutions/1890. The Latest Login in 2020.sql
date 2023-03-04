/* Write your PL/SQL query statement below */
SELECT USER_ID,LAST_STAMP FROM(
SELECT
USER_ID,
TIME_STAMP AS LAST_STAMP,
ROW_NUMBER() OVER(PARTITION BY USER_ID ORDER BY TIME_STAMP DESC) RN
FROM LOGINS
WHERE EXTRACT(YEAR FROM TIME_STAMP)=2020)
WHERE RN=1
