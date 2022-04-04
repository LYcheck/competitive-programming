class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        heap = []
        for row in range(m):
            cur = mat[row].count(1)
            heapq.heappush(heap, (cur, row))
        
        res = [ heapq.heappop(heap)[1] for i in range(k) ]
        return res