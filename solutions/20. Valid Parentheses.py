class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        openers=['[','(','{']
        for i in s:
            if i in openers:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i=='}':
                    if stack[-1]!='{':
                        return False
                    stack.pop()
                if i==']':
                    if stack[-1]!='[':
                        return False
                    stack.pop()
                if i==')':
                    if stack[-1]!='(':
                        return False
                    stack.pop()
        if not stack:    
            return True
        else:
            return False
