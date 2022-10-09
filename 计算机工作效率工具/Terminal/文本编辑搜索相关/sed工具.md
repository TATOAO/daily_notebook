
# Sed
https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/
https://www.geeksforgeeks.org/sed-command-linux-set-2/

## replace subsitude

``` bash
$sed 's/unix/linux/2' geekfile.txt
$sed 's/unix/linux/' geekfile.txt
$sed 's/unix/linux/g' geekfile.txt

```


后置option:
/g 全部
/1，2 是第1次第2次出现的matching
/3g 从第三次出现的matching，包括第三次


代替的时候可以有matching group的标志位置代号

```bash
$ echo "Welcome To The Geek Stuff" | sed 's/\(\b[A-Z]\)/\(\1\)/g'
Output:
(W)elcome (T)o (T)he (G)eek (S)tuff
```

\1 就是第一个group



## delete 

``` bash
sed 'nd' filename.txt

# output 删除第n行的结果
```

n 是第几行，从第一行开始 n=1

2,5d range delete
3,$d 


```bash

sed '/pattern/d' filename.txt
```
删除matching line



