-- Write your query below
select
    app_sales.sale_date,
    app_sales.sold_num - org_sales.sold_num as diff
from sales app_sales
join sales org_sales
on 
    app_sales.sale_date = org_sales.sale_date
where app_sales.fruit = 'apples' and org_sales.fruit = 'oranges'
order by 1