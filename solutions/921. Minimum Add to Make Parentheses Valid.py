class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        c=0
        for i in s:
            if i=='(':
                stack.append(i)
                c+=1
            else:
                if not stack:
                    c+=1
                else:
                    stack.pop()
                    c-=1
        return c
