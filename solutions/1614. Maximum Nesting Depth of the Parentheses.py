class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        c=0
        stack=[]
        for i in s:
            if i=='(':
                c+=1
            elif i==')':
                c-=1
            else:
                continue
            maxi=max(maxi,c)
            #print(maxi)
        return maxi
