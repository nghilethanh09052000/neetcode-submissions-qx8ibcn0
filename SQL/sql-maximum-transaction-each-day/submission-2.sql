select
    a.transaction_id
from transactions a
where ( date(day), amount ) IN (
    select date(day), max(amount) from transactions 
    group by date(day)
)
order by 1 asc