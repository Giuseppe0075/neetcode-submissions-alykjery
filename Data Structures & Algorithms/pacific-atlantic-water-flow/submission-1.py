class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        #initialize every element on the border to its ocean
        atlantic = set()
        pacific = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i: int ,j: int ,s: set, prev_height: int) -> None:
            if i < 0 or i == n or j < 0 or j == m:
                return
            if (i,j) in s:
                return
            if heights[i][j] < prev_height:
                return
            
            s.add((i,j))
            for direction in directions:
                dfs(i + direction[0], j + direction[1], s, heights[i][j])
            return

        #for each element of the atlantic border we recursevely look for all its neighbors that are heigher than it and are not in the set(dfs)
        for i in range(n):
            dfs(i, 0, pacific, heights[i][0])
        for j in range(m):
            dfs(0,j, pacific, heights[0][j])
        for i in range(n):
            dfs(i, m-1, atlantic, heights[i][m-1])
        for j in range(m):
            dfs(n-1, j, atlantic, heights[n-1][j])
        # Do the same for the other ocean

        # we return a list of the elements that are in both sets
        return list(atlantic & pacific)