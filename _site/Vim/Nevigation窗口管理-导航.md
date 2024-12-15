# 窗口导航-管理

## Control + 快捷键

#### Control + W  , Vim 左右上下split 屏幕
https://www.linux.com/training-tutorials/vim-tips-using-viewports/

`: vsplit  分成左右两个`
`: split   分成上下两个`

```
:sp 
:vsp
Ctrl-w   +  (hjkl)  左下上右
Ctrl-w   +  (+-=)    空间扩大缩小相等

```


https://gist.github.com/tuxfight3r/0dca25825d9f2608714b
搜 CTRL + w 之后一大堆

```bash
# TAB SHORTCUTS
CTRL+W T            -   Break out current window into a new tabview
CTRL+W o            -   Close every window in the current tabview but the current one
CTRL+W n            -   create a new window in the current tabview
CTRL+W c            -   Close current window in the current tabview



# WINDOW MANAGEMENT
CTRL+w s       -   Split current window horizontally
CTRL+w v       -   Split current window vertically
CTRL+w c       -   Close current window
CTRL+w m       -   Move to window according to motion m
CTRL+w o       -   Maxmize current window (note: this overwrites your current window configuration)



# MOVING WINDOWS
CTRL+W r       -   Swap bottom/top if split horizontally
CTRL+W R       -   Swap top/bottom if split horizontally

CTRL+w r       -   Rotates the windows from left to right - only if the windows are split vertically
CTRL+w R       -   Rotates the windows from right to left - only if the windows are split vertically

CTRL+w H       -   Move current window the far left and use the full height of the screen
CTRL+w J       -   Move current window the far bottom and use the full width of the screen
CTRL+w K       -   Move current window the far top and full width of the screen
CTRL+w L       -   Move current window the far right and full height of the screen

# NAVIGATE BETWEEN WINDOWS
CTRL+w CTRL+w  -   switch between windows
CTRL+w UP      -   Move to the top window from current window
CTRL+w DOWN    -   Move to the bottom window from current window
CTRL+w LEFT    -   Move to the left window from current window
CTRL+w RIGHT   -   Move to the right window from current window

# RESIZING WINDOWS
#Sometimes windows open up funny or are rendered incorrectly after separating from an external monitor. Or maybe you want to make more room for an important file.

CTRL+w _       -   Max out the height of the current split
CTRL+w |       -   Max out the width of the current split
CTRL+w =       -   Normalize all split sizes, which is very handy when resizing terminal

CTRL+w >       -   Incrementally increase the window to the right. Takes a parameter, e.g. CTRL-w 20 >
CTRL+w <       -   Incrementally increase the window to the left. Takes a parameter, e.g. CTRL-w 20 <
CTRL+w -       -   Incrementally decrease the window's height. Takes a parameter, e.g. CTRL-w 10 -
CTRL+w +       -   Incrementally increase the window's height. Takes a parameter, e.g. CTRL-w 10 +



```