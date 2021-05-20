CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    select distinct salary into result from (
    select salary, dense_rank() over (order by salary desc) rn from employee)
    where rn=n;
    
    RETURN result;
END;
