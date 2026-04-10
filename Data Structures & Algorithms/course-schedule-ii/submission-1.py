class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, requirement in prerequisites:
            graph[course].append(requirement)
        
        state = [0] * numCourses
        output = []
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1

            for requirement in graph[course]:
                if not dfs(requirement):
                    return False
            
            graph[course] = []
            state[course] = 2
            output.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
