# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, pre: List[int]) -> TreeNode:
        #this method is using stacks. I can also create BST from preorder by simply using insert
        s=[]
        root=TreeNode(pre[0])
        s.append(root)
        i=1
        while i<len(pre):
            temp=None
            while s and pre[i]>s[-1].val:
                temp=s.pop()
            
            if temp:
                temp.right=TreeNode(pre[i])
                s.append(temp.right)
            else:
                temp=s[-1]
                temp.left=TreeNode(pre[i])
                s.append(temp.left)
            i+=1
        
        return root
