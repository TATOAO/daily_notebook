
[SO](https://stackoverflow.com/questions/53150265/how-could-i-shuffle-python-infinite-generator ":)")



```py


import random

class obj(object):
     def __init__(self):
         pass
     def items(self):  # Generator
         a = list(range(10))
         while True:
             yield random.choice(a)


```
