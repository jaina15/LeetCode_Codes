/* Write your PL/SQL query statement below */
SELECT NAME, BALANCE FROM(
SELECT U.NAME,U.ACCOUNT,SUM(T.AMOUNT) BALANCE
FROM USERS U
LEFT JOIN TRANSACTIONS T
ON U.ACCOUNT=T.ACCOUNT
GROUP BY U.NAME,U.ACCOUNT)
WHERE BALANCE>10000