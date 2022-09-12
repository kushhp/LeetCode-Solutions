class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = {} 
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        heap = []
        for num in frequency:
            value = frequency[num]
            heapq.heappush(heap, (value, -1*num))
        
        res = []
        while heap:
            pair = heapq.heappop(heap)
            freq = pair[0]
            num = pair[1]*-1
            for i in range(freq):
                res.append(num)
        return res