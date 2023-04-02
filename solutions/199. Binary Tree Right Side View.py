# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        l,a=[],[]
        q=queue()
        q.append(root)
        q.append(None)
        while len(q)>0:
            curr=q.popleft()
            if curr is None:
                l.append(a[-1])
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
