class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        ans = []
        for c in candies:
            if c+extraCandies >= maxi:
                ans.append(True)
            else:
                ans.append(False)
        return ans
