class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l,r=0,sum(nums)
        for i,num in enumerate(nums):
            r-=num
            if l==r:
                return i
            l+=num
        return -1
