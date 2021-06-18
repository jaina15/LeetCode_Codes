# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        l=[]
        ans=dict()
        self.inorder(root,l)
        #print(l)
        if len(l)==1:
            return l
        
        for i in l:
            if i in ans:
                ans[i]+=1
            else:
                ans[i]=1
        maxx=max(ans.values())
        #print(maxx)
        l=[]
        for key,value in ans.items():
            if value==maxx:
                l.append(key)    
        #print(l)
        return l
        
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
