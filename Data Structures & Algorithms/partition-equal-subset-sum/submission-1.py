class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Brute force approach:
        #For each element, it can be included or not in the partition
        #sum the elements in both partitions at the end
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        targetSum = totalSum // 2
        
        n = len(nums)
        memo = [[-1] * (targetSum + 1) for _ in range(n+1)]
        def dp(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            
            memo[i][target] = dp(i+1, target) or dp(i+1, target - nums[i])
            return memo[i][target]
            
        return dp(0, targetSum)