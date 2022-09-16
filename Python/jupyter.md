# short count


## 非编辑状态


(以下 快捷键 区分大小写)

##### cell nevigate 操作
jk 上下

##### 多cell 操作
J   -   选中下一个cell
M   -   Merge

##### cell 改变状态
m   -   enter markdown mode
y   -   enter code mode

##### cell nevigate 操作
dd  -   删除cell
z   -   撤销删除cell


##### cell edit
x   -   cut
v   -   paste
c   -   copy


#### jupyter import module， model更新不同步问题

```py

import importlib
correct = importlib.import_module('correct') 
importlib.reload(correct)

## correct.user_replace_table

```


#### magic function

https://ipython.readthedocs.io/en/stable/interactive/python-ipython-diff.html