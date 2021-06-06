class Solution:
    def minInsertions(self, s: str) -> int:
        stack=[]
        ans=0
        i=0
        while i < len(s):
            if s[i]=='(':
                stack.append(s[i])
            elif s[i]==')':
                if i+1<len(s):
                    if s[i+1]==')':
                        if stack:
                            stack.pop()
                        else:
                            ans+=1
                        i+=1
                    else:
                        if stack:
                            stack.pop()
                            ans+=1
                        else:
                            ans+=2
                else:
                    if stack:
                        stack.pop()
                        ans+=1
                    else:
                        ans+=2
            #print(ans)
            i+=1
        if stack:
            ans+=len(stack)*2
            
        return ans
