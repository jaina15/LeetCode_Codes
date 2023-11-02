from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return [k for k,v in cnt.items() if v>1]
            
