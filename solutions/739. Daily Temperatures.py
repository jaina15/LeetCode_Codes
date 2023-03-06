class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #j=0
        stack,ans=[],[0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append([temperatures[i],i])
            else:
                while stack and temperatures[i]>stack[-1][0]:
                    j=stack[-1][1]
                    ans[j]=i-j
                    stack.pop()
                stack.append([temperatures[i],i])
        
        return ans
