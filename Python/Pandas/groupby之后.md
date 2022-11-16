# groupby 索引

``` py

grouped = df.groupby("column_name")

grouped.get_group("game_name")
## directly return the sub set of df

```



# groupby agg 单列数据
``` py
df.groupby('id')['是客服先说'].agg(lambda x: any(x)).value_counts() / 8975
```

## unique count

df.groupby('date').nunique()


# groupby agg 多个单列数据

``` py

def agg_path(x):
    return ','.join(x)

df.groupby("customer_no")[['date', 'name']].agg(agg_path)
#  return seperat column of path connected by ','
```
