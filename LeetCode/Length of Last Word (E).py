class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ch = s.split(" ")
        
        for _ in range (len(ch)-1, -1, -1):
            if ch[_] != "" and ch[_] != " ":
                return len(ch[_])
            else:
                continue
        return 0
