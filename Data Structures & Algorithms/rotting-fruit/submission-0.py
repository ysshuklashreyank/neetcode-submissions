class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten += 1
                    q.append((i,j))
        if rotten == 0 and fresh == 0:
            return 0
                    
        minutes = -1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
                        q.append((r,c))
                        grid[r][c] = 2
                        fresh -= 1
                        # print(f"deleting {r=} {c=}")
            minutes += 1
        # print(f"{fresh=}")
        if fresh != 0:
            return -1
        return minutes
        

        


        