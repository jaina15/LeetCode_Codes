class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for a in accounts:
            maxi=max(maxi,sum(a))
        return maxi
