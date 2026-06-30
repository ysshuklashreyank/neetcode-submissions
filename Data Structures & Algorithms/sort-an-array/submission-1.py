class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(a,b):
            res = []
            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            while i < len(a):
                res.append(a[i])
                i += 1
            while j < len(b):
                res.append(b[j])
                j += 1
            return res
        
        def sort(a):
            if len(a) <= 1:
                return a
            mid = len(a)//2
            left = sort(a[:mid])
            right = sort(a[mid:])
            return merge(left, right)
        
        return sort(nums)