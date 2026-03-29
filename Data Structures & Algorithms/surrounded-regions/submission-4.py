from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'
            
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(r + dr, c + dc)
        
        # Mark border-connected 'O'
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        
        # Flip and restore
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

        