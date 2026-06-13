-- Write your query below
select
    a.seller_name
from seller a
where a.seller_id not in (
    select seller_id from orders
    where extract(year from sale_date) = '2020'
)
order by 1 asc