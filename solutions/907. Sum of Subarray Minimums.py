class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        mod=1000000007
        stack=[]
        left=[]
        right=[]
        for i in range(len(a)):
            c=1
            if i==0:
                stack.append([a[i],c])
            else:
                while stack and a[i]<stack[-1][0]:
                    c+=stack[-1][1]
                    stack.pop()
                stack.append([a[i],c])
            left.append(c)
            
        stack.clear()
        for i in range(len(a)-1,-1,-1):
            c=1
            if i==len(a)-1:
                stack.append([a[i],c])
            else:
                while stack and a[i]<=stack[-1][0]:
                    c+=stack[-1][1]
                    stack.pop()
                stack.append([a[i],c])
            right.append(c)
        right=right[::-1]
        #print(left)
        #print(right)
        s=0
        for i in range(len(a)):
            s=((s%mod)+(a[i]*left[i]*right[i])%mod)%mod
        
        return s
