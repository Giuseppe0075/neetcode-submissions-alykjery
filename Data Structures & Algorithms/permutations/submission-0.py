class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, remaining):
            print(remaining)
            if not remaining:
                res.append(path.copy())
                print("~",path)
                return
            for j in range(len(remaining)):
                path.append(remaining[j])
                temp = remaining[:j]
                temp.extend(remaining[j+1:])
                dfs(path, temp)
                path.pop()
        dfs([], nums)
        return res