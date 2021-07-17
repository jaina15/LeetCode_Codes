# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        l=[]
        self.inorder(root,l)
        l.append(val)
        
        node=self.creator(l)
        return node
    
    def creator(self,l):
        if not l:
            return
        maxi=max(l)
        ix_max=l.index(maxi)
        root=TreeNode(maxi)
        
        root.left=self.creator(l[:ix_max])
        root.right=self.creator(l[ix_max+1:])
        
        return root
        
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
