-- Write your query below
select
    b.player_id, 
    b.player_name,
    count(a.player_id) as grand_slams_count
from (
    select wimbledon as player_id from championships
    union all
    select fr_open as player_id from championships
    union all
    select us_open as player_id from championships
    union all
    select au_open as player_id from championships
) a
join players b
on a.player_id = b.player_id
group by b.player_id, b.player_name