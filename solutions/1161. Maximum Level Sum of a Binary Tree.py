# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
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
        
        for i in range(len(l)):
            l[i]=sum(l[i])
        #print(l)
        maxx=float('-inf')
        level=0
        for i in range(len(l)):
            if l[i]>maxx:
                maxx=l[i]
                level=i+1
        print(level)
        return level
