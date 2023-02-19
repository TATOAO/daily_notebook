

# Drop


## 混合格式，在数字列去掉文本的行


[SO](https://stackoverflow.com/questions/54953980/drop-rows-in-a-subset-of-columns-in-mixed-data-type-data-frame ":)")


```py

d = np.array([[18, 1, 0, 1.0, 5.0, 0, 1],
                [89, 3, 1, 1.0, 1.0, 1, 1],
                [100, 4, 7, 0.0, 1.0, 1, 0],
                [200, 0, 1, 0.0, 0.0, 1, 0],
                [300, 1, 1, 0.0, 1.0, 1, 1],
                [19, 1, 1, 1.0, 1.0, 6, 1]])

df = pd.DataFrame(data=d, columns = ['Age','Prod1','Prod2', 'Day 4', 'Day 5', 'Day 6', 'Region'])
df = df.drop(
		df[~df.loc[:, 'Prod1':'Region'].isin([0, 1]).all(axis=1)].index
	)    
print(df)

```


[SO](https://stackoverflow.com/questions/54426845/how-to-check-if-a-pandas-dataframe-contains-only-numeric-values-column-wise ":)")

```py

df.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all())

```

