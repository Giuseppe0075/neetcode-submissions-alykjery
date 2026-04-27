class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1

        for num in nums:
            tmp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(curMin * num, tmp, num)
            res = max(curMax, res)
        return res

        