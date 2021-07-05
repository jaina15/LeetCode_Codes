# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans=[-9999999]
        h=self.height(root,ans)
        #print(ans)
        #print(h)
        return ans[0]
    
    def height(self,root,ans):
        if root is None:
            return 0
        l=self.height(root.left,ans)
        r=self.height(root.right,ans)
        ans[0]=max(ans[0],l+r)
        #print(ans)
        
        return 1+max(l,r)
