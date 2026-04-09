class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n == 0:
            return nums[0]
            
        dp = [-1] * n
        def solve(i, arr):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(solve(i+1, arr), solve(i+2, arr) + arr[i])

            return dp[i]
        ans1 = solve(0, nums[:n])
        dp = [-1] * n
        ans2 = solve(0, nums[1:])
        return max(ans1, ans2)