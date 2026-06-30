class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    tup = (i, j)
                    if tup not in visited:
                        # visited.add(tup)
                        count += 1
                        st = [tup]
                        while st:
                            x, y = st.pop()
                            visited.add((x, y))

                            # down
                            if x + 1 < m and grid[x+1][y] == "1" and ((x+1,y) not in visited):
                                st.append((x+1, y))
                            # up
                            if x - 1 >= 0 and grid[x-1][y] == "1" and ((x-1,y) not in visited):
                                st.append((x-1, y))
                            # right
                            if y + 1 < n and grid[x][y+1] == "1" and ((x,y+1) not in visited):
                                st.append((x, y+1))
                            # left
                            if y - 1 >=0 and grid[x][y-1] == "1" and ((x,y-1) not in visited):
                                st.append((x, y-1))
        return count





        