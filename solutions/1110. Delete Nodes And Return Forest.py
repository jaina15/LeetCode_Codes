# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans=[]
        self.order(root,to_delete,ans)
        if root.val not in to_delete:
            ans.append(root)
        return ans
​
    def order(self,root,to_delete,ans):
        if not root:
            return None
        root.left=self.order(root.left,to_delete,ans)
        root.right=self.order(root.right,to_delete,ans)
        
        if root.val in to_delete and not root.left and not root.right:
            root=None
        elif root.val in to_delete and ((root.left and not root.left.left and not root.left.right) or (root.right and not root.right.left and not root.right.right)):
            if root.left:
                ans.append(root.left)
            if root.right:
                ans.append(root.right)
            root=None
        elif root.val in to_delete and ((root.left and (root.left.left or root.left.right)) or (root.right and (root.right.left or root.right.right))):
            if root.left:
                ans.append(root.left)
            if root.right:
                ans.append(root.right)
            root=None
            
        return root
