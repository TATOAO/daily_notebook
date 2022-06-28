# Screen

---
title: 2021-04-10
date: 2021-04-10 14:41
---
````sh
screen 
Contral + a ,  C # 创建并跳到新窗口
Control + a， k # 关闭当前窗口
Control + a， "  #（双引号）查看开了几个窗口
Control + a， n #跳到下一个窗口
Control + a , 数字。# 也是跳到对应窗口
Control + a，两次 # 上一个窗口
Control + a， p # 上一个窗口
Control + a， ' #（单引号） 输入一个数字，跳到那个对应窗口
Control + a， a # 光标到行首
Control + a， \ # kill all windows
Control + a ， d # detach 当前对话

screen -ls # 查看有几个回话
screen -r 2514 # 输入任务 id 进入目标对话
kill 2513 # 直接 kill 整个会话
screen -d 2515 # 手动断开一个连接

screen -x 2512 # 可以连接一个已经被连接的会话， 就是两个人同时能看到对方的编辑

```



多屏之间互动
复制东西到别的窗口
```sh
control + a,  [ #复制 
hjkl # 移动光标
空格 # 开始文本复制/ 结束文本复制
control + a， ] # 粘贴
```

分屏
```sh
control + a, S # 上下分屏
control + a，｜ # 左右分屏
control + a ， tab # 在分屏中切换光标 （注意要 contral + a， c 开始会话）
control + a, X # （大写关闭某个分屏（不关闭会话）
```

```sh
watch "data >> test.txt" # 每秒把时间写入到文件最后
tail -f test.txt # 只看最后的几行
```

其他
```sh
control +a , x # 锁住输入
control + a, s # 锁住屏幕
control + a，q #解锁屏幕

control + a， ？ # 查看其他的快捷键
```



### 改zsh 为默认的shell 

```sh
chsh -s $(which zsh)
```


