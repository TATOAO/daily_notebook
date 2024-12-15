## Index Product

``` py
In [8]: iterables = [["bar", "baz", "foo", "qux"], ["one", "two"]]

In [9]: pd.MultiIndex.from_product(iterables, names=["first", "second"])
Out[9]: 
MultiIndex([('bar', 'one'),
            ('bar', 'two'),
            ('baz', 'one'),
            ('baz', 'two'),
            ('foo', 'one'),
            ('foo', 'two'),
            ('qux', 'one'),
            ('qux', 'two')],
           names=['first', 'second'])

```


[SO](https://stackoverflow.com/questions/17287933/filling-in-date-gaps-in-multiindex-pandas-dataframe ":)")


### groupby 天然有一个方便的方法

```py

groupby_df = df.groupby('xxxx')
new_index = pd.MultiIndex.from_product(df.index.levels)

```


## reindex

reindex

df2.reindex(index=all_dates).fillna(0)




