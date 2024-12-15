



# 窗口函数 安日期 设 time frame


```sql
-- hive sql

select 

count(1) over (partion by mb_no order by unix_timestamp(stat_dt) range between
604800 preceding and current row) as last_7_day_send_count

from ..

-- 604800 = 60 * 60 * 24 * 7 这个里面只能放一个整数，不能放运算

```
