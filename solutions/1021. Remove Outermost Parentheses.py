class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=''
        ans=''
        stack=[]
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
            
            res+=i
            
            if not stack:
                ans+=res[1:-1]
                res=''
        
        return ans
