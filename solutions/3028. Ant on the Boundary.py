class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans,summ=0,0
        for i in nums:
            summ+=i
            if summ==0:
                ans+=1
        return ans
