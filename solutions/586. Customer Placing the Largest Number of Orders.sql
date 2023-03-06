/* Write your PL/SQL query statement below */
SELECT * FROM (
SELECT CUSTOMER_NUMBER
FROM ORDERS
GROUP BY CUSTOMER_NUMBER
ORDER BY COUNT(ORDER_NUMBER) DESC)
WHERE ROWNUM=1
