# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#used the same logic as for building BST from sorted array
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        node=self.creator(nums)
        return node
    
    def creator(self,nums):
        if not nums:
            return
        maxi=max(nums)
        ix_max=nums.index(maxi)
        root=TreeNode(maxi)
        
        root.left=self.creator(nums[:ix_max])
        root.right=self.creator(nums[ix_max+1:])
        
        return root
