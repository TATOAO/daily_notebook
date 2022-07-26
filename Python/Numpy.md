
# array

### 创建


##### np.concatenate
###### hstack
``` py
# by nested array

# array([list(['问候', '提供信息']), list(['被动确认']), list(['客套']), ...,
#        list(['客套']), list(['客套']), list(['再见'])], dtype=object)

np.concatenate(df['用户意图list_clean'].values)
np.hstack(df['用户意图list_clean'].values)

```



### 支持query

```py
import numpy as np
a = np.array([3.2, 3.1, 2])

a[a>=3]
# array([3.2, 3.1])
```

# random

``` py
import numpy as np
### 设置seed
np.random.seed(23)

### 没有放回抽样
np.random.choice(range(N), size = 2000, replace=False)

```