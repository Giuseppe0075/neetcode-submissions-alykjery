class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums and target != 0:
            return 0
        if not nums and target == 0:
            return 1
        return self.findTargetSumWays(nums[1:], target - nums[0]) + self.findTargetSumWays(nums[1:], target + nums[0])
        