/* Write your PL/SQL query statement below */
SELECT
CLASS
FROM COURSES
GROUP BY CLASS
HAVING COUNT(1)>=5
