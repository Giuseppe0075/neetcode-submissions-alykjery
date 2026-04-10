class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        graph = defaultdict(list)
        for i in range(n):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        
        curr_path = set()

        def dfs(u):
            if u in curr_path:
                return False
            curr_path.add(u)
            for v in graph[u]:
                if not dfs(v):
                    return False
            curr_path.remove(u)
            graph[u] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        