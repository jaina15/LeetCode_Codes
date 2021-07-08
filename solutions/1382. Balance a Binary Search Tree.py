# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        l=[]
        self.inorder(root,l)
        ans=self.creator(l)
        return ans
    
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
    
    def creator(self,l):
        if not l:
            return None
        mid=len(l)//2
        root=TreeNode(l[mid])
        root.left=self.creator(l[:mid])
        root.right=self.creator(l[mid+1:])
        return root
