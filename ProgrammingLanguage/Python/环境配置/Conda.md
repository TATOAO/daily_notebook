# anaconda

如果要创建环境


根据ymlfile
```bash
conda env create -file environment.yml
conda env create -f environment.yml

```
yml 里面会提供一个名字


## 制定python版本
conda create -n mypython3 python=3

直接创建：
```bash
conda create --name myenv
```

然后后来再用yml update 
```bash
conda activate myenv
conda env update --file local.yml

```

检查现在有什么包：

``` bash
conda list
```


检查现在有什么环境：
``` bash
conda env list

```



指定特定的目录 create 环境

[SO](https://stackoverflow.com/questions/37926940/how-to-specify-new-environment-location-for-conda-create ":)")

```bash
conda create --prefix /tmp/test-env python=2.7

## 删除环境

```

conda remove -n env_name --all
>>>>>>> main

```
