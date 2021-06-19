# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return
        q=queue()
        q.append([root,None,None])
        q.append(None)
        l,a=[],[]
        s=0
        while len(q)>0:
            curr=q.popleft()
            if curr is None:
                l.append(a)
                a=[]
                if len(q)==0:
                    break
                q.append(None)
            else:
                if curr[0].left:
                    q.append([curr[0].left,curr[0].val,curr[1]])
                if curr[0].right:
                    q.append([curr[0].right,curr[0].val,curr[1]])
                a.append([curr[0].val,curr[2]])
                if curr[2] is not None and curr[2]%2==0:
                    s+=curr[0].val
        return s
        
