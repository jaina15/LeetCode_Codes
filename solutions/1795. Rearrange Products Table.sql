/* Write your PL/SQL query statement below */
​
SELECT 
PRODUCT_ID,LOWER(STORE) STORE,PRICE
FROM PRODUCTS
UNPIVOT(
PRICE
FOR STORE IN (store1,store2,store3))
ORDER BY 1
​
/*
​
SELECT product_id, 'store1' AS store, store1 AS price FROM Products WHERE store1 IS NOT NULL
UNION 
SELECT product_id, 'store2' AS store, store2 AS price FROM Products WHERE store2 IS NOT NULL
UNION 
SELECT product_id, 'store3' AS store, store3 AS price FROM Products WHERE store3 IS NOT NULL
​
ORDER BY 1,2 ASC
​
*/
