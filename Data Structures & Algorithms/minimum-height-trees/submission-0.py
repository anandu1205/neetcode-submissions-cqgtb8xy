from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        graph = defaultdict(list)
        in_degree = [0] * n

        # build graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            in_degree[a] += 1
            in_degree[b] += 1

        # initial leaves
        leaves = deque()
        for i in range(n):
            if in_degree[i] == 1:
                leaves.append(i)

        remaining_nodes = n

        # 🔥 trim leaves layer by layer
        while remaining_nodes > 2:
            size = len(leaves)
            remaining_nodes -= size

            for _ in range(size):
                leaf = leaves.popleft()

                for neighbor in graph[leaf]:
                    in_degree[neighbor] -= 1

                    if in_degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)
        