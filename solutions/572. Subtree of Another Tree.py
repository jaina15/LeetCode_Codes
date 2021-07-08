# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subroot: TreeNode) -> bool:
        if subroot is None:
            return True
        if root is None:
            return False
        if self.sameTree(root,subroot):
            return True
        
        return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)
        
    
    def sameTree(self,root,subroot):
        if root is None and subroot is None:
            return True
        if root is None or subroot is None:
            return False
        return root.val==subroot.val and self.sameTree(root.left,subroot.left) and self.sameTree(root.right,subroot.right)
