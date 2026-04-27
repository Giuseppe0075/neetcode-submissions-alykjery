class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = set()
        def dp(s):
            if s == "":
                return True
            if s in seen:
                return False
            
            for word in wordDict:
                if not s.startswith(word):
                    continue
                
                if dp(s[len(word):]):
                    return True
            seen.add(s)
            return False
        return dp(s)