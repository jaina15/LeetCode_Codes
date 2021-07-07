# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s=0
    maxx=float('-inf')
    def goodNodes(self, root: TreeNode) -> int:
        self.maxx=root.val
        print(self.helper(root,self.s,self.maxx))
        #print(self.s)
        return self.s
    
    def helper(self,root,s,maxx):
        if root is None:
            return 0
        if root:
            if root.val>=maxx:
                #print(root.val)
                self.s+=1
                maxx=max(maxx,root.val)
            if root.left is not None and root.right is not None:
                self.helper(root.left,self.s,maxx)
                self.helper(root.right,self.s,maxx)
            elif root.left is not None and root.right is None:
                self.helper(root.left,self.s,maxx)
            elif root.left is None and root.right is not None:
                self.helper(root.right,self.s,maxx)
