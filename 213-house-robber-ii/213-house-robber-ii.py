class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.maxProfit(nums[1:]), self.maxProfit(nums[:-1]))
    
    def maxProfit(self, nums):
        if not nums:
            return 0
        dp = [0]*len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
                continue
            if i == 1:
                dp[i] = max(nums[i], dp[i-1])
                continue
            choice1 = dp[i-1]
            choice2 = nums[i] + dp[i-2]
            dp[i] = max(choice1, choice2)
        return dp[-1]