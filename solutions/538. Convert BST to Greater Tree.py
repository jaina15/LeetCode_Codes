# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #ye mene kia inorder bana k har node ka prefix sum nikal k node k sath map kia or baad me firse traverse kara k value badal di, but this is not efficient way
    #def convertBST(self, root: TreeNode) -> TreeNode:
    #    l=[]
    #    d={}
    #    self.inorder(root,l)
    #    #print(l)
    #    for i in range(len(l)):
    #        d[l[i]]=sum(l[i:])
    #    #print(d)
    #    self.modifier(root,d)
    #    #print(root)
    #    return root
    
    #def modifier(self,root,d):
    #    if root:
    #        self.modifier(root.left,d)
    #        #print(root.val)
    #       root.val=d[root.val]
    #        self.modifier(root.right,d)
        
    #def inorder(self,root,l):
    #    if root:
    #        self.inorder(root.left,l)
    #        l.append(root.val)
    #        self.inorder(root.right,l)
    
    #ye seekha h, kaise single traverse me karna h ise
    #using reverse inorder traversal (Right, Root, Left)
    sum_val=0
    def convertBST(self, root: TreeNode) -> TreeNode:
        node=self.modifier(root)
        return node
    
    def modifier(self,root):
        if root:
            self.modifier(root.right)
            self.sum_val+=root.val
            root.val=self.sum_val
            self.modifier(root.left)
        
        return root
