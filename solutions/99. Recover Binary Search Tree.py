# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag=False
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l=[]
        self.inorder(root,l)
        sl=sorted(l)
        print(l)
        print(sl)
        for i in range(len(l)):
            if l[i]!=sl[i]:
                self.swap(root,l[i],sl[i])
                return
    
    def swap(self,root,x,y):
        if root:
            self.swap(root.left,x,y)
            if root.val==x and not self.flag:
                root.val=y
                self.flag=True
            elif root.val==y:
                root.val=x
            self.swap(root.right,x,y)
            
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
