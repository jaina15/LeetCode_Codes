# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        q=queue()
        q.append(root)
        q.append(None)
        maxi,level,a=-10000000,1,[]
        while len(q)>0:
            curr = q.popleft()
            if curr is None:
                if sum(a)>maxi:
                    maxi = sum(a)
                    ans = level
                a=[]
                level+=1
                if len(q)==0:
                    break
                q.append(None)
            else:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                a.append(curr.val)
        
        return ans
