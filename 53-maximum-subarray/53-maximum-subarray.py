class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        maxSum = nums[0]
        currSum = nums[0]
        
        for num in nums[1:]:
            currSum = max(num, currSum+num)
            maxSum = max(currSum, maxSum)
            
        return maxSum