class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            l = i + 1
            r = len(nums)-1
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total < target:
                    l += 1
                else:
                    r -= 1

        return res
