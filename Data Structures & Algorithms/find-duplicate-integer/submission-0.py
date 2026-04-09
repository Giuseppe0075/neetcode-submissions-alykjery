class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        for v in nums:
            if v in s:
                return v
            s.add(v)

        return 0