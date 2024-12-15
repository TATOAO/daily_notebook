# Buffer

Buffer 定义 一段固定长度的数据

## node 

https://nodejs.org/api/buffer.html#buffer

``` js

var firstBuf = Buffer.alloc(1024);
// 声明 1024 bit = 1kb 空间的Buffer （默认0)

var firstBuf = Buffer.alloc(1024, 1);
// 默认成1


const buf4 = Buffer.from([1, 2, 3]);
// <Buffer 01 02 03>
```


