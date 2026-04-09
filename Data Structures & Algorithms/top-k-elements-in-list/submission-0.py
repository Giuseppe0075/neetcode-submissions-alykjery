class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        l = [[] for _ in range(len(nums) + 1)]
        for key, value in d.items():
            l[value].append(key)
        ans = []
        
        for i in reversed(range(len(nums) + 1)):
            if len(l[i]) == 0: continue
            ans.extend(l[i])
            k -= len(l[i])
            if k <= 0:
                return ans
        return []