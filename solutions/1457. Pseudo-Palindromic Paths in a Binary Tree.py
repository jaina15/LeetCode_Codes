# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#The second remove or add to the set restores the path to what it was in the node that originally passed down the call, so that when we backtrack to it, the path keeps its integrity at the current node.
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        s=set()
        ans=self.dfs(root,s)
        return ans
    
    def dfs(self,root,s):
        if not root:
            return 0
        if root.val in s:
            s.remove(root.val)
        else:
            s.add(root.val)
        res=0
        if not root.left and not root.right:
            if len(s)<=1:
                res=1
        else:
            res+=self.dfs(root.left,s)+self.dfs(root.right,s)
        #this part again is to backtrack
        if root.val in s:
            s.remove(root.val)
        else:
            s.add(root.val)
        
        return res
        
