class Solution:
    def removeKdigits(self, a: str, k: int) -> str:
        stack=[]
        c=0
        if len(a)==1 and k==1:
            return '0'
        for i in range(len(a)):
            while stack and stack[-1]>a[i] and c<k:
                stack.pop()
                c+=1
            stack.append(a[i])
           # print(stack)
        if c==k:
            return str(int(''.join(stack)))
        else:
            while c<k and stack:
                stack.pop()
                c+=1
            if stack:
                return str(int(''.join(stack)))
            else:
                return '0'
