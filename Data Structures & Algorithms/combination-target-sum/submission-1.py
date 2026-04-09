class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        backtrack = []
        results = []
        def dfs(i,t):
            if i >= n:                    
                return

            if nums[i] > t:
                dfs(i+1,t)
                return

            #Add the current number to the sum
            backtrack.append(nums[i])
            t -= nums[i]
            if t == 0:
                results.append(backtrack.copy())
                
            #Try with the same number
            dfs(i, t)
            
            #Remove the current number from the sum
            backtrack.pop()
            t += nums[i]

            #Go to the next number
            dfs(i+1, t)
        dfs(0,target)
        return results

# Backtrack [5]
# Result [[2,2,5]]
# i = 0
# t = 2
# nums[2,5,6,9]


