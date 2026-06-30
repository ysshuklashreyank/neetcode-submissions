class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()

        def dfs(row, col):
            board[row][col] = "#"
            for x,y in directions:
                r,c = row+x, col+y
                if r in range(ROWS) and c in range(COLS) and board[r][c] == "O":
                    dfs(r,c)

        for row in range(ROWS):
            if board[row][0] == "O":
                board[row][0] = "#"
                dfs(row, 0)
            if board[row][COLS-1] == "O":
                dfs(row, COLS-1)

        for col in range(COLS):
            for row in [0, ROWS-1]:
                if board[row][col] == "O":
                    dfs(row, col)



        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "#":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"

                