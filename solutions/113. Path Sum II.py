# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        l=[]
        s=''
        self.creator(root,l,s,targetSum)
        return l
    
    def creator(self,root,l,s,targetSum):
        if root is None:
            return
        
        s+=str(root.val)+' '
        #s.append(root.val)
        #print(s)
        if root.left is None and root.right is None:
            #print(s)
            l.append(list(map(int, s.split())))
            if sum(l[-1])!=targetSum:
                l.pop()
            
        self.creator(root.left,l,s,targetSum)
        self.creator(root.right,l,s,targetSum)
