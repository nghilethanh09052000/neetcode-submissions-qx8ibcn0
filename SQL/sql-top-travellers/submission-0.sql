-- Write your query below
select
    a.name,
    coalesce(sum(distance), 0 ) as travelled_distance
from users a 
left join rides b
on a.id = b.user_id
group by a.name
order by 2 desc, 1 asc