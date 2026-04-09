class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        
        def solve(i):
            if i > len(cost):
                return int("inf")
            if dp[i] != -1:
                return dp[i]
            dp[i] = min(solve(i+1),solve(i+2)) + cost[i]
            return dp[i]
            
        return min(solve(0), solve(1))