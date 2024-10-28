

# date

## formatting

+%s 
用秒来表示   = timestamp 从 1970-01-01 开始

```bash
date +'%Y-%m-%d %H:%M:%s'
# 2024-10-28 14:53:1730098416
date +'%Y-%m-%d %H:%M:%S'
# 2024-10-28 14:53:38
```


## target date

date --date='2024-01-02'
返回目标的日期
date --date='2024-01-02' +%s 就可以返回固定日期的timestamp
