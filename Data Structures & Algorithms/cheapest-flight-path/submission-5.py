import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(
        self, 
        n: int, 
        flights: List[List[int]], 
        src: int, 
        dst: int, 
        k: int
    ) -> int:
        
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        # (cost, node, stops)
        pq = [(0, src, 0)]
        
        # (node, stops) -> min cost
        best = {}
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            if (node, stops) in best and best[(node, stops)] <= cost:
                continue
            
            best[(node, stops)] = cost
            
            for nei, price in graph[node]:
                heapq.heappush(pq, (cost + price, nei, stops + 1))
        
        return -1




        