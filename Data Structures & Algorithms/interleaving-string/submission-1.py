class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dp(i,j):
            if i > len(s1) or j > len(s2):
                return False
            if i + j == len(s3):
                return True
            
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = False
            if i < len(s1) and s1[i] == s3[i+j]:
                memo[(i,j)] = dp(i+1,j)
                if memo[(i,j)]:
                    return True
            
            if j < len(s2) and s2[j] == s3[i+j]:
                memo[(i,j)] = dp(i, j+1)
            return memo[(i,j)]
        return dp(0,0)

        # s1 = aba
        # s2 = 
        # s3 = aba
        # memo = {(0,0) = False, (1,0) = False}

        # i = 1, j = 0
        
