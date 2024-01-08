
# 按interval 聚合


```py

ranges = [100*i for i in range(22)]
df.groupby(pd.cut(df['content_length'], ranges)).count()['content_length'].plot(kind='bar', figsize=(12,8), title='Labeled Dialog Content Length')

```