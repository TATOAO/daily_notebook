


## 查看编译后的二进制文件大小

``` bash
cargo size --features v2 --target thumbv7em-none-eabihf -- -A
```


## build and flash 


```bash
cargo embed --features v2 --target thumbv7em-none-eabihf --release
```


## debug

```bash
gdb target/thumbv7em-none-eabihf/release/led-roulette
```
in MacOS, 我们可以设
alias gdb="arm-none-eabi-gdb"



## Series 

### 找到 file

#### Linux
dmesg | tail | grep -i tty
echo 'Hello, world!' > /dev/ttyACM0

#### MacOS
ls /dev/cu.usbmodem*
echo 'Hello, world!' > /dev/cu.usbmodem.xxxxxx

### 用 minicom 链接 开发板

#### 配置
cat ~/.minirc.dfl
pu baudrate 115200
pu bits 8
pu parity N
pu stopbits 1
pu rtscts No
pu xonxoff No

#### 链接
minicom -D /dev/cu.usbmodem144202 -b 115200
