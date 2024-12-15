
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

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)

class RecordesTreeNode(TreeNode):
    def __init__(self, val=0, left=None, right=None):
        super().__init__(val=0, left=None, right=None)
        self.left_num = 0
        self.right_num = 0
        
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = RecordesTreeNode(val = root.val)

    def insert(self, v: int) -> int:
        temp_node: RecordesTreeNode | None = self.root

        new_node = RecordesTreeNode(val=v)
        
        while temp_node:
            if v < temp_node.val:
                temp_node.left_num += 1
                if temp_node.left == None:
                    temp_node.left = new_node

                temp_node = temp_node.left

            else:
                temp_node.right_num += 1
                if temp_node.right == None:
                    temp_node.right = new_node

                temp_node = temp_node.right
            
        return 0

    def get_root(self) -> TreeNode:
        return self.root

    



# Your CBTInserter object will be instantiated and called as such:
root = TreeNode(0)
obj = CBTInserter(root)
param_1 = obj.insert(3)
param_2 = obj.get_root()
import ipdb;ipdb.set_trace()
print('xxx')



