class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        # print(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        # print(self.nums)
        

    def add(self, val: int) -> int:
        # print("#", val, self.nums)
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
