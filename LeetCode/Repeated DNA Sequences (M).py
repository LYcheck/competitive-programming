class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []
        intarr = [0]*len(s)
        mapping = {
            'A':0,
            'C':1,
            'G':2,
            'T':3
        }
        for i, _ in enumerate(s):
            intarr[i] = mapping[_]
        
        ptr = 0
        bitset = 0
        while ptr < 10:
            bitset <<= 2
            bitset |= intarr[ptr]
            ptr += 1
            
        seen = {bitset}
        res = set()
                
        while ptr < len(s):
            bitset <<= 2
            bitset |= intarr[ptr]
            bitset &= ~(3 << 20)
            
            if bitset in seen: res.add(s[ptr-9:ptr+1])
            else: seen.add(bitset)
            ptr += 1
        
        return res