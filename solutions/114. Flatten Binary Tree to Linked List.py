# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l=[]
        self.preorder(root,l)
        for i in range(len(l)-1):
            l[i].left=None
            l[i].right=l[i+1]
        
    def preorder(self,root,l):
        if root:
            l.append(root)
            self.preorder(root.left,l)
            self.preorder(root.right,l)
