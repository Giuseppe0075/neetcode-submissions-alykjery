class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        explored = [[False for _ in range(m)] for _ in range(n)]
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def explore(x,y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == "0" or explored[x][y]:
                return
            explored[x][y] = True
            for nx, ny in directions:
                explore(x+nx, y+ny)
        
        total = 0
        for i in range(n):
            for j in range(m):
                if explored[i][j]:
                    continue
                if grid[i][j] == "0":
                    continue
                explore(i,j)
                total += 1
        return total