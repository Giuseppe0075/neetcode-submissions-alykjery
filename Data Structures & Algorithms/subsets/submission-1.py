class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        import copy
        n = len(nums)
        subset=[]
        result = [[]]
        def dfs(i):
            if i >= n:
                return
            subset.append(nums[i])
            result.append(copy.deepcopy(subset))
            dfs(i+1)
            subset.pop()
            dfs(i+1)
            return

        dfs(0)
        return result




# [0, 1, 2, 3]
# subset: [0]
# result: [[0]]