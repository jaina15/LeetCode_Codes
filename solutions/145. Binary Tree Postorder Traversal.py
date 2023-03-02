# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        self.helper(root,l)
        return l
    
    def helper(self,root,l):
        if root:
            self.helper(root.left,l)
            self.helper(root.right,l)
            l.append(root.val)
