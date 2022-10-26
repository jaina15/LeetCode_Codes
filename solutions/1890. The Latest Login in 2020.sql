/* Write your PL/SQL query statement below */
SELECT USER_ID,
        MAX(TIME_STAMP) AS LAST_STAMP
FROM(
        SELECT
        USER_ID,
        TIME_STAMP
        FROM LOGINS
        WHERE EXTRACT(YEAR FROM TIME_STAMP)=2020)
GROUP BY USER_ID
