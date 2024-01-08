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




### jupyter notebook convert to py

```
jupyter nbconvert --to script *.ipynb

jupyter nbconvert --to html --stdout *.ipynb
jupyter nbconvert --to script --stdout *.ipynb
```


### defined variables

https://stackoverflow.com/questions/633127/viewing-all-defined-variables

```
dir()
globals()
locals()

$who

```


## 增加 jupyter notebook kernal

https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084


https://marketsplash.com/tutorials/ipython/ipython-kernel-install/

往jupyter 增加kernal 

```
pip install jupyter
pip install ipykernel
python -m ipykernel install --user --name=firstEnv
```



## python 版本

```py

import sys
sys.version_info
```
