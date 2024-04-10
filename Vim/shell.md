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




# redirect & 查看vim的所有key binding, mapping 快捷键


[SO](https://stackoverflow.com/questions/7642746/is-there-any-way-to-view-the-currently-mapped-keys-in-vim ":)")

```shell
:redir! > vim_keys.txt
:silent verbose map
:redir END
```

redir! 就是redirect到指定的文件
