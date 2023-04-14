# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        l,a=[],[]
        q=queue()
        q.append(root)
        q.append(None)
        c=0
        while len(q)>0:
            curr = q.popleft()
            if curr is None:
                if c%2!=0:
                    a=a[::-1]
                l.append(a)
                a=[]
                c+=1
                if len(q)==0:
                    break
                q.append(None)
            else:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
