class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed)))
        n = len(position)
        stack = []
        arrives = [0] * n
        for i in range(n):
            tmp = (target - position[i]) / speed[i]
            
            arrives[i] = tmp
        for i in reversed(range(n)):
            if not stack or stack[-1] < arrives[i]:
                stack.append(arrives[i])
        
        return len(stack)