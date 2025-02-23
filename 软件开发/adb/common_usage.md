
# 找进程

```
adb shell "ps|grep tence"
```
system        7808   828 6693040  43816 0                   0 S com.tencent.soter.soterserver
u0_i9004      9813   828 262117000 597988 0                 0 S com.tencent.mm:xweb_sandboxed_process_0:com.tencent.xweb.pinus.sdk.process.SandboxedProcessService
u0_a298       9862   828 25125452 280816 0                  0 S com.tencent.mm:xweb_privileged_process_0
u0_a298       9892   828 370497108 539276 0                 0 S com.tencent.mm:appbrand0
u0_a298      12818   828 139856532 637936 0                 0 S com.tencent.mm
u0_a298      12925   828 9686084 171760 0                   0 S com.tencent.mm:push
u0_a298      30714   828 114579612 263208 0                 0 S com.tencent.mm:appbrand1


# 按进程抓包


adb shell logcat | grep 9813 | grep -v png
