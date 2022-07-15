
# format

``` py

# 2f 小数点后两位
"{#: 2f}"

# 井号是符号，如果是数字 0，1，2 就是format的顺序


# 固定至少5位的整数,  超过5位就直接打印全部数字
"{#: 05d}"



# instance 方法
"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first


正负号
'{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
# +3.14 ; -3.14
```



# format 2  f""
``` py
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

""" 
The value of pi is approximately 3.142.
"""
Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

"""
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
"""

```