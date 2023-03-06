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
        q=queue()
        q.append(root)
        q.append(None)
        l,a=[],[]
        j=0
        while len(q)>0:
            curr = q.popleft()
            if curr is None:
                if j%2==0:
                    l.append(a)
                else:
                    l.append(a[::-1])
                j+=1
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
