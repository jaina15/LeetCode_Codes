# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l=[]
        self.helper(root,l)
        return l == sorted(l) and l == sorted(list(set(l)))
    
    def helper(self, root, l):
        if root:
            self.helper(root.left, l)
            l.append(root.val)
            self.helper(root.right, l)
