# 批量改名字  bulkrename

[Link](https://vim.fandom.com/wiki/Bulk_rename_files_with_Vim ":)")

```
\ls | vim -
```

ls 之后用vim打开

vim - 从 stdin里读取


前面那个\ 好像不需要也可以打开


更改

:%s/.*/mv -i '&' '&.orig'/g

& 代表已经匹配的词



