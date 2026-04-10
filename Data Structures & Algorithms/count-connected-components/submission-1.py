class DSU:
    def __init__(self, nodes):
        self.parent = nodes
        self.rank = defaultdict()
        for node in nodes:
            self.rank[node] = 1

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(list(range(n)))
        res = n
        for u,v in edges:
            if dsu.union(u,v):
                res -= 1
        return res