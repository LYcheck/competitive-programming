# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        havemap = {}
        q = [(root, 0, 0)]
        res = []

        while q:
            cur, curx, cury = q[0][0], q[0][1], q[0][2]
            q.pop(0)
            
            if curx in havemap: 
                if havemap[curx][0] > cury:
                    
                    havemap[curx] = (cury, cur.val)
            else: havemap[curx] = (cury, cur.val)
                
            if cur.left: q += [(cur.left, curx-1, cury+1)]
            if cur.right: q += [(cur.right, curx+1, cury+1)]

        for x in sorted(havemap.keys()):
            res += [havemap[x][1]]
        return res