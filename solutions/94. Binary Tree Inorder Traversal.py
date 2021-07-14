# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    #one liner    
    #    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
    
    #recursive
    #    l=[]
    #    self.recursive_call(root,l)
    #    return l
    
    #def recursive_call(self,root,l):
    #    if root:
    #        self.recursive_call(root.left,l)
    #        l.append(root.val)
    #        self.recursive_call(root.right,l)
     
    #Morris Traversal
        curr=root
        l=[]
        while curr:
            if not curr.left:
                l.append(curr.val)
                curr=curr.right
            else:
                pre=curr.left
                while pre.right:
                    pre=pre.right
                pre.right=curr
                temp=curr
                curr=curr.left
                temp.left=None    
        return l
                    
