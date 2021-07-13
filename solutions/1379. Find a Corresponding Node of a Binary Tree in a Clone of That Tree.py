# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# dekh kar kia h
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(original: TreeNode, cloned: TreeNode):
            if original:
                inorder(original.left,cloned.left)
                if original is target:
                    self.node=cloned
                inorder(original.right,cloned.right)
        inorder(original,cloned)
        return self.node
    
