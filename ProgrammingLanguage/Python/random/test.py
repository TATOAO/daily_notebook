

import random

class obj(object):
     def __init__(self):
         self.a = range(3)
         pass
     def items(self):  # Generator
         while True:
             yield random.choice(self.a)


o = obj()


print(next(o.items()))
print(next(o.items()))
print(next(o.items()))
print(next(o.items()))
print(next(o.items()))
print(next(o.items()))
