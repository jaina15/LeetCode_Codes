/* Write your PL/SQL query statement below */
SELECT DISTINCT P.PRODUCT_ID,P.PRODUCT_NAME
FROM PRODUCT P
INNER JOIN SALES S
ON P.PRODUCT_ID=S.PRODUCT_ID
WHERE SALE_DATE BETWEEN '2019-01-01' AND '2019-03-31'
AND P.PRODUCT_ID NOT IN (SELECT PRODUCT_ID FROM SALES WHERE SALE_DATE NOT BETWEEN '2019-01-01' AND '2019-03-31')
