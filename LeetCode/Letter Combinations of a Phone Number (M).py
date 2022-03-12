class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = { 0:"", 1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz" }
        n = len(digits)
        res = []
        if not digits: return []
        
        def backtrack(temp, idx):
            if idx == n:
                nonlocal res
                res += [temp]
                return
            
            num = int(digits[idx])
            for char in letters[num]:
                backtrack(temp+char, idx+1)
                
        backtrack('', 0)
        
        return res