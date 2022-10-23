/*
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your PL/SQL query statement below
 */
DELETE FROM PERSON WHERE ID IN (
    SELECT ID FROM (
        SELECT
        EMAIL,ID,ROW_NUMBER() OVER(PARTITION BY EMAIL ORDER BY ID) RN
        FROM PERSON
    ) WHERE RN>1
)
