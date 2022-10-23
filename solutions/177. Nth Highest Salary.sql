CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    SELECT (
    SELECT DISTINCT SALARY FROM(
    SELECT SALARY,
           DENSE_RANK() OVER(ORDER BY SALARY DESC) RN
    FROM EMPLOYEE)
    WHERE RN=N) INTO RESULT
    FROM
    DUAL;
    
    RETURN result;
END;
