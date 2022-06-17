class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d=dict()
        for i,v in enumerate(sorted(nums)):
        #    print(i,v)
            if v in d:
                pass
            else:
                d[v]=len(nums)-(len(nums)-i)
        #print(d)
        return [d[i] for i in nums]
