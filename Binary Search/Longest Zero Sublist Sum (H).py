class Solution:
    def solve(self, ip):
        n = len(ip)
        def check(s):
            for i in range(len(s)-1, -1, -1):
                if s[i] == '.': 
                    return 0 <= int(s[i+1:len(s)]) < 256
            return 0 <= int(s) < 256

        def bt(res, temp, i, cnt):
            if i == n and cnt == 3 and check(temp):
                res += [temp]
                return
            elif i == n or cnt > 3: return

            if not temp or temp[-1] == '.':
                if ip[i] != '0':
                    bt(res, temp+ip[i], i+1, cnt)
                else:
                    bt(res, temp, i+1, cnt)
            else:
                bt(res, temp+ip[i], i+1, cnt)
                if check(temp): bt(res, temp+'.', i, cnt+1)

        res = []
        bt(res, "", 0, 0)
        return res