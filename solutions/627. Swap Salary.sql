/* Write your PL/SQL query statement below */
UPDATE
SALARY SET SEX = CASE WHEN SEX='m' then 'f'
                      else 'm'
                 end;
