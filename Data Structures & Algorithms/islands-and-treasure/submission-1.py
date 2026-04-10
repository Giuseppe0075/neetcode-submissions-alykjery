class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    visited[i][j] = True
                    q.append((i,j,0))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q:
            i, j, distance = q.popleft()
            grid[i][j] = distance
            for dir_i, dir_j in directions:
                new_i = i + dir_i
                new_j = j + dir_j
                if new_i < 0 or new_i == n or new_j < 0 or new_j == m:
                    continue
                if visited[new_i][new_j] or grid[new_i][new_j] == -1:
                    continue
                visited[new_i][new_j] = True
                q.append((new_i, new_j, distance + 1))
        
