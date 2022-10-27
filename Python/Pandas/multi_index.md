
## reindex

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



https://stackoverflow.com/questions/17287933/filling-in-date-gaps-in-multiindex-pandas-dataframe


reindex