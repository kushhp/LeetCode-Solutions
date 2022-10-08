class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0]*(len(nums))
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            if i == 1:
                dp[i] = max(nums[i], nums[i-1])
            choice1 = dp[i-1]
            choice2 = nums[i] + dp[i-2]
            dp[i] = max(choice1, choice2)
        return dp[-1]
            
        