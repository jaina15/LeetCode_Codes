/* Write your PL/SQL query statement below */
select e.name as employee from employee e inner join employee m 
on e.managerid=m.id and e.salary>m.salary
