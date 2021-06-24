# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        mindis=float('inf')
        l=[]
        self.inorder(root,l)
        for i in range(len(l)-1):
            mindis=min(mindis,(l[i+1]-l[i]))
        return mindis
    
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
