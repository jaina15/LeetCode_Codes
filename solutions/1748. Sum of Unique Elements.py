from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        s=0
        for k,v in cnt.items():
            if v==1:
                s+=k
        return s
