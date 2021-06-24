# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        l=[]
        self.inorder(root,l)
        print(l)
        l.sort()
        f=0
        for i in range(len(l)-1):
            if l[i]!=l[i+1]:
                f=1
                break
        if f==1:
            return l[i+1]
        else:
            return -1
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
