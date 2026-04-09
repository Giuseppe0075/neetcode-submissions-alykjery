class Solution:
    def findMin(self, nums: List[int]) -> int:
        def solve(l,r):
            if l == r:
                return nums[l]
            m = int((l+r)/2)
            if nums[m] > nums[r]:
                return solve(m+1,r)
            return solve(l, r-1)
        return solve(0, len(nums)-1)
        #[3,4,5,6,1,2]
        #l=0, r=5, v=5
        #l=3, r=5, v=1
        #l=3, r=4, v=6
        #l=4, r=4, v=1
