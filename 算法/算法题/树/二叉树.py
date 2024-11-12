
# class BinaryTree():
#     def __init__(self, val, left = None, right = None):
#         self.val = val
#         self.left = None
#         self.right = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        pass


    def insert(self, v: int) -> int:
        return 0


    def get_root(self) -> TreeNode:
        return TreeNode()



# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()


