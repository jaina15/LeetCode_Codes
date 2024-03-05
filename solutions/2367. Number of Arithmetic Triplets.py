class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen=defaultdict(int)
        cnt=0
        for num in nums:
            if num-diff in seen and num-2*diff in seen:
                cnt+=1
            seen[num]+=1
        return cnt
