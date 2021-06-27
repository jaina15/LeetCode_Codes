# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        l=[]
        s=''
        t=0
        self.creator(root,l,s)
        return sum(l)
    
    def creator(self,root,l,s):
        if root is None:
            return
        s+=str(root.val)
        if root.left is None and root.right is None:
            l.append(int(s))
            
        self.creator(root.left,l,s)
        self.creator(root.right,l,s)
