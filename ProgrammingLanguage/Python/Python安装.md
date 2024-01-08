# 从源码安装


https://tecadmin.net/how-to-install-python-3-9-on-ubuntu-20-04/




```bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo 
sudo 
sudo 
sudo 
sudo 



tar xzf Python-3.9.16.tgz 
cd Python-3.9.16 
sudo ./configure --enable-optimizations 
sudo make altinstall 
```




## 经常遇到的问题


### 漏装 各种包 _ctype
前面没装全 prerequisite


https://stackoverflow.com/questions/27022373/python3-importerror-no-module-named-ctypes-when-using-value-from-module-mul

```bash

sudo apt-get install libffi-dev
cd Python3.xxx
./configure
sudo make altinstall
```


### 

