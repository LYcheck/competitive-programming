class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        cursum = 0
        ctr = 0
        for num in nums:
            cursum += num
            heapq.heappush(heap, -num)
            
        targsum = cursum / 2
        
        while heap and cursum > targsum:
            temp = -(heapq.heappop(heap))
            temp /= 2
            cursum -= temp
            heapq.heappush(heap, -temp)
            ctr += 1
            
        return ctr