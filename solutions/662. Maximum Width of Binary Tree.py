# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        level_old,num_old,max_width=1,1,0
        q=queue([[num_old,level_old,root]])
        
        while q:
            [num,level,node]=q.popleft()
            if level>level_old:
                level_old,num_old=level,num
                
            max_width=max(max_width,num-num_old+1)
            if node.left:
                q.append([num*2,level+1,node.left])
            if node.right:
                q.append([num*2+1,level+1,node.right])
        
        return max_width
