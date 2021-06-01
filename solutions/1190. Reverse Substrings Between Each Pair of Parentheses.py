class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        opener='('
        closer=')'
        
        for i in s:
            if i==opener:
                stack.append(i)
            elif i==closer:
                s1=''
                while stack[-1]!=opener:
                    s1+=stack.pop()
                #print(s1)
                stack.pop()
                j=0
                while j<len(s1):
                    stack.append(s1[j])
                    j+=1
                #print(stack)
            else:
                stack.append(i)
        return "".join(stack)
