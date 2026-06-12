select
    c.customer_id,
    c.customer_name
from customers c
join orders o
on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name
having 
    COUNT(DISTINCT CASE WHEN o.product_name IN ('A', 'B') THEN o.product_name END) = 2
    AND COUNT(CASE WHEN o.product_name = 'C' THEN 1 END) = 0
order by 2