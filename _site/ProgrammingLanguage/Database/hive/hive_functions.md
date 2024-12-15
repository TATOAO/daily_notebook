


# to Unix time

hive unix_timestamp('2022-12-07')
会返回null，需要先变成日期的格式，
unix_timestamp( cast('2022-12-07' as date))

# 日期


```sql
date_add('2022-10-10', 5)

datediff('2022-10-11', '2022-10-10') 
-- 1


```

null handle 

datediff('2022-10-11', null) 不允


# format 

```sql

date_format(from_unixtime(unix_timestamp('20221011', 'yyyyMMdd')), 'yyyy-MM-dd')

```



