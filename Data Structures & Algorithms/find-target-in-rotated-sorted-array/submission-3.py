class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def solve(l,r):
            if l > r:
                return -1
            m = int((l+r)/2)
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    return solve(m+1,r)
                else:
                    return solve(l,m-1)                
            else:
                if target < nums[m] or target > nums[r]:
                    return solve(l,m-1)
                else:
                    return solve(m+1,r)

        return solve(0, len(nums)-1)

        #[5,1,3]
        #l=0,r=2,m=1