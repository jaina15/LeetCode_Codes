# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=float('-inf')
    def maxAncestorDiff(self, root: TreeNode) -> int:
        l=[]
        s=''
        self.creator(root,l,s)
        #print(l)
        #print(self.ans)
        return self.ans
            
    def creator(self,root,l,s):
        if root is None:
            return
        s+=str(root.val)+' '
        if root.left is None and root.right is None:
            l.append(list(map(int,s.split())))
            maxx=max(l[-1])-min(l[-1])
            self.ans=max(self.ans,maxx)
            l.pop()
        
        self.creator(root.left,l,s)
        self.creator(root.right,l,s)
