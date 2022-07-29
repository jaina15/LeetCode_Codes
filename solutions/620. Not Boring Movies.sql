/* Write your PL/SQL query statement below */
SELECT * FROM CINEMA
WHERE DESCRIPTION <> 'boring' AND MOD(ID,2) <> 0
ORDER BY RATING DESC
