class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        ans=[]
        return [k for k,v in d.items() if v>(len(nums)//3)]
