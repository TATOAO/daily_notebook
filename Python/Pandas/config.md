
# config

## display 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 一个cell里的长度，比如非常长的string, 只能展示一  半
pd.set_option('display.max_colwidth', None)


## float展示格式，展示成百分比


You could also set the default format for float :

pd.options.display.float_format = '{:.2%}'.format



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


## 服务器上的中文乱码问题

关键是怎么把字体文件传上去+怎么配置+清除缓存

[博客](https://www.biaodianfu.com/matplotlib-chinese.html ":)")

```py

import matplotlib as mpl
print(mpl.matplotlib_fname())

# font.family: sans-serif
# font.sans-serif:FangSong, Kaiti, DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
# axes.unicode_minus: True   ## use unicode for the minus symbol
                           ## rather than hyphen.  See
                           ## http://en.wikipedia.org/wiki/Plus_and_minus_signs#Character_codes

# rm -rf ~/.cache/matplotlib
# rm -rf ~/.matplotlib

```





