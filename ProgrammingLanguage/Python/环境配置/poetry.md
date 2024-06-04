

# poetry 用法


配置地址： pyproject.toml


```
poetry add module_name
poetry show 
poetry show module_name
poetry remove module_name


# specific version
poetry add module_name@8.8.8

# newer than current but smaller than the major version 3.0.0
# This is the default way when poetry add xxxx
poetry add module_name^2.3.1  -> 2.9.5

# newer than current but smaller than the minor version 2.3.99
poetry add module_name~2.3.1  -> 2.3.5
```


```

poetry install
```
when given a pyproject.toml file




```
poetry shell
```

Enter the virutal environment

uptdate poetry
```
poetry version minor
```



```
poetry publish
```




