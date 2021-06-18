# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l=[]
        self.recursive_call(root,l)
        return l
    
    def recursive_call(self,root,l):
        if root:
            l.append(root.val)
            self.recursive_call(root.left,l)
            self.recursive_call(root.right,l)
