-- Write your query below
select
    c.customer_id, c.name
from orders o
join customers c
on o.customer_id = c.customer_id
join product p
on o.product_id = p.product_id
where
    TO_CHAR(o.order_date, 'YYYY-MM') IN ('2020-06', '2020-07')
group by c.customer_id, c.name
having
    sum(
        case when TO_CHAR(o.order_date, 'YYYY-MM') = '2020-06' then p.price * o.quantity end
    ) >= 100
    and 
    sum(
        case when TO_CHAR(o.order_date, 'YYYY-MM') = '2020-07' then p.price * o.quantity end
    ) >= 100
