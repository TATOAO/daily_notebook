# Seaborn 中文乱码问题 

除了配置plt还需要额外配一下，而且需要每次运行画图前都执行一下这个命令？
```py
sns.set(font='SimHei', font_scale=0.8)        # 解决Seaborn中文显示问题

```

# seaborn 左右坐标

```py

fix, ax = plt.subplots()
nplot = sns.liineplot(x = 'age', y = 'uv_average_day', data = uv_avg, ax=ax)

plt.xticks(rotation = 90)
ax2 = nplot.twinx()

splot = sns.boxplot(data = percentage_df, x = 'age', y = 'huoyue_rate',
					orient='v', ax=ax2)

sns.set(rc={"figure.figsize":figure_ratio})

fig = splot.get_figure()
fig.savefig("xxxx.png")

```

[普通hold on plot for seabornSO](https://stackoverflow.com/questions/32899463/how-can-i-overlay-two-graphs-in-seaborn ":)")


[箱型图 seaborn 官网](https://seaborn.pydata.org/generated/seaborn.boxplot.html ":)")
