class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0]*(n+1)
        for i in range(1, n+1):
            if i % 2 != 0:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i//2]
        return dp
        