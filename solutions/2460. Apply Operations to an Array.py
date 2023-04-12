class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
        ans=[]
        for i in nums:
            if i!=0:
                ans.append(i)
        ans.extend([0]*(len(nums)-len(ans)))
        return ans
