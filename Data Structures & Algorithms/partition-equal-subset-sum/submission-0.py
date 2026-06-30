class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = [[False]*(total//2+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True
        if nums[0] <= total//2 +1:
            dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(total//2 + 1):
                if j - nums[i] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j- nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


        