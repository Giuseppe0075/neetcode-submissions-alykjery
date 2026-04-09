class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            tot *= num
        ans = []
        for num in nums:
            if num == 0:
                zeros -= 1
            if zeros > 0:
                if num == 0:
                    zeros += 1
                ans.append(0)
                continue
            if num == 0:
                zeros += 1
                ans.append(int(tot))
            else:
                ans.append(int(tot / num))
        return ans