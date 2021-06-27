# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1=[]
        l2=[]
        self.helper(root1,l1)
        self.helper(root2,l2)
        return l1==l2
    
    def helper(self,root,l):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            l.append(root.val)
        
        self.helper(root.left,l)
        self.helper(root.right,l)
