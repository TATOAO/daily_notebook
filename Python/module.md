

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


 
# What is __init__.py
[__init__.py blog]( https://pcarleton.com/2016/09/06/python-init/#:~:text=The%20most%20minimal%20thing%20to,the%20API%20of%20the%20package.":)")


local module not found issues
[SO](https://stackoverflow.com/questions/37233140/python-module-not-found ":)")
