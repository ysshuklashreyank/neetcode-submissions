class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        # getting initial treasures
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        # doing multi-source BFS
        cost = 1

        while q:
            nextQ = deque()
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] != -1 and (nr,nc) not in visited:
                        grid[nr][nc] = cost
                        nextQ.append((nr,nc))
                        visited.add((nr,nc))
            
            q = nextQ
            cost += 1
            



 


        
        