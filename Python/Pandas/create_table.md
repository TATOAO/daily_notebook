

# create tables by column (List)

``` py

count_dict = [[k,v] for k,v in Counter(ass_int_split).items() if v > 5]

import pandas as pd
df = pd.DataFrame(count_dict, columns=['intent','count'])


"""

[
    ['alan', 10],
    ['blan', 34],
    ...
]
"""

```


## create by nested dictionary
``` py

"""
{'id': xxx,
 'content': [
    {'s1': xxx,
     's2': yyy,
     '用户意图': xxx,
     ....
    }
    ,...
 ]
}
"""
df = pd.DataFrame([[dialog['id'], 
                    turn['[SPEAKER 1]'], 
                    turn.get('[SPEAKER 2]'), 
                    turn.get('客服意图'), 
                    turn.get('用户意图'),
                    list(turn).index('客服意图') < list(turn).index('用户意图') 
                   ] for dialog in data for turn in dialog['content']],
                  columns = ['id', 'S1', 'S2', '客服意图', '用户意图', '是客服先说']
                 )

```