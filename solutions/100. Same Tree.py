# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        l1=[]
        l2=[]
        pls,prs=0,0
        qls,qrs=0,0
        plsn,prsn=p,p
        qlsn,qrsn=q,q
        while plsn:
            plsn=plsn.left
            pls+=1
        while prsn:
            prsn=prsn.right
            prs+=1
        while qlsn:
            qlsn=qlsn.left
            qls+=1
        while qrsn:
            qrsn=qrsn.right
            qrs+=1
        print(pls,prs,qls,qrs)
        if pls!=qls or prs!=qrs:
            return False
        
        self.inorder(p,l1)
        self.inorder(q,l2)
        
        if l1==l2:
            return True
        return False
    
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
