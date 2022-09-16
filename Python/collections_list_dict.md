
# Counter

``` py
from collections import Counter
# flatten the nested list
Counter([i for li in ass_intents for i in li ])
```


## flatten
https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists

``` bash
$ python -mtimeit -s't=[[1,2,3],[4,5,6], [7], [8,9]]*99' '[x for xs in t for x in xs]'
10000 loops, best of 3: 143 usec per loop
$ python -mtimeit -s't=[[1,2,3],[4,5,6], [7], [8,9]]*99' 'sum(t, [])'
1000 loops, best of 3: 969 usec per loop
$ python -mtimeit -s't=[[1,2,3],[4,5,6], [7], [8,9]]*99' 'reduce(lambda x,y: x+y,t)'
1000 loops, best of 3: 1.1 msec per loop

$ python -mtimeit -s'from itertools import chain; l=[[1,2,3],[4,5,6], [7], [8,9]]*99' 'list(chain.from_iterable(l))'
10000 loops, best of 3: 73 usec per loop

```