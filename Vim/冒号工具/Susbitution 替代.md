

# Scecond Occurence 替换第二个出现的匹配结果


https://vi.stackexchange.com/questions/8621/substitute-second-occurence-on-line
```vim
:%s/\(.\{-}\zstemp\.\)\{2}//
:%s/\(.\{-}\zs\t\)\{2}//

```

