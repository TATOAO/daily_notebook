

# TYPE


## INT
TINYINT#
A 8-bit signed two’s complement integer with a minimum value of -2^7 and a maximum value of 2^7 - 1.

SMALLINT#
A 16-bit signed two’s complement integer with a minimum value of -2^15 and a maximum value of 2^15 - 1.

INTEGER#
A 32-bit signed two’s complement integer with a minimum value of -2^31 and a maximum value of 2^31 - 1. The name INT is also available for this type.

BIGINT#
A 64-bit signed two’s complement integer with a minimum value of -2^63 and a maximum value of 2^63 - 1.




## 和普通sql函数对比

``` sql

from_unixtime() -- presto , sql 也有？

unix_timestamp() -- sql ? 

```

FROM_TZ(CAST(datetime AS TIMESTAMP), 'UTC')



#### typeof

``` sql

typeof() -- presto


-- sql 没有 typeof 函数？

```


#### set variable

not able to set variable in presto


### date time and var

!! presto 双引号和单引号是不同的，一般表示varchar都是用的单引号

``` sql
select date_parse('7/22/2016 6:05:04 PM','%m/%d/%Y %h:%i:%s %p')
```

compare

```sql

from date_parse(stat_dt, '%Y-%m-%d') >= date '2022-10-10'

```
