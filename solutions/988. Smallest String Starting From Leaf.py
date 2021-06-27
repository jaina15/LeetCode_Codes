# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        l=[]
        s=''
        t=0
        self.creator(root,l,s)
        l.sort()
        return l[0]
    
    def creator(self,root,l,s):
        if root is None:
            return
        s+=chr(97+root.val)
        #print(s)
        if root.left is None and root.right is None:
            l.append(s[::-1])
            
        self.creator(root.left,l,s)
        self.creator(root.right,l,s)
