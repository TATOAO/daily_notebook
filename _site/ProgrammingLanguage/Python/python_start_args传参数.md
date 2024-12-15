https://www.geeksforgeeks.org/args-kwargs-python/


# 结合用法

```py


def f(csv, chunksize=1000, **args):
    # 这样就可以把 keywoards 参数传进去
    return pd.read_csv(csv, chunksize=chunksize, **args)


```