# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l=[]
        s=''
        self.creator(root,l,s)
        return l
    
    def creator(self, root, l, s):
        if not root:
            return
        s+=str(root.val)+' '
        if not root.left and not root.right:
            l.append('->'.join(list(map(str,s.split()))))
        self.creator(root.left,l,s)
        self.creator(root.right,l,s)
