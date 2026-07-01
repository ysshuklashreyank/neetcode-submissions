class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        def dfs(i,j):
            visited.add((i,j))
            temp = 0
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                r = i + dr
                c = j + dc
                if 0 <= r < ROWS and 0 <= c < COLS and (r,c) not in visited and grid[r][c] == 1:
                    temp += dfs(r,c)
            return 1 + temp            


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    res = max(res, dfs(i,j))
                    print(res)

        return res
        