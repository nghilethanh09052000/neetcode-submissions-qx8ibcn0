with max_scores as (
    select
        student_id,
        max(score) as score
    from exam_results
    group by student_id
)

select
    a.student_id,
    min(b.exam_id) as exam_id,
    a.score
from max_scores a
join exam_results b
on 
    a.student_id = b.student_id
    and a.score = b.score
group by a.student_id, a.score
order by 1 asc