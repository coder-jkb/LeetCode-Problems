class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for s,d,c in roads:
            graph[s][d] = graph[d][s] = c
            
        # print(graph[i])
        
        q = deque()
        q.append(1)
        # print(q)
        mini = 10000
        visited = set()
        while q:
            node = q.popleft()
            for adj, cost in graph[node].items():
                if adj not in visited:
                    visited.add(adj)
                    q.append(adj)
                mini = min(mini, cost)
            
        return mini
            