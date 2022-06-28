# Mac Terminal Command

简单的说就是Unix 的一些简单的命令


### Soft link

```sh
ln -s original_file softed_linked_path

readlink (file)
```

### Alias

相当于形成捷径
```sh
alias something_named=' 一个命令 '

```


### For loop

[SO convert an entire directory with ffmpeg](https://stackoverflow.com/questions/5784661/how-do-you-convert-an-entire-directory-with-ffmpeg)
```
for i in *.avi;
  do name=`echo "$i" | cut -d'.' -f1`
  echo "$name"
  ffmpeg -i "$i" "${name}.mov"
done
```

for loop 果然好用,相信这是一切的基础。

```
for i in *.mkv; 
  do name=`echo "$i" | cut -d'.' -f1`; 
  echo "$name";
  ffmpeg -i "$i" -vcodec copy -acodec copy "$name.mp4";
done
```
稍微改编了一下, done！
很方便的把当前文件夹的所有mkv 转成了mp4, 又快又好！


# Linux Setup


### Create a user and set passward

```sh
useradd tatoao
useradd -e 2022-10-10 tatoao # 设有效期至
passwd tatoao
```

### add user to a group / sudo group

```sh
usermod -aG sudo tatoao

groups tatoao
# list all groups tatoao in
```

-aG append add

[set up permission](https://askubuntu.com/questions/487527/give-specific-user-permission-to-write-to-a-folder-using-w-notation ":)")

```sh

```




[传不同的 变量 pipe result ](https://stackoverflow.com/questions/3437514/bash-how-to-pipe-result-from-the-which-command-to-cd/3437518 ":)")

```sh

cd < `which ranger`

cd $(which oracle)
```



### 在后台跑process

```sh
nohup jupyter notebook 

kill xxxxx(task id)
```


control + z  # suspend process
```sh

bg  # keep running in background
```

