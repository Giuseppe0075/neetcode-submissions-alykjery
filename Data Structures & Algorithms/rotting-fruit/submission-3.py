class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        good_fruit = set()
        q = deque()

        #initialize a queue with all the rotten fruit positions
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    good_fruit.add((i,j))
                elif grid[i][j] == 2:
                    q.append((i,j))

        #initialize a counter of the minutes
        minutes = 0
        #while there are values in the queue
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            neighbors = []
            while q:
                i, j = q.popleft()
                for direction in directions:
                    new_pos = (i + direction[0], j + direction[1])
                    if new_pos not in good_fruit:
                        continue
                    good_fruit.remove(new_pos)
                    neighbors.append(new_pos)
            q.extend(neighbors)
            if neighbors:
                minutes += 1
        
        return minutes if not good_fruit else -1

        """
        [1,1,0]
        [0,1,1]
        [0,1,2]

        good_fruit = {(0,0),(0,1),(1,1),(2,1)}
        q = []
        new_pos = (1,2)
        (i,j) = (2,2)
        minutes = 0
        neighbors = [(1,2)]
        """


        #create a temp list for rotten fruit neighbors
        #for eache element of the queue, add its neighbors to the temp list
        #put the temp list in the queue and increase the counter

        #we can put each fruit in a set, if the fruit is in the set, there is still some good fruit