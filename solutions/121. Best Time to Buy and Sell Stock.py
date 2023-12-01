class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini,profit=prices[0],0
        for i in prices:
            cost = i-mini
            profit = max(profit,cost)
            mini = min(mini,i)
        return profit
