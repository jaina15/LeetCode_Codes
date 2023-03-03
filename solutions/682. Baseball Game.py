class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i=='+':
                stack.append(int(stack[-1])+int(stack[-2]))
            elif i=='D':
                stack.append(2*int(stack[-1]))
            elif i=='C':
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)
