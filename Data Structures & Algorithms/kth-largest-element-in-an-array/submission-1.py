class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        elements = []
        heapq.heapify(elements)
        for num in nums:
            heapq.heappush(elements, num)
            if len(elements) > k:
                heapq.heappop(elements)

        
        return heapq.heappop(elements)
