/* Write your PL/SQL query statement below */
SELECT 
    SCORE,
    DENSE_RANK() OVER(ORDER BY SCORE DESC) AS RANK
FROM SCORES
