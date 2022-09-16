# data Application

## Dummy Variable， hot code 

``` py
import pandas as pd
df = pd.concat([df, pd.dummies(df[['renew', 'hprice_cn']])], axis=1)
# 会自动合并 column name 和 value 的类型



```

## Query



#### Any 只要一列

df[df.isna().any(axis=1)]
df[df.isin([25]).any(axis=1)]


