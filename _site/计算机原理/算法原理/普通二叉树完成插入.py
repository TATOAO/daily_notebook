
from typing import Optional

class BinaryNode():

    def __init__(self, val) -> None:
        self.val = val
        self.left:Optional[BinaryNode] = None
        self.right:Optional[BinaryNode] = None


t5 = BinaryNode(5)
t3 = BinaryNode(3)

# 大的先排前
t5.left = t3

# 现在有三种情况, X 3 Y 5 Z

# 1. X 比两个都小 -> 随便插一个位置都可
# 2. Y 在中间， 只能在5 的子节点 
# 3. Z 最大, 两个都可以： 变成 5 的父节点， 或者把3，5 都变成他的左右子节点




t1 = BinaryNode(1)


t8 = BinaryNode(8)
t9 = BinaryNode(9)
t7 = BinaryNode(7)





    
