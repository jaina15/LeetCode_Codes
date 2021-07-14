# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d={}
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        for i in range(len(inorder)):
            self.d[inorder[i]]=i
        return self.creator(postorder,inorder,0,len(inorder)-1)
    
    def creator(self,postorder,inorder,lb,ub):
        if lb>ub:
            return None
        node=TreeNode(postorder.pop())
        if lb==ub:
            return node
        print(node)
        mid=self.d[node.val]
        node.right=self.creator(postorder,inorder,mid+1,ub)
        node.left=self.creator(postorder,inorder,lb,mid-1)
        return node
