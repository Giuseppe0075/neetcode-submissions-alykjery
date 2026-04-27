class Solution:
    def numDecodings(self, s: str) -> int:

        mem = dict()
        def dp(i):
            if i >= len(s):
                return 1
            
            if i in mem:
                return mem[i]
            
            if s[i] == '0':
                mem[i] = 0
                return 0
            
            mem[i] = dp(i+1)
            if i+1 < len(s):
                num = int(s[i:i+2])
                if 1 <= num <= 26:
                    mem[i] += dp(i+2)
            return mem[i]
        return dp(0)

