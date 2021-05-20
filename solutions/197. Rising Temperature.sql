/* Write your PL/SQL query statement below */
​
select w.id from weather w, weather r where w.recorddate-r.recorddate=1
and w.temperature>r.temperature
​
