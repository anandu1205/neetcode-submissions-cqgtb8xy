from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original = image[sr][sc]
        
        # If the color is already the same, no need to process
        if original == color:
            return image
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        visited = set()
        
        while queue:
            row, col = queue.popleft()
            visited.add((row, col))
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                if nr < 0 or nc < 0 or nr >= m or nc >= n or (nr, nc) in visited:
                    continue
                
                if image[nr][nc] == original:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        
        return image