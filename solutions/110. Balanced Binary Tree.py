# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.balance = True
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.balance
    
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if abs(left-right)>1:
            self.balance = False
        return max(left,right)+1
