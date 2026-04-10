class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        treasures = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    treasures.append((i,j))
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def update_distances(i,j, curr_distance):
            # Base cases: the cell is water, 
            # the distance in the cell is less than the current distance
            if i < 0 or i == n or j < 0 or j == m:
                return
            if (grid[i][j] <= 0 and curr_distance > 0) or grid[i][j] < curr_distance:
                return

            # set the distance to be curr_distance
            grid[i][j] = curr_distance

            # explore all directions to update
            for x,y in directions:
                update_distances(i+x,j+y, curr_distance + 1)

        for i, j in treasures:
            update_distances(i,j,0)
