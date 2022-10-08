

# skill a few lines

``` bash
$ tail -n +<N+1> <filename>
< filename, excluding first N lines. >
```

所以如果是 只去掉第一行

```
cat test.txt | tail -n +2 
tail -n +2 test.txt
```