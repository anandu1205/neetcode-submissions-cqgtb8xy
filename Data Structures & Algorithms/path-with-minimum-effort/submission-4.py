from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # Min effort to reach each cell
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        
        heap = [(0, 0, 0)]  # (effort, row, col)
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while heap:
            effort, r, c = heapq.heappop(heap)
            
            # ✅ Stop when reaching destination
            if r == rows - 1 and c == cols - 1:
                return effort
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(
                        effort,
                        abs(heights[nr][nc] - heights[r][c])
                    )
                    
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        
        return 0

