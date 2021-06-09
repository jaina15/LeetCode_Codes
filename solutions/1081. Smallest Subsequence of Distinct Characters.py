class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index={}
        
        for i,c in enumerate(s):
            last_index[c]=i
        
        stack=[]
        
        for i,c in enumerate(s):
            if c not in stack:
                while stack and c<stack[-1] and i<last_index[stack[-1]]:
                    stack.pop()
                stack.append(c)
        
        return ''.join(stack)
