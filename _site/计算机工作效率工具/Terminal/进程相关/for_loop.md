



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


要确认；的用法，不能随便加？
``` bash
for OUTPUT in $(Linux-Or-Unix-Command-Here)
do
    command1 on $OUTPUT
    command2 on $OUTPUT
    commandN
done
```






