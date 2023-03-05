class Solution:
    def missingNumber(self, n: List[int]) -> int:
        return (len(n)*(len(n)+1))//2-sum(n)
