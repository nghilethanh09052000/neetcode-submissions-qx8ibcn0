-- Write your query below
select
    a.team_id,
    a.team_name,
    coalesce(
        sum(
            case 
                when a.team_id = b.host_team and b.host_goals > b.guest_goals then 3
                when a.team_id = b.guest_team and b.guest_goals > b.host_goals then 3
                when b.host_goals = b.guest_goals then 1
            else 0 end
        ), 0
    ) as num_points
from teams a
left join matches b
on a.team_id = b.host_team or a.team_id = b.guest_team
group by a.team_id, a.team_name
order by 3 desc, 1 asc