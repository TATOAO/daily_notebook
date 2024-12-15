

# 查看程序安装的时间

```
zgrep 'install ' /var/log/dpkg.log* | sort | cut -f1,2,4 -d' '
```


[StackExchange](https://askubuntu.com/questions/1087998/how-to-get-list-of-installed-packages-with-installation-date ":)")
