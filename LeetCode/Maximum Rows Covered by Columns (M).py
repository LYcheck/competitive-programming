class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        def next_popcnt(n):
            c = (n & -n)
            r = n + c;
            return (((r ^ n) >> 2) // c) | r

        colset = {}
        res = 0
        for i in range(len(mat)): colset[i] = 0
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]:
                    colset[row] |= (1<<(len(mat[0])-1-col))

        mask = (1<<cols)-1
        for i in range(math.comb(len(mat[0]), cols)):
            temp = 0
            for k in range(len(mat)):
                if (colset[k] & mask) == colset[k]: temp += 1
            mask = next_popcnt(mask)
            res = max(temp, res)
        
        return res