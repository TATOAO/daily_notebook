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

找到有null的columns name
df.columns[df.isna().any()].tolist()


### query function


```py
df.query('value < 10 | value.isnull()')


In general, you could use @local_variable_name, so something like

>>> pi = np.pi; nan = np.nan
>>> df = pd.DataFrame({"value": [3,4,9,10,11,np.nan,12]})
>>> df.query("(value < 10) and (value > @pi)")
```

[StatckOverflow value](https://stackoverflow.com/questions/26535563/querying-for-nan-and-other-names-in-pandas ":)")








