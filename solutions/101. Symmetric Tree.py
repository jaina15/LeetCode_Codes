# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSame(root.left,root.right)
​
    def isSame(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.val==root2.val and self.isSame(root1.left,root2.right) and self.isSame(root1.right,root2.left)
​
"""
This was my earlier approach to solve the problem
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        l,t=[],[]
        temp1,temp2=root,root
        lefts,rights=0,0
        while temp1.left:
            temp1=temp1.left
            lefts+=1
        while temp2.right:
            temp2=temp2.right
            rights+=1
        if lefts!=rights:
            return False
        self.inorder(root.left,l)
        self.reverseinorder(root.right,t)
        print(l,t)
        if len(l)!=len(t) or l!=t:
            return False
        else:
            return True
        
    def inorder(self,root,l):
        if root:
            if root.left or root.right:
                if root.left:
                    self.inorder(root.left,l)
                else:
                    l.append(None)
                l.append(root.val)
                if root.right:
                    self.inorder(root.right,l)
                else:
                    l.append(None)
            if not root.left and not root.right:
                l.append(root.val)
            
    def reverseinorder(self,root,l):
        if root:
            if root.left or root.right:
                if root.right:
                    self.reverseinorder(root.right,l)
                else:
                    l.append(None)
                l.append(root.val)
                if root.left:
                    self.reverseinorder(root.left,l)
                else:
                    l.append(None)
            if not root.left and not root.right:
                l.append(root.val)
        
"""
