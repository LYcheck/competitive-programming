class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 0:
            if num & 1:
                cnt += 1
                num -= 1
            else:
                cnt += 1
                num >>= 1
        return cnt
