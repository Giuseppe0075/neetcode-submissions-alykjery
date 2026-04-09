class Solution:

    def encode(self, strs: List[str]) -> str:
        s = str()
        for string in strs:
            s += "#" + str(len(string)) + "#" + string
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        n = len(s)
        while i < n:
            i += 1
            number = ""
            while s[i] != '#':
                number += s[i]
                i += 1
            i += 1
            if number == "":
                continue
            number = int(number)
            ans.append(s[i:i+number])
            i += number
        return ans