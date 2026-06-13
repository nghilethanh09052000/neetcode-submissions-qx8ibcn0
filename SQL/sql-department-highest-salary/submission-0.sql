-- Write your query below
with cte as (
    select
        b.name as department,
        a.name as employee,
        a.salary,
        dense_rank() over (partition by b.name order by a.salary desc) as rn
    from employee a
    join department b
    on a.department_id = b.id
)
select 
    department,
    employee,
    salary
from cte
where rn = 1
