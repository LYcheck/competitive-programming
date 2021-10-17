class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split(' ')
        
        curr = -1
        
        for _ in tokens:
            if _.isnumeric():
                if int(_) > curr:
                    curr = int(_)
                else:
                    return 0
                
        return 1