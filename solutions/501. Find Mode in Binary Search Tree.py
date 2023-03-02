# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        self.helper(root,l)
        d=Counter(l)
        maxi=d.most_common(1)[0][1]
        return [k for k,v in d.items() if v==maxi]
            
    
    def helper(self,root,l):
        if root:
            self.helper(root.left,l)
            l.append(root.val)
            self.helper(root.right,l)
