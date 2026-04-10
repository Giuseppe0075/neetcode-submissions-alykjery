class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        explored = set()
        def dfs(u):
            explored.add(u)
            for v in graph[u]:
                if v not in explored:
                    dfs(v)
        dfs(0)
        return len(explored) == n 