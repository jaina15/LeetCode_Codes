class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        ans=0
        
        for i in ops:
            if i=='C':
                stack.pop()
            elif i=='D':
                stack.append(int(stack[-1])*2)
            elif i=='+':
                stack.append(int(stack[-1])+int(stack[-2]))
            else:
                stack.append(i)
       # print(stack)
        for i in stack:
            ans+=int(i)
        return ans
