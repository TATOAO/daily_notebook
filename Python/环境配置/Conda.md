# anaconda

如果要创建环境


根据ymlfile
```bash
conda env create -file environment.yml
conda env create -f environment.yml
```
yml 里面会提供一个名字


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
