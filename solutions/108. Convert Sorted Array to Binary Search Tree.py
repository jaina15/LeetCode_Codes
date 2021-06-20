# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        node=self.creator(nums)
        return node
    def creator(self,a):
        if not a:
            return
        mid=len(a)//2
        
        root=TreeNode(a[mid])
        
        root.left=self.creator(a[:mid])
        root.right=self.creator(a[mid+1:])
        return root
