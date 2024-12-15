

# date format changing

``` sql

date_format(date(date_date) + interval '-1' day, 'yyyy-MM-dd') as minus_one_day

```



# from YYYYMMDD to YYYY-MM-DD


```sql

方法1: from_unixtime+ unix_timestamp
--20171205转成2017-12-05 
select from_unixtime(unix_timestamp('20171205','yyyymmdd'),'yyyy-mm-dd') from dual;

--2017-12-05转成20171205
select from_unixtime(unix_timestamp('2017-12-05','yyyy-mm-dd'),'yyyymmdd') from dual;

方法2: substr + concat
--20171205转成2017-12-05 
select concat(substr('20171205',1,4),'-',substr('20171205',5,2),'-',substr('20171205',7,2)) from dual;

--2017-12-05转成20171205
select concat(substr('2017-12-05',1,4),substr('2017-12-05',6,2),substr('2017-12-05',9,2)) from dual;
```
