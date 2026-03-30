from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Edge count check
        if len(edges) != n - 1:
            return False

        # 2. Build graph (undirected)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        # 3. DFS
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        dfs(0)

        # 4. Check connectivity
        return len(visited) == n



            

        