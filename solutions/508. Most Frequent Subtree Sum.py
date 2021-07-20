# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    m={}
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.m.clear()
        if not root:
            return []
        self.summer(root)
        print(self.m)
        v=max(self.m.values())
        ans=[]
        for key,value in self.m.items():
            if value==v:
                ans.append(key)
        print(ans)
        return ans
    
    def summer(self,root):
        if not root:
            return 0
        summ=root.val+self.summer(root.left)+self.summer(root.right)
        if summ in self.m:
            self.m[summ]+=1
        else:
            self.m[summ]=1
        return summ
        
            
