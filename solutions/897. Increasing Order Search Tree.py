# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l=[]
        self.inorder(root,l)
        ans=temp=TreeNode(l[0])
        for i in range(1,len(l)):
            temp.right=TreeNode(l[i])
            temp=temp.right
        return ans
            
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
