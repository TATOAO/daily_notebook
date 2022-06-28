# File Open

``` py
with open("myfile.txt") as fp:
    while True:
        count += 1
        line = fp.readline()
  
        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))
```

mode 
r: read
w: override
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: read & append (not override)

### ?
t	Opens in text mode. (default)
b	Opens in binary mode. (就只是避开一些特殊的符号 比如 换行 变成了 \r\n )



# Module import issue



-- A.py (import pandas as pd) 
-- B.py (import pandas as pd ? or import A)
-- C.py (import A import B)


# Process bar

``` py
import progressbar
from time import sleep
bar = progressbar.ProgressBar(maxval=20, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage(), ' ', progressbar.ETA()])
bar.start()
for i in xrange(20):
    bar.update(i+1)
    sleep(0.1)
bar.finish()

```

或者使用alive-progress
https://github.com/rsalmei/alive-progress




# modules

```py
import pip
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])    

```

