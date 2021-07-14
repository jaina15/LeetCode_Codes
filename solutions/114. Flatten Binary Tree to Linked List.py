# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        l=[]
        def preorder(root,l):
            if root:
                l.append(root.val)
                preorder(root.left,l)
                preorder(root.right,l)
        preorder(root,l)
        print(l)
        root.left=None
        root.right=None
        i=1
        temp=root
        while temp and i<len(l):
            temp.right=TreeNode(l[i])
            i+=1
            temp=temp.right
