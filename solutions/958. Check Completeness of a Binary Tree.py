# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#in this we are trying to find the node in the tree which will make it incomplete(left child is none and right chile is not none), if we found this we return False, else we are returning True
from collections import deque as queue
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        have_null =False
        
        q=queue()
        q.append(root)
        while len(q)>0:
            curr=q.popleft()
            if not curr:
                have_null =True
                continue
            if have_null :
                return False
            q.append(curr.left)
            q.append(curr.right)
        
        return True
