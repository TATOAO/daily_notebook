
# array

支持query

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