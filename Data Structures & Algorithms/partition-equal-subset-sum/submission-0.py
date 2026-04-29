class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Brute force approach:
        #For each element, it can be included or not in the partition
        #sum the elements in both partitions at the end
        targetSum = sum(nums) / 2
        if targetSum % 1 != 0:
            return False
        currSum = 0
        def dp(i):
            nonlocal currSum
            print(targetSum, currSum)
            if currSum > targetSum:
                return False
            if i == len(nums):
                return currSum == targetSum
            currSum += nums[i]
            if dp(i+1):
                return True
            currSum -= nums[i]
            return dp(i+1)
            
        return dp(0)