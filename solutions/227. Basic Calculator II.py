class Solution:
    def calculate(self, s: str) -> int:
        operator_precedence={
            '-' : 0,
            '+' : 0,
            '*' : 1,
            '/' : 1
        }
        
        operator_stack=[]
        postfix_expression=[]
        i=0
        while i < len(s):
            if s[i]==' ':
                pass
            elif s[i].isdigit():
                v=0
                while i<len(s) and s[i].isdigit():
                    v=v*10+int(s[i])
                    i+=1
                    #print('i k value andar',i)
                #print('value ',v)
                postfix_expression.append(v)
                i-=1
                #print('bahar wala',i)
            else:
                if len(operator_stack)>0 and operator_precedence[s[i]]<=operator_precedence[operator_stack[-1]]:
                    while len(operator_stack)>0 and operator_precedence[s[i]]<=operator_precedence[operator_stack[-1]]:
                        postfix_expression.append(operator_stack.pop())
                    operator_stack.append(s[i])
                else:
                    operator_stack.append(s[i])
            
            i+=1
        
        while len(operator_stack)>0:
            postfix_expression.append(operator_stack.pop())
        
        print(postfix_expression)
        
        stack=[]
        
        for i in postfix_expression:
            if i not in operator_precedence:
                stack.append(int(i))
            else:
