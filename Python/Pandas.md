# data Application


## Stack

### column里有list，展开成一个元素一行
``` py
s = df['label'].apply(lambda x: pd.Series(x.split("#"))).stack().reset_index(level=1, drop=True)
df.drop('label', axis=1).join(s)
```


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


# config

## display 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

