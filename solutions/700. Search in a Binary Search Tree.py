# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # this is recursive solution
        # if not root:
        #     return
        # if root.val == val:
        #     return root
        # elif root.val > val:
        #     return self.searchBST(root.left, val)
        # else:
        #     return self.searchBST(root.right, val)
        
        # this is iterative solution
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return
