"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque as queue
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        l,a=[],[]
        q=queue()
        q.append(root)
        q.append(None)
        while len(q)>0:
            curr=q.popleft()
            if curr is None:
                for i in range(len(a)-1):
                    a[i].next=a[i+1]
                a[-1].next=None
                a=[]
                if len(q)==0:
                    break
                q.append(None)
            else:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                a.append(curr)
        return root
