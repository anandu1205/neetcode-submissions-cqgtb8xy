class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        from collections import defaultdict
        graph=defaultdict(list)
        for source,target,time in times:
            graph[source].append((target,time))
        dist={}
        for i in range(1,n+1):
            dist[i]=float('inf')
        dist[k]=0
        heap=[(0,k)]
        while heap:
            current_dist,node=heapq.heappop(heap)
            if current_dist>dist[node]:
                continue
            for neighbour,time in graph[node]:
                new_dist=current_dist+time
                if new_dist<dist[neighbour]:
                    dist[neighbour] = new_dist  
                    heapq.heappush(heap,(new_dist,neighbour))
        max_dist = max(dist.values())
        
        return max_dist if max_dist != float('inf') else -1



        