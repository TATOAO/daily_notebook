
# bar plot


``` py

ax = df.sort_values('count',ascending=False).set_index("intent").plot(kind='bar',
                                    figsize=(14,8),
                                    title="Number for intents")

# 使用 index 作为 x 坐标的值, 所以需要 set_index

ax.set_xlabel("intents")
ax.set_ylabel("Frequency")
```


### bar count plot 

.value_counts()
``` py
stack_df['用户意图2'].value_counts().sort_values(ascending=False).plot(kind = 'bar')
```