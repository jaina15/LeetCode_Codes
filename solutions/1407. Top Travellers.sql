/* Write your PL/SQL query statement below */
SELECT NAME,TRAVELLED_DISTANCE FROM (
    SELECT U.ID,U.NAME,SUM(COALESCE(R.DISTANCE,0)) AS TRAVELLED_DISTANCE
    FROM USERS U LEFT JOIN RIDES R
    ON U.ID=R.USER_ID
    GROUP BY U.ID,U.NAME
    ORDER BY SUM(COALESCE(R.DISTANCE,0)) DESC,U.NAME)
