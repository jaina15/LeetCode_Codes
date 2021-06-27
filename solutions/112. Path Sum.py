# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        l=[]
        s=''
        self.creator(root,l,s,targetSum)
        if len(l)>=1:
            return True
        return False
    
    def creator(self,root,l,s,targetSum):
        if root is None:
            return
        
        s+=str(root.val)+' '
        if root.left is None and root.right is None:
            print(s)
            l.append(list(map(int, s.split())))
            if sum(l[-1])!=targetSum:
                l.pop()
            
        self.creator(root.left,l,s,targetSum)
        self.creator(root.right,l,s,targetSum)
        
