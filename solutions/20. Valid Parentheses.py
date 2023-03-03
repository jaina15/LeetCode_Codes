class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opening = ['[','(','{']
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                    
                elif (stack[-1]=='(' and c==')') or (stack[-1]=='{' and c=='}') or (stack[-1]=='[' and c==']'):
                    stack.pop()
                else:
                    return False
            #print(stack)
        return False if len(stack)>0 else True
                    
            
