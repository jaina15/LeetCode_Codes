class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        return [True if c+extraCandies>=maxi else False for c in candies]
