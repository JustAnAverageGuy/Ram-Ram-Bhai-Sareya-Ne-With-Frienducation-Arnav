# @leet start

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2: return 0


        n = len(prices)

        bought = -prices[0]
        sold = 0

        for i in range(1,n): bought, sold =  max(bought, sold - prices[i]), max(sold, bought + prices[i]-fee)

        return sold

        
# @leet end
