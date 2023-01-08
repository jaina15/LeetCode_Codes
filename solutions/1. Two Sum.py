class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        for i,v in enumerate(nums):
            if target-v in d:
                return [d[target-v],i]
            else:
                d[v]=i
