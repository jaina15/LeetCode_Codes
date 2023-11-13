# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive solution
#         l=[]
#         self.helper(root,l)
#         return l
​
#     def helper(self, root, l):
#         if root:
#             l.append(root.val)
#             self.helper(root.left,l)
#             self.helper(root.right,l)
            
        if not root:
            return
        stack,preorder=[],[]
        stack.append(root)
        while stack:
            curr = stack.pop()
            preorder.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return preorder
