class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if x > y:
                x = x-y
                heapq.heappush(stones, -x)
            elif x < y:
                y = y-x
                heapq.heappush(stones, -y)
        return -heapq.heappop(stones) if stones else 0