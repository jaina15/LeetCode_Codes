class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        #ans=[]
        #pos=0
        #open_count=0
        #close_count=0
        #for i in range(len(s)):
        #    if s[i]=='(':
        #        open_count+=1
        #    if s[i]==')':
        #        open_count-=1
        #    if open_count==0:
        #        ans.append(s[pos+1:i])
        #        pos=i+1
        #        #print(pos)
        #return "".join(ans)
        
        res=''
        ans=''
        stack=[]
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                stack.pop()
            
            res+=i
            
            if not stack:
                ans+=res[1:-1]
                res=''
        return ans
