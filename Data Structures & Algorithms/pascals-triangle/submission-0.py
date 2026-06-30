class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            curr = [1]
            print(i)
            for j in range(1, i):
                print(i,j)
                curr.append(res[-1][j]+ res[-1][j-1])
            curr.append(1)
            res.append(curr)
            print(res)
        return res
        