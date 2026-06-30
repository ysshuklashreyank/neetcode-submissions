"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        req = 0
        res = 0
        minHeap = []
        i = 0
        for i in range(len(intervals)):
            while minHeap and intervals[i].start >= minHeap[0]:
                heapq.heappop(minHeap)
                req -= 1
            req += 1
            res = max(res, req)
            heapq.heappush(minHeap, intervals[i].end)

        return res
        

            


        
        