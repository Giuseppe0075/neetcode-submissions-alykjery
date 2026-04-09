class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        explored = [[False for _ in range(m)] for _ in range(n)]

        def dp(i, j):
            if i < 0 or i == n or j < 0 or j == m or grid[i][j] == 0 or explored[i][j]:
                return 0
            
            explored[i][j] = True
            area = 1
            for x,y in directions:
                area += dp(i+x, j+y)
            return area

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                area = dp(i,j)
                ans = max(ans, area)
        return ans

        #dp: 0,1,0,0,0
        #    0,0,0,0,0
        #    0,0,0,0,0
        #    0,0,0,0,0

