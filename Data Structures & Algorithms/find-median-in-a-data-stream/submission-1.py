class MedianFinder:

    # Space Complexity = O(n)
    # Time Complexity = O(1)
    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []

    # Time Complexity = O(log n)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)

        val = -heapq.heappop(self.leftHeap)
        heapq.heappush(self.rightHeap, val)

        if len(self.rightHeap) > len(self.leftHeap):
            val = -heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, val)

    # Time Complexity = O(1)
    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return -1 * self.leftHeap[0]
        return (-1 * self.leftHeap[0] + self.rightHeap[0]) / 2
        
        