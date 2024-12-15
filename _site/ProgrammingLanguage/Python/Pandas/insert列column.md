
# insert column

``` py
df.insert(loc, column, value)

df = pd.DataFrame({'B': [1, 2, 3], 'C': [4, 5, 6]})

df
Out: 
   B  C
0  1  4
1  2  5
2  3  6

idx = 0
new_col = [7, 8, 9]  # can be a list, a Series, an array or a scalar   
df.insert(loc=idx, column='A', value=new_col)

df
Out: 
   A  B  C
0  7  1  4
1  8  2  5
2  9  3  6

```