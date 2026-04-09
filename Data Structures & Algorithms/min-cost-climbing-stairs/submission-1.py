class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        
        for i in reversed(range(len(cost)-2)):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]

        return min(dp[0], dp[1])