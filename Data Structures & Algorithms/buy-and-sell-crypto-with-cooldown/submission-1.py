class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, sell):
            if i >= len(prices):
                return 0
            
            if (i,sell) in memo:
                return memo[(i,sell)]
            
            cooldown = dp(i+1, sell)
            if sell:
                sell = dp(i+2, not sell) + prices[i]
                memo[(i,sell)] = max(sell, cooldown)
            else:
                buy = dp(i+1, not sell) - prices[i]
                memo[(i,sell)] = max(buy, cooldown)
            return memo[(i,sell)]
        
        return dp(0, False)