# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#   this is recursive solution
#         l=[]
#         self.helper(root,l)
#         return l
    
#     def helper(self,root,l):
#         if root:
#             self.helper(root.left,l)
#             l.append(root.val)
#             self.helper(root.right,l)
​
#   this is iterative solution
​
        stack=[]
        inorder=[]
        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
            while curr:
                stack.append(curr)
                curr = curr.left
        return inorder
