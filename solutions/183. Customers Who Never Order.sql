/* Write your PL/SQL query statement below */
--select name as customers from customers where id not in(
--select c.id from customers c inner join orders o
--on o.customerid=c.id)
​
select c.name as customers from customers c left join orders o
on o.customerid=c.id where o.customerid is null
