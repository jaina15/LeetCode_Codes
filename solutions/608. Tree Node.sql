/* Write your PL/SQL query statement below */
SELECT
ID,
CASE
    WHEN id IN (SELECT DISTINCT ID FROM TREE where p_id is null) THEN 'Root'
    WHEN ID IN (SELECT DISTINCT P_ID FROM TREE) THEN 'Inner'
    ELSE 'Leaf'
END AS TYPE
FROM TREE
