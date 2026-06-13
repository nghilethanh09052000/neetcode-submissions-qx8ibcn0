-- Write your query below
with cte as (
    select
        transaction_id,
        dense_rank() over (partition by extract(day from day) order by amount desc) as rnk
    from transactions
)
select
    transaction_id
from cte
where rnk = 1
order by 1 asc

