class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #i am not satisfied.
        stack=[]
        ans=[-1]*len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                stack.append(i)
                #ans[i]=-1
            else:
                while stack and nums[i]>=nums[stack[-1]]:
                    stack.pop()
                if stack:
                    ans[i]=nums[stack[-1]]
                stack.append(i)
        #print(ans)
        #print(stack)
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i]>=nums[stack[-1]]:
                    stack.pop()
            if stack:
                ans[i]=nums[stack[-1]]
            stack.append(i)
        #print(ans)
        #print(stack)
        return ans
                
            
