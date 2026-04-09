class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkValid(arr):
            counts = [0] * 10
            for el in arr:
                if el == '.':
                    continue
                num = int(el)
                counts[num] += 1
                if counts[num] > 1:
                    return False
            return True

        #Rows check
        for i in range(9):
            if not checkValid(board[i]):
                return False
            
        #Columns check
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if not checkValid(column):
                return False

                #Boxes check
        for i in range(3):  # blocchi di righe
            for j in range(3):  # blocchi di colonne
                box = []
                for r in range(i * 3, i * 3 + 3):
                    for c in range(j * 3, j * 3 + 3):
                        box.append(board[r][c])
                if not checkValid(box):
                    return False
        return True
     
