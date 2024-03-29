/* Write your PL/SQL query statement below */
SELECT U.USER_ID AS BUYER_ID,TO_CHAR(U.JOIN_DATE,'YYYY-MM-DD') AS JOIN_DATE,COUNT(O.ORDER_ID) AS ORDERS_IN_2019
FROM USERS U
LEFT JOIN ORDERS O
ON U.USER_ID=O.BUYER_ID
AND EXTRACT(YEAR FROM O.ORDER_DATE)=2019
GROUP BY U.USER_ID,TO_CHAR(U.JOIN_DATE,'YYYY-MM-DD') 
ORDER BY 1
