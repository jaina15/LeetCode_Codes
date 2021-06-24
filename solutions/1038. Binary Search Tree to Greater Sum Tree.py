# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_val=0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        node=self.modifier(root)
        return node
    
    def modifier(self,root):
        if root:
            self.modifier(root.right)
            self.sum_val+=root.val
            root.val=self.sum_val
            self.modifier(root.left)
        
        return root
