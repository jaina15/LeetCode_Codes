# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s=0
    def goodNodes(self, root: TreeNode) -> int:
        maxi=maxi=root.val
        self.counter(root,maxi)
        return self.s
        
    def counter(self,root,maxi):
        if root:
            if root.val>=maxi:
                maxi=root.val
                self.s+=1
            self.counter(root.left,maxi)
            self.counter(root.right,maxi)
