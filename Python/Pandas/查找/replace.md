# 替换


https://stackoverflow.com/questions/49413005/replace-multiple-substrings-in-a-pandas-series-with-a-value

用dict 替换值
```

dataUS['sec_type'].str.strip().replace(dict(zip(["LOCAL", "FOREIGN", "HELLO"], ["CORP"]*3)),regex=True)


```
注意 .str.strip().replace != .str.replace()