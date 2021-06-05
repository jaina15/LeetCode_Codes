class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #khud s logic nhi bana, dekha h.
        s=list(s)
        #print(s)
        stack=[]
        i=0
        while i < len(s):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if stack:
                    stack.pop()
                else:
                    s[i]=''
            i+=1
        
        #print(s)
        while stack:
            s[stack.pop()]=''
        #print(s)
        
        return "".join(s)
