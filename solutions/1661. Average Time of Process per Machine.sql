/* Write your PL/SQL query statement below */
WITH CTE AS (
    SELECT
    machine_id ,
    process_id ,
    SUM(CASE WHEN activity_type ='start' THEN timestamp  ELSE 0 END) AS STARTT,
    SUM(CASE WHEN activity_type ='end' THEN timestamp  ELSE 0 END) AS ENDD
    FROM ACTIVITY
    GROUP BY machine_id ,process_id )
​
SELECT
MACHINE_ID,
ROUND(SUM(ENDD-STARTT)/COUNT(PROCESS_ID),3) AS PROCESSING_TIME
FROM CTE
GROUP BY MACHINE_ID
