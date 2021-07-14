# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        l=[]
        self.inorder(root,l)
        #print(l)
        for i in range(len(l)-1,-1,-1):
            if l[i]<low or l[i]>high:
         #       print('hello')
                root=self.deleteNode(root,l[i])
         #      print(root)
               
        return root
​
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
    
    def deleteNode(self,root,key):
        if not root:
            return
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                temp=root.left
                while temp.right:
                    temp = temp.right
                root.val = temp.val
                root.left=self.deleteNode(root.left,temp.val)
        
        return root
