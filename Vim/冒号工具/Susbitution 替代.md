

# Scecond Occurence 替换第二个出现的匹配结果


https://vi.stackexchange.com/questions/8621/substitute-second-occurence-on-line
```vim
:%s/\(.\{-}\zstemp\.\)\{2}//
:%s/\(.\{-}\zs\t\)\{2}//

```



# 根据位置信息 替换

[SO](https://stackoverflow.com/questions/70464175/vim-duplicate-whole-line-to-the-end-of-each-line ":)")


```vim
:%s/^\(.*\)$/\1      \1
```

