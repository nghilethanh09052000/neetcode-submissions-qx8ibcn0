-- Write your query below
select
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE
        WHEN e.operator = '>' AND lv.value > rv.value THEN 'true'
        WHEN e.operator = '<' AND lv.value < rv.value THEN 'true'
        WHEN e.operator = '=' AND lv.value = rv.value THEN 'true'
        ELSE 'false'
    END AS value
from expressions e
join variables lv on e.left_operand = lv.name
JOIN variables rv ON e.right_operand = rv.name;
