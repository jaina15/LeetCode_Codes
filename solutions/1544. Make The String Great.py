class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            #print(ord(s[i]))
            if not stack:
                stack.append(s[i])
            else:
                if s[i]==chr(ord(stack[-1])-32) or s[i]==chr(ord(stack[-1])+32):
                    #print(s[i])
                    i+=1
                    stack.pop()
                else:
                    stack.append(s[i])
            #print(stack)
        return "".join(stack)
                
