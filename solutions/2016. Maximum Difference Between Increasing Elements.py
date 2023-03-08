class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxi=-1
        l,r=0,1
        
        while r<len(nums):
            if nums[l]<nums[r]:
                diff=nums[r]-nums[l]
                maxi=max(maxi,diff)
            else:
                l=r
            r+=1
        return maxi
