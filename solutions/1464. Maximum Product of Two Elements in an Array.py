class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=nums[0]
        secmaxi=-1
        for i in range(1,len(nums)):
            if nums[i] > maxi:
                secmaxi = maxi
                maxi = nums[i]
            else:
                secmaxi = max(secmaxi, nums[i])
        return (maxi-1)*(secmaxi-1)
