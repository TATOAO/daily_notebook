
## 镜像

可以在使用pip的时候在后面加上-i参数，指定pip源

```
pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
```


-  阿里云 http://mirrors.aliyun.com/pypi/simple/
-  中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
-  豆瓣(douban) http://pypi.douban.com/simple/
-  清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
-  中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/



## Wheel 

https://www.activestate.com/resources/quick-reads/python-install-wheel/

Open source Python packages can be installed from Source Distributions (sdist) or Wheels (whl). According to the Python Packaging Authority (PyPA), wheels are the preferred way that pip installs Python modules from the Python Package Index (PyPI) because they’re smaller, faster to install, and more efficient than building the package from the source code contained in an sdist.


##### pip download wheel
python -m pip download --only-binary :all: --dest . --no-cache <package_name> 

##### pip install wheel

pip install some-packge.whl




##### manage cache 

(python -m means directly run module as script)

python -m pip cache dir
python -m pip cache info
python -m pip cache list [<pattern>] [--format=[human, abspath]]
python -m pip cache remove <pattern>
python -m pip cache purge