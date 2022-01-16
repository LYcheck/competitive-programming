class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = {}
#         heap = []
        
#         for num in nums:
#             if num not in freq:
#                 freq[num] = 0
#             freq[num] += 1
        
#         for key in freq.keys():
#             val = freq[key]
#             heapq.heappush(heap, (val, key))
#             if len(heap) > k:
#                 heapq.heappop(heap)
                
#         return [ y for x, y in heap ]

        freq = {}
        buckets = {}
        res = []
        
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
            
        for num in freq.keys():
            val = freq[num]
            if val not in buckets:
                buckets[val] = []
            buckets[val] += [num]
            
        for i in range(len(nums), -1, -1):
            if len(res) >= k:
                break
            if i not in buckets:
                continue  
            res += buckets[i]
            
        return res