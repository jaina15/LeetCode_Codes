# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        t1,t2=[],[]
        self.helper(root1,t1)
        self.helper(root2,t2)
        return sorted(t1+t2)
    
    def helper(self,root,t):
        if root:
            self.helper(root.left,t)
            t.append(root.val)
            self.helper(root.right,t)
