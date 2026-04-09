class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = [[] for i in range(len(board))]
        for u in used:
            u.extend([False] * len(board[0]))
        
        def backtrack(i, j, n, track):
            w = "".join(c for c in track)
            if w == word:
                return True
            if n >= len(word):
                return False
            if i < 0 or i >= len(board):
                return False
            if j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[n] or used[i][j]:
                return False
            track.append(board[i][j])
            used[i][j] = True
            if backtrack(i-1, j, n+1, track) or \
                backtrack(i+1, j, n+1, track) or \
                backtrack(i, j-1, n+1, track) or \
                backtrack(i, j+1, n+1, track):
                return True
            used[i][j] = False
            track.pop()
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i,j,0,[]):
                    return True
        return False
        

