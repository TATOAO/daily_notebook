# Speration Line

### awk

echo "iowjef owejfioooooooo wiefj fwe" | awk '{print $2}'
从1开始计数， $2 是第二个


awk -f
from file


``` bash
awk -v FS="," '{print $2}' test.txt


# 最后一列
awk -F',' '{print $NF}'

```


## 简单的计算

一列里面统计counter


```
awk -F '\t' '{sum[$1]++}END{for(i in sum) print i "\t" sum[i]}' example.txt
```

https://blog.csdn.net/tianyunzqs/article/details/76767952




## 分隔csv 成每一列一个文件

[se](https://unix.stackexchange.com/questions/635139/how-to-split-columns-of-a-csv-file-into-separate-files ":)")

```bash

$ cat tst.awk
BEGIN { FS="," }
NR==1 {
    for (i=1; i<=NF; i++) {
        out[i] = $i ".txt"
    }
    next
}
{
    for (i=1; i<=NF; i++) {
        print $i > out[i]
    }
}


$ awk -f tst.awk list.csv
```



注意如果用的 \u0001 分隔符

[Link](https://superuser.com/questions/1014694/fetch-required-column-from-a-file-with-001-delimiter ":)")

可以改成 \001
