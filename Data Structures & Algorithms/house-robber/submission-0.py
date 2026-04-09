class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def solve(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(solve(i+1), solve(i+2) + nums[i])
            return dp[i]
        return solve(0) 