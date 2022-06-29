
# Snip
[我用的是UltiSnip 这是github 官网](https://github.com/SirVer/ultisnips ":)")

[Git 上可以参考的snip script](https://github.com/honza/vim-snippets/blob/master/UltiSnips/all.snippets ":)")

Snip 有自动填充的功能的 Control + N 就会自动弹出来啦


## 跳动自动填充位置。Triggor

control + b 下一个
control + z 上一个 
这些都是能在vimrc里设的

## Snippet 信标机制
(这是我取得名字)

[2020-03-31]
```snippet
${1:xxxx}	# 数字代表第几号信标 xxxx代表默认初始字符
$1		# 没有默认字符的话是这样的
$1 ...  $1	# 允许同一个信标出现多次，这样意味着编辑一处会影响几处
${1:VISUAL}	# 特殊的默认字符：用visual 状态中用 tab 扣取的字段代替
```
我还不确定为什么是tab键，我看了一下：reg 里面只是简单的放进了默认的""里，可能是snip预设的吧。

[官方的tutorial](https://www.sirver.net/blog/2012/02/05/third-episode-of-ultisnips-screencast/ ":)")

## snip script option

snippet 句末

` snippet keyward "xxxx" r/b/w/empty ` 最后的b是说，只有当这个t是行首的时候才显示

[b/w/empty]

- empty 什么都不输入默认是 一个独立的单词+tab 触发 
- b 	仅句首的单词触发
- w 
- r 这是一个 regular express 的pattern  (要配合python才能使用)
2020-04-04

[原来这里有总结啦！](https://developpaper.com/vim-code-snippet-plug-in-ultisnips-usage-tutorial/ ":)")


<img src="post_asset/2020-03-30-vim_note_1.png" alt="2020-03-30-vim_note_1.png failed" width="400"/>

[正式的doc](https://github.com/SirVer/ultisnips/blob/master/doc/UltiSnips.txt ":)")



`<${1:div}> ` 
默认是\<div> 的意思，然后后面全部 $1 都会同时变化

要去掉变化，要用另外的代替符：
`</${1/(\w+).*/$1/}>`


## Snip 调用其他的窗口内容 `

vim script: 调用当前时间
`` `v strftime("%c")` `` (`` `v ``)就是用vim窗口的内容， vimL， vim script （有待挖掘）
`` `echo $USER` `` (`` ` ``)就是直接用shell的指令




## Snip + python
使用python
```bash
`!p
#python code!
`
```

```python
snip.c    # current value ?
snip.rv  #Represents the return Value,python code that was processed after the execution of the string assigned to RV
snip.fn # Represents the current file name
snip.basename # is also the current file name
snip.ft #Represents the current file type
snip.v #Represents a visual pattern variable that representssnip.v.modea pattern type that 
snip.v.text #represents a selected character in visual mode
```
[这篇文章有详解，还有关于 全局comment的snip function，待以后仔细研究](https://topic.alibabacloud.com/a/vim-snippet-plugin-ultisnips-use-tutorial_1_57_30130694.html ":)")


[来源](https://developpaper.com/vim-code-snippet-plug-in-ultisnips-usage-tutorial/ ":)")

信标也可以用 t[1] 来表示
```
snippet req "require a module"
let ${1:${VISUAL: my_name}} = require ('`!p snip.rv = t[1]`');
endsnippet
```
[来源](https://stackoverflow.com/questions/38687756/define-ultisnip-with-variable-default-placeholder ":)")


2020-04-04

这里 生成matrix， 先要获取

```python
p = r'[\[\(](\d+)x(\d+)[\]\)]'
s = '[2x3]'
re.match(p,s)
match.group(0)		-> '[2x3]'
match.group(1)		-> '2'
match.group(2)		-> '3'
match.group(3)		-> No such group
```
group(0) 就是原string的意思。








## Interactive Snip (Screenshot)! 
[2020-03-30]
耶✌️ 我成功把 mac的截图功能整合到 vim snip + markdown 里了！

```bash
snippet ss "take a screen shot and save to the 
directory(post_asset) with title of the same title of your file(snip.basename) + number(in order)"
`!p
import os
from subprocess import Popen

# get the number that 
file_name_lists = [name.replace('.png','') for name in os.listdir('post_asset') if snip.basename in name]

file_numbs_exist = [int(i.split('_')[-1]) for i in file_name_lists]
file_index = str(max(file_numbs_exist+[0]) + 1)
file_name = snip.basename + '_' + file_index + '.png'

# should be modified if change the directory name
target_path = os.path.join("post_asset",file_name)

# exec the interactive screen capture
# not be able to use subprocess.call, it would cause screencapture process not stop, 
# and keep taking multiple screencapture, and the filename index breaks, I think this is a snippet bug.
Popen(["screencapture", "-i", target_path])

# snip.rv = '![alt image path: '+ file_name +' failed](' + target_path +' "' +file_name+'")'
snip.rv = '< img src="{0}" alt="{1}" width="400"/>'.format(target_path, file_name + ' failed')
`
endsnippet
```

这样我只要 按ss [tab] 就可以直接截图到对应的文件夹里，并且在markdown里显示成img了🐮


## 下一个项目： snip + markdown 自动录屏转 gif
要下个月才能开始做了！得先搞学校的东西了！

[命令行 转gif (git)](https://gist.github.com/dergachev/4627207 ":)")


---
[有人在git做了 git相关的 snip命令，可以参考一下](https://github.com/mgedmin/dotvim/blob/master/UltiSnips/python.snippets ":)") 


