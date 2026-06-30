class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [[]]

        def solve(curr, i):
            for j in range(i+1,n):
                ans.append(curr + [nums[j]])
                print(curr + [nums[j]], "\n")
                solve(curr + [nums[j]], j)
        
        solve([], -1)

        return ans
            


        