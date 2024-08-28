
## 安装python offline
[opensource article](https://opensource.com/article/20/4/install-python-linux ":)")


```
$ tar -xf Python-3.?.?.tar.xz
$ cd Python-3.*
$ ./configure // build configure 适应当前系统
$ sudo make altinstall
```



## Openssl

openssl 是安装python 的一个重要前提依赖 （涉及到网络连接）

### centos 7


cd /usr/local/src
wget https://www.openssl.org/source/openssl-1.1.1v.tar.gz
tar -xzvf openssl-1.1.1v.tar.gz
cd openssl-1.1.1v
./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl
make
make install

这两步是8️⃣一些.so依赖关系重建，也是非常关键的两部
echo "/usr/local/openssl/lib" >> /etc/ld.so.conf.d/openssl-1.1.1.conf
ldconfig 
ldconfig -v


export PATH=/usr/local/openssl/bin:$PATH


[官方下载地址](https://openssl-library.org/source/ ":)")

[博客](https://gist.github.com/Bill-tran/5e2ab062a9028bf693c934146249e68c ":)")
