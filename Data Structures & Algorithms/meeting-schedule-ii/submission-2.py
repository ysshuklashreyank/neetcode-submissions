"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        arr = []
        for x in intervals:
            st = x.start
            end = x.end
            arr.append([st , 1])
            arr.append([end, -1])
        arr.sort()
        ans = 0
        maxx = 0
        for x in arr:
            ans += x[1]
            maxx = max(ans, maxx)
        return maxx
        
        