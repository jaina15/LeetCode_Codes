# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#in this we are trying to Flase the node in the tree which will make it incomplete(left child is none and right chile is not none), if we found this we return False, else we are returning True
from collections import deque as queue
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        check=False
        
        q=queue()
        q.append(root)
        while len(q)>0:
            curr=q.popleft()
            #print(curr)
            #print('===')
            if not curr:
                check=True
                #print(curr,'heloooo')
                continue
            if check:
                return False
            q.append(curr.left)
