# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        q=queue()
        q.append(root)
        q.append(None)
        l,a=[],[]
        while len(q)>0:
            curr=q.popleft()
            if curr is None:
                l.append(max(a))
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
        
        return l
