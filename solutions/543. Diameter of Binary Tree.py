# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=float('-inf')
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        h=self.height(root)
        return self.ans
    
    def height(self,root):
        if root is None:
            return 0
        l=self.height(root.left)
        r=self.height(root.right)
        self.ans=max(self.ans,l+r)
        return 1+max(l,r)
