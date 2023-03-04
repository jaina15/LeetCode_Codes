/*
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your PL/SQL query statement below
 */
DELETE FROM PERSON WHERE (EMAIL,ID) NOT IN (
SELECT EMAIL,MIN(ID) AS ID
FROM PERSON
GROUP BY EMAIL)
