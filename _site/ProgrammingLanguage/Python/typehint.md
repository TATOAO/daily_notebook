

```python


from typing import TypeVar, Iterable

T_co = TypeVar("T_co", covariant=True)
T = TypeVar("T")
T_dict = Dict[str, T_co]
T_tuple = Tuple[T_co, ...]
T_stack = TypeVar("T_stack", T_tuple, T_dict)

```


T_co = covariant type variable

```python
from typing import TypeVar, Iterable

T_co = TypeVar("T_co", covariant=True)

class Box(Iterable[T_co]):
    def __init__(self, value: T_co):
        self.value = value

int_box: Box[int] = Box(42)
obj_box: Box[object] = int_box  # Covariance allows this

```
