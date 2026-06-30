class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        if ROWS == 1:
            return [[0,c] for c in range(COLS)]
        if COLS == 1:
            return [[r,0] for r in range(ROWS)]

        flag = [[1]*COLS for _ in range(ROWS)]
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()
        for r in range(ROWS):
            q.append((r,0))
            flag[r][0] = 2
        for c in range(COLS):
            q.append((0,c))
            flag[0][c] = 2
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for x, y in directions:
                    row, col = r+x, c+y
                    if (row in range(ROWS) and col in range(COLS)
                        and flag[row][col] != 2
                        and heights[row][col] >= heights[r][c]
                         ):
                         q.append((row,col))
                         flag[row][col] = 2

        q = deque()
        for r in range(ROWS):
            q.append((r,COLS-1))
            flag[r][COLS-1] *= 3
        for c in range(COLS):
            q.append((ROWS-1,c))
            flag[ROWS-1][c] *= 3
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for x, y in directions:
                    row, col = r+x, c+y
                    if (row in range(ROWS) and col in range(COLS)
                        and flag[row][col] % 3 != 0 # not 3 or 6
                        and heights[row][col] >= heights[r][c]
                         ):
                         q.append((row,col))
                         flag[row][col] *= 3

        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if flag[r][c] % 6 == 0:
                    ans.append([r,c])
        print(flag)

        return ans

        