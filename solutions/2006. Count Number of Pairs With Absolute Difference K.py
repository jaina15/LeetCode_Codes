class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        cnt = 0
        for num in nums:
            cnt += seen[num-k]+seen[num+k]
            seen[num]+=1
        return cnt
