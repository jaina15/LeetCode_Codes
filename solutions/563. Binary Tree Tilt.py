# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.ans
    
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.ans+=abs(left-right)
        return left+right+root.val
