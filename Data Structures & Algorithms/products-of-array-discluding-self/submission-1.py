class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left[0] = 1
        right[-1] = 1
        
        tot = 1
        for i in range(1, n):
            tot *= nums[i-1]
            left[i] = tot
        
        tot = 1
        for i in reversed(range(0,n-1)):
            tot *= nums[i+1]
            right[i] = tot

        ans = [0] * n
        for i in range(n):
            ans[i] = left[i] * right[i]

        return ans