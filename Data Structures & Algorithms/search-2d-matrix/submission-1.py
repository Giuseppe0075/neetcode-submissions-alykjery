class Solution:
    def search(self, row, target, l, r):
        if l > r:
            return False
        m = int((l+r)/2)
        if row[m] == target:
            return True
        if target < row[m]:
            return self.search(row, target, l, m-1)
        return self.search(row, target, m+1, r)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) - 1
        for row in matrix:
            if self.search(row, target, 0 , n):
                return True
        return False