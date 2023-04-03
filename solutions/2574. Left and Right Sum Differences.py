class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        suffix = sum(nums)
        ans=[]
        prefix=0
        for x in nums:
            prefix+=x
            ans.append(abs(suffix-prefix))
            suffix-=x
        return ans
