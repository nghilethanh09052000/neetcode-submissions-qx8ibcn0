with all_friends as (
    select user1_id as user_id from friendship where user2_id = 1
    union
    select user2_id as user_id from friendship where user1_id = 1
)
, joined as (
    select
        a.page_id as recommended_page
    from likes a
    join all_friends b
    on a.user_id = b.user_id
    where a.page_id not in (select page_id from likes where user_id = 1)
)

select distinct * from joined