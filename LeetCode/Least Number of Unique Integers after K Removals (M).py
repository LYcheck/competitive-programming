class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        hv = 0
        for _ in arr:
            if _ in freq: freq[_] += 1
            else: 
                freq[_] = 1
                hv += 1
        
        buckets = [ [] for _ in range(len(arr)+1)]
        for ke, v in freq.items():
            buckets[v] += [ke]

        for i in range(len(arr)+1):
            while buckets[i] and k >= i:
                buckets[i].pop(0)
                k -= i
                hv -= 1
        return hv