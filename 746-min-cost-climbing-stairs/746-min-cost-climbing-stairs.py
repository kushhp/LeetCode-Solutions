class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*(len(cost))
        
        for i in range(len(cost)):
            if i == 0:
                dp[0] = cost[0]
                continue
            if i == 1:
                dp[1] = cost[1]
                continue
            choice1 = dp[i-1] + cost[i]
            choice2 = dp[i-2] + cost[i]
            dp[i] = min(choice1, choice2)

        return min(dp[-1], dp[-2])