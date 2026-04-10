class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i, j):
            if i < 0 or i == n or j < 0 or j == m or board[i][j] != 'O':
                return
            
            board[i][j] = '*'
            for direction in directions:
                dfs(i+direction[0], j+direction[1])
        
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][m-1] == 'O':
                dfs(i,m-1)
        for j in range(m):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[n-1][j] == 'O':
                dfs(n-1,j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'
