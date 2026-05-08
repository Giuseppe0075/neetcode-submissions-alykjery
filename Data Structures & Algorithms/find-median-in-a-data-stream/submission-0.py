class MedianFinder:

    # Space Complexity = O(n)
    # Time Complexity = O(1)
    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []

    # Time Complexity = O(log n)
    def addNum(self, num: int) -> None:
        if self.rightHeap and num > self.rightHeap[0]:
            heapq.heappush(self.rightHeap, num)
        else:
            heapq.heappush(self.leftHeap, num * -1)

        if len(self.leftHeap) > len(self.rightHeap) + 1:
            val = -1 * heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, val)
        if len(self.rightHeap) > len(self.leftHeap) + 1:
            val = -1 * heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, val)

    # Time Complexity = O(1)
    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return -1 * self.leftHeap[0]
        if len(self.rightHeap) > len(self.leftHeap):
            return self.rightHeap[0]
        return (-1 * self.leftHeap[0] + self.rightHeap[0]) / 2
        
        