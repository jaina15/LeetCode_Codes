class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=len(nums)*(len(nums)+1)//2
        summ=0
        for i in nums:
            summ+=i
        return s-summ
