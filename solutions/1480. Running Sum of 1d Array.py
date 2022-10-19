class Solution:
    #def runningSum(self, nums: List[int]) -> List[int]:
    #    s=0,ans=[]
    #    for i in nums:
    #        s+=i
    #        ans.append(s)
    #    return ans
​
    #to do in O(1) space
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
