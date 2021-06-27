# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        l=[]
        s=''
        ans=0
        self.creator(root,l,s)
        for i in l:
            n=self.binarytodecimal(i)
            ans+=n
        return ans
    
    def creator(self,root,l,s):
        if root is None:
            return
        s+=str(root.val)
        
        if root.left is None and root.right is None:
            l.append(s)
            s=''
        
        self.creator(root.left,l,s)
        self.creator(root.right,l,s)
    
    def binarytodecimal(self,s):
        p=0
        n=0
        for i in range(len(s)-1,-1,-1):
            n+=(int(s[i])*pow(2,p))
            p+=1
        return n
