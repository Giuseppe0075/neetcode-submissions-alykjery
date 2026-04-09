class Solution:
    def solve(self, nums: List[int], target: int, left, right):
        if left > right:
            return -1
        middle = int((left + right) / 2)
        if nums[middle] == target:
            return middle
        if target < nums[middle]:
            return self.solve(nums, target, left, middle-1)
        return self.solve(nums, target, middle+1, right)
            

    def search(self, nums: List[int], target: int) -> int:
        return self.solve(nums,target, 0, len(nums)-1)

# left = 6
# right = 5
# middle = 5