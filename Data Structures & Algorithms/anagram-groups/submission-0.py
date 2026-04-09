class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            key = str(arr)
            if key not in d:
                d[key] = []
            d[key].append(s)
        ans = []
        for value in d.values():
            ans.append(value)
        return ans