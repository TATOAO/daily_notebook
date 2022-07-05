

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