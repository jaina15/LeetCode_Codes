import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=['+','-','*','/']
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
                #print(stack)
            else:
                v2=stack.pop()
                v1=stack.pop()
                v=0
                if i=='+':
                    v=v1+v2
                elif i=='-':
                    v=v1-v2
                elif i=='/':
                    v=int(v1/v2)
                elif i=='*':
                    v=v1*v2
                #print(v)
                stack.append(v)
        return stack.pop()
            
