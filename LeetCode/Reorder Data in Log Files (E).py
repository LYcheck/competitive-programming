class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]: #mine, faster
        let, dig = [], []
        
        for log in logs:
            log = log.split(' ')
            if log[1].isalpha(): let += [log]
            else: dig += [log]
         
        
        def keySort(log1, log2):
            for i in range(1, min(len(log1), len(log2))):
                if log1[i] > log2[i]: return 1
                elif log2[i] > log1[i]: return -1
            
            if len(log1) == len(log2): return 1 if log1[0] > log2[0] else -1
            return 1 if len(log1) > len(log2) else -1
                
            
        let.sort(key=cmp_to_key(keySort))
        
        return [ ' '.join(log) for log in let + dig ]

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]: #cleaner
        let, dig = [], []
        
        for log in logs:
            log = log.split()
            if log[1].isdigit(): dig += [log]
            else: let += [log]
        
            
        let.sort(key=lambda log: (log[1:], log[0]))
        
        return [ ' '.join(log) for log in let + dig ]