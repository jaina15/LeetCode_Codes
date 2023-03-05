class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            if i>0:
                s.add(i)
        return len(s)
