# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total=float('-inf')
    maxi=float('-inf')
    mod=1000000007
    def maxProduct(self, root: TreeNode) -> int:
        self.total=self.summer(root)
        print(self.total)
        self.maxprod(root)
        print(self.maxi)
        return self.maxi%self.mod
    
    def maxprod(self,root):
        if not root:
            return 0
        left=self.maxprod(root.left)
        right=self.maxprod(root.right)
        node=root.val+left+right
        alt_node=self.total-node
        self.maxi=max(self.maxi,node*alt_node)
        return root.val+left+right
    
    def summer(self,root):
        if not root:
            return 0
        left=self.summer(root.left)
        right=self.summer(root.right)
        return root.val+left+right
