class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        for i in range(ord(s[3])-ord(s[0])+1):
            letter = chr(ord(s[0])+i)
            for i in range(min(int(s[1]), int(s[4])), max(int(s[1]), int(s[4]))+1):
                res += [letter+str(i)]
                
        return res