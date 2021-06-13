class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        next_greater=[]
        ans=[i for i in range(len(temperatures))]
        
        for i in range(len(temperatures)):
            while next_greater and temperatures[next_greater[-1]]  < temperatures[i]:
                #print(i)
                ans[next_greater[-1]]=i-next_greater[-1]
                next_greater.pop()
            next_greater.append(i)
            #print(ans)
            #print(next_greater)
        
        while next_greater:
            ans[next_greater.pop()]=0
            
        #print(ans)
        return ans
