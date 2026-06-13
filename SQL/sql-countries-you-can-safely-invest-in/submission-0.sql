select
    b.name as country
from person a
join country b
on substring(a.phone_number, 1, 3) = b.country_code
join calls c
on a.id = c.caller_id or a.id = c.callee_id
group by b.name
having avg(c.duration) > (select avg(duration) from calls)