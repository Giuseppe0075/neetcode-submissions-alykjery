class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # dp
        # amount = 0 -> 1
        # i > len(coins) && amount != 0 -> 0
        memo = {}
        def dp(i, amount):
            if amount == 0:
                return 1
            if i >= len(coins) or amount < 0:
                return 0
            
            if (i,amount) in memo:
                return memo[(i,amount)]
                
            memo[(i,amount)] = dp(i, amount-coins[i]) + dp(i+1, amount)
            return memo[(i,amount)]
        
        return dp(0,amount)
