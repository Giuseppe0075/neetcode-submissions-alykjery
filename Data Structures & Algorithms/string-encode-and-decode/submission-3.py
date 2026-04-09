class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while(i < len(s)):
            temp = ""
            while(s[i] != '#'):
                temp += s[i]
                i += 1
            l = int(temp)
            print(s[i])
            temp = ""
            for k in range(i+1, l+i+1):
                temp += s[k]
            i += l+1
            strs.append(temp)
        
        return strs