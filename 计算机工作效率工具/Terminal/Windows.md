
## map 

mv      : move 
ls      : dir                       :/b 只放名字
rm      : Del / rmdir
wc      : find /c ":"
grep    : findstr
clear	: cls




## example
##### count how many files start with 6

dir 6* | find /c ":"

dir * /b | findstr "^2" 

dir * /b | findstr "^2"  > log.txt


## findstr


findstr "^[a-z]"
但是这个[]是有问题的，[a-A] 只有 aA。

## explore

start .
用explore 打开当前文件夹
