

# explode

一个比较重要的场景， 把 split拆成一个独立的表

```
select rename,age 
from demo as ttt
lateral view explode(split(name,',')) ttt as rename;
```
