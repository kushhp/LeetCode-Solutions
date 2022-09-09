class Solution:
    def permute(self, nums):
        res = []
        
        def backtrack(permutation, seen):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            for j in range(len(nums)):
                if not seen[j]:
                    permutation.append(nums[j])
                    seen[j] = True
                    backtrack(permutation, seen)
                    permutation.pop()
                    seen[j] = False
                    
        backtrack([], [False]*len(nums))
        return res
                
                
            