# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root is None:
            return
        q=queue()
        q.append(root)
        q.append(None)
        l,a=[],[]
        c=0
        while len(q)>0:
            curr=q.popleft()
            if curr is None:
                if c==0:
                    if a[0]%2==0:
                        return False
                    l.append(a)
                if c%2==0:
                    if len(a)==1:
                        if a[0]%2==0:
                            return False
                    for i in range(len(a)-1):
                        if a[i]%2==0 or a[i+1]%2==0:
                            return False
                        if a[i]>=a[i+1]:
                            return False
                else:
                    if len(a)==1:
                        if a[0]%2!=0:
                            return False
                    for i in range(len(a)-1):
                        if a[i]%2!=0 or a[i+1]%2!=0:
                            return False
                        if a[i]<=a[i+1]:
                            return False
                #print(a)
                l.append(a)
                a=[]
                if len(q)==0:
                    break
                q.append(None)
                c+=1
                
            else:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                a.append(curr.val)
        return True
