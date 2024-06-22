
slice 是一个特殊的类

这里有个很好的例子

当重写list的__getitem__ 的时候

```
class A:
    def __getitem__(self, item):
        ifnone = lambda a, b: b if a is None else a
        if isinstance(item, slice):
            if item.stop is None:
                # do something with itertools.count()
            else:
                return list(range(ifnone(item.start, 0), item.stop, ifnone(item.step, 1)))
        else:
            return item
```
