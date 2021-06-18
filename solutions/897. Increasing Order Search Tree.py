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
        print(l)
        temp=TreeNode(l[0])
        for i in range(1,len(l)):
            self.insert(temp,l[i])
        return temp
        
    def insert(self,root,val):
        if root is None:
            root.val=val
            return
        else:
            while root.right:
                root=root.right
            root.right=TreeNode(val)
        
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
