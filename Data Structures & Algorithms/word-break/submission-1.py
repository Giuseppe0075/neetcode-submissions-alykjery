class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        t = 0
        for word in wordDict:
            t = max(t, len(word))
        
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            
            for j in range(min(len(s), i+t)):
                if s[i: j + 1] in wordSet:
                    if dp(j + 1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dp(0)