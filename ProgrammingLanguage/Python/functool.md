


# total ordering

@functools.total_ordering
给定一个声明一个或多个全比较排序方法的类，这个类装饰器实现剩余的方法。这减轻了指定所有可能的全比较操作的工作。

此类必须包含以下方法之一：__lt__() 、__le__()、__gt__() 或 __ge__()。另外，此类必须支持 __eq__() 方法。

例如：

```python

@total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
```

comparison	available	alternative
a > b	a < b	(not a < b) and (a != b)
        a <= b	(not a <= b)
        a >= b	(a >= b) and (a != b)

a <= b	a < b	(a < b) or (a == b)
        a > b	(not a > b)
        a >= b	(not a >= b) or (a == b)

a < b	a <= b	(a <= b) and (a != b)
        a > b	(not a > b) and (a != b)
        a >= b	(not a >= b)

a >= b	a < b	(not a < b)
        a <= b	(not a <= b) or (a == b)
        a > b	(a > b) or (a == b)




# cache
