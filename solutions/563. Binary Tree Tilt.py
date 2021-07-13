# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=0
    def findTilt(self, root: TreeNode) -> int:
        self.calculator(root)
        return self.ans
    def calculator(self,root):
        if root is None:
            return 0
        else:
            left=self.calculator(root.left)
            right=self.calculator(root.right)
            #print('root=',root.val)
            #print(root.val,' ka left ', left)
            #print(root.val,' ka right ', right)
            #print(abs(left-right))
            self.ans+=abs(left-right)
            return left+right+root.val
