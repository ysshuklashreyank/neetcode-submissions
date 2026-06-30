class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        res = -1
        for x in c:
            if c[x] == x:
                res = max(res,x)
        return res
        