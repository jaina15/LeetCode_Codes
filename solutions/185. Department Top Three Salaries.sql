/* Write your PL/SQL query statement below */
SELECT DEPARTMENT,EMPLOYEE,SALARY FROM (
    SELECT
    D.NAME AS DEPARTMENT,
    E.NAME AS EMPLOYEE,
    E.SALARY,
    DENSE_RANK() OVER(PARTITION BY D.NAME ORDER BY E.SALARY DESC) RN
    FROM EMPLOYEE E
    INNER JOIN 
    DEPARTMENT D
    ON E.DEPARTMENTID = D.ID)
WHERE RN <=3
