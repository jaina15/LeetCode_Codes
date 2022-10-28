class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d=dict()
        for i,v in enumerate(nums):
            if v not in d:
                d[v]=i
            else:
                if abs(i-d[v])<=k:
                    return True
                d[v]=i
        return False
