class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        next_smaller=[]
        prev_smaller=[]
        stack=[]
        
        for i in range(len(a)):
            prev_smaller.append(i)
            next_smaller.append(len(a)-i-1)
            
        for i in range(len(a)):
            while stack and a[stack[-1]] >=  a[i]:
                next_smaller[stack[-1]]=i-stack[-1]-1
                stack.pop()
            stack.append(i)
        
        stack.clear()
        for i in range(len(a)-1,-1,-1):
            while stack and a[stack[-1]] >  a[i]:
                prev_smaller[stack[-1]]=stack[-1]-1-i
                stack.pop()
            stack.append(i)
            
        s=0
        mod=1000000007
        for i in range(len(a)):
            s=((s%mod)+(a[i]*(next_smaller[i]+1)*(prev_smaller[i]+1))%mod)%mod
        
        return s
