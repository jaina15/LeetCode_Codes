class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum,rsum=[0],[0]
        csum=0
        for i in range(1,len(nums)):
            csum+=nums[i-1]
            lsum.append(csum)
        csum=0
        for i in range(len(nums)-1,0,-1):
            csum+=nums[i]
            rsum.append(csum)
        rsum=rsum[::-1]
        ans=[0]*len(nums)
        for i in range(len(nums)):
            ans[i]=abs(lsum[i]-rsum[i])
        return ans
