class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i] in ('(','{','['):
                stack.append(s[i])
            elif len(stack)>0:
                if s[i]==')' and stack[-1]=='(':
                    stack.pop()
                elif s[i]==']' and stack[-1]=='[':
                    stack.pop()
                elif s[i]=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        return False if len(stack)>0 else True
