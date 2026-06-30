class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            i = 0
            j = 0
            k = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            while i < len(left):
                res.append(left[i])
                i += 1
            while j < len(right):
                res.append(right[j])
                j += 1
            return res


        def mergeSort(nums, start, end):
            if start == end:
                return [nums[start]]
            mid = (start+end)//2
            left = mergeSort(nums, start, mid)
            right = mergeSort(nums, mid+1, end)
            return merge(left, right)

        return mergeSort(nums, 0, len(nums)-1)




            
        