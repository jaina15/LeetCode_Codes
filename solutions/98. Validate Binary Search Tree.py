# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        l=[]
        self.inorderTraverse(root,l)
        #print(l)
        for i in range(len(l)-1):
            if l[i]>=l[i+1]:
                return False
        return True
        
    def inorderTraverse(self,root,l):
        if root:
            self.inorderTraverse(root.left,l)
            l.append(root.val)
            self.inorderTraverse(root.right,l)
