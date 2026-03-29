class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        perimeter=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==1:
                    for dx,dy in directions:
                        nx,ny=i+dx,j+dy
                        if nx<0 or ny<0 or nx>=rows or ny>=columns or grid[nx][ny] == 0:
                            perimeter+=1
        return perimeter