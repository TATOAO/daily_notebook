


# g global 工具
只能在 vim 原生里面使用， vscode 不支持 g 工具

``` bash
#直接吧match 的行删除 command d
:g/pattern/d
#######
# Delete all lines that do not match a pattern. The commands shown are equivalent (v is "inverse").
:g!/pattern/d
:v/pattern/d




########

:g/pattern/z#.5    展示patter context五行




:g/pattern/t$       # Copy all lines matching a pattern to end of file.
:g/pattern/m$       # Move all lines matching a pattern to end of file.
qaq:g/pattern/y A   # Copy all lines matching a pattern to register 'a'.

```