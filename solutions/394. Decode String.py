class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=']':
                stack.append(i)
            else:
                #print(stack)
                s1=''
                while stack[-1]!='[':
                    if len(stack[-1])>1:
                        s2=''
                        s2=stack.pop()
                        s2=s2[::-1]
                        s1+=s2
                    else:    
                        s1+=stack.pop()
                stack.pop()
                j=''
                while stack and stack[-1].isdigit():
                    j+=stack.pop()
                j=j[::-1]
                #print(j)
                j=int(j)
                #print(s1)
                #print(stack)
                s1=s1[::-1]
                #print(s1)
                #print(stack)
                stack.append(s1*j)
        
        #print(stack)
        #print(s1)
        return ''.join(stack)
