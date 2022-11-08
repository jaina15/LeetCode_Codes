class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=-1
        p=0
        for i in s:
            if i == '(':
                p+=1
            elif i == ')':
                p-=1
            maxi = max(maxi,p)
        return maxi
