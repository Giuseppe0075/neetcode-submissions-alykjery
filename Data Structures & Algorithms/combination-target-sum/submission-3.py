class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        result = []
        current = []
        current_sum = 0
        def dfs(i):
            nonlocal current_sum
            if i == n:
                if current_sum == target:
                    # Save the result
                    result.append(current.copy())
                return
            if current_sum > target:
                return
            
            dfs(i+1)
            current_sum += nums[i]
            current.append(nums[i])
            dfs(i)
            current_sum -= nums[i]
            current.pop()
            return

        dfs(0)
        return result

        # nums = [1,2]
        # target = 3

        # n = 2
        # i = 2
        # result = [[1,2], [1,1,1]]
        # current = [1,1,1]
        # current_sum = 3
            
