/* Write your PL/SQL query statement below */
with driver as(
select users_id from
users
where
banned='No'
and role='driver')
SELECT
REQUEST_AT AS DAY,
ROUND(CANCELLED/TOTAL,2) AS "Cancellation Rate" 
FROM(
    SELECT 
    T.REQUEST_AT,
    SUM(CASE WHEN STATUS <> 'completed' then 1 else 0 end) as cancelled,
    count(1) as total
    FROM TRIPS T
    INNER JOIN
    USERS U
    ON U.USERs_ID = T.CLIENT_ID
    inner join
    driver d
    on t.driver_id = d.users_id
    WHERE U.BANNED='No'
    AND T.REQUEST_AT BETWEEN '2013-10-01' AND '2013-10-03'
    group by t.request_at
    )
ORDER BY 1
