
# config

## display 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 一个cell里的长度，比如非常长的string, 只能展示一  半
pd.set_option('display.max_colwidth', None)




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
