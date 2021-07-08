# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        q=queue()
        q.append(root)
        q.append(None)
        l,a=[],[]
        while len(q)>0:
            curr=q.popleft()
            if curr is None:
                l.append(a)
                a=[]
                if len(q)==0:
                    break
                q.append(None)
            else:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                a.append(curr.val)
        #print(l)
        if len(l[-1])==1:
            return TreeNode(l[-1][0])
        node = self.lowestCommonAncestor(root,l[-1][0],l[-1][1])
        #instead of calculating lca of all nodes, just calculate lca of first and last node of last level
        #for i in range(2,len(l[-1])):
        #    node=self.lowestCommonAncestor(root,node.val,l[-1][i])
        #return node
        return self.lowestCommonAncestor(root,l[-1][0],l[-1][len(l[-1])-1])
        
    def lowestCommonAncestor(self,root,p,q):
        if root is None:
            return None
        if root.val==p or root.val==q:
            return root
        l=self.lowestCommonAncestor(root.left,p,q)
        r=self.lowestCommonAncestor(root.right,p,q)
        if l is not None and r is not None:
            return root
        if l is None and r is None:
            return None
        return l if l is not None else r
