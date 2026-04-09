class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and s[left] not in valid_chars:
                left += 1
            while right > left and s[right] not in valid_chars:
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True