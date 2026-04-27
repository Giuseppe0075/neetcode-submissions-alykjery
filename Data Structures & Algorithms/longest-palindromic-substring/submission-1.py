class Solution:
    def longestPalindrome(self, s: str) -> str:

        def is_palindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        mem = {}
        def dp(s):
            if not s:
                return ""
            if s in mem:
                return mem[s]
            
            if is_palindrome(s):
                mem[s] = s
                return mem[s]
            
            s1 = dp(s[1:])
            s2 = dp(s[:-1])

            if len(s1) > len(s2):
                mem[s] = s1
            else:
                mem[s] = s2
            return mem[s]
        
        return dp(s)
        