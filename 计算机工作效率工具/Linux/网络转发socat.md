

# 转发网络

```
socat TCP-LISTEN:8888,fork TCP:localhost:8887
```
比如说，暴露0.0.0.0:8888 接收到之后，转发给 localhost:8887
