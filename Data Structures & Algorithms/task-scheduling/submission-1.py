class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # x,x,x,y,y ; n = 2
        # x,y,idle,x,y,idle,x

        # y,x,idle,y,x,idle,idle,x

        # frequencies = {'x': 3, 'y': 2}

        # free_tasks = [-3,-2]
        # cycle = 0

        # pop from the free_tasks, and put the element in another cooldown where 
        # the "resume time" is saved (cooldown, freq)
        # while the first element in the cooldown_queue has a cooldown value <= cycle, put that
        # element in the free_tasks queue

        # if no elements in free_tasks but in cooldown, pop the first element and
        # add it to free_tasks, make cycle value equal to cooldown

        frequences = defaultdict(int)
        for task in tasks:
            frequences[task] += 1
        
        free_tasks_queue = [-count for count in frequences.values()]
        heapq.heapify(free_tasks_queue)

        cooldown_queue = deque()
        cycle = 0
        while free_tasks_queue or cooldown_queue:
            if free_tasks_queue:
                freq = 1 + heapq.heappop(free_tasks_queue)
                cycle += 1
                if freq < 0:
                    cooldown_queue.append((cycle + n, freq))
                while cooldown_queue and cooldown_queue[0][0] <= cycle:
                    _, freq = cooldown_queue.popleft()
                    heapq.heappush(free_tasks_queue, freq)
            else:
                cooldown_cycle, freq = cooldown_queue.popleft()
                cycle = cooldown_cycle
                heapq.heappush(free_tasks_queue, freq)
        return cycle

        # tasks = [A,A,A,B,C], n = 3
        # frequences = {A: 3, B: 1, C: 1}
        # free_tasks_queue = []
        # cooldown_queue = []
        # cycle = 9

        # freq = 0
        # cooldown_cycle = 8

