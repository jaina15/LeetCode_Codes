class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #stack=[]
        #for i in logs:
        #    if i=='../':
        #        #print('heya')
        #        if stack:
        #            stack.pop()
        #    elif i=='./':
        #        pass
        #    else:
        #        #print('helo')
        #        #print(i)
        #        stack.append(i)
        #return len(stack)
        
        
        #without using stack
        ans=0
        
        for i in logs:
            if i=='../':
                if ans>0:
                    ans-=1
            elif i=='./':
                pass
            else:
                ans+=1
        
        return ans
