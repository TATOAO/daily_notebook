
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
