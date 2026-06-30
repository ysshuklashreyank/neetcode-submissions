from bisect import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        if target not in nums:
            return [-1,-1]
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        return [left, right-1]
        