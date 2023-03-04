/* Write your PL/SQL query statement below */
SELECT *
FROM CINEMA
WHERE MOD(ID,2)=1
AND DESCRIPTION<>'boring'
order by rating desc
