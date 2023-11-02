class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for ac in accounts:
            s = sum(ac)
            ans = max(ans,s)
        return ans
