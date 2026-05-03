class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict,deque
        if n==1:
            return [0]
        graph=defaultdict(list)
        in_degree=[0]*n
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            in_degree[a]+=1
            in_degree[b]+=1
        leaves=deque()
        for i in range(n):
            if in_degree[i]==1:
                leaves.append(i)
        remaining_nodes=n
        while remaining_nodes>2:
            remaining_nodes=remaining_nodes-len(leaves)
            for _ in range(len(leaves)):
               leaf=leaves.popleft()
               for neighbour in graph[leaf]:
                in_degree[neighbour]-=1
                if in_degree[neighbour]==1:
                    leaves.append(neighbour)
        return list(leaves)


        