class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]
        m -= 1
        n -= 1
        def dp(i,j):
            if i == m or j == n:
                memo[i][j] = 1
                return 1
            if memo[i][j] != 0:
                return memo[i][j]
            memo[i][j] = dp(i+1, j) + dp(i, j+1)
            return memo[i][j]
            
        
        dp(0,0)
        return memo[0][0]