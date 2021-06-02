class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # bahot samjha re baba ise, tab jaake aaya. Par time complexity toh fir bhi zyada h
        stack=[]
        ans=[0]*len(temp)
        stack.append(0)
        #print(temp[stack[-1]])
        for i in range(1,len(temp)):
            c=0
            if temp[i]>temp[stack[-1]]:
                #print('temp i',temp[i])
                #print('temp stack wala',temp[stack[-1]])
                while stack and temp[i]>temp[stack[-1]]:
                    ans[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)
            else:
                stack.append(i)
            
            #print('stack status',stack)
        #print(ans)
        return ans
