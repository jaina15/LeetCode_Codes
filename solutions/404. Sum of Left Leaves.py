# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        temp=root
        temp1=root
        r=0
        l=0
        while temp is not None:
            if temp.left is not None:
                l+=1
            temp=temp.right
            r+=1
            
        while temp1 is not None:
            if temp1.right is not None:
                r+=1
            temp1=temp1.left
            l+=1
        #print(l,r)
        if l==0:
            return 0
        if root is None:
            return
        q=queue()
        q.append(root)
        q.append(None)
        
        s=0
        while len(q)>0:
            curr=q.popleft()
            if curr is None:
                if len(q)==0:
                    break
                q.append(None)
            else:
                if curr.left:
                    if curr.left.left is None and curr.left.right is None:
                        print(curr.left.val)
                        s+=curr.left.val
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        return s
