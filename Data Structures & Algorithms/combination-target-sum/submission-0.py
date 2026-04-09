class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def comb(i, cur, total):
            if total > target:
                return
            if total == target:
                res.append(cur.copy())
                return
            for j in range(i, len(nums)):
                cur.append(nums[j])
                comb(j, cur, total + nums[j])
                cur.pop()
        comb(0, [], 0)
        return res
            