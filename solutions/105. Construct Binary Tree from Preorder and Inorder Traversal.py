# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d={}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        for i in range(len(inorder)):
            self.d[inorder[i]]=i
        return self.creator(preorder,inorder,0,len(inorder)-1)
    
    def creator(self,preorder,inorder,lb,ub):
        if lb>ub:
            return None
        node=TreeNode(preorder.pop(0))
        if lb==ub:
            return node
        #print(node)
        mid=self.d[node.val]
        node.left=self.creator(preorder,inorder,lb,mid-1)
        node.right=self.creator(preorder,inorder,mid+1,ub)
        return node
