# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # l basically tracks the index of the least value we have seen till now
        profit = 0
        for r in range(1,len(prices)):
            cur = prices[r] - prices[l]
            if cur <= 0: l = r
            profit = max(profit, cur)

        return profit
        
# @leet end
