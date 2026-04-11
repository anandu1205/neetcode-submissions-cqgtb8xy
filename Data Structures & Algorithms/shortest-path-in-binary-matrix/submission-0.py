from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If start or end is blocked
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        # 8 directions
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        
        q = deque([(0, 0, 1)])  # (row, col, distance)
        grid[0][0] = 1  # mark visited
        
        while q:
            r, c, dist = q.popleft()
            
            # reached destination
            if r == n - 1 and c == n - 1:
                return dist
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    q.append((nr, nc, dist + 1))
                    grid[nr][nc] = 1  # mark visited
        
        return -1
        