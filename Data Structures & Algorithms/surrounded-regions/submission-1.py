class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c):
            
            if r not in range(rows) or c not in range(cols):
                return 

            board[r][c] = "Y" 

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and board[nr][nc] == "O":
                    dfs(nr, nc)

        
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == "O":
                    dfs(r, c)

        for c in range(cols):
            for r in [0, rows - 1]:
                if board[r][c] == "O":
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Y":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"


