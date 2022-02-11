class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(x, y):
            if x == y: return 0
            return 1 if x+y > y+x else -1
        
        nums = [ str(x) for x in nums ]
            
        nums.sort(key=cmp_to_key(comparator), reverse=True)
        
        temp = ''.join([x for x in nums])
        temp = temp.lstrip('0')
            
        return temp if temp else '0'