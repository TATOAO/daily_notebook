

# 启动远端docker引擎
编辑这个 sudo vim /etc/docker/daemon.json
```
 {
  "hosts": ["unix:///var/run/docker.sock", "tcp://0.0.0.0:9998"]
}
```
sudo systemctl edit docker.service
也会打开一个编辑页面，注意要把下面新增内容放在中间，不然无法保存
```
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd
```
然后重启docker
```
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl restart docker
```
检查 （远端）
```
$ sudo ss -tuln | grep 9998
tcp   LISTEN 0      4096                                   *:9998             *:*
```
检查 （本地）
```
docker -H tcp://<remote-ip-adress>:9998 ps
```

然后就可以使用远端的docker engine 进行build啦

