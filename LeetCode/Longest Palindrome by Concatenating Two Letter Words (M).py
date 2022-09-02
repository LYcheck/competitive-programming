class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        distincts, sames = {}, {}
        res = 0
        
        for _ in words:
            if _[0] == _[1]:
                if _ in sames: sames[_] += 1
                else: sames[_] = 1
            else:
                if _ in distincts: distincts[_] += 1
                else: distincts[_] = 1
                    
        for k in distincts.keys():
            rev = k[::-1]
            if rev in distincts:
                res += min(distincts[k], distincts[rev])*4
                distincts[k] = 0
                distincts[rev] = 0
        flag = 0
        
        for k in sames.keys():
            if not flag and sames[k] & 1:
                res += 2
                flag = 1
            res += (sames[k]//2)*4
                
        return res