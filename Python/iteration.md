
# for loop

``` py


listA = [1,2,3]

dictB = {1: ['a','b','c'], 2: [], 3: ['d','e']}

for a in listA:
    for b in dictB[a]:
        print(a, b)

```

很自然的如果list B是空的，相当于直接会