-- Write your query below
with cte as (
    select
        p.product_name,
        p.product_id,
        o.order_id,
        o.order_date,
        dense_rank() over(partition by o.product_id order by o.order_date desc) as rn
    from orders o
    join products p
    on o.product_id = p.product_id 
)
select
    product_name,
    product_id,
    order_id,
    order_date
from cte
where rn = 1
order by 1 asc , 2 asc, 3 asc
