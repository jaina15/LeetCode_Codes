CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    SELECT DISTINCT SALARY INTO RESULT FROM (
        SELECT 
            SALARY,
            DENSE_RANK() OVER(ORDER BY SALARY DESC) RN
        FROM EMPLOYEE)
    WHERE RN=N;
    
    RETURN result;
END;
