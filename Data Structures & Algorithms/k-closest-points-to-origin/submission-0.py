class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x,y in points[:k]:
            heapq.heappush(h, [-1*(x*x+y*y), x, y])

        for i in range(k, len(points)):
            x,y = points[i][0], points[i][1]
            heapq.heappushpop(h, [-1*(x*x + y*y), x, y])
        res = []
        for a,b,c in h:
            res.append([b,c])
        return res
        
        