# Ranger


## config 

create a config file by command
```

ranger --copy-config=all
```

into the folder ~/.config/ranger

Ranger command

F7 mkdir

### 重命名 

一共三种插入名字方式:
| 从前面  | 后缀点前一格   | 整体后面   |
|-------------- | -------------- | -------------- |
| I   | a     | A     |


cw 直接全量改名字


t 只是一个标记的功能

空格 v 选中

### 批量编辑文件名
:bulkrename




### Preview

快捷键 zp
toggle 打开preview


### delete file

dD

### view 隐藏文件 
zh
toggle 打开展示隐藏文件


## change editor 
[StackExchang](https://unix.stackexchange.com/questions/367452/how-to-change-the-default-text-editor-in-ranger ":)")

改成nvim

## use fancy markdown previewer

[github](https://github.com/CallumHoward/dotfiles/blob/master/.config/ranger/scope.sh ":)")

use glow 

## reload config

[StackExchang](https://unix.stackexchange.com/questions/107159/how-to-refresh-or-reload-rc-conf-in-ranger-file-manager ":)")


### preview scroll 
```
map <A-j> scroll_preview 1
map <A-k> scroll_preview -1

# Preview movement
# ∆ = Option + j
map ∆ scroll_preview 1
# ˚ = Option + k
map ˚ scroll_preview -1
```

### 剪切 / 移动

dd cut
pp paste



