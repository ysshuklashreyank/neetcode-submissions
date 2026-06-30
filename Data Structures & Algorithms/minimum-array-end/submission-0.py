class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # print(bin(n), bin(x))
        res = 0
        j = 0
        for i in range(64):
            if x & (1<<i):
                res |= (1<<i)
            else:
                if (n-1) & (1<<j):
                    res |= (1<<i)
                j += 1
        return res


