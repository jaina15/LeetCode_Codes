select case when mod(id,2)=0 then id-1
when id in(select max(id) from seat) then id
when mod(id,2)=1 then id+1
end id, student from seat order by id
