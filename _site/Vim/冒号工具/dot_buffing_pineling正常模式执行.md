

# 在vim execute shell command and bring buffing to editor

[Youtube Vim Tips](https://www.youtube.com/watch?v=dVIP72Uwt2A&list=LL&index=14&t=372s&ab_channel=BenKadel ":)")

加一个英文句号在感叹号前面即可
: .! ls



## figlet 

very cool title generator with combining characters  


```

 _____ _     _       _               ____                       
|_   _| |__ (_)___  (_)___    __ _  |  _ \  ___ _ __ ___   ___  
  | | | '_ \| / __| | / __|  / _` | | | | |/ _ \ '_ ` _ \ / _ \ 
  | | | | | | \__ \ | \__ \ | (_| | | |_| |  __/ | | | | | (_) |
  |_| |_| |_|_|___/ |_|___/  \__,_| |____/ \___|_| |_| |_|\___/ 
                                                                

```


very fancy





### 输入

#### json pretifier


[StackExchangVim](https://vi.stackexchange.com/questions/16906/how-to-format-json-file-in-vim ":)")

.%! jq 
把整个文件作为输入，执行 jq 命令

.'<>! jq  也可以用选中模式，变成jq的输入丢进去
