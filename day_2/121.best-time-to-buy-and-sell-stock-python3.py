# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2-pointer
        l = 0
        profit = 0
        for r in range(1,len(prices)):
            cur = prices[r] - prices[l]
            if cur <= 0: l = r
            profit = max(profit, cur)

        return profit
        
# @leet end
