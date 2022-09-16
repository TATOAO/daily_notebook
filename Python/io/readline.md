# File Open

``` py
with open("myfile.txt") as fp:
    while True:
        count += 1
        line = fp.readline()

        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))
```

mode
r: read
w: override
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: read & append(not override)

# ?
t	Opens in text mode. (default)
b	Opens in binary mode. (就只是避开一些特殊的符号 比如 换行 变成了 \r\n)
