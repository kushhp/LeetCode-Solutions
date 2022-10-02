class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(n, -1, -1):
            if i == n:
                dp[i] = 1
                continue
            if i+1 <= n:
                dp[i] += dp[i+1]
            if i+2 <= n:
                dp[i] += dp[i+2]
        return dp[0]