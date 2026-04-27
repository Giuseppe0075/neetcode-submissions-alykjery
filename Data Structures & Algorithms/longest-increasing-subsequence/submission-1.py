class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        max_lenght = 1

        def binary_search(arr, target):
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = (l+r) // 2
                if arr[m] == target:
                    return m
                if arr[m] > target:
                    r = m -1
                else:
                    l = m + 1
            return l

        for num in nums[1:]:
            if num > subsequence[-1]:
                subsequence.append(num)
            else:
                idx = binary_search(subsequence, num)
                subsequence[idx] = num
            max_lenght = max(max_lenght, len(subsequence))

        return max_lenght

        # subsequence = [0,1]
        # num = 1