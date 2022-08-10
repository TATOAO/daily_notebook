
# 展开 不一样的 字段的 周围几句

https://stackoverflow.com/questions/5288875/how-can-i-expand-collapse-a-diff-sections-in-vimdiff

``` py

zr # reducing folding level 张开 read
zm # one more folding level zm minimized



]c # 跳到下一个diff

[c # 跳到上一个diff


dp             # diffput: puts changes under the cursor into the other file
               #         making them identical (thus removing the diff).
do             # diffget: (o => obtain). The change under the cursor is replaced
               #        by the content of the other file making them identical.

```