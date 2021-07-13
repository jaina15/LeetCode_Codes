# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                temp=root.left
                while temp.right:
                    temp = temp.right
                root.val = temp.val
                root.left=self.deleteNode(root.left,temp.val)
        
        return root
