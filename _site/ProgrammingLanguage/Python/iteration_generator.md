
# for loop

``` py


listA = [1,2,3]

dictB = {1: ['a','b','c'], 2: [], 3: ['d','e']}

for a in listA:
    for b in dictB[a]:
        print(a, b)

```

很自然的如果list B是空的，相当于直接会跳过，



# Generator


[Tutorial ](https://realpython.com/introduction-to-python-generators/#:~:text=You%20can%20assign%20this%20generator,yielded%20value%20to%20the%20caller. ":)")



# itertools


### zip_longest
```python
from itertools.import zip_longest

for x in zip_longest(range(2), range(3)):
    print(x)
'''
0, 0
1, 1
None, 2
'''

```

iter
