class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def isPalindrome(s: str):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        result = []
        current = []
        def dfs(i):
            if i == n:
                result.append(current.copy())
                return
            for j in range(i, n):
                if isPalindrome(s[i : j+1]):
                    current.append(s[i:j+1])
                    dfs(j+1)
                    current.pop()
            
            
        dfs(0)
        return result

        # s = aabac
        # result = [["a", "a", "b", "a", "c", ""]]
        # current = ["a", "a", "b", "a", "c", ""]
        # i = 4
