class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # X, X, X, Y, Y n = 2

        # frequency = {'X': 3, 'Y': 2}
        # heap = [5,4,1]
        
        # heap.pop() -> 5,
        # cycle_time = 1
        # queue = [(4,1+n)]

        frequency = defaultdict(int)
        for task in tasks:
            frequency[task] += 1
        
        heap = [-count for count in frequency.values()]
        heapq.heapify(heap)

        cycle = 0
        queue = deque()
        while heap or queue:
            cycle += 1

            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    queue.append([count, cycle + n])

            while queue and queue[0][1] <= cycle:
                heapq.heappush(heap, queue.popleft()[0])
        return cycle
