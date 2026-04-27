class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        def dp(amount):
            # No more cash to change
            if amount == 0:
                return 0

            #Already calculated
            if amount in mem:
                return mem[amount]

            ans = float("inf")
            for coin in coins:
                # value of the coin bigger than the current amount
                if amount - coin >= 0:
                    ans = min(dp(amount - coin)+1, ans)
            
            # If it is possible to change this amount
            mem[amount] = ans
            return ans
        minCoins = dp(amount)
        return -1 if minCoins >= float("inf") else minCoins
                
