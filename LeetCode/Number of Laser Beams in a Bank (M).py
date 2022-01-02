class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if not bank:
            return 0
        
        ctr = 0
        last = bank[0].count('1')
        for row in range(1, len(bank)):
            cnt = bank[row].count('1')
            ctr += last * cnt
            if cnt != 0:
                last = cnt
                
        return ctr