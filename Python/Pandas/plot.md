
# 中文乱码问题
``` py

#### Windows
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'



#### MacOS
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

```

# bar plot


``` py

ax = df.sort_values('count',ascending=False).set_index("intent").plot(kind='bar',
                                    figsize=(14,8),
                                    title="Number for intents")

# 使用 index 作为 x 坐标的值, 所以需要 set_index

ax.set_xlabel("intents")
ax.set_ylabel("Frequency")
```
