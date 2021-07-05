# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    bal=True
    def isBalanced(self, root: TreeNode) -> bool:
        self.helper(root)
        return self.bal
    
    def helper(self,root):
        if root is None:
            return 0
        else:
            left=self.helper(root.left)
            right=self.helper(root.right)
            if abs(left-right)>1:
                self.bal=False
            return 1+max(left,right)
