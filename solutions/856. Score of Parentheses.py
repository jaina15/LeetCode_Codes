class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        #dekha h
        ans=0
        stack=[]
        i=0
        while i < len(s):
            if s[i]=='(':
                stack.append(ans)
                ans=0
            else:
                ans+=stack.pop()+max(ans,1)
            i+=1
        return ans
        
