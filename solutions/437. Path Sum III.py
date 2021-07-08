# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cnt=0
    def pathSum(self, root: TreeNode, target: int) -> int:
        if root is None:
            return 0
        self.findPath(root,target,0)
        self.pathSum(root.left,target)
        self.pathSum(root.right,target)
        return self.cnt
    
    def findPath(self,root,target,curr):
        if root is None:
            return
        curr=curr+root.val
        if curr==target:
            self.cnt+=1
        self.findPath(root.left,target,curr)
        self.findPath(root.right,target,curr)
